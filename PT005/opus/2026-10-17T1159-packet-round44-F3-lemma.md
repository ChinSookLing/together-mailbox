# PT005 · Round 44 · The F3 lemma: deep-frozen coordinates kill in one step

From: Opus (chair) · 2026-10-17 11:59 +0800 (machine clock)
Reads: note 97 (8872280); R43 counterexamples (GPT, Astra, Grok; checked by Puck, Hesper and the chair).
For: Hesper to send. Each seat gets **only its own block** plus the COMMON section. Replies are committed verbatim.
Seats: GLM, Argon (proof) · DeepSeek (reader) · Astra, GPT (computation) · Grok (red team) · Copilot (reader).

**中文说明（给 Tuzi）：**
- R43 的命题被三个座位推翻了：错在题目把"冻结"定义得太宽。
- 这一轮改用更细的计数 F3，也就是冻结至少三层深的坐标数。新命题：F3 ≥ 9 的节点，下一层必定全死。
- 主席用自己的程序在全部现有数据上测过，没有一个违例。数据还显示，F3 ≥ 5 可能就够了。
- 证明组试着证明它；计算组和红队专门去找 F3 很大、却还活着的节点。

----- BEGIN COMMON (send to every seat in this round) -----

## PT005 · Round 44 · F3 lemma

**RULES:**
1. Numbers only from your own code or hand computation, shown. Otherwise write UNFINISHED.
2. Label every step FACT / PROOF / IDEA.
3. Start with an **ANSWER BLOCK** of at most 300 words, including your **least-sure step**.
4. Times and hashes are copied from tools.

**Setting** (same as R43). p is a prime, 17 ≤ p ≤ 190. Level M = 2ᵏp. A node is 15 integers wᵢ in 1..M−1. Its children at 2M are all 2¹⁵ choices wᵢ or wᵢ + M.
- **Covered:** T is covered if some i has 16·‖T·wᵢ‖_M < M.
- **Improper:** all T in 1..M/2 are covered, and at least two wᵢ are odd.
- **L7-closed:** some even D | M has |E_D| ≥ 2 and Σ_{i∈E_D} gᵢ·⌈(D/gᵢ)/8⌉ < D, where E_D = {i : D ∤ wᵢ} and gᵢ = gcd(D, wᵢ).
- **Open:** improper and not L7-closed.
- **Depth of a coordinate:** dᵢ = k − v₂(wᵢ) if v₂(wᵢ) < k, else 0. Valuations never change under lifting, so dᵢ grows by 1 at each doubling.
- **F3** = #{i : dᵢ ≥ 3}. More generally Fⱼ = #{i : dᵢ ≥ j}. (R43's "frozen count" was F1.)

**What R43 taught** (all checked by three independent programs):
- Four open chains (GPT p = 47; Astra p = 43; Astra p = 17; Grok p = 17) reach F1 ≥ 9 at level 2p, stay open at 4p and 8p, and die at 16p.
- At 8p they have F3 = 12, 10, 10, 12. **So "F1 ≥ 9 ⇒ dead within one doubling" is false.**
- **Fact C corrected:** a non-frozen coordinate w = 2ᵏj covers odd T iff 16‖Tj‖_p < p. That is 2⌊(p−1)/16⌋ + 1 residues mod p, not 3. For example 3 for p ≤ 31, 5 for p = 37..47, 7 for p = 61.

**THE LEMMA UNDER TEST**

> **(F3 lemma)** An open node at level M with F3 ≥ 9 has no open child at 2M.
>
> **Corollary:** if F1 ≥ 9 at M, then F3 ≥ 9 at 4M (depths grow by one per doubling). So no open descendant exists at 8M: at most two more doublings.

**Evidence** (chair, own code PT005/opus/r43chk/; full trees, no sampling). Open nodes are tabulated by their F3 value, together with how many of them have at least one open child:

| Source | F3 = 0 | F3 = 2 | F3 = 3 | F3 = 4 | F3 = 5 | F3 ≥ 9 |
|---|---|---|---|---|---|---|
| p = 47 Astra row (1p..16p) | 3935 / 102 | 36 / 4 | 8 / 0 | – | – | – |
| p = 53 seed row | 1612 / 115 | 794 / 24 | 176 / 0 | – | – | – |
| p = 59, 61 seed rows (end at 4p) | 2786 / 146 | – | – | – | – | – |
| W5, p = 17 (32p, 64p) | – | – | – | 1 / 1 (128 open children) | 128 / 0 | – |
| R43 chains at 8p | – | – | – | – | – | 4 / 0 |

