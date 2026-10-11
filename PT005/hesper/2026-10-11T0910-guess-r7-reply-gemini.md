BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 09:11 +08
RE: 猜公式 Round 7 (packet 1006d95), send text r7_send_full.txt or r7_send_short.txt
SEAT: gemini
MODEL: Gemini Auto + High (Extra thorough)
CHAT: https://gemini.google.com/app/9fbd6ef002471a67

--- reply verbatim ---
SOURCE: https://gemini.google.com/app/9fbd6ef002471a67
ACCOUNT: csllanna@gmail.com (Chin Sook Ling)
MODE SETTING: Auto + High (Extra thorough) — Auto selected (Gemini 3 models), High selected in mode picker. 3.1 Pro / Extended thinking not exposed on this account.
MODEL LABEL SHOWN: Gemini Auto
COPY BUTTON: Copy response button (testid copy) present; two click attempts did not surface clipboard to this tool. Reply text below is captured verbatim from the rendered response via extract_content (region=viewport) while the response was complete (no Stop button; Redo/Good/Bad/Copy/More action row rendered).
CAPTURED VERBATIM (line breaks and intra-line spaces as rendered):

回答区块 (Answer Block)
Q1（底线猜想 C-core4）
：
IDEA
: C-core4 成立。小速度（
≤
15
）在各缩放下通过窗口交叠与细胞覆盖边界，被强制至少选用 4 个以维持全局覆盖网格。
Q2（为什么是 4？）
：
IDEA
: 4 与 16 跑者（
N
=
16
）的比例结构相关（
16/4
=
4
）。对于一般阈值
1/
N
且有
N
−
2
个速度的系统，核心底线约为
⌊
N
/4
⌋
。
Q3（从底线到公式）
：
IDEA
: 将 14-cover 约简为检查 1,365 个核心（大小为 4）加 10 个扩展，使计算复杂度从组合爆炸降至可控范围；窗口包含法则可进一步剪枝不相容核心，这解释了高位素数（
>
431
）因自由度耗尽导致覆盖消亡的相变机制。
Q4（337 预测）
：
IDEA
: 在 337 的 1,477 个覆盖中，预计
M
15
​
=
4
的数量在 [12, 22] 之间，最大
M
15
​
在 [8, 10] 之间。置信度 70%（UNFINISHED）。
推导与论证 (Reasoning)
关于 Q1 的底线证明路径 (IDEA / PROOF)
FACT
: 已知当
p
≥
347
时平均核心大小
210/
n
很小，但所有实测覆盖的
M
15
​
均
≥
4
。
PROOF/IDEA
: 当缩放因子
u
=
1
时，位于区间
[
H
+
1
,
2
H
]
的细胞必须由特定速度覆盖。若
M
15
​
≤
3
，则小速度的细胞贡献度不足以支撑边界的“太近”条件。依据 Astra 的
2
v
重叠引理与 Kimi 的窗口包含法则（
g
c
d
(
i
,
v
)
>
1
时复合速度不产生独立细胞），速度在不同模缩放下的同余群分布必须包含足够的生成元交集，从而在代数上锁定了
M
15
​
≥
4
的硬性下界。
关于 Q2 的比例推导 (IDEA)
IDEA
: 阈值分母
N
=
16
决定了窗口大小
H
≈
p
/16
。核心容量底线 4 恰好是
16/4
。对于一般的系统阈值
1/
N
，底线规律表现为
⌊
N
/4
⌋
。这反映了将连续网格离散化为同余类时，确保 14 个速度在各个模缩放（
u
=
1
…
n
）下不发生系统性真空所需的最小基底维数。
关于 Q3 的计算约简与相变解释 (IDEA)
IDEA
: 穷举
(
14
n
​
)
的代价随
n
剧烈增长。若固定
M
15
​
核心
K
（
∣
K
∣
=
4
，总计
(
4
15
​
)
=
1
,
365
种可能），搜索空间被大幅压缩。窗口包含法则允许我们利用
g
c
d
(
i
,
v
)
直接过滤掉无法在边界产生有效覆盖的核心。
FACT
: 数据显示
p
>
431
后 14-covers 骤降为 0。
IDEA
: 随着
p
增大，满足 1,365 个核心与窗口包含相容性的解空间收缩为空集，这正是高位素数处 14-cover 消失的根本原因。
关于 Q4 的 337 预测与不确定性 (FACT / IDEA)
FACT
:
p
=
307
有 4,369 个覆盖，其中
M
15
​
=
4
有 40 个（约占 0.9%）。
p
=
337
有 1,477 个覆盖。
IDEA
: 按此比例粗略外推，337 的
M
15
​
=
4
覆盖数约为
1477
×
(
40/4369
)
≈
13.5
。结合 307 中最高
M
15
​
达到 9 的表现，预测 337 的最大
M
15
​
在 [8, 10] 之间。
最不确定的步骤 (Least-sure step)
: 将
p
=
307
的统计比例线性外推到 337 的假设——不同素数的二次剩余微观结构具有波动性，低端核心数量可能存在非线性涨落。

MODEL LABEL (as shown beneath the response): Gemini Auto

NOTE ON LINE BREAKS: The Gemini rendered response breaks many inline tokens across lines (e.g. "≤", "15", "N", "=", "16", fractions like "1/N", "⌊N/4⌋", subscripts on "M₁₅", and characters inside "(gcd(i,v)>1)" each appear on their own line in the rendered DOM). The text above preserves those exact rendered line breaks.
--- end verbatim ---
END LETTER
