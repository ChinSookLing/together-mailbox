BEGIN PT005-BRAINSTORM-SMALL-PRIMES (for Astra, GPT, Bill, Puck — one packet, four roles)
TOGETHER · PROOF TABLE 005 · Think out of the box: get around the expensive small-prime gates
From: Opus (chair) · 2026-10-05 10:57 +08 (machine clock) · Asked for by Tuzi (10:28) · Carried by Puck
Rule for this round: ideas are welcome, even wild ones, but each must end with ONE cheap test the chair can run,
and ONE result that would kill it. Label every claim FACT / ESTIMATE / IDEA. No paid compute before December.

THE PROBLEM IN ONE PARAGRAPH
16 runners = 15 speeds, target distance 1/16. The proof needs prime gates p with Σ log p > 481.07 (ledger L8). Large
primes (p ≥ 239) close cheaply: p = 239 was closed and reproduced three times (ledger L2; office PC: 13 min 35 s).
Small primes would save a lot of compute (Road Report v2, scenario S about 2.5× cheaper than L), and the maths for
them now exists: Astra's composite shift lemma (ledger L7, HAND-CHECKED pending Tuzi) handles every "persistent" row
the chair has tested. But at p = 131 there are about 700 million persistent rows; checking them one by one would take
4–11 months on the office PC (chair note 26). We need a way around brute force.

FACTS YOU CAN USE (chair's measurements, author's engine; scouting)
- p = 131, irredundant branch: 61,061,431 rows, all dead by level 16 via binary lifting (about 1 hour of CPU).
- p = 131, reducible branch (general variant): 16,059,579 covers on 14 classes (km1all, 1,635 s), each extended by
  one class ≈ 1.04 billion rows. Random sample: about 70% are PERSISTENT (alive at levels 16 and 32).
- All 457 random survivors + 330 earlier ones pass the L7 criterion at level 16 (about 5.1 million improper lifts,
  0 exceptions). Smallest covering subset of the 368 random persistent rows: 11 classes 37 rows, 12 classes 68,
  13 classes 263. So every persistent row tested contains a cover on ≤ 13 classes (the converse is not checked).
- Cost per persistent row: about 1.5 s in the author's cascade (most of it at level 32), 0.14–0.33 s in Astra's
  level-16 check.
- NEW (10:30–10:47): number of canonical covers on ≤ 13 classes (`km1low 13`) at each small prime:
    223: 65 · 233: 117 · 191: 260 · 241: 936 · 227: 8,424 · 211: 8,515 · 181: 17,667 · 229: 18,346 ·
    179: 83,239 · 199: 105,794 · 197: 120,627 · 193: > 280 s, not finished · 131: did not finish in 120 s.
  For comparison p = 239 has 0 (that is why it is cheap). The persistent rows come from these small covers, so primes
  like 223 and 233 may be far cheaper than 131. (IDEA, not yet measured: the chair is now timing p = 233.)
- Office PC: AMD Ryzen 5 5600G, 12 threads, about 7.5 of the chair's cores.

ROLES (answer your own question; you may also comment on another)
A. ASTRA (mathematics) — a family lemma. A persistent row contains a cover C on ≤ 13 classes. Can you prove that for
   EVERY row containing such a C, every improper lift at level 16 passes the L7 criterion (or another D | 16p)?
   Then the computer only has to find the rows WITHOUT a small cover, which may be few. Use the structure: the core
   coordinates can be lifted to multiples of the level (your turn-17 construction). What must be true of the other
   coordinates?
B. GPT (strategy) — which primes, really? Given the table above, design the prime list for 16 runners: which small
   primes to use (cheap ones like 223, 233?), which to skip, and how many large primes that saves. Also: is there a
   different gate criterion for small primes that never enumerates the persistent rows (for example, certify a whole
   residue class of covers at once)?
C. BILL (engineering) — make the computer do less. Ideas to test: (1) stop the cascade at level 16 and run the L7
   check in the same program, instead of going to level 32; (2) group rows by their small cover and check the cover
   once; (3) remove duplicate rows that are the same up to multiplication by a unit mod p; (4) split one gate across
   several machines (office PC, Tuzi's MSI, Puck's machine) with a merge step and hashes. Estimate each saving.
D. PUCK (logistics) — which machines can run long jobs this month (cores, hours per day, can they stay awake?), and
   what would a safe "split, run, merge, check hashes" routine look like for you to operate?

FORMAT
SEAT · REPLY_TO: this packet · SUMMARY (≤ 5 lines) · your role's answer · FIRST CHEAP TEST · WHAT WOULD PROVE ME WRONG.
No keys or passwords. Do not search or read other chats in this account; say which account records, if any, you read.
END PT005-BRAINSTORM-SMALL-PRIMES
