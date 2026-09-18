#!/usr/bin/env bash
# Builds the upload-ready zip for claude.ai > Settings > Skills > Upload skill.
#
# The archive must contain a single top-level directory whose name matches the
# `name` field in SKILL.md, so we zip the skill folder from inside skills/.
set -euo pipefail

SKILL_NAME="fix-cv-find-job-skill"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/skills/$SKILL_NAME"
OUT="$ROOT/dist/$SKILL_NAME.zip"

[ -f "$SRC/SKILL.md" ] || { echo "error: $SRC/SKILL.md not found" >&2; exit 1; }

command -v zip >/dev/null 2>&1 || { echo "error: zip is not installed" >&2; exit 1; }

mkdir -p "$ROOT/dist"
rm -f "$OUT"

# -x excludes editor cruft that would otherwise trip the security scan.
( cd "$ROOT/skills" && zip -q -r "$OUT" "$SKILL_NAME" \
    -x '*.DS_Store' '*/.git/*' '*.swp' '*~' )

echo "built: $OUT"
unzip -l "$OUT"
