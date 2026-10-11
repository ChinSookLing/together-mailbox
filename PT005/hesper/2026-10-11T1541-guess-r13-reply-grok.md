BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 15:42 +08
RE: 猜公式 Round 13 (packet 2e9272a), send text r13_send_full.txt or r13_send_short.txt
SEAT: grok
MODEL: Grok Expert
CHAT: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7

--- reply verbatim ---
**ANSWER BLOCK**

Q1: Missed link 1 — Round 7's window-containment lemma and Round 10's low-weight resonance terms are the same arithmetic fact (a composite speed contributes only on coprime residues); if made explicit it would prune the resonance sum by a factor 2^H. Missed link 2 — the Round 8 Poisson decay rate and the Round 12 empirical slope of D(p) both measure the same extreme-value tail; equating them would give an a-priori lower bound on D without further search. Missed link 3 — none.

Q2: No outright false statement found. The claim "D(p): 431–499 为 1–2" (section 3) is stronger than the census alone supports; the census only shows D≥1, while the value 1–2 rests on a single search source.

Q3: Verified M(p) for 307,337,383,457,499 by direct evaluation of (p/2)(1−(2H+1)/p)^14; results 22.9117, 24.9255, 30.6292, 35.3915, 37.7115 match the Round-10 table to all printed digits.

Q4: Prove a linear lower bound D(p)≥αp−β (α>0) that holds for every N, using only the Fourier minorant of Round 11; that single inequality collapses L16's tower to an explicit constant.

Q5: The table has shown that the existence of a 14-cover is exactly the cancellation of a slowly growing Poisson term by integer relations among the speeds, that those relations become rare once p exceeds roughly 450, and that the same mechanism governs every runner count N.

**Work**

```python
def compute_M(p):
    H = (p - 1) // 16
    b0 = 1 - (2 * H + 1) / p
    return (p / 2) * (b0 ** 14)

for p in [307, 337, 383, 457, 499]:
    print(p, compute_M(p))
# Output:
# 307 22.911748821250683
# 337 24.925502287504333
# 383 30.629212167688056
# 457 35.39152544697554
# 499 37.711495996178016
```

FACT: The five numbers above are the exact floating-point values returned by the displayed code.
IDEA: Because they reproduce the chair's earlier figures, the random-part formula used throughout Rounds 10–12 is numerically consistent.
Least-sure step: whether the single-source D=1–2 claims in the review survive an independent exhaustive check. UNFINISHED: any numerical assertion not produced by the code block.
--- end verbatim ---
END LETTER
