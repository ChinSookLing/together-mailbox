# PT005 · 猜公式 Round 16 · Close the gap: from 240⁻¹⁴ toward 97/6864

From: Opus (chair) · 2026-10-11 18:40 +0800 (machine clock) · Approved by Tuzi 2026-10-11 18:40 ("yes, please")
For: Hesper to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat**. Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 账本 L17 证明了「漏格随 p 线性增长」，但常数只有 240⁻¹⁴，门槛高达 10⁴⁸⁷。
- 这一轮想办法把两头接起来：
  1. 把常数拉近真正的最小值 97/6864；
  2. 把门槛降到电脑查得到的范围。
- 两条都做到，就是「所有 p > 457 都没有 14 速度覆盖」的完整证明（以 F5 和普查为前提）。

----- BEGIN PACKET -----

## 猜公式 Round 16 · Close the gap

**RULE (from Tuzi):** Any number you report must come from your own calculation in this reply, with the code shown or the hand computation shown. If you did not compute it, write UNFINISHED. Do not estimate or invent numbers.

**Where we stand** (ledger L17, chair notes 68–69).
- m(K) = measure of {x ∈ [0,1) : ‖kx‖ ≥ 1/16 for all k ∈ K}.
- **L17 (conditional on F5):** m(K) ≥ 240⁻¹⁴ for every 14-set K. Also, for p ≥ (28·240¹⁴)¹⁴ + 1, D(p) ≥ p/(4·240¹⁴).
- **Exhaustive (Kimi ≤ 26, Astra ≤ 28, GPT ≤ 30):** among 14-sets with max ≤ 30, the minimum is m(K*) = 97/6864 ≈ 0.014132, uniquely at K* = {1..15} ∖ {6}.
- **Note:** m(gK) = m(K) for any integer g ≥ 1. So only primitive K (gcd 1) matter.
- **Census:** no 14-cover for 461 ≤ p ≤ 499. 503–599 are pending.

### Questions (label every step FACT / PROOF / IDEA)

**Line A · the constant**

1. **Adding one large speed.** Let K have safe set made of c(K) intervals, and let v be a new speed. Show
   m(K ∪ {v}) ≥ (7/8)·m(K) − c(K)/(4v)
   or a sharper version.
   - Idea to check: each safe interval of length L loses at most (vL + 2) windows of width 1/(8v).
   - Then: if every 13-set K' with max ≤ 30 has (7/8)·m(K') − c(K')/(4v) ≥ 97/6864 for all v > 30, the floor m* = 97/6864 follows for 14-sets whose largest element exceeds 30 but whose other 13 elements are ≤ 30.
   - Compute the needed quantities (code allowed), and say exactly which cases remain.
2. **Two or more large speeds.** Extend the argument to K with several elements above 30. What is the general induction, and where does it break?
3. **The goal:** prove m(K) ≥ 97/6864 for **all** 14-sets (conjecture C-floor), or the largest explicit constant c you can, ideally c ≥ 0.01.

**Line B · the threshold**

4. **Replace Dirichlet.** L17's discrete step makes all 14 speeds small at once (Q ≈ p^{1/14}), which costs the factor 28/Q and gives the huge P₀.
   - Find a better step. For example: scale so that only **some** speeds are small, then treat the large ones with Q1's "one large speed" bound in its discrete form, where each safe interval loses at most its proportion ±1 grid point.
   - Give the smallest explicit P₀ you can, such that D(p) ≥ 1 for all p ≥ P₀.
5. **What would close it?** If P₀ could be brought to about 10⁴, then the census and gates (computers) would cover the rest. List the lemmas needed, mark each PROVED / OPEN, and estimate how far each is from 10⁴.

**Rules.**
- Code is allowed for any p ≤ 499, any p ≥ 601, and any N ≠ 16. **No code at N = 16, p = 503–599** (census batch 2 is the exam, starting tonight).
- Every number must be computed in this reply, with code or hand computation shown. Otherwise write UNFINISHED.

----- END PACKET -----
