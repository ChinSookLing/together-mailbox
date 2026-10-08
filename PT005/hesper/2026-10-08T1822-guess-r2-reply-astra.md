BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-08 18:22 +08
RE: 猜公式 Round 2 packet (aaa37b9), BEGIN…END block pasted verbatim
SEAT: astra
MODEL: Astra (ChatGPT project The Civilisation Field, Medium; transient 'Searching 5 websites' step occurred, arXiv chip; reply self-labels SEAT: GPT)
CHAT: ChatGPT project chat (session astra-r2)

--- reply verbatim ---
=== ROUND 2 ASSISTANT REPLY — START (spliced from page text because ChatGPT Copy button toast appeared but read_clipboard returned empty in this browser) ===

猜公式 Round 2 · GPT 审稿与证明策略

SEAT: GPT · ROLE: INDEPENDENT REFEREE + PROOF STRATEGY · 2026-10-08

总体裁决：T1 与 T2 的数学推导成立，条件是接受 F5 所述的 Lonely Runner Conjecture 已证明结果。

但我不建议把下一轮主要资源继续投入改进 Dirichlet（同时逼近）常数。我们真正需要的是：证明 13 个速度无法覆盖所有模 p 时间格，而不是仅证明它们经过缩放后能够变小。

我提出两条路线：
严格路线（PROOF）： 确认 T1／T2，建立可以单独检查的覆盖不存在证书。
突破路线（IDEA）： 利用覆盖集合的乘法群结构与剩余覆盖需求，尝试找到比通用同时逼近更强的障碍。

1. Referee T1

审核对象	裁决	说明
Lemma A	YES	LRC(14) 对应 13 个移动速度，数量正确
Lemma B	YES	Dirichlet 同时逼近适用，符号等价与不同速度均保留
T1 final step	YES	缩放不改变覆盖性质，矛盾成立
T2	YES	需要 LRC(15)、14 个速度及通用 15-cover 上界

PROOF · Lemma A
取 LRC(14) 所给的 x，使每个 w_i 满足 ∥w_i x∥ ≥ 1/14.
取最接近 px 的整数 t，并利用距离函数的 Lipschitz 性质：
∥w_i t/p∥ ≥ 1/14 − w_i/(2p).
当 w_i ≤ M 且 p ≥ 56M 时，
1/14 − M/(2p) ≥ 1/14 − 1/112 = 1/16.
端点正确。题目把严格小于 1/16 定义为 too near，因此等于 1/16 的格子也不会被覆盖。
t 非零模 p，且可利用 t ∼ −t 化为合法时间格。

PROOF · Lemma B
设 N = ⌊(p−1)^{1/13}⌋.
Dirichlet 给出 1 ≤ q ≤ N^{13} ≤ p−1 与 ∥q s_i / p∥ ≤ 1/N.
因为 p 为素数，q ≢ 0 (mod p)，乘以 q 是模 p 非零元素上的双射。
若两个缩放后的速度满足 q s_i ≡ ± q s_j (mod p)，则 s_i ≡ ± s_j (mod p)，与原来 13 个速度属于不同正负等价类矛盾。
因此 distinct up to sign 正确。

=== END OF PORTION SAVED SO FAR (truncation occurred mid-Lemma B / T1&T2 section in full extract; will be spliced with portion 2) ===
=== PORTION 2 (spliced here; overlaps slightly with portion 1 to cover the truncation seam at "PROOF · T1 与 T2") ===

PROOF · T1 与 T2
T1 的门槛条件为 N ≥ 56 ⟺ p−1 ≥ 56^13.
原稿采用 p > 56^13，是足够条件，没有错误。
对于 T2： 1/15 − 1/16 = 1/240，需要 M/(2p) ≤ 1/240，即 p ≥ 120M.
证明排除所有 14-cover，结合 γ(p) ≤ 15，得到 γ(p) = 15。

审稿结论：APPROVE T1 / T2，作为依赖 F5 的条件性定理。
论文 arXiv:2609.02604 的 v2 确实声称证明了 14 与 15 runners 的情形，并提供计算证书；我确认了文献版本，但没有独立复核整套原论文计算证书。
arXiv Combinatorics +1

2. Shrink the threshold · 如何真正缩小门槛？

2A · 先提出一个精确的结构性引理

PROOF · 任何 13-cover 都可以缩放成包含速度 1 的 cover。
设 S = {s_1, …, s_13} 是一个覆盖集合。取 u = s_1^{-1} (mod p).
根据 F2，uS 仍然是 cover，而且其中一个速度成为 1。
因此：γ(p) ≤ 13 ⟺ ∃ 一个至多 13-speed cover 包含速度 1
这给我们一个无需 Dirichlet、对所有素数都成立的精确降维。
注意：这里减少的是需要搜索的自由选择，不是直接减少覆盖所需的速度数。

