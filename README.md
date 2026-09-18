# fix-and-find-jobskill

**Fixes your CV and finds you a job.** A Claude skill that audits your resume
like a recruiter, rewrites it as a master template you can adapt to any opening,
searches the job boards you actually use, applies for you, aligns your LinkedIn,
and triages your inbox for replies.

Works for **any industry**. It derives your field from your own CV instead of
assuming you work in tech.

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

### Upload as a skill

The simplest path, and the one to use if you work in the Claude in Chrome side
panel.

1. Download `fix-and-find-jobskill.zip` from
   [Releases](https://github.com/atarico/fix-and-find-jobskill/releases), or
   build it yourself with `./scripts/package.sh`
2. In Claude, go to **Settings → Skills → Upload skill**
3. Select the zip. A security scan runs on save.

Once enabled it is available across your account — including the Chrome side
panel, which runs as a Cowork session and picks up your account skills
automatically.

### Install as a plugin

```
/plugin marketplace add atarico/fix-and-find-jobskill
/plugin install fix-and-find-jobskill@fix-and-find
```

### Claude Code

```bash
git clone https://github.com/atarico/fix-and-find-jobskill.git
ln -s "$PWD/fix-and-find-jobskill/skills/fix-and-find-jobskill" ~/.claude/skills/
```

## Use it

You do not invoke it with a command. Just say what you want:

> review my CV · revisa mi CV · find me a job · buscame trabajo · check my email

It answers in your language.

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
