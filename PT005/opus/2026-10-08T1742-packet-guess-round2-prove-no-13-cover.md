# PT005 · 猜公式 Round 2 · From guessing to proving: why 13 speeds stop covering

From: Opus (chair) · 2026-10-08 17:42 +08 (machine clock) · Approved by Tuzi 2026-10-08 17:40 ("yes")
For: Hesper / Puck to send to the thinking seats. Send the block BEGIN … END verbatim. Replies are committed verbatim under PT005/hesper/ or PT005/puck/.

**中文说明（给 Tuzi）：** 第一轮是猜数字，第二轮是证明。主席在第一轮的基础上写了一个**证明草稿**：p 够大时，13 个速度一定盖不满。草稿用到作者的预印本（14、15 个跑者的 LRC），但目前的门槛大得离谱，约 5 × 10²²，而数据显示真正的门槛大约在 300。这一轮请大家：
1. 先检查主席的证明有没有错；
2. 想办法把门槛从 10²² 往下压。

压得越低，这个结果对我们的门才越有用。

----- BEGIN PACKET -----

## 猜公式 Round 2 · Prove it: no 13-speed cover for large p

**Setup (same as Round 1).**
- p is a prime. n = (p−1)/2, H = ⌊(p−1)/16⌋.
- Cells t = 1..n (time t/p). Speeds v = 1..n. Both are taken mod p up to sign.
- Speed v is **too near** at cell t iff 16 · min(vt mod p, p − vt mod p) < p, that is, ‖vt/p‖ < 1/16.
- A **cover** is a set S of speeds such that every cell has a too-near speed in S. γ(p) is the smallest size of a cover.

**What is now known.** Status words: FACT = checked, PROOF = a full argument given, DATA = computed.
- F1 (FACT): each speed is too near at exactly H cells, and each cell has exactly H too-near speeds.
- F2 (FACT, scaling): if u is not divisible by p, then S is a cover iff uS = {us mod p} is a cover. Reason: replace cell t by u⁻¹t.
- F3 (PROOF, Round 1, found independently by GPT, Gemini and Kimi): **γ(p) ≤ 15 for every prime p > 16.**
  - The speeds {1, …, 15} always cover. Among the 16 points 0, x, …, 15x (x = t/p) on the circle, two are within 1/16 of each other, and their difference is jx with 1 ≤ j ≤ 15.
  - Equality 1/16 is impossible: it would need 16jt = (16k ± 1)p, which has an even left side and an odd right side.
  - The chair checked this by program for all 297 primes 17 < p < 2000.
- F4 (DATA, Round 1 results, all public): γ(p) is 10–12 for 101 ≤ p ≤ 179, and 12 or 13 up to 263. Among the primes computed:
  - the last 13-cover is at 277;
  - γ(p) ≥ 14 at 239, 269, 271, 281, 283, 293, 307, 311 and 313.
  - Round 1 exam answers: 199 → 12, 227 → 12, 257 → 13, 271 → ≥14, 283 → ≥14, 311 → ≥14, 313 → ≥14.
  - 401 is still computing; we already know γ(401) ≥ 13.
  - The lower bounds come from the gate engine's exhaustive search. Every upper bound has a witness cover checked in plain Python.
- F5 (literature): the Lonely Runner Conjecture is proved for 14 and for 15 runners, by computer, in the preprint arXiv:2609.02604 ("Fourteen and fifteen lonely runners").
  - **LRC(14):** for any 13 distinct positive integers w₁, …, w₁₃ there is a real x with ‖wᵢx‖ ≥ 1/14 for all i.
  - **LRC(15):** the same for 14 integers and 1/15.

**The chair's draft theorem (T1). Status: PROOF DRAFT. Not yet read by anyone else. It depends on F5.**

> **T1.** If p > 56¹³ ≈ 5.3 × 10²², then γ(p) ≥ 14.

*Lemma A (small speeds cannot cover).* Let w₁, …, w₁₃ be distinct integers in [1, M], and let p ≥ 56M. Then {wᵢ} is not a cover.
1. By LRC(14), take a real x with ‖wᵢx‖ ≥ 1/14 for all i.
2. Let t be the integer nearest to xp, so |x − t/p| ≤ 1/(2p).
3. Then ‖wᵢt/p‖ ≥ 1/14 − wᵢ/(2p) ≥ 1/14 − M/(2p) ≥ 1/14 − 1/112 = 1/16. So no speed is too near at t.
4. t is not divisible by p, because ‖w₁t/p‖ ≥ 1/16 > 0. ∎

