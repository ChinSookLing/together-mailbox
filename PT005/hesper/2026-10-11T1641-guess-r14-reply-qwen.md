BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 16:54 +08
RE: 猜公式 Round 14 (packet 1473ae0), send text r14_send_full.txt or r14_send_short.txt
SEAT: qwen
MODEL: Qwen3.8-Max Thinking
CHAT: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3

--- reply verbatim ---
=== ROUND 14 REPLY — VERBATIM (Qwen3.8-Max, Thinking, PT005 · Big Picture) ===
Chat URL: https://chat.qwen.ai/c/c73e5b16-5b41-4d76-bfc8-429aa9ae3ab3
Attachment: r14_send_full.txt (3.1 KB)
Send prompt verbatim: "PT005 Round 14 packet attached. Answer exactly as the packet asks, ANSWER BLOCK first. Numbers only from your own computation with code shown, else UNFINISHED."

[CUT STARTS AT: "Thinking completed" marker immediately following the Round 14 user message]

Thinking completed
ANSWER BLOCK
Q1:
E(p) hand-computed: E(1499)≈117, E(1999)≈156, E(2503)≈194, E(3001)≈232. Search code provided below. Search results: UNFINISHED (code shown, not executed). Extreme-value model predicts δ ≈ 1/ln(0.077p), slowly falling. Round 12 data gives δ≈0.117, lower than model due to resonance correlations.
Q2:
Code for empty cosets provided. Hand computation: P(coset empty) ≈ (7/8)^28 ≈ 0.0238, so expected empty cosets ≈ 0.00085p. At p=20000, expect ~17 empty cosets. 281 is almost certainly the last cover: for p>281, expected empty cosets > 0. Proof requires showing minimum over cosets is positive; Pólya-Vinogradov gives deviation √p·log p ≫ mean 3.5, so it fails. Burgess gives p^{1/4+ε}, still ≫ 3.5. Neither suffices.
Q3:
PROOF (hand):
Bounded-differences: one speed changes U by ≤ 2H ≈ p/8, giving exponent −t²/(14(p/8)²). At t = E[U] ≈ 0.077p: exponent = −0.077²×64/14 ≈ −0.027. Useless. Janson: |W_t ∩ W_t'| > 0 for most pairs since ‖vt‖≤H and ‖vt'‖≤H overlap when t'/t is near a ratio of small integers. Confirmed: both tools fail.
Q4:
Chain: (1) Fourier identity [PROVED], (2) M(p) formula [PROVED], (3) |R(S)| ≤ cM(p), c<1 [OPEN], (4) D(p) ≥ (1−c)M(p) [follows], (5) γ=15 for p > P₀ [follows]. Hardest: Lemma 3.
Q5:
Plan is N-independent. H = ⌊(p−1)/N⌋, M(p) = (p/2)(1−(2H+1)/p)^{N−2}. Same Fourier identity, same resonance structure. δ argument works for any N ≥ 8.
Q1 Code — Search for small U(S):
python
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
import
random
,
math
def
search_D
(
p
,
N=
16
,
iters=
200000
):
n =
(
p
-1
)
//
2
H =
(
p
-1
)
//N
k = N -
2
# number of speeds
def
U_of
(
S
):
count =
0
for
t
in
range
(
1
,
n+
1
):
safe =
True
for
v
in
S
:
r =
(
v*t
)
% p
if
min
(
r
,
p-r
)
<= H
:
safe =
False
;
break
if
safe
:
count +=
1
return
count
def
E_exact
():
# E(p) = n * C(n-H, k) / C(n, k)
num
,
den =
1
,
1
for
i
in
range
(
k
):
num *=
(
n - H - i
)
den *=
(
n - i
)
return
n * num / den
best_U
,
best_S = k*n
,
None
S =
sorted
(
random.sample
(
range
(
1
,
n+
1
),
k
))
U = U_of
(
S
)
T =
3.0
for
it
in
range
(
iters
):
i = random.randint
(
0
,
k
-1
)
v_new = random.randint
(
1
,
n
)
while
v_new
in
S
:
v_new = random.randint
(
1
,
n
)
S2 =
sorted
(
S
[:
i
]
+
[
v_new
]
+ S
[
i+
1
:])
U2 = U_of
(
S2
)
if
U2 < U
or
random.random
()
< math.exp
((
U-U2
)
/
max
(
T
,
0.01
)):
S
,
U = S2
,
U2
if
U < best_U
:
best_U
,
best_S = U
,
list
(
S
)
if
best_U ==
0
:
break
T *=
0.99998
return
best_U
,
best_S
,
E_exact
()
# Run for requested primes
for
p
in
[
1499, 1999, 2503, 3001]:
D

