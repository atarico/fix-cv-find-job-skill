# Evals

Behavioural checks for phases 1 and 2, run with `claude plugin eval`. The tests
in `tests/` check the files; these check what an agent actually does with them.

| Case | Starts from | Checks |
|---|---|---|
| `phase1-audit-es` | a Spanish request with an English CV pasted in | the skill fires; the audit is in Spanish; no invented figures; no question about Chrome; no unsourced statistic |
| `phase2-rewrite-es` | the audit done, the applicant's answers | the rewrite is shown for approval before anything renders; plain-hyphen date ranges; Spanish; only the figures the applicant gave |
| `phase2-render-es` | the rewrite approved | a toolchain probe before the render; the .docx produced; confirmed facts in the brief; the close in Spanish |
| `phase3-chat-es` | a later session without Claude in Chrome, the campaign brief attached | chat mode: a web search, postings read in full, tailored CVs for the top ones, none for a company already applied to, only links this run opened, nothing sent, a ranked report in Spanish |

The phase 2 cases resume a scripted conversation (`history.jsonl`); the phase 3
case starts from the campaign brief phase 2 hands over (`brief.md`), which its
`scaffold.sh` copies into the run's directory. Edit the turns and the brief in
`make_histories.py`, never the generated files, and regenerate them:

```bash
python3 evals/make_histories.py
python3 tests/test_evals.py      # free: the transcripts and the case files are well formed
```

## Running

Every run is a full Claude Code session on your own account, and each case runs
three times. Cap the spend:

```bash
claude plugin eval . --ablation none --judge-model sonnet --allow-tools Bash Write Edit WebSearch WebFetch --scaffold --max-cost-usd 15
claude plugin eval . --ablation none --judge-model sonnet --case 'phase1-*' --max-cost-usd 2   # phase 1 only
```

- `--ablation none` skips the no-plugin baseline, which would double the runs.
  These checks are absolute, not a comparison.
- `--judge-model sonnet`: the default judge, Haiku, failed an all-Spanish
  audit on language and read the audit's "10 seconds" section name as a
  statistic in the first runs. The judge's cost is small next to the runs'.
- On a Claude subscription the runs use the plan's usage; the dollar figure
  is the runner's API-price equivalent, which `--max-cost-usd` caps.
- The phase 2 cases need Bash, which the runner only grants inside its sandbox:
  on Linux that needs `bubblewrap` and `socat`. On Ubuntu 24.04 and later,
  AppArmor also has to let `bwrap` create user namespaces, or every command
  fails with `bwrap: loopback: Failed RTM_NEWADDR`. A profile for
  `/usr/bin/bwrap` with `userns,` in `/etc/apparmor.d/` does it.
- Inside the runner's sandbox LibreOffice converts nothing, even with a
  writable profile, and a pandoc installed under `/home/linuxbrew` was not
  found. So the render case checks the .docx, and the pandoc flags and the
  PDF are checked by `tests/test_reference_docx.py`, which runs phase 2's
  render block as written.
- `--scaffold` lets the runner run `phase3-chat-es/scaffold.sh`, as you; it
  only copies the brief. Without it that case runs with no brief.
- The phase 3 case searches the real web, so its openings differ on every run.
  Its checks are about behaviour, not about which postings come back.
- The first run asks you to trust the plugin directory.
- Results land in `evals/results/`, which is not committed.
- A phase 2 run writes the continued session next to its `history.jsonl`,
  named after the session id; git ignores it.

The suite is not in CI: it costs money on every run and needs a credential.
Run it before a release that changes phases 1 or 2.