2B · 更进一步：先固定速度 1 所留下的时间格
速度 1 覆盖的时间格恰好是 B_1 = {1, …, H}.
因此，寻找一个包含速度 1 的 13-cover，等价于寻找其余最多 12 个速度覆盖 U = {H+1, …, n}.
定义 A_v = B_v ∩ U. 则有以下等价关系。
PROOF：γ(p) ≤ 13 ⟺ ∃ T ⊆ {2, …, n}, |T| ≤ 12, ∪_{v∈T} A_v = U
这个形式直接对应标准集合覆盖问题（Set Cover），而不需要重新运行完整的 15-speed gate engine。
为什么重要？因为我们现在能够将 part (c) 独立出来，用更简单、更容易审计的搜索算法进行认证。

3. IDEA · Residual Capacity Bound（剩余覆盖容量界）
我认为最值得开发的不是平均覆盖密度，而是搜索中每个阶段的最大剩余覆盖能力。
假设已经选择速度集合 T，仍有时间格集合 R 未被覆盖。
剩余可选速度为 V，还能选择 k 个速度。
对于每个 v ∈ V，定义 a_v(R) = |B_v ∩ R|.
将这些数从大到小排列：a^(1) ≥ a^(2) ≥ ….
那么存在一个严格的必要条件：
|R| ≤ ∑_{j=1}^k a^(j)(R)
PROOF：任意 k 个速度覆盖的剩余时间格数量，至多为各自命中数量之和。而最大的这种和不会超过排序前 k 项之和。
因此，如果 |R| > ∑_{j=1}^k a^(j)(R)，

=== END OF PORTION 2 (seam continues into "3. IDEA · Residual Capacity Bound" and beyond; next portion will cover the tail of section 3 onward) ===
=== PORTION 3 (continues from "排序前 k 项之和" onward; overlaps slightly) ===

因此，如果 |R| > ∑_{j=1}^k a^(j)(R)，便可以立即证明当前分支不可能完成覆盖。
这是一条严格、安全的剪枝规则（Sound Pruning Rule）。
它并不能直接证明所有 p ≥ 300 都不存在 13-cover，但可以把计算量集中于真正难处理的覆盖结构。

更强的版本：考虑两个速度的重叠
上述容量界高估了覆盖能力，因为不同速度可能命中同一时间格。
如果对一组剩余候选速度 W 定义 C(W, R) = |R ∩ ∪_{v∈W} B_v|，
则真正的可完成性条件是 max_{W⊆V, |W|≤k} C(W, R) = |R|.
直接求这个最大值又会回到原问题。
因此，我建议使用中间层级：
一级：单速度容量上界。
二级：两两重叠形成的安全覆盖上界。
三级：对最难覆盖的少数时间格做局部精确搜索。

弱点（WEAKEST STEP）：尚未证明这些界足以排除所有大素数的 13-cover，也没有测量它们相对于现有 gate engine 的计算优势。

4. IDEA · 用覆盖证书取代大型 Gate 搜索
对于固定 p，建立布尔变量 x_v ∈ {0, 1}, v = 2, …, n.
其中 x_v = 1 表示选择速度 v。
寻找 13-cover 等价于下列约束系统可满足：
∑_{v=2}^n x_v ≤ 12
以及每个 t = H+1, …, n：
∑_{2≤v≤n, t∈B_v} x_v ≥ 1.
这是严格等价的整数规划（Inte…

=== END OF PORTION 3 (seam cut inside the SetCover formulation paragraph; continuing) ===
=== PORTION 4 (spliced at SetCover formulation; overlaps slightly with portion 3) ===

这是严格等价的整数规划（Integer Linear Programming, ILP），也可以转换成 SAT。
若求解器给出可验证的不可满足证书（UNSAT Certificate），则该 p 满足 γ(p) ≥ 14.
建议给主席的 Cheap Test 在已知训练素数上先做独立复核：
p	已知结果	新方法应给出的结果
229	γ = 12	SAT
239	γ ≥ 14	UNSAT
257	γ = 13	SAT
269	γ ≥ 14	UNSAT
277	γ = 13	SAT
281	γ ≥ 14	UNSAT
307	γ ≥ 14	UNSAT
313	γ ≥ 14	UNSAT
这是建议的测试清单，不是我本轮已经执行的实验。
如果新求解器在这些实例上得出相反答案，必须先排查模 p 正负等价、严格不等式以及 cardinality constraint 的编码。
如果结果一致，再比较运行时间、内存和证书大小。
WHAT KILLS IT：如果独立 ILP/SAT 的运行成本不低于原搜索，或证书庞大到难以复核，则该方法不能算计算层面的突破。

