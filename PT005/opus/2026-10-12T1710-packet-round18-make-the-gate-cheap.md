# PT005 · Round 18 · Make the gate cheap (route 3), plus one lane on two large speeds (route 2)

From: Opus (chair) · 2026-10-12 17:10 +0800 (machine clock) · Requested by Tuzi 16:31 ("then we do" route 3)
For: Hesper to send to **every seat**, in each seat's "PT005 · Big Picture" chat. Send BEGIN … END verbatim. Replies are committed verbatim.
Data and code: PT005/opus/guess_r18/ (sym_101.txt, sym_103.txt, depth_383_r0_s10.txt, bgk_instr.diff = the print-only patch, explore2.py and its output).

**中文说明（给 Tuzi）：**
- 终点线是 Σ log p > 481.07。现在入账 27.07；还差大约 67 道门。
- 一道门要算 4 到 17 小时，而且质数越大越贵。所以这一轮的目标是让每道门都变便宜。
- 已经证明行不通的路（对称性、min-priv 剪枝等），题里都写明了，不准再交。
- 另外留一条小路，给 Astra 和 GLM 去攻"两个大速度"。

----- BEGIN PACKET -----

## PT005 · Round 18 · Make the gate cheap

**RULE (from Tuzi):** Any number you report must come from your own calculation in this reply, with the code shown or the hand computation shown. If you did not compute it, write UNFINISHED. Do not estimate or invent numbers.

**RULE (soundness):** A pruning rule or certificate is useful only if it **never loses a row** that the gate must check. Every proposal must come with a proof of that, labelled PROOF. If you have only an argument, label it IDEA.

**RULE (citations):** As in Round 17, tag each one READ / ABSTRACT / MEMORY. A fabricated citation voids the reply.

### Where we stand

- **Method.** This is the method of Allikvere's 14/15-runner proof (arXiv:2609.02604), carried to 16 runners (15 speeds, threshold 1/16). A primitive counterexample has log(v₁⋯v₁₅) < B = 494.558. Each closed prime gate p forces p | some vᵢ. So closed gates with Σ log p > 481.07 finish the proof (ledger L8).
- **Closed and in the ledger:** p = 191, 223, 233, 239, 241. Σ log p = 27.07.
- **Part (a) closed on the office PC but not yet in the ledger:** 307, 337, 383.
- **Still needed:** about 67 more gates. Taking every prime from 503 upward, the total reaches 481.07 at p = 953 (chair computation).

**The gate at p.** Setup: n = (p−1)/2 folded time classes; speed class v is too near at t iff 16·min(vt mod p, p − vt mod p) < p; each class covers exactly m = ⌊(p−1)/16⌋ times.
- **(c):** rows containing a cover on ≤ 13 classes.
- **(b):** a 14-class cover plus one class.
- **(a), the irredundant branch:** 15 classes that cover all n times, none removable. Each row is lifted to the grids 2p, 4p, 8p, 16p and dies as soon as a lift has a good time.

The gate closes when no row is alive at level 16. When γ(p) = 15 (no 14-class cover; census, chair notes 48–50), (b) and (c) are empty and **only (a) remains**.

