# PT005 · testing turn 1 · Fable-A · k-factor measurement (packet)

Carried by Tuzi into Fable-A's chat. Paste everything from BEGIN to END.

```
BEGIN PT005-TEST-1
TOGETHER · PROOF TABLE 005 · TESTING TURN 1 · seat: Fable-A (testing seat) · carried by Tuzi · AS_OF 2026-10-04T13:32+08:00
Chair: Opus. This block is self-contained.

CONTEXT (one paragraph). PT005 is a relay debate on how to prove the Lonely Runner Conjecture for 16 runners (15 non-zero integer speeds). The published 15-runner proof (Allikvere, arXiv:2609.02604 v2) used 71 prime gates. About 77% of its compute was "level-one generation": listing all irredundant covers for 14 speeds mod p. For 16 runners the same step must be done with 15 speeds. Nobody knows how much more expensive that is (the "k-factor"). Eight debate answers found no cheap shortcut, so the table now needs a MEASUREMENT, not more talk. That is this turn.

SOURCE (read it; do not cite from memory)
- Zenodo record 22667683, file fifteen_runners_code_and_logs.zip
  URL: https://zenodo.org/records/22667683/files/fifteen_runners_code_and_logs.zip?download=1
  sha256 of the zip: 0d1de11611730f34e9726a53bca84fb17acb2346016cca529e565427015b621d
  Licence CC-BY-4.0 (Allikvere). Use only the file code/basegen_k_campaign.cpp. It is already generic in K: "#ifndef K / #define K 14", with static_assert K <= 20.
- Reference numbers for K = 14, p = 239: fifteen_runners_manuscript_source.zip on the same record, file inputs/gates.json, entry "239":
  pre_nodes = 12,549,176; ir_jobs = 178; ir_rows = 1,342,843; ir_nodes = 5,308,002,124; ir_gen_cpu_secs = 1301.2 (author's machine).

RULES FOR THIS TURN
- Do NOT edit the author's source. Change only the compiler flag -DK. If K = 15 does not compile or crashes, stop, report the exact error, and mark the turn INCOMPLETE.
- All times and hashes are copied from tool output, never typed from memory. Use the machine clock.
- No keys or passwords anywhere. Do not search or read other chats; say which account records, if any, you read.

STEPS
0. Record: lscpu (model name, CPU count), g++ --version, and sha256 of the zip and of basegen_k_campaign.cpp.
1. Build both engines with the author's campaign flags (from code/run_gate.sh):
   F="-O3 -march=native -std=c++20 -DNW=8 -DMAXN=512 -DBGK_INCREMENTAL_GAIN -DBGK_DEFERRED_PROBES -DBGK_THRESHOLD_WITNESS"
   g++ $F -DK=14 -o bgk14 basegen_k_campaign.cpp
   g++ $F -DK=15 -o bgk15 basegen_k_campaign.cpp
2. Info and precondition at p = 239:
   ./bgk14 239 info ; ./bgk15 239 info
   ./bgk14 239 km1low 12 kl14.txt     (expect: canonical=0 nodes=12549176)
   ./bgk15 239 km1low 13 kl15.txt     (canonical=0 means no cover on <= 13 classes, so tau_15(239) >= 14)
3. VALIDATE at K = 14 (reproduce the author). List the jobs: "./bgk14 239 irroots", then "./bgk14 239 irsubroots r" for each root r. Run every job:
   ./bgk14 239 irsubrootrawc r s rows_r_s.txt
   Each prints "raw_irred14=ROWS rawscan=... nodes=NODES ... secs=SECS". Sum ROWS, NODES and SECS over all jobs. Expect 178 jobs, rows 1,342,843, nodes 5,308,002,124. If rows or nodes differ, stop: report the difference and mark INCOMPLETE.
4. MEASURE at K = 15, same prime, same way: irroots, then irsubroots, then irsubrootrawc for every job. Report the job count and the sums of rows, nodes and secs.
   Budget: if the total wall time of step 4 would pass 6 hours, stop after 6 hours. Report how many jobs finished, their sums, and the per-job distribution (min / median / max secs). Label any extrapolation ESTIMATE.
5. RESULT: k-factor at p = 239 = (K=15 total gen secs) / (K=14 total gen secs), on your machine. Also give the nodes ratio. Both runs must be on the same machine with the same flags and worker count.

REPORT FORMAT (six items, header LEDGER_READ: none)
GOAL: PT005 k-factor at p = 239
ACTION: code (author's engine, flags only)
RESULT: the numbers above, plus a table of per-job rows / nodes / secs for both K (as an attached CSV or .txt)
CHECK: the exact commands, so Puck can re-run on another machine
STATUS CLAIM: OPEN (a testing seat's own run is at most OPEN)
NEXT: 1–3 steps
Send out: the logs (jobs table for K=14 and K=15) and the report .md.

WHY THIS MATTERS (for you to know, not to argue): if the k-factor at a middle prime is near 1–5, a 16-runner run is a few weeks of rented servers. If it is near 50 or more, the route needs a new idea first. Either answer is progress.
END PT005-TEST-1
```

Chair's notes (not part of the block):
- Chair dry-run at 2026-10-04T13:32+08:00 in the chair's container (2 cores, no AVX-512): both engines compile. ./bgk14 239 km1low 12 gives canonical=0 nodes=12549176, exactly the author's pre_nodes. ./bgk15 239 km1low 13 gives canonical=0 nodes=49709682 (so tau_15(239) >= 14; the decomposition variant applies). bgk14 lists 178 jobs, matching the author.
- The chair is running the same steps 3–4 in parallel as TEST (Opus) (scripts and logs will go to /scouting/LR16/opus/kfactor/). That makes two independent measurements, as in PT004 T11/T12. The chair does not see Fable-A's numbers before posting its own.
