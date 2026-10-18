#!/usr/bin/env python3
"""Spec-conformance guard for ``skills/fix-cv-find-job-skill/SKILL.md``.

The skill claims to run in any Agent Skills client, so its frontmatter must
stay inside the Agent Skills specification (agentskills.io):

* a frontmatter block delimited by ``---`` lines;
* ``name``: lowercase letters, digits and single hyphens, at most 64
  characters, equal to the folder name;
* ``description``: 1-1024 characters;
* ``compatibility``: at most 500 characters, when present;
* ``metadata``: a flat map of string values, when present;
* every ``references/...`` and ``assets/...`` path the body mentions exists.

Standard library only; the frontmatter is parsed line by line, which is enough
for this file (plain scalars and one flat map), so there is no PyYAML to
install in CI.

Run:  python3 tests/test_skill_spec.py      (or: pytest tests/)
"""

from __future__ import annotations

import pathlib
import re
import sys
import traceback

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "fix-cv-find-job-skill"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):[ \t]*(.*)$")
PATH_RE = re.compile(r"\b((?:references|assets)/[A-Za-z0-9._/-]*[A-Za-z0-9_])")


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def split_frontmatter(text: str) -> tuple[list[str], str]:
    lines = text.splitlines()
    assert lines and lines[0].strip() == "---", "SKILL.md must start with a --- frontmatter line"
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    raise AssertionError("frontmatter is not closed by a second --- line")


def parse_frontmatter(block: list[str]) -> dict:
    """Top-level ``key: value`` pairs; an empty value followed by indented
    ``k: v`` lines is a flat map; other indented lines (and ``>`` / ``|``
    block scalars) continue the previous scalar."""
    out: dict = {}
    key = None
    for raw in block:
        if not raw.strip():
            continue
        if raw[0] not in " \t":
            m = KEY_RE.match(raw)
            assert m, "unparseable frontmatter line: %r" % raw
            key, value = m.group(1), m.group(2)
            assert key not in out, "duplicate frontmatter key: %s" % key
            out[key] = "" if value.strip() in (">", "|", ">-", "|-") else (_unquote(value) if value.strip() else {})
            continue
        assert key is not None, "indented line before any key: %r" % raw
        current = out[key]
        if isinstance(current, dict):
            m = KEY_RE.match(raw.strip())
            assert m, "unparseable %s entry: %r" % (key, raw)
            current[m.group(1)] = _unquote(m.group(2))
        else:
            out[key] = (current + " " + raw.strip()).strip()
    return out


def check(skill_dir: pathlib.Path) -> list[str]:
    """Return every spec problem found for the skill in ``skill_dir``."""
    problems: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return ["%s does not exist" % skill_md]
    try:
        block, body = split_frontmatter(skill_md.read_text(encoding="utf-8"))
        fm = parse_frontmatter(block)
    except AssertionError as e:
        return [str(e)]

    name = fm.get("name")
    if not isinstance(name, str) or not name:
        problems.append("name is missing")
    else:
        if not NAME_RE.match(name):
            problems.append("name %r must match %s" % (name, NAME_RE.pattern))
        if len(name) > 64:
            problems.append("name is %d characters (max 64)" % len(name))
        if name != skill_dir.name:
            problems.append("name %r does not equal the folder name %r" % (name, skill_dir.name))

    desc = fm.get("description")
    if not isinstance(desc, str) or not 1 <= len(desc) <= 1024:
        problems.append("description must be 1-1024 characters, got %s" % (len(desc) if isinstance(desc, str) else desc))

    if "compatibility" in fm:
        comp = fm["compatibility"]
        if not isinstance(comp, str) or not 1 <= len(comp) <= 500:
            problems.append("compatibility must be 1-500 characters, got %s" % (len(comp) if isinstance(comp, str) else comp))

    if "metadata" in fm:
        meta = fm["metadata"]
        if not isinstance(meta, dict):
            problems.append("metadata must be a map")
        else:
            for k, v in meta.items():
                if not isinstance(v, str):
                    problems.append("metadata.%s must be a string" % k)

    for rel in sorted(set(PATH_RE.findall(body))):
        if not (skill_dir / rel).exists():
            problems.append("SKILL.md mentions %s, which does not exist in the skill folder" % rel)
    return problems


def test_skill_md_conforms_to_the_agent_skills_spec():
    problems = check(SKILL_DIR)
    assert not problems, "SKILL.md breaks the Agent Skills spec:\n  - " + "\n  - ".join(problems)


def test_parser_reads_folded_and_nested_values():
    fm = parse_frontmatter(["name: x", "description: >", "  one", "  two", "metadata:", "  a: 1", "  b: 'two'"])
    assert fm == {"name": "x", "description": "one two", "metadata": {"a": "1", "b": "two"}}, fm


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