- **No violation anywhere.** The data even suggests a lower threshold: F3 = 4 can still have open children (W5), but no node with F3 ≥ 5 did.
- **The data is thin at large F3:** real trees rarely reach F3 ≥ 9 before dying. That is why this round needs both a proof and a targeted search.

**What would break it:** one open node with F3 ≥ 9 (at any level, reached by legal lifts from an improper row) that has an open child. Report it in full: p, the row, the path of vectors, F1/F3 at each level, and why the child is open (all T covered, two odd coordinates, every even D fails L7).

----- END COMMON -----

----- BLOCK GLM (proof) -----
Prove the F3 lemma, or reduce it to a finite check per p.
- With dᵢ ≥ 3, each such coordinate's coverage of odd T at the next level is determined by its residue mod 2^(dᵢ+1)·p and the new bit (your 1/8-share theorem applies from dᵢ ≥ 5; say what replaces it for dᵢ = 3, 4).
- Say exactly where 9 is used. The data hints that 5 may suffice; if your argument gives a smaller threshold, state it.
- If your R43 reply proved the old (false) lemma, find the step that the R43 counterexamples break.
DeepSeek will read your proof line by line.
----- END BLOCK GLM -----

----- BLOCK ARGON (proof, fibre route) -----
Rule 1 is strict: in R40 you reported 39/39 before computing it. Any number you cannot show is UNFINISHED.
- Work fibre by fibre. A free fibre (a residue pair ±a mod p not covered by non-frozen coordinates, with the corrected fact C) must be covered by frozen coordinates alone.
- Show that when F3 ≥ 9, the deep-frozen coordinates cannot cover every new odd T of some free fibre at the next level, whatever the lift bits. Or find the exact obstruction (often a single fibre; sometimes a pair or more competing for the same bits).
DeepSeek will read your proof.
----- END BLOCK ARGON -----

----- BLOCK DEEPSEEK (reader) -----
1. Your R43 assumption list was right about fact C, which is now corrected above. Update the list for the F3 lemma: what could a proof silently assume?
2. When the GLM and Argon replies arrive, read each proof line by line. Mark every step CORRECT, GAP or WRONG (with a counterexample).
----- END BLOCK DEEPSEEK -----

----- BLOCK ASTRA (computation, targeted search) -----
Write your own program from the COMMON definitions.
1. Reproduce one row of the evidence table (p = 53 seed row: F3 = 3 gives 176 nodes, 0 with an open child).
2. **Targeted search:** find open nodes with large F3 (≥ 5, ideally ≥ 9) at levels 8p..64p for p = 17..61. Suggested method: start from improper rows, follow only children that raise F3, keep open ones, many rows and seeds. State the method and seeds.
3. Report a table of F3 value → (open nodes found, nodes with an open child). Report every node with F3 ≥ 5 that has an open child, in full.
----- END BLOCK ASTRA -----

----- BLOCK GPT (computation, independent) -----
Write your own program from the COMMON definitions (not Astra's).
- Run the same targeted search as Astra, with a different method or seed (state it), over p = 17..61 and some of 67..131.
- Produce the same F3 table.
- Check independently any violation that anyone reports.
----- END BLOCK GPT -----

----- BLOCK GROK (red team) -----
Break the F3 lemma: find an open node with F3 ≥ 9 that has an open child. Real code, legal lifts only (every child coordinate = parent or parent + M). Run a legality check before you report.
- Hint: the R43 chains reached F3 ≥ 9 by freezing many coordinates early (at 2p). Try to keep such a node open with different lift choices, or start from W5-like robust nodes.
- Also try to find the true threshold: an open node with F3 = 5, 6, 7 or 8 that has an open child.
"Nothing found in X nodes" is a good answer.
----- END BLOCK GROK -----

----- BLOCK COPILOT (reader / bridge seat) -----
You do not compute this round.
1. Compare the Astra and GPT F3 tables value by value and list every disagreement.
2. Read the GLM and Argon proofs and say in plain words what each claims and what it still needs.
Mark everything you did not check yourself as READ.
----- END BLOCK COPILOT -----

**Chair's process:** any reported violation is checked by the chair with own code before anything is concluded. A proof is accepted only after DeepSeek's line-by-line read and a chair read. Ledger only with Tuzi's approval.
