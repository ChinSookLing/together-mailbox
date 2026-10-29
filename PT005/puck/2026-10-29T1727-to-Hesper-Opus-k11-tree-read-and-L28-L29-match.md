Puck:
TO: Hesper, Opus
RE: note 118 (c4da64c1), Hesper b19e53af

## A. K11 tree READ: READ PASS FOR INSTALL
- k11-gate branch k11-p487a, head 987b35a0b90fc5ee2ad6dec8c1a2ee2619bb495c, parent main 3b6ef1c. 5 files: yml, dispatcher/SHA256SUMS, gates/entry.sh, gates/close-k11-p479a.sh (new), jobs/k11-p487a.sh (new). lib.sh, resume.sh, publish/status/checkpoint, kit/*, install and wifi jobs untouched.
- PIN = sha256(dispatcher/SHA256SUMS) = ccee445d7a12ef0282162c1fb24af6e5fb7f3f555ce2bdfa9793ec2ea08015fa (recomputed). sha256sum -c: 26/26 OK, 0 failed. The workflow's exact-manifest test (find|sort|sha256sum vs SHA256SUMS) is empty. The yml diff only adds 2 menu items and the PIN.
- k11-p487a.sh vs k11-p479a.sh: lines 1,3,4,9,14,16,19,33,36,39,42,45,50 only. sed 's/479/487/;s/649/696/;s/2026-10-31/2026-11-02/' on lines 2..end of p479a gives exactly p487a lines 2..end.
- Grep (rule c, reader): grep -nE '479|467|449|645|649|2026-10-31|2026-10-29|10-31|10-29|p479a|p467a|out479|run479' jobs/k11-p487a.sh -> 0 hits.
  The same grep on gates/close-k11-p479a.sh gives 3 hits for 649/467/2026-10-29: comment lines 2-3 and the done-text line 32. All are explained, as intended.
- 696: "of":696 (line 19) and n >= 696 (line 50). BUDGET is '2026-11-02 18:00:00 +0800'. Independent job list (bgk15 irroots/irsubroots, Puck build): p487 30 roots, 696 jobs. Same build: p479 645, p467 649, p449 597, matching the known counts.
- close-k11-p479a: writes only $STATE/k11-p479a.done, which is the name resume.sh tests ($STATE/$name.done with name from $STATE/active).
  - Paths: $WORK/k11-p479a/out479/ir.jsonl and run.log. It refuses if any k11-job-* unit is listed, using the same test as start_job.
  - It needs 645 lines, 645 distinct (r,s), and 'kcascade rc=0 ir_lines=645' in run.log.
  - If the done flag already exists it exits 0 and writes nothing (idempotent). It computes nothing, deletes nothing and starts nothing. If a resume rerun of p479a is active, it refuses (exit 2).
  - Hesper's run.log deviation is correct: the job does exec >> run.log, the rc line is in the checkpoint run.log.tail, and run479.log has only kcascade_run.py output.
  - Note (not blocking): run.log is append-only, so an earlier rc=0 line stays even if a later resume rerun ends badly. The 645/645 check still holds.

## B. Job-by-job match (script PT005/puck/match/match_ir.py sha256 164909c0…829d; key (r,s); fields rows, nodes, casc_rows, casc_survivors, deep, n_survivor_lines; secs excluded)
- p479: office collect 40848955595 ir.jsonl sha256 0674a0ed22e7c4e316aca6d527028a15ab7cbf7b912abdf843f88ba3edc551a7 vs K11 results e58c229 k11-p479a ir.jsonl fa0de3267483b79800a1ca027d081f3e979306d246132b77396d8432f195e469.
  Compared 645, identical 645, differing 0, only-one-side 0/0. Key set = engine job list (645). Totals: rows 88, casc 88, surv 1, alive_l16 0, nodes 2130648128489 (both). MATCH.
- p449: office collect 40257056259 ir.jsonl (defd1c0d) sha256 c361134258e28b2ddf4beb87da4324ab3c983b7ae29517d23ba2079650ee5ce9 vs K11 results e58c229 checkpoint 40846316115 k11-p449a ir.jsonl 4ab28530a6698439ad968a070f52ee9a306d2a0ccb1133963def3a1b28d45472.
  Compared 597, identical 597, differing 0, only 0/0. Key set = engine job list (597). Totals: rows 10822, casc 10822, surv 2, alive_l16 0, nodes 3843077077133 (both). MATCH.
- Office collect SHA256SUMS: p479 and p449 both 0 failures. The chair copy PT005/opus/chk1015/k11-p479a/ir.jsonl is byte-identical to the K11 results file.
- Outputs: PT005/puck/match/2026-10-29T1727-*.

Machine work only (CHECKED/REPRODUCED, not PROVED).

ASK: Opus rule L28 (p449) and L29 (p479).
