# Releasing

Every release ships the same way and is announced with the same notes, so a
reader of any release page knows where to find what changed, how to upgrade,
and what was verified.

## Checklist

1. Merge the release's pull requests into `main` and pull it locally.
2. Bump the version in every place it is declared — five files:
   `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` (twice),
   `skills/fix-cv-find-job-skill/SKILL.md` (`metadata.version`), and the badge
   in `README.md` and `README.es.md`.
   `rg -n --hidden -g '!.git' '<old version>'` must return nothing afterwards.
3. Run the suites: `python3 tests/test_skill_spec.py`,
   `python3 tests/test_skill_consistency.py`, `python3 tests/test_evals.py` and
   `python3 tests/test_reference_docx.py`. When the release changes phases 1
   to 3, also run the paid eval suite (`evals/README.md`) and record its result in
   the notes.
4. Commit `chore: release <version>` on `main` and push.
5. Tag it: `git tag -a v<version> -m "v<version> - <title>"`, then push the tag.
6. Build the zip: `./scripts/package.sh`. Open it and check the version.
7. Publish: `gh release create v<version> dist/fix-cv-find-job-skill.zip
   --verify-tag --latest --title "v<version> — <title>" --notes-file <notes>`,
   with notes written from the template below.

Versioning: a release with a new capability bumps the minor version; a release
with fixes only bumps the patch.

## Notes template

Write the notes in English. Replace every `<…>`; delete a section only where
the template says it may go.

````markdown
fix-cv-find-job-skill v<version> is a <minor|patch> release. <One paragraph:
what changed for the applicant, in their terms, and why it matters.>

## Provenance

- **Previous stable:** `v<previous>` → `<full sha>`
- **Release target:** `v<version>` → `<full sha>`
- **CI:** [run <id>](<url of the test workflow run on the release commit>)
- **Verification:** <the suites that passed, and the native review outcome
  with its lineage, or "no native review was due">

## What's new

### <Capability, as a sentence>

<What it does and where it applies. Plain words; no internal jargon.>

Included work: [#<pr>](https://github.com/atarico/fix-cv-find-job-skill/pull/<pr>)

## Breaking changes

<"No breaking changes." or what an existing applicant or installer must do
differently. Behaviour that changed on a surface counts.>

## Upgrade now

Claude Code:

```bash
claude plugin marketplace update fix-cv-find-job
claude plugin update fix-cv-find-job-skill@fix-cv-find-job
```

Restart Claude Code to apply. An uploaded skill (claude.ai or ChatGPT): upload
the new `fix-cv-find-job-skill.zip` from this release. A clone or copied folder
(Claude Code, Codex, OpenCode): `git pull`, or replace the folder.

## What was fixed

<Delete this section when nothing was fixed.>

### <The fix, as a sentence>

<What went wrong before and what happens now.>

Included work: [#<pr>](https://github.com/atarico/fix-cv-find-job-skill/pull/<pr>)

## Numbers

<n> non-merge commits, <n> merged pull requests, and <n> unique authors since
v<previous>.

## Install

See [Install](https://github.com/atarico/fix-cv-find-job-skill#install): the
Claude plugin, the zip upload, or the skill folder for ChatGPT, Codex and
OpenCode (phases 1 and 2, and phase 3 in chat mode).

**Full changelog**: https://github.com/atarico/fix-cv-find-job-skill/compare/v<previous>...v<version>
````

Count the numbers with:

```bash
git rev-list --no-merges --count v<previous>..v<version>
git log --merges --oneline v<previous>..v<version> | rg -c 'Merge pull request'
git log --no-merges --format='%ae' v<previous>..v<version> | sort -u | wc -l
```
