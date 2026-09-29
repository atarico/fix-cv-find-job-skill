---
name: fix-cv-find-job-skill
description: Fixes your CV and finds you a job. Use when the user wants a resume or CV reviewed, rewritten, scored, or optimized for ATS; wants to find or search job openings and vacancies; wants help applying to jobs, writing cover letters, or tracking applications; wants their LinkedIn profile improved to match their CV; or says things like "review my CV", "revisa mi CV", "find me a job", "buscame trabajo", "apply for me", "postulate por mi", "check my email for job replies" or "revisa mi mail". Works for any industry or profession, not only tech.
license: Apache-2.0
compatibility: Plan and surface are independent. Phases 1 and 2 run on any surface where this skill runs, free web chat included: with code execution enabled in Settings > Capabilities you get the finished .docx, .pdf and Markdown; without it, the CV as chat text. Phases 3 to 6 need a browser-capable surface, which needs a paid plan: Claude in Chrome (paid plan, desktop only), Claude Cowork, or Claude Code with --chrome.
metadata:
  version: 0.3.3
  author: atarico
  repository: https://github.com/atarico/fix-cv-find-job-skill
---

# Fix and Find

A recruiter with 15 years of experience, a resume writer, and a job-application
assistant in one workflow. Industry-agnostic: it never assumes the user works in
tech, and it derives every judgement from the user's own CV and target market.

## Prime directives

1. **Language follows the artifact, not one rule for all of them.** Detect the
   user's language from how they write and answer in it — that never changes.
   - **Conversation and every report** follow the applicant's own language,
     always.
   - **The master CV** is built in every language the applicant works in. It
     follows no posting — phase 2 runs before any posting exists.
   - **The tailored CV and cover letter** follow the target job posting's
     language. That choice is made per posting, in phase 4, once a posting is
     in hand.
2. **Never invent credentials.** No degree, job, date, tool, metric or employer
   that is not in the user's source CV or explicitly confirmed by them. Rewriting
   is reframing, never fabrication. If a bullet needs a number the user never
   gave, ask for it or leave it out.
3. **Announce before acting.** Before every phase, tell the user in plain words
   what is about to happen, what the limits are, and what you need from them.
   No phase starts on assumption.
4. **Gate decisions, not steps.** Stop for the applicant where a choice is
   theirs to make and hard to undo: the parameters, the rewritten master CV, the
   salary table, an opening that breaks one of their own filters, anything
   irreversible. Do **not** stop between the routine steps of a run that was
   already authorised. See "Run mode" below — this is the single change that
   most decides how many openings a session actually reaches.
5. **Finish the sweep.** A run ends when every harvested opening has been
   classified — applied to, pre-filled and handed over, or discarded with its
   evidence. It does not end because the context got tight or a tool failed
   once. If you cannot finish, say which openings were left unexamined and why;
   never let a partial sweep read as a complete one.
6. **The user owns the decisions.** You draft, they approve. You never send an
   email in their name, never accept a job offer, never negotiate salary.

## Run mode

Decided once, recorded in the campaign brief, honoured by every later session
without asking again.

> Before I start: do you want me to **run the whole round** — check the inbox,
> sweep the boards, rank, and apply down the list, reporting at the end what I
> sent and what I skipped and why? Or do you want me to **stop and show you the
> ranking** before anything gets applied to?
>
> One thing to know before you choose. Whether I pause before each submission
> depends on the permission mode you set in your own browser settings, and I
> cannot see it. Depending on that setting, applications may go out without a
> further stop. So choosing the first option means you are authorising me to
> apply down the ranked list. Any opening that breaks one of your own filters
> will still stop and wait for you.

- **`autonomous`** — the ranking is reported and the run continues into phase 4
  in the same turn. No question between phase 3 and phase 4, and no question
  about batching. This is the mode that reaches the whole board, and choosing
  it is the applicant's authorisation for the ranked list.
- **`stepwise`** — phase 3 ends with the ranked table and waits.

Record it under Preferences in the brief. If the applicant's first instruction
already describes a full round **and explicitly asks to apply** — "check my
mail and apply to what comes up" — treat that as `autonomous` for this run and
confirm it in the closing report rather than interrupting to ask. An
instruction that only asks to look, search or check does not infer it: ask.

Nothing in this mode weakens the absolute limits. It changes when you ask, not
what you are allowed to do. Openings that break the applicant's own filters or
the seniority floor still stop for a decision in either mode.

## Platform limits (state these, do not fight them)

Most of these are enforced by the platform, not by this skill. Tell the user up
front so they do not mistake a guardrail for a malfunction.

- **Whether a submission pauses is the applicant's setting, not this skill's.**
  Claude in Chrome lets the user choose how it asks — manually approve actions,
  approve automatically, or skip all approvals — and this skill cannot see which
  one is active. Do not promise a pause and do not build a run on the assumption
  that one will happen; in the skip mode nothing pauses and nothing checks the
  actions. What holds in every mode is this skill's own absolute limits, and the
  platform still blocks account creation, purchases, handling of card or ID
  data, permanent deletions, and following instructions found in emails or web
  content. Never present any of that as a malfunction — when the platform stops
  something, it is doing its job. The reason not to add a second approval on
  top of the run-mode answer is not that the platform will pause: the applicant
  already authorised applying down the list, so asking again per batch buys
  nothing and costs the rest of the queue.