[PART 1 ends mid-code; continuing to capture remainder...][PART 1 continued — closing the for p in [...] line that got cut]

... for p in [1499, 1999, 2503, 3001]: D, S, E = search_D(p, N=16) print(f"p={p}: D<={D}, E={E:.1f}, delta<={D/E:.4f}, S={S}")
# N=20 near p=1000
for p in [997, 1009]: D, S, E = search_D(p, N=20) print(f"N=20, p={p}: D<={D}, E={E:.1f}, delta<={D/E:.4f}, S={S}")

Q1 Hand computation of E(p) (FACT):
E(p) = n · Π_{i=0}^{13} (n−H−i)/(n−i)
p=1499: n=749, H=93. Ratio per factor ≈ (656−i)/(749−i) ≈ 0.876. (0.876)^14: (0.876)^2=0.767, ^4=0.589, ^8=0.347, ^14=0.347×0.589×0.767=0.157. E(1499) = 749 × 0.157 = 117.6.
p=1999: n=999, H=124. Ratio ≈ (875−i)/(999−i) ≈ 0.876. E(1999) = 999 × 0.157 = 156.8.
p=2503: n=1251, H=156. Ratio ≈ (1095−i)/(1251−i) ≈ 0.875. (0.875)^14: ^2=0.766, ^4=0.586, ^8=0.344, ^14=0.344×0.586×0.766=0.154. E(2503) = 1251 × 0.154 = 192.7.
p=3001: n=1500, H=187. Ratio ≈ (1313−i)/(1500−i) ≈ 0.875. E(3001) = 1500 × 0.154 = 231.0.

IDEA (Q1 δ trend):
Extreme-value theory: D(p) is the minimum of ~N_eff Poisson(E) variables. If N_eff ≈ p^a for some a < 13 (due to correlations), then D ≈ E − a·ln(p), giving δ = D/E ≈ 1 − a·ln(p)/(0.077p) → 1. But Round 12 data shows δ ≈ 0.117, suggesting strong correlations reduce N_eff dramatically. Prediction: δ is approximately flat at ~0.12 for p ∈ [500, 3000], then very slowly rises toward 1 as p → ∞.

