> 🇪🇸 **[DOC en español](README.es.md)**

<div align="center">

# fix-cv-find-job-skill

**Fixes your CV and finds you a job.**

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.0-blue.svg)](.claude-plugin/plugin.json)
[![Phases](https://img.shields.io/badge/phases-6-blue.svg)](#six-phases-none-of-them-automatic)
[![Industry](https://img.shields.io/badge/industry-any-blue.svg)](skills/fix-cv-find-job-skill/SKILL.md)
[![No browser needed](https://img.shields.io/badge/no%20browser%20needed-2%2F6-blue.svg)](#requirements)

</div>

---

A **Claude skill** that audits your CV like a recruiter, rewrites it as a
**master template**, searches the job boards you actually use, applies for
you, aligns your **LinkedIn**, and triages your inbox for replies. It works
for **any industry** — it derives your field from your own CV instead of
assuming you work in tech.

It drafts, searches, and applies on your behalf. It never sends, accepts, or
decides anything without you seeing it first.

A phase 1 run reads like this (trimmed to the shape, not the full 20-role list):

```
Reading this as: mid-level logistics coordinator, targeting supply chain roles.
Correct me if that's the wrong market.

ROLES (20, ranked)
  DIRECT    Supply Chain Coordinator
  ADJACENT  Procurement Analyst
  STRETCH   Logistics Operations Manager

ATS KEYWORDS
  present   WMS (Warehouse Management System)
  weak      vendor negotiation — implied, never stated
  missing   Six Sigma — experience is there, the CV never names it

SCREENER (10-second read)
  "results-oriented professional" opens the summary — a phrase 40% of this
  pile also uses. It buys you nothing and costs you your best line.

SCORE   6/10 — ATS compatibility and quantification are dragging the average
  down. Ceiling without a certification you don't have yet: 8/10.
```

## Contents

- [Why this exists](#why-this-exists)
- [Six phases, none of them automatic](#six-phases-none-of-them-automatic)
- [Requirements](#requirements)
- [Install](#install)
  - [From the interface — no download, no terminal](#from-the-interface--no-download-no-terminal)
  - [Upload the zip instead](#upload-the-zip-instead)
  - [From the terminal](#from-the-terminal)
- [How you actually use it](#how-you-actually-use-it)
  - [Before you start](#before-you-start)
  - [Starting](#starting)
  - [What happens, step by step](#what-happens-step-by-step)
  - [Answer honestly when it asks](#answer-honestly-when-it-asks)
  - [Triggering the inbox check on its own](#triggering-the-inbox-check-on-its-own)
  - [Keeping your campaign between sessions](#keeping-your-campaign-between-sessions)
- [What it will not do](#what-it-will-not-do)
  - [Two things to know](#two-things-to-know)
- [Set your expectations](#set-your-expectations)
- [Contributing](#contributing)
- [License](#license)

## Why this exists

I got tired of doing this by hand.

Tired of opening the same CV for the twentieth time to move three bullets
around because this posting wanted something slightly different from the last
one. Tired of keeping a spreadsheet of where I had applied so I would not apply
twice to the same company. Tired of digging through an inbox full of automated
receipts to find the one message that was an actual reply. Tired of reading a
posting, reading my CV, and doing the keyword matching in my head — again.

None of that is hard work. It is repetitive work, and it is the kind of
repetitive work that quietly eats the hours you should be spending on the
applications that actually matter. Doing it badly costs you interviews. Doing
it well costs you your week.

So I wrote down every rule I had learned the expensive way — the ones that came
from rejections, from applications that vanished, from a posting I misread —
and turned them into a skill. Now the repetitive part runs on rails and I spend
my attention on the parts that need a human.

I built it for my own job search. I am publishing it because nobody should have
to relearn these rules one lost application at a time.

## Six phases, none of them automatic

| Phase | What you get | Needs a browser |
|---|---|---|
| 1. CV audit | 20 roles you are the best candidate for, the ATS keywords to carry, what a screener sees in 10 seconds, and a score out of 10 with the path to raising it | no |
| 2. Master CV | Your CV rebuilt on the XYZ formula, ATS-ready, two pages, with swappable summary variants — delivered as `.docx`, `.pdf` and Markdown | no |
| 3. Job search | Every matching opening across your platforms, ranked, with a match score and the keywords each one wants | yes |
| 4. Apply | A tailored CV and cover letter per opening, forms filled, applications tracked, full report | yes |
| 5. LinkedIn | Your profile aligned with the rewritten CV | yes |
| 6. Inbox | Replies, new openings and acknowledgements sorted — triggered any time with "check my email" | yes |

Every phase ends with a report and a question. Nothing runs end to end on its
own, and nothing is sent without you seeing it first.

## Requirements

Two independent things decide what you can run: your **plan**, and the
**surface** you are on.

**Plan.** Phases 1 and 2 — the CV audit and the master CV rewrite — run on the
free plan, in ordinary web chat, either way: turn on **Code execution and
file creation** under **Settings → Capabilities** and you get the finished
`.docx`, `.pdf` and Markdown; leave it off and you get the rewritten CV as
text in the chat. Phases 3 to 6 need a browser-capable surface, and every one
of those surfaces needs a paid plan.

**Surface**, for phases 3 to 6, needs one of:

- **Claude in Chrome** side panel — any paid plan, Chrome on desktop only
- **Claude Cowork** on desktop
- **Claude Code** started with `claude --chrome`

If you have none of those — including if you are on the free plan — the skill
stops after phase 2 and hands you the files with instructions for applying by
hand. **That is a complete outcome, not a failure.**

## Install

### From the interface — no download, no terminal

The easiest path, and the right one for most people.

1. In Claude, open **Customize → Plugins**
2. Click **+** → **Add marketplace** → **Add from a repository**
3. Paste `atarico/fix-cv-find-job-skill` and confirm
4. Install the plugin

That is it. Installing the plugin activates the skill, and it works the same way
an uploaded one does.

Plugins are enabled per account, so doing this once from claude.ai also covers
the Claude in Chrome side panel and Claude Cowork on desktop — there is no
separate setup for each.

### Upload the zip instead

Plugins run in Cowork, in the Chrome side panel and in Claude Code, but **not in
ordinary claude.ai chat**. If that is where you work, install it as a skill:

1. Download `fix-cv-find-job-skill.zip` from
   [Releases](https://github.com/atarico/fix-cv-find-job-skill/releases), or
   build it yourself with `./scripts/package.sh`
2. Go to **Customize → Skills**, click **+**, then **Create skill → Upload a
   skill**. The path is the same on every plan, free included.
3. Select the zip. A security scan runs on save.

### From the terminal

```
/plugin marketplace add atarico/fix-cv-find-job-skill   # register this repo as a plugin source
/plugin install fix-cv-find-job-skill@fix-cv-find-job   # install the skill from it
```

Or in Claude Code, straight from a clone:

```bash
git clone https://github.com/atarico/fix-cv-find-job-skill.git
ln -s "$PWD/fix-cv-find-job-skill/skills/fix-cv-find-job-skill" ~/.claude/skills/   # symlink so ~/.claude/skills picks it up
```

## How you actually use it

### Before you start

- Your CV in any format — PDF, Word, or pasted as plain text. If you do not have
  one, a link to your professional profile works to begin with.
- **A browser Claude can drive**, for phases 3 to 6. The usual route is the
  [Claude extension for Chrome](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) — install it and sign in before you
  start. Claude Cowork and `claude --chrome` do the same job; see
  [Requirements](#requirements) for all three, and what happens if you have
  none of them.
- For the job search phases: be **logged in** on the job boards you want to
  search, in the same browser. This skill never creates accounts and never
  enters passwords.

### Starting

There is no command to remember. Attach your CV and write what you want:

> review my CV · find me a job · check my email for replies

It replies in whatever language you write in.

### What happens, step by step

**1. It asks what it needs.** Your CV, a campaign brief if you have one from a
previous session, and which Claude surface you are on — the answer decides
whether the browser phases are available. Attach a brief and it resumes exactly
where that session stopped, without repeating the audit or the rewrite; attach
a brief alongside a new CV and it asks once whether to run the audit and
rewrite on the new one.

**2. You get the audit.** Twenty roles you are the best candidate for split into
direct, adjacent and stretch; the ATS keywords you should be carrying, marked as
present, weak or missing; what a screener sees in the first ten seconds; and a
score out of ten with a breakdown and the path to raising it.

Then it stops and asks whether to rewrite.

**3. You get the master CV.** Every bullet rebuilt on the XYZ formula — result,
number, method — with vague and passive language stripped out, the keywords
worked in, two pages, and several named, swappable summary variants — one per
specialisation from the audit — so you can retarget it per opening by name. It
is built in every language you work in; the CV itself never targets one job
posting's language, only the tailored copies in step 5 do. Delivered as `.docx`,
`.pdf` and Markdown, one set per language.

If you have no browser available, this is where it ends, and it hands you the
files plus instructions for applying by hand. That is a complete outcome.

**4. It surveys the market.** It asks which platforms you use, your salary
expectations as a table by seniority and market (it searches for a range and
gets your sign-off if you do not have a number), your target seniority — and
that you will not apply below it — and your hard disqualifiers, the
requirements you genuinely cannot meet. Then it searches, scores every opening,
and gives you a ranked table plus the list of what it discarded and why, with
the posting's own wording kept as evidence for every hard disqualifier that
fired.

Then it stops and asks whether to apply.

**5. It applies.** A tailored CV and cover letter per opening, matched to that
posting's language, forms filled, everything recorded — including a match
score. Duplicates are checked with each platform's own verification method
before anything is filled in. It asks first whether you want to approve
submissions in one batch at the end or one at a time.

**6. LinkedIn and inbox, if you want them.** Profile aligned with the new CV;
inbox sorted into real replies, new openings and automatic receipts.

### Answer honestly when it asks

**The audit is a mirror, not an oracle.** The audit and the match scores are
only as good as what you tell it. If you overstate your seniority or hide a
disqualifier, it will send you to interviews you cannot pass. It cannot invent
a degree, job, date, tool, metric or employer you did not give it — which also
means it cannot fix what you misreport.

### Triggering the inbox check on its own

You do not have to run the whole workflow. At any point, in any conversation:

> check my email

It sorts replies, new openings and receipts, and reports back.

### Keeping your campaign between sessions

The Chrome side panel has no persistent disk, so nothing carries over on its
own. At the end of a session the skill produces a **campaign brief** — download
it, and attach it next time. It restores your profile, your targets, everything
you have applied to, and everything still blocked — and it resumes exactly
where the brief says the last session stopped, so the CV audit and the master
CV rewrite never run again once the brief shows them done.

Attach a new CV alongside an existing brief and it asks once whether to rerun
the audit and rewrite on it; say no and it keeps the CV already on file and
goes straight to searching or applying.

It also prevents the most common failure of a long search: applying twice to the
same job.

## What it will not do

These limits are built in and not configurable.

- Create accounts, enter passwords, or sign in via SSO
- Solve CAPTCHAs
- Invent personal data, dates, credentials or experience
- Invent a salary figure — it only uses what you confirmed or a market range you
  accepted
- Claim any skill or qualification absent from your CV
- Apply below the seniority floor you set, even to a posting that otherwise
  scores well
- Send email in your name — it drafts, you send
- Accept an offer, agree to terms, or negotiate
- Delete email permanently — acknowledgements go to Trash, recoverable
- Open your personal email

It also honours postings that forbid AI-assisted applications: it flags them and
hands them to you.

### Two things to know

**Wondering whether a run can go fully unattended? It can't, and here's why.**
Claude always asks before submitting a form or sharing personal data. This is a
platform rule and cannot be switched off. The skill asks at the start whether
you want to approve in one batch at the end or one at a time — but a fully
unattended run is not possible, and any tool promising you one is misleading
you.

**The inbox pass is a first pass.** The skill decides what to open from sender
and subject, so it will miss things that are worded unusually. Check your inbox
yourself as well.

## Set your expectations

This skill helps you pass filters and spend your attention where it matters.
It does not guarantee you a job, and it cannot guarantee one soon. It is not
infallible, and it will not turn into a hundred interviews in two weeks —
nobody's tool does that, and anything that promises it is not being straight
with you.

It is built to be run repeatedly, not once: the standalone inbox and job
search entry points exist because postings and replies keep changing, and
duplicate detection exists because re-running is the expected pattern, not an
edge case. Run it at least once a day if you want it covering what changed
since yesterday.

And back up what it writes. This skill's rules forbid adding a degree, job,
date, tool, metric or employer you did not supply — every claim on the master
CV traces back to something you said. That does not make it infallible: it can
still reframe or emphasise something wrongly, and it is your name on the page.
Read the master CV before it goes anywhere, and confirm it reflects your real
situation. If a line would not hold up in an interview, cut it before a
recruiter finds that out for you.

## Contributing

The rules in `references/` are the substance of this skill — most of them were
paid for with lost applications. If your field works differently, or you learned
something the hard way, open an issue or a PR.

> **A new rule needs a real cost behind it — a rejection, a lost application, a
> misread posting — not a guess about what might work.**

Particularly welcome: field-specific screening conventions, regional CV norms,
platform quirks, and rules that saved you from a mistake.

## License

Apache-2.0. See [`LICENSE`](LICENSE).
