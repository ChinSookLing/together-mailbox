BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 19:46 +08
RE: 猜公式 Round 19a structure of covers (packet ff5f466), send text r19a_send_gpt.txt
SEAT: gpt
MODEL: GPT-6 High (Power), web off
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6accc3cc-55a4-83ec-b793-b0db458b55dc

--- reply verbatim ---
（Worked for 16m 27s；page model label: High / GPT-6；code block from code-pane Copy, prose from page extract）

PT005 · Round 19a · GPT PROPOSER REPLY

题包 ff5f466 · Structure of irredundant covers · 【READ：r19a_send_gpt.txt，含完整数据】

ANSWER BLOCK

FACT — 数据核验。 两份 p=383 样本共 125 行（11＋114），全部是互不重复的 15-class irredundant covers。125/125 含普通三项等差关系（3-term arithmetic progression, AP3）。另附的五个稀有覆盖样本也全部含 AP3。

PROOF — 提议一：模关系种子生成器（Modular Chord Generator）。

令 m=⌊(p−1)/16⌋，将覆盖正规化，使 1∈S。对每个测试时间 t>m，必须有另一类 v∈S 满足

tv≡±r(modp), 1≤r≤m.

由这些短模关系构造最小击中集（minimal transversals），再扩展成 15 类候选。此生成方式对所有正规化覆盖成立，不依赖统计猜测。

FACT — 383 实测。 采用 t=24,…,43 的测试窗口：

严格可靠的生成规则：125/125，候选数 17,512,037,305,854,513,146。

增加低端及高端锚点的实验性规则：125/125，候选数 4,048,872,897,838,882,650。

两项数量均由下方代码使用容斥法（inclusion–exclusion）精确计算。

IDEA — 提议二。 覆盖可能存在低速锚点、模关系骨架与加法结构之间的耦合。AP3 是值得进一步检验的生成核心。

UNFINISHED。 未证明实验性锚点条件对全部覆盖成立，也未证明 AP3 必然存在。当前候选空间仍过大，不能宣称已取代闸门搜索。

1. 结构陈述（Structural Statement）
1.1 PROOF — 模关系骨架

定义

n=(p−1)/2, m=⌊(p−1)/16⌋.

取一个包含 class 1 的正规化覆盖 S。

在时间 t>m、t≤n 时，class 1 已经不能覆盖该时间。

因此，必有另一个 class v∈S∖{1}，使

min(vt mod p, p−(vt mod p))≤m.

等价于

tv≡±r(mod p), 1≤r≤m.

这给出了可直接计算的模关系（modular relation），而不只是“覆盖似乎具有较多加法关系”的统计描述。

对每一个选定时间 t，定义

Ht = {v∈{2,…,n} : tv≡±r(mod p), 1≤r≤m}.

则任何符合条件的覆盖必须满足

S∩Ht ≠ ∅ 对所有选定的 t.

这是严格必要条件。

1.2 PROOF — 从条件到生成算法

将每个 Ht 视为一条超边（hyperedge）。

不直接枚举所有 15 类集合，而是先求这组超边的最小击中集。

初始 M0 = {∅}.

每加入一条超边 Ht，执行

M_{i+1} = Min⊆{K∪{v} : K∈Mi, v∈Ht}.

其中 Min⊆ 删除包含其他候选的非最小集合。

最后，对每个最小种子 K，补入其余 classes，使集合达到指定大小，并去重。

为什么不会漏掉真实覆盖？

任何真实覆盖都击中全部 Ht，而任何有限击中集都包含一个包含关系下的最小击中集。因此真实覆盖必定包含某个生成器种子。

这一点已经证明。

这是一种通过最小击中集扩展候选的方法，而非从所有 15 类组合开始逐一测试。但最小种子的计算仍可能昂贵，不能据此声称算法更快。

1.3 IDEA — 实验性锚点结构

针对本次 p=383 数据，再提出：