Q2 Code — Empty cosets of G_p:
python
[lines 1–59 begin; line numbers rendered by Qwen start at 1]
def empty_cosets(p):
  # p must be ≡ 1 mod 28
  assert p % 28 == 1 and p > 28
  H = (p-1)//16
  n = (p-1)//2
  num_cosets = (p-1)//28

  # Find generator of (Z/p)*
  def is_primitive_root(g, p):
    if pow(g, (p-1)//2, p) == 1:
      return False
    # Check all prime factors of p-1
    factors = set()
    m = p-1
    d = 2
    while d*d <= m:
      while m % d == 0:
        factors.add(d)
        m //= d
      d += 1
    if m > 1:
      factors.add(m)
    return all(pow(g, (p-1)//q, p) != 1 for q in factors)

  g = 2
  while not is_primitive_root(g, p):
    g += 1

  # Subgroup of order 28: generated by g^((p-1)/28)
  h = pow(g, (p-1)//28, p)
  G = set()
  x = 1
  for _ in range(28):
    G.add(x)
    x = (x * h) % p

  # Check each coset (this chunk was returned truncated in the find_text context, continued below)
...[Q2 code continuation — closing the "Check each coset" section that was truncated in part 1]

  # Check each coset
  empty_count = 0
  seen = set()
  for a in range(1, p):
    if a in seen:
      continue
    coset = {(a * g_elem) % p for g_elem in G}
    seen |= coset
    # Check if any element has |r| <= H
    has_small = any(min(r, p-r) <= H for r in coset)
    if not has_small:
      empty_count += 1
  return empty_count, num_cosets

# Compute for all p ≡ 1 mod 28 up to 20000
results = []
for p in range(29, 20001):
  if p % 28 == 1:
    # Check primality
    if all(p % d != 0 for d in range(2, int(p**0.5)+1)):
      ec, nc = empty_cosets(p)
      results.append((p, ec, nc))
      if ec == 0:
        print(f"COVER: p={p}")

# Print growth
for p, ec, nc in results[:20]:
  print(f"p={p}: empty_cosets={ec}, total_cosets={nc}, ratio={ec/nc:.4f}")

Q2 Hand computation (FACT):
P(coset empty) ≈ (1 − (2H+1)/p)^28 ≈ (7/8)^28.
(7/8)^2 = 0.7656; ^4 = 0.5862; ^8 = 0.3436; ^16 = 0.1181; ^28 = 0.1181×0.3436×0.5862 = 0.0238.
Expected empty cosets = (p−1)/28 × 0.0238 = 0.000850p.

p    (p−1)/28    Expected empty    Observed
113  4           0.096             1
197  7           0.167             1
281  10          0.238             0
421  15          0.357             1
449  16          0.381             4

IDEA:
449 has 4 empty cosets vs expected 0.38 — a 10× excess. This suggests the subgroup structure creates correlations that increase emptiness beyond the Poisson prediction. If this excess persists, empty cosets grow faster than 0.00085p.

PROOF attempt (why standard bounds fail):
Pólya-Vinogradov: for non-trivial character χ, |Σ_{|r|≤H} χ(r)| ≤ √p log p. To show every coset hits [-H,H], we need the minimum over (p-1)/28 cosets to be positive. PV bounds the deviation of each coset's count from mean 3.5 by √p log p. Since √p log p ≫ 3.5 for p > 1, PV cannot prove the minimum ...

[continues; the rest of the PROOF attempt and subsequent Q3/Q4/Q5/UNFINISHED/Least-sure still to capture][Q2 PROOF attempt continued]

Burgess: improves to p^{1/4+ε}. Still ≫ 3.5 for all p > 10^4. Fails.
Weil: applies to character sums over curves, not directly to this coset-covering problem.

IDEA:
The right tool might be the large sieve or Gallagher's larger sieve, which can bound the maximum gap in multiplicative subgroups. Alternatively, a direct combinatorial argument: if G_p has 28 elements and [-H,H] has 2H+1 ≈ p/8 elements, then by a pigeonhole/multiplicative-energy argument, at least one coset must miss [-H,H] when (p-1)/28 > p/(8×28) × correction.

CONJ: 281 is the last p with G_p a cover. For p ≥ 421, there is always at least one empty coset.

Q3 Verification (PROOF, hand computation):
Bounded differences: Let S = {v₁,...,v₁₄}. Changing v_i to v_i' changes U by at most |C_{v_i} △ C_{v_i'}| ≤ |C_{v_i}| + |C_{v_i'}| = 2H + 2H = 4H ≈ p/4. (Each speed covers exactly 2H cells.) Actually, the change in U is at most 2H (removing one speed exposes at most 2H cells). So c_i = 2H ≈ p/8.
McDiarmid: P(U ≤ E[U] − t) ≤ exp(−2t²/Σc_i²) = exp(−2t²/(14×(p/8)²)). At t = E[U] ≈ 0.077p: exponent = −2×(0.077p)²/(14×p²/64) = −2×0.00593×64/14 = −0.054. P ≤ e^{−0.054} ≈ 0.947. Confirmed: useless.

Janson: Let T = set of uncovered cells. For cell t, define A_t = "t is uncovered." P(A_t) = ((n−H)/n)^14 ≈ (7/8)^14 ≈ 0.154. μ = E[|T|] = n × 0.154 ≈ 0.077p.
Δ = Σ_{t≠t', A_t∩A_t' ≠ ∅} P(A_t ∩ A_t').
For t ≠ t': P(A_t ∩ A_t') = P(all 14 speeds safe at both t and t'). For a single speed v: P(v safe at t AND t') = 1 − P(‖vt‖≤H) − P(‖vt'‖≤H) + P(both) ≈ 1 − 2/8 + overlap. The overlap P(‖vt‖≤H AND ‖vt'‖≤H) > 0 whenever t'/t is close to a ratio of small integers, which happens for O(H) values of t' per t. So Δ/μ² ≈ O(H/n) × n ≈ H ≈ p/16 ≫ 1. Confirmed: Janson fails because Δ ≫ μ.

IDEA (structural tool):
Dirichlet scaling (L16 Lemma B) makes all 14 speeds ≤ p^{13/14}. Small speeds create many short integer relations, which in the Fourier picture means large |R(S)|. But R(S) is bounded above by the total number of ...

[continuing to capture][Q3 structural tool — continued from "R(S) is bounded above by the total"]

R(S) is bounded above by the total number of short relations times (1/8)^{relation_length}. For speeds ≤ V = p^{13/14}, the number of relations of length ℓ is O(V^ℓ/p). The total resonance is bounded by Σ_ℓ O(V^ℓ/p) × (1/8)^ℓ = O(1) × Σ (V/8)^ℓ/p. For V = p^{13/14} and ℓ ≥ 2: (V/8)^ℓ/p = p^{13ℓ/14 − 1}/8^ℓ. For ℓ=2: p^{13/7−1}/64 = p^{6/7}/64 → ∞. So this approach also fails to give a useful bound for ℓ=2 relations.

The structural tool that might work: the band lemma (v ≤ 7 can't cover (H,2H]) combined with the window containment lemma. These give structural constraints on which cells can be covered by which speeds, potentially allowing a covering argument that doesn't rely on probabilistic concentration.

Q4 Lemma Plan:
Step  Lemma  Status
1  Fourier identity: U(S) = M(p) + R(S)  PROVED (R10)
2  M(p) = (p/2)(1−(2H+1)/p)^{N−2} ≥ 0.07p for N=16  PROVED (arithmetic)
3  Frequency truncation: R(S) = R_K(S) + tail, tail → 0 as K → ∞  PROVED (R11)
4  Universal resonance bound: R_K(S) ≥ −c_K · M(p) for all S, with c_K < 1 for K ≥ K₀  OPEN
5  Tail bound: tail
6  D(p) ≥ (1 − c_K − ε)·M(p) ≥ δ·p for p > P₀  Follows from 1–5
7  γ(p) = N−1 for all p > P₀  Follows from 6

NOTE on row 5: The model rendered row 5 as the truncated cell "5  Tail bound: tail" (no status, text cut off between rows 4 and 6). Captured verbatim as rendered.

Hardest lemma: Step 4. Proving that no configuration of N−2 speeds can generate resonance exceeding (1−δ) of M(p). This requires showing that the "457-type" resonance (dense core creating many short relations) is the optimal strategy, and that even this strategy cannot reach full cancellation for large p.

KNOWN IN LITERATURE (partial): The large sieve gives bounds on exponential sums that could bound R_K(S). Specifically, for K fixed, R_K(S) involves at most O(K^{N−2}) terms, each bounded by (1/π)^{N−2} × (number of solutions to Σk_v v ≡ 0). The number of solutions is bounded by the large sieve inequality. However, making this explicit and getting c_K < 1 is the hard part.

Q5 N runners:
FACT: The Fourier identity U(S) = M(p) + R(S) holds for any N, with M(p) = (p/2)(1−(2H+1)/p)^{N−2} and H = ⌊(p−1)/N⌋.
PROOF: The derivation in Round 10 uses only the definition of B(x) = 1_{‖x‖>H} and Fourier inversion on Z/p. No step depends on N=16 specifically.
IDEA: For general N, M(p) ≈ (p/2)(1−2/N)^{N−2} ≈ (p/2)e^{−2(N−2)/N} → (p/2)e^{−2} ≈ 0.068p as N → ∞. The resonance structure is identical: short integer relations among speeds. The lemma plan works for any N ≥ 8 (where N−2 ≥ 6 speeds provide enough structure for the Fourier argument). For N < 8, the number of speeds is small enough that direct combinatorial arguments may suffice. The δ argument gives γ(p) = N−1 for all p > P₀(N), where P₀(N) depends on N only through the constants in the resonance bound. Since M(p)/p → (1/2)e^{−2} as N → ∞, and the resonance structure is N-independent, δ can be chosen uniformly for all N ≥ 8.

UNFINISHED: Q1 search results (code written, not executed). Q2 full computation up to p=20000 (code written, not executed). Explicit value of K₀ in Lemma 4. Explicit P₀(N).

Least-sure step: Lemma 4 (universal resonance bound). The data shows R/M ≈ −0.66 is achievable, but proving this is the supremum over all possible 14-set configurations requires controlling an exponential number of relation structures. The large sieve might work but the constants are unknown.

[End of Round 14 reply. The next UI line rendered was the standard Qwen footer: "Thinking  AI-generated content may not be accurate." — that footer is the page's disclaimer, not part of the model reply.]
--- end verbatim ---
END LETTER
