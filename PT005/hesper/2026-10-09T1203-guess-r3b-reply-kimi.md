BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 12:11 +08
RE: 猜公式 Round 3 ADD-ON (chair note 46, 34bd541; C16), one narrow task, send text r3b_send_kimi.txt
SEAT: kimi
MODEL: Kimi K3 Max, web off
CHAT: https://www.kimi.ai/chat/1a11ecf4-4732-8493-8000-09ced57127e1

--- reply verbatim ---
## ANSWER BLOCK

**C16 fails at 14 speeds: min c₁₄ < 1/16 at every M computed (15–20, exhaustive, exact rationals, all 38,759 sets, 79 s).**

FACT — results (sets with max = M; c = M × longest 1/16-safe piece):

| M | min c₁₄ | vs 1/16 | argmin S | longest piece |
|---|---|---|---|---|
| 15 | 5/88 ≈ 0.05682 | 10/11 of it | {1..13, 15} | 1/264, at [17/48, 63/176] |
| 16 | 2/35 ≈ 0.05714 | 32/35 | {1..6, 9..16} | 1/280 |
| 17 | 119/2496 ≈ 0.04768 | ~0.76 | {1..5, 7..13, 15, 17} (+1 more) | 7/2496 |
| 18 | 21/416 ≈ 0.05048 | ~0.81 | {1..5, 10..18} | 7/2496 |
| 19 | 57/1280 ≈ 0.04453 | ~0.71 | {1..4, 10..19} | 3/1280 |
| 20 | 35/624 ≈ 0.05609 | ~0.90 | {1..5,7,8,9,11,12,13,15,17,20} (+1 more) | 7/2496 |

Overall min over all 14-subsets of {1..20}: **57/1280 ≈ 1/22.5** (M = 19 set). Compare 13-speed min **1/16 = 0.0625**.

PROOF (validation): the same code reproduces the chair's 13-speed data exactly — min c = 1/16 at {1,2,3,4,5,7..14} with longest piece 1/224, and c({1..13}) = 1/8 — and every 14-speed argmin was independently confirmed by 4×10⁶-point float sampling (agreement to 3×10⁻⁶). Arithmetic is exact: bad intervals ((16k−1)/(16v), (16k+1)/(16v)) merged as Fractions; safe pieces are the gaps.

IDEA: minimizers are near-intervals {1..M} minus a short block, echoing the 13-speed shape; but going 13 → 14 speeds strictly lowers c_min, so C16 looks like a 13-speed accident, not a pattern. For Lemma A at 14 speeds the constant is ≤ 57/1280 — the hoped-for "replace 56 by 16" already fails here.

## Least-sure step

Piece-count bookkeeping: my merge drops zero-length safe points (I count 12 pieces on the chair's minimizer vs the reported 18). c and the longest piece agree exactly on both validation sets, so the conclusion is unaffected — but open/closed-endpoint handling at touching intervals is where an error could hide. Runtime allowed exactly M = 15..20 as tasked; M = 21 (C(20,13) = 77,520 sets) is feasible at ~4 min on request.

UNFINISHED: nothing within the assigned range; the 14-speed analogue of C16 is settled (false) for max(S) ≤ 20.

--- end verbatim ---
END LETTER
