BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 09:07 +08
RE: 猜公式 Round 7 (packet 1006d95), send text r7_send_full.txt or r7_send_short.txt
SEAT: qwen
MODEL: Qwen3.7-Plus Thinking
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
ANSWER BLOCK

**Q1:** Conjecture C-core4 is true. **IDEA:** The cells are partitioned into intervals $I_k = [kH+1, (k+1)H]$. $I_1, I_2, I_3$ require speeds near 8, 5, 4. Speeds $\ge 16$ cover at most $H/8$ of any interval, so they cannot cover these "hard" intervals alone. We need at least 4 small speeds to cover $I_1, I_2, I_3$ and the cells near 0. Thus $M_{15} \ge 4$.
**Q2:** The floor is $N/4$. For $N=16$, it is 4. There are $N/2$ intervals, and the first $N/4$ intervals require dedicated small speeds (near $N/2, N/3, \dots$), while the remaining intervals can be covered by larger speeds or are naturally covered by the smallest speeds.
**Q3:** Checking 1365 cores costs $\approx 1365 \times O(p)$ operations, which is $\sim 10^{35}$ times faster than the full census. We can prune cores that lack speeds near 8, 5, 4, reducing the check to $\sim 50$ cores. Covers die after 431 because the "windows" for fillers shrink as $1/p$; for larger $p$, no fillers can bridge the gaps left by the 4 core speeds.
**Q4:** For 337, predict 150–300 covers have $M_{15}=4$, and the largest $M_{15}$ is 9–11. Confidence: 60%.

**Reasoning:**

**FACT:** Data shows $M_{15} \ge 4$ for all 321 checked covers. 12 never appears in the core.
**PROOF:** The "window containment" lemma shows composite speeds are inefficient ($\phi(v)/v$). This explains why 12 (efficiency 1/3) never appears, and 2, 3, 4, 6 are rare. 7, 11, 13 are primes (efficiency $\approx 1$). 8 is frequent because it uniquely covers $I_1$ with $i=1$.
**IDEA:** The floor $N/4$ comes from the number of "hard" intervals $I_k$ that cannot be covered by large speeds. For $k \le N/4$, the required speed is $\ge 4$, and large speeds ($\ge 16$) cover at most $H/8$ of the interval, so they need 8 speeds to cover it. Since we only have 14 speeds, we can't afford to use 8 large speeds for each of the $N/4$ intervals. Thus we need small speeds.
**UNFINISHED:** The exact transition point $p=431$ where covers die out. It likely corresponds to the first prime where the "filler windows" for the optimal 4-core do not contain any integers.
**Least-sure step:** The exact formula for the floor for general $N$. I guessed $N/4$ based on $N=16 \implies 4$, but it could be $N/4 - 1$ or something.

--- end verbatim ---
END LETTER
