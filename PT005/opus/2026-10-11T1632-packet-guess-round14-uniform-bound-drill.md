# PT005 · 猜公式 Round 14 · Drill: the uniform resonance bound

From: Opus (chair) · 2026-10-11 16:32 +0800 (machine clock) · Requested by Tuzi 2026-10-11 16:30 ("set for 14th for drill further"); direction = Round 13 consensus (chair note 67)
For: Hesper to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat**. Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 第十三轮的共识：要证明「大素数没有 14 速度覆盖」，就要证明共振永远抵消不了随机部分，至少差 δ 倍。
- 这一轮分四步往下挖：
  1. 把漏格资料推到 3000，看 δ 会不会稳定；
  2. 先在最整齐的一类（子群集合）上证明；
  3. 检查常见的机率工具为什么不够用；
  4. 把整个证明拆成几个引理。

----- BEGIN PACKET -----

## 猜公式 Round 14 · Drill: −R(S) ≤ (1 − δ)·M(p)

**RULE (from Tuzi):** Any number you report must come from your own calculation in this reply, with the code shown or the hand computation shown. If you did not compute it, write UNFINISHED. Do not estimate or invent numbers.

**Setup** (Rounds 10–13).
- U(S) = uncovered cells of a 14-set S = M(p) + R(S), with M(p) = (p/2)(1 − (2H+1)/p)¹⁴.
- For 14 **distinct** speeds the exact mean is E(p) = n·C(n−H, 14)/C(n, 14). It is about 1 cell below M (Round 13).
- D(p) = min_S U(S). Round 12 data: D ≈ 0.009p − 2.6; D(1009) ≤ 6 while E(1009) ≈ 75.7.
- **Target (Round 13 consensus):** δ(p) := D(p)/E(p) ≥ δ > 0 for all large p. This would give γ(p) = 15 for all p > P₀.
- **Subgroup sets** (chair, note 67): for p ≡ 1 (mod 28), let G_p be the order-28 subgroup taken up to sign. Then U(G_p) = 14 × (number of cosets of G_p containing no element r with |r| ≤ H).
  - 113, 197, 421: one empty coset each.
  - 449: four.
  - 281: none, so G_281 is a cover.

### Questions (label every step FACT / PROOF / IDEA)

1. **Does δ settle?** (code required)
   - Search for small U(S) at p ≈ 1499, 1999, 2503, 3001 (any primes near these), and at N = 20 for two primes near 1000.
   - Report D upper bounds, E(p), and δ = D/E, with the best sets.
   - Is δ(p) rising, flat, or falling? Fit it.
2. **The subgroup class first** (code allowed for any p ≡ 1 mod 28; none lies in 503–599).
   - Compute the number of empty cosets of G_p for all p ≡ 1 (mod 28) up to 20,000. Does it grow like a constant times p, as the Poisson picture predicts (each coset holds about 28·2H/(p−1) ≈ 3.5 small elements, so it is empty with chance ≈ e^{−3.5})?
   - Try to **prove** that G_p is not a cover for all large p ≡ 1 (mod 28). Which bound would be needed: Pólya–Vinogradov, Burgess, Weil? Where does each one fail?
   - Is 281 the last p with G_p a cover?
3. **Why the usual tools fail.** The chair's quick check (IDEA, please verify or refute):
   - The bounded-differences inequality gives only a constant exponent, because one speed changes U by up to H ≈ p/16.
   - Janson's inequality on T = complement of S fails, because the unsafe sets W_t of size H overlap for almost all pairs (t, t'), so Δ ≫ μ.
   - Is there a tool that uses the structure? For example: Dirichlet scaling (ledger L16, Lemma B) to make speeds small, then the resonance of small speeds.
4. **A lemma plan.** Write the shortest chain of lemmas that would prove δ(p) ≥ δ > 0 for p > P₀. Mark each lemma PROVED / KNOWN IN LITERATURE / OPEN. Name the single hardest one.
5. **N runners.** Does your plan depend on 16? Would it work for N = 17, 18, 20 with the same δ argument?

**Rules.**
- Code is allowed for any p ≤ 499, any p ≥ 601, and any N ≠ 16. **No code at N = 16, p = 503–599.**
- Every number must be computed in this reply, with code or hand computation shown. Otherwise write UNFINISHED.

----- END PACKET -----
