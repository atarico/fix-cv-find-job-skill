# Skill rules — bring them to working-model detail

## Objective

Raise `skills/fix-cv-find-job-skill/` from "get the number they want, the floor
and the currency" to the resolution the user already works at by hand: a salary
table by market and seniority, named headline variants in both languages, hard
disqualifiers carried with textual evidence, and per-platform duplicate checks.

Closes judgment-day round one for target `062a763b…`
(`odd/judgments/skills-prose-2026-09-19.md`).

## Branch

`feat/skill-rules`, cut from `main`. It was originally stacked on
`feat/landing-page`, which is on hold until the demo clips exist. The skill-rule
work is finished and independently review-approved, so it was unstacked to ship
on its own: the README edits here are behaviour claims, and they applied to
`main`'s READMEs without a conflict, which confirms they never depended on that
branch's restyle.

## The four findings and the user's rulings

**JD-1 — phases 1 and 2 run once, not every session.** User's specification,
verbatim in intent:

- First session: CV is loaded, phases 1 and 2 run, then the rest.
- While no new CV is supplied, phases 1 and 2 never run again.
- A new CV triggers a question — "do you want the audit and rewrite run on
  this CV?" Yes routes to phase 1. No routes straight to the browser phases.
- Next session, "check my email" or "find me openings" starts there. No redo.

**JD-2 — the master CV holds every language, the tailored CV picks one.** The
master is built in phase 2, before any posting exists, so it cannot follow "the
language of the target posting". It carries named variants in each language the
user works in. The posting's language is applied when tailoring, in phase 4.

**JD-3 — the two-page cap stays. The scope note is what was missing.** The user
is explicit: this serves people hiring through platforms, the ordinary
applicant. Academic, research and government CVs follow other conventions and
do not pass through those platforms. Keep the cap and the `pdfinfo` gate; state
the scope where the rule lives so the constraint reads as deliberate rather
than as an oversight. Do not touch the "any industry" headline — the vast
majority of professions hiring through platforms fit two pages.

**JD-4 — salary is never invented.** The user's specification:

- The applicant states what they want to earn.
- If they do not know, search for a market range, present it, and use it only
  once they accept it.
- When a posting publishes a range, the applicant decides in advance whether to
  take the bottom, the middle or the top.
- The seniority stated in the posting governs, not the applicant's own.

## Enrichment carried over from the user's working models

The user supplied two real campaign briefs as the reference for how rules
should read. Carry the **shape**, never the instance:

- Salary as a table across markets and seniority levels, not one figure.
- Free-text salary field takes "negotiable" first; only a validator rejection
  forces the number. Currency conversion mandatory for numeric fields.
- Named headline variants per specialisation, held in every working language.
- A fixed number of portfolio items per application, chosen against the posting.
- Hard disqualifiers recorded with the posting's own wording as evidence.
- Never apply below the applicant's own seniority.
- Duplicate checks with the exact verification path per platform.
- Anything only the human can supply — photo, ID, CAPTCHA, a local file —
  leaves that tab open and the run continues down the list.
- A non-negotiable limits section.
- The campaign brief carries all of it so a fresh session operates from it alone.

## Hard constraints

- **Person-agnostic.** The models contain one real person's name, ID number,
  phone, salary figures and target companies. None of it may enter the skill.
  Encode the structure; the brief template holds placeholders.
- **Industry-agnostic.** The models are a software developer's. Every rule must
  generalise — "headline variants by specialisation", never "backend/frontend".
  A nurse, an accountant and an electrician must all read it as written for them.
- **Language-agnostic.** The models use Spanish and English. The rules describe
  "each language the applicant works in", not those two.
- The existing limits stay exactly as strong: no accounts, no passwords, no
  CAPTCHAs, no invented data, no unattended sending.
- Artifacts stay in English. Only user-facing README copy is bilingual.

## Tasks

- [x] **T1** — `SKILL.md`: Entry branches on restored state; prime directive 1 split
- [x] **T2** — `references/02-master-cv.md`: named variants, per-language masters, two-page scope note
- [x] **T3** — `references/03-job-search.md`: salary table/range collection, seniority rule, hard disqualifiers
- [x] **T4** — `references/04-auto-apply.md`: salary application, duplicate checks, blocked handling, Match column
- [x] **T5** — `references/06-inbox-triage.md`: standalone entry prerequisites, routing to phase 4
- [x] **T6** — `assets/campaign-brief-template.md`: carry every field the phases restore
- [x] **T7** — `README.md` / `README.es.md`: reflect the changed behaviour
- [x] **T8** — Scoped re-judgment over the frozen ledger plus this delta

## Checks

- [ ] No personal data, company name or currency figure from the models appears
- [ ] No instruction assumes a software or office occupation
- [ ] Every README claim still traces to an instruction
- [ ] Anchors in both READMEs still resolve
- [ ] The limits list is unchanged in strength

## Native review

`gentle-ai review assess` rated the branch **medium**, naming one path:
`odd/judgments/skills-prose-2026-09-19.md`, flagged `executable_change`. That
file is the judgment ledger — a markdown record whose fenced blocks quote
`pandoc` and `pdfinfo` as evidence for the findings. The heuristic reads a
command and does not distinguish quoting one from running one. The tier was
not argued with.

The user granted consent. Medium selected one consolidated lens rather than
four: `review-reliability` returned **approved** with no findings, and the exact
acknowledgement burned the authority.

```yaml
lineage: review-41f73765a132db23
target: sha256:68be24d646a5019c84110dad839ad37b19b34cbfaf3ad080e389bf38cc7a5c1f
lens: review-reliability
result: approved
authority: burned
```

A review outcome is informational and authorizes no delivery. Commit, push, PR
and merge stay ordinary repository decisions.

## Progress

- All eight tasks done.
- Judgment day: two fix rounds, verdict `escalated`, both surviving defects then
  closed as ordinary work in `89312e9`.
- Native review: approved and acknowledged on the five-commit candidate.
- Remaining, and only the repository owner can do it: enable GitHub Pages with
  source "GitHub Actions", record the demo clips, publish them to a Release and
  paste their URLs into `landing/src/config/clips.ts`, then land both branches.
