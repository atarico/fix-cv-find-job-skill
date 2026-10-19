---
name: fix-cv-find-job-skill
description: Fixes your CV and finds you a job. Use when the user wants a resume or CV reviewed, rewritten, scored, or optimized for ATS; wants to find or search job openings and vacancies; wants help applying to jobs, writing cover letters, or tracking applications; wants their LinkedIn profile improved to match their CV; or says things like "review my CV", "revisa mi CV", "find me a job", "buscame trabajo", "apply for me", "postulate por mi", "check my email for job replies" or "revisa mi mail". Works for any industry or profession, not only tech.
license: Apache-2.0
compatibility: Phases 1 and 2 (CV audit, rewritten CV as .docx, .pdf and Markdown) run in any Agent Skills client that can execute code, such as Claude, ChatGPT, Codex or OpenCode; without code execution the CV comes back as Markdown in chat. Phase 3 runs there too, in chat mode: openings found by web search and tailored CVs for the best, sent by the applicant. Applying, LinkedIn and inbox (phases 4 to 6) need Claude in Chrome, which needs a paid Claude plan and Chrome on desktop.
metadata:
  version: 0.7.0
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
     always. The quoted lines in this skill (`> …`) say what to tell the
     applicant, written in English for you: say them in the applicant's
     language, never verbatim in English to someone who writes in another.
   - **The master CV** is built in every language the applicant works in. It
     follows no posting — phase 2 runs before any posting exists.
   - **The tailored CV and cover letter** follow the target job posting's
     language. That choice is made per posting, in phase 4, once a posting is
     in hand.
2. **Never invent credentials.** No degree, job, date, tool, metric or employer
   that is not in the user's source CV or explicitly confirmed by them. Rewriting
   is reframing, never fabrication. If a bullet needs a number the user never
   gave, ask for it or leave it out. Today's date is never assumed either:
   take it from your context or the system clock (`date +%F` where code runs)
   before writing a date, counting years of experience or reading "Present".
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

Phases 3 to 6 only, and only when the capability check at Entry found Claude in
Chrome. Without it, skip this section, chat mode included: it sends nothing, so
there is nothing to authorise. Do not ask the question.

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
> apply down the ranked list. An opening that clearly breaks one of your own
> filters I will discard, with the posting's own words as the reason, and the
> borderline ones I will list for you to decide.

- **`autonomous`** — the ranking is reported and the run continues into phase 4
  in the same turn. No question between phase 3 and phase 4, and no question
  about batching. This is the mode that reaches the whole board, and choosing
  it is the applicant's authorisation for the ranked list.
- **`stepwise`** — phase 3 ends with the ranked table and waits.

Record the applicant's answer under Preferences in the brief. If the
applicant's first instruction already describes a full round **and explicitly
asks to apply** — "check my mail and apply to what comes up" — treat that as
`autonomous` for this run only and confirm it in the closing report rather than
interrupting to ask. An inferred mode is not recorded in the brief: only an
answer to the run-mode question is, so the next session with no recorded mode
asks. An instruction that only asks to look, search or check does not infer it:
ask.

Nothing in this mode weakens the absolute limits. It changes when you ask, not
what you are allowed to do. An opening that clearly breaks the applicant's own
filters or the seniority floor is discarded with the posting's sentence as
evidence, and the run continues, in either mode. Genuinely borderline openings
go to the report's "Needs a decision" list.

## Platform limits (state these, do not fight them)

Most of these are enforced by the platform, not by this skill. Tell the user up
front so they do not mistake a guardrail for a malfunction. They describe
Claude in Chrome: when the capability check at Entry found it absent, skip this
section and do not mention Chrome limits.

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
  demands signup or SSO, tailor the CV and letter, run the document
  verification, skip the form and hand the opening over with the documents
  ready. Recognise it early, using the destination table in
  `references/07-sweep-mechanics.md`, so no time goes into filling a form that
  cannot be completed.
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

| # | Phase | Reference | Needs Claude in Chrome |
|---|---|---|---|
| 1 | CV audit and score | `references/01-cv-audit.md` | no |
| 2 | Master CV rewrite (.docx + .pdf + Markdown) | `references/02-master-cv.md`, `references/08-document-engine.md` | no |
| 3 | Job search and match table | `references/03-job-search.md`, `references/07-sweep-mechanics.md` | no: without it, chat mode |
| 4 | Auto-apply | `references/04-auto-apply.md`, `references/08-document-engine.md` | yes |
| 5 | LinkedIn alignment | `references/05-linkedin.md` | yes |
| 6 | Inbox and messages triage | `references/06-inbox-triage.md` | yes |

Two of those references are techniques rather than phases, and both are worth
loading with the phase that uses them:

