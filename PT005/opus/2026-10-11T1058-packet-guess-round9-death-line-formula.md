# PT005 · 猜公式 Round 9 · The death-line formula P*(N)

From: Opus (chair) · 2026-10-11 10:58 +0800 (machine clock) · Approved by Tuzi 2026-10-11 10:57 ("yes, please")
For: Hesper to send to the thinking seats, **in each seat's "PT005 · Big Picture" chat**. Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 第八轮得到了覆盖数目的泊松公式；Kimi 和主席也查了 17、18、20 个跑者。
- 第九轮请座位们写出**死线公式 P*(N)**：门槛 1/N 时，最后一个还有 (N − 2) 速度覆盖的素数，作为 N 的函数。
- 然后**先猜后算**：预测 22 和 24 个跑者的 P*。主席在交卷后才搜索，而且搜索规则现在就写死。

----- BEGIN PACKET -----

## 猜公式 Round 9 · The death line P*(N)

**Setup.**
- Threshold 1/N, with N runners. p prime, n = (p−1)/2, H = ⌊(p−1)/N⌋.
- Speed v is too near at cell t iff N·min(vt mod p, p − vt mod p) < p.
- An **(N−2)-cover** is N − 2 speeds that are too near at every cell t = 1..n. (For N = 16 these are the 14-covers of Rounds 5–8.)
- **P*(N)** = the largest prime p that has an (N−2)-cover.

**Data.**
- **N = 16:** office census (author's engine, exhaustive): last cover at **457**. Zero at 461–499. 503–599 are pending (Round 5 exam).
- **N = 17, 18, 20:** chair search, `scouting/LR16/opus/guess_r8/findcoversN.py`. Random-restart local search, about 150 s per prime. Every cover found was re-checked cell by cell. **Found = fact; not found ≠ proof.**

| N | speeds | covers found at | searched, none found |
|---|---|---|---|
| 17 | 15 | 479 | 487, 491, 499, 503 |
| 18 | 16 | 509, 523 | 521 |
| 20 | 18 | 601, 613, 631, 661 | 641, 653, 677, 691, 701, 809 |

- Kimi's independent search (Round 8) agrees: 17 → 479, 18 → 509, 20 → beyond 601.
- **Round 8 count model** (Kimi, GLM, GPT). Expected uncovered cells for a random set U ≈ n·e^{−(N−2)H/n}. The count ≈ (number of sets, polynomial in p) × e^{−κU}, so it falls by a constant factor per step in p. At N = 16 the census fits ln(covers) ≈ 28.2 − 0.0645·p − 0.54·s with s = n − 8H.

### Questions (label every step FACT / PROOF / IDEA)

1. **The formula.** Give P*(N) as a formula in N, with at most 3 fitted constants. Derive it from the count model if you can: solve "expected count = 1". Fit it on N = 16, 17, 18, 20 and report the errors.
2. **More data (code allowed).**
   - Compute P*(N), or a lower bound for it, for small N, e.g. N = 8 … 15. For small N and small p you can search exhaustively, which turns "not found" into a fact.
   - Say which cases are exhaustive and which are search only.
3. **Predictions** (prediction before computation; **no code for N = 22 or N = 24**).
   - Give P*(22) and P*(24): a point value and a range, with a confidence.
4. **Why not smooth?** At N = 20, 641 and 653 show no cover but 661 does; 661 ≡ 1 (mod 20).
   - Is the death line a single cliff, or a region with scattered survivors (like 457 at N = 16)?
   - What arithmetic makes a late survivor?

**How the chair will score Question 3** (fixed now, before any reply):
- After all replies are committed, the chair runs `findcoversN.py` (sha256 above the commit of this packet in the mailbox) for N = 22 and N = 24.
- Every prime is searched for 150 s. Primes are taken in increasing order from a start well below the predictions.
- The **observed death line** is the largest prime with a found cover before **six consecutive primes** with none found.
- A prediction scores if its range contains the observed death line. The closest point value wins the round.
- The chair publishes every prime searched, found or not.

**Rules.**
- Code is allowed for every N except **22 and 24**, and at N = 16 not at 503–599.
- Give exact numbers or the code.
- Say where you are unsure.

----- END PACKET -----

## Chair's record (not for seats)
- findcoversN.py sha256 prefix 1586938f.
- N = 18 probes at 541–569 are running now; any result will be published, and does not change the questions.
