# Phase 2 — Master CV

Rewrite the CV as a master template the user adapts to any opening. Not a
finished CV for one job: a base where swapping a handful of marked lines
retargets the whole document.

## Format — ask once, before rewriting, only if there is something to ask

Look at the source CV before starting. If it is already plain — no photo, no
colour — there is nothing to decide: skip this and go straight to the rewrite.

If the source CV carries a photo or colour, ask once, before rewriting
anything, in the applicant's own language:

> This skill returns your CV in the Harvard style: black and white, no photo.
> Do you want it that way, or do you want to keep the styles your CV already
> has? (Harvard style works better for foreign markets.)

Then branch:

- **Harvard.** Proceed with the rest of this phase exactly as written below.
- **Keep their styles.** Rewrite only the text: content, wording, ordering and
  ATS keywords still change under every rule in this phase. By intent, the
  visual format does not.

  Tell the applicant this before producing files, so the choice is informed:
  the production step below — `assets/reference.docx` on Claude Code, or the
  equivalent `python-docx` build on Claude in Chrome and Cowork — builds the
  `.docx` from clean Markdown into one fixed template, the same one used for
  the Harvard branch. That pipeline has no way to carry over the source
  file's original photo, colour or layout. So with "keep their styles," what
  this skill can actually deliver is the rewritten text in that same plain,
  one-column template, not a copy of the original design. Say so plainly
  before delivering the files, rather than handing over a plain document
  without warning. If the applicant wants their original layout back, they
  will need to paste the rewritten sections into their own file themselves —
  this skill's toolchain does not do that step for them today.

## Language — every language the applicant works in, not the posting's

No target posting exists yet at this phase, so nothing here follows one.
Produce one complete master CV per language the applicant actually works in —
ask which those are if it is not already obvious from the source CV. Build
each language's master independently: translate the structure and the named
summary variants (below), never machine-paraphrase one language from another
in a way that drifts the claims apart. The posting's language only enters at
phase 4, when a specific posting exists to tailor a copy toward.

## The XYZ formula

Every bullet, without exception:

> Accomplished **[X]** as measured by **[Y]**, by doing **[Z]**.

X is the result. Y is the number that proves it. Z is the method that shows
competence. English word order puts the result first; other languages may need
Z earlier to read naturally — keep the three components, adapt the order to the
language.

Good: *Cut month-end close from 9 days to 4 by rebuilding the reconciliation
workflow and training the 6-person team on it.*

Bad: *Responsible for improving accounting processes.* No result, no number, no
method, and "responsible for" describes a job description rather than a person.

### When there is no number

Most people have numbers and do not know it. Before dropping Y, dig:

- Volume — how many, how often, how large.
- Time — how long before, how long after.
- Money — budget held, cost cut, revenue touched.
- People — team size, students, patients, clients, tickets.
- Scope — sites, countries, product lines, systems.
- Quality — error rate, satisfaction, compliance, retention.

Ask the user for the ones only they know. Ask in one grouped block.

If a number genuinely does not exist, use scale or outcome instead of inventing
one: *for a 400-bed hospital*, *across three provinces*, *approved without
revisions*. Never fabricate a figure. Never round a guess into a fact.

## Language rules

Strip on sight:

- Passive voice and "responsible for", "in charge of", "tasked with",
  "participated in", "helped with", "involved in", "duties included".
- Adjective stacking with no evidence: *proactive*, *dynamic*, *results-oriented*,
  *passionate*, *hardworking*, *team player*, *detail-oriented*.
- Hedges: *helped to*, *assisted in*, *supported the*, *contributed to* — unless
  the contribution is genuinely named and bounded.

Every bullet opens with a strong past-tense verb of action, varied across the
document. Current role in present tense, everything else past.

## Structure — two pages maximum

This cap, and the machine-checked gate below that enforces it, serve the
ordinary case this skill is built for: applicants hiring through job platforms,
matched by recruiters and ATS software that expect a short, scannable
document. Academic, research and government CVs — publications lists, clinical
rotations, full grant histories, dossiers running well past two pages — follow
longer conventions of their own field and are out of scope for this skill. That
scope does not narrow the industry this skill serves: the overwhelming majority
of professions hiring through platforms fit two pages; the exceptions above are
named because they do not.

1. **Header** — name, target job title, location and work arrangement (remote,
   hybrid, relocation), phone, professional email, and the links that matter in
   that field. Plain text, never inside an image or a header/footer element.

2. **Flexible summary** — three to four lines. This is the block the user swaps
   per opening, so build it modular: seniority and years, core specialty, two or
   three proof points, and a closing line on the differentiator. Then supply
   **three to five ready-made variants, each with its own name**, one per
   specialisation found in phase 1's role clusters — derived from the
   applicant's own CV, never assumed. Name each variant after what it targets
   (for example, the specialisation itself, or "Direct" versus "Adjacent"
   framing), so the applicant and phase 4 can pick one by name instead of by
   guessing which block fits. Hold the same named set, translated, in every
   language from the section above — a variant keeps its name and its target
   across languages, only the text changes.

