# PT005 · 猜公式 Round 3 · Cross-reading, and the grid picture

From: Opus (chair) · 2026-10-09 10:50 +08 (machine clock) · Approved by Tuzi 2026-10-09 10:44 ("yes, definitely")
For: Hesper / Puck to send to the thinking seats. Send the block BEGIN … END verbatim. Each seat also gets its own line from §A. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 第三轮有两件事：一是互相审读，二是从一个新角度去攻「13 个速度为什么盖不满」。
- **新角度：** 「13 个速度是一个覆盖」，等价于「时间格 t/p 一个不剩地，全部躲开这 13 个速度的安全时段」。这一点主席用 223 和 239 两个例子看得很清楚。
- **必须老实说：** 239 到 307 之间，主席找得到只差**一个**格子就能盖满的 13 个速度。所以「盖不满」在这附近是非常微弱的效应。不可能在几天里找到一条对所有 p 都成立的简单公式，把门槛一路压到 300。比较实际的目标，是把门槛压下几个数量级，再用便宜、可检查的计算补上中间那一段。

----- BEGIN PACKET -----

## 猜公式 Round 3 · Cross-read, then attack through the grid

**Setup (unchanged).**
- p is prime, n = (p−1)/2, H = ⌊(p−1)/16⌋.
- Cells t = 1..n (time t/p); speeds v = 1..n (both taken up to sign).
- v is **too near** at t iff 16·min(vt mod p, p − vt mod p) < p.
- A cover is a set of speeds that is too near at every cell; γ(p) is the smallest cover size.

**Now in the ledger** (approved by Tuzi 2026-10-09 10:44):
- **L15:** γ(p) ≤ 15 for every prime p > 16, because {1..15} always covers.
- **L16:** T1 and T2, conditional on F5 (arXiv:2609.02604, the lonely-runner theorem for 13 and 14 speeds):
  - T1: γ(p) ≥ 14 for p > 56¹³;
  - T2: γ(p) = 15 for p > 120¹⁴.
  - Proof: Lemma A (small speeds cannot cover when p ≥ 56M) plus Lemma B (Dirichlet scaling).
  - All 8 readers said YES. Nobody improved the threshold.

**Round 2 levers, checked by the chair** (details in chair note 45):
- (1) An interval instead of a point does not change 56.
- (2) Fixing speed 1 does not lower the exponent.
- (3) Dividing by the gcd helps only when the gcd is ≥ 2.
- (4) **The fractional (LP) cover bound is exactly n/H ≈ 8.** Put weight 1/H everywhere: by L15's regularity this is optimal for both the primal and the dual. So LP certificates cannot prove 14.
- (5) Symmetry alone does not make the search polynomial.
- (6) **Kimi's data:** a 13-cover of 223 whose best scaling still has largest speed 81, while Lemma A needs about 4. So the cover property alone does not force small speeds.

**New facts for this round (DATA, chair, plain Python; scripts in `scouting/LR16/opus/guess_r3/`):**
1. **Near-misses.** A local search, which is a heuristic and proves nothing, finds 13 speeds that leave exactly **one** cell uncovered:
   - p = 239: {1, 9, 16, 19, 56, 65, 66, 73, 75, 92, 102, 108, 111}, hole t = 24.
   - p = 269: hole t = 62. p = 281: hole t = 129. p = 307: hole t = 61.
   - At 401 and 409 its best is 3 holes.
   - So near p ≈ 300 the obstruction is razor-thin. Any proof must kill even a single remaining hole.
2. **The grid picture.** For a set S of speeds, its *safe set* is {x ∈ [0,1) : ‖vx‖ ≥ 1/16 for all v ∈ S}, a union of short intervals ("safe pieces"). Then **S is a cover ⇔ no grid point t/p (1 ≤ t ≤ p−1) lies in the safe set.** Exact rational computation:

   | p | S | safe pieces | total safe length | longest piece | grid spacing 1/p | grid points inside |
   |---|---|---|---|---|---|---|
   | 223 | {1, 6, 16, 19, 28, 34, 40, 52, 54, 59, 86, 96, 99} (a cover) | 118 | 0.1136 | 0.00344 | 0.00448 | **none** |
   | 239 | the near-miss above | 148 | 0.1138 | 0.00265 | 0.00418 | **24 and 215** |

   - The safe set is not small: it is about 11% of the circle, so a random grid of p points would hit it about 25 times.
   - A cover is a set S whose safe set is broken into pieces that are **all shorter than 1/p, and placed exactly between the grid points.**
   - Lemma A is the special case "one piece is longer than 1/p".
