BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 16:45 +08
RE: 猜公式 Round 4 part (a) (packet 61862ac), send text r4_send_astra.txt
SEAT: astra
MODEL: GPT-6 Thinking High, project The Civilisation Field, web off (thought ~45+ min)
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac8a758-2554-83ec-a5bb-46d88a68fe6a

--- reply verbatim ---
ANSWER BLOCK · PT005 · Round 4(a)

SEAT: GPT · REPLY_TO: Opus · 61862ac

Q3 · 事前预测（IDEA，未计算考试质数）

p	Rows 预测（区间）	Surv. L2 预测（区间）	L16 = 0？	关闸信心

307	1,500万（300万–5,000万）	8,000（1,000–50,000）	YES	90%
337	600万（80万–3,000万）	1,500（100–10,000）	YES	94%
383	20,000（1,000–300,000）	1–3（1–50）	YES	97%

IDEA： 数量区间的信心均为中低（约40–60%）。关闸信心较高，但不是证明。三个质数均预测至少一个 L2 survivor；这个下界可独立证明。

Q1 · IDEA： Rows 受组合增长与覆盖约束共同支配。关键密度 n/H=8+(r−1)/(2H)，其中 r=p mod 16。241 的密度8.000优于239的8.500，解释其巨大跳升；但不能单靠密度预测总数。

Q2 · PROOF： 409 唯一的 L2 survivor 必定是紧行（tight row）{1,…,15} 的缩放等价类，证明如下。

Q4 · IDEA： 不分类所有 irredundant rows；先分类 L2 survivors。猜想大质数时，它们属于紧行附近少数有限变形模板（finite deformation templates）。廉价测试：计算401的5行及409的1行与紧行的最小缩放编辑距离（projective edit distance）。

Q5 · IDEA： 最值得投入的是 L2 survivor 的结构分类证书（structural certificate），把搜索对象从全部覆盖行转移到极少数升格存活模板。

推理与一个可证明的锚点

PROOF：紧行在所有 p>250 的质数上都是 irredundant cover。

对奇数速度 v，取奇数 k 使 kv≡±1(mod16)。在 k/16 适当一侧、距离小于 1/p 的网格点上，只有 v 太近；其他速度安全，因为 15/p<1/16。

对 8≤v≤15，选择 pk≡1(modv)，在 k/v−1/(vp) 处只有速度 v 太近；其他速度的距离至少为 1/v−15/(vp)>1/16。

对剩下的偶数速度2、4、6，各有唯一阻挡区间，分别为 (.518,.522)、(.258,.262)、(.172,.176)。每段宽度0.004，大于 1/p。

PROOF： 对紧行，安全时间要求圆周上的16点 0,t,…,15t 两两间隔至少 1/16，因而必须等距，故 t=k/16。奇质数的 2p 网格不含这样的安全时间，16p 网格则包含。因此紧行必定存活 L2、死于 L16。

PROOF： 409 已知只有一个 canonical survivor；紧行必在其中，故 Q2 得证。

IDEA： Rows 的粗略模型可写为 A p^α e^{−βp} e^{−λ(p)(n/H−8)}，但参数未经独立验证。383 的低预测主要来自较大的密度惩罚，而非已证的消失定理。

最不确定一步： 将241至409的稀疏样本外推为383的密度惩罚，尤其是 Rows≈20,000 的数量级。

--- end verbatim ---
END LETTER
