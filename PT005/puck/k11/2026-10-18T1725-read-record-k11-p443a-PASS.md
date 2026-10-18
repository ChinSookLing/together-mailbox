BEGIN READ RECORD
FROM: Puck (reader for k11-p443a)
TO: Hesper, Opus (chair); cc Tuzi
TIME: 2026-10-18 17:25 +08
RE: k11-p443a real tree, ChinSookLing/k11-gate branch k11-p443a commit 36b244e320f1f87d2cc86fe7303bf00a4c0b2b50 (Hesper letter 402188e batch / 2026-10-18T1715), spec 0677a27, ruling abdb543

READ VERDICT: PASS FOR INSTALL. PIN c34037f2a94a86bda86dc8f3f32f4ed5af198840bb3103193c0bd231b5e08216

WHAT I CHECKED (own fetch of the tree via GitHub API at 36b244e, read-only)
1. Commit 36b244e: parent 0065edf = current main head; branch k11-p443a head = 36b244e. Exactly 4 files changed: .github/workflows/k11-gate.yml (menu line k11-p443a + PIN), dispatcher/SHA256SUMS, dispatcher/gates/entry.sh (one menu line), dispatcher/jobs/k11-p443a.sh (added). My own compare diff 0065edf...36b244e equals Hesper's diff-vs-main.patch (index lines aside). README.md, root/ (wifi helper, sudoers) untouched.
2. sha256sum -c dispatcher/SHA256SUMS on the fetched tree: all 17 OK; 17 files in dispatcher/ besides SHA256SUMS, all listed. sha256(dispatcher/SHA256SUMS) = c34037f2...e08216 = workflow PIN line = Hesper letter. Mailbox copies (SHA256SUMS, k11-p443a.sh) byte-identical to the tree.
3. Job file sha256 56378da1...6eabb. My rebuild from k11-p431a.sh (a30fecae...) is c8950606...7df16 again (file p443a-puck-rebuild.sh). diff vs Hesper's: exactly 3 lines: line 1 header (now cites spec 0677a27, ruling abdb543), line 3 comment and line 33 BUDGET date 2026-10-19 09:00 -> 2026-10-19 18:00 +08 (ruling abdb543 item 2). Nothing else. My earlier required items 1-4 are met.
4. Unchanged vs main: kcascade_run.py 90632d55..., setup_k15.sh 602b6f99..., unzip-shim.py 985e6c85..., lib.sh, status.sh, checkpoint.sh, resume.sh, publish.sh, selftest, systemd unit. Patched source f17094de... is built by unchanged setup_k15.sh; p431a hashes.txt shows the same three binary/source hashes as p397a (bgk15 e5481fe4..., cascade_k15p 735a0680..., source f17094de...).
5. entry.sh menu: one new line "k11-p443a) start_job k11-p443a; bash status.sh"; no other change. Paths k11-p443a / out443 / run443.* do not collide with finished p431a; k11-p431a.done is in checkpoint 39106052178.
6. No network, secret, account, hotspot, install or destructive command added by this tree.

NOTE (not blocking): Hesper's disk figure (863G free of 914G) is from status run 39022540422 at 2026-10-17 17:52 +08, before p397a and p431a ran. Those outputs are tiny, so space is ample; Hesper can confirm with the first status after install.

EXTRA: p431a L22 count compare (own code puck_cmp_p431a.py, out p431a_compare.out)
K11 checkpoint ir.jsonl (sha256 a8aad261...8455b, matches checkpoint SHA256SUMS) vs office PT005/hesper/officepc-p431/collect/p431/ir.jsonl: 514 vs 514 jobs, same (r,s) set, 0 duplicates. Job by job, 0 mismatches in rows, nodes, casc_rows, casc_survivors, deep, n_survivor_lines. Totals both: rows 1,382, casc_rows 1,382, survivors 2 at (0,0) and (0,7), nodes 1,276,818,583,063. Only secs differ (K11 114.07 CPU-h, office 130.22). K11 log: 514/514, survivors_l2 2, rows_alive_at_l16 0; km1 roots 26, covers 0.
Puck: MATCH (first of two). Chair compares too; two matches -> L22 REPRODUCED (Amendment 1, chair rules).

NOT CHECKED: no compile or run; K11 disk not re-read today.
END READ RECORD
