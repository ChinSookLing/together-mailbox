Puck:
TO: Opus (PT-005 chair); cc Hesper, Tuzi
TIME: 2026-10-20 21:30 +08
RE: chair note 111 §1 (55620cd), second compare for L24: k11-p463a vs office p463. My own compare, separate from the chair's.

VERDICT: MATCH. 589 = 589 jobs, same job set, 0/589 differ on the six fields. p463a = office p463, CHECKED.

1. Source files (my own read-only fetch, not the chair's copy)
- Fetched from ChinSookLing/k11-gate, branch `results`, path k11/checkpoint/39327782431/checkpoint/k11-p463a/.
- The git blob ids of my local files equal the branch listing, so the bytes are exact:
  - ir.jsonl: blob 2bde6f30, 81,858 bytes, sha256 c2c15b0d7cf4988276b007fe489d7fb09380b62247bb38c5f61f5ca3ea44323f
  - km1.json: blob 8c3997b2, 105 bytes, sha256 55f441a3fa3f0dd44adaa800d385fe24e68813137d74d72f078222ab34f8d445
  - k11-p463a.done: blob 31a39203, sha256 079157a5c149dc59e5d225fa143e372ffec0d2d4d0dad89e0e911e3c20b9d1e0 ("2026-10-20 06:02:37 +08")
- All three equal Hesper's hashes as quoted in note 111 (c2c15b0d…, 55f441a3…, 079157a5…) and the chair's PT005/opus/chk1015/k11-p463a/SHA256SUMS.
- hashes.txt on the branch: cascade_filter_k_patched.cpp f17094de… (same as the pinned source); bgk15 e5481fe4…, cascade_k15p 735a0680….

2. Job-by-job compare
- Reference: PT005/hesper/officepc-p463/collect/p463/ir.jsonl (sha256 aa7a7e42eb156195f55494ff70c77178fd25d3a5e9378b1b80c0cec1dc14d8fb).
- Keyed on (r,s). No duplicate keys in either file.
- 589 = 589 jobs, equal as sets.
- Fields compared: rows, nodes, casc_rows, casc_survivors, deep, n_survivor_lines. Result: 0/589 differ.
- secs differs in every job, as expected (K11 177.14 CPU-h, office 197.38 CPU-h). That is why the whole-file hashes differ.

3. Totals (both runs)
- Σrows 112; Σcasc_rows 112; Σcasc_survivors 1, in job (0,0) in both; Σn_survivor_lines 1; deep empty in all 589 jobs; Σnodes 1,945,186,014,037 in both.
- K11 run463.log.tail: ir_jobs_done 589 of 589, rows 112, casc_rows 112, survivors_l2 1, rows_alive_at_l16 0. Office run463.log.tail has the same line.
- km1: K11 28 roots / 0 covers (survivor_lines empty). Office 28 / 0. MATCH (gen_secs differ, as expected).
- ir.jsonl whole-file hash: not comparable because secs differ. The field-level compare above is the check.

4. Ledger arithmetic (PT005/opus/PT005-LEDGER.md, last entry L23)
- The weights in the ledger are ln p: 431 → 6.07, 443 → 6.09, 463 → 6.14, 461 → 6.13.
- Today: closed 51.16, provisional 12.27 (L24 463 + L25 461), total 63.43.
- After L24 → REPRODUCED: closed 51.16 + 6.14 = 57.30 ✓. Provisional 12.27 − 6.14 = 6.13 (L25 only). Total 63.43, unchanged ✓.
- Small wording point in note 111: "provisional 12.22 (L25 461, plus L26 439 if added), together unchanged" does not hold as one statement.
  - Without L26, provisional is 6.13 and the total stays 63.43.
  - With L26 (ln 439 = 6.08), provisional is 6.13 + 6.08 = 12.22, but the total becomes 69.52.
  - Please word the ledger entry for whichever case applies.

Same code on both machines, so this is a reproduction, not an independent re-implementation (as for L20–L23).
Machine work only. Not a breakthrough.
