BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 15:51 +08
RE: 猜公式 Round 13 (packet 2e9272a), send text r13_send_full.txt or r13_send_short.txt
SEAT: lumo
MODEL: Lumo 2.0 Max Fast
CHAT: https://lumo.proton.me/u/24/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
Lumo 2.0 Max, Fast mode, short version r13_send_short.txt.


Worked through your question

1. Missed connections (two candidates):
(a) The review's connection list omits that R7's M₁₅ statistics and R6's scaling observations are the same object: the frequency table over 23 scalings (counts 8:16, 11:18, 12:0) is precisely the empirical distribution of small speeds under the scaling group — the scarcity of 12 is window-containment (speed 12's windows sit inside those of 3, 4, 6, so 12 adds almost nothing if those are present). If real, this makes C-core-type conjectures testable locally: a cover must contain speeds whose coprime-position windows are disjoint, predicting the core not by size but by coprime skeleton. Notably this explains 389's scattered structure: coprime speeds spread out maximally.
(b) The review says the (a)-collapse (R4) "looks like Poisson decay" but no one connects it to R10's k=0 term: row-collapse in (a) should be governed by the same b̂(0)^14 factor, i.e. (1−(2H+1)/p)^#columns. If true, (a) is not merely "similar" — it is a second instantiation of the same identity, and its collapse rate should match the per-16-prime factor ≈0.3 from R8.
UNFINISHED: verifying the column count arithmetic against (a) row counts — I did not compute it here.

2. Errors:
Review table 三: "D(p)：431–499 为 1–2" — earlier stated D=1 exactly at 431, 433, 439, 449, 467; if five primes have D=1 and others "1–2," fine, but the R12 packet said D≥1 at all listed primes without upper bound 2. Overstated unless recomputed.
Review 六 attributes "R_4 足以区分有无覆盖" to 主席 (R11 设想) — correct as refuted, but the review's 五 table "最负 R_4 ≈ −0.66·M(p)" is labeled FACT; it should note it is a search-based minimum, not exhaustive. Status slightly overstated.
I could not verify the 281 subgroup cover attribution without recomputation — UNFINISHED.

3. Next step:
Prove the tail bound with frequency truncation (R11 item 1) for one structured class first — subgroup covers (p ≡ 1 mod 28) — where the resonance sum collapses to coset sums that can be bounded exactly. This is the cheapest place to convert the Fourier identity into a D(p) ≥ αp − β result, and it directly targets the known exceptional class.

4. For Tuzi:
In twelve rounds this table established that whether a prime's lonely runners need 15 speeds is governed by one bookkeeping identity: every 14-speed set misses M(p) ≈ 0.077p cells "at random," and only rare arithmetic resonance (long runs like 457's 111–117, or multiplicative subgroups) cancels it. The census confirms the resonators die out by 457, and a tested Poisson formula predicts extinction for all larger p — what remains is turning the heuristic "resonance can't keep up" into a theorem, closing the gap between threshold 457 and the proved 120¹⁴.
--- end verbatim ---
END LETTER
