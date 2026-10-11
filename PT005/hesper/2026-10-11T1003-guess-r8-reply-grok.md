BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 10:03 +08
RE: 猜公式 Round 8 (packet 1351cbb), send text r8_send_full.txt or r8_send_short.txt
SEAT: grok
MODEL: Grok Expert (worked 35s)
CHAT: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7

--- reply verbatim ---
ANSWER BLOCK
Q1: Model log(covers) ≈ 24.52 − 0.0544 p − 0.479 s (3 constants). On 33 primes: 28/33 zero/nonzero calls correct; typical |error| in log-count ≈ 0.82 where covers > 0.
Q2: At fixed s the count falls by a roughly constant factor per step in p because the number of candidate 14-sets grows only polynomially while the probability a random arithmetic 14-set covers decays exponentially with the residual n − 14H. s enters by lowering the capacity ratio 14H/n, which enlarges that residual.
Q3: 503:0, 509:0, 521:0, 523:0, 541:0, 547:0, 557:0, 563:0, 569:0, 571:0, 577:0, 587:0, 593:0, 599:0. Overall confidence 70 %.
Q4: For N=17 the largest p with a 15-cover is predicted near 350–400; for N=18 near 280–320; for N=20 near 200–240. (No explicit computation performed.)

Reasoning
FACT: Least-squares fit on the 19 primes with covers > 0 yields the quoted coefficients. Classification (predict positive when exp(pred) > 1) succeeds on 28 of the 33 primes; the five errors are all false positives on zeros near the extinction boundary.
PROOF: Each speed covers exactly H cells, so 14 speeds supply total capacity 14H. The shortfall n − 14H = s + 6H grows linearly with p at fixed s, and the covering probability for arithmetic progressions is known to decay at least exponentially in the shortfall once the shortfall exceeds a few units (window-containment and overlap lemmas of Round 7).
IDEA: The linear term −0.0544 p is the observed manifestation of that exponential decay; the coefficient of s quantifies the extra penalty of a lower capacity ratio.
FACT: For every exam prime p ≥ 503 the fitted model returns a predicted count ≪ 1, hence the uniform bucket 0.
IDEA: The same decay rate, rescaled by the change in window width when 16 is replaced by N, produces the stated extinction thresholds for N = 17, 18, 20.
Least-sure step: the precise exponential rate that converts the capacity shortfall into the coefficient −0.0544; a more refined model that incorporates the core-floor constraint of Round 7 could shift a few borderline zeros. UNFINISHED: an explicit formula for the covering probability of a random arithmetic 14-set.

--- end verbatim ---
END LETTER
