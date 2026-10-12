# PT005 · Round 20 · Brainstorm: close the gates in bulk (look back over Rounds 1–19b, think out of the box)

From: Opus (chair) · 2026-10-13 07:03 +0800 (machine clock) · Requested by Tuzi 07:00/07:02 ("next 20th, we do the brainstorming — review from 1st – 19b and THOOTB … 暴力计算 — 勝之不武"; "Ok, let's go")
For: Hesper to send. Two steps, as in Round 19:
- **20a (ideas):** all nine seats.
- **20b (review):** pairs, each seat attacks one other seat's idea. The chair assigns the pairs after 20a.

Send BEGIN … END verbatim. Replies are committed verbatim.

**中文说明（给 Tuzi）：**
- 暴力算下去要 75 道门、约 9.6 万 CPU 小时（笔记 77）。这一轮不要力气，要点子。
- 用你的会计语言说：证明就是一张资产负债表（balance sheet）。
  - **资产**是关上的门：每关一道，记一笔 log p。
  - **负债**是上界 B。
  - **毛利** = 资产 − 负债，只要 ≥ 0 就证完。这和 THOOTB 的 S = min(…) ≥ 0 是同一个形状。
- 要赢，有三种办法：
  1. 降负债：把 B 压低；
  2. 便宜地加资产：关掉 190 以下的小质数门；
  3. 一条定理一次记入一整批资产：大质数自动关门。
- 这一轮让大家先回顾 19 轮的"已知 / 已死 / 还开着"，再从这三个杠杆里提点子。

----- BEGIN PACKET 20a -----

## PT005 · Round 20a · Brainstorm: close gates in bulk, not one by one

**RULES:**
1. Numbers only from your own code or hand computation, shown. Otherwise write UNFINISHED.
2. Label every step FACT / PROOF / IDEA. IDEAs are welcome this round, but each needs a **first test** that is cheap and decisive.
3. Start with an **ANSWER BLOCK** of at most 300 words.
4. Citations are tagged READ / ABSTRACT / MEMORY.

### The balance sheet (Allikvere's method, carried to 16 runners)

A primitive counterexample has log(v₁⋯v₁₅) < B = 494.558 (ledger L8). Each closed prime gate p adds log p. The proof is finished when

    Σ_{closed gates} log p  >  B − 13.49  =  481.07.

| | Amount |
|---|---|
| Closed and in the ledger: 191, 223, 233, 239, 241 | 27.07 |
| Part (a) done on the office PC: 307, 337, 383, 401, 409 | not yet in the ledger |
| **Brute-force bill** (note 77): cost law nodes ≈ e^16.21 · p^6.19 · e^(−3.13·n/H), leave-one-out error within ×1.2 | 75 more gates, up to p = 719, about **96,000 CPU-hours** |

**What lowering B buys** (same cost law; chair computation):

| B | gates still needed | largest prime | CPU-hours |
|---|---|---|---|
| 494.6 (today) | 75 | 719 | 95,939 |
| 450 | 68 | 661 | 59,901 |
| 400 | 60 | 617 | 32,536 |
| 350 | 52 | 571 | 16,161 |
| 300 | 44 | 509 | 7,397 |
| 250 | 36 | 461 | 3,413 |

**Unused assets.** The 36 primes from 17 to 190 together hold Σ log p = **157.16**. None is closed yet.
- At p = 131 the irredundant branch is closed (0 rows alive at level 16, chair note 20).
- Persistent rows there pass Astra's shift lemma L7 (L9, sampled).
- The reducible branch, about 1.04 × 10⁹ extension rows, was never run.

### What 19 rounds established (one line each; details in the ledger and notes)

**Known (FACT or PROOF):**
- L1/L1a/L8 shape lemma and B.
- L2, L10, L12, L13, L14 five closed gates.
- L7 shift lemma.
- L15: γ(p) ≤ 15.
- L16: T1/T2 thresholds (for p > 120¹⁴ there is no 14-class cover, so γ(p) = 15; conditional on Allikvere's 14/15-runner theorem; this does not by itself close the gate).
- L17: uniform floor 240⁻¹⁴.
- L18: one-large-speed inequality, and the C-floor for ≤ 1 speed > 30.
- L19: 97/6864 in closed form (Zhang).
- The count formula and death lines (Rounds 8–9, prediction before computation).
- The 14-cover census for 307–557.
- The gate cost law (note 77).

**Dead (tested, do not re-propose):**
- Skipping non-tight classes (unsound).
- Fourier sums at p ≤ 700.
- Dilation symmetry (≤ 1.1×).
- Min-private rooting.
- Proactive W4, packing bound, LP dual bound (note 75: none faster).
- Generic minimal-transversal search (≥ 4.6× slower at p = 383, note 76).
- Structure generators from 19a (broken, or bigger than the search, note 76).
- Kimi's L-D1 (false, note 70).
- Scaling alone reaching 10⁴ (2¹⁴ > 10⁴).

**Open:**
- The C-floor for 14-sets with ≥ 2 speeds > 30.
- The effective threshold P₀: about 10⁴² conditional on the C-floor, against a target of about 10³.
- A mod-p version of Beck–Everett relations for covers.
- The small primes 17–190.
- A sharper B.

### The one question

**Name at most two ideas that move the balance sheet in bulk, through one of these three levers or a fourth of your own:**
- **Lever 1 · cut the liability B.** Sharpen the shape lemma or flag bound (Allikvere Thm 3.8, GPT's step in L8), or find another product bound for primitive counterexamples. What B can you reach, and with what proof?
- **Lever 2 · cheap assets.** Close the small primes 17–190 in bulk, using L7-type lemmas or a family argument instead of row-by-row lifting. Which family of persistent rows, and what lemma kills it?
- **Lever 3 · one theorem, many gates.** A statement that closes every prime in a range at once, for example every p ≥ P₁ with P₁ ≤ 1000, via the C-floor, Beck–Everett-type relations, or something else.
- **Lever 4 · your own.** Think out of the box. A different modulus (prime powers, composites), a different decomposition of the conjecture, or an idea from another field. Say why it could beat 96,000 CPU-hours.

**For each idea give:**
- (i) the lever;
- (ii) the mechanism, in five lines or fewer;
- (iii) the first cheap, decisive test (what to compute or prove, and what result would kill the idea);
- (iv) the saving if it works, priced with the table above (COMPUTED, or IDEA with reasoning).

**Last line:** the one idea, of all you know, that you would bet the table's next week on, and why.

----- END PACKET 20a -----

Chair's process:
1. Sort the 20a ideas by lever.
2. Run every "first cheap test" that the chair can run.
3. Assign 20b pairs: each idea goes to a seat that did not propose it, to try to break it.
4. Nothing goes to the ledger without Tuzi's approval.
