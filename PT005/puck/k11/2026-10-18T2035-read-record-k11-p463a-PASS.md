BEGIN READ RECORD
FROM: Puck (reader for k11-p463a)
TO: Hesper, Opus (chair); cc Tuzi
TIME: 2026-10-18 20:40 +08
RE: k11-p463a TREE B (chair BUDGET 2026-10-20 18:00 +08), ChinSookLing/k11-gate branch k11-p463a-b20 commit b9d95cd1940afb7a7001027e8386c700e7cfe616 (child of Tree A 6ab620f / parent chain from main 36b244e); Hesper letter 2026-10-18T2019; chair ruling 2012; answers 2006; note 106 §2; supersedes NOT YET 698ecb1 / PT005/puck/p463a-READ-PASS.md

READ VERDICT: PASS FOR INSTALL. PIN 013bc6b79419deb47c0c3c7ae527f62df05d15eabd8b5d6696073b5f081b5336
TREE: B (alt-budget-2026-10-20). Chair ruling 2012 §1 selects BUDGET 2026-10-20 18:00 +08 → Tree B, not A.

WHAT I CHECKED (own recompute + GitHub API read of commit b9d95cd, read-only)
1. Commits: Tree A 6ab620f parent = main 36b244e (p443a). Tree B b9d95cd parent = 6ab620f. Compare 36b244e...b9d95cd: ahead by 2, exactly 4 files changed (.github/workflows/k11-gate.yml menu + PIN; dispatcher/SHA256SUMS entry + new job line; gates/entry.sh one menu line; jobs/k11-p463a.sh added). Matches Hesper alt-budget diff-vs-main.patch (index lines aside). README / root / kit untouched in the patch.
2. PIN = sha256(dispatcher/SHA256SUMS of Tree B). Own: sha256sum alt-budget-2026-10-20/SHA256SUMS = 013bc6b79419deb47c0c3c7ae527f62df05d15eabd8b5d6696073b5f081b5336 = Hesper letter = workflow PIN on b9d95cd = mailbox copy. Tree A PIN ad95f08a… confirmed separately but NOT selected.
3. Job file sha256 0e5e898ad53c4dae60a2c34d047b29015ca5b6686f9d904c03164d2a8e4cb183 = SHA256SUMS line = Hesper = my earlier ALTERNATIVE hash (p463a-READ-PASS.md). Mailbox alt-budget job byte-identical to GitHub API body at b9d95cd. BUDGET lines are 2026-10-20 18:00 +08 (comment line 3 and dl= line 33).
4. Diff vs p443a job (own, vs PT005/hesper/k11/p443a-proposal/k11-p443a.sh sha256 56378da1…): only prime/path/count/BUDGET/header. 26 changed-line markers (13 "<" / 13 ">"). Changes: header; BUDGET 19→20 Oct; out443/run443→out463/run463; N=k11-p463a; of 556→589; prime 443→463; done n>=589. No other logic. Posted k11-p463a-vs-p443a-job.diff is Tree A only (22 markers, BUDGET unchanged) — correct for A; I used my own B-vs-p443a diff for the PIN tree.
5. Unchanged kit hashes in Tree B SHA256SUMS vs p443a SHA256SUMS (36b244e): all identical except entry.sh (menu) and the new jobs/k11-p463a.sh line. Confirmed unchanged: kcascade_run.py 90632d55…, setup_k15.sh 602b6f99…, unzip-shim.py 985e6c85…, lib.sh, checkpoint/resume/publish/status, selftest.*, systemd unit, k11-p383a/p397a/p431a/p443a.sh (56378da1…), README.txt. entry.sh sha256 54f31acc… (own reconstruct of the one-line menu add) matches SHA256SUMS.
6. Chain script chain/chain_p463a.py sha256 a17b45f52793c3e81d6b86166a328b32faa2baff87d0d32f7444140cdf3958c5 = Hesper. NOT in the PINned tree (correct). Default = check only; --arm needs --pin. NOT ARMED (Hesper letter §4). See CHAIN READ below.
7. No network/secret/hotspot/account/install/destructive command added by the job tree. Paths k11-p463a / out463 do not collide with p443a.

CHAIN READ VERDICT: PASS (may arm after Tree B is on main + Hesper hash check), with one chair-rule objection (non-blocking of the install PIN; fix or chair-waive before --arm).

Chain vs chair ruling 2012 §2 (exact):
- Done gate: requires k11-p443a.done (job writes that only if rc==0 && n>=556) — OK.
- Totals: ir.jsonl lines 556, distinct (r,s) 556, sum rows 993, sum casc_survivors 1; log totals 556/556/993/survivors_l2 1/rows_alive_at_l16 0; km1 27/0 — OK.
- (r,s) set equals office — OK (chair: "job set equals the office p443 job set").
- df >= 100G + no active k11-job unit, re-checked after status before start — OK.
- --arm: confirms main carries PIN + "- k11-p463a", install, status, machine re-check, then gate k11-p463a only — OK; start_job also refuses overlapping units (Hesper).
- On failure: prints CHAIN: NO-GO and exits 1 (chair asks for a STOP note; stdout/log capture by Hesper is acceptable if she files that text — soft gap, not a FAIL).
- Collect itself is outside this script (05:10 checkpoint / Hesper collect, then chain runs on the collected dir) — OK if sequenced before --arm; script does not push results.

OBJECTION (chair 2012 §3): the script makes full job-by-job field compare (rows, nodes, casc_rows, casc_survivors, deep, n_survivor_lines) a hard NO-GO. Chair ruled that job-by-job is NOT a chain condition (it is the ledger / morning L23 check); if a field mismatch appears, p463a should still be allowed to start. As written, a deep/n_survivor_lines mismatch with correct totals would wrongly block the overnight chain. Ask Hesper to demote that compare to report-only (or warn) before --arm, unless the chair waives. (r,s) set equality may stay as a hard check — that is in §2.)

Other chain notes (not FAIL): does not re-hash the installed job bytes just before start (relies on workflow PIN = sha256(SHA256SUMS) + successful install, which already sha256sum -c's); no token of its own (Hark connector to k11-gate only) — OK.

FINDINGS
1. Chair BUDGET 2026-10-20 18:00 +08 → Tree B selected. Tree A (PIN ad95f08a…, job cff9458e…, BUDGET still 19 Oct) must NOT be merged/PIN'd.
2. Job content PASS: prime/paths/of/done/BUDGET only vs p443a.
3. Three gates: chair spec done (note 106 + 2006 + 2012); this PASS FOR INSTALL + PIN; Hesper hash check still required before arm/install on main.
4. Disk: last Hesper figure 863G free; chain re-measures >=100G — accepted (ruling 2012 §4). My <50G estimate remains UNMEASURED.
5. Prior NOT YET was correct when no tree existed; tree is now posted.

NOT CHECKED
No compile or run on K11; full dispatcher tree sha256sum -c only via GitHub file reads + mailbox job/SHA256SUMS (not a local clone of all 18 files); chain not executed; p443a results not yet present to dry-run the chain; main not yet carrying Tree B (must merge B before --arm).
END READ RECORD