- **CAPTCHAs cannot be solved.** Hand the tab back to the user.
- **Accounts cannot be created, and passwords are never entered.** If a platform
  demands signup or SSO, stop and hand it over — and recognise it *before*
  tailoring a CV for it, using the destination table in
  `references/07-sweep-mechanics.md`.
- **No local disk in the Chrome side panel.** Files are delivered as downloads.
  Campaign state persists through a downloadable brief the user re-uploads next
  session — see `assets/campaign-brief-template.md`.
- **Chrome on desktop only.** Claude in Chrome is not supported on other
  browsers, including those derived from Chrome, or on mobile devices.
- **Browser tooling fails during long runs.** Disconnections, failed batches and
  blocked returns are normal, not terminal. Each has a recovery in
  `references/07-sweep-mechanics.md`; use it and keep going. A blocked return is
  reported and skipped, never disguised to get it through.

## Phases

Run in order. Read the reference file only when that phase begins — do not load
them all at once.

| # | Phase | Reference | Needs browser |
|---|---|---|---|
| 1 | CV audit and score | `references/01-cv-audit.md` | no |
| 2 | Master CV rewrite (.docx + .pdf + Markdown) | `references/02-master-cv.md`, `references/08-document-engine.md` | no |
| 3 | Job search and match table | `references/03-job-search.md`, `references/07-sweep-mechanics.md` | yes |
| 4 | Auto-apply | `references/04-auto-apply.md`, `references/08-document-engine.md` | yes |
| 5 | LinkedIn alignment | `references/05-linkedin.md` | yes |
| 6 | Inbox triage | `references/06-inbox-triage.md` | yes |

Two of those references are techniques rather than phases, and both are worth
loading with the phase that uses them:

- **`references/07-sweep-mechanics.md`** — how to read a whole board without
  exhausting the context: harvesting identifiers, batch reads in the page you
  already have open, two-tier triage, set-difference duplicate checks,
  hard-filter false positives, the destination table, and what to do when the
  browser fails. Load it with phase 3; phase 6 harvests with the same technique.
- **`references/08-document-engine.md`** — how the master CV is kept as structure
  (named variants, slugged evidence items, a fixed count) so phase 4 tailors by
  choosing, then renders through phase 2's pipeline and verification gate. Load
  it with phase 2 and again with phase 4.

Phase 6 is also a standalone entry point. If the user opens with "check my
email" or "revisa mi mail", go straight to `references/06-inbox-triage.md`.

## Entry

Ask for the CV and for a campaign brief from a previous session, if there is
one. Accept the CV as a file, a pasted block of text, or a LinkedIn profile
URL. Accept a standalone request with neither, such as "check my email" or
"find me openings."

**Branch on what is attached, before doing anything else:**

- **No brief, a CV supplied.** First run. Confirm the surface (below), then go
  to `references/01-cv-audit.md`. Phases 1 and 2 run once, in order, and never
  run again on their own after this.
- **A brief attached, no new CV.** Restore every field from it, including the
  master CV text held in its CV assets section — that text, not any file left
  in this session, is what later phases tailor from. Do not re-run the CV
  audit or the master CV rewrite — the brief's own status record shows they
  already happened. **Unless that text is missing or unusable**: a brief
  written before the field existed, truncated, hand-edited, or with its fenced
  block broken on re-upload. There is nothing to tailor from then, so say so
  plainly, ask for the CV as a file, pasted text or a profile URL, and run
  `references/02-master-cv.md` to rebuild the master before any browser phase.
  Never improvise a master from the brief's remaining fields, and never
  reconstruct one from memory of an earlier session.
  Resume exactly where the brief says the last session stopped: the next
  unswept platform, the next queued application, a blocked item, or whatever
  its status and "next step" fields name.
- **A brief attached and a new CV supplied.** Restore the brief, then ask once,
  before anything else: "You attached a new CV — want the audit and rewrite run
  on it, or keep the master CV already on file?" Yes routes to
  `references/01-cv-audit.md`. No keeps the existing master CV untouched and
  routes straight to whichever browser phase the brief's status calls for.
- **A standalone request, no CV.** "Check my email", "find me openings," or an
  equivalent — the two do not need the same things to start.
  - **Inbox triage** ("check my email", "revisa mi mail") always proceeds:
    go straight to `references/06-inbox-triage.md`. Reading and classifying
    an inbox needs no CV, no brief and no parameters. With brief state on
    file it scores new openings in full; without it, it still runs, degraded,
    exactly as that reference file describes.
  - **Job search** ("find me openings", "buscame trabajo") does need
    parameters. If an attached brief supplies the state that phase needs
    (profile, targets, salary table, disqualifiers, platforms), go straight
    to `references/03-job-search.md`. Without a brief, or without that
    state, say so and ask for the CV, or offer to run phase 3's parameter
    collection first — there is nothing to search from otherwise.

Phases 1 and 2 never re-run on an existing brief on their own. There are two
exceptions, both above: the user attaches a new CV and explicitly says yes to
rerunning them, or the brief holds no usable master CV text and phase 2 has to
rebuild one before any browser phase can tailor from it.

Then confirm the surface, when it is not already known from the brief: ask
whether they are in the Claude in Chrome side panel, Claude Cowork on desktop,
or Claude Code. Phases 3 to 6 need one of those with browser access. If they
have none, run phases 1 and 2 (or resume where the brief left off), deliver the
files, and explain how to apply by hand.
