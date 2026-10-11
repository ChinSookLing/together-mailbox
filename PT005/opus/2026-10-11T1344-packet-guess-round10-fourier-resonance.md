# PT005 · 猜公式 Round 10 · Fourier: the random part and the resonance part

From: Opus (chair) · 2026-10-11 13:44 +0800 (machine clock) · Asked for by Tuzi 2026-10-11 13:43 ("release 10th round - 傅立叶"); idea from Tuzi 11:15 (Fourier series video)
For: Hesper to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat**. Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 你上午的直觉：复杂的波浪可以拆成简单的正弦波。
- 用在我们的问题上：
  - 「漏掉的格子数」可以**精确地**拆成两部分：
    - 一个「随机部分」，就是第八、九轮的泊松公式；
    - 一个「共振部分」，只在速度之间有整数关系时才出现。
  - 一组速度要成为覆盖，共振部分必须刚好把随机部分抵消掉。
- 这一轮请座位们：
  - 写出这条恒等式；
  - 找出 457 的覆盖靠的是哪些「共振」；
  - 想一想：能不能证明 p 够大时，14 个速度的共振不够强，抵消不了随机部分。那就是一个真正的定理。

----- BEGIN PACKET -----

## 猜公式 Round 10 · The random part and the resonance part

**Setup** (N = 16, as in Rounds 5–8).
- p prime, n = (p−1)/2, H = ⌊(p−1)/16⌋.
- Write ‖x‖ = min(x mod p, p − x mod p).
- **Safe indicator:** B(x) = 1 if ‖x‖ > H, else 0. Speed v is safe at time t iff B(vt) = 1.
- For a set S of 14 speeds, the number of **uncovered cells** is
  U(S) = (1/2) · Σ_{t ∈ Z/p} Π_{v∈S} B(vt).
  The term t = 0 is 0. S is a cover iff U(S) = 0.

**Fourier on Z/p.**
- Write e(x) = exp(2πi x/p) and B(x) = Σ_k b̂(k) e(kx).
- Then b̂(0) = 1 − (2H+1)/p, and for k ≢ 0, b̂(k) = −(1/p)·Σ_{|j|≤H} e(−jk) = −(1/p)·sin(π(2H+1)k/p) / sin(πk/p).

**The identity** (prove it in Q1):

  U(S) = (p/2) · Σ over k = (k_v)_{v∈S} ∈ (Z/p)^S with **Σ_v k_v·v ≡ 0 (mod p)** of Π_{v∈S} b̂(k_v).

- **Random part** (k = 0): M(p) = (p/2)·b̂(0)¹⁴ = (p/2)(1 − (2H+1)/p)¹⁴. Chair's values:
  - 307: 22.91;
  - 337: 24.93;
  - 383: 30.63;
  - 457: 35.39;
  - 499: 37.71.
  - It grows linearly in p. This is the Round 8–9 Poisson term ("expected uncovered cells").
- **Resonance part:** R(S) = the sum over all k ≠ 0 with Σ k_v v ≡ 0 (mod p).
  - Each such k is an **integer relation** among the speeds.
  - Each factor with k_v ≠ 0 has size |b̂(k_v)| ≤ (2H+1)/p ≈ 1/8, and much less once |k_v| is large (roughly 1/(π|k_v|) for |k_v| ≥ 8).
  - So the large terms come from **short relations**: few nonzero coefficients, all of them small.
- **A cover is a perfect cancellation:** U(S) = 0 ⟺ R(S) = −M(p). At 457, the resonances of the 14 speeds must add up to exactly −35.39.

**Known structures to look at:**
- **457:** S = [1, 2, 55, 60, 68, 111, 112, 113, 114, 115, 116, 117, 169, 221]. Here 4·114 ≡ −1 and the run 111..117 maps to the odd numbers 1..13 under ×4. That gives many short relations, e.g. 112 − 111 − 1 ≡ 0 and 4·114 + 1 ≡ 0.
- **281 (subgroup cover, GPT):** S = the 14 classes of x²⁸ ≡ 1. Closed under multiplication, so it has a huge number of relations.
- **337 (chair, note 58), M₁₅ = 3:** S = [1, 7, 15, 40, 43, 58, 63, 65, 83, 101, 106, 108, 115, 164].
- **Random 14-sets:** few short relations, so R(S) is small and U(S) ≈ M(p).

### Questions (label every step FACT / PROOF / IDEA)

1. **The identity.** Prove the formula for U(S) and the values of b̂(k). One short paragraph is enough.
2. **Where does 457's cancellation come from?** (code allowed)
   - Enumerate the short relations of the 457 cover, e.g. all k with |k_v| ≤ 4 and at most 4 nonzero entries.
   - Sum their contributions. How much of −35.39 do they explain?
   - Which relations dominate?
   - Do the same for a random 14-set at 457, and for one 14-cover at 307 or 337.
3. **A resonance budget.** Bound |R(S)| in terms of the number and shape of short relations.
   - Then: how many short relations must 14 numbers mod p have for a cover to exist, as a function of p?
   - Does this explain why covers become rare and then vanish? Does it explain why 457 survives?
4. **Toward a theorem.** Could one prove "for p > P₀, no 14-set has R(S) = −M(p)", i.e. γ(p) = 15, with P₀ far below the 120¹⁴ of ledger L16?
   - Where does Dirichlet scaling (Lemma B of L16) enter? It says any 14 speeds can be scaled so they are all ≲ p^{13/14}. Small speeds create many short relations.
   - State clearly what is proved and what is not.
5. **One sentence for Tuzi:** what does Fourier add that the Poisson formula could not?

**Rules.**
- Code is allowed for any p ≤ 499. **No code at 503–599** (census batch 2 is still the exam for Rounds 5 and 8).
- Give exact numbers or the code.
- Say where you are unsure.

----- END PACKET -----

## Chair's record (not for seats)
- M(p) values computed by the chair: (p/2)(1 − (2H+1)/p)¹⁴.
- The identity is standard: expand each B in its Fourier series and sum over t, which gives orthogonality.
