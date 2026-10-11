BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 19:28 +08
RE: 猜公式 Round 16 (packet d712a00), send text r16_send_full.txt or r16_send_short.txt
SEAT: glm
MODEL: GLM-5.3 Deep Think Max (chat.z.ai)
CHAT: https://chat.z.ai/c/34fdce03-7235-4413-8ecc-bd1de5351dbe

--- reply verbatim ---
[Pasted by Tuzi in Hark chat 2026-10-11 19:27 +08 from the GLM Big Picture chat; first line is her note.]

GLM done , Kimi still thinking : **Conclusions.** Q1's bound: PROVED (sharper form too), but vacuous at v ≈ 31, so the 13-set scan must be exact — UNFINISHED, cases listed. Q4: per-interval "±1 grid point" is FALSE (counterexample); exact per-speed count PROVED; conditional P₀ = 1982¹⁴ + 1 ≈ 1.4·10⁴⁶.

**Q1.** [PROOF] Unsafe(v) = v disjoint windows, centers j/v, width 1/(8v). Each length-L safe interval is reached by ≤ vL + 2 centers, losing ≤ (vL+2)/(8v) = L/8 + 1/(4v). Summing: m(K∪{v}) ≥ (7/8)m(K) − c(K)/(4v). Sharper: loss ≤ c″/(8v), c″ = #windows meeting Safe(K). [FACT] At v = 31 the proposed criterion needs m(K′) ≥ 0.0162 + c′/108.5 (c′ = 1 → 0.0254) — too strong near the minimum [IDEA]. [UNFINISHED] Remaining cases: exact m(K′∪{v}) for K′ ⊂ {1..30}, v ∈ [31, v*(K′)], v* = c/(4((7/8)m − 97/6864)) — diverges as m ↓ 0.0162 (3.6·10⁶ at m = 0.0162, c = 625 = 1 + 2·312). Scan C(30,13) ≈ 1.2·10⁸ sets, pruned; not run.

**Q2.** [IDEA] c(K∪{v}) ≤ c(K) + 2v; the next speed pays (c + 2v₁)/(4v₂): induction needs large speeds growing geometrically (ratio ≳ 2). Breaks at two nearby large speeds — Q3's gap.

**Q3.** Proven: max ≤ 30 only. No new unconditional constant: UNFINISHED.

**Q4.** [PROOF] Every unit v kills exactly ⌊p/16⌋ cells in [1, n]: t ↦ vt mod p bijects; arcs ±⌊p/16⌋ are swapped by t ↔ p−t. [FACT] "±1 grid point" is FALSE: v = (p−1)/2 kills every even t ≤ p/8 — half of I = (0, p/8). [PROOF] Repair: killed(I) ≤ ℓ/8 + min(vℓ/p + p/(4v), w/8 + ℓ/w) + 2, w = v⁻¹. [IDEA] So "some small + rest large" fails: min(v, w) is adversary-sized; μ ≥ 1 − k/8 caps D at p(8−k)(k−6)/128. [PROOF, conditional on C-floor] Dirichlet u ≤ N¹⁴ puts all speeds ≤ p/N; c₂ ≤ 14p/N + 1; D ≥ pμ/2 − 14p/N − 15 ⟹ N = ⌈192192/97⌉ = 1982, P₀ = 1982¹⁴ + 1 ≈ 1.4·10⁴⁶ (14·log 1982 = 46.2).

**Q5.** (i) C-floor, all 14-sets: OPEN — alone gives 10⁴⁶. (ii) Repaired concentration lemma: OPEN; with a 7-split, exponent 14 → 7 (needs μ₇, OPEN; C(30,7) = 2.0·10⁶ feasible). (iii) [IDEA] 10⁴ needs per-p computation: all-speeds-≤30 scales exist only for p ≲ 61^{14/13} ≈ 84.
--- end verbatim ---
END LETTER
