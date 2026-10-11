# PT005 · 猜公式 Round 11 · The low-frequency budget

From: Opus (chair) · 2026-10-11 14:11 +0800 (machine clock) · Requested by Tuzi via Hesper 2026-10-11 14:09（「等主席出下一題」）
For: Hesper to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat**. Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 第十轮发现：只看最低的几个频率，覆盖的「共振」就比随机集合强很多（约 5 个标准差）。
- 第十一轮要把这个发现变成一条可以证明的路，分两步：
  1. 证明高频尾项有上界；
  2. 证明在 γ = 15 的素数上，任何 14 个速度的低频共振都不够强。
- 另外请座位们用电脑找「低频共振最强的 14 个速度」，看它在不同素数上够不够抵消随机部分。

----- BEGIN PACKET -----

## 猜公式 Round 11 · The low-frequency budget

**Setup** (Round 10).
- U(S) = (p/2)·Σ_{Σ k_v v ≡ 0} Π_v b̂(k_v). The random part is M(p) = (p/2)·b̂(0)¹⁴. A cover has resonance R(S) = −M(p).
- **Frequency truncation:** let B_K be the Fourier series of B cut at |k| ≤ K, and U_K(S) = (1/2)·Σ_t Π_v B_K(vt). Define **R_K(S) = U_K(S) − M(p)**. It keeps relations of every length, but only frequencies |k_v| ≤ K.

**Round 10 results** (chair note 65; code `scouting/LR16/opus/guess_r10/resonance_K.py`):

| K | 4 | 8 | 16 | 64 | all |
|---|---|---|---|---|---|
| 457 cover | −18.95 | −25.59 | −29.95 | −33.21 | −35.39 |
| 337 cover | −12.97 | −19.34 | −21.12 | −24.09 | −24.93 |
| random 14-sets at 457: mean (sd) | −1.57 (3.25) | −1.71 (3.44) | −2.56 (3.51) | | |
| random 14-sets at 457: most negative | −5.04 | −7.17 | −7.30 | | |

- **Truncating by relation length diverges:** at 457, 2-term +5.90, 3-term −59.18, 4-term +96.48.
- **Truncating by frequency converges.** At K = 4 it already separates the cover from random sets by about 5 standard deviations.

### Questions (label every step FACT / PROOF / IDEA)

1. **The tail.**
   - B is a sharp step, so its Fourier series converges slowly (Gibbs).
   - Find a rigorous inequality of the form **U(S) ≥ M̃(p) + R̃_K(S) − E_K(p)**, where R̃_K uses only frequencies |k| ≤ K and E_K(p) is explicit.
   - Ideas to try, not hints of the answer:
     - replace B by a smooth function below it (Fejér or Beurling–Selberg type), with a slightly narrower safe arc;
     - handle the product of 14 factors carefully, since a minorant of B that can be negative does not give a minorant of the product.
   - State exactly what you prove.
2. **The budget** (code allowed for p ≤ 499).
   - For p in {307, 337, 383, 431, 457, 461, 499}, search for the 14-set with the **most negative R_4(S)**, and compare it with −M(p).
   - Report the best value you find, the set, and how you searched.
   - **Key question:** at the γ = 15 primes (383, 431, 461, 499), is the best R_4 clearly short of what a cover needs? At 457 (one cover), is the best set the cover?
3. **Anatomy.** Decompose the 457 cover's R_4 = −18.95 by relation families. Which families carry most of it: the run 111..117 with speed 1, the relation 4·114 + 1 ≡ 0, or something else?
4. **Scaling.** R_K is not scaling-invariant; U is. Does the most negative R_4 over the n scalings of a cover predict anything, for instance that the best scaling of the 457 cover is ×4?
5. **One sentence for Tuzi:** is this a road to a theorem, and what is the hardest step?

**Rules.**
- Code is allowed for any p ≤ 499. **No code at 503–599** (census batch 2 is still the exam).
- Give exact numbers or the code.
- Say where you are unsure.

----- END PACKET -----