**Measured cost of part (a)** (office PC, 8 workers; author's engine `basegen_k_campaign.cpp` built with -DK=15, plus `cascade_k15p`):

| p | rows | L2 survivors | alive L16 | search nodes | CPU hours | wall |
|---|---|---|---|---|---|---|
| 307 | 11,677,696 | 6,909 | 0 | 3.35e11 | 29.7 | 4.5 h |
| 337 | 7,325,187 | 1,832 | 0 | 7.31e11 | 65.0 | 9.8 h |
| 383 | 5,171 | 2 | 0 | 5.19e11 | 71.1 | 7.2 h |
| 401 | 198,769 | 5 | 0 | 1.93e12 | — | — |
| 409 | 17,546 | 1 | 0 | 1.34e12 | — | 16.9 h |

**The key fact.**
- At p = 383 the search visits about **10⁸ nodes per row it outputs**. Almost the whole cost is dead branches.
- Rows collapse as p grows, but nodes do not.
- In the 15-runner proof, generation was 77% of compute and grew about as p^5.9 (chair measurement, 10-04).

### What the engine already does (do not re-propose these)

The author's search is well engineered:
- It branches on the **rarest uncovered time** (DLX style).
- It cuts when the sum of the top `slots` gains is below the number of uncovered times.
- It uses probe times at slots 2 and 3.
- It tracks each chosen class's **private times** and cuts when one empties.
- It applies a private-time **quota** to class 1 (Lemma "Private times", q_s = ⌈max(0, 2n − sm)/s⌉).
- It splits the work by root and sub-root.

**Measured and dead:**
1. **Dilation symmetry.** Chair, today, EXP_SYM build, p = 101 and 103, all roots. Visits per distinct unit-orbit by depth are 1.00–1.13. At most a ~1.1× gain is possible.
2. **Min-private rooting cut.** Author's own measurement: it would cut 68 of 246,819 nodes at p = 83.
3. **Skipping non-tight classes.** Unsound (author's ST Prop. 7.1).
4. **Fourier sums at p ≤ 700.** Every class has relations with |cᵢ| ≤ 2 (closed at this table on 10-04, Qwen packet).
5. **Qwen's W2, W3.** Already in the engine. W1 and W4 were never instrumented; a measurement is welcome.

**What worked before.** GPT's **core certificate** (chair note 29):
- It turned the quantifier around: check all rows containing a small cover C at once, instead of row by row.
- At p = 223 this became 65 cores and 1.5 CPU hours instead of hundreds of millions of rows.
- That is a 100×-scale gain from one idea. We want the same kind of idea for part (a).

**Where the dead branches are** (chair, today: one p = 383 job, root 0, sub-root 10, author's engine with a print-only counter; nodes 1,443,729,149 and rows 11, both identical to the office run):

| classes chosen | 3 | … | 8 | 9 | 10 | 11 | 12 | 13 | rows |
|---|---|---|---|---|---|---|---|---|---|
| nodes | 1 | … | 715,161 | 9,406,628 | 117,898,116 | **821,519,143** | **479,879,260** | 14,254,875 | 11 |

- **90% of the work** is at 11–12 classes chosen, with 3–4 slots left. Almost all of it is branches that can never be completed.
- **What a perfect cut would buy** (IDEA, not measured): a test that recognises "cannot finish with 4 more classes" already at 10 classes chosen would remove about 9/10 of the nodes. The same test at 9 classes chosen would remove about 99/100.
- The leaves (271) are only about 1 per 5 million nodes.

### Questions (label every step FACT / PROOF / IDEA)

**Q1 · A stronger sound cut.**
- Give a rule that kills dead branches of the irredundant search earlier than the top-k gain bound, with a PROOF that no irredundant cover is lost.
- Candidates you may develop:
  - an LP or fractional-cover bound;
  - private-time capacity (W4);
  - a pairwise-overlap bound, using the arithmetic of v·t mod p;
  - your own.
- If you can, test it with code on p = 101 or 103, where a full run takes about 2 minutes. Report the nodes cut and rows kept (must be identical).

**Q2 · Turn the quantifier around for part (a).**
- At p = 383 there are only 5,171 irredundant rows and 2 survive the first lift.
- Find a **structure theorem** for irredundant 15-class covers mod p at large p, so that they can be **generated from the structure** instead of searched for. Examples of the kind wanted:
  - "every irredundant cover contains a dilate of a long arithmetic progression";
  - "every irredundant cover satisfies a short linear relation Σ cᵢvᵢ ≡ 0 (mod p) with Σ|cᵢ| ≤ L".
- Note: Beck–Everett (arXiv:2609.06259, Thm 1.1) prove the real-number analogue: a tight instance with k speeds has a relation with ‖c‖₁ ≤ 2k+3 and odd coordinate sum. Is there a mod-p version for covers?
- A useful answer states the theorem, proves it (or labels it IDEA), and says how many candidate rows the structure leaves at p = 383 (COMPUTED or UNFINISHED).

**Q3 · Which primes, in which order?**
- With the table above, which primes from 401 to 1009 are cheapest to close? Consider whether cost tracks p mod 16, H = ⌊(p−1)/16⌋, γ(p), or the census counts.
- Give a ladder of primes reaching Σ log p > 481.07 with the lowest predicted cost, and say what in your prediction is model, not measurement.
- The census so far: γ = 15 at 383, 397, 431, 433, 439, 443, 449, 461, 463, 467, 479, 487, 491, 499, and at 503, 509, 521 (batch 2, in progress).

**Q4 · Two large speeds (route 2; lane for Astra and GLM, others welcome).**
- L18 settles every 14-set with at most one speed > 30 (m(K) ≥ 97/6864); L19 gives the deleted baselines in closed form.
- Open: 14-sets with **two or more** speeds > 30.
- Chair exploration (heuristic local search, speeds ≤ 120, EXPLORATORY, not a proof):
  - the lowest set found is {1,2,3,5,7,8,9,11,12,13,29,30,31,42} and its double, with m = 3938177/215975760 ≈ 0.018234;
  - that is about 29% above 97/6864 ≈ 0.014132;
  - the low sets again **omit 6** and contain multiples of 6 (30, 42).
- Prove a two-large-speed inequality, m(K ∪ {v, w}) ≥ …, with an explicit term for a short relation between v and w. Or show where it must fail.

**Q5 · Red team (Grok first, all welcome).** Pick one other likely proposal (for example an LP cut) and try to break its soundness on a concrete small p.

### Suggested lanes

| Seat | Lane |
|---|---|
| GPT | Q2 (it found the core certificate) |
| Kimi, DeepSeek | Q1 |
| Qwen, Lumo | Q3 |
| Astra, GLM | Q4 |
| Grok | Q5 |
| Gemini | Q1 or Q3 |

Lanes are suggestions; a strong answer anywhere is welcome.

### Last question (one line)

If the table could build only one change to the engine this week, which one, and what speed-up do you expect? (Label it IDEA unless measured.)

----- END PACKET -----

Chair's process after replies:
1. Check each PROOF of soundness.
2. Implement the strongest Q1/Q2 idea behind a flag in a scouting copy.
3. Require identical rows on all jobs at p = 101, 103 and one 383 job.
4. Count the nodes saved.

Nothing changes the office engine without Bill's build, a GPT quick read and Tuzi's nod.
