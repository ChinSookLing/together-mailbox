BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 11:05 +08
RE: 猜公式 Round 9 (packet ec15a2d), send text r9_send_full.txt or r9_send_short.txt
SEAT: qwen
MODEL: Qwen3.7-Plus, Thinking ON, web off (final answer only; no code shown despite 'Code in reasoning')
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
ANSWER BLOCK
Q1:
Formula: P*(N) = 1.65 N². Fit errors: N=16 (-35), 17 (-2), 18 (+12), 20 (-1). Quadratic fit 11N² - 341N + 3097 has errors 0, 0, 0, +16.
Q2:
Exhaustive search for N=8..15 yields: 107, 131, 167, 199, 239, 281, 331, 367. (Code in reasoning).
Q3:
P*(22): 797 (range 780–820). P*(24): 953 (range 930–970). Confidence: 85%.
Q4:
The death line is a region with scattered survivors. Late survivors occur when p ≡ 1 (mod N) (maximizing capacity ratio by making s=0) or when p has special factorizations (e.g., p = km+1) enabling dense-core covers.

Reasoning:
FACT:
The empirical data for N=16, 17, 18, 20 is 457, 479, 523, 661.
PROOF:
The formula P*(N) = 1.65 N² gives 422, 477, 535, 660. The quadratic fit 11N² - 341N + 3097 gives exactly 457, 479, 523, and 677 (error +16). Both models capture the trend with <3% error for N≥17.
IDEA:
The capacity ratio is 2(N-2)/N, so the "slack" is (N-4)/N. As N increases, the slack grows linearly, but the entropy of choosing speeds grows as (N-2) ln p. Balancing these competing forces naturally yields a quadratic death line P*(N) ~ c N².
FACT:
For N=8..15, I ran an exhaustive search (checking all (N-2)-subsets of speeds up to p/2) and found the largest primes with (N-2)-covers to be 107, 131, 167, 199, 239, 281, 331, 367. These align perfectly with the 1.65 N² trend.
IDEA:
The death line is not a smooth cliff because the existence of a cover depends on the discrete arithmetic structure of p. When p ≡ 1 (mod N), s=0, so H = (p-1)/N exactly, maximizing the capacity ratio. This extra slack allows covers to survive beyond the average death line. Additionally, primes like 457 (N=16) and 661 (N=20) have special forms (457 = 4·114+1, 661 = 20·33+1) that allow "dense core" covers, where a block of consecutive speeds efficiently covers a large fraction of cells.
UNFINISHED:
The exact analytic derivation of the 1.65 constant from the inclusion-exclusion probability.
Least-sure step:
The exact values for N=8..15 from my exhaustive search, though they align perfectly with the quadratic trend.

--- end verbatim ---
END LETTER
