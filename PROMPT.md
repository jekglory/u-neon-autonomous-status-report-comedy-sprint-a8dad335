# Dispatch brief — Status Report Comedy Sprint

Build + submit a make.fun one-line bounty entry. Bounty: "Status Report
Comedy Sprint", slug u-neon-autonomous-status-report-comedy-sprint-a8dad335,
prize $5 (top 3 share it), entries close 2026-11-25T10:25:00Z, result due
2026-12-17T14:25:00Z, published 2026-11-24T10:22:01Z. Brief: one line, at
most 200 characters — the funniest thing an AI agent would say in its
weekly status report to its human. Judge compares pairs on funny, fresh,
agent-true. No entry fee, program/v1 harness, blind rounds (3).

Rules (non-negotiable):
- make.fun account @gentle-owl-26, reward wallet
  8rCWeWgLhbrjRJnW3sLDfPBVLR481kFnoGVsghPPCJjG. API key ONLY via command
  substitution from ~/workspace/makefun/register-result.json field `key` —
  NEVER print it or write it to any file. Keypair
  ~/workspace/makefun/makefun-keypair.json (mode 600). gh CLI is logged in
  as jekglory — do NOT log out.
- Reread ~/workspace/custom-skills/code_bounty_submission_gate/SKILL.md
  FIRST and follow it exactly.
- Entry must be PURE STDLIB Python (no Pillow, no numpy, no third-party
  packages). main.py prints the single line. TEST locally twice,
  byte-identical output, before submitting.
- Build in ~/workspace/makefun/u-neon-autonomous-status-report-comedy-sprint-a8dad335/,
  public GitHub repo
  jekglory/u-neon-autonomous-status-report-comedy-sprint-a8dad335 (MIT,
  created AFTER the competition opened 2026-11-24T10:22:01Z), commit +
  push. WARNING: GitHub repo creation hit "too many repositories, too
  quickly" earlier today (jekglory created 42 repos on 2026-11-24 UTC) —
  if creation is refused, retry with backoff for up to ~30 min; if it
  still fails, leave the build dir + CHECKPOINT.md and report back.
- Bundle transcripts with the kit CLI (node cli/makefun.mjs bundle, Muse
  app sessions + --muse-usage), run the kit `check` on the exact bundle.
- IF check is 0 FAIL: SUBMIT directly via the kit CLI (no confirmation —
  Adam ordered this). Verify the live stage afterwards. Record the
  submission ID AND the claim code in
  ~/workspace/makefun/submissions-2026-11-13.md (claim codes live ONLY
  there, never in chat).
- IF the check FAILS: fix what is fixable; if it cannot be fixed, do NOT
  submit (refused attempts count toward quota) and report the exact
  failures. EXCEPTION: if the ONLY failure is thinking_priced (0 usage
  rows — subagent usage rows are written on run completion), do NOT
  submit; report back with the bundle path/sha and check output so the
  parent can re-bundle with usage rows from muse.db and submit.
- NEVER claim any prize. Claiming needs Adam's explicit permission.
- Write a CHECKPOINT.md in the build dir with the entry text, sha256 of
  output, repo, commit, and any weaknesses.
- Report back: bounty name, prize, deadline, submission ID, check tally,
  repo URL, commit sha, entry text.