A = {2,3,…,8},
B = {170,171,…,191}.

实验性条件为

S∩A ≠ ∅, S∩B ≠ ∅.

它表示正规化集合除了 class 1，还需要一个低端锚点，以及一个接近 folded-class 上界的锚点。

这与题包描述的低速聚集和结构化余部相容，但并非它们的证明。

此条件仅是一项由样本支持的候选假说，不是通用定理。

2. 真实数据测试（Data Test）
2.1 FACT — 核验结果

以下所有计数都来自下方代码。

检查项目                  结果
第一组数据                 11
第二组数据                 114
合计                       125
满足完整覆盖与不可约性     125
通过模关系测试窗口         125
同时包含 A,B 锚点         125
含普通 AP3                 125
附件中含 AP3 的稀有样本    5 / 5

其中，AP3 指存在三个不同的、按整数顺序排列的 classes：

a<b<c, a+c=2b.

这不是模 p 下容许正负号的更宽松定义。

2.2 FACT — 实验性条件并非跨素数普遍成立

我还检查了附件中的稀有覆盖样本。

p     AP3  低端锚点 2–8  高端 22 类窗口
379  有     有            有
409  有     有            有
419  有     有            没有
421  有     有            有
457  有     有            有

高端窗口在这里按 n−21,…,n 取值。

IDEA： 419 的例子已经表明，不能把在 383 观察到的端点锚定形式直接提升为所有素数的定理。

尤其要注意，383 的两个工作分支并非均匀抽样。因此 125/125 不等于全闸门的 100%，也不能据此确定未提供的数据满足同一条件。

3. 候选空间的精确计数
3.1 PROOF — 容斥计数

对 p=383，代码算得 n=191, m=23.

选取

T = {24,25,…,43},
V = {2,…,191}.

首先只使用可证明的 Ht 必要条件。

对于任意排除集合 E⊆V，定义

F(E) = ∑_{J⊆T} (−1)^{|J|}  C(|V ∖ (E ∪ ⋃_{t∈J} Ht)|, 14).

理由是：容斥法从所有不包含 E 的 14 类候选中，逐项排除完全避开某个 Ht 的集合。

因此

N_safe = F(∅).

如额外要求同时击中 A,B，则

N_hyp = F(∅) − F(A) − F(B) + F(A∪B).

这里的 N_safe 是严格可靠的超集大小；N_hyp 是实验性规则所定义的超集大小。

3.2 FACT — 精确计算结果

正规化后的全部 15-class 组合           561,085,262,732,401,541,415
严格可靠的 20 个模关系约束             17,512,037,305,854,513,146
再加入实验性低端／高端锚点             4,048,872,897,838,882,650

上述均为去重后的不同候选行数，而不是种子扩展时重复输出的次数。

4. 完整复算代码（Python）

以下代码仅使用题包内的数据，不调用网络，也不使用随机估计。

