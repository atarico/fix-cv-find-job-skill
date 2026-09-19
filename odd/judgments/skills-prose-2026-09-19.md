# Judgment Day — skills/fix-cv-find-job-skill prose corpus

```yaml
target_identity: 062a763b0fdee85c4f004f48c97377741c1dd0e858a4965a7388c910ea261f6e
frozen_at: dd6cdbf
scope: 10 files, 1542 lines
round: 1
scoped_rejudgment: not_run
terminal_state: pending_user_decision
skill_resolution: none — this repository has no .claude/ skill registry
```

Scope: `SKILL.md`, `references/01`–`06`, `assets/campaign-brief-template.md`,
`README.md`, `README.es.md`. Two blind judges, identical scope and criteria.

## Confirmed — both judges, both CRITICAL

**JD-1 · `SKILL.md:71-80` — a restored campaign brief still runs the full CV audit.**

Entry says to restore state from the attached brief "before doing anything
else", then unconditionally routes to `references/01-cv-audit.md`. There is no
branch on what the brief says was already done. A returning user is sent back
through the phase they finished last session.

Three places promise the opposite:

- `references/06-inbox-triage.md:115` — "Attach it next time and I will pick up
  exactly where we left off."
- `assets/campaign-brief-template.md:3-4` — "A new session with no memory of
  previous ones can pick up the campaign from this file alone."
- `README.md` — "It restores your profile, your targets, everything you have
  applied to, and everything still blocked."

Independently verified by the orchestrator against the source.

## Confirmed — both judges, severity disputed

**JD-2 · `SKILL.md:20-22` — artifact language keys off a posting that does not exist yet.**
Judge A: CRITICAL. Judge B: WARNING.

Prime directive 1 says every artifact "follows the language of the target job
posting instead, not the conversation". The master CV is produced in phase 2,
before job search happens in phase 3, so no target posting exists. Phase 3, 4
and 6 reports aggregate many postings that may be in different languages.
Judge A also notes `README.md` states "It replies in whatever language you write
in", which points the other way.

## Suspect — one judge only, not auto-fixed

| ID | Location | Sev | Judge | Claim |
|---|---|---|---|---|
| JD-3 | `references/02-master-cv.md:55,79-82,124` | CRITICAL | A | A hard two-page cap, machine-gated by `pdfinfo … must be 2 or fewer`, against "whatever the field demands — publications, clinical rotations". Academic, research and government CVs routinely exceed two pages; the gate contradicts the "any industry" headline for exactly the fields that need length. **Orchestrator verified the contradiction exists.** |
| JD-4 | `references/03-job-search.md:16,31-36` | CRITICAL | A | The forced-numeric salary rule says to use "the number for the seniority in the posting — a junior posting gets the junior number", but collection gathers only one target, one floor and a currency. No per-seniority figure exists to draw from, on a field that goes into a real submitted application. **Orchestrator verified the collected fields.** |
| JD-5 | `references/06-inbox-triage.md:1-9,61-63,112` | WARNING | A | The standalone "check my email" entry bypasses Entry, yet instructs scoring with phase 3 criteria and updating the campaign brief — neither of which exists on that path. |
| JD-6 | `references/04-auto-apply.md:63-64,87-88` | WARNING | B | Instructs recording a match score per application, but the final report table has no Match column, while the campaign brief table does. |
| JD-7 | `README.es.md:31-54` | WARNING | A+B | The Spanish README's phase-1 sample block is left verbatim in English. *(Both judges raised it; WARNING, so informational under the protocol.)* |
| JD-8 | `references/06-inbox-triage.md:110-118` | SUGGESTION | B | Phase 6's closing question does not route to `04-auto-apply.md`, unlike phase 3's close which names its next file. |
| JD-9 | `SKILL.md:5` | SUGGESTION | B | The `compatibility` frontmatter lists job search, auto-apply and inbox as needing a browser, omitting phase 5 (LinkedIn), which the phase table marks as needing one. |

