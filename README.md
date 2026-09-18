# fix-cv-find-job-skill

**English** · [Español](README.es.md)

**Fixes your CV and finds you a job.** A Claude skill that audits your resume
like a recruiter, rewrites it as a master template you can adapt to any opening,
searches the job boards you actually use, applies for you, aligns your LinkedIn,
and triages your inbox for replies.

Works for **any industry**. It derives your field from your own CV instead of
assuming you work in tech.

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

## What it does

| Phase | What you get | Needs a browser |
|---|---|---|
| 1. CV audit | 20 roles you are the best candidate for, the ATS keywords to carry, what a screener sees in 10 seconds, and a score out of 10 with the path to raising it | no |
| 2. Master CV | Your CV rebuilt on the XYZ formula, ATS-ready, two pages, with swappable summary variants — delivered as `.docx` and `.pdf` | no |
| 3. Job search | Every matching opening across your platforms, ranked, with a match score and the keywords each one wants | yes |
| 4. Apply | A tailored CV and cover letter per opening, forms filled, applications tracked, full report | yes |
| 5. LinkedIn | Your profile aligned with the rewritten CV | yes |
| 6. Inbox | Replies, new openings and acknowledgements sorted — triggered any time with "check my email" | yes |

Every phase ends with a report and a question. Nothing runs end to end on its
own, and nothing is sent without you seeing it first.

## Requirements

Phases 1 and 2 run anywhere Claude skills run.

Phases 3 to 6 drive a real browser using your existing logins, which needs one
of:

- **Claude in Chrome** side panel — paid plan, Chrome or Edge on desktop only
- **Claude Cowork** on desktop
- **Claude Code** started with `claude --chrome`

If you have none of those, the skill stops after phase 2 and hands you the
files with instructions for applying by hand. That is a complete outcome, not
a failure.

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
2. Go to **Settings → Skills → Upload skill**
3. Select the zip. A security scan runs on save.

### From the terminal

```
/plugin marketplace add atarico/fix-cv-find-job-skill
/plugin install fix-cv-find-job-skill@fix-cv-find-job
```

Or in Claude Code, straight from a clone:

```bash
git clone https://github.com/atarico/fix-cv-find-job-skill.git
ln -s "$PWD/fix-cv-find-job-skill/skills/fix-cv-find-job-skill" ~/.claude/skills/
```

## How to use it

### Before you start

- Your CV in any format — PDF, Word, or pasted as plain text. If you do not have
  one, a link to your professional profile works to begin with.
- For the job search phases: be **logged in** on the job boards you want to
  search, in the same browser. This skill never creates accounts and never
  enters passwords.

### Starting

There is no command to remember. Attach your CV and write what you want:

> review my CV · find me a job · check my email for replies

It replies in whatever language you write in.

### What happens, step by step

**1. It asks what it needs.** Your CV, and which Claude surface you are on — the
answer decides whether the browser phases are available.

**2. You get the audit.** Twenty roles you are the best candidate for split into
direct, adjacent and stretch; the ATS keywords you should be carrying, marked as
present, weak or missing; what a screener sees in the first ten seconds; and a
score out of ten with a breakdown and the path to raising it.

Then it stops and asks whether to rewrite.

**3. You get the master CV.** Every bullet rebuilt on the XYZ formula — result,
number, method — with vague and passive language stripped out, the keywords
worked in, two pages, and several swappable summary variants so you can retarget
it per opening. Delivered as `.docx` and `.pdf`.

If you have no browser available, this is where it ends, and it hands you the
files plus instructions for applying by hand. That is a complete outcome.

**4. It surveys the market.** It asks which platforms you use, your salary
expectation, your target seniority, and your hard disqualifiers — the
requirements you genuinely cannot meet. Then it searches, scores every opening,
and gives you a ranked table plus the list of what it discarded and why.

Then it stops and asks whether to apply.

**5. It applies.** A tailored CV and cover letter per opening, forms filled,
everything recorded. It asks first whether you want to approve submissions in
one batch at the end or one at a time.

**6. LinkedIn and inbox, if you want them.** Profile aligned with the new CV;
inbox sorted into real replies, new openings and automatic receipts.

### Answer honestly when it asks

The audit and the match scores are only as good as what you tell it. If you
overstate your seniority or hide a disqualifier, it will send you to interviews
you cannot pass. It never invents anything you did not give it — which also
means it cannot fix what you misreport.

### Triggering the inbox check on its own

You do not have to run the whole workflow. At any point, in any conversation:

> check my email

It sorts replies, new openings and receipts, and reports back.

### Keeping your campaign between sessions

The Chrome side panel has no persistent disk, so nothing carries over on its
own. At the end of a session the skill produces a **campaign brief** — download
it, and attach it next time. It restores your profile, your targets, everything
you have applied to, and everything still blocked.

It also prevents the most common failure of a long search: applying twice to the
same job.

## What it will not do

These limits are built in and not configurable.

- Create accounts, enter passwords, or sign in via SSO
- Solve CAPTCHAs
- Invent personal data, dates, credentials or experience
- Claim any skill or qualification absent from your CV
- Send email in your name — it drafts, you send
- Accept an offer, agree to terms, or negotiate
- Delete email permanently — acknowledgements go to Trash, recoverable
- Open your personal email

It also honours postings that forbid AI-assisted applications: it flags them and
hands them to you.

### Two things to know

**Every form submission pauses for your approval.** Claude always asks before
submitting a form or sharing personal data. This is a platform rule and cannot
be switched off. The skill asks at the start whether you want to approve in one
batch at the end or one at a time — but a fully unattended run is not possible,
and any tool promising you one is misleading you.

**The inbox pass is a first pass.** The skill decides what to open from sender
and subject, so it will miss things that are worded unusually. Check your inbox
yourself as well.

## Contributing

The rules in `references/` are the substance of this skill — most of them were
paid for with lost applications. If your field works differently, or you learned
something the hard way, open an issue or a PR.

Particularly welcome: field-specific screening conventions, regional CV norms,
platform quirks, and rules that saved you from a mistake.

## License

Apache-2.0
