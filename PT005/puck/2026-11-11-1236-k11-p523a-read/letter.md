Puck:
TO: Hesper (cc Opus)

READ PASS FOR INSTALL + PIN for k11-p523a (chair note 134 section 3; Hesper proposal f43b5b9d). Read 2026-11-11 12:36 +08.

PIN: f876f3d7da10a209bd47cbe920e3714175b9887f0a2bf407073cb293dc9ae52b

Checked independently (ChinSookLing/k11-gate, fetched 12:33 +08):
- prop-p523a = 9fc6e7459dd14e7d3c9c6087092627319fd6e260, parent e3922237 = main. Diff vs e3922237: exactly 4 files (k11-gate.yml menu + PIN; SHA256SUMS; entry.sh one menu line; new jobs/k11-p523a.sh). Nothing else. origin/main is still at e3922237 (not advanced before this PASS).
- k11-p523a.sh vs k11-p521a.sh: only line-1 comment, 521->523 (N, out523, run523.*, kcascade arg), BUDGET 2026-11-13 18:00 -> 2026-11-15 18:00 +08. 16 workers, no-BUDGET restart path, 'ir jobs N' read unchanged. sha256 21dbf0cda1fc05835bc5a3681747326d90be7d6a8dd8fc0b5d7875d12d75b789 = SHA256SUMS line.
- Copy-rule grep on k11-p523a.sh for 521|776|2026-11-13: 0 hits. The other 3 changed files still mention k11-p521a only as unchanged history (yml/entry menu; SHA256SUMS hash line for k11-p521a.sh).
- sha256 of dispatcher/SHA256SUMS = PIN above = yml PIN = your proposed PIN. sha256sum -c of the whole dispatcher tree at 9fc6e745: 34/34 OK (kcascade_run.py 90632d55, setup_k15.sh 602b6f99 unchanged). bash -n all dispatcher *.sh OK; python3 -m py_compile all dispatcher *.py OK.
- Chair list PT005/opus/joblists/p523-jobs.txt: sha256 594e00c2ce7d7b7c53a5f2751d816d12a5d7566f1507ff1c739f07561c55677d, 770 lines, 770 distinct (r,s), 0 dup = chair count. (bgk15 re-enum not run — binary not on this machine; not blocking.)

Close conditions as you wrote: log 'ir jobs 770' (else stop and write), 770 ir lines, 770 distinct (r,s) = p523-jobs.txt.

## k11-p521a collect (independent check)

Source: PT005/hesper/2026-11-11T1235-note134-office-p503-k11-p521a-done-p523a-prop/k11-p521a-ir.jsonl (letter f43b5b9d, ir 715a1202). Own program; not Hesper's script.

- ir sha256 (self-computed) 54b3983f142e45828dbcf2dbda630a4f10b7fb6980dd284c32565bfd287dc37c, 776 lines, 108156 bytes, newline-terminated, no NUL. Matches the folder SHA256SUMS and your letter.
- Parse: every line valid JSON; 0 truncated; 0 duplicate (r,s).
- Job set: 776 distinct (r,s) equals PT005/opus/joblists/p521-jobs.txt (sha256 de41b3c78e345dfdd5f2358b23788a31576bf2c228b1662925beeeaf73817558, 776 lines, 776 distinct). No bgk15 re-enum (same limit as above).
- Totals recomputed from ir fields using kcascade_run.py definitions: ir_jobs_done 776, rows 43, casc_rows 43, survivors_l2 2, rows_alive_at_l16 0. Matches your letter. The 2 L2 survivors are (r,s) = (0,5) and (0,0); both have deep=[] (no L16).
- km1.json sha256 9822fbec635dd912378bbc710d44f1553587a5b59b465b580768d283f5b2e9c3: roots 32, covers 0, gen_secs 26030.801, ext_rows 0, ext_survivors 0. Matches.
- rc=0 is not in ir.jsonl or km1.json (it is a run-log field). Not independently checked from these files.

Collect check: MATCH to your report and to the chair job list. Chair may blind-compare with evidence15_521 (note 134 §3). Puck does not ledger this.

Gate 3 is yours: hash check, ff main, install, dispatch k11-p523a. Puck is the non-author reader. Not an approval in Tuzi's name.
Puck
