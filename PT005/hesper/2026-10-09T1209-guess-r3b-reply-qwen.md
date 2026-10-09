BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 12:11 +08
RE: 猜公式 Round 3 ADD-ON (chair note 46, 34bd541; C16), one narrow task, send text r3b_send_qwen.txt
SEAT: qwen
MODEL: Qwen3.8-Max thinking, web off, code interpreter
CHAT: https://chat.qwen.ai/c/3640df5e-ab11-4218-ad90-50f6abfcdc9a

--- reply verbatim ---
**ANSWER BLOCK**
FACT: M=30: best c(S) = 45/704 (≈0.0639) at S = {2,4,6,8,10,14,16,18,20,22,24,26,30}.
FACT: M=40: best c(S) = 17/192 (≈0.0885) at S = {2,4,6,16,22,26,28,30,32,34,36,38,40}.
FACT: M=60: best c(S) = 5/48 (≈0.1042) at S = {4,8,18,32,38,40,44,46,48,50,52,56,60}.
FACT: Method: Simulated annealing (up to 50,000 iters/M) utilizing a sweep-line over interval endpoints. Float64 precision flawlessly sorts events (min gap > $10^{-6}$ vs $\epsilon \approx 10^{-16}$). Total runtime ~30s.
FACT: All best sets were strictly verified using exact `Fraction` arithmetic. None fell below the 1/16 (0.0625) threshold.
IDEA: C16 holds securely for M ∈ {30, 40, 60}, with minima comfortably exceeding 1/(16M).
UNFINISHED: Global optimality remains unproven given the massive search spaces (e.g., $\binom{59}{12} \approx 10^{11}$ sets for M=60).
Least-sure step: Guaranteeing the SA heuristic escaped all local minima to discover the absolute global minimum.

***

**Search Details & Verification**
The sweep-line algorithm calculates unsafe intervals $I_v = \bigcup_{k=0}^{v-1} (\frac{16k-1}{16v}, \frac{16k+1}{16v})$. For $M=60$, the maximum denominator is 960. The minimum non-zero distance between any two rational endpoints is $1/(960^2) \approx 1.08 \times 10^{-6}$. Because double-precision floats have 53 bits of accuracy ($\approx 10^{-16}$), sorting event boundaries via floats is mathematically exact. This allowed rapid SA iterations.

The exact verification using Python's `Fraction` confirmed the final reported c(S) values:
- $45/704 = 0.06392... > 0.0625$
- $17/192 = 0.08854... > 0.0625$
- $5/48 = 0.10416... > 0.0625$

--- end verbatim ---
END LETTER
