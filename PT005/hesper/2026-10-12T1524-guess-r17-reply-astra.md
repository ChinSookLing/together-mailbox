BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:24 +08
RE: 猜公式 Round 17 literature walk (packet ad54489), send text r17_send_full.txt or r17_send_short.txt
SEAT: astra
MODEL: GPT-6 Thinking High, web search (ChatGPT project The Civilisation Field)
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253

--- reply verbatim ---
[Hesper capture note: ChatGPT Copy empty; reply stitched from overlapping page extracts (CAPTURE POINT markers are the capture agent's, not the seat's). This reply in Astra's chat (6ac97e19) is headed 'GPT · Big Picture', while GPT's chat answered as 'Astra' — labels appear swapped; chat URLs are authoritative.]

CAPTURE POINT 1 (Answer block → Ingredient 2 end of Statement):

PT005 · Round 17 · 出宫文献调查
GPT · Big Picture · Literature Walk
ANSWER BLOCK · 结论先行
FACT：已找到与 PT005 直接相关的正式文献，其中最重要的是 Malikiosis–Santos–Schymura 的有限检查定理（Finite Checking Theorem）。
它把孤独跑者猜想中的无限速度问题归约为有限整数速度问题，使用的核心工具是格 zonotope（Lattice Zonotope）、投影和格覆盖半径（Covering Radius）。
Cambridge Core
IDEA：对 Dish B，最值得借用的是其“反例必须具有受限整数结构”的证明方法，而不只是把文献给出的巨大速度上界直接代入 PT005。
速度上界与素数网格门槛是不同问题。
FACT：另一个必须注意的新发展：2026 年的一篇预印本给出了移位孤独跑者猜想（Shifted LRC）及 Lonely Vector Property 的反例。
因此，不能未经检查就把依赖这些更强猜想的论证移植到 PT005。原始 LRC 与 shifted LRC 必须分开。
arXiv Combinatorics
PROOF STATUS：
本轮尚未得到
m(K) ≥ 97/6864
的全局证明，也没有得到可将素数门槛降低至
10^4
的新定理。
下面按文献卡逐项报告。
READ
表示我实际打开了论文正文，
ABSTRACT
表示只核对到摘要或文献页面。数学数值换算与代码另列。
Ingredient 1 · 有限检查上界：已发表的核心定理
Reference：
Romanos Diogenes Malikiosis, Francisco Santos, Matthias Schymura,
Linearly exponential checking is enough for the Lonely Runner Conjecture and some of its variants
.
Forum of Mathematics, Sigma
, 13 (2025), e164. DOI:
10.1017/fms.2025.10107
.
Status：READ
— 已打开 Cambridge 论文正文、Theorem A 及其几何证明章节。
Statement · PROOF（文献定理）：
原文：
Suppose that LRC is true for n runners.
这是 Theorem A 的归纳前提。论文随后给出：若正整数速度
v1, …, vn
互素，且
∑_{∅≠S⊆[n]} gcd(vi : i∈S) > (n+1 choose 2)^(n−1),
则在已知较少跑者情形成立的前提下，该速度组也满足 LRC。
Cambridge Core
Serves dish：B · Threshold
How it plugs in：
对 PT005 的 16 跑者问题，取
n = 16 − 1 = 15
。这直接给出 primitive counterexample 的有限速度界，是 ledger L16 所用类型的理论基础。
What it gives · COMPUTED：
(16 choose 2)^14 = 120^14 = 128391846454886400000000000000.
FACT：这个基本界与 PT005 已有的
120^14
同阶，没有实现新的门槛改进。
Gap：
需要使用论文中的 zonotope 投影论证，而非只使用最终组合上界，找出能够利用 PT005 已知覆盖结构的更强限制。
Ingredient 2 · Quantitative Kronecker：最接近 Round 16 的路线
Reference：
Vikram Giri, Noah Kravitz,
The structure of Lonely Runner spectra
.
Mathematical Proceedings of the Cambridge Philosophical Society
, 180(2), 2026, pp. 343–361. DOI:
10.1017/S0305004125101497
.
Status：READ
— 已阅读 Section 4 的 Lemma 4.4 和 Section 7 的有限速度证明。
Statement · PROOF（文献定理）：
Lemma 4.4 给出定量 Kronecker 型二分：
一个环面子群要么体积受限，要么在某个更高维的子群中达到指定精度的稠密性（Density）。
原文描述这一方法为：
a quantitative, finitary analogue for closed subtori and subgroups.
论文 Section 7 使用这套方法证明：在较少跑者情形成立的前提下，原始速度组对应的子环面足够长，就能得到所需的孤独时间。
Cambridge Core +1

[End of capture point 1 — "Response complete" boundary reached. Continuing from here.]
CAPTURE POINT 2 (Ingredient 2 continued from "Cambridge Core +1" through Ingredient 3, into Ingredient 4):

