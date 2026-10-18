#!/usr/bin/env python3
"""Cross-file consistency guard for the skill's Markdown.

The skill is instructions spread over ``SKILL.md``, ``references/*.md`` and
``assets/campaign-brief-template.md``. Nothing else checks that they still
agree after an edit, so this does, for three kinds of pointer:

1. every ``references/<file>.md`` and ``assets/<file>`` path mentioned exists
   in the skill folder;
2. every ``scripts/<file>`` path mentioned exists at the repository root
   (those files live in the repo, not in the shipped skill folder);
3. every brief section cited by number as ``section <n>`` or ``§<n>``
   (``brief section 5``, ``Section 3``, ``§9b``) resolves to a ``## <n>.``
   heading in ``assets/campaign-brief-template.md``.

Deliberately not checked, because the pattern would need guesswork: sections
named by title only, plural forms ("sections 3 and 4"), and bare "step 3" /
"phase 3" prose.

Standard library only. To run against another tree (the tests do this to
prove the guard fails on a broken copy) set ``SKILL_CONSISTENCY_ROOT`` to a
directory laid out like the repository root.

Run:  python3 tests/test_skill_consistency.py      (or: pytest tests/)
"""

from __future__ import annotations

import os
import pathlib
import re
import sys
import traceback

ROOT = pathlib.Path(
    os.environ.get("SKILL_CONSISTENCY_ROOT") or pathlib.Path(__file__).resolve().parent.parent
)
SKILL_DIR = ROOT / "skills" / "fix-cv-find-job-skill"
BRIEF = SKILL_DIR / "assets" / "campaign-brief-template.md"

SKILL_PATH_RE = re.compile(r"\b((?:references|assets)/[A-Za-z0-9._/-]*[A-Za-z0-9_])")
SCRIPT_PATH_RE = re.compile(r"\b(scripts/[A-Za-z0-9._/-]*[A-Za-z0-9_])")
SECTION_REF_RE = re.compile(r"(?:\bsection\s+|§\s*)(\d+[a-z]?)\b", re.IGNORECASE)
HEADING_RE = re.compile(r"^## (\d+[a-z]?)\.", re.MULTILINE)


def skill_files() -> list[pathlib.Path]:
    files = [SKILL_DIR / "SKILL.md"]
    files += sorted((SKILL_DIR / "references").glob("*.md"))
    files.append(BRIEF)
    return files


def _lines(path: pathlib.Path):
    rel = path.relative_to(ROOT)
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        yield rel, n, line


def find_missing_skill_paths(files: list[pathlib.Path]) -> list[str]:
    bad = []
    for path in files:
        for rel, n, line in _lines(path):
            for m in SKILL_PATH_RE.finditer(line):
                if not (SKILL_DIR / m.group(1)).exists():
                    bad.append("%s:%d: %s does not exist in the skill folder" % (rel, n, m.group(1)))
    return bad


def find_missing_scripts(files: list[pathlib.Path]) -> list[str]:
    bad = []
    for path in files:
        for rel, n, line in _lines(path):
            for m in SCRIPT_PATH_RE.finditer(line):
                if not (ROOT / m.group(1)).exists():
                    bad.append("%s:%d: %s does not exist at the repository root" % (rel, n, m.group(1)))
    return bad


def find_dangling_sections(files: list[pathlib.Path], brief_text: str) -> list[str]:
    headings = set(HEADING_RE.findall(brief_text))
    bad = []
    for path in files:
        for rel, n, line in _lines(path):
            for m in SECTION_REF_RE.finditer(line):
                if m.group(1).lower() not in headings:
                    bad.append(
                        "%s:%d: brief section %s has no '## %s.' heading in the template"
                        % (rel, n, m.group(1), m.group(1))
                    )
    return bad


def test_brief_has_numbered_section_headings():
    headings = HEADING_RE.findall(BRIEF.read_text(encoding="utf-8"))
    assert len(headings) >= 10, "expected the brief's numbered '## <n>.' headings, found %r" % headings


def test_skill_paths_exist():
    bad = find_missing_skill_paths(skill_files())
    assert not bad, "\n" + "\n".join(bad)


def test_script_paths_exist():
    bad = find_missing_scripts(skill_files())
    assert not bad, "\n" + "\n".join(bad)


def test_brief_section_references_resolve():
    bad = find_dangling_sections(skill_files(), BRIEF.read_text(encoding="utf-8"))
    assert not bad, "\n" + "\n".join(bad)


def test_patterns_catch_what_they_claim():
    assert SECTION_REF_RE.findall("brief section 5, Section 3 and §9b; see section 12.") == [
        "5", "3", "9b", "12",
    ]
    assert SECTION_REF_RE.findall("the language section above") == []
    assert SKILL_PATH_RE.findall("see `references/07-sweep-mechanics.md`.") == [
        "references/07-sweep-mechanics.md"
    ]
    assert SCRIPT_PATH_RE.findall("`scripts/make-reference-docx.py` is") == [
        "scripts/make-reference-docx.py"
    ]


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
