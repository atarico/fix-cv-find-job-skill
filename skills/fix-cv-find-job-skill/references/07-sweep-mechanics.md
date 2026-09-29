# Sweep mechanics — how to read a market without running out of context

Phase 3 tells you *what* to do: read the full posting, not the snippet; verify
duplicates against the platform's own record; keep the evidence for every
discard. This file is *how*, and it is the difference between triaging seventy
openings and triaging seven.

Read this before the first search of a session. It also serves phase 6, which
harvests the same identifiers out of digest emails.

## The cost problem, stated plainly

Opening a posting in a tab and reading the rendered page costs somewhere between
two and six thousand tokens. Do that eight times and the window is compromised;
do it fifteen times and the run stops applying and starts summarising. Every
report that ends "I reviewed the most relevant openings" instead of a full table
is this failure.

The fix is not to read less. It is to read cheaply.

## The pattern: identify, batch-read, extract, then score

**1. Harvest identifiers, not pages.** A search results page, a job alert email
and a digest all carry the same thing: links with an identifier in them. Collect
the identifiers first, in one pass, and never navigate per result. On a results
page that is one selector over the links. In a digest email it is the same, run
against the message body — digests are truncated for humans but their links are
intact, and a single digest routinely yields ten to twenty identifiers.

Deduplicate as you collect. Accumulate into one object keyed by identifier so
the same opening arriving through three digests is stored once.

**2. Read in batches, in the page the applicant is already viewing.** Most of
the context cost is not the reading, it is returning whole pages into the
conversation. So read each posting where it already is: in the logged-in page or
tab you have open, parse it there with a script over the page's own elements
(the title, the criteria block, the description container) and return only the
decision fields in step 3. The page never has to be rendered into the
conversation, and nothing leaves the session the applicant already has open.
This alone gets most of the saving.

Work through the harvested openings six or seven per tool call, opening each in
the tab or panel the platform itself uses to show a posting. Twelve calls cover
eighty openings. Keep a courteous pace — a pause of a second or so between
postings, the way a person reading them would — because hammering a site is bad
manners and is what its terms of use are written against. If the platform slows
you down or a posting will not load, fall back to tabs for the shortlist only,
never for the whole sweep.

Some platforms also serve a posting's full detail from a separate endpoint their
own pages call. That can be cheaper still, but it is optional and it is not the
default, for two reasons that belong to the applicant, not to this skill.
Endpoints nobody documented can change or disappear without notice. And
automated access to them may breach the platform's terms, and the consequence
of that lands on the applicant's account, not on whoever wrote these
instructions. So use one only if the applicant has agreed to it, after being
told that, and record the agreement in the brief's platform table under "Read
method". Without that agreement, extract in the page.

**3. Extract decision fields, not the posting.** This is the step that protects
the context window, and the one most often skipped. Never return the full
description into the conversation. Parse it in the page and return only what a
score depends on:

- title, company, location, posted date
- the platform's own seniority and employment-type criteria
- **the sentence** containing each hard-disqualifier keyword from the campaign
  brief — not a boolean, the sentence, because the "Hard filters" section below depends on it
- the sentence containing a years-of-experience figure
- the sentence containing a salary figure
- whether the posting is closed
- a compact stack or requirements fingerprint: which of the applicant's known
  tools, licences or credentials appear at all

Keep the full text available behind a helper you can call for a single posting
when the shortlist needs a closer look. Read whole postings only for the ones
you are about to apply to.

**4. Score from the extraction.** Phase 3's scoring rules run on this table.

## Three-tier triage

Do not pay for a deep read on an opening the cheap fields already killed.

**Tier one, from the list alone** — title, company, location, posted date. This
removes openings that are closed, in a country the applicant cannot work from, in
an obviously foreign specialisation, or already in the applications table. It
costs nothing.

**Tier two, the batch read above**, only for what survived tier one.

**Tier three, the full posting in a tab**, only for what you are about to apply
to or hand over with tailored documents, because the cover letter needs a
specific detail from it and the screening questions need the exact wording.

