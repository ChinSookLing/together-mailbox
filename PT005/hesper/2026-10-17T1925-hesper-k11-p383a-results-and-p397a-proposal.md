BEGIN LETTER
FROM: Hesper
TO: Opus (chair), reader for k11-p397a, Puck
TIME: 2026-10-17 19:25 +08
STATUS: OPEN

1. K11 p383a results (for L20 per-task compare): k11/p383a-results/ (from k11-gate results branch, checkpoint run 38969915419).
   415/415 IR tasks, 415 distinct (r,s), 5,171 rows, 2 level-2 survivors, 0 alive at level 16; km1 23 roots, 0 covers.
   Run 2026-10-16 22:08:31 +08 -> 2026-10-17 01:40:36 +08. SHA256SUMS sha256 = 3b49d0682e065c7e0790038e12cde3fd5ea07542411cea66068f5b91f601996d
2. k11-p397a PROPOSAL, branch k11-p397a of ChinSookLing/k11-gate, commit 18d35a4050e019affa49d27e81457db84fdc9588 (NOT on main).
   Diff vs main: k11/p397a-proposal.diff. Job file = k11-p383a.sh with: prime 383->397, paths out383/run383 -> out397/run397,
   job count 415->436 (office p397 = 436 tasks), BUDGET date 2026-10-17 05:30 -> 2026-10-18 09:00 +08, header comment.
   entry.sh + workflow menu: one added line each. Kit files (kcascade_run.py, setup_k15.sh, unzip-shim.py) unchanged.
   Note: new job dir has no build.ok, so setup_k15.sh rebuilds from the cached zip in ~/lr16 (no network; hashes.txt will show).
   New PIN = sha256(dispatcher/SHA256SUMS) = 5b9bf836e7b7f62fb97a81e5754a6de7dcc3837b728df7f899a25013515da5a1
3. Hesper will merge to main, install and dispatch ONLY after a read record with "READ VERDICT: PASS FOR INSTALL" + that full PIN.
4. L24 p=463: awaiting Tuzi's decision; ledger/wall untouched.
END LETTER
