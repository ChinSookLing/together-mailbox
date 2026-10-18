SEAT: GPT
CARRIED_BY: Puck
CHAT: https://chatgpt.com/c/6ad46f07-e4f0-83ec-8cf6-53047a7ac1bc
SENT: 2026-10-18 15:02:35 +0800 (see meta.txt)
COLLECTED: 2026-10-18 ~15:25-15:35 +0800, text read from the page (Copy button did not reach the clipboard); thinking excluded; formulas written once in plain form, tables as | rows, wording unchanged
SEND_TEXT: PT005/puck/r47B/send_R47B_GPT.txt
NOTE: thinking High; no Stop/Regenerate. GPT's ZIP/CSV links live in its chat only; not downloaded.
PUCK READ: PARTIAL. 91.8875% (45,148/49,134), 0 live flagged; 131/2,000 non-2-SAT-dead need one 3-clause. KEY FLAG: CSV labels dead nodes that have a covering child (row 1069130). Puck REPRODUCED row 1069130: 16 covering bit choices, mask 17625 child covers every T in 1..847 (exact Fraction test). Rows 644992 and 262542: 0 covering children, consistent with GPT's certificates.
---
ANSWER BLOCK — PT005 · Round 47 Track B

状态：PARTIAL（主要计算完成，数据一致性存在问题）

FACT｜独立复算

随机种子（Seed）：47047，无放回抽样。

50,000 节点中，CSV 标记死亡 49,134；2-SAT 判死 45,148，占标记死亡节点的 91.8875%。

2-SAT 对 CSV 标记存活节点的误判：0。

32,787 个节点存在直接冲突的单文字子句；另外 12,361 个需要非直接冲突的蕴含链（Implication Chains）。

从 3,986 个非 2-SAT 死亡候选中抽取 2,000 个：131 个（6.55%）只需一个三文字子句即可判死。

FACT｜重要异常

重新计算子节点的实际覆盖后，50,000 个样本存在 251 个 n_open_children 数值差异，其中 51 个 CSV 标记死亡的节点实际上存在合法覆盖子节点。

2,000 个第二阶段样本中也有 26 个此类节点。

PROOF｜方法

以完整的 2^15 种位选择建立满足赋值集合，使用精确集合覆盖（Exact Set Cover）搜索最少三文字子句，并逐个验证所得证书。

最不确定处（Least-sure step）

CSV 的 n_open_children 是否包含题包未说明的额外筛选规则。若只按题包定义的覆盖条件判断，部分标签与实际计算不符。

Astra 第 1–3 项的原始题目未随本包提供，无法确认逐项对应；已独立复算可明确确定的 2-SAT 统计。

FACT 1 — 三文字子句的精确最小数量

在 2,000 个抽样节点中，所有短子句（Short Clauses）固定保留，只优化额外需要的三文字子句数量。

最少三文字子句数 | 节点数
1 | 131
2 | 928
3 | 50
4 | 213
5 | 22
6 | 55
7 | 8
8 | 27
9 | 4
10 | 9
11、12、13、14、16 | 各 1
所有三文字子句仍不足 | 548
合计 | 2,000

最后的 548 个节点进一步分为：

FACT：522 个需要至少一个四文字或更长的子句才能证明死亡。

FACT：26 个即使加入所有长度的子句，仍有满足赋值，与 CSV 的死亡标签冲突。

PROOF 2 — 单个三文字子句足够的具体证书

CSV 第 644992 行（零起始索引）：
p=23, k=4, M=368.

独立计算得到以下子句，坐标索引从零开始：

时间 T | 子句
139 | b_5=1
159 | b_7=0 ∨ b_11=0
209 | b_7=1 ∨ b_11=0
67 | b_3=1 ∨ b_11=1
133 | b_3=0 ∨ b_5=0 ∨ b_11=1

PROOF

前四个短子句强制：
b_5=1, b_11=0, b_3=1.

代入第五个三文字子句：
(1=0)∨(1=0)∨(0=1)=FALSE.

因此四个短子句加上 T=133 这一个三文字子句 已经构成不可满足证书（Unsatisfiability Certificate）。

PROOF 3 — 没有相反单文字子句，也能形成短蕴含矛盾

另一个独立证书来自 CSV 第 262542 行，M=1088。

T=19 : (b_4=0)∨(b_10=0),
T=49 : b_10=1,
T=155 : (b_4=1)∨(b_10=0).

PROOF

第二句强制 b_10=1。第一句因而强制 b_4=0，第三句强制 b_4=1。

b_4=0 ∧ b_4=1 ⟹ ⊥.

这证明除了 Antipodal Singleton Lemma 的直接冲突之外，短子句的蕴含结构确实提供另一种死亡机制。

FACT 4 — 必须交给 Opus 核查的数据问题

最明确的反例是 CSV 第 1069130 行：
p=53, M=424.

CSV 记录：
n_open_children = 0

但独立穷举得到 16 个满足全部子节点覆盖条件的位选择。

其中位掩码 17625 对应子节点：

432, 10, 16, 448, 480,
164, 608, 656, 235, 267,
704, 320, 336, 384, 816

逐一验证 1≤T≤424 后，没有发现任何未覆盖时间。

这意味着在题包给定的定义下，该节点并未死亡。

因此，91.9% 可以作为当前 CSV 标签下的统计结果，但若用于证明真实死亡机制，应先核对标签生成逻辑。

复算文件

已保存逐节点最小证书、数据差异清单及独立计算程序：

完整复算程序与结果 ZIP

2,000 节点的最小三文字证书 CSV

50,000 节点中的 251 项数值差异 CSV

IDEA｜给主席 Opus 的结论

Round 47 Track B 已获得可独立复算的正面结果：2-SAT 矛盾解释了约 92% 的 CSV 标记死亡节点；在剩余候选中，单个三文字子句足以解释 6.55% 的抽样节点。

但现阶段最优先的工作不是进一步强化这个百分比，而是核对 n_open_children 的语义。否则，部分被研究为“死亡”的节点实际上拥有覆盖全部时间的子节点，可能影响后续结构性证明。
