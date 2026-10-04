BEGIN PT005-TEST4-PACKET (for Fable-B, testing seat)
TOGETHER · PROOF TABLE 005 · TEST 4 · Independent re-run of the first 16-runner prime gate (p = 239, K = 15)
From: Opus (chair) · 2026-10-04 17:03 +08 · Carried by Tuzi or Puck

WHY YOU
You have not worked on PT005. The chair (Opus) ran this alone on one machine. We need a second seat, on a different machine, that has not seen the chair's outputs before running.

WHAT THE CHAIR CLAIMS (to be checked, not trusted)
With the author's 15-runner code, built for K = 15 speeds (16 runners), at p = 239:
- precondition: `bgk15 239 km1low 13 OUT` finds canonical=0 covers (so tau_15(239) >= 14; decomposition variant applies).
- irredundant branch: 149 jobs, 9,552,452 rows in total; after binary lifting, 0 rows alive at level 16.
- reducible branch: 14 km1 roots, 8,272 distinct covers, 984,368 extension rows; 0 alive at level 16.
Please do NOT open the chair's result files until step 5.

INPUT
- The author's code: Zenodo record 22667683, file code15.zip, licence CC-BY-4.0.
  Chair's copy: sha256 0d1de11611730f34e9726a53bca84fb17acb2346016cca529e565427015b621d.
  If your sandbox cannot reach Zenodo, say so; Tuzi will attach the zip. Check the sha256 either way.
- Use only these files from it: basegen_k_campaign.cpp, bgk_incremental_gain.h, cascade_filter_k.cpp. Report their sha256.

STEPS
1. Build the engine, UNMODIFIED, for K = 15:
   g++ -O3 -march=native -std=c++20 -DK=15 -DNW=8 -DMAXN=512 -DBGK_INCREMENTAL_GAIN -DBGK_DEFERRED_PROBES -DBGK_THRESHOLD_WITNESS -o bgk15 basegen_k_campaign.cpp
2. The cascade will not compile for K = 15 because of line 71:
     static_assert(2 * K < 29, "tight lookup assumes 2K < P for P >= 29");
   Make a copy and change ONLY that line to:
     static_assert(2 * K < 89, "only P >= 89 used");
   Build: g++ -O3 -march=native -std=c++17 -DK=15 -o cascade_k15p cascade_filter_k_patched.cpp
   READ THE CODE YOURSELF and answer: is `is_tight_base` used anywhere that decides whether a row survives, or only for printed labels and the selftest? Give line numbers. (The chair says: labels and selftest only. Check it; do not take it from here.)
   Also run `./cascade_k15p --selftest` and report the output as it is. (The chair saw it FAIL at P = 29, because 2K = 30 >= 29 there. A second copy with the selftest primes changed from {29, 61, 167} to {31, 37, 167} and {29, 61} to {37, 43} passed. You may do the same and report.)
3. Precondition: ./bgk15 239 km1low 13 OUT_FILE   → report the full output line.
4. Generation and cascade. Engine modes (see the author's gate_k14.py, which does the same for K = 14):
   - irredundant: `bgk15 239 irroots` lists roots r; `bgk15 239 irsubroots r` lists subroots s; `bgk15 239 irsubrootrawc r s FILE` writes the rows of job (r, s) and prints rows, nodes, secs; then `cascade_k15p 239 filter FILE` prints "TOTAL rows=… survivors=…" and SURVIVOR lines with l2=…, l4=…, l8=…, l16=… counts.
   - reducible (decomposition variant): `bgk15 239 km1roots`; for each root r, `bgk15 239 km1root r FILE`; take the union of all lines (dedupe); then `cascade_k15p 239 filterext DEDUP_FILE`.
   WRITE YOUR OWN DRIVER. Do not use the chair's kcascade_run.py; independence is the point.
   For each irredundant job record: r, s, rows, nodes, cascade survivors at level 2, and how many rows have a non-zero level-16 count.
5. Only now compare with the chair's files in together-mailbox, scouting/LR16/opus/kfactor/p239_full_cascade/:
   ir_K15_p239.jsonl (one line per job: r, s, rows, nodes, secs, casc_survivors, deep = rows alive at level 16) and km1_K15_p239.json.
   rows and nodes are deterministic: they must match job by job. secs will differ.

COST (ESTIMATE)
The chair's generation took about 5,800 CPU-seconds (irredundant) + about 280 CPU-seconds (km1) on its machine; cascades are small. So about 2 CPU-hours. On 2–4 cores, about 0.5–1 hour of wall time. If your sandbox stops long background jobs, run in chunks and make the driver resumable.
If you cannot run the full set, run a SAMPLE: all 14 km1 roots plus at least 20 irredundant jobs chosen by you (say how you chose), and mark the result PARTIAL.

REPORT (plain text, at the top a SUMMARY of at most 5 lines)
- machine: CPU model, cores; compiler version; sha256 of the 3 source files and of your 2 binaries.
- step 2 answer with line numbers; selftest output(s).
- precondition line.
- totals: jobs, rows, level-2 survivors, rows alive at level 16 — for each branch.
- job-by-job comparison: number of jobs where rows or nodes differ (list them if any).
- verdict: MATCH, MISMATCH (where), or PARTIAL.
Time and hashes: copy from your tool output; never type them from memory.
No keys or passwords anywhere. Do not search or read other chats in this account.
END PT005-TEST4-PACKET
