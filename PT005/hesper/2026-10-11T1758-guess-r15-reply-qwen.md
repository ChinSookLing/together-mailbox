BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 18:00 +08
RE: 猜公式 Round 15 (packet 6cfc07f), send text r15_send_full.txt or r15_send_short.txt
SEAT: qwen
MODEL: Qwen3.8-Max Thinking
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
=== METADATA ===
Chat URL: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3
Model: Qwen3.8-Max
Captured at: ~17:58 SGT (11 Oct 2026)
Status: Reply COMPLETE (Thinking completed; action bar with Copy/Regenerate/Good/Bad visible; nothing appended after the reply's Summary of status table)
Reply belongs to: "PT005 · 猜公式 Round 15 (Opus packet 6cfc07f)"
=== VERBATIM REPLY START ===
ANSWER BLOCK
Q1:
From the four interval endpoints I compute m(K*) = 2(7/2496 + 3/704) = 97/6864 = 0.0141317.
Thus δ* = m*/(7/8)^14 = 0.09164 (hand computation).
My independent exhaustive extension to max ≤ 24: UNFINISHED (code shown); so I cannot independently say whether any K beats 97/6864.
Speed 6 is missing because its unsafe band around 1/6, (5/32, 17/96), contains both residual safe intervals.

Q2:
I do not have a proof of a uniform c > 0 for all 14-element integer sets. The conjectural floor c = 97/6864 remains CONJ; an explicit weaker c: UNFINISHED.

Q3:
PROVED here: for fixed finite K, U(u·K mod p) = (p/2)·m(K) + O_K(1).
For arbitrary S, Lemma B can reduce to speeds ≤ p^{13/14} with o(p) error, but the missing uniform continuous floor is still needed.

Q4:
I compute the erratum limit exactly: (7/8)^14 = 678223072849/4398046511104 = 0.15421007.
Expected empty cosets coefficient is this divided by 28: 96889010407/17592186044416 = 0.00550750.
Explicit P0: UNFINISHED. Pólya–Vinogradov/Burgess fail because the mean small elements per coset is only ≈ 3.5.

Q5:
m*_N for N = 17, 18, 20: UNFINISHED (code shown).
Comparison with the N = 20 near-1000 upper bounds therefore also UNFINISHED.

1. Check the floor
1.1 Exact measure from the four intervals
FACT (my hand arithmetic).
The supplied safe intervals in [0, 1/2] are I1 = [33/208, 31/192], I2 = [11/64, 31/176].
Their lengths are |I1| = 31/192 − 33/208 = (403 − 396)/2496 = 7/2496,
|I2| = 31/176 − 11/64 = (124 − 121)/704 = 3/704.
Mirror symmetry about 1/2 doubles the total: m(K*) = 2(7/2496 + 3/704).
Common denominator 27456: 7/2496 = 77/27456, 3/704 = 117/27456.
So m(K*) = 2·(194/27456) = 194/13728 = 97/6864.
FACT (decimal). 97/6864 = 0.0141317016…

1.2 Why speed 6 is the missing speed
PROOF.
Speed 6 is unsafe when ‖6x‖ < 1/16.
Near 1/6, this is the interval (1/6 − 1/96, 1/6 + 1/96) = (15/96, 17/96) = (5/32, 17/96).
Check containment of I1: 33/208 > 5/32 ⟺ 33·32 > 5·208 ⟺ 1056 > 1040,
31/192 < 17/96 ⟺ 31·96 < 17·192 ⟺ 2976 < 3264.
Check containment of I2: 11/64 > 5/32 ⟺ 11 > 10,
31/176 < 17/96 ⟺ 31·96 < 17·176 ⟺ 2976 < 2992.
Thus both positive-half safe intervals lie inside the unsafe band of speed 6. Their mirrors lie inside the unsafe band near 5/6. Therefore adding 6 kills the entire safe set of K*.
IDEA.
This explains the Round 3 link: among {1,…,15}, speed 6 is the one whose unsafe intervals exactly cover the tiny residual gaps left by the other fourteen.

1.3 Code for exact recomputation
Code (not executed in this reply).
python
from fractions import Fraction as F

def bad_length(K, N=16):
    bad = []
    for k in K:
        r = F(1, N*k)
        for j in range(k):
            a = F(j, k) - r
            b = F(j, k) + r
            if a < 0:
                bad.append((F(0), b))
                bad.append((1 + a, F(1)))
            elif b > 1:
                bad.append((a, F(1)))
                bad.append((F(0), b - 1))
            else:
                bad.append((a, b))
    bad.sort()
    if not bad:
        return F(0)
    total = F(0)
    cur_a, cur_b = bad[0]
    for a, b in bad[1:]:
        if a > cur_b:
            total += cur_b - cur_a
            cur_a, cur_b = a, b
        elif b > cur_b:
            cur_b = b
    total += cur_b - cur_a
    return total

def safe_measure(K, N=16):
    return F(1) - bad_length(K, N)

Kstar = tuple(k for k in range(1, 16) if k != 6)
# safe_measure(Kstar, 16) should equal Fraction(97, 6864)

1.4 Exhaustive extension
Code (not executed in this reply).
python
from itertools import combinations
best = (F(1), None)
for M in range(21, 25):  # extend to max <= 24
    for K in combinations(range(1, M+1), 14):
        v = safe_measure(K, 16)
        if v < best[0]:
            best = (v, K)
    print(best)

UNFINISHED.
I did not execute this exhaustive search, so I cannot report an independent maximum reached or an independent yes/no on whether some K beats 97/6864.

2. Prove a floor for all K
OPEN.
I cannot prove a uniform explicit c > 0 for every 14-element set of positive integers.
CONJ.
The natural conjecture from the continuous floor is m(K) ≥ 97/6864 for every 14-element set K ⊂ Z>0.
IDEA (possible route).
Split K into small and large speeds. Large speeds should behave close to independently, giving safe measure near (7/8)^14 ≈ 0.154, much larger than 97/6864. Small speeds can be exhausted. The missing step is a rigorous reduction saying: if max K > B, then m(K) is already larger than 97/6864. I do not have this reduction.
FACT (my computation).
The random-like benchmark is (7/8)^14 = 678223072849/4398046511104 = 0.1542100728…
This is much larger than 97/6864 = 0.0141317, so the extremal sets must be highly arithmetic, not random-like.

3. From discrete to continuous
3.1 Fixed-K asymptotic
PROOF.
Fix a finite set K of positive integers. Let A_K(α) = {x ∈ [0, 1/2] : ‖kx‖ ≥ α ∀ k ∈ K}.
3.1 Fixed-K asymptotic
PROOF.
Fix a finite set K of positive integers. Let A_K(α) = {x ∈ [0, 1/2] : ‖kx‖ ≥ α ∀ k ∈ K}.
For threshold 1/16, meas(A_K(1/16)) = m(K)/2 by symmetry x ↦ 1 − x.
For prime p, cells are t = 1,…,(p−1)/2. The discrete safe condition is ‖kt/p‖ ≥ (H+1)/p, H = ⌊(p−1)/16⌋.
Set α_p = (H+1)/p = 1/16 + O(1/p).
For fixed K, the boundary of A_K(α_p) consists of O_K(1) intervals whose endpoints move by O(1/p) when α changes by O(1/p).
Counting grid points t/p in a finite union of intervals gives
#{t : t/p ∈ A_K(α_p)} = p·meas(A_K(α_p)) + O_K(1).
Therefore U(K mod p) = p(m(K)/2 + O(1/p)) + O_K(1) = (p/2)m(K) + O_K(1).
Scaling by a unit u permutes nonzero residue classes and preserves the identification t ∼ −t, so U(u·K mod p) = U(K mod p).
Thus U(u·K mod p) = (p/2)m(K) + O_K(1).

3.2 Check against Round 14 upper bounds
FACT (my hand arithmetic).
Since (p/2)m(K*) = 97p/13728, I compute:
p = 1999: 97·1999/13728 = 14.1246…
p = 2503: 97·2503/13728 = 17.6859…
p = 3001: 97·3001/13728 = 21.2046…
These are consistent with the reported best upper bounds 14, 17, 21.

3.3 Arbitrary sets
IDEA.
An arbitrary set S can fail to look like a dilate of a fixed small K. Lemma B of L16 gives a scaling with all speeds ≲ p^{13/14}. If one had a uniform continuous floor for all 14-sets with entries ≤ p^{13/14}, the fixed-K argument would give U(S) ≥ (p/2)c − o(p). But the required uniform floor is exactly the open part of Q2.

4. Subgroup theorem: making P0 explicit
4.1 Erratum limit
FACT (my hand arithmetic).
Since −1 ∈ G_p, a coset up to sign has 14 cells. If those cells are modeled as independent uniform residues, the probability that a coset has no element with |r| ≤ H is asymptotically (1 − 1/8)^14 = (7/8)^14.
I computed above: (7/8)^14 = 678223072849/4398046511104 = 0.1542100728…
[Continuation of 4.1 Erratum limit]
The number of cosets is (p−1)/28, so the expected number of empty cosets is asymptotically ((p−1)/28)·(7/8)^14.
The coefficient is (1/28)·(7/8)^14 = 7^13 / (4·8^14) = 96889010407 / 17592186044416 = 0.0055075026…
So the Poisson picture predicts about 0.0055075 p empty cosets.

4.2 Why standard character-sum bounds fail
PROOF (failure mechanism).
Let I = {r : |r| ≤ H}. For a coset C, let X_C = |C ∩ I|.
The average is |I| / ((p−1)/28) ≈ (p/8) / (p/28) = 3.5.
To force some coset to have X_C = 0 by character-sum bounds, one would need a deviation bound smaller than this average. Pólya–Vinogradov gives deviations O(√p log p), and Burgess gives roughly O(p^{1/4+ε}). Both are much larger than the constant 3.5 for large p, so neither can force an empty coset.

4.3 Norm / Erdős–Turán route
IDEA.
If a cover forced a short relation Σ_j k_j g^j ≡ 0 (mod p) with small Σ|k_j|, then p | Norm(Σ_j k_j ζ_28^j).
Since φ(28) = 12, |Norm(Σ_j k_j ζ_28^j)| ≤ (Σ_j |k_j|)^{12}.
To get a contradiction, one would need something like Σ_j |k_j| < p^{1/12}.
I do not know how to get such a short relation from the covering property.
UNFINISHED. I cannot make P0 explicit.

4.4 Code for empty cosets
Code (not executed in this reply).
python
def primitive_root(p):
    # short version: test candidates against prime factors of p-1
    from math import gcd
    factors = set()
    m = p - 1
    d = 2
    while d*d <= m:
        while m % d == 0:
            factors.add(d)
            m //= d
        d += 1
    if m > 1:
        factors.add(m)
    g = 2
    while True:
        if all(pow(g, (p-1)//q, p) != 1 for q in factors):
            return g
        g += 1

def empty_cosets_p28(p):
    assert p % 28 == 1
    H = (p - 1) // 16
    g = primitive_root(p)
    h = pow(g, (p-1)//28, p)
    G = {pow(h, j, p) for j in range(28)}
    seen = set()
    empty = 0
    for a in range(1, p):
        if a in seen:
            continue
        C = {(a*x) % p for x in G}
        seen |= C
        if all(min(r, p-r) > H for r in C):
            empty += 1
    return empty

5. Other N
Code (not executed in this reply).
python
def min_safe_measure_N(N, maxv):
    from itertools import combinations
    ksize = N - 2
    best = (F(1), None)
    for K in combinations(range(1, maxv+1), ksize):
        v = safe_measure(K, N)
        if v < best[0]:
            best = (v, K)
    return best

# examples:
# min_safe_measure_N(17, 20)
# min_safe_measure_N(18, 20)
# min_safe_measure_N(20, 22)

UNFINISHED.
I did not compute m*_17, m*_18, m*_20, so I cannot compare them with the N=20 discrete upper bounds near 1000.

Summary of status
Item                                              | Status
m(K*) = 97/6864 from stated intervals             | FACT (hand computation)
Speed 6 kills the residual intervals              | PROOF
Independent exhaustive search beyond max 20        | UNFINISHED
Uniform floor for all 14-sets                     | OPEN / CONJ
Fixed-K discrete asymptotic                       | PROOF
Arbitrary S linear floor                          | OPEN
Empty-coset limit (7/8)^14                        | FACT (hand computation)
Explicit subgroup P0                              | UNFINISHED
m*_N for N = 17, 18, 20                           | UNFINISHED
=== VERBATIM REPLY END ===

--- end verbatim ---
END LETTER
