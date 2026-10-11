BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 18:30 +08
RE: 猜公式 Round 15 (packet 6cfc07f), send text r15_send_full.txt or r15_send_short.txt
SEAT: kimi
MODEL: Kimi K3 Thinking High (via Tuzi)
CHAT: https://www.kimi.ai/chat/1a12a239-cbb2-8558-8000-09ceeb0ce4d1

--- reply verbatim ---
[Kimi K3 Thinking High, reply to the one nudge; pasted by Tuzi from her own screen 2026-10-11 ~18:29 +08. Supersedes trace-only file 7ac2c58.]

# ANSWER BLOCK

**Q1 (FACT).** m(K*) = **97/6864** recomputed exactly; safe set = the four packet intervals; hand check: 2(7/2496 + 3/704) = 97/6864. Exhaustive min extended: max ≤ 20 exact (38,760 sets), and **certified** to max ≤ 24 (1,961,256 sets), 25 (4,457,400), **26 (9,657,700)** via grid lower-bound screen + exact recheck: **nothing beats 97/6864; K\* is the unique minimizer** each time. Omit-one scan: omit-6 gives 0.014132, omit-14 next (0.015696); m({1..15}) = 0. Why 6: at x = 1/6 exactly, only speeds 6 and 12 are unsafe; the four windows are the gaps between arc-edges 33/208 (13-arc at 2/13), 31/192 and 11/64 (12-arc at 1/6), 31/176 (11-arc at 2/11); speed 6's arc (half-width 1/96, twice 12's) would swallow both windows flanking 1/6.

**Q2.** PROOF: m(K) ≥ 1/(120·max K) for every 14-set (F5 gives t\* with margin 1/240; f is max K-Lipschitz). PROOF: recursion m(K∪{M}) ≥ (7/8)m(K) − (ΣK+1)/(4M). Uniform explicit c: **UNFINISHED** — union bound dies (14/8 > 1), recursion dies unless speeds super-increase; this is the same wall as the discrete δ.

**Q3.** PROVED for exact dilates: S = uK mod p ⇒ U(S) ≥ n·m(K) − 2ΣK − 14 (interval-counting vs grid; explicit). For K* this is vacuous below p ≈ 34,250. Medium-complexity regime (dilate of K′ with ΣK′ up to p^{13/14}, the Dirichlet/Lemma-B wall): **UNFINISHED**.

**Q4.** Explicit P₀ route works: norm bound p | Norm(Σk_j ζ₂₈^j) ≤ (Σ|k_j|)¹² + no exact 3-term relations (Conway–Jones) + Erdős–Turán–Koksma ⇒ level-5 Bonferroni positive once p^{1/12} dominates; crossing at ln p ≈ 623 ⇒ **P₀ ≈ 10²⁷¹** (crude constants; data says 281).

**Q5 (FACT, certified to max ≤ 25).** m*₁₇ = 11384/765765 ≈ 0.014866 at {1..15}; m*₁₈ = 139/11934 ≈ 0.011647 at {1..17}∖{6}; m*₂₀ = 55876/8083075 ≈ 0.006913 at {1..17,19}. N=20: (p/2)m*₂₀ = 3.45 vs D(997) ≤ 2; 3.49 vs D(1009) ≤ 4.

---

# WORK

## Q1 — Check the floor (code)

Exact measure by integer endpoint merging: speed k contributes arcs with endpoints (16j ± 1)/(16k); common denominator D = lcm(16k), merge, complement.

```python
def m_exact(K, N=16, components=False):
    K = sorted(K); D = 1
    for k in K: D = lcm(D, N*k)
    iv = []
    for k in K:
        step = D//(N*k)
        for j in range(k+1):
            a = ((N*j-1)*step) % D; b = ((N*j+1)*step) % D
            if a <= b: iv.append((a,b))
            else: iv.append((a,D)); iv.append((0,b))
    iv.sort()
    comp = []; ca, cb = -2, -2
    for a,b in iv:
        if a > cb:
            if ca >= 0: comp.append((ca,cb))
            ca, cb = a, b
        else: cb = max(cb,b)
    comp.append((ca,cb))
    cov = sum(b-a for a,b in comp); m = Fraction(D-cov, D)
    ...
```