As an illustration of the proportions: seventy-seven harvested openings can come
down to fifty-six after tier two and the hard filters, with only a handful ever
needing a full read in a tab.

## Duplicates: harvest to a set, then difference

Phase 3 says to use the platform's own duplicate-verification path. At scale
that means paginating it, not looking at it.

Page through the platform's applied-jobs record to the end — most paginate ten
per page behind numbered buttons — collecting identifiers into a set, the same
way you harvested candidates. Then take the set difference against the candidate
identifiers. The answer is exact, it takes two calls, and it does not depend on
remembering anything.

An applicant three months into a campaign has a hundred applications. Eyeballing
that list is how the same company gets applied to twice.

## Hard filters: the keyword marks, the sentence decides

Never discard on a keyword match alone. Match to find candidates for the filter;
read the whole sentence to decide.

A language filter's keyword can fire on all of these:

- *"Advanced level of written and oral English proficiency"* — discard
- *"Advanced conversational English (C1-C2), this is a client-facing role"* — discard
- *"Spanish (native), English (intermediate)"* — **keep**, the word matched the wrong half
- *"Good level of English"* — **keep**, that is not a level above the applicant's

Declare a grey zone in the brief for the phrasings that sit on the boundary —
"intermediate to advanced" is the common one — and treat them as a tiebreak
against the rest of the posting, not as an automatic discard.

Both errors are expensive and they are not symmetric in an obvious way: over-
discarding silently removes good openings and nobody ever sees them, while
under-discarding produces an application that gets rejected for the exact reason
the filter existed. Quote the sentence in the discard table either way — that is
what makes the decision checkable later.

## Know the destination before you invest

The apply button tells you what is possible, before any form is touched.
Classify first, then decide whether to fill the form.

| Destination | What is possible |
|---|---|
| Native one-click apply on the board itself | Complete and submit, screening questions included |
| Hosted ATS with an open application form (Ashby, Lever, Greenhouse and similar) | Fill every field; the applicant uploads the document and confirms |
| ATS that opens on account creation (Workday and similar) | **No form.** Tailor the CV and letter, verify them, hand the opening over with the documents ready |
| Anything gated by a CAPTCHA at submit | Fill everything, leave it loaded, hand over the last click |
| Company-owned form | Read it before investing; highly variable |

Record each platform's and each ATS's classification in the brief the first time
you meet it. The point is to spend form-filling effort only where the
application can actually be completed, and to recognise in ten seconds what
starts with a password field: it still gets its documents, and the applicant
gets the last steps.

## When the browser fails

Browser tooling fails routinely in long runs. None of these should end a sweep;
each has a known recovery. Try the recovery once, and if it fails, say so and
keep going with whatever does not need that tool.

- **A batch call fails as a whole.** Re-issue its steps as single calls. Batches
  fail more often than the calls inside them.
- **A scripted call returns blocked or empty.** Extract and return only decision
  fields — never raw URLs, tokens or query strings; you do not need them, the
  identifier and the fields are enough. If a return is still blocked, do not
  encode, split or disguise it to get it through: that is working around a
  safety filter. Report that this opening could not be read, record it as
  blocked with the reason, and continue with the next one.
- **A tab identifier is rejected.** Ask for tab context again; never reuse an
  identifier from earlier in the session.
- **The extension or bridge disconnects.** Retry once. If it still fails, tell
  the applicant plainly, and continue with the phases that need no browser —
  documents, drafts, the report, the brief.
- **A page will not render or an element will not respond after two or three
  attempts.** Stop on that opening, record it as blocked with the reason, and
  move to the next. One stuck posting must never stall the queue.

## What to hand to phase 4

A table sorted by match, and for each row: identifier, company, role, link,
score, the destination class from the table above, the evidence sentences you
extracted, and the duplicate-check result. Phase 4 should never have to re-read
a posting to know whether it can apply to it.
