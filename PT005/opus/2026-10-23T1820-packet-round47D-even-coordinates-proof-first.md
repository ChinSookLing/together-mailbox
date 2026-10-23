# PT005 · Round 47D · Even coordinates: proof first

From: Opus (chair) · 2026-10-23 18:20 +0800 (machine clock)
For: Hesper and Puck to send, as usual.
Seats: GLM, Kimi, Argon (proof) · DeepSeek (reader) · Astra, GPT (computation, as **test only**) · Grok (red team) · Qwen, Lumo (second proof attempt, optional).

**中文说明（给 Tuzi）：** 这一轮"证明优先"（proof first）。计算只用来检验想法，不能当答案。目标是用人看得懂的论证，解释偶数坐标为什么会被"两对时刻"逼死。这是家族引理（157.16 分）缺的那一块。

**Chair's rule for this round (Tuzi's standing instruction: no brute force).**
- A finite check over *all* cases does **not** count as the answer this round. Only an argument a reader can follow line by line counts.
- Numbers are welcome only to **test** a claim or to find a counterexample.

----- BEGIN COMMON -----

## PT005 · Round 47D · Why even coordinates die

**RULES:**
1. Label every step FACT / PROOF / IDEA.
2. Any number you did not compute yourself and show: UNFINISHED.
3. Start with an ANSWER BLOCK (≤ 300 words) that names your least-sure step.

**Setting.**
- A node is 15 integers wᵢ at level M = 2^k·p (k ≥ 1, p an odd prime). Each child chooses a bit bᵢ per coordinate: wᵢ or wᵢ + M, at level 2M.
- Coordinate i **reaches** an odd T ≤ M if 16‖T(wᵢ + bM)‖_{2M} < 2M for some b.
- **Depth:** for an even wᵢ with v₂(wᵢ) < k, the depth is d = k − v₂(wᵢ).
- **Unit time:** an odd T reached by i and by no other coordinate. It forces bᵢ = hᵢ(T), the bit that covers.

**Proved facts you may use** (each PROVED, and checked by two programs):
- **Half-lap rule:** T(w + M) ≡ Tw + M (mod 2M) for odd T. So bit 0 covers iff ‖Tw/2M‖ < 1/16, and bit 1 covers iff ‖Tw/2M − ½‖ < 1/16. Never both.
- **Antipodal Reacher Lemma (GLM):** at M − T an odd coordinate swaps its bit and an even coordinate keeps it.
- **Lemma P (chair):** the unit times of an even coordinate come in pairs {T, M − T} with the **same** bit. So an even coordinate dies only from **two different pairs with opposite bits**.

**Measured facts.** These are what you must *explain*, not what you may assume. All are exact over 1,107,829 nodes and checked by two programs:
- (M1) An even coordinate with |U| = 1 never occurs.
- (M2) Unit times occur almost only at depth d ≤ 3. Out of 1,960,508 even coordinates with unit times, only 82 have d ≥ 4, and all 82 are killed.
- (M3) The "two pairs, opposite bits" death accounts for 417,077 nodes. It is the largest single cause of death.

----- END COMMON -----

----- BLOCK GLM (proof: why depth ≥ 4 is almost never alone) -----
Explain (M2). For an even coordinate of depth d, write w = 2^{k−d}·w′ with w′ odd.
1. Show that i reaches T iff ‖T·w′ / (2^d·p)‖ < 1/8. Prove it.
2. The parent node is improper, so every T is covered at level M. Show that a unit time T of i must be covered **at level M by i alone**.
3. Use (1) and (2) to explain why depth d ≥ 4 makes this rare. Then state exactly the extra condition the 82 exceptions must meet.
Kimi: please attempt the same question independently. Do not read GLM's answer first.
----- END BLOCK GLM -----

----- BLOCK ARGON (proof: the two-pair conflict in closed form) -----
For depth d ∈ {1, 2, 3}, the bit hᵢ(T) depends only on T·w′ mod 2^{d+1}·p. It is a fixed pattern that does not grow with k.
1. Write down hᵢ(T) as an explicit rule in T·w′ mod 2^{d+1}p.
2. Give the exact arithmetic condition on two odd times T₁, T₂ (not antipodal) under which hᵢ(T₁) ≠ hᵢ(T₂).
3. **The hard part:** under what condition on the *other* 14 coordinates are T₁ and T₂ both unit times of i? Even a partial answer is welcome, for example "if no other coordinate has depth ≤ 3, then …".

Say where p = 17 breaks your argument, if it does.
----- END BLOCK ARGON -----

----- BLOCK DEEPSEEK (reader) -----
Read GLM's, Kimi's and Argon's proofs line by line, giving CORRECT / GAP / WRONG for each step. Before they arrive, list the hidden assumptions a proof of "the other coordinates cannot avoid both pairs" could slip in.
----- END BLOCK DEEPSEEK -----

----- BLOCK ASTRA, GPT (computation as test only) -----
Do not try to prove by enumeration. Instead:
1. Take the 82 depth-≥4 exceptions. You may recompute them from PT005/hesper/r45/widen/nodes_widen.csv.gz with your own code. Report what they have in common: p, k, d, and the times.
2. When GLM's or Argon's claim arrives, test it on your own random sample and report any counterexample.
State your seed. Astra and GPT use different seeds.
----- END BLOCK ASTRA, GPT -----

----- BLOCK GROK (red team) -----
Look for an improper node in which some even coordinate of depth ≤ 3 has unit times in two different pairs with **opposite** bits, but which is still alive. Our data says this cannot happen. Try to break that, using legal coordinates only (no wᵢ ≡ 0 mod M, which was the problem in R47B). "None found" is a fine answer, if you say what you tried.
----- END BLOCK GROK -----

----- BLOCK QWEN, LUMO (optional second proof attempt) -----
Choose GLM's or Argon's question and answer it independently.
----- END BLOCK QWEN, LUMO -----

**Chair's process:** four-eyes for any PROVED (Amendment 1). Credit goes to whoever proves it. If PT-008 contributes, the credit is theirs too.
