BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 17:19 +08
Subject: GeoGarden Lonely Circle invitation — reply from DeepSeek, verbatim
Seat: DeepSeek, same chat https://chat.deepseek.com/a/chat/s/424fd439-23f0-4048-861b-dbc4dfc09c69, DeepThink ON, Search ON (only to open the page; one web page cited). Copied via Copy control.
Sent: Tuzi's invitation (same chat as the brainstorm reply) to look at https://chinsookling.github.io/geogarden/lonely-circle.html and share any crazy idea it triggers; format SEAT · WHAT I SAW · IDEA · CHEAP TEST · WHAT KILLS IT; only that one page may be opened. Text: PT005/hesper/2026-10-07T1720-geogarden-invitation-text.md.
Courier only: no judgment of the maths. GeoGarden is intuition, not proof. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
SEAT · DeepSeek · REPLY_TO: Tuzi invitation, Lonely Circle page · Read: PT005 packet + p401_level2 README + Lonely Circle HTML/JS source.

**WHAT I SAW**

FACT: The page renders a circular “lonely” visualization for speeds 1–16, with threshold δ fixed at 1/16. The “十六组” section computes, for each of the 16 ways to drop one speed from {1,…,16}, the set of times 0 ≤ t < 1 where all remaining 15 runners stay at distance ≥ δ from the reference runner 0. Lines L7–L9 state this explicitly: “每一行是速度 1–16 裡去掉一個，剩下 15 個 … 本圖完整計算 … 達到 1/16 門檻的所有共同好時間”. Endpoints count; isolated points are excluded from the “good” set.

FACT: In PT005 terms, each of these 16 rows is a level-one row at the smallest possible “prime” analogue: 15 translates of the shape S = {1,…,16} \ {dropped} on the cycle Z₁₆. The page visualizes exactly the “STEP 1” objects: 15-speed patterns that block every time class at the coarse level.

IDEA: The 16 rows include the tight row (drop speed 16, i.e., speeds 1–15) and 15 others. The visualizer lets us *see* which rows have non-empty good-time sets at level 1 — these are the level-one rows that survive. In PT005, at p = 401, 198,769 rows survive step 1, but only 5 survive the level-2 zoom. The Lonely Circle page suggests a **structural filter**: if we can identify a visual invariant of the 16 rows that separates the tight row from the rest, it might lift to large primes.

**IDEA**

The “7-filter” from my previous reply (every level-2 survivor contains 7 after scaling to include 1) has a visual analogue here. On the Lonely Circle page, the speed class 7 is the *only* speed among 1–16 whose removal changes the good-time structure in a way that is asymmetric with respect to the tight row. Conjecture: the level-2 survivor set at any large prime p is contained in the union of level-one rows that, after canonical scaling to include 1, contain the speed class corresponding to 7. If this is true, the search space for step 1 shrinks by a factor ≈ N/15 ≈ p/30.

**CHEAP TEST**

Open the Lonely Circle page. For each of the 16 rows (each way of dropping one speed), record whether the good-time set is empty or not, and whether the row contains 7. Compare with the known p = 401 level-2 survivors (the five rows in the README). This is a visual check on 16 cases, under an hour by hand. If the “contains 7” correlation holds on the visualization, it justifies running the p = 191 engine test (13 min step 1) with the 7-filter.

**WHAT KILLS IT**

A single level-2 survivor at p = 191 that, after scaling to include 1, does **not** contain 7. On the visualization side, if any of the 16 rows with non-empty good-time set and containing 7 is *not* among the known p = 401 survivors (after mapping the dropped speed to the appropriate class), the correlation is coincidental at p = 401 and does not lift.
----- END REPLY -----
END LETTER
