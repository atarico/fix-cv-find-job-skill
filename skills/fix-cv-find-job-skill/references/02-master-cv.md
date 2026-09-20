# Phase 2 — Master CV

Rewrite the CV as a master template the user adapts to any opening. Not a
finished CV for one job: a base where swapping a handful of marked lines
retargets the whole document.

**What the master must be.** It covers the bases of the applicant's whole
sector, not one posting or one recent role — the CV you would hand someone who
says they need people in that sector, without naming a specific opening. There
is one master per language, never one per specialisation: specialisations live
in the summary variants built later in this phase, as instructions for adapting
this one document, not as separate CVs. State this plainly here, because
nothing downstream checks for it: without this rule, a model tends to bias the
master toward whichever job sits most recent in the source CV, and nothing
later in this workflow catches that drift.

The CV always comes back in the Harvard style: black and white, one column,
the fixed template in `assets/reference.docx`. There is nothing to weigh
against it, and nothing to ask about colour, columns or typography.

The master ships without a photo. Photos are routinely discarded in the
United States, the United Kingdom and Canada on bias-avoidance grounds, and
expected across much of continental Europe and Latin America — whether to
add one depends on the market the applicant is targeting, not on this skill.
An applicant whose market expects a photo adds it themselves afterwards, in
their own copy, with a word processor.

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

## Producing the three files

Write the CV as clean Markdown first and show it to the user in chat before
converting. Then convert with whatever the current surface has. Every run now
delivers the same three files — `.docx`, `.pdf`, and the clean Markdown —
there is no branch left that skips any of them:

**Any surface with code execution enabled in Settings > Capabilities** — the
Claude in Chrome side panel, Cowork, and ordinary web chat, including the free
plan, all qualify once that setting is on; this is the same capability
`SKILL.md`'s compatibility line promises. Build the .docx with `python-docx`
and the .pdf with `reportlab`, or generate the .docx and render the .pdf from
it. Also write the clean Markdown already produced above to a file, named
`CV_<Name>_Master_<Language>.md`. Deliver every file the naming rule below
calls for as downloads. There is no local working directory here; the user
saves the files through the browser.

**That same setting, off.** It is off by default, so do not assume it is on.
Without code execution there is no way to build a .docx or a .pdf on these
surfaces: hand the applicant the clean Markdown already produced above,
directly in the chat, as the deliverable. Say plainly why there are no
files — code execution is off — and name the toggle: **Code execution and
file creation**, under Settings > Capabilities. Let the applicant decide:
turn it on and ask again for the finished files, or take the Markdown as is.
Close the phase with the second opener below — the file-naming rules that
follow this section do not apply to this branch.

**Claude Code** — convert locally, and **always pass the reference document**.
Run this whole produce-and-verify block once per language, from a separate
`CV_<Language>.md`, so one language's output never overwrites another's:

```bash
pandoc "CV_<Language>.md" -o "CV_<Name>_Master_<Language>.docx" --reference-doc=assets/reference.docx
libreoffice --headless --convert-to pdf "CV_<Name>_Master_<Language>.docx" --outdir .
```

The third deliverable needs no extra conversion: `CV_<Language>.md` above is
already the pandoc input, sitting on disk. Copy it to
`CV_<Name>_Master_<Language>.md` and hand that file over alongside the .docx
and .pdf:

```bash
cp "CV_<Language>.md" "CV_<Name>_Master_<Language>.md"
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

Produce this set once per language from the language section above. Name the
files `CV_<Name>_Master_<Language>.docx`, `CV_<Name>_Master_<Language>.pdf`
and `CV_<Name>_Master_<Language>.md`. The suffix is never dropped, not even
for an applicant who works in a single language: the commands above emit it
unconditionally and the two-page gate checks for it, so an exception here
would leave the gate looking for a file that was never written.

Verify the Markdown was actually written, once per language, before it is
ever named to the applicant: on Claude Code, run
`test -s "CV_<Name>_Master_<Language>.md"` right after the `cp` above. On
the browser branches, where there is no shell to check with, the
file-creation tool's own result is the check — the write succeeded and the
file appears among the downloads offered, not merely named in the closing
line. Either way, if the check fails, retry once; if it still fails, say so
plainly and hand over the Markdown already shown in chat instead of naming a
file that was never produced.

## Close the phase

An angle-bracket token marks a value to fill in: a slot in a message written
to the applicant, such as `<files>` below, or a variable in a filename, such
as `<Name>` and `<Language>` throughout this phase. Those must always be
substituted, and no angle-bracket token may ever reach text the applicant
actually reads or a file they receive. The same holds for the campaign
brief: a field that still carries its placeholder, such as `<surface>` or
`<seniority>`, is legitimately unanswered and counts as empty, never as a
recorded answer, for every placeholder field in the brief.

Show the user the finished CV and point out what changed and why — they should
be able to maintain this themselves afterwards. Then send exactly one of the
two openers below, chosen by the outcome just reached, never more than one.
The label before each opener is for the model only — only the quoted line is
applicant-facing. The first opener carries a `<files>` slot: fill it with
every `.docx`, `.pdf` and `.md` produced this run, one set of three per
language processed. Never a fixed count — a bilingual or multilingual run
produces one set per language. The second opener has no slot: code execution
was off, so no file was produced to name. Before sending, check: exactly one
opener went out, matching the outcome reached, never more than one; on the
first opener, `<files>` was replaced — no angle-bracket token reaches the
applicant.

Files produced:

> The master CV is ready: <files>.

Code execution off, no file produced:

> There are no files this run — code execution is off. The rewritten CV is
> the Markdown already shown above, ready to paste into your own document, and
> your campaign brief is here as text too. Keep both, and attach the brief next
> time: it is what lets me pick up where we left off instead of starting over.
> Turn on Code execution and file creation in Settings > Capabilities and ask
> again for the finished .docx, .pdf and Markdown, or keep the Markdown as is.

Both outcomes above still get the same handoff:

> From here I can search openings and apply for you, but that needs a browser
> Claude can drive: the Claude in Chrome side panel, Claude Cowork on desktop,
> or Claude Code started with `--chrome`. Any of those needs a paid plan, and
> Claude in Chrome runs on Chrome on desktop only.
>
> If you have it, tell me and we keep going. If you would rather not, we stop
> here — you have what this run produced and I will show you how to adapt it
> per opening.

Generate the campaign brief from `assets/campaign-brief-template.md` either
way, before branching on the answer. Fill Section 3's master CV text field with
the clean Markdown already produced above, one fenced block per language,
following that field's own fencing rule. Phase 4 always tailors from that text,
never from a file left in this session, and an applicant who stops here may
come back in a later session — the brief is the only thing that carries this
run forward, so it is written whether or not this session continues.

Deliver it the way this run delivered the CV: as a download where file creation
is available, and pasted into the chat as text where it is not. The brief is
Markdown and needs no file creation, so the branch that produced no files still
produces this one. Tell the applicant to keep it and attach it next time —
without it, nothing from this run survives the session.

If the user declines, hand over whatever this run produced — the files, or the
Markdown already shown in chat — together with the brief, a short guide on
swapping the summary and skills per opening, and the naming convention when
files exist. Then stop cleanly. This is a complete outcome, not a failure.

If the user says they have it, go to `references/03-job-search.md`.