3. **Skills** — grouped by category, front-loaded with the ATS keywords from
   phase 1 that the user can legitimately claim. Scannable, no rating bars, no
   percentages, no star graphics.

4. **Experience** — reverse chronological. Employer, title, location, dates as
   MM/YYYY. Three to five XYZ bullets each, strongest first. Older or less
   relevant roles compress to one or two lines.

5. **Education, certifications and licences** — full name plus acronym,
   institution, year. Put this section above experience only when the field
   screens on credentials first, such as medicine, law, education or engineering.

6. **Whatever the field demands** — publications, portfolio, clinical rotations,
   languages, security clearance, union membership, tooling. Include only what
   that market actually asks for.

Mark every swappable block with a comment the user can find and replace.

## ATS compatibility

- One column. No tables, no text boxes, no columns for content.
- Standard section headings. "Work Experience", not "My Journey".
- No critical information in headers, footers, images or graphics.
- Standard fonts. No icons carrying meaning that text does not repeat.
- Dates in a consistent MM/YYYY format.
- The file itself is real text, never a scan or an exported image.

## Producing .docx and .pdf

Write the CV as clean Markdown first and show it to the user in chat before
converting. Then convert with whatever the current surface has:

**Claude in Chrome side panel or Cowork** — use the file creation capability.
Build the .docx with `python-docx` and the .pdf with `reportlab`, or generate
the .docx and render the .pdf from it. Deliver both as downloads. There is no
local working directory here; the user saves the files through the browser.

**Claude Code** — convert locally, and **always pass the reference document**.
Run this whole produce-and-verify block once per language, from a separate
`CV_<Language>.md`, so one language's output never overwrites another's:

```bash
pandoc CV_<Language>.md -o "CV_<Name>_Master_<Language>.docx" --reference-doc=assets/reference.docx
libreoffice --headless --convert-to pdf "CV_<Name>_Master_<Language>.docx" --outdir .
```

`assets/reference.docx` ships with this skill. It matters: pandoc's stock
styling is built for reports — one-inch margins, 12pt body, oversized headings —
and renders the same CV across four pages. Without this flag you will cut good
content to fix a problem that was never the content's.

If the file is missing, regenerate it with `scripts/make-reference-docx.py` from
the repository. Do not work around its absence by shrinking the font.

### Verify, do not trust

Check the output rather than assuming the conversion behaved. Run this gate
separately for each language's file — every language must pass it on its own;
one language passing never excuses another from the check:

```bash
pdfinfo "CV_<Name>_Master_<Language>.pdf" | grep Pages     # must be 2 or fewer
pdftotext "CV_<Name>_Master_<Language>.pdf" - | wc -c      # must be non-trivial
```

A PDF that yields almost no characters is an image, and an image is invisible to
every ATS. Then spot-check that the contact details, every employer, and the
headline metrics all survived into the extracted text.

A finished two-page CV lands around 3,000 characters per page. Substantially
less means the layout is loose, not that the content is thin — fix the layout
before cutting anything.

If it still runs long, **cut content**: drop the weakest bullet from each role,
keeping the ones carrying numbers, and fold any evidence worth saving into a
surviving bullet. Never shrink the font below readable size and never squeeze
the margins to hide the overflow. A cramped CV reads as desperate.

Produce this pair once per language from the language section above. Name the
files `CV_<Name>_Master_<Language>.docx` and `CV_<Name>_Master_<Language>.pdf`.
The suffix is never dropped, not even for an applicant who works in a single
language: the commands above emit it unconditionally and the two-page gate
checks for it, so an exception here would leave the gate looking for a file
that was never written.

## Close the phase

Show the user the finished CV and point out what changed and why — they should
be able to maintain this themselves afterwards. Then:

> The master CV is ready in .docx and .pdf.
>
> From here I can search openings and apply for you, but that needs a browser
> Claude can drive: the Claude in Chrome side panel, Claude Cowork on desktop,
> or Claude Code started with `--chrome`. Claude in Chrome needs a paid plan
> and runs on Chrome on desktop only.
>
> If you have it, tell me and we keep going. If you would rather not, we stop
> here — you have the files and I will show you how to adapt them per opening.

If the user declines, hand over the files, a short guide on swapping the summary
and skills per opening, and the naming convention. Then stop cleanly. This is a
complete outcome, not a failure.

If the user says they have it, generate the campaign brief from
`assets/campaign-brief-template.md` before moving on, and go to
`references/03-job-search.md`.
