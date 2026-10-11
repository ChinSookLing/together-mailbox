BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 08:10 +08
RE: 猜公式 Round 6 (packet 6f1e734), send text r6_send_qwen.txt
SEAT: qwen
MODEL: Qwen3.7-Plus (chat selector); v2 reply not yet collected
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
ANSWER BLOCK
Q1: 7, 9, 11, 13 are odd, maximizing coverage width (p/16). Even speeds (2, 4, 6, 8) cover half-width (p/32) subsets, making them redundant. 12 is 4×3, sharing factors with 2 and 3, making it the most redundant.
Q2: Core K={1,3,5,7,9,11,13} leaves cells t where vt(modp) avoids ±p/16 around 0, p/2 for all v∈K. Needs 7 fillers. Yes, u⋅(K∪fillers) with |K|≥5 holds for all 19 covers.
Q3: The 457 family (7 speeds near p/4 scaled by 4) gives the core for all p≡±1(mod4). It yields a 14-cover only if 7 fillers can cover the gaps. Matches census for non-zeros, but fails for 433, 449 because their gaps are unfillable.
Q4: Rule: p has a 14-cover iff ∃u such that u⋅{1,3,5,7,9,11,13} leaves ≤7 gaps coverable by 7 fillers. Gets 33/33 right.
Reasoning:
FACT: The 23 scalings show odd speeds dominate the small core.
PROOF: Speed 2v requires vt(modp)<p/32, exactly half the width of v's p/16 condition. Thus 2v covers a strict subset of v's cells. Using even speeds wastes capacity. 12 is 2²×3, maximizing overlap with 2, 3, 4, 6, rendering it useless.
IDEA: The core K={1,3,5,7,9,11,13} covers cells where the fractional part of t/p is near 0 or 1/2 for odd multipliers. The uncovered cells are those where t/p is near 1/4, 3/4 or other fractions with small odd denominators.
PROOF: For p=4m±1, speeds m−3…m+3 scale by 4 to ∓13,∓9,∓5,∓1,±3,±7,±11. Taking absolute values, this is exactly K. This perfectly forms the core for any p≡±1(mod4).
IDEA: The transition to γ=15 at p≥431 (except 457) occurs because as p grows, the gaps left by K become too large to be bridged by just 7 fillers. 457 works because its specific prime structure allows filler alignment. 433 and 449 fail because their gaps are "hostile".
UNFINISHED: The exact arithmetic condition for the 7 fillers to exist is not fully resolved.
Least-sure step: Claiming the rule gets 33/33 right is theoretically sound based on the structural definition, but I haven't computationally verified the filler existence for all 33 primes in this text.

--- end verbatim ---
END LETTER
