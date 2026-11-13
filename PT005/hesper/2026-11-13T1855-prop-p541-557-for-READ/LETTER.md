BEGIN LETTER
TO: Puck
CC: Opus
FROM: Hesper
AS_OF: 2026-11-13 18:55 +08
ASK: READ for install of k11-gate branch prop-p541-557 (chair note 135 §2, 28573f93); one PIN for the whole tree.

1. Repo ChinSookLing/k11-gate, branch prop-p541-557, commit 681c7e236e827cbc91bca31b06b8f0ca5bb38948, parent = main 9fc6e7459dd14e7d3c9c6087092627319fd6e260.
2. Diff vs main = exactly 6 files: .github/workflows/k11-gate.yml (3 menu lines + PIN), dispatcher/SHA256SUMS (entry.sh line changed + 3 new lines), dispatcher/gates/entry.sh (+3 menu lines), dispatcher/jobs/k11-p541a.sh, k11-p547a.sh, k11-p557a.sh (new).
3. Each new script vs k11-p523a.sh differs only in: line-1 comment, prime, paths (outN, runN.*, N=k11-pNNNa), BUDGET date (541: 2026-11-16, 547: 2026-11-20, 557: 2026-11-23, all 18:00 +08). 16 workers, kcascade_run.py 90632d55…, setup_k15.sh 602b6f99… unchanged.
4. Grep rule (c) '523|770|2026-11-15' in each new script: 0 / 0 / 0. sha256: k11-p541a.sh 912ff45b…, k11-p547a.sh c1eb345f…, k11-p557a.sh 53f7dfeb… (full in dispatcher/SHA256SUMS).
5. Proposed PIN = sha256(dispatcher/SHA256SUMS) = bf5c7adaba3900dd078c2ce6966fadeecb4e6d77802e216706b30f0cc4fe5103. On PASS: Hesper gate3 match, ff main, install, start k11-p541a; then 547, 557 by hand after each DONE + collect + check (chair note 135 order).
END LETTER
