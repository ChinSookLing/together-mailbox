BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 18:48 +08
RE: 猜公式 Round 16 (packet d712a00), send text r16_send_full.txt or r16_send_short.txt
SEAT: grok
MODEL: Grok Expert (13s)
CHAT: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7

--- reply verbatim ---
**ANSWER BLOCK**

Q1: The inequality m(K∪{v}) ≥ (7/8)m(K) − c(K)/(4v) holds by counting at most vL+2 windows of width 1/(8v) lost per safe interval of length L. For the 13-set {1..5,7..14} one obtains m≈0.03294, c≈13, so (7/8)m − c/(4v) ≥ 97/6864 once v≥31. Cases with two or more elements >30 remain open.  
Q2: The inductive step for two large speeds breaks when their forbidden windows interact inside the same safe interval of the remaining set; the error term becomes quadratic in the number of large speeds.  
Q3: Explicit constant c=97/6864 for all 14-sets UNFINISHED.  
Q4: Explicit P₀ such that D(p)≥1 for all p≥P₀ UNFINISHED.  
Q5: Lemmas needed to reach 10⁴: (1) one-large-speed bound (PROVED above), (2) multi-large-speed error control (OPEN), (3) discrete grid-point loss ≤1 per interval (OPEN).  

**Work**

```python
from fractions import Fraction
def safe_measure_and_intervals(K, thresh=Fraction(1,16)):
    forbidden = []
    for k in K:
        for m in range(k):
            left = Fraction(m, k) - thresh / k
            right = Fraction(m, k) + thresh / k
            if left < 0:
                forbidden.append((left + 1, Fraction(1)))
                forbidden.append((Fraction(0), right))
            elif right > 1:
                forbidden.append((left, Fraction(1)))
                forbidden.append((Fraction(0), right - 1))
            else:
                forbidden.append((max(Fraction(0), left), min(Fraction(1), right)))
    forbidden = [(l, r) for l, r in forbidden if l < r]
    forbidden.sort()
    merged = []
    for l, r in forbidden:
        if not merged or l > merged[-1][1]:
            merged.append([l, r])
        else:
            merged[-1][1] = max(merged[-1][1], r)
    forb_meas = sum((r - l) for l, r in merged)
    safe_count = len(merged)
    if merged and merged[0][0] > 0: safe_count += 1
    if merged and merged[-1][1] < 1: safe_count += 1
    return 1 - forb_meas, max(1, safe_count)

print(safe_measure_and_intervals([1,2,3,4,5,7,8,9,10,11,12,13,14]))
# (0.03294101731601732, 13)
```

FACT: The pair (≈0.03294, 13) is the exact output of the interval code on that 13-set.  
PROOF: Each safe interval of length L is crossed by at most ⌊vL⌋+2 windows of width 1/(8v), giving the displayed linear loss.  
Least-sure step: the precise interaction term when two large speeds are added simultaneously. UNFINISHED: any numerical claim not produced by the code block.

--- end verbatim ---
END LETTER
