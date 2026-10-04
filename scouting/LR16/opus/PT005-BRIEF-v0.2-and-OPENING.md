# PT005 简报 v0.2 · 接力辩论桌（Relay Debate）· 16 名跑者

草稿人：Opus（主席）· 按 Tuzi 10:41 的方式改写 · 等 Tuzi 批准后由 Puck 上墙

## 一、流程（Tuzi 的方式）

1. **Opus 当主席，而且要有创意。** 主席不只是核对，还可以提出想法和问题。主席提出的想法要标明 IDEA，别的席位可以攻击。
2. **Puck 把开场题目贴上墙**（下面的 OPENING 块），附上 Opus 侦察到的事实。
3. **Tuzi 点名。** 先点一位席位给出方案；再点下一位，回应上一位并给出自己的方案；依此接力。
4. **每个回答都由 Puck 贴上 PT005 的墙。** Opus 在两种时候检查：Tuzi 通知时，或者每 15 分钟一次。每个回答之后，Opus 写一则**主席评语**（chair note），内容包括：
   - 事实核对（有错就指出）；
   - 这个回答最强的一点和最弱的一点；
   - **给下一位的一个创意问题或方向**。

   有话要说时，Opus 会推送通知到 Tuzi 的电脑。
5. **结束条件：** 由 Tuzi 决定什么时候停。停的时候，主席写路线图（route map），列出最好的两三条路线、仍然存在的分歧、第一批实验和成本。

## 二、给 Puck 的送信要求

- 很多席位打不开墙（Kimi 已经遇到过）。所以**每次送信都要附上：开场块 + 前面所有回答和主席评语的原文**，让包自成一体。
- 每个回答限 500 字，所以包不会太大。
- 照旧：先拉信箱再写信，时间和哈希从工具输出复制。

## 三、开桌前要先解决的

- 请 Bill 开 PT005 的墙页面（proof-table-005）。
- 解决 Puck 电脑被墙挡住的问题。否则每一行都要借 Tuzi 的电脑。

---

```
BEGIN PT005-OPENING
TOGETHER · PROOF TABLE 005 · RELAY DEBATE · How do we get the 16th runner out?
Chair: Opus (chairs and may add ideas, marked IDEA) · Host: Tuzi (picks who answers next) · Courier: Puck
Rules: Proof Table Rules v0.5.1, plus the debate rules at the end of this block.

THE QUESTION
The Lonely Runner Conjecture (fixed-runner form): for n non-zero integer speeds v1 … vn there is a real t with ‖vi·t‖ ≥ 1/(n+1) for every i, where ‖x‖ is the distance from x to the nearest integer. (n speeds = n+1 runners.)
It is proved up to 15 runners (n = 14). 16 runners (n = 15 speeds, bound 1/16) is open.
Give ONE concrete path to proving 16 runners. Build on, or attack, the answers before yours.

WHAT IS KNOWN (sources; read them, do not cite from memory)
- Allikvere, "Fourteen and fifteen lonely runners", arXiv:2609.02604 v2. Code and data: Zenodo 22066772 (14 runners), 22667683 (15 runners), CC-BY-4.0.
- The method has three parts:
  (1) a product bound for a primitive counterexample (Theorem 3.8, "flag bound");
  (2) prime gates: for a prime p, a finite computation shows p must divide v1⋯vn (Lemma 2.2);
  (3) enough gates that the sum of log p beats the bound.
- The 15-runner proof used 71 primes up to 569. It cost about 2,137 CPU-hours on a 16-vCPU machine (the author's data). The cost per prime grows about as p^5.9.

CHAIR'S SCOUTING FOR 16 RUNNERS (Opus, 2026-10-04; code and outputs in together-mailbox /scouting/LR16/opus/)
FACT  The Theorem 3.8 method extends to n = 15: its ratio condition holds (3751/2349 > 4/3, exact arithmetic). Our code reproduces the paper's constants for n = 13 and n = 14 exactly.
FACT  If the shape lemma R_15 < 1/2 is proved, the bound is log(v1⋯v15) < 497.03. Numerically, sup R_15 ≈ 0.48796, so the margin is comfortable. This lemma is NOT yet proved.
FACT  Forced divisor lcm(2..16) = 720720, so the gates must supply Σ log p > 483.54.
ESTIMATE  That needs about 80–86 prime gates, the largest near 600–700. Compare 71 gates up to 569 for 15 runners.
UNKNOWN   The "k-factor": how much more one gate costs with 15 speeds than with 14 at the same prime. An old cost law suggests about 11× at p ≈ 600; the author's newer algorithm may do better. Not measured.
ESTIMATE  Total: about 16,000–188,000 vCPU-hours, roughly €200–€2,500 of rented servers at today's prices. The real budget is 2–3× that, for development and failed runs.
IDEA      For the tight tuple (1,…,15), the final level is 16 = 2^4, reachable by binary lifting. That may be simpler than 15 runners' level 15 = 3·5. Not checked.
FACT  Literature check (2026-10-04): no public work on 16 runners was found. The author went from 14 to 15 runners in about 17 days. The paper states the full computation "has not been independently reimplemented or formally verified."

FOUR STARTING ROUTES (you may pick one, combine them, or propose a new one)
A  Brute compute: adapt the published pipeline to 15 speeds and rent servers.
B  Sharpen the bound (pure mathematics). Lowering it by 80 cuts compute to about 35–45% (scouting table).
C  A better gate algorithm, to lower the k-factor. Most room for new ideas.
D  Collaborate or verify: independently re-implement the 15-runner proof, or contact the author.

YOUR ANSWER (at most 500 words; plain text)
SEAT: your name · REPLY_TO: the wall line(s) you answer (the first answer replies to this opening)
1. POSITION: your path in one sentence.
2. WHY IT CAN WORK: the argument. Label each claim FACT (with source), ESTIMATE or IDEA.
3. ON THE PREVIOUS ANSWER(S): agree / attack / build, and exactly where. (The first answer skips this.)
4. FIRST CHEAP TEST: one step that costs little and tells us if the path is alive.
5. WHAT WOULD PROVE ME WRONG: a concrete result.
6. COST AND RISK: rough, labelled ESTIMATE.

DEBATE RULES
- Read the answers before yours (they are included in your packet). Answer them, do not repeat them.
- Changing your mind is credit, not loss. Keeping a position needs a new reason.
- No "impossible" without a check you actually ran or a source you actually read.
- Agreement is not a check. Do not guess. If something you need is missing, say INCOMPLETE.
- Independence: do not search or read other chats in this account; say which account records, if any, you read.
- No keys or passwords anywhere.
END PT005-OPENING
```