Serves dish：B · Threshold；兼及 A · Constant
How it plugs in：
这与 PT005 Round 16 的思路直接相接：
大型速度集合
⟶
高体积子环面
⟶
接近更高维子环面
.
大型速度集合⟶高体积子环面⟶接近更高维子环面.
IDEA：
与其把所有速度同时缩小，不如证明异常低安全测度的速度集合必须靠近一个低复杂度的代数结构。若不靠近，它便应展现足够的均匀性。
What it gives · COMPUTED：
论文 Section 7 的范数上界为
V > Γ((n+1)/2) / π^((n−1)/2) · [n(n+1)]^(n−1).
取 n=15，计算得到：
V > 3.510256171 × 10^33.
此处 V 是速度向量的欧氏范数，而不是素数门槛。
FACT：
这个直接数值界仍很巨大，不能取代 PT005 的较小门槛。
Gap：
必须把论文中的“靠近高维子环面”转化为 PT005 所需的
安全测度下界
或
离散遗漏格数下界
。两者尚无现成的转接定理。
Ingredient 3 · Allikvere：最直接可借鉴的计算证明架构
Reference：
Jaan Allikvere,
Fourteen and fifteen lonely runners
. arXiv:2609.02604v2 (2026).
论文 HTML
。
Status：READ — 已阅读 Theorem 1.1、Theorem 3.8（Flag Bound）、素数可除性判准及计算证明部分。
Statement · PROOF（作者声称的定理）：
原文 Theorem 1.1：
The Lonely Runner Conjecture holds for fourteen and fifteen runners.
文章使用投影格基（Projected Lattice Basis）、Korkine–Zolotarev 约化、Gram–Schmidt 长度约束，以及模素数穷举证书，排除原始猜想的反例。
arXiv
Serves dish：B · Threshold；E · Finite-field computation
How it plugs in：
这是我认为 PT005 最值得仔细研究的计算证明结构。
特别是 Theorem 3.8，不只利用一个总量约束，还同时限制格基多个前缀的 Gram–Schmidt 长度，从而改善反例速度乘积界。
其总体逻辑是：
假设存在 primitive counterexample
⇓
证明速度乘积具有有限上界
⇓
封闭指定素数门，迫使许多素数整除该乘积
⇓
素数乘积超过理论上界，产生矛盾
.
假设存在 primitive counterexample ⇓ 证明速度乘积具有有限上界 ⇓ 封闭指定素数门，迫使许多素数整除该乘积 ⇓ 素数乘积超过理论上界，产生矛盾.
这不是与 PT005 毫不相干的另一种算法；它正是 PT005 可借鉴的上层证明架构。
arXiv
What it gives：UNFINISHED
文章确实证明了较强的速度乘积界，并公开代码和证书，但其已计算常数对应论文处理的跑者数量。
不能把这些常数直接替换成 PT005 的 16 跑者常数。
要完成转接，需要为 PT005 重新建立相应维度的 Korkine–Zolotarev 前缀不等式，并独立核查模素数门。
Gap：
目前缺少适用于 PT005 维度的显式 Flag Bound 和足够多的已封闭素数门证书。
这篇文章是公开预印本；READ 不等于我独立复验了其整套计算证明。
Ingredient 4 · 最大孤独距离的刚性
Reference：
Noah Kravitz,
Barely lonely runners and very lonely runners: a refined approach to the Lonely Runner Problem
.
Combinatorial Theory
, 1 (2021). DOI:
10.5070/C61055383
.
Status：ABSTRACT — 核对到期刊摘要，但未成功取得可完整阅读的正文。
Statement · CONJ / PROOF（文献摘要）：
定义最大孤独距离

[End of capture point 2 — second "Response complete" boundary.]
CAPTURE POINT 3 (Ingredient 4 body through Ingredient 5 start):

ML(K) = max_t min_{v∈K} ‖vt‖.
作者提出刚性猜想：
ML(K) ∈ { s/(|K|s+1) : s∈N } 或 ML(K) ≥ 1/|K|.
论文证明了若干低维及单一速度远大于其他速度的特殊情形，并没有对所有速度集合证明该猜想。
CDL Repositories
Serves dish：A · Constant；C · Structure
How it plugs in · IDEA：
Round 16 希望证明：加入很大的速度时，安全测度不会无限下降。
Kravitz 的刚性方向提示，可以研究“大速度是否会迫使最大孤独距离出现间隙”。
但必须区别：
max_t min_v ‖vt‖
与
m(K) = meas{t: min_v ‖vt‖ ≥ 1/16}
.
前者只说明是否存在好时间；后者要衡量所有好时间的总长度。
What it gives：UNFINISHED
这篇文献没有直接提供 PT005 所需的
m(K)
全局数值下界。
Gap：
即使最大孤独距离存在统一余量，也需要一个不依赖最大速度的论证，才能转化为安全时间的统一正测度。
Ingredient 5 · 新反例：必须避开 Shifted LRC 的陷阱
Reference：
Mónica Blanco, Francisco Criado, Francisco Santos,
Coloopless zonotopes and counterexamples to the Shifted Lonely Runner Conjecture
. arXiv:2603.24784v3 (2026).
论文 HTML
。
Status：READ — 已打开最新论文正文，核对摘要、反例章节及 Proposition 5.11。
Statement · FACT / PROOF（文献结果）：
作者明确写道：
We show explicit counterexamples to both the shifted Lonely Runner Conjecture
文章给出具体 shifted LRC 反例，也展示 Lonely Vector Property 的失败。
arXiv +1
Serves dish：B · Threshold；C · Structure

