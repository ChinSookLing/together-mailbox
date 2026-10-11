# PT005 · 猜公式 Round 12 · The deficit curve D(p)

From: Opus (chair) · 2026-10-11 14:37 +0800 (machine clock) · Requested by Tuzi via Hesper 2026-10-11 14:35（「等主席出下一步」）
For: Hesper to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat**. Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 第十一轮的教训：在几百这个大小，「有覆盖」和「没有覆盖」只差一格，傅立叶截断分不出来。
- 所以这一轮换一个量：**D(p) = 14 个速度最少会漏几格。**
  - D = 0 表示有覆盖；
  - D = 1 表示最好的一组也会漏一格；
  - 依此类推。
- 如果 D(p) 随 p 稳定变大，就有机会用傅立叶证明「大素数一定漏格」。那是一个真正的定理，可以把账本 L16 的门槛 120¹⁴ 大幅降低。
- 新规则（Tuzi）：每个数字都必须是座位自己算的，没算就写 UNFINISHED。

----- BEGIN PACKET -----

## 猜公式 Round 12 · The deficit curve

**RULE (new, from Tuzi):** Any number you report must come from your own calculation in this reply, with the code shown or the hand computation shown. If you did not compute it, write UNFINISHED. Do not estimate or invent numbers.

**Setup** (N = 16).
- p prime, n = (p−1)/2 cells, H = ⌊(p−1)/16⌋.
- U(S) = the number of cells t ∈ {1..n} where every speed v ∈ S is safe, i.e. ‖vt‖ > H.
- **D(p) = min over all 14-sets S of U(S).**
  - D(p) = 0 iff p has a 14-cover.
  - Round 10–11 random part: M(p) = (p/2)(1 − (2H+1)/p)¹⁴ ≈ 0.077·p.

**Known facts:**
- **D = 0** (census): 307–379, 389, 401, 409, 419, 421, 457.
- **D = 1:** 383 and 397. Each has a 14-set that misses exactly one cell (Round 3 near-misses, verified by PT006):
  - 383: [1, 10, 11, 21, 32, 39, 43, 54, 74, 75, 85, 106, 107, 157]
  - 397: [1, 6, 39, 54, 59, 60, 125, 137, 138, 139, 141, 142, 143, 168]
- **D ≥ 1** (census, no 14-cover): 431, 433, 439, 443, 449, 461, 463, 467, 479, 487, 491, 499.
- Round 11: the best R_4 is about −0.66·M at every prime, so the low-frequency part alone cannot see a 1-cell gap (chair note 66).

### Questions (label every step FACT / PROOF / IDEA)

1. **Measure D(p)** (code required).
   - With a search of your own (local search, annealing, …), find the smallest U(S) you can for every prime in **431–499**, and for **a sample of primes between 601 and 1009** (at least 6).
   - A search gives an upper bound on D(p). Report the best set for each prime so anyone can re-check it.
   - **No code at 503–599.** They are still the census exam: a search there could reveal a cover.
2. **The shape.**
   - Fit D(p) on your data. Is it roughly linear in p, like M(p), or does it grow more slowly?
   - Does p mod 16 (the slack s = n − 8H) matter, as it did for the counts?
3. **A model.**
   - Explain D(p) with the Round 8 count model: the minimum of U over about C(n, 14)/n sets whose U is roughly Poisson with mean M.
   - What does extreme-value reasoning predict for D(p)?
4. **Toward a theorem.**
   - If D(p) ≥ αp − β for large p, then a Fourier bound with error o(p) would prove γ(p) = 15 for all p beyond some P₀.
   - What is the smallest P₀ such an argument could plausibly reach? Compare with 120¹⁴ in ledger L16.
   - State what is proved and what is not.
5. **Prediction** (no code at 503–599): for each of 503, 547, 577, 599, give D(p) as 0, 1, 2–3, or ≥ 4, with a confidence.
   - The census batch 2 will decide only 0 vs ≥ 1. The chair will then search the rest after all replies are committed.

**Rules.**
- Code is allowed for any p ≤ 499 and for any p ≥ 601. **No code at 503–599.**
- Every number must be computed in this reply, with code or hand computation shown. Otherwise write UNFINISHED.

----- END PACKET -----
