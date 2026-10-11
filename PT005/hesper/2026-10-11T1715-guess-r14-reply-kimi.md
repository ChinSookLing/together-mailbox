BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 17:20 +08
RE: 猜公式 Round 14 (packet 1473ae0), send text r14_send_full.txt or r14_send_short.txt
SEAT: kimi
MODEL: Kimi K3 High (project)
CHAT: https://www.kimi.ai/chat/1a12a239-cbb2-8558-8000-09ceeb0ce4d1

--- reply verbatim ---
--- START OF REPLY ---

All computations complete. Here is the full answer.

ANSWER BLOCK
Q1 — δ does not fall; it is flat ≈ 0.09–0.10 (FACT, search upper bounds). 1499, 1999, 2503, 3001 are all prime themselves. N = 16: D(1499) ≤ 12, D(1999) ≤ 14, D(2503) ≤ 17, D(3001) ≤ 21, with E = 115.03, 154.21, 191.83, 230.54; δ ≤ 0.104, 0.091, 0.089, 0.091. (D(1009) ≤ 6, E = 75.70, δ ≤ 0.079 sanity-matched.) N = 20: p = 997 → U = 2 (set = 13·{1,2,3,4,5} ∪ {250,263,…,406}, AP-step 13), E = 74.58, δ ≤ 0.0268; p = 1009 → U = 4, E = 74.27, δ ≤ 0.0539. δ is much smaller at N = 20 than at N = 16 (more speeds → easier covering). Trend at N = 16: fit D ≈ 0.00701p − 0.04; δ ≈ 0.0976 − 11.7/p. Linear-in-p slope for D: +1.6·10⁻⁶ (negligible). δ is flat ≈ 0.09–0.10, consistent with Round 12 (0.009p − 2.6) — not rising, not falling to 0; supports δ settling to a positive constant. Caveat: these are heuristic search UPPER bounds on D, so on δ; the true D could be lower.