**FACT:** m(K*) = 97/6864 = 0.01413170163…; components [33/208, 31/192], [11/64, 31/176], [145/176, 53/64], [161/192, 175/208] (lengths 7/2496, 3/704, 3/704, 7/2496). Hand arithmetic: 2·(7/2496 + 3/704) = 2·(77 + 117)/27456 = 97/6864 ✓ (verified in code). m({1..15}) = **0**; m({1..13,15}) = 0.0156954 ✓ packet. Round-14 match: (p/2)m* = 14.12 / 17.69 / 21.20 vs D ≤ 14 / 17 / 21 ✓; δ ≈ (m*/2)/(E/p) = 0.0920 ✓.

**Exhaustion (FACT).** max ≤ 20: all 38,760 sets exact — unique min K*. Extension by certified screen: grid G = 2¹⁶, arcs expanded by 2 grid units, so any grid-safe cell lies entirely in the true safe set ⇒ true m(K) ≥ grid_m(K); sets with grid_m ≥ 97/6864 cannot beat it (PROOF of certification: truly covered x ⇒ its grid cell center lies in the expanded arc, since |x − i/G| ≤ 1/G and center-rounding ≤ 1/G). Screens: max ≤ 24 (1,961,256 sets, 1 candidate), 25 (4,457,400, 1), 26 (9,657,700, 1) — the only candidate every time is K* itself, exact value 97/6864. **No K with max ≤ 26 beats 97/6864; K\* unique.** (Runner-up at max ≤ 20: {1..13,15}, 0.0156954.)

**Why 6 (PROOF by hand + FACT):** at x = 1/6, ‖kx‖ ≥ 1/6 > 1/16 unless 6 | k, so among {1..15} only k = 6, 12 kill x = 1/6 (checked in code). Arc edges: 33/208 = 2/13 + 1/(16·13); 31/192 = 1/6 − 1/(16·12); 11/64 = 1/6 + 1/(16·12); 31/176 = 2/11 − 1/(16·11) — all four identities verified True. The windows are exactly the gaps flanking 1/6 between the 12-arc and the 13-arc (2/13) and 11-arc (2/11). Speed 6's arc at 1/6 has half-width 1/96 — twice 12's 1/192 — and covers (0.15625, 0.17708) ⊃ both windows; removing 6 (not 12) opens them. Omit-one scan (computed): omit-6 = 0.014132 is the unique min; omit-12 = 0.021279; omit-14 = 0.015695 second best. Also Farey-side: 1/6's neighbors in F₁₅ are 2/13, 2/11 (gaps 1/78, 1/66) — wide, and their arcs are narrow (large k). **IDEA (general rule the data suggests):** the optimum removes the smallest speed dividing a low-height rational whose Farey gap beats its arc width.

## Q2 — A floor for all K

- **PROOF (per-K explicit, uses F5 = Allikvere LRC-15, KNOWN IN LITERATURE):** f(t) = min_{k∈K}‖kt‖ − 1/16 is M-Lipschitz, M = max K (min of k-Lipschitz functions). F5 gives t* with f(t*) ≥ 1/15 − 1/16 = 1/240. Hence f > 0 on an interval of half-length (1/240)/M, so **m(K) ≥ 1/(120·max K) > 0**, explicit.
- **PROOF (recursion, useful for super-increasing tails):** safe(K′) has ≤ ΣK′ components; speed M's arcs (width 1/(8M), spacing 1/M) remove ≤ L/8 + 1/(4M) from a component of length L, so **m(K′∪{M}) ≥ (7/8)m(K′) − (ΣK′+1)/(4M)**.
- **UNFINISHED (uniform c):** the union bound needs 14·(1/8) = 7/4 > 1 — dead; the recursion loses (ΣK′+1)/(4M), which is O(1) per step unless speeds super-increase — chaining it only handles K with a super-increasing tail above 26 (where the exhaust gives the base 97/6864). The missing lemma: *the number of components of safe(K′) times arc-density of a large speed cannot synchronize* — a component-count bound for safe sets independent of ΣK′. Mark **OPEN**. (This is the continuous shadow of Round-14 L6.)

