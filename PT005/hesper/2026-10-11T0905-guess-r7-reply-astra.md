BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 09:05 +08
RE: 猜公式 Round 7 (packet 1006d95), send text r7_send_full.txt or r7_send_short.txt
SEAT: astra
MODEL: ChatGPT Thinking High (Astra project)
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253

--- reply verbatim ---
# Round 7 reply metadata
- Model/effort: ChatGPT / Thinking effort High
- Worked for: 2m 9s
- Status on page: Latest response (no Stop button, generation complete)
- "Analysis paused" label shown, but final answer rendered

# Round 7 ANSWER BLOCK (captured verbatim)

ANSWER BLOCK · GPT · Round 7

Q1 · PROOF / FACT： 尚未证明 C-core4 对所有素数成立。但对 31 ≤ p ≤ 139，任何 14-speed 集合都有 M₁₅ ≥ 4。另外，主席完整枚举的 10 个素数、47 个覆盖全部满足 C-core4。新找到 p = 307 的 14-speed 集合具有 M₁₅ = 3，但遗漏 16 格，不是 cover。

Q2 · IDEA： 4 未必是 16 跑者独有的常数。对一般阈值 1/N，可以证明平均核心容量为 2(N−2)(N−1)/(p−1)。猜测在接近覆盖极限的素数上，核心底线可能随 N 增长；候选 f(N) ≈ N/4，信心 20%，未经其他 N 验证。

Q3 · FACT / IDEA： 1,365 个四速核心可显著缩减原始组合空间。以 p = 431 为例，直接扩展四速核心的候选量约为全部 14-speed 组合的 1.58%，理论枚举量缩小约 63 倍。但这不是实际运行时间保证。可以用约数窗口包含关系和剩余覆盖容量进一步剪枝。457 的存在说明覆盖并未在 431 后彻底消失。

Q4 · IDEA： 337 盲预测 M₁₅ = 4：150–360 个，中心预测约 230；置信度 65%。 最大 M₁₅：8–10，单点预测 9；置信度 70%。# Round 7 Reasoning — captured verbatim

Reasoning

1. C-core4 的严格部分证明

PROOF： 令 S 为任意 14 个不同速度，n = (p−1)/2。对所有缩放计算小核心数量：

(1/n) ∑_{u=1}^{n} #{v ∈ S : ‖uv‖_p ≤ 15} = 210/n.

因此，M₁₅(S) ≥ ⌈210/n⌉。当 p ≤ 139，有 n ≤ 69，故 M₁₅ ≥ 4。

FACT： 但这个平均数界无法证明 p = 307 的 C-core4。 我在允许计算的 p = 307，用整数规划构造：

Plain text
S = [29,36,37,49,50,77,78,92,95,124,132,136,144,149]
M15(S) = 3
Uncovered cells = 16

PROOF： 其结果可由下面的穷举检查复现：

Python
p = 307
S = [29,36,37,49,50,77,78,92,95,124,132,136,144,149]
n, H = (p-1)//2, (p-1)//16
def d(x):
    r = x % p
    return min(r, p-r)
M = max(sum(d(u*v)<=15 for v in S) for u in range(1,n+1))
U = [t for t in range(1,n+1) if all(d(v*t)>H for v in S)]
assert (M,len(U)) == (3,16)

IDEA： 这说明「四速底线」不是纯粹的集合大小定理；若成立，必须真正利用 cover 条件。2. 1,365 核心的搜索成本

PROOF： 不去重的候选数为： 1365·C(n−4, 10)。全部候选数为 C(n, 14)。

p     核心搜索占原始空间  理论缩减
307   6.23%              16.1 倍
431   1.58%              63.4 倍
499   0.87%              114.4 倍

IDEA： 更值得尝试的剪枝是：对四速核心 K，计算未覆盖集合 U_K。将所有候选补位速度在 U_K 上的覆盖数量排序；如果最大的十项之和仍小于 |U_K|，则这个核心必然无法完成覆盖。

PROOF： 若 a | v，且速度 v 的窗口分子 i 满足 v/a | i，那么该窗口已包含在速度 a 的窗口内。因此当 a ∈ K 时，可以排除这些重复贡献。

3. 337 预测依据

FACT： 307 的 274 个随机样本中，40 个具有 M₁₅ = 4，比例约 14.6%；321 个汇总样本则约为 15.6%。

IDEA： 将约 15.6% 暂作预测参考，应用于 337 的 1,477 个覆盖，得到约 230 个。最大容量 9 则依据 307 样本已达到 9 的观察，而非定理。

最不确定的一步： 不同素数的 14-cover 核心容量分布是否足够接近，能够用 307 的抽样结果推断 337？

STATUS：C-core4 UNFINISHED。337 与 503–599 均未计算。

— End of Round 7 reply —
--- end verbatim ---
END LETTER
