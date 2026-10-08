BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-08 16:42 +08
RE: 猜公式 Round 1 packet (ebc63af), BEGIN…END block pasted verbatim
SEAT: qwen
MODEL: Qwen3.7-Plus
CHAT: https://chat.qwen.ai/c/18cf253d-2f8c-48b4-a549-bb7f140a3902

--- reply verbatim ---
# Guess γ(p) — Round 1

## 1. Rule

**Empirical formula:** 
$$\gamma(p) \approx \left\lceil 2.5 \ln(p) - 1.0 \right\rceil$$

with a residual scatter of ±1 depending on the arithmetic structure of $p-1$.

**For the yes/no question "$\gamma(p) \geq 14$?":** 
The data shows a clean threshold: **$\gamma(p) \geq 14$ for all $p \geq 281$** (every prime $\geq 281$ in the table is $\geq 14$; the last prime with $\gamma = 13$ is $p = 277$). Below 281, $\gamma$ transitions: roughly 12 for $p \in [120, 200]$, roughly 13 for $p \in [180, 280]$.

## 2. Predictions

| EXAM prime | Prediction | 
|---|---|
| 199 | **13** |
| 227 | **13** |
| 257 | **13** |
| 271 | **13** |
| 283 | **14 or more** |
| 311 | **14 or more** |
| 313 | **14 or more** |
| 401 | **14 or more** |

## 3. Reason

The covering problem is equivalent to covering the cells $\{1, \dots, n\}$ with $m$ "arithmetic progressions" of length $H$ in $\mathbb{Z}/p\mathbb{Z}$: speed $v$ covers cell $t$ iff $\|vt/p\| < 1/16$, meaning $t \in v^{-1} \cdot (-p/16, p/16)$. 

The trivial lower bound $\lceil n/H \rceil = 8$ or $9$ assumes zero overlap. But the multiplication table mod $p$ has pseudo-random discrepancy: the products $vt \bmod p$ are not perfectly uniformly distributed. As $p$ grows, the "fluctuations" in coverage force additional speeds beyond the volume bound. 

The excess $\gamma(p) - \lceil n/H \rceil$ grows from $\sim 2$ (at $p \approx 100$) to $\sim 5$ (at $p \approx 300$). This is consistent with a logarithmic correction $\sim c \ln p$, which is the typical integrality gap for set cover on pseudo-random hypergraphs. The formula $2.5 \ln p - 1.0$ fits all 33 training values to within $\pm 1$.

The threshold $p \approx 281$ emerges because $2.5 \ln(281) - 1.0 \approx 13.1$, pushing the ceiling to 14. The $\pm 1$ scatter explains the "early" $\geq 14$ primes (239, 269) and the "late" 13-primes (241, 251, 263, 277).

## 4. Big Question

**Yes**, $\gamma(p) \geq 14$ for every prime $p > P_0$ with $P_0 \approx 280$. 

$\gamma(p)$ will keep growing, but **slowly** — logarithmically, not linearly. The formula predicts:
- $\gamma \geq 15$ for $p \gtrsim 350$
- $\gamma \geq 16$ for $p \gtrsim 520$  
- $\gamma \geq 17$ for $p \gtrsim 780$

This slow growth means part (c) of the gate is indeed deleted for all large $p$, but the threshold is not dramatically larger than what we already see. The growth rate $d\gamma/dp \approx 2.5/p$ means each increment of 1 in $\gamma$ requires roughly a $40\%$ increase in $p$.

*Honesty note:* This rule does not touch parts (a) and (b) of the gate. It only eliminates part (c) for large $p$.

## 5. Confidence

| EXAM prime | Confidence |
|---|---|
| 199 | 60% |
| 227 | 60% |
| 257 | 70% |
| 271 | 50% |
| 283 | 75% |
| 311 | 85% |
| 313 | 85% |
| 401 | 95% |

The "far" EXAM primes (311, 313, 401) are high confidence because the logarithmic trend is unambiguous at that range. The mid-range primes (271, 283) are lower confidence because they sit near the transition zone where the $\pm 1$ scatter matters most.
--- end verbatim ---
END LETTER