*Lemma B (any 13 speeds can be scaled small).* Let S = {s₁, …, s₁₃} be speeds mod p, and let N = ⌊(p−1)^{1/13}⌋.
1. By Dirichlet's simultaneous approximation, there is an integer 1 ≤ q ≤ N¹³ ≤ p − 1 with ‖q sᵢ/p‖ ≤ 1/N for all i.
2. So each qsᵢ is ≡ ±cᵢ (mod p) with 1 ≤ cᵢ ≤ p/N. The cᵢ are distinct and nonzero, because q is a unit and the sᵢ are distinct up to sign.

*Proof of T1.*
1. Suppose S is a 13-cover. By F2, qS is also a cover. Up to sign it is {c₁, …, c₁₃} with all cᵢ ≤ p/N.
2. Lemma A with M = p/N needs p ≥ 56p/N, that is N ≥ 56, that is p − 1 ≥ 56¹³.
3. Then qS is not a cover, a contradiction. ∎

> **T2 (same proof with LRC(15)).** If p > 120¹⁴ ≈ 1.3 × 10²⁹, then γ(p) = 15.
> The margin becomes 1/15 − 1/16 = 1/240, so Lemma A needs p ≥ 120M.

**Why it matters, and why it is not enough.**
- In the proof gate for p:
  - part (c) needs a cover with at most 13 speeds;
  - part (b) is built from 14-speed covers. The chair still has to confirm that the two definitions are the same.
- So T1 deletes part (c), and T2 would also delete part (b), **but only for p beyond 10²² or 10²⁹**. Our gates use primes in the hundreds.
- The data says the true threshold for 13 is near 280. The gap is about 20 orders of magnitude. **This round is about closing that gap.**

**Questions (answer any you can; label each step FACT / PROOF / IDEA; name your weakest step).**
1. **Referee T1.**
   - Is the proof correct? Answer YES / NO / UNSURE for Lemma A, Lemma B and the final step.
   - If NO, give the exact line and, if possible, a counterexample.
   - Check especially: signs and the "distinct up to sign" claim; the strict versus non-strict inequality at 1/16; whether LRC(14) is used with the right number of speeds.
2. **Shrink the threshold.** Any proven improvement counts, even a factor of 10. Possible levers (ideas, not requirements):
   - (a) *Better margin.* We only need loneliness 1/16, but LRC gives 1/14. Can a whole interval of good times, rather than one point, be used? For speeds ≤ M, how long must a good interval be?
   - (b) *Better scaling.* Dirichlet works for any 13 numbers. But a cover is very special: its 13 translates must tile the group with little overlap (F1). Does that structure force a much smaller q, or speeds much smaller than p^{12/13}?
   - (c) *A different route,* for example counting uncovered cells with characters or Fourier sums, or a direct combinatorial obstruction.
   - (d) *Hybrid.* Prove the theorem above some P₁, and propose how the range 300 … P₁ could be certified by a computation that is much cheaper than the gate engine.
3. **The 14 question.** Is γ(p) = 15 for all large p, or is there an infinite family of 14-covers? Give a reason either way.
4. **One sentence for Tuzi:** what is the single most promising lever, and why?

**Rules.**
- No seals this round. A proof is judged by being checked, not by being guessed.
- Each reply will be read by at least two other seats in Round 3.
- Code is allowed for exploring. Any claim that rests on code must say so and give the code or the exact numbers.

----- END PACKET -----

## Chair's record (not for seats)

- **Sanity checks of Lemma A** (chair, plain Python, 2026-10-08 17:41 +08):
  - p = 1009 and p = 1013 with M = 18 (p ≥ 56M): none of the 8,568 13-subsets of 1..18 covers.
  - 13-subsets of 1..15: exactly 1 covers at p = 101; 0 cover at 211, 307, 401, 503, 601, 701, 809 and 907.
- **Constants:** 56¹³ = 5.327 × 10²²; 120¹⁴ = 1.284 × 10²⁹.
- **Status:** T1 and T2 are the chair's drafts. Nothing enters the ledger until at least two non-author readers say HOLDS, and Tuzi approves.
