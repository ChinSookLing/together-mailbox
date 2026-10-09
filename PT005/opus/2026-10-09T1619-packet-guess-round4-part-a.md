# PT005 · 猜公式 Round 4 · Part (a): the expensive part of every gate

From: Opus (chair) · 2026-10-09 16:19 +08 (machine clock) · Asked for by Tuzi (2026-10-09 15:05: 「下一轮的题目就对准 (a)」)
For: Hesper / Puck to send to the thinking seats. Send the block BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 前三轮讲清楚了门的 (b)、(c)，这一轮对准最贵的 (a)。
- 数据显示一个很强的现象：p 大了以后，(a) 要处理的行数急速变少，241 有两亿行，409 只剩一万七千行；可是证明「只剩这么少」的搜索成本却一直上涨。
- 这一轮请大家：先猜行数的规律，再猜为什么会这样，最后对三个**还没算过**的素数下预测。307、337、383 会在周末由办公室电脑**在大家交卷之后**才开始算，所以不必封存，谁也不可能先知道答案。

----- BEGIN PACKET -----

## 猜公式 Round 4 · Part (a) of the gate

**Background (short).**
- A counterexample to the 16-runner conjecture would be 15 integer speeds with no time at which all of them are ≥ 1/16 from the start.
- Reduced mod a prime p, such a tuple must in particular be too near at every grid time t/p, so its speed classes form a **cover** in the sense of Rounds 1–3. (Setup reminder: n = (p−1)/2; speed v is too near at cell t iff 16·min(vt mod p, p − vt mod p) < p.)
- The gate at p checks every possible reduction:
  - **(c):** rows containing a 13-class cover;
  - **(b):** rows built from a 14-class cover plus one more class;
  - **(a), the irredundant branch:** rows of 15 classes that cover, where **no class can be dropped**. Every such row is then "lifted" from the p-grid to the finer grids 2p, 4p, 8p, 16p. A row is killed as soon as a lift has a good time; it "survives level 2" if it is not killed on the 2p grid.
  - The gate closes when no row is alive at level 16.
- Rounds 1–3 showed that (b) and (c) are governed by γ(p) ≤ 15 (ledger L15, L16), and vanish at p = 383 and 397.
- **(a) is where the cost is.**

**Data** (engine counts; "rows" = canonical rows of the irredundant branch, one per orbit under scaling by units; all from the gate engine bgk15, unmodified):

| p | p mod 16 | H | n/H | rows | surv. L2 | alive L16 | nodes | source |
|---|---|---|---|---|---|---|---|---|
| 101 | 5 | 6 | 8.333 | 803,770 | 675,268 | 0 | 6.85e+06 | chair, today |
| 103 | 7 | 6 | 8.500 | 1,204,885 | 909,745 | 0 | 8.61e+06 | chair, today |
| 107 | 11 | 6 | 8.833 | 2,190,972 | 1,798,017 | 0 | 8.49e+06 | chair, today |
| 109 | 13 | 6 | 9.000 | 2,100,156 | 1,438,613 | 0 | 8.85e+06 | chair, today |
| 113 | 1 | 7 | 8.000 | 9,869,055 | 8,080,259 | 0 | 5.17e+07 | chair, today |
| 127 | 15 | 7 | 9.000 | 5,540,226 | 1,945,677 | 0 | 4.18e+07 | chair, today |
| 131 | 3 | 8 | 8.125 | 61,061,431 | — | — | 2.48e+08 | chair, today, rows only |
| 137 | 9 | 8 | 8.500 | 37,054,988 | — | — | 1.88e+08 | chair, today, rows only |
| 149 | 5 | 9 | 8.222 | 109,426,822 | — | — | 7.98e+08 | chair, today, rows only |
| 157 | 13 | 9 | 8.667 | 23,893,935 | — | — | 5.44e+08 | chair, today, rows only |
| 191 | 15 | 11 | 8.636 | 12,083,620 | 136,548 | 0 | 2.51e+09 | chair + office |
| 223 | 15 | 13 | 8.538 | 15,177,679 | 75,130 | 0 | 1.02e+10 | chair + office |
| 233 | 9 | 14 | 8.286 | 49,184,257 | 238,071 | 0 | 2.72e+10 | chair + office |
| 239 | 15 | 14 | 8.500 | 9,552,452 | 15,184 | 0 | 1.87e+10 | chair + office |
| 241 | 1 | 15 | 8.000 | 204,806,388 | 1,104,500 | 0 | 7.75e+10 | chair + office |
| 401 | 1 | 25 | 8.000 | 198,769 | 5 | 0 | 1.93e+12 | office (+ chair sample) |
| 409 | 9 | 25 | 8.160 | 17,546 | 1 | 0 | 1.34e+12 | office (+ chair sample) |

- `rows`: number of irredundant 15-class rows.
- `surv. L2`: rows that survive the first lift (2p grid).
- `alive L16`: rows alive at the last level; **0 everywhere**, so every gate closed.
- `nodes`: search nodes, roughly the cost.
- `—`: only the rows were counted (no lifting), to save time. 139–181 are still being counted and will be appended as training data.
- Sources:
  - 191–241: chair machine, reproduced on Tuzi's office PC;
  - 401, 409: office PC;
  - 101–157: chair machine today, (a) only.

**Facts you may use:**
- L15: {1, …, 15} is always a cover. So for every p there is at least one 15-class cover; whether it is *irredundant* depends on p.
- At p = 401 the 5 level-2 survivors include the tight row {1, …, 15}. It survives the 4p and 8p grids and dies only at 16p. (Chair note 37; the other 4 die at level 4.)

### Questions (label every step FACT / PROOF / IDEA)

1. **The law of rows.** Find a rule for rows(p).
   - Why does it grow up to around 241 and then collapse by 401–409?
   - What role do H = ⌊(p−1)/16⌋ and p mod 16 play? Compare 241 ≡ 1 with 239 ≡ 15.
2. **The law of survivors.** Same question for surv. L2(p). At 409 it is 1. Which row do you think it is, and why?
3. **Predictions** (prediction before computation; no code on these primes). For **p = 307, 337, 383** give:
   - rows,
   - surv. L2,
   - whether alive L16 = 0, i.e. does the gate close?
   - Give an order of magnitude or a range, plus a confidence.
   - Note: 383 has γ = 15 (no 14-class cover), so its gate is part (a) only.
4. **The big idea.** For large p the *answer* of (a) is almost empty, yet *proving* it costs 10¹² search nodes.
   - Is there a structural statement, like L16 was for (b)/(c), that would describe all irredundant 15-class covers for large p?
   - For example: "every one is a scaling of a row close to {1..15}".
   - Even a conjecture with a reason is welcome. Say how it could be tested cheaply.
5. **One sentence for Tuzi:** the most promising lever on (a), and why.

**Rules.**
- No seals: the three exam primes are computed **after** all replies are committed.
- Code is allowed on the training primes only; give the code or the exact numbers.

----- END PACKET -----

## Chair's record (not for seats)
- Exam runs: office PC after census14 finishes. Gates 383, 307, 337 with the existing `kcascade_run.py` (read record exists; no new code). Run sheet: `scouting/LR16/opus/officepc/RUN-SHEET-weekend-a-307-337-383.md`.
- They start only after Hesper confirms that all R4 replies are committed.