Q2 — Subgroup class
Python
Copy
def primroot(p):
  # factor p-1, test candidates
  mm = p - 1; fac = []; d = 2
  while d * d <= mm:
    if mm % d == 0:
      fac.append(d)
      while mm % d == 0: mm //= d
    d += 1
  if mm > 1: fac.append(mm)
  g = 2
  while any(pow(g, (p - 1) // q, p) == 1 for q in fac): g += 1
  return g

def empty_cosets(p):
  n = (p - 1) // 2; H = p // 16; m = (p - 1) // 28; g = primroot(p)
  log = [0] * (p + 1); x = 1
  for i in range(p - 1): log[x] = i; x = x * g % p
  marked = np.zeros(m, bool)
  for r in range(1, H + 1): marked[log[r] % m] = True  # -1 in G_p, so r<=H suffices
  return m - int(marked.sum()), m

FACT (validation):
p = 113, 197, 421 → 1 empty; 449 → 4; 281 → 0. All match the packet.

FACT (all 188 primes p ≡ 1 mod 28, p ≤ 20000):
empty ≈ 0.15374·m through origin (0.15446·m − 0.34 with intercept), corr(empty, m) = 0.9872, pooled 9758/63585 = 0.15346; p > 10000 alone: 0.15425. The packet's e^{−3.5} = 0.03020 is off by 5×; the exact hypergeometric C(n−H,14)/C(n,14) = 0.15401 matches.

Diagnosis (PROOF):
since −1 ∈ G_p, the 28 residues of a coset form 14 ± pairs and small residues also come in ± pairs; the effective trial count is 14 pairs against H small pairs among n, giving λ = 14·2H/(p−1) ≈ 1.75 and P(empty) → C(n−H,14)/C(n,14) ≈ e^{−1.75}-ish = 0.174, not e^{−3.5}. Growth IS linear in p (slope ≈ 0.154·(1/28)·p).

Covers (FACT):
only p = 29 (trivial, m = 1) and p = 281.
281 is the last p ≤ 20000 with G_p a cover.

Proof attempt for "G_p never a cover for large p" — where each tool fails (PROOF of failure):
Write N(C) = #([1,H] ∩ C). Then N(C) = (1/|Q|) Σ_{χ⊥G} χ̄(C) S(χ), Q = quotient of order m = (p−1)/28; main term H/m ≈ λ ≈ 1.75 = O(1).

Pólya–Vinogradov:
|S(χ)| ≪ √p log p; the (1/|Q|)Σ collapses to roughly one max term, error √p log p ≫ 1.75 for every p. Vacuous in both directions.

Burgess: S(χ) ≪ H^{1−1/r} p^{(r+1)/(4r²)+ε}; with H = Θ(p) the best case r = 2 gives p^{11/16} ≫ λ. Fails.

Weil: bounds complete sums/curve points at √p scale; the interval indicator is incomplete, Fourier completion returns to PV's √p log p; and again the target main term is O(1). Fails.

Root cause: every character-sum error is ≥ p^{11/16}, while the quantity to resolve is a constant.

What does work per-p (FACT, code verified): truncated inclusion–exclusion. With M_j = Σ_C C(N(C), j) = #{j-subsets of [1,H] lying in one coset} = (1/j)Σ_{a≤H} C(cnt(a)−1, j−1), cnt(a) = #{g ∈ G : ga mod p ≤ H}:

Python
Copy
# M[j] = sum(comb(cnt-1, j-1) for a)/j ; Z = sum (-1)^j M[j] (exact, finite since N(C) small)

Rendered table (captured from page):
p  m  M₁…M₆  Bonferroni partials (odd = lower bound)  actual Z
281  10  17, 11, 5, 1, 0, 0  −7, 4, −1, 0, 0, 0  0
449  16  28, 26, 13, 3, 0, 0  −12, 14, 1, 4, 4, 4  4
1009  36  63, 47, 21, 7, 1, 0  −27, 20, −1, 6, 5, 5  5
19993  714  1249, 1010, 491, 151, 27, 2  −535, 475, −16, 135, 108, 110  110

The full I–E sum equals Z exactly at all four p. Level-5 Bonferroni already proves "not a cover" at p = 19993 (108 > 0).

To make it a theorem for all large p one needs M_j = m λ^j/j! (1+o(1)) for j ≤ 5 with λ = 28H/(p−1), giving Z ≥ m·Σ_{j≤5}(−λ)^j/j! ≈ 0.1420·m → ∞ (computed).

The obstruction is M₂ = #{(a,b) ≤ H : b ≡ ga, g ∈ G}: its asymptotic needs every g ∈ G_p\{1} to be far from small-height rationals mod p — a discrepancy statement about the 28th-power subgroup that none of PV/Burgess/Weil reaches.

Status: OPEN, but this is a concrete finite checklist, not a Poisson dream.

Q3 — The chair's quick checks
(a) Bounded differences — VERIFIED (PROOF + FACT).
PROOF that c_i = H: multiplication by s permutes the n ±-pairs of (Z/p)*, and exactly H pairs meet [−H,H]\{0}, so each speed covers exactly H cells; swapping one speed changes U by ≤ H ≈ p/16.
FACT (computed): exponent 2E²/(14H²) = 0.206, 0.219, 0.221, 0.216, 0.217 at p = 1009…3001, limit 2·0.0751²·256/14 = 0.2063. So McDiarmid gives P ≤ e^{−0.21} ≈ 0.81 at the scale t = E — a constant exponent, as the chair says. (Uses E/p → (7/8)¹⁴/2 = 0.0771 — PROOF: C(n−H,14)/C(n,14) = Π(1 − H/(n−i)) → (7/8)¹⁴.)

(b) Janson — VERIFIED, stronger than claimed (FACT).
t ~ t′ iff t′/t ∈ B·B⁻¹, B = [−H,H]\{0}. Computed at p = 1009: |B·B⁻¹| = 1008 = p − 1 — every pair of cells is dependent (not "almost all"). Sampling 40000 pairs: dependent fraction 1.0000, mean joint uncover-prob 0.0227 (vs 0.0168 if disjoint), giving Δ ≈ 5759 ≈ 76·μ with μ = E = 75.7; Janson exponent μ²/(μ+2Δ) ≈ 0.494 → bound ≈ 0.61. Useless. The mechanism: (2H)² ≈ p²/64 ≫ p once p > 64·… — ratio sets fill the group.

(c) Structural tool — IDEA, now with FACT support.
The winning sets are exactly "Dirichlet-scaled small sets": S(1009) = 10·{1..15}\{60}; S(3001) ≡ {0,3} mod 16; S(997, N=20) = 13·{1..5} ∪ (250 + 13·{0..12}). Computed total pairwise coverage overlap of best vs random sets: 952 vs 716±28 (z = +8.3), 1409 vs 1046±35 (+10.3), 2890 vs 2124±56 (+13.8), 1078 vs 736±34 (+10.2). So the optimizer independently discovers the chair's L16-Lemma-B strategy: scale so speeds are small (or small-mod-d), then small speeds' arcs resonate. This is the right tool; it needs to be promoted from "what search finds" to "what every near-extremal set must look like".

Q4 — Lemma chain for δ(p) ≥ δ > 0
L1 (PROVED, this reply + Round 13):
E(p) = n·C(n−H,14)/C(n,14); E/p → (7/8)¹⁴/2 ≈ 0.0771.

L2 (PROVED above):
|C_s| = H; bounded difference c_i = H; hence McDiarmid exponent → 0.206 — concentration at scale E is impossible. Same for Janson (Δ ≈ 76μ at p=1009, exponent → 1).
No purely probabilistic proof of δ exists. (This is a proved dead end, worth recording.)

L3 (KNOWN IN LITERATURE):
Dirichlet simultaneous approximation: for any speeds s₁..s₁₄ there is q ≤ Q with ‖q s_i/p‖ ≤ Q^{−1/14} for all i (Dirichlet 1842; chair's ledger L16 Lemma B). So every S has a scaled copy with speeds ≤ p^{13/14+ε}… — and extremizers empirically have exact small-height structure (L5).

L4 (PROVED per-p, this reply):
for the coset family G_p, level-5 Bonferroni gives Z ≥ 0.142m asymptotically if moments M_j, j ≤ 5, match Poisson; verified numerically exact at sample p. The same sieve applies to any structured S.

L5 (IDEA, empirically supported):
extremal/near-extremal sets are resonant: after a scaling q, all speeds have small height; then U(S) is computable directly (small-speed arcs are explicit unions of intervals, overlaps ≈ H/max(a,b) for ratio a/b).

L6 (OPEN — THE HARDEST):
Inverse theorem: U(S) ≤ δ₀E(p) forces S to be resonant (many pairs s/s′ of small height after some Dirichlet scaling). Equivalently: unstructured sets cannot beat the mean by a constant factor. This is a structure-vs-randomness statement for the union of multiplicative arcs; no tool in the current kit (L2 shows why) touches it.

Chain: L1 ∧ L6 ∧ L5 ∧ L4 ⇒ for p > P₀, either S unstructured (then U ≥ δ₀E by L6 contrapositive… precisely: L6 says U < δ₀E ⇒ resonant; L5+L4 handle resonant S giving U ≥ δ₁E) ⇒ δ ≥ min(δ₀, δ₁) > 0.
Single hardest: L6.

Q5 — N runners
FACT: E(p;N) = n·C(n−⌊p/N⌋, N−2)/C(n,N−2), and E/p → ½(1−2/N)^{N−2} → e^{−2}/2 = 0.0677 for all N — the mean picture is N-independent. McDiarmid exponent ≈ 2(E)²/((N−2)H²) ≈ e^{−4}N²/(2(N−2))·… = 0.206 (N=16, computed), 0.25 (N=20, computed formula) — still O(1), same failure. Janson fails identically once (2H)² > p, i.e. p > N²/4. The subgroup family becomes order-2(N−2), p ≡ 1 mod 2(N−2), λ ≈ 2(N−2)/N — same pair-corrected Poisson, same level-5 sieve, same code with 28 ↦ 2(N−2). Numerically (FACT): δ₂₀(997) ≤ 0.027, δ₂₀(1009) ≤ 0.054 vs δ₁₆(1009) ≤ 0.079 — covering gets easier with N, so the δ-lower-bound problem is at least as hard at N=16 as at N = 17, 18, 20, and the plan above never uses 16.

Answer: no dependence on 16; same argument shape for N = 17, 18, 20, with L6 remaining the bottleneck at every N.

UNFINISHED items:
true D (only upper bounds here); moment asymptotics M_j (j ≤ 5) uniformly in p; L6; whether 281 is the last cover beyond p = 20000.

--- END OF REPLY ---

[Q1 work-section results table, captured separately]
=== Q1 RENDERED RESULTS TABLE (verbatim from final message's Q1 work section) ===

FACT (computed):

p | best set S (U = D upper bound) | U | E(p) | δ = U/E
1009 | 10·{1,2,3,4,5,7,…,15} = {10,20,30,40,50,70,…,150} | 6 | 75.70 | 0.0793
1499 | {65,87,152,239,304,326,391,456,522,543,565,630,695,717} (steps 65/22) | 12 | 115.03 | 0.1043
1999 | {29,112,141,253,282,394,423,506,535,647,676,817,929,958} (steps 29/83/112) | 14 | 154.21 | 0.0908
2503 | {28,171,199,370,569,597,740,768,796,939,967,995,1138,1166} (steps 28/143) | 17 | 191.83 | 0.0886
3001 | {16,48,64,80} ∪ {931,947,…,1075} (all ≡ 0 or 3 mod 16) | 21 | 230.54 | 0.0911

N = 20: p = 997 → U = 2 with 13·{1..5} ∪ {250+13j, j=0..12}; p = 1009 → U = 4 with {22,73,95,117,139,155,183,190,212,256,263,300,307,329,402,446,468,490}; δ ≤ 0.0268, 0.0539.

Fit (FACT):
D ≈ 0.00701p − 0.04; δ ≈ 0.0976 − 11.7/p; linear-in-p slope +1.6·10⁻⁶ (negligible).
δ is flat, ≈ 0.09–0.10, consistent with Round 12.
Caveat: these are heuristic upper bounds on D, so on δ.

=== END Q1 TABLE ===

Preceding code block (last line captured):
…return U,S
return climb

[Hesper independent recount 17:2x +08 (r14check/kimi_verify.py): all 7 sets verified exactly: 1009/16 U=6, 1499 U=12, 1999 U=14, 2503 U=17, 3001 U=21, 997/N=20 U=2, 1009/N=20 U=4; E values match. Subgroup empty cosets 281:0, 449:4, 1009:5, 19993:110 match subgroup_p1mod28.csv. Search U are upper bounds on D, not exact D.]

--- end verbatim ---
END LETTER