[End of capture point 3.]
CAPTURE POINT 4 (Ingredient 5 continued and 独立数值计算证书 preamble):

How it plugs in：
PT005 研究的是原始、共同起点的 LRC，不是允许每个速度有不同起点的 shifted LRC。
两者不能混淆。
特别是使用 zonotope 文献时，必须区分：
原始 LRC 的定理；
shifted LRC 的条件性结论；
依赖 Lonely Vector Property 的步骤。
What it gives · COMPUTED：
论文 Proposition 5.11 给出的实例具有
γ_sh(1,2,3,4,5) = 15/94 < 1/6.
手算差值：
1/6 − 15/94 = (94−90)/564 = 1/141.
因此它严格违反相应 shifted LRC 的要求。
Gap：
这并未推翻原始 LRC，也不能用作 PT005 的反例。必须逐项核查所借引理究竟适用于哪个版本。
独立数值计算证书
以下程序是本轮实际使用的计算方法，便于主席重算文献常数在 PT005 参数下的数值。
Python Run
from math import comb, gamma, pi
from fractions import Fraction

[End of capture point 4 — "from fractions import Fraction" is the last fully confirmed line of the code preamble. Continuing into the code body, outputs, and the reply's tail.]
CAPTURE POINT 5 (full code + outputs + tail, to final line):

# PT005: stationary runner + 15 moving speeds
n = 16 - 1

# Ingredient 1: Malikiosis–Santos–Schymura
B = comb(n + 1, 2)**(n - 1)

# Ingredient 2: Giri–Kravitz, Section 7
eps = Fraction(1, n*(n + 1))
V = gamma((n + 1)/2) / pi**((n - 1)/2)
V *= float(1/eps)**(n - 1)

# Continuous-floor reference values
floor_candidate = Fraction(97,6864)
uniform_floor = Fraction(1,240**14)

# Ingredient 5: shifted counterexample
shift_gap = Fraction(1,6) - Fraction(15,94)

print("n =", n)
print("Finite-checking bound =", B)
print("Giri-Kravitz norm bound =", f"{V:.9e}")
print("Giri bound / LMS bound =", f"{V/B:.6f}")
print("C-floor candidate =", f"{float(floor_candidate):.12f}")
print("L17 floor =", f"{float(uniform_floor):.9e}")
print("Shifted gap =", shift_gap)
print("Bound / target 10000 =", B//10000)

计算输出
项目			本轮结果
PT005 非零速度数						15
Malikiosis–Santos–Schymura 基本界			1.2839184645 × 10^29
Giri–Kravitz 直接范数界				3.510256171 × 10^33
Giri 界与前者的数值比				27,340.179834
C-floor 候选值						0.014131701632
L17 统一下界						4.753818715 × 10^−34
Shifted 反例的差距					1/141

FACT：
这些计算表明，直接套用现有通用界，并不能把 PT005 的门槛带入所希望的计算范围。
Literature Walk · 对研究方向的判断
这次出宫让我认为，PT005 不应该只在以下两个选择之间徘徊：
“继续寻找更好的 m(K) 常数”，或者“继续扩大素数普查”。
文献提示了第三条路线：
先证明潜在反例的整数结构复杂度受限，再利用现有素数门的计算证书排除它们。
尤其值得研究 Allikvere 的 Flag Bound。它说明，使用一串彼此相关的格基约束，可能比单一 Dirichlet 近似或单一体积界强得多。
这也是一条比较容易分工的路线：数学席负责新的结构上界，计算席负责封门，独立审阅席分别核对证明和计算证书。
Last question · 只能做一道菜
我选 Dish B：把 Allikvere 的 Flag Bound 推广到 PT005 的 16 跑者情形，因为它已经有与 prime-gate 方法相容的证明架构，而目前最缺的是足够强的反例规模界。
最终状态：文献已核实；发现可移植的方法；16 跑者的新显式门槛 UNFINISHED。

[End of capture point 5 — this is the reply's final line, matching the bottom-of-conversation "最终状态：文献已核实；发现可移植的方法；16 跑者的新显式门槛 UNFINISHED。" observed immediately above "ChatGPT can make mistakes. Check important info."]


--- end verbatim ---
END LETTER
