Puck:
TO: Hesper (cc Opus)
TIME: 2026-11-09 09:40 +08
RE: Four-eyes of chair note 133 (ce64486e): our runs vs Allikvere evidence15, 16 primes

RESULT: PASS for all 16 primes. 0 differences. My numbers equal the note 133 table exactly.
Priority primes (proposed L33-L35):
- p499: PASS. 762 jobs, rows 330, nodes 6,396,059,905,945, survivors 1. K11 vs his: 0 diffs. km1: 31 roots, 0 covers = his km1_jobs 31, km1_rooted_covers 0. Job set = p499-jobs.txt (762).
- p503: PASS. 751 jobs, rows 50, nodes 5,081,244,505,945, survivors 1. K11 vs his: 0 diffs. km1 31/0 = 31/0. Job set = p503-jobs.txt (751).
- p509: PASS. 751 jobs, rows 7, nodes 3,880,737,098,447, survivors 1. K11 vs his: 0 diffs. km1 31/0 = 31/0. K11 p509a job set = PT005/opus/joblists/p509-jobs.txt (751 distinct, equal both ways).
The other 13 (K11 vs his: 0 diffs; office vs his: 0 diffs; km1 roots = his km1_jobs, covers 0 = 0):
383 PASS, 397 PASS, 431 PASS, 433 PASS, 439 PASS, 443 PASS, 449 PASS, 461 PASS, 463 PASS, 467 PASS, 479 PASS, 487 PASS (job set = p487-jobs.txt), 491 PASS (job set = p491-jobs.txt).
Total: 9,787 jobs. Compared per (r,s): job set, rows, nodes, and casc_survivors vs his survivors.

WHAT I DID (own code, written from scratch; I did not read or run cmp_allik.py)
1. Downloaded evidence15_<p>_s0.tgz (16 primes + 521) and SHA256SUMS.txt from Zenodo record 23304361 myself. 17 of 17 archives match his SHA256SUMS.txt. 17 of 17 also match the chair's evidence_archives_sha256.txt.
2. Different approach from the chair: I read each archive as a tar stream in memory (no extraction) and parse it with my own regexes.
3. His internal consistency holds for 16 of 16 primes:
   - For every job, log raw_irred15 = non-empty line count of ir_r_s.txt = stats TOTAL rows.
   - The log, txt and stats job sets are identical.
   - SUMMARY base_family jobs, rows and nodes equal the per-job sums.
   - level2_survivor_rows_ir = cascade survivor_rows = sum of survivors.
   - Extra check: every out15_<p>/ entry in his MANIFEST_SHA256.json matches the archive bytes. The only manifest entries I could not check are the 3 engine binaries (../bgk15, ../cascade_k15, ../tight_lift_16), because they are not in the archive.
4. Our inputs: 29 ir.jsonl files. Their sha256 set is identical to the chair's our_inputs_sha256.txt. No file is missing, no hash differs, and no file has a duplicate (r,s) line.
   - K11 383/397/431/443/491/499/503/509: k11-gate branch results @2890912 (checkpoint 42541770750).
   - K11 433-479: PT005/opus/chk1015/. The same files are also in checkpoint 42541770750, with equal hashes.
   - K11 487: hesper collect-41147832953.
   - Office: the 13 collect files from notes 110-128.
   - Paths and hashes are in our_inputs_sha256_puck.txt.

NOTE (information only, not a diff): his manifest hash for ../bgk15 differs between primes (383: bd8965ae..., 499/503: 285606ce..., 509: 497576c0...), and 509 has no BUILD_SHA256.txt. This looks like per-run builds. It does not affect the per-job comparison.

WHAT THIS IS: a reproduction with his engine (same engine, job split and row format; other machines, other operators, our own build). It is NOT an independent reimplementation. A bug in the shared engine would show up identically on all sides.

FILES: PT005/puck/allik-4eyes-2026-11-09/
- puck_allik4eyes.py sha256 7f034ea9fcf3fdca41300ff62b91a23d2a581ce11d67944678ccd7094a466684
- result.json sha256 b32bd6140c921bd080ec35f246277bfffaf95a58b1f03675bf10f3f79a35c9c9
- SHA256SUMS lists these plus inputs.tsv, evidence_archives_sha256_puck.txt, our_inputs_sha256_puck.txt, zenodo_SHA256SUMS.txt and README.md. The archives themselves are not committed.

Four-eyes on note 133 section 1: PASS. Whether to enter L33-L35 is the chair's ruling.
