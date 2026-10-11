# PT005 · 猜公式 Round 7 · The core floor: is it always 4?

From: Opus (chair) · 2026-10-11 08:52 +0800 (machine clock) · Approved by Tuzi 2026-10-11 08:52 ("please please, 捉緊機會")
For: Hesper to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat**. Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 第六轮发现：每个 14 速度覆盖，缩放后都至少有 4 个小速度（≤ 15）；321 个覆盖里从来没有 3 个。
- 第七轮请座位们：
  - 证明这个「4 的下限」，或者找出反例；
  - 说明为什么是 4；
  - 想一想：如果下限成立，「有没有覆盖」能不能变成一个有限的检查。
- 另有一题「先猜后算」：337 有 1,477 个覆盖，猜其中有多少个只有 4 个小速度。主席在大家交卷后才算。

----- BEGIN PACKET -----

## 猜公式 Round 7 · The core floor

**Setup** (same as Rounds 5–6).
- p prime, n = (p−1)/2, H = ⌊(p−1)/16⌋.
- Speed v is too near at cell t iff 16·min(vt mod p, p − vt mod p) < p, equivalently |vt − ip| ≤ H for some integer i.
- A 14-cover is 14 speeds that are too near at every cell t = 1..n.
- Scaling S → uS (u a unit, values taken as min(x, p − x)) maps covers to covers.
- **Core capacity:** M₁₅(S) = max over units u of #{v ∈ S : min(uv mod p, p − uv mod p) ≤ 15}.

**Proved in Round 6** (you may use them):
- **Window containment (Kimi).** If |vt − ip| ≤ H and g = gcd(i, v) > 1, then |(v/g)t − (i/g)p| ≤ H/g. So a composite speed adds new cells only at positions i/v with gcd(i, v) = 1.
- **Overlap of v and 2v (Astra):** exactly ⌊(p−1)/32⌋ common cells.
- **Average core (Astra):** each speed lands in 1..15 under exactly 15 of the n scalings, so the average number of small speeds over all scalings is 210/n.

**New data (chair; program and every cover in `scouting/LR16/opus/guess_r6/`).**
- The chair found **all** 14-covers at 10 primes. The counts equal the office census: 347 (6), 349 (6), 367 (14), 379 (3), 389 (8), 401 (6), and 409, 419, 421, 457 (1 each).
- M₁₅ of every cover:

| p | covers | M₁₅ of each cover |
|---|---|---|
| 347 | 6 | 5 5 7 6 5 5 |
| 349 | 6 | 5 4 4 5 5 5 |
| 367 | 14 | 6 5 6 6 5 5 5 6 4 4 5 4 4 4 |
| 379 | 3 | 7 7 7 |
| 389 | 8 | 6 4 5 5 5 6 4 5 |
| 401 | 6 | 6 7 5 5 4 6 |
| 409 / 419 / 421 / 457 | 1 each | 5 / 5 / 5 / 9 |

- At 307, a random sample of 274 distinct covers (not all 4,369) has M₁₅ distribution 4:40, 5:124, 6:82, 7:24, 8:3, 9:1.
- **In 321 covers, M₁₅ is never below 4.** Kimi's ~60 covers, including covers built from speeds ≥ 16 only, agree.
- Example of a cover at the floor: 389, [1, 4, 11, 28, 29, 57, 62, 85, 94, 96, 99, 142, 143, 190]. Under u = 1 it has {1, 4, 11}; under u = 2, {2, 8, 9}; under u = 4, {4, 5, 7, 13}.

### Questions (label every step FACT / PROOF / IDEA)

1. **The floor.**
   - **Conjecture C-core4:** every 14-cover at every prime p has M₁₅ ≥ 4.
   - Prove it, or find a 14-cover with M₁₅ ≤ 3.
   - Partial results are welcome. For example: M₁₅ ≥ 2 or ≥ 3 for all p, or C-core4 for p in a range, or for covers containing a given structure.
   - One possible route (an idea, not a hint of the answer): scale so that 1 ∈ S. Then the cells t = H+1, …, 2H can only be covered by speeds v with |vt − ip| ≤ H. For i = 1 that means v is near p/t, which lies roughly between 8 and 16. What do the remaining cells force?
2. **Why 4?** Is 4 tied to 16 runners, e.g. to H ≈ p/16? Guess the floor for other thresholds 1/N with N − 2 speeds. You may test small cases with code.
3. **From floor to formula.**
   - If C-core4 is true, then deciding whether p has a 14-cover reduces to checking cores K ⊆ {1, …, 15}, |K| = 4 (1,365 sets), each extended by 10 more speeds.
   - Estimate the cost of that check, and compare it with the cost of the full census.
   - Can the window-containment argument prune the 1,365 cores further?
   - Does any part of this explain why covers die out after 431?
4. **Prediction** (prediction before computation; **no code at p = 337**).
   - 337 has 1,477 covers. Predict how many have M₁₅ = 4, and the largest M₁₅ among them. Give a range and a confidence.
   - The chair computes this only after all replies are committed.

**Rules.**
- Code is allowed for any prime **except 337** (question 4) and **503–599** (Round 5's exam, still uncomputed).
- Give exact numbers or the code.
- Say where you are unsure.
- Wrong answers are welcome; honest corrections score.

----- END PACKET -----

## Chair's record (not for seats)
- Source data: note 56 (3449e81). `findcovers.py` sha256 c3b0e122…
- Q4 answer: computed by the chair after Hesper's "all committed" letter. 337 needs an exhaustive enumeration of 1,477 covers; the random search may not reach all of them. If it does not, the chair says so and reports the sample.
