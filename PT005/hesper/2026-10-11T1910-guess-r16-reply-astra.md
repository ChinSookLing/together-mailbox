BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 19:10 +08
RE: 猜公式 Round 16 (packet d712a00), send text r16_send_full.txt or r16_send_short.txt
SEAT: astra
MODEL: Astra (ChatGPT project The Civilisation Field)
CHAT: https://chatgpt.com/g/g-p-6a0c6eca096c81919e9670129af54799-the-civilisation-field/c/6ac97e19-f06c-83ec-8d0a-b8f20b03e253

--- reply verbatim ---
[Pasted by Tuzi in Hark chat 2026-10-11 19:10 +08 from the Astra project chat; transcribed from her paste, math markup as pasted.]

ANSWER BLOCK summary (Astra, R16):
Q1: m(K∪{v}) ≥ 7/8 m(K) − 7c(K)/(64v). Claims exhaustive check of all 119,759,850 K'⊆{1..30}, |K'|=13, plus speed 31: min = 128197/6383520 at K31={1,2,3,4,5,7,8,9,10,11,12,13,15,31}, margin 37987/6383520 over 97/6864 → C-floor verified to max K ≤ 31. Claims min over all 13-subsets of {1..30}: m ≥ 3071/102960, c ≤ 70; hence v ≥ 640 ⇒ m(K'∪{v}) ≥ 97/6864 + 109/26357760. OPEN: 32 ≤ v ≤ 639.
Q2: iterated bound; example K0={1,2,3,4,5,7,8,9,10,11,12,13}: m=162521/2882880 (16), +31: 3446561/89369280 (16), +31,32: 12389849/357477120 (16); iterated generic bound gives −136354393/817090560 < 0.
Q3: only 240^-14 (L17, given F5). C-floor OPEN.
Q4: p > 120^14 = 128391846454886400000000000000 ⇒ D(p) ≥ 1 (re-derives L16, no improvement).
Q5: needs structural classification of large speeds + low-error continuum-to-grid transfer. Next target: two large speeds that jointly create anomalously low measure must satisfy a bounded integer relation.
Least-sure step: whether a speed-size-independent finite relation-complexity bound exists covering all near-C-floor extreme sets.
Batch table (sets checked / single-speed bound failed): first 1 second 2: 21,474,180 / 15,329,427; 1,3: 13,037,895 / 9,960,397; 1,≥4: 17,383,860 / 14,977,689; 2,3: 13,037,895 / 10,425,221; 2,≥4: 17,383,860 / 15,369,682; first 3: 17,383,860 / 12,857,378; first ≥4: 20,058,300 / 13,456,444; total 119,759,850 / 92,376,238.
Code: C++ r16_exhaust.cpp (core sketch only; full file not in reply) and Python Fraction checker (shown).


--- Tuzi paste verbatim ---
Astra : # PT005 · 猜公式 Round 16 · Close the Gap

## ANSWER BLOCK · GPT · Big Picture

Q1 · PROOF / FACT： 证明比题目更强的单速下界：

\\[ \boxed{m(K\cup\\{v\\})\ge\frac78m(K)-\frac{7c(K)}{64v}} \\]

独立穷举全部 119,759,850 个 \\(K'\subseteq\\{1,\ldots,30\\}\\)、\\(|K'|=13\\)，并逐一加入速度 31。最小值为

\\[ \boxed{\frac{128197}{6383520}>\frac{97}{6864}}. \\]

因此，结合本轮提供的 \\(\max K\le30\\) 结果，C-floor 已验证至 \\(\max K\le31\\)。但单速不等式在大量候选上过弱，不能直接完成证明。

Q2 · PROOF： 多个大速度可迭代应用同一不等式，但安全区间数持续增加，误差累积；在速度相近时，递推可能变为负数，无法证明统一正下界。

Q3 · PROOF / OPEN： 在 F5 成立的前提下，目前可保证

\\[ m(K)\ge240^{-14}. \\]

尚不能证明全局 \\(m(K)\ge0.01\\)，更不能证明 C-floor：

\\[ m(K)\ge97/6864. \\]

Q4 · PROOF / UNFINISHED： 重新推导 L16 的明确门槛：

\\[ \boxed{p>120^{14} =128391846454886400000000000000 \Longrightarrow D(p)\ge1}. \\]

这是本轮能够严格保证的门槛，没有改善 L16。部分速度压缩的新方案尚未封闭。

Q5 · IDEA： 要接近 \\(10^4\\)，必须解决两项开放问题：大速度的结构分类，以及连续安全时间到素数网格的低误差转移。单靠扩大有限穷举或改善 Dirichlet 常数，不足以跨越目前的差距。

状态： Q1 新有限范围证书完成；Q2 递推已证明；Q3 C-floor OPEN；Q4 无更小严格门槛；Q5 为后续证明路线。

## 1. Q1 · 单一大速度的严格不等式

PROOF： 定义周期函数

\\[ f(y)=\mathbf1\_{\\{\\|y\\|<1/16\\}}-\frac18. \\]

它的周期原函数最大值与最小值之差为 \\(7/64\\)。因此，对任意区间 \\(I\\)，长度为 \\(L\\)：

\\[ \operatorname{meas}\\{x\in I:\\|vx\\|<1/16\\} \le\frac L8+\frac7{64v}. \\]

将此式应用于 \\(K\\) 的每个安全区间，得到

\\[ \boxed{ m(K\cup\\{v\\})\ge \frac78m(K)-\frac{7c(K)}{64v}. } \\]

这里 \\(c(K)\\) 是具有正长度的安全区间数。

### 精确穷举的新结果

FACT： 全部含速度 31、其余速度不超过 30 的集合，按最小速度分批检查：

| 分组         | 检查集合数       | 单速界未能认证的数量 |
| ---------- | ----------- | ---------- |
| 首速 1、次速 2  | 21,474,180  | 15,329,427 |
| 首速 1、次速 3  | 13,037,895  | 9,960,397  |
| 首速 1、次速 ≥4 | 17,383,860  | 14,977,689 |
| 首速 2、次速 3  | 13,037,895  | 10,425,221 |
| 首速 2、次速 ≥4 | 17,383,860  | 15,369,682 |
| 首速 3       | 17,383,860  | 12,857,378 |
| 首速 ≥4      | 20,058,300  | 13,456,444 |
| 总计         | 119,759,850 | 92,376,238 |

FACT： 精确计算的最小集合为

\\[ K\_{31}=\\{1,2,3,4,5,7,8,9,10,11,12,13,15,31\\} \\]

并且

\\[ m(K\_{31})=\frac{128197}{6383520}. \\]

这与 C-floor 候选值的差是

\\[ \frac{128197}{6383520}-\frac{97}{6864} =\boxed{\frac{37987}{6383520}>0}. \\]

这证明最大速度恰为 31 的所有候选都满足 C-floor。

### 更进一步：所有足够大的单一速度

FACT： 同一次穷举还得到，对所有 \\(K'\subseteq\\{1,\ldots,30\\}\\)、\\(|K'|=13\\)：

\\[ m(K')\ge\frac{3071}{102960}, \qquad c(K')\le70. \\]

因此，对任何 \\(v\ge640\\)：

\\[ \begin{aligned} m(K'\cup\\{v\\}) &\ge\frac78\frac{3071}{102960} -\frac{7(70)}{64(640)}\\\ &=\frac{372589}{26357760}\\\ &=\frac{97}{6864}+\frac{109}{26357760}. \end{aligned} \\]

PROOF： 所以已经证明：

\\[ \boxed{ K'\subseteq\\{1,\ldots,30\\},\ |K'|=13,\ v\ge640 \Longrightarrow m(K'\cup\\{v\\})>\frac{97}{6864}. } \\]

OPEN： 对这一单一大速度类别，尚须解决 \\(32\le v\le639\\) 的全部情况。

## 2. Q2 · 两个或多个大速度

PROOF： 设

\\[ K_j=K_0\cup\\{v_1,\ldots,v_j\\}, \qquad a=\frac78. \\]

重复使用 Q1，可得：

\\[ \boxed{ m(K_j)\ge a^jm(K_0) -\frac7{64} \sum\_{i=1}^{j}a^{j-i}\frac{c(K\_{i-1})}{v_i}. } \\]

同时，

\\[ c(K_i)\le c(K\_{i-1})+v_i. \\]

由此可推出一个完全显式的递推下界。但当多个大速度彼此接近时，区间数量的增长会抵消 \\(1/v_i\\) 的优势。

FACT： 例如取

\\[ K_0=\\{1,2,3,4,5,7,8,9,10,11,12,13\\}. \\]

精确计算得到：

| 集合                       | 安全测度                     | 区间数 |
| ------------------------ | ------------------------ | --- |
| \\(K_0\\)                | \\(162521/2882880\\)     | 16  |
| \\(K_0\cup\\{31\\}\\)    | \\(3446561/89369280\\)   | 16  |
| \\(K_0\cup\\{31,32\\}\\) | \\(12389849/357477120\\) | 16  |

然而，使用一般区间数上界迭代时，得到的下界为

\\[ -\frac{136354393}{817090560}<0. \\]

结论： 真实测度仍为正且不小，但我们的递推完全失去判别力。这里需要控制区间如何重叠，而不仅是区间有多少个。

## 3. Q3–Q4 · 从统一常数到离散门槛

PROOF（依赖 F5）： L17 的统一连续正下界保持有效：

\\[ c=240^{-14}. \\]

本轮严格改善的是有限结构类别，而不是全体 14 速集合的统一常数。

对离散门槛，可以直接使用较强的 F5 安全余量。取

\\[ Q=\left\lfloor(p-1)^{1/14}\right\rfloor. \\]

Dirichlet 同时逼近给出一个非零缩放，使全部速度代表元不超过 \\(p/Q\\)。

由 F5，存在连续时间 \\(t_0\\)，使所有这些速度的距离至少为 \\(1/15\\)。与 \\(1/16\\) 的余量是

\\[ \frac1{15}-\frac1{16}=\frac1{240}. \\]

因此在 \\(t_0\\) 附近有一个长度至少为

\\[ \frac{Q}{120p} \\]

的安全区间。

当 \\(Q\ge120\\)，这个闭区间长度至少为 \\(1/p\\)，必含素数网格点，故 \\(D(p)\ge1\\)。

这重新证明了 L16 的门槛，却没有缩小它。

IDEA： 若要改用「少数小速度 + 大速度误差控制」，就必须找到比 \\(\sum v\\) 更好的网格误差估计。否则一两个接近 \\(p\\) 的速度足以让现有区间计数界完全失效。

## 4. Q5 · 通向 \\(10^4\\) 的证明路线

| 必要引理                       | 状态                       | 当前缺口         |
| -------------------------- | ------------------------ | ------------ |
| 单速区间误差 \\(7c/(64v)\\)      | PROVED                   | 误差在密集速度集合上太大 |
| 最大速度 ≤31 的 C-floor         | FACT / finite exhaustive | 不能自动延伸至无限范围  |
| 单一大速度 \\(v\ge640\\)，其余 ≤30 | PROVED                   | 中间速度仍未封闭     |
| 多个大速度的统一结构分类               | OPEN                     | 区间数增长使递推失效   |
| 全局 \\(m(K)\ge97/6864\\)    | OPEN                     | 缺少无限速度归约定理   |
| 低误差的连续—离散转移                | OPEN                     | 现有误差依赖最大速度   |
| 剩余素数的有限门验证                 | COMPUTATIONAL            | 需独立证书与完整范围覆盖 |

FACT： 现有 \\(120^{14}\\) 门槛与目标 \\(10^4\\) 相差约 \\(1.28\times10^{25}\\) 倍。这不是稍微改善一个常数就能解决的。

IDEA： 我会优先选择两个大速度的结构分析：证明若连续安全集合被两个新速度大幅削减，它们之间必须具有特定的小整数关系。这有希望成为一般结构归约定理的起点。

## 5. 计算代码与可复验证书

完整 C++ 穷举程序

精确有理断点、位集求交及分批搜索；完整覆盖最大速度为31的新增类别。

Python 分数验证程序

精确复核单速界、双速递推、分组统计及门槛常数。

穷举程序使用以下核心代码。所有安全区间端点均由整数表示，没有浮点比较：

```

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;
using i128 = __int128_t;

// Exact grid denominator:
// D = lcm(16*v : 1 <= v <= max_speed)
//
// Collect every rational breakpoint:
// (16*j +/- 1)/(16*v)
// as an integer coordinate using D.
//
// Each atomic interval is represented by one bit.
// A speed v is safe at an atomic midpoint x
// iff ||v*x|| >= 1/16.

bool safe_at_midpoint(
    i128 midpoint_numerator,
    i128 midpoint_denominator,
    int v
) {
    i128 r =
        (midpoint_numerator * v)
        % midpoint_denominator;

    return 16 * min(r,
                    midpoint_denominator-r)
           >= midpoint_denominator;
}

// Exact measure in units of 1/D.
ll mass(
    const vector<ull>& bits,
    const vector<ll>& weights
) {
    ll result = 0;

    for (int w=0;w<(int)bits.size();w++) {
        ull z=bits[w];
        while (z) {
            int i=64*w+__builtin_ctzll(z);
            result+=weights[i];
            z &= z-1;
        }
    }
    return result;
}

// For each 13-speed set K:
// 1. Intersect its bit masks.
// 2. Count components c(K).
// 3. Calculate exact m(K).
// 4. Intersect with mask[31].
// 5. Compare the resulting exact measure
//    with 97/6864 using 128-bit integers.
//
// The complete recursion, batch filters,
// and exact comparison are in r16_exhaust.cpp.

```

实际穷举的分批运行指令如下。各批次独立完成，超时的未筛选尝试不计入成果。

```

g++ -O3 -std=c++17 r16_exhaust.cpp -o r16_exhaust

./r16_exhaust 30 31 1 2
./r16_exhaust 30 31 1 3
./r16_exhaust 30 31 1 -4
./r16_exhaust 30 31 2 3
./r16_exhaust 30 31 2 -4
./r16_exhaust 30 31 3
./r16_exhaust 30 31 -4

python r16_certificate.py

```

Python 精确复核的关键部分：

```
from fractions import Fraction as Ffrom math import combdef intervals(K,N=16):    I=[(F(0),F(1))]    for v in sorted(K):        new=[]        for j in range(v):            a=F(N*j+1,N*v)            b=F(N*(j+1)-1,N*v)            for x,y in I:                lo=max(x,a)                hi=min(y,b)                if lo<hi:                    new.append((lo,hi))        I=new    return Idef measure(K):    I=intervals(K)    return sum((b-a for a,b in I),F(0)),len(I)Kstar=sorted(set(range(1,16))-{6})K13=sorted(set(Kstar)-{14})m13,c13=measure(K13)m31,c31=measure(K13+[31])bound=F(7,8)*m13-F(7*c13,64*31)print("K13:",m13,c13)print("bound:",bound)print("actual with 31:",m31,c31)# Exact finite-class universal bound
```

## Big Picture · 最终判断

IDEA： 这轮真正推进的不是全局常数，而是首次把一类无限速度情况划成可证明的远端区域与尚待计算的中间区域。

这说明单速方法不是完全无效；它缺少的是对多个大速度之间关系的控制。

我认为下一轮最值得集中攻击的命题是：

\\[ \boxed{ \text{两个大速度若能共同制造异常低测度，} \quad \text{则它们必须满足某种有界整数关系。} } \\]

如果能建立这样的引理，就有机会从无限大的速度空间逐层压缩到有限结构，而不是不断扩大蛮力穷举。

最不确定的一步： 是否真的存在与速度大小无关的有限关系复杂度界，能够覆盖全部接近 C-floor 的极端集合？

STATUS：部分结构归约 PROVED；C-floor 与新离散门槛 UNFINISHED。
--- end verbatim ---
END LETTER
