BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 15:47 +08
RE: 猜公式 Round 13 (packet 2e9272a), send text r13_send_full.txt or r13_send_short.txt
SEAT: gpt
MODEL: GPT-6 High
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6acb3150-2f20-83ec-8f22-82b1f371fad7

--- reply verbatim ---
GPT-6, thinking High. Chat 'Review packet answers'. Recovered after 'Connection interrupted' by one reload; no resend. Captured by page extraction.


PT005 · 猜公式 Round 13 · ANSWER BLOCK

Q1 — Missed connections

FACT / IDEA — 三条值得补上的连接：

R8 ↔ R10：随机基线并不完全相同。 Fourier 零频项 M0 不等于从互异速度中随机抽样的精确期望。有限总体修正可能影响 Poisson 模型对稀有覆盖的预测。

R7 ↔ R11 ↔ R12：乘法对称性、子群与极值统计。 缩放等价类可能具有特殊稳定子（stabilizer）。简单除以 n 的候选数模型需要检验。

R2 ↔ R10：Dirichlet 缩放与共振复杂度。 缩小速度代表元不一定降低 Fourier 频率复杂度。如果能建立两者的定量关系，可能绕开过大的指数门槛。

Q2 — Errors

FACT： 回顾中至少有三处需要修正：

§3「431–499 为 1–2」遗漏了 p=457 的零缺口。

§7「合数速度的窗口落在因数窗口里」若指全局包含，则错误；只有特定窗口可能包含。

§7 把随机计数模型与 Fourier 零频项视为同一件事，忽略了互异速度抽样的修正。

Q3 — Independent verification

FACT： 独立求解 p=337，找到一个包含恰好三个小速度的覆盖集合，并逐格验证 U=0。这确认了 §3 的一项存在性事实，而非全部分布。

Q4 — Next step

IDEA： 优先证明针对所有速度集合的统一共振反抵消定理（uniform resonance anti-cancellation theorem），并参数化到一般跑者数 N。它将直接给出 D_N(p)>0，不依赖穷举。

Q5 — For Tuzi

这张证明桌找到了一条把随机现象与速度之间的数学关系连接起来的精确公式，也找到了越来越有效的预测方法。它已经能解释为什么覆盖会变得罕见，以及某些特别的速度组合为什么仍能成功。但我们尚未证明这些例外最终一定消失。现在最重要的，不是再收集更多漂亮数字，而是证明共振不可能永远完全抵消随机部分。

WORK

Q1 · 三条连接的数学意义

1. FACT — 随机抽样与零频项的差异

令 n=(p−1)/2、H=⌊(p−1)/16⌋。

Fourier 零频基线为

M0(p) = p/2 (1 − (2H+1)/p)^14.

从 n 个速度类中不放回地均匀抽取 14 个，则实际期望为

E_distinct[U] = n * C(n−H, 14) / C(n, 14).

PROOF： 对固定格点，恰有 H 个速度不安全。全部抽中安全速度的概率是上述组合数之比；对格点求和即得期望。

本轮计算：

p     M0          E_distinct[U]    差
337   24.925502    23.864545        1.060957
457   35.391525    34.349743        1.041783

IDEA： 若极值模型主要由接近零的尾部决定，这种有限总体修正可能影响预测。尚未检验其实际预测收益。

2. IDEA — 对称性影响极值候选数

R11 的缩放不变性说明：

U(aS) = U(S),  a ∈ F_p^×.

因此，缩放轨道中的集合不是独立样本。

R7 的子群构造还提示，部分轨道具有非平凡稳定子。若要精确计数，可考虑使用轨道–稳定子定理（Orbit–Stabilizer Theorem）及 Burnside 引理，而不是统一除以 n。

若成立： 可改进 R8 的候选集合计数，并识别哪些代数结构更容易形成异常小的 U。

3. IDEA — Dirichlet 缩放与 Fourier 关系

R2 通过模缩放选取较小的速度代表元；R11 则表明截断共振在相同模缩放下不变。

潜在结论： 几何上的小速度与 Fourier 意义上的低频关系不是同一个概念。下一步应研究是否存在一个同时控制两者的、缩放不变的复杂度指标。

这条连接目前只是研究方向。

Q2 · 回顾中的错误与修订

错误 A — 范围表述

「D(p)：431–499 为 1–2」

FACT： p=457 存在完整覆盖，因此该范围的 D 可以为零。

修订： 应排除 457，或者明确将范围改为包含零的表述。其他质数的精确最小值仍依赖主席普查或独立验证。

错误 B — 窗口包含的范围

「合数 v = g·(v/g) 的窗口落在因数窗口里」

FACT： 这不是普遍的集合包含关系。

计算反例：

p=101, H=6, t=8.
‖12t‖_p = 5 ≤ H,  ‖6t‖_p = 48 > H.

所以 t ∈ C_12，但 t ∉ C_6。

修订： 必须限定具体窗口及其指标；这不推翻 Kimi 原先较窄的窗口引理。

错误 C — 两个随机量的等同

「R5 普查 = R8 泊松公式 = R10 随机部分 M(p)」

FACT： 这是一条有用的概念连接，但不是三个数学表达式的严格等同。实际均匀互异抽样期望与 Fourier 零频项不同。