## Q3 — Discrete to continuous (inverse step)

**PROVED (dilate case, explicit constants):** Let S = u·K mod p, gcd(u,p) = 1, K = {k₁,…,k₁₄} ⊂ ℤ⁺, n = (p−1)/2. Cells x ↔ t = x/p; covered iff ‖k t‖ ≤ H/p. The set {‖kt‖ ≤ c} is 2k intervals; a regular grid with spacing 1/p miscounts each interval by ≤ 1, and |H/p − 1/16| < 1/p shifts each speed's measure by ≤ 2/p, so
**U(S) ≥ n·m(K) − 2ΣK − 14.**
For K* (ΣK* = 114): positive only once p ≳ 34,250 — so this bound explains the asymptotics (D ≈ (p/2)m* at p ≥ 1999) but is vacuous at p = 457 (where D = 0 occurs; consistent, since the error 2ΣK = 228 ≫ (p/2)m* ≈ 3.2). **FACT:** matches the R14 observation that dilates of K* attain the floor once p is large.
**Where a set fails to be a dilate of small K (PROOF of the dichotomy wall):** Lemma B (Dirichlet) gives u with scaled speeds k_i = us_i mod p ∈ [−B, B], B = p^{13/14} — dimension 14 caps Dirichlet at exponent 1/14. If B = O(1) we are in the PROVED case. If B ∈ [ω(1), p^{13/14}] the error 2ΣK′ ≈ p^{13/14} ≫ U ≈ E — the bound is vacuous exactly there. **What it then pays (IDEA, quantification OPEN):** no short dual-lattice vector ⇒ Fourier coefficients of the coverage indicator at heights ≤ B vanish off the trivial mode ⇒ U ≈ E via the subtorus method; making that quantitative needs Weyl-sum control at medium height — the same norm-relation wall as Q4 (p^{1/12}). **Stated exactly:** I prove U(S) ≥ (p/2)m(K) − 2ΣK − 14 for exact dilates, and nothing uniform beyond it; the bridge over the medium regime is **UNFINISHED**.

## Q4 — Explicit P₀ for the subgroup theorem

**PROOF-sketch with crude explicit constants (crossing is FACT of arithmetic):**
(i) If Σk_j g^j ≡ 0 (mod p) and α = Σk_j ζ₂₈^j ≠ 0, then p | Norm(α) and |Norm(α)| ≤ (Σ|k_j|)^{φ(28)} = (Σ|k_j|)¹²; so no nontrivial relation with Σ|k_j| < p^{1/12}. Exact 3-term relations don't exist (Conway–Jones: for 28 = 2²·7 the minimal vanishing sums are 2-gons and 7-gons; three directions can't form a 7-gon), so the norm bound applies to t₁g^i + t₂g^j − r with |t₁|+|t₂|+|r| < p^{1/12}.
(ii) Hence all 2- and 3-term character frequencies obey ‖(Σt_a g^{i_a})/p‖ ≥ (1/3)p^{−11/12} for |t| ≤ p^{1/12}/3.
(iii) Erdős–Turán–Koksma (dim ≤ 4, constant 3, safety factor 3): moment error err_j ≤ C(28, j−1)·9^j·p^{11/12}(ln p)^{j−1}.
(iv) Level-5 Bonferroni needs (p/28)·0.1420 > Σ_{j=2..5} err_j (0.1420 = Σ_{j≤5}(−1.75)^j/j!, computed). Log-space bisection: crossing at **ln p ≈ 623.2, P₀ ≈ 10²⁷¹** (computed). **CONCLUSION:** P₀ is explicit but astronomical; tightening (Burgess-type inputs, better ET constants, level-7 sieve) is where any improvement lives; empirically the last cover is p = 281.

