#!/usr/bin/env python3
"""Free checks for the paid eval suite in ``evals/``.

``claude plugin eval`` has no dry run: a malformed case only shows up once a
paid run starts. This catches the mistakes that need no model:

1. every committed ``history.jsonl`` and campaign brief matches what
   ``evals/make_histories.py`` generates, so the CV and the scripted turns
   exist in one place;
2. every history is a transcript ``claude --resume`` can rebuild: one JSON
   object per line, unique ids, a ``parentUuid`` chain that starts at null,
   turns alternating from the applicant and ending on the assistant;
3. the phase 1 prompt carries the fixture CV verbatim, and the phase 2
   rewrite prompt is the answer turn the render history continues from;
4. the phase 3 brief holds the approved master CV and every numbered section
   of the brief template;
5. every ``case.yaml`` names its own directory, uses schema 1.1 and only
   grader types the runner knows, and the files it names exist.

Standard library only (no YAML parser), so the case checks read lines.

Run:  python3 tests/test_evals.py      (or: pytest tests/)
"""

from __future__ import annotations

import importlib.util
import json
import pathlib
import re
import sys
import traceback

ROOT = pathlib.Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"
# The types the runner's grader loader accepts, as its own error message lists
# them in Claude Code 2.1.302. Update when the runner adds one.
GRADER_TYPES = {"regex", "tool_order", "tool_used", "file_exists", "llm", "baseline"}


def _builder():
    spec = importlib.util.spec_from_file_location("make_histories", EVALS / "make_histories.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _cases():
    return sorted(p.parent for p in EVALS.glob("*/case.yaml"))


def test_generated_files_are_up_to_date():
    builder = _builder()
    generated = {**builder.histories(), **builder.briefs()}
    stale = [
        str(path.relative_to(ROOT))
        for path, text in generated.items()
        if not path.exists() or path.read_text(encoding="utf-8") != text
    ]
    assert not stale, "run python3 evals/make_histories.py: stale %s" % stale


def test_histories_are_resumable_transcripts():
    for path in _builder().histories():
        lines = path.read_text(encoding="utf-8").splitlines()
        records = [json.loads(line) for line in lines]
        assert records, "%s is empty" % path.name
        assert records[0]["parentUuid"] is None, path
        ids = [r["uuid"] for r in records]
        assert len(set(ids)) == len(ids), "%s repeats a uuid" % path
        for previous, current in zip(records, records[1:]):
            assert current["parentUuid"] == previous["uuid"], path
        roles = [r["type"] for r in records]
        assert roles[0] == "user" and roles[-1] == "assistant", (path, roles)
        assert all(a != b for a, b in zip(roles, roles[1:])), (path, roles)
        for r in records:
            assert r["message"]["role"] == r["type"], path
            assert {"sessionId", "timestamp"} <= r.keys(), path


def _prompt(case_name):
    """The ``execution.prompt`` block scalar of a case, dedented."""
    lines = (EVALS / case_name / "case.yaml").read_text(encoding="utf-8").splitlines()
    start = lines.index("  prompt: |") + 1
    block = []
    for line in lines[start:]:
        if line.strip() and not line.startswith("    "):
            break
        block.append(line[4:])
    return "\n".join(block).strip() + "\n"


def test_phase1_prompt_carries_the_fixture_cv():
    assert _builder().cv_text() in _prompt("phase1-audit-es"), \
        "phase1 prompt drifted from evals/fixtures/cv-sparse-en.md"


def test_rewrite_prompt_is_the_answer_turn():
    assert _prompt("phase2-rewrite-es") == _builder().ANSWERS + "\n"


def test_phase3_briefs_hold_the_master_cv_and_the_template_sections():
    builder = _builder()
    briefs = builder.briefs()
    assert {p.parent.name for p in briefs} == {"phase3-chat-es", "phase3-paste-es"}
    template = (ROOT / "skills" / "fix-cv-find-job-skill" / "assets" /
                "campaign-brief-template.md").read_text(encoding="utf-8")
    headings = re.findall(r"^## \d+b?\. .+$", template, re.M)
    for path, brief in briefs.items():
        assert "````\n" + builder.master_cv() + "````" in brief, \
            "%s: the master CV is not the one phase 2 approved" % path.parent.name
        missing = [h for h in headings if h not in brief.splitlines()]
        assert not missing, "%s lacks template sections %s" % (path.parent.name, missing)


def test_cases_are_well_formed():
    cases = _cases()
    assert cases, "no eval cases found"
    for case_dir in cases:
        text = (case_dir / "case.yaml").read_text(encoding="utf-8")
        assert re.search(r'^schema_version: "1\.1"$', text, re.M), case_dir.name
        assert re.search(r"^name: %s$" % re.escape(case_dir.name), text, re.M), case_dir.name
        types = re.findall(r"^  - type: (\S+)$", text, re.M)
        assert types, "%s has no graders" % case_dir.name
        unknown = set(types) - GRADER_TYPES
        assert not unknown, "%s: unknown grader types %s" % (case_dir.name, unknown)
        names = re.findall(r"^    name: (\S+)$", text, re.M)
        assert len(names) == len(types), "%s: every grader needs one name" % case_dir.name
        assert len(set(names)) == len(names), "%s repeats a grader name" % case_dir.name
        for key in ("history_file", "scaffold_script"):
            named = re.search(r"^  %s: (\S+)$" % key, text, re.M)
            if named:
                assert (case_dir / named.group(1)).is_file(), (case_dir.name, key)
        # The runner compiles these as JavaScript RegExps; the patterns here
        # stay inside the syntax Python's re shares with it.
        for quoted in re.findall(r"^\s+(?:pattern|input_match): '((?:[^']|'')*)'$", text, re.M):
            re.compile(quoted.replace("''", "'"))


# --------------------------------------------------------------------------- #
# runner (no pytest required)
# --------------------------------------------------------------------------- #

def _main() -> int:
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
        except Exception:
            failed += 1
            print("FAIL  %s" % name)
            traceback.print_exc()
        else:
            print("ok    %s" % name)
    print("\n%d test(s), %d failed" % (len(tests), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(_main())