## Contradictions

None on existence. One severity split, recorded as JD-2.

## Notes

- Criterion 4 (safety, personal data, fabricated credentials) came back clean
  from both judges. Neither found an instruction that could fabricate experience
  or move data out of the user's control undisclosed.
- Criterion 5 (industry-agnosticism) was reported clean by Judge B after a
  vocabulary sweep; Judge A reached it through JD-3 instead, which is the
  sharper reading.
- A judgment issues no receipt and carries no delivery authority.

---

# Round two — terminal

```yaml
round: 2
corrected_target: f598fc0baef1e522182c906114a33cc680cce8f46ea5350218181453c14028f6
confirmed: []
suspect: [RJ-6, RJ-7]
contradictions: []
fix_work_units: [round-1: JD-1..JD-4 plus JD-6, JD-8, JD-9; round-2: RJ-1..RJ-5]
scoped_rejudgment: escalated
terminal_state: escalated
skill_resolution: none
```

## What the two rounds fixed

Round one implemented the user's rulings on JD-1 through JD-4 and folded in the
three smaller ledger items. Round one then introduced five defects of its own,
which round two repaired: the three-way standalone-entry contradiction, the
per-language master CVs overwriting each other, the standing limits that never
reached the file governing submission, the portfolio step written as universal,
and an Entry clause reading a brief field that did not exist.

## Why this escalates rather than approving

Two defects survive the final round. Neither is confirmed by both judges, so
neither qualifies for correction under this protocol, and there is no round
three. Both were independently verified by the orchestrator against the source.

**RJ-6 · `references/06-inbox-triage.md:12-15` — CRITICAL, Judge B.**
Entry accepts "a standalone request with neither" a CV nor a brief. The degraded
fallback for that path instructs scoring new openings "on fit to the CV alone".
With no CV there is nothing to score against, and no branch anywhere handles
that sub-case. Verified: grep for a no-CV branch in that file returns nothing.

Judge B's pass carried two errors of its own, recorded for whoever reads this:
it could not run the requested diff and reconstructed the delta by reading whole
files instead, and it reported that `README.md` and `README.es.md` do not exist
at the repository root, which is false. The finding was verified independently
rather than taken on the judge's word.

**RJ-7 · `references/02-master-cv.md:171-174` — WARNING, Judge A.**
The naming rule permits dropping the `_<Language>` suffix "when the applicant
works in a single language", but the produce-and-verify commands emit and check
`_<Language>` unconditionally. A monolingual applicant following the carve-out
writes `CV_<Name>_Master.pdf` while the two-page gate checks
`CV_<Name>_Master_<Language>.pdf` — the same gate/filename mismatch RJ-2 was
chartered to remove.

Both are the same shape: a documented exception the surrounding mechanics do not
honour.

## Standing

A judgment issues no receipt and carries no delivery authority. `escalated` does
not block anything; it records that two verified defects remain and that this
protocol has no move left. Fixing them is ordinary work under ordinary
repository policy, at the user's direction.

---

## Both escalated items resolved as ordinary work

Outside the protocol, at the user's direction. The verdict stands as recorded —
a later fix does not retroactively approve a judgment.

**RJ-6** — the degraded fallback now branches on what is actually in hand. With
a CV it scores on fit and marks every score provisional. With neither a CV nor
a brief it scores nothing and lists the openings plainly unranked, saying why;
classification still works, because replies, new openings and acknowledgements
sort on their own evidence. The scoring step twelve lines below now defers to
that branch instead of restating half of it.

**RJ-7** — the carve-out is gone rather than honoured. The suffix is never
dropped, and the text says why: four commands emit it unconditionally and the
gate checks for it, so an exception leaves the gate looking for a file nobody
wrote. Both surviving defects were the same shape — a documented exception the
surrounding mechanics did not honour — so the durable fix was to delete the
exception, not to teach the mechanics about it.
