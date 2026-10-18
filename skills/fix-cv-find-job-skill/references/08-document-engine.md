# Document engine — tailor from structure, render with the phase 2 pipeline

Phase 2 ends with a master CV. Phase 4 then says "tailor the CV". Taken
literally that means rewriting a whole document for every application, which is
slow, drifts in quality across a campaign, and has no way to keep the two-page
promise.

The fix is not a second document builder. It is to hold the master CV as
**structure** — named summary variants and slugged evidence items — so that
tailoring one application is a small choice, and then to render the result
through **exactly the pipeline phase 2 already uses**. There is one layout
source in this skill, `assets/reference.docx`, and this file never creates
another.

This file applies on every surface. The structure needs no code execution; only
the rendering step depends on the surface, and it depends on it in the same way
phase 2 does.

## What is kept as structure

Three things, all living in the master CV text that the campaign brief stores.

**1. Summary variants, by name and language.** Phase 2 already builds three to
five named variants, one per specialisation, held in every language. They stay
exactly as phase 2 defines them. The name is what phase 4 selects by.

**2. Evidence items, by slug.** The applicant's portfolio items or, where there
is no portfolio, the field's own equivalent: licences, certifications,
rotations, registration numbers, a trade record. Give each a short lowercase
slug that says what it is. A nurse might have `icu_rotation`,
`rapid_response_training` and `preceptor_program`; an accountant
`month_end_close`, `audit_support` and `payroll_migration`. Each item's text is
written once, in every language, in the master CV. The slug is how phase 4 picks
it in one word instead of re-describing it.

**3. A fixed evidence count for the campaign.** Decide it once — how many items
go on each tailored CV — and record it in the brief. The count is what keeps
every application at the same length; the choice of *which* items is made per
posting.

In the master CV text, mark each variant and each evidence item with a comment
the assembly step can find, on the same principle as phase 2's rule that every
swappable block carries a marker:

```
<!-- variant: critical_care -->
<the variant's summary text>
<!-- /variant -->

<!-- evidence: icu_rotation -->
<the item's lines>
<!-- /evidence -->
```

Strip the markers before anything is rendered; they exist only for assembly.

## The per-application config

This is the whole cost of tailoring one application, written out before
anything is assembled:

```
language: en
variant: critical_care
evidence: icu_rotation, rapid_response_training, preceptor_program
letter: three or four short paragraphs, in the posting's language
```

The language is the posting's, and it picks which master and which language of
the variant. The variant is the one whose specialisation matches the posting; if
none fits, that is a signal to add a variant to the master, not to improvise
prose for one application. The evidence slugs are exactly as many as the
campaign's fixed count, chosen against what this posting asks for and never the
same set every time.

## Assembling and rendering

**Assemble.** From the master CV text for that language, build the
per-application CV as Markdown: keep the chosen variant as the summary, keep
only the chosen evidence items, keep the rest of the master as it is, reorder
skills so the posting's keywords come first, and select the experience most
relevant to this role. Build the cover letter as its own Markdown from the
letter paragraphs. Nothing is invented: every line comes from the master CV or
from what the applicant confirmed.

**Render exactly as phase 2 does.** Phase 2's "Producing the three files" in
`references/02-master-cv.md` owns the capability probe, the three branches, the
skill-folder asset path and where outputs go; do not restate them here. Run the
same probe once for the session and use the same branch, with the per-application
Markdown as input, for the CV and for the letter. With no code execution, hand
over the assembled Markdown in chat, and say once that files need code execution.

Name the files as phase 4 specifies. There is no other layout source: no HTML,
no browser print step, no builder kept in the brief.

## Verify before sending

Run phase 2's "Verify, do not trust" gate in `references/02-master-cv.md` on each
produced PDF and do not restate it here: page count, extracted text, and the
font check. The CV must pass at two pages or fewer. The letter must be exactly
one page, and it goes through the same text and font checks. A font fallback is
not a content problem — install the font and re-render before shortening
anything, as that gate says.

Then look at the first page of each document as rendered, which no count
catches: a heading orphaned at the bottom, a paragraph that ran to the margin, a
variant left as a marker or a placeholder. On surfaces that cannot run the gate,
do the parts of it the surface can run and say which were not. If a document is
over length, shorten the letter or drop one evidence item and render again;
never ship it over and never silently cut.

Record in the brief that the check ran and what it returned.

## Keep the structure across sessions

The master CV text in the brief already carries the markers, so a resumed
session restores the variants and evidence items along with it. What the brief
adds is the table of slugs and the fixed count — see its CV assets section. When
the master CV changes, the master text changes; regenerate, never hand-edit a
produced file.

## When there is no code execution

Nothing about the structure changes; only the output does.

- Keep the same variants and slugs in the brief. The selection discipline is what
  makes tailoring fast and consistent.
- Assemble each tailored CV and letter as Markdown and hand it over in chat.
- Keep length under control by what you can control — a fixed section order and
  the fixed evidence count — since there is no file to measure.
- Tell the applicant once that this environment delivers text rather than files, and
  that code execution, where it can be turned on, changes that.
