# PT005 · 猜公式 Round 15 · The continuous floor m* = 97/6864

From: Opus (chair) · 2026-10-11 17:33 +0800 (machine clock) · Following Tuzi's drill direction (16:30) and Round 14 results (chair note 68)
For: Hesper to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat**. Send the block BEGIN … END verbatim. **Put the Round 14 erratum (cf1d31f) at the top of every send, as Tuzi asked.** Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 主席发现，漏格的斜率来自一个「连续」的最小值：速度 1 到 15 去掉 6 这一组，在连续时间里安全时段只占 97/6864。
- 大素数的最佳集合，正是这一组的放大。
- 这一轮请座位们：
  1. 核对这个最小值；
  2. 想办法证明它对所有 14 个速度的组合都是下限；
  3. 证明「漏格少的集合一定是小集合的放大」；
  4. 把 GPT 的子群定理变成有明确门槛的版本。

----- BEGIN PACKET -----

## 猜公式 Round 15 · The continuous floor

**ERRATUM to Round 14, Q2** (found by PT006): G_p contains −1, so a coset holds 14 cells, not 28 independent elements. It is empty with chance ≈ (7/8)¹⁴ ≈ 0.154, not e^{−3.5}. Data for p > 2000: 0.1534. GPT's exact limit: 0.1542089.

**RULE (from Tuzi):** Any number you report must come from your own calculation in this reply, with the code shown or the hand computation shown. If you did not compute it, write UNFINISHED. Do not estimate or invent numbers.

**Setup.**
- For a finite set K of positive integers, let **m(K)** = the Lebesgue measure of {x ∈ [0, 1) : ‖kx‖ ≥ 1/16 for every k ∈ K}. This is the continuous "safe time" of K.
- If S = u·K mod p for a fixed small K, then as p grows, U(S) = (p/2)·m(K) + O(1). Scaling only permutes the cells, and the grid t/p fills [0, 1) evenly.

**Chair's finding** (note 68; code `scouting/LR16/opus/guess_r14/min_safe_measure.py`):
- Over **all** 14-element sets K ⊂ {1, …, 20} (38,760 sets), m(K) is smallest at
  **K* = {1, …, 15} ∖ {6}, with m(K*) = 97/6864 ≈ 0.014132.**
  - Its safe set is four intervals: [33/208, 31/192], [11/64, 31/176], and their mirror images about 1/2.
  - Second smallest: {1, …, 13, 15}, with m = 0.0157.
- **Match with Round 14:** the best D upper bounds at 1999, 2503, 3001 are 14, 17, 21, and (p/2)·m(K*) = 14.1, 17.7, 21.2. The best sets found are dilates of K* (Astra 3001: 8·K*; Kimi 1009: 10·K*). So δ ≈ (m*/2)/(E/p) ≈ 0.092.
- **Round 3 link:** the C16 extremal 13-set {1..5, 7..14} also omits 6.
- **Arithmetic sets can do a little better** than dilates of K*: 457 has D = 0 while (p/2)·m* ≈ 3.2. At N = 20, p = 997, Kimi's run-type set has U = 2 while (p/2)·m*₂₀ ≈ 3.4.

### Questions (label every step FACT / PROOF / IDEA)

1. **Check the floor** (code required).
   - Recompute m(K*) exactly as a fraction.
   - Extend the exhaustive minimum to 14-sets with max ≤ 24 or more, and report how far you got.
   - Does any K beat 97/6864?
   - Why is 6 the missing speed? Explain with the safe intervals.
2. **Prove a floor for all K.** Show m(K) ≥ c > 0 for **every** 14-element set of positive integers, with c explicit.
   - It is known that 15 runners always get a lonely time (Lonely Runner Conjecture for 15, Allikvere 2026, the preprint our ledger relies on, F5). That gives m(K) > 0 for each K, but not uniformly.
   - Hint, not an answer: large speeds behave randomly (m ≈ (7/8)¹⁴ ≈ 0.154), and Dirichlet scaling (L16, Lemma B) reduces to small speeds. Can you prove m(K) ≥ 97/6864 for all K, or at least m(K) ≥ c for an explicit c?
3. **From discrete to continuous** (the inverse step).
   - Prove: for every 14-set S mod p, U(S) ≥ (p/2)·c − C(K) for some K, or U(S) ≥ c'·p directly.
   - Where can a set fail to look like a dilate of a small K, and what does it then pay? Use GPT's Round 14 subtorus method, or Lemma B of L16.
   - State exactly what you prove.
4. **Make the subgroup theorem explicit.**
   - GPT proved that G_p is not a cover for all large p ≡ 1 (mod 28), with P₀ ineffective.
   - Make P₀ explicit. One route: a short relation Σ k_j g^j ≡ 0 (mod p) forces p | Norm(Σ k_j ζ₂₈^j) ≤ (Σ|k_j|)^{12}, then Erdős–Turán.
   - Data: only 29 and 281 up to 20,000.
5. **Other N.**
   - Compute m*_N, the minimum of m over (N−2)-sets with threshold 1/N, for N = 17, 18, 20, as far as you can exhaust.
   - Compare (p/2)·m*_N with D upper bounds at N = 20 near 1000 (Round 14: 997 → 2, 1009 → 4).

**Rules.**
- Code is allowed for any p ≤ 499, any p ≥ 601, and any N ≠ 16. **No code at N = 16, p = 503–599.**
- Every number must be computed in this reply, with code or hand computation shown. Otherwise write UNFINISHED.

----- END PACKET -----
