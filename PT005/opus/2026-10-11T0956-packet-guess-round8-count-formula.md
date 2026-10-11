# PT005 · 猜公式 Round 8 · A formula for the number of 14-covers

From: Opus (chair) · 2026-10-11 09:56 +0800 (machine clock) · Approved by Tuzi 2026-10-11 09:55 ("great, omg... please")
For: Hesper to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat**. Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 「小核心」那条路走完了：C-core4 在 281（GPT）和 337（主席）被推翻。
- 这一轮换个问法：**一个素数有多少个 14 速度覆盖？** 写出一条公式，只用 p 和「容量比」两个量。
- 先用 307–499 的普查检验，再预测 503–599 的覆盖**个数**。普查第二批算出来以后就是考卷。
- 最后把公式推广到 N 个跑者。

----- BEGIN PACKET -----

## 猜公式 Round 8 · How many 14-covers does p have?

**Setup** (same as Rounds 5–7).
- p prime, n = (p−1)/2 cells, H = ⌊(p−1)/16⌋.
- Each speed is too near at **exactly H cells**. 14 speeds therefore have total capacity 14H against n cells.
- Write **s = n − 8H**. It takes values 0..7 and depends only on p mod 16 (s = (r − 1)/2 for r = p mod 16). The capacity ratio is 14H/n = 1.75·8H/n.
- "covers" = number of canonical 14-covers (one per scaling orbit), from the office census (km1census v2). 0 means γ(p) = 15.

**Data · census, 33 primes**

| p | H | n | s = n − 8H | 14H/n | covers |
|---|---|---|---|---|---|
| 307 | 19 | 153 | 1 | 1.739 | 4,369 |
| 311 | 19 | 155 | 3 | 1.716 | 546 |
| 313 | 19 | 156 | 4 | 1.705 | 106 |
| 317 | 19 | 158 | 6 | 1.684 | 71 |
| 331 | 20 | 165 | 5 | 1.697 | 155 |
| 337 | 21 | 168 | 0 | 1.750 | 1,477 |
| 347 | 21 | 173 | 5 | 1.699 | 6 |
| 349 | 21 | 174 | 6 | 1.690 | 6 |
| 353 | 22 | 176 | 0 | 1.750 | 496 |
| 359 | 22 | 179 | 3 | 1.721 | 21 |
| 367 | 22 | 183 | 7 | 1.683 | 14 |
| 373 | 23 | 186 | 2 | 1.731 | 26 |
| 379 | 23 | 189 | 5 | 1.704 | 3 |
| 383 | 23 | 191 | 7 | 1.686 | 0 |
| 389 | 24 | 194 | 2 | 1.732 | 8 |
| 397 | 24 | 198 | 6 | 1.697 | 0 |
| 401 | 25 | 200 | 0 | 1.750 | 6 |
| 409 | 25 | 204 | 4 | 1.716 | 1 |
| 419 | 26 | 209 | 1 | 1.742 | 1 |
| 421 | 26 | 210 | 2 | 1.733 | 1 |
| 431 | 26 | 215 | 7 | 1.693 | 0 |
| 433 | 27 | 216 | 0 | 1.750 | 0 |
| 439 | 27 | 219 | 3 | 1.726 | 0 |
| 443 | 27 | 221 | 5 | 1.710 | 0 |
| 449 | 28 | 224 | 0 | 1.750 | 0 |
| 457 | 28 | 228 | 4 | 1.719 | 1 |
| 461 | 28 | 230 | 6 | 1.704 | 0 |
| 463 | 28 | 231 | 7 | 1.697 | 0 |
| 467 | 29 | 233 | 1 | 1.742 | 0 |
| 479 | 29 | 239 | 7 | 1.699 | 0 |
| 487 | 30 | 243 | 3 | 1.728 | 0 |
| 491 | 30 | 245 | 5 | 1.714 | 0 |
| 499 | 31 | 249 | 1 | 1.743 | 0 |

**What the chair sees (FACT, for you to test, not a hint of the answer):**
- At equal capacity ratio the count falls steadily with p. At s = 0 (ratio 1.750): 337 → 1,477; 353 → 496; 401 → 6; 433 → 0; 449 → 0.
- At lower ratios the count reaches 0 earlier. At s = 6–7 (ratio ≈ 1.69): 317 → 71; 367 → 14; 383, 397, 431 → 0.
- 457 (s = 4, one cover) is an outlier.

**Known since Round 7 (PROOF or FACT):**
- Kimi's band lemma: speeds v ≤ 7 never cover the cells t ∈ (H, 2H].
- Subgroup covers (GPT): if p ≡ 1 (mod 28), the order-28 subgroup is a cover iff every coset contains some |r| ≤ H. This works at 29 and 281, and fails at 113, 197, 421, 449.
- C-core4 is refuted at 281 and at 337 (chair notes 57, 58). At 337, S = {1, 7, 15, 40, 43, 58, 63, 65, 83, 101, 106, 108, 115, 164} is a cover with M₁₅ = 3.

### Questions (label every step FACT / PROOF / IDEA)

1. **The count formula.**
   - Give a formula, or a model with at most 3 fitted constants, for log(covers) as a function of p and s, or of p and the ratio 14H/n.
   - Report the fit on the 33 primes: how many 0 / > 0 calls are right, and the typical error in log-count where covers > 0.
   - One natural model, if you want one: expected count ≈ (number of 14-sets / n) × P(a random 14-set covers). P is the hard part. Independence fails: the 14 sets of too-near cells are arithmetic, not random.
2. **Why it falls.**
   - Explain in one paragraph why the count drops by roughly a constant factor per step in p at fixed s.
   - Where does s enter?
3. **Predictions** (prediction before computation; **no code at 503–599**).
   - For each of 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, give your predicted **number** of 14-covers: 0, 1–5, 6–50, or > 50. Give one overall confidence.
   - These are exactly Round 5's exam primes. The office PC computes them after Rounds 4–5 finish.
4. **N runners.**
   - Replace 16 by N: H = ⌊(p−1)/N⌋, (N−2)-covers, s = n − (N/2)·H.
   - What does your formula predict for the largest p with an (N−2)-cover, for N = 17, 18, 20?
   - Code is allowed for small N and small p. Say which cases you computed.

**Rules.**
- Code is allowed for any p ≤ 499 and for N ≠ 16. **No code at 503–599** for N = 16.
- Give exact numbers or the code.
- Say where you are unsure.

----- END PACKET -----

## Chair's record (not for seats)
- Census source: Round 5, Data 1. The s column is n − 8H, computed by the chair.
- Exam: census batch 2 (503–599), after the Round 4 exam gates.