```python
from pathlib import Path
from math import comb

text = Path("r19a_send_gpt.txt").read_text()

def lines(section):
    part = text.split(
        "=== " + section + " ===", 1
    )[1].split("=== ", 1)[0]
    return [s.strip() for s in part.splitlines()
            if s.strip()]

def dec(h):
    return [int(h[i:i+2], 16)
            for i in range(0, len(h), 2)]

G0 = [dec(s) for s in lines("rows_383_0_10.txt")]
G1 = [dec(s) for s in lines("rows_383_14_4.txt")]
rows = G0 + G1

rare = [
    list(map(int, s.split()))
    for s in lines("rare_14class_covers.txt")
    if not s.startswith("#")
]

p = 383
n = (p - 1) // 2
m = (p - 1) // 16
T = list(range(m + 1, m + 21))
V = range(2, n + 1)

def near(v, t, modulus=p):
    a = (v * t) % modulus
    return 16 * min(a, modulus-a) < modulus

def AP3(S):
    z = set(S)
    return any(
        2*b-a in z
        for a in S for b in S if a < b
    )

def irredundant(S):
    near_sets = [
        {v for v in S if near(v,t)}
        for t in range(1,n+1)
    ]
    return (
        all(near_sets)
        and all(
            any(Q == {v} for Q in near_sets)
            for v in S
        )
    )

def bits(values):
    return sum(1 << (v-2) for v in values)

H = [
    bits(v for v in V if near(v,t))
    for t in T
]

A = bits(range(2,9))
B = bits(range(170,n+1))

# Exact inclusion-exclusion.
def F(exclude):
    U = [0] * (1 << len(T))
    ans = 0

    for J in range(len(U)):
        if J:
            bit = J & -J
            U[J] = (
                U[J ^ bit]
                | H[bit.bit_length()-1]
            )

        available = 190 - (
            U[J] | exclude
        ).bit_count()

        if available >= 14:
            term = comb(available,14)
            ans += (
                -term if J.bit_count()%2
                else term
            )

    return ans

f0 = F(0)
fa = F(A)
fb = F(B)
fab = F(A | B)

empirical = f0 - fa - fb + fab

print("Groups:",len(G0),len(G1))
print("Total:",len(rows))
print("Irredundant:",
      sum(map(irredundant,rows)))

print("All probes:",
      sum(all(any(near(v,t) for v in S)
              for t in T) for S in rows))

print("Both anchors:",
      sum(any(2<=v<=8 for v in S)
          and any(170<=v<=191 for v in S)
          for S in rows))

print("AP3:",sum(map(AP3,rows)))
print("Rare AP3:",
      sum(AP3(z[2:]) for z in rare))

print("n,m:",n,m)
print("Baseline:",comb(190,14))
print("F0, FA, FB, FAB:",f0,fa,fb,fab)
print("Safe generator:",f0)
print("Empirical generator:",empirical)

for pp, count, *S in rare:
    nn = (pp-1)//2
    print(
        "Rare",pp,
        "AP3",AP3(S),
        "low",any(2<=v<=8 for v in S),
        "high",any(nn-21<=v<=nn for v in S)
    )
```

4.1 FACT — 四个容斥中间值

项目                       精确值
F(∅)                       17,512,037,305,854,513,146
F(A)                       12,790,823,628,732,364,923
F(B)                        2,369,578,828,542,577,332
F(A∪B)                      1,697,238,049,259,311,759

按公式相减相加，即得实验性生成器的精确候选数。

5. PROOF / IDEA — 这是否接近真正的结构定理？

PROOF： 模关系骨架提供了一种严格正确的生成方式。每个真实覆盖都包含一个击中全部指定超边的最小种子。

IDEA： 可以将 AP3 作为种子中的加法配置（additive configuration），研究最小击中集是否必须同时包含这样的配置，以及配置与低速锚点是否存在更强的耦合。

UNFINISHED： 还不能证明 AP3 是所有 irredundant covers 的必要条件。即使添加 AP3 后实测样本仍全部保留，加入 AP3 过滤后的精确候选数量也尚未计算。

对 Beck–Everett 的关联，本答复只依据题包提供的概述，【MEMORY／未独立阅读原论文】。这里证明的短模关系不等同于题包所说的奇数坐标和、受限 ℓ1 范数的关系定理；不能互相替代。

最关键的限制是：当前生成器虽然数学上可靠，但输出候选仍极多。是否能通过最小种子压缩、加法配置过滤与后续提升（lift）条件，把它变为优于现有 gate 的实际算法，仍需实验。

6. 最后一行回答（One-line last question）

FACT / IDEA： 在 p=383，严格可靠的模关系生成器产生 17,512,037,305,854,513,146 个不同候选；加入尚未证明的低端／高端锚点假说后为 4,048,872,897,838,882,650 个。两者均是精确计算值；真正可用于加速闸门的强结构生成定理仍为 UNFINISHED。

--- end verbatim ---
END LETTER
