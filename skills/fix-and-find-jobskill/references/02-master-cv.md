# Phase 2 — Master CV

Rewrite the CV as a master template the user adapts to any opening. Not a
finished CV for one job: a base where swapping a handful of marked lines
retargets the whole document.

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

1. **Header** — name, target job title, location and work arrangement (remote,
   hybrid, relocation), phone, professional email, and the links that matter in
   that field. Plain text, never inside an image or a header/footer element.

2. **Flexible summary** — three to four lines. This is the block the user swaps
   per opening, so build it modular: seniority and years, core specialty, two or
   three proof points, and a closing line on the differentiator. Then supply
   **three to five ready-made variants** aimed at the different role clusters
   found in phase 1, clearly marked as swappable.

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

**Claude Code** — convert locally:

```bash
pandoc CV.md -o "CV_<Name>.docx" --reference-doc=reference.docx
libreoffice --headless --convert-to pdf "CV_<Name>.docx" --outdir .
```

Then verify the result rather than trusting it: confirm the page count is two
or fewer, confirm the text is selectable in the PDF, and confirm no content was
dropped in conversion. If it runs to three pages, cut — do not shrink the font
below readable size or squeeze the margins to hide the overflow.

Name the files `CV_<Name>_Master.docx` and `CV_<Name>_Master.pdf`.

## Close the phase

Show the user the finished CV and point out what changed and why — they should
be able to maintain this themselves afterwards. Then:

> The master CV is ready in .docx and .pdf.
>
> From here I can search openings and apply for you, but that needs a browser
> Claude can drive: the Claude in Chrome side panel, Claude Cowork on desktop,
> or Claude Code started with `--chrome`. Claude in Chrome is a paid feature and
> runs on Chrome or Edge on desktop only.
>
> If you have it, tell me and we keep going. If you would rather not, we stop
> here — you have the files and I will show you how to adapt them per opening.

If the user declines, hand over the files, a short guide on swapping the summary
and skills per opening, and the naming convention. Then stop cleanly. This is a
complete outcome, not a failure.

If the user says they have it, generate the campaign brief from
`assets/campaign-brief-template.md` before moving on, and go to
`references/03-job-search.md`.
