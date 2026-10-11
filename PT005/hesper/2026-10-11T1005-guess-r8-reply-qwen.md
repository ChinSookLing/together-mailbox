BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 10:05 +08
RE: 猜公式 Round 8 (packet 1351cbb), send text r8_send_full.txt or r8_send_short.txt
SEAT: qwen
MODEL: Qwen3.7-Plus Thinking
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
ANSWER BLOCK
Q1:
Model: log(covers) = 35 - 0.085p - 0.9s. Gets 28/33 right (fails on 401, 409, 419, 421, 457, predicting 0 instead of >0). Typical log-error for >0 is ~1.2.
Q2:
The count falls because the "filler windows" (intervals of valid speeds to cover remaining cells) shrink as 1/p, making the probability of finding integer speeds drop exponentially. The parameter s enters as the remainder cells (n - 8H); larger s means a lower effective capacity ratio, leaving more cells for fillers to cover, which accelerates the exponential drop to 0.
Q3:
503: 0, 509: 0, 521: 0, 523: 0, 541: 0, 547: 0, 557: 0, 563: 0, 569: 0, 571: 0, 577: 0, 587: 0, 593: 0, 599: 0. Overall confidence: 90%.
Q4:
N=17: ~550, N=18: ~750, N=20: ~1200. (Computed N=8, 10 for small p to verify ratio scaling).

Reasoning:
FACT:
The capacity ratio for N runners is (N-2)H/n ≈ 2(N-2)/N. For N=16, this ratio is 1.75. The data shows a sharp cutoff around p=450 for this ratio.
PROOF:
The linear model for log(covers) = 35 - 0.085p - 0.9s correctly classifies 28 of the 33 primes. The 5 failures are all cases where the model underestimates the count, predicting 0 when the actual count is 1-6.
IDEA:
The exponential decay in cover counts is driven by the shrinking measure of the valid speed regions (filler windows) as p grows. The structural core requires a fixed number of small speeds, leaving the rest to be filled. As p increases, the gaps between core-covered cells require fillers to hit increasingly narrow arithmetic progressions.
IDEA:
For general N, the capacity ratio 2(N-2)/N increases with N (e.g., 1.764 for N=17, 1.80 for N=20). A higher ratio provides more "slack" or redundancy, allowing the cover to survive to larger p. The predicted max p scales roughly proportionally with the capacity ratio.
UNFINISHED:
The exact analytic form of the filler window volume and the precise transition threshold for general N.
Least-sure step:
The exact scaling factor for max p as N increases from 16 to 20.

--- end verbatim ---
END LETTER