- **`references/07-sweep-mechanics.md`** — how to read a whole board without
  exhausting the context: harvesting identifiers, batch reads in the page you
  already have open, three-tier triage, set-difference duplicate checks,
  hard-filter false positives, the destination table, and what to do when the
  browser fails. Load it with phase 3; phase 6 harvests with the same technique.
- **`references/08-document-engine.md`** — how the master CV is kept as structure
  (named variants, slugged evidence items, a fixed count) so phase 4 tailors by
  choosing, then renders through phase 2's pipeline and verification gate. Load
  it with phase 2, and again with phase 4 or chat mode.

Phase 6 is also a standalone entry point. If the user opens with "check my
email" or "revisa mi mail", go straight to `references/06-inbox-triage.md`.

## Entry

Ask for the CV and for a campaign brief from a previous session, if there is
one. Accept the CV as a file, a pasted block of text, or a LinkedIn profile
URL. Accept a standalone request with neither, such as "check my email" or
"find me openings."

**Branch on what is attached, before doing anything else:**

- **No brief, a CV supplied.** First run. Run the capability check (below),
  then go to `references/01-cv-audit.md`. Phases 1 and 2 run once, in order, and never
  run again on their own after this.
- **A brief attached, no new CV.** Restore every field from it, including the
  master CV text held in its CV assets section — that text, not any file left
  in this session, is what later phases tailor from. Do not re-run the CV
  audit or the master CV rewrite — the brief's own status record shows they
  already happened. **Unless that text is missing or unusable**: a brief
  written before the field existed, truncated, hand-edited, or with its fenced
  block broken on re-upload. There is nothing to tailor from then, so say so
  plainly, ask for the CV as a file, pasted text or a profile URL, and run
  `references/02-master-cv.md` to rebuild the master before any later phase.
  Never improvise a master from the brief's remaining fields, and never
  reconstruct one from memory of an earlier session.
  If its section 5b lists openings handed over, ask once which of them the
  applicant sent, and move those to section 5 before anything else. Then resume
  exactly where the brief says the last session stopped: the next
  unswept platform, the next queued application, a blocked item, or whatever
  its status and "next step" fields name.
- **A brief attached and a new CV supplied.** Restore the brief, then ask once,
  before anything else: "You attached a new CV — want the audit and rewrite run
  on it, or keep the master CV already on file?" Yes routes to
  `references/01-cv-audit.md`. No keeps the existing master CV untouched and
  routes straight to whichever later phase the brief's status calls for.
- **A standalone request, no CV.** "Check my email", "find me openings," or an
  equivalent — the two do not need the same things to start.
  - **Inbox triage** ("check my email", "revisa mi mail") needs no CV, no
    brief and no parameters: once the capability check (below) allows phase 6,
    go straight to `references/06-inbox-triage.md`. With brief state on
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
rebuild one before any later phase can tailor from it.

### Capability check

Run it at the start of every session, from your own tools. A brief's record of
the surface is a note about the previous session, never the answer: the same
brief may have been written on another agent. Detect; do not ask what your own
tools already tell you. Ask only what you cannot tell, and
never by product name.

- **Can you drive a browser through Claude in Chrome?** Look at your tools: the
  Claude in Chrome browser tools, or the step that turns them on, are either
  there or not. That covers the side panel, Cowork and Claude Code started with
  `--chrome`.
- **Can you search the web, and read a page from its link?** Look at your
  tools: one that runs a web search, one that fetches or opens a URL. Either
  can be missing; chat mode (`references/03-job-search.md`) says what each
  absence changes.
- **Can you execute code, and with which tools?** Yes or no is enough here; the
  probe in `references/02-master-cv.md` settles which tools when phase 2
  renders. If you cannot tell whether code execution is on, say what each answer
  changes and ask once.

The result decides the run:

- **Claude in Chrome available.** All six phases, exactly as written. Run mode
  and the platform limits apply from phase 3.
- **Claude in Chrome absent** (ChatGPT, Codex, OpenCode, Claude without the
  extension). The run is phases 1 and 2, then phase 3 in chat mode
  (`references/03-job-search.md`, "Chat mode"): openings found by web search or
  given by the applicant, tailored CVs for the best of them, and a ranked
  report. Nothing is sent: the applicant applies through each link. Skip run
  mode and the platform limits entirely, and do not ask the user about Chrome,
  Cowork or Claude Code. Say once, plainly: here you audit and rewrite the CV,
  find openings and prepare a tailored CV for the best ones; sending the
  applications, LinkedIn and the inbox (phases 4 to 6) need Claude in Chrome
  and continue in Claude with the extension, from the campaign brief. Any route
  above that would lead to phase 4 or later ends at that sentence, offering what
  runs here: phases 1 and 2 when there is a CV, chat mode when there is a
  master CV.