修订： R10 是恒等分解，R8 是概率近似，R5 是离散普查；三者应明确区分。

状态修正建议： §6 将「短关系没有信号」列为 REFUTED 时，应说明“按关系长度截断”与“按 Fourier 频率截断”不同。一个截断方法有效，并不能自动反驳另一个方法的特定失败结果。

Q3 · 独立验证（代码）

选取 §3 的事实：

「337 覆盖样本……其中 3 个 M_15 = 3」

本轮只验证存在一个 M_15=3 的覆盖，不尝试重建样本总数或完整分布。

FACT — 独立找到的集合：

S = {2, 6, 14, 16, 17, 20, 22, 23, 26, 29, 36, 38, 42, 43}.

其中小速度为 2, 6, 14。

以下代码以混合整数规划（MILP）独立寻找集合，再以整数模运算逐格复核。

[code block 1 — MILP search]
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

p = 337
n = (p-1)//2
H = (p-1)//16

A = np.array([
    [int(min(v*t % p, p-v*t % p) <= H)
     for v in range(1,n+1)]
    for t in range(1,n+1)
], dtype=float)

B = np.zeros((2,n))
B[0,:] = 1
B[1,:15] = 1

r = milp(
    np.linspace(0,1,n),
    integrality=np.ones(n),
    bounds=Bounds(np.zeros(n),np.ones(n)),
    constraints=[
        LinearConstraint(A,np.ones(n),np.inf),
        LinearConstraint(B,[14,3],[14,3])
    ],
    options={"time_limit":7,"mip_rel_gap":0.5}
)

assert r.x is not None
S = (np.where(r.x > 0.5)[0]+1).tolist()

U = sum(
    all(min(v*t%p,p-v*t%p)>H for v in S)
    for t in range(1,n+1)
)

本轮运行结果：M15 = 3；U = 0。MILP 负责发现候选，最后的整数检查负责验证覆盖。

PROOF（有限实例）： 每个格点至少被集合中某个速度覆盖，所以该集合确实是有效的 14-cover。

UNFINISHED： §3 关于完整样本分布的计数尚未独立复核。

额外算术复核

以下代码独立复算 Q1 的基线差异以及 Q2 的两个反例；每次只涉及一个质数的直接计算。

[code block 2 — baseline + counterexamples]
import math

for p in [337,457]:
    n=(p-1)//2
    H=(p-1)//16
    M0=(p/2)*(1-(2*H+1)/p)**14
    E=n*math.prod(
        (n-H-j)/(n-j) for j in range(14)
    )
    print(p,round(M0,9),round(E,9),
          round(M0-E,9))

p=457
S=[1,30,34,56,57,58,118,144,
   170,171,172,173,201,228]
H=(p-1)//16
U=sum(
    all(min(v*t%p,p-v*t%p)>H for v in S)
    for t in range(1,(p-1)//2+1)
)
print("p457 U =",U)

p,t=101,8
for v in [6,12]:
    z=v*t%p
    print(v,min(z,p-z))

输出关键结果：

p=457：U=0。

p=101, t=8：速度 6 的距离为 48，速度 12 的距离为 5。

两组随机基线数值如前表。

Q4 · 只选一个下一步

IDEA — 统一共振反抵消定理

设对一般 N，使用 N−2 个速度类，定义相应的 Fourier 零频项 M_N(p) 与共振项 R_N(S)。

希望证明存在仅依赖 N 的正常数 ε_N, C_N，使所有足够大的质数和所有候选集合满足

R_N(S) ≥ −(1−ε_N) M_N(p) − C_N.

由恒等式立即得到

U_N(S) ≥ ε_N M_N(p) − C_N.

若 M_N(p) 随 p 线性增长，则足够大的 p 必有 U_N(S)>0。

PROOF（条件推论）： 该不等式一旦建立，就直接给出最终无覆盖结论。

IDEA： 与其继续拟合 D(p)，更有价值的是识别哪些短整数关系能产生强负共振，再证明这些关系不能同时消灭全部剩余格点。

这也能自然推广至不同 N。

UNFINISHED： 当前没有证明 ε_N>0，也没有控制高频共振尾部的统一估计。

Q5 · 给 Tuzi 的总结

这十二轮真正建立的，是一套能够让不同 AI 共同提出猜想、独立计算、发现反例并逐项校验的数学研究方法。我们不仅知道哪些速度组合可能成功，也开始理解为什么成功：一般组合会留下缺口，特殊的数字关系却可能把缺口全部填掉。现在数学上最难的墙已经很清楚——要证明这种特殊关系不可能无限延续，而不是只靠电脑发现它越来越罕见。如果攻破这一点，成果就可能不只属于十六跑者，也能帮助研究更多跑者的情况。

Least-sure step： 从已观察到的低频关系和有限样本，推断存在统一的正共振余量 ε_N。这是整份答复中最关键、也最没有得到证明的环节。

最终状态： Q3 独立验证完成；Q1 的连接为待检验研究方向；Q2 提供可复核修正；Q4 的统一定理仍为 UNFINISHED。


--- end verbatim ---
END LETTER
