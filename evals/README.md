# Evals

Behavioural checks for phases 1 and 2, run with `claude plugin eval`. The tests
in `tests/` check the files; these check what an agent actually does with them.

| Case | Starts from | Checks |
|---|---|---|
| `phase1-audit-es` | a Spanish request with an English CV pasted in | the skill fires; the audit is in Spanish; no invented figures; no question about Chrome; no unsourced statistic |
| `phase2-rewrite-es` | the audit done, the applicant's answers | the rewrite is shown for approval before anything renders; plain-hyphen date ranges; Spanish; only the figures the applicant gave |
| `phase2-render-es` | the rewrite approved | a toolchain probe before the render; pandoc without smart typography; .docx and .pdf produced; confirmed facts in the brief; the close in Spanish |

The phase 2 cases resume a scripted conversation (`history.jsonl`). Edit the
turns in `make_histories.py`, never the transcripts, and regenerate them:

```bash
python3 evals/make_histories.py
python3 tests/test_evals.py      # free: the transcripts and the case files are well formed
```

## Running

Every run is a full Claude Code session on your own account, and each case runs
three times. Cap the spend:

```bash
claude plugin eval . --ablation none --allow-tools Bash Write Edit --max-cost-usd 8
claude plugin eval . --ablation none --case 'phase1-*' --max-cost-usd 2   # phase 1 only
```

- `--ablation none` skips the no-plugin baseline, which would double the runs.
  These checks are absolute, not a comparison.
- The phase 2 cases need Bash, which the runner only grants inside its sandbox:
  on Linux that needs `bubblewrap` and `socat`. Rendering also needs pandoc and
  LibreOffice, as in `tests/test_reference_docx.py`.
- The first run asks you to trust the plugin directory.
- Results land in `evals/results/`, which is not committed.

The suite is not in CI: it costs money on every run and needs a credential.
Run it before a release that changes phases 1 or 2.