5. 关于整个好时间区间（Good-Time Interval）
我同意主席提出的方向值得检查，不过这里有一个重要限制。
LRC(14) 给出某个 x，所有 13 个速度距…

=== END OF PORTION 4 (seam cut at "5. 关于整个好时间区间"; continuing) ===
=== PORTION 5 (Section 5 Good-Time Interval + Section 6 The 14 Question; overlaps with portion 4) ===

5. 关于整个好时间区间（Good-Time Interval）
我同意主席提出的方向值得检查，不过这里有一个重要限制。
LRC(14) 给出某个 x，所有 13 个速度距离整数至少 1/14。
由于每个速度最多为 M，在 |y − x| ≤ 1/(112M) 内，所有速度仍满足 ∥w_i y∥ ≥ 1/16.
所以我们确实得到一个好时间区间，长度至少 1/(56M).
PROOF：直接应用 Lipschitz 界。
但要保证这个区间必然包含某个 t/p，仍需要基本上相同的条件：p ≥ 56M.
因此：仅仅把一个好时间点改写成一个好时间区间，并不会自动改善 T1 的门槛。
要取得真正的改进，必须利用额外信息，例如存在多个分离的好时间区间、它们的分布规律，或它们相对于 p-网格的特殊位置。
这正是现阶段尚未证明的部分。

6. The 14 Question · 最终 γ(p) 会不会等于 15？
我选择：
CONJECTURE: γ(p) = 15 for all sufficiently large primes p.
信心：80%，条件是接受 T2 的证明前提。
这已经不只是基于数据的猜测。T2 实际上给出了一个显式的充分大阈值，因而在 F5 成立的前提下：p > 120^14 ⟹ γ(p) = 15.
所以，不可能存在无限多个素数同时具有 14-cover。
这也修正了我 Round 1 的猜测。当时我提出 γ(p) 可能按 log p 无界增长；但 Round 2 的 F3 已证明 γ(p) ≤ 15 对所有 p > 16 成立。
因此 Round 1 的无界增长猜测已经被否定。正确的长期问题不是增长速度，而是何时达到并永久保持上界 15。
真正有意思的是两个不同的有限阈值：P_13: γ(p) ≥ 14，以及 P_14: γ(p) = 15.
它们的实际最小值可能远小于 T1／T2 给出的保守界。

=== END OF PORTION 5 (Section 7, 8, FINAL VERDICT and the "SEAT: GPT · ROUND 2 · SUBMITTED FOR ROUND 3 REFEREE REVIEW" line were already captured verbatim from the earlier viewport extract and will be spliced as Portion 6) ===
=== PORTION 6 (tail: Sections 7, 8, FINAL VERDICT, closing line — verified verbatim in two separate viewport reads) ===

7. 对 TCF Proof Table 的进一步建议
我建议将研究分成两个独立任务。
PROOF 有限素数证书
将每个待检验素数转化成固定速度 1 的 12-choice residual set cover。优先测试 239、269、281、307 和 313，并建立独立、可重复的 UNSAT 证书。
IDEA 统一代数障碍
研究 B_v 的交集及乘法缩放对称性，尝试证明当 p 充分大时，任何 13 个集合都会留下至少一个未覆盖时间格。这一部分尚无完整证明。
需要特别提醒：即使独立求解器能够快速认证 300 ≤ p ≤ 10000 的所有素数，它仍然只是有限范围结论，不能与 T1 共同自动推出从 10000 到 56^13 的结果。中间的空档需要新的数学界或进一步认证。

8. One sentence for Tuzi
我最看好把 13-cover 问题独立转成「固定速度 1、剩余 12 个速度覆盖剩余时间格」的精确证书问题，因为它有严格等价证明，可以立即独立复核，并且不必为 part (c) 承担整个 15-speed gate 的计算成本。

FINAL VERDICT · GPT
T1：YES — mathematically valid, conditional on F5
T2：YES — mathematically valid, conditional on F5
New proven reduction：13-cover → fixed-1 residual 12-cover
New proven pruning：Residual Capacity Bound
Numerical improvement to 56^13：NOT YET PROVED
Proposed path：Independent SAT/ILP certificates + multiplicative structure
Weakest step：没有证明计算上的改进能够转化为统一的大素数定理。

SEAT: GPT · ROUND 2 · SUBMITTED FOR ROUND 3 REFEREE REVIEW

=== END OF FINAL ASSISTANT ANSWER ===

--- end verbatim ---
END LETTER
