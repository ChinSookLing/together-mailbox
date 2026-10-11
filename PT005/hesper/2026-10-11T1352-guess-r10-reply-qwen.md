BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 13:52 +08
RE: 猜公式 Round 10 (packet 0104439), send text r10_send_full.txt or r10_send_short.txt
SEAT: qwen
MODEL: Qwen3.7-Plus Thinking
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
Model: Qwen3.7-Plus, Thinking ON, web search off
Chat: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

ANSWER BLOCK

**Q1:** **PROOF:** Expanding $B(vt)$ via Fourier gives $\sum_t \prod \hat{b}(k_v) e(t \sum k_v v)$. The sum over $t$ is $p$ if $\sum k_v v \equiv 0$, else $0$. $\hat{b}(k)$ is the geometric series sum for the indicator of $[-H, H]$.
**Q2:** 457's run 111..117 yields 6 relations (e.g., $v_{i+1}-v_i-1=0$) and $4\cdot 114+1=0$. These short relations have large $|\hat{b}(k_v)|$, summing to $\approx -0.15$. Random sets lack them, so $R'(S) \approx 0$.
**Q3:** **IDEA:** For $U(S)=0$, $R'(S)$ must exactly equal $-\hat{b}(0)^{14} \approx -0.154$. Since $\hat{b}(k) \approx -\frac{\sin(\pi k/8)}{\pi k}$, each short relation contributes $O(1)$. Covers require enough short relations to hit this exact constant.
**Q4:** **IDEA:** $\hat{b}(0)^{14}$ is smooth in $1/p$, while $R'(S)$ is oscillatory. They cannot match for all large $p$. Dirichlet scaling bounds speeds, limiting $k$ vectors. PROVED: The identity and $O(1)$ bound on $\hat{b}(k)$. NOT PROVED: The explicit $P_0$.
**Q5:** Fourier separates unavoidable random gaps (Poisson) from structural arithmetic correlations (resonance), proving a cover exists iff speeds have exactly the right short integer relations to cancel the randomness.

**Reasoning:**

**FACT:** The identity for $U(S)$ is a direct application of Fourier inversion on $\mathbb{Z}/p$. The values of $\hat{b}(k)$ are exact geometric sums.
**PROOF:** For $k \neq 0$, $\hat{b}(k) = -\frac{1}{p} \frac{\sin(\pi(2H+1)k/p)}{\sin(\pi k/p)}$. Since $2H+1 \approx p/8$, for small $k$, $\hat{b}(k) \approx -\frac{\sin(\pi k/8)}{\pi k}$, which is $O(1)$ and independent of $p$.
**IDEA:** The "resonance budget" requires $R'(S) = -\hat{b}(0)^{14} \approx -(7/8)^{14} \approx -0.154$. A random 14-set has $R'(S) \approx 0$ because short relations are rare. 457's cover has a dense core (the run 111..117), generating many short relations like $v_{i+1} - v_i - 1 = 0$. Each such relation contributes $\approx (-\frac{\sin(\pi/8)}{\pi})^3 \approx -0.02$. About 7-8 such relations are needed to reach $-0.154$.
**FACT:** As $p$ increases, the target $-\hat{b}(0)^{14}$ changes slightly because $H = \lfloor (p-1)/16 \rfloor$ introduces a fractional part.
**IDEA:** To prove $\gamma(p) = 15$ for $p > P_0$, we must show no 14-set can achieve the exact resonance. Dirichlet scaling (Lemma B) forces any 14 speeds to be $\lesssim p^{13/14}$. This restricts the possible integer relations $\sum k_v v = 0$ to those with small coefficients $k_v$. The number of such "short" relations is bounded. Since $R'(S)$ is a finite sum of smooth oscillatory functions of $1/p$, and the target is a different smooth function, they can only intersect finitely many times.
**UNFINISHED:** The exact bound $P_0$ requires quantifying the minimum non-zero difference between the oscillatory sum and the target polynomial in $1/p$.
**Least-sure step:** The exact application of Dirichlet scaling to bound the number of short relations; it restricts the speeds, but the relation coefficients $k_v$ could still be large if the speeds share a common factor, though we can assume $\gcd(S)=1$.

--- end verbatim ---
END LETTER
