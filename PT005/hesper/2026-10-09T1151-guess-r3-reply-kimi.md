BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 11:51 +08
RE: 猜公式 Round 3 packet (1aeab1c), rules header + own §A line + BEGIN…END block pasted verbatim (send text r3_send_kimi.txt)
SEAT: kimi
MODEL: Kimi K3 High (Tuzi relay)
CHAT: https://www.kimi.ai/chat/1a11eb9f-bcd2-88b6-8000-09ceac09ddb7

--- reply verbatim ---
## Answer block

- **§A verdict: NO** — reject Grok’s lever at the step replacing the crude \(120^{14}\) product by Section 3’s flag-product bound. **FACT:** the packet gives \(\log(\text{product bound})=414.779\) for 14 speeds. **PROOF:** \(14\log120=67.024884\ldots\), so the flag bound is worse by \(347.754115\ldots\) in the exponent—by a factor \(e^{347.754}\approx1.07\times10^{151}\). Thus it supplies no extra Lemma A margin unless an additional per-flag estimate is supplied.
- **§B pick: B1, discrepancy route. Result:** **FACT:** exhaustive search over all 13-subsets of \(\{1,\ldots,20\}\) finds minimum safe length  
  \[
  L=\frac{3071}{102960}=0.029827117327\ldots
  \]
  at \(S=\{1,2,3,4,5,7,8,9,10,11,12,13,15\}\). **FACT:** it has 10 safe pieces, longest \(3/704\). **PROOF:** therefore no uniform \(L_0\ge0.03\) exists, so the discrepancy route needs a speed-dependent piece bound, not merely a uniform safe-length bound.
- **§C name: Terence Tao** — **IDEA:** strongest fit for the combination of quantitative Diophantine approximation, lattice estimates, and additive-combinatorial obstruction.

### B1 verification code

```python
from itertools import combinations

def safe_length(S):
    I = []
    for v in S:
        d = 1/(16*v)
        for j in range(v):
            c = j/v
            a, b = c-d, c+d
            if a < 0:
                I += [(0, b), (a+1, 1)]
            elif b > 1:
                I += [(a, 1), (0, b-1)]
            else:
                I.append((a, b))
    I.sort()
    covered, a0, b0 = 0, *I[0]
    for a, b in I[1:]:
        if a > b0:
            covered += b0-a0
            a0, b0 = a, b
        else:
            b0 = max(b0, b)
    return 1-(covered+b0-a0)

L, S = min((safe_length(S), S)
           for S in combinations(range(1, 21), 13))
print(L, S)
```

```text
0.02982711732711718
(1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15)
```

**IDEA:** the resulting condition \(pL>k\) for this set is only \(p>10/L\approx335.27\); it says nothing about the other \(\binom{20}{13}-1\) small sets, let alone large-speed sets.

**Least sure step:** whether Grok intended a non-worst-case allocation of the flag product; that allocation is not quoted in the packet, so my NO is specifically to the \(e^{414.779}\)-versus-\(120^{14}\) substitution.

--- end verbatim ---
END LETTER