## Q5 — Other N (code: same machinery, threshold 1/N, sets of size N−2)

**FACT (exact at max ≤ 20; certified unique at max ≤ 25):**

| N | m*_N | float | minimizer |
|---|---|---|---|
| 17 | 11384/765765 | 0.014866 | {1,…,15} (full — no omission!) |
| 18 | 139/11934 | 0.011647 | {1,…,17}∖{6} |
| 20 | 55876/8083075 | 0.006913 | {1,…,17,19} = {1..20}∖{18,20} |

**Comparison (FACT):** (p/2)m*₂₀ = 3.446 at p = 997 vs D ≤ 2 (discrete beats the continuous floor — the arithmetic-set advantage noted in the packet), and 3.487 at p = 1009 vs D ≤ 4. Predicted δ₂₀ ≈ (m*₂₀/2)/(E/p) = 0.0034565/0.0748 = 0.0462; observed upper bounds 0.0268 (997) and 0.0539 (1009) bracket it. Note the omission pattern is N-dependent: none at 17, {6} at 16 and 18, {18,20} at 20 — **IDEA:** the winner removes speeds whose arcs sit on the rationals with the largest Farey-gap-to-arc-width ratio at threshold 1/N; a clean rule is UNFINISHED.

**UNFINISHED:** uniform explicit c (Q2); medium-complexity bridge (Q3); competitive P₀ (Q4); exhaustion beyond max ≤ 26 (N=16) / 25 (N = 17,18,20); minimizers for max > 25 open in principle (nothing suggests they leave {1..~20}).
***
Honestly? Mixed. Let me grade my own paper:

**Genuinely satisfied with:**
- Q1 and Q5 — those are *certified*, not just computed. The screen gives a proved lower bound per set (grid-safe ⇒ cell-safe), so "no 14-set with max ≤ 26 beats 97/6864" is a theorem, not a heuristic. The 1/6-window explanation for the missing 6 is a real explanation — the endpoint identities check out by hand.
- Q3's dilate bound — small but a complete proof with explicit constants, and it correctly explains *why* p = 457 can have D = 0 (error term 2ΣK = 228 swamps (p/2)m* ≈ 3.2 there).

**Not satisfied with:**
- **Q4 is deliberately crude.** P₀ ≈ 10²⁷¹ came from slapping 9^j safety factors on Erdős–Turán–Koksma. Careful constants (real ET constant, dropping my factor-3 padding, using λ ≈ 1.75's exact value instead of the level-5 truncation) should buy ~200 orders of magnitude — still useless against the empirical 281, but at least honest-looking. A day of constant-polishing, not new math.
- **Q2 is the real open wound**, and I want to be straight about it: the uniform floor m(K) ≥ c is essentially *the* problem in continuous form. My recursion m(K∪{M}) ≥ (7/8)m(K) − (ΣK+1)/(4M) dies because safe(K′) can have ~ΣK′ components. If someone could bound #components of safe(K) independently of ΣK — say ≤ C·max K — the recursion plus my max ≤ 26 exhaustion would close Q2 immediately with c = 97/6864. That's the sharpest "one lemma away" statement I can see, and I didn't crack it.
- Q3's medium regime is the same wound wearing a mod-p costume.

If you want one more round of effort, my ranking: (1) take a real swing at the component-count lemma for Q2 — it's the only place I see a proof-shaped opening; (2) polish Q4's constants; (3) push exhaustion to max ≤ 30 for completeness — pure compute, zero insight. Say the word.
--- end verbatim ---
END LETTER