3. **Census of 14-covers** (part (b) of the gate; office PC, running):

   | p | 307 | 311 | 313 | 317 | 331 | 353 | 359 | 367 | 401 | 409 |
   |---|---|---|---|---|---|---|---|---|---|---|
   | 14-covers | 4,369 | 546 | 106 | 71 | 155 | 496 | 21 | 14 | 6 | 1 |

   A prime with 0 here has γ = 15 and an empty part (b).

### §A. Cross-reading (each seat: your assigned item; YES / NO / UNSURE + the exact step)

| Seat | Check this claim (all quoted in chair note 45) |
|---|---|
| GPT | Kimi 2(c): a uniform non-tight loneliness gap η turns 56 into 1/(2(1/112 + η)), e.g. η = 1/500 → 45.75. And the chair's proof that the LP value is exactly n/H. |
| Grok | The chair's two refutations: Qwen's "speeds aligned to multiples of 16", and GLM's "p²-size certificate". |
| Gemini | Kimi 2(b), the gcd normalization. And the chair's claim that the author's product bound (log 414.779 for 14 speeds) gives no extra margin for Lemma A. |
| Astra | Kimi 2(f), SAT + DRAT with the unit clause x₁ = 1. Is the encoding correct, and why was the chair's first test on 239 slower than the engine? |
| Kimi | Grok's product-bound lever, read against the author's Section 3 (lattice flag bound). |
| Qwen | Repair your Round 2 alignment argument for speeds near p/2, or withdraw it. |
| GLM | Check new fact 2 (the grid picture) on one more prime of your choice in plain Python, with the code. |
| Lumo | Check the chair's LP refutation, then say whether any *strengthened* LP (e.g. adding pair constraints) could reach 14. |
| DeepSeek | (if reachable) Check L15's proof and the parity argument for equality. |

### §B. The attack (everyone; pick one, label every step FACT / PROOF / IDEA)

1. **Discrepancy route.** Write the safe set of S as a union of pieces.
   - FACT: a piece of length ℓ contains at least pℓ − 1 grid points, so a safe set of total length L in k pieces contains at least pL − k grid points. If pL > k, S is not a cover.
   - After Lemma B's scaling all speeds are ≤ p/N, and the number of pieces is at most Σ v ≤ 13p/N. So "L > 13/N" would be enough.
   - **Honest arithmetic:** with L ≈ 0.114 (the data), this needs N > 114, which is *worse* than Lemma A's N ≥ 56. The naive version does not win. It wins only with (i) a much better count of pieces, (ii) a larger uniform L₀, or (iii) a weighted count of grid points instead of the worst case per piece.
   - **Question:** is there a uniform lower bound L ≥ L₀ > 0 on the safe length of any 13 distinct speeds at threshold 1/16? And how many pieces can a 13-set with all speeds ≤ M really have?
   - Data: both examples above have L ≈ 0.114. What is the smallest L over all 13-sets you can find? A counterexample family with L → 0 also counts as an answer.
2. **Provable improvement of T1 by any route**, even one decimal order.
3. **Cheaper certificate** for γ(p) ≥ 14 at a fixed p (SAT/DRAT, or a smarter exact search). Test on 239, 269 and 281 against the engine's times: 87 s, 151 s and 334 s on the chair's machine.

### §C. One name
Recommend one mathematician (lonely runner / Diophantine approximation / additive combinatorics) best suited to read our eventual write-up, with one reason. Tuzi decides.

**Rules.**
- No seals.
- Code is allowed; give the code or the exact numbers.
- Say where you are unsure.

----- END PACKET -----
