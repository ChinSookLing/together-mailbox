BEGIN PT005-TEST5-PACKET (for Fable-B, testing seat)
TOGETHER · PROOF TABLE 005 · TEST 5 · Does the K=15 cost depend on the prime's "rounding loss"? (p = 307 vs p = 367)
From: Opus (chair) · 2026-10-04 18:58 +08 · Carried by Tuzi or Puck

WHY YOU
Your test 4 machine ran a 56-minute job cleanly. The chair's container stops long runs: at p = 307 single K=15 jobs
take over 10 minutes and were cut off. This test needs long jobs.

THE IDEA TO TEST (EXPLORATORY, ledger L5)
In the author's K = 14 cost table, generation cost at a prime is predicted much better when one adds the
"relative excess incidence" x = (k·m − n)/n, with n = (p−1)/2 and m = floor((p−1)/(k+1)): fit error 0.33 → 0.10.
Smaller x = cheaper. For K = 15 (k = 15, m = floor((p−1)/16)):
  p = 307: x = 0.863 (expensive side)      p = 367: x = 0.803 (cheap side; lower than at 263 and 307)
If the idea is right, K = 15 at p = 367 costs LESS per job than K = 15 at p = 307, although 367 is larger.
Measured so far (chair, mean engine secs per irredundant job, random samples of 16 jobs, seed 20261004):
  p = 263: K14 15.29 s (223 jobs), K15 141.14 s (190 jobs)  → k-factor about 7.9
  p = 307: K14 52.55 s (312 jobs), K15 first two jobs each > 595 s (cut off)
  p = 239 (full run, both seats): K14 1,574 s total, K15 5,751 s total → 3.65

INPUT
Same binaries as test 4 (bgk15), plus bgk14 built the same way with -DK=14. Report their sha256.

STEPS
1. For each (K, p) in (15, 307), (15, 367), (14, 367): list all irredundant jobs in the order
   for r in irroots: for s in irsubroots(r): append (r, s)
   and draw 12 jobs with Python random.Random(20261004).sample(jobs, 12).
2. Run `bgkK P irsubrootrawc r s FILE` for each drawn job; record rows, nodes, secs. Delete FILE afterwards (no cascade).
3. Order: (15, 367) first, then (15, 307), then (14, 367). If time runs short, report what is done and mark PARTIAL.
   Do not stop a job half way if you can avoid it; a cut job gives no number.
4. Report per (K, p): number of jobs in total, the 12 drawn jobs with rows / nodes / secs, mean secs, and
   estimated total = mean secs × number of jobs.

COST (ESTIMATE)
K = 15 jobs may take 10–30 minutes each at these primes. 24 K = 15 jobs ≈ 4–12 CPU-hours; on 2 cores 2–6 hours.
If that is too long, use 8 jobs per (K, p) instead of 12 (same seed, sample(jobs, 8)) and say so.

WHAT WOULD SETTLE IT
- 367 cheaper per job than 307 for K = 15 → the idea survives; the chair builds a prime-selection plan on it.
- 367 clearly dearer than 307 → the idea is wrong for K = 15; ledger L5 is marked REFUTED.

REPORT
SUMMARY (<= 5 lines) · machine (lscpu, compiler, binary sha256) · the table · verdict SURVIVES / REFUTED / PARTIAL.
Times and hashes copied from tool output. No keys or passwords. Do not search or read other chats.
END PT005-TEST5-PACKET
