# PT005 · Chair note 101 · K11 audit: L20 (383) and L21 (397) reproduced on a second machine; ledger proposals

From: Opus (chair) · 2026-10-18 04:44 +0800 (machine clock)
Reads:
- K11 p383a results: PT005/hesper/k11/p383a-results/ (7a89c5e …)
- K11 p397a results: PT005/hesper/k11/p397a-results/ (685f0a7 …)
- Puck count check 8d603fa
- Office references: collect-38060748868 (383) and collect-38496413434 (397)

## 1. Chair comparison (own script), job by job
Fields compared: r, s, rows, nodes, casc_rows, casc_survivors, deep, n_survivor_lines.

| Gate | Office jobs | K11 jobs | Same job set | Jobs with any field different | Rows (K11) | Alive at level 16 | km1 covers (K11) |
|---|---|---|---|---|---|---|---|
| 383 | 415 | 415 | yes | **0** | 5,171 | 0 | 0 (23 roots) |
| 397 | 436 | 436 | yes | **0** | 23,452 | 0 | 0 (24 roots) |

- No duplicate job lines in the K11 files.
- The patched cascade source on K11 has sha256 f17094de…. The chair reproduced exactly this hash by applying the ledger L2 patch to cascade_filter_k.cpp 50fa9385…. **Same code on both machines.** The binaries differ (-march=native), as expected.
- K11 is a GMKtec mini PC with a Ryzen 9 8945HS and 16 threads; the office PC is a different machine. Both ran the same pinned runner kcascade_run.py 90632d55….

## 2. Ledger proposals (Tuzi decides each)
- **(a) L20 · p = 383 and L21 · p = 397: PROVISIONAL → REPRODUCED.**
  - This is the same standard as L10–L14: two machines, same code, a job-by-job comparison with 0 differences, and 14-class covers = 0 on both.
- **(b) L24 · p = 463: new, OFFICE-RUN, CHAIR-SPOT-CHECKED (provisional).**
  - Job list 589 = 589; spot reruns 2 of 2 match (note 100).

**Gate totals if both are approved:**

| | Σ log p |
|---|---|
| Closed (L2…L14, L20, L21) | 27.07 + 11.93 = **39.00** |
| Provisional (L22 431, L23 443, L24 463) | **18.30** |
| Together | **57.30 of 481.07** |

## 3. Next K11 job (proposal)
**k11-p431a**, the same pattern as p397a with prime 431. It turns L22 into REPRODUCED. It takes about 130 CPU-hours, so roughly 9–10 hours on K11, which fits one night. After it: p443a, then p463a.
