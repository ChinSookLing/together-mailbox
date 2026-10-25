Puck: R47D proof-read reply, seat=gpt, chat PT-005(2) (Astra: standing chat), collected 2026-10-25 11:47 +08 via copy button, verbatim below. Attachments (.py/.json) not copied.
---
## RESULT BLOCK · PT005 R47D · GPT

FACT｜随机种子（Seed）：47002｜WEB OFF

| 命题                                   | 判定              | 独立样本数                |
| ------------------------------------ | --------------- | -------------------- |
| C1 · Reduced reach criterion         | HOLDS-IN-SAMPLE | 5,000                |
| C2 · Parent cover ⇒ reach            | HOLDS-IN-SAMPLE | 3,000                |
| C2 · Unit time ⇒ parent cover（无附加假设） | COUNTEREXAMPLE  | 4 个 unit cases，3 个反例 |
| C3 · Shallow-depth divisibility      | HOLDS-IN-SAMPLE | 4,027                |
| C4 · Opposite-bit criterion          | HOLDS-IN-SAMPLE | 2,000                |
| C5 · Shallow residue invariance      | HOLDS-IN-SAMPLE | 3,000                |
| C5 · Exact quarter law               | COUNTEREXAMPLE  | 8/8 失败；另 20/20 通过    |

C6｜IDEA： 同意 Kimi 的限制判断。C1–C2 本身未控制其他坐标对 unit times 的竞争，不能单独推出 M2 的深度稀少规律（Depth-rarity law）。

关键发现： C2 的第二句缺少父节点完全覆盖条件；C5 的精确 \\(1/4\\) 比例在 \\(d_j=d+2\\) 失败，但在本次测试的 \\(d_j\ge d+3\\) 情况全部成立。

### FACT｜补充 C2 测试

除了结果块中的 3,000 个偶数坐标样本，又对任意奇偶坐标增加 3,000 个父层覆盖样本：

- 偶数坐标：1,491
- 奇数坐标：1,509
- 违反 parent cover ⇒ reach：0

因此 C2 第一部分合计 6,000/6,000 HOLDS-IN-SAMPLE。

## FACT｜C2 的三个完整反例

这里测试 C2 按字面写出的第二部分，未假设父节点所有奇数时间均被覆盖。

三例均满足：在 \\(2M\\) 层，只有指定的 \\(i=0\\) 坐标能够 reach \\(T\\)，但在父层 \\(M\\)，没有任何坐标覆盖 \\(T\\)。

```

C2-CE1
p=23, k=6, M=1472, d=4
i=0, w_i=180, w'=45, T=115
L=368, ||Tw'||_L=23
h_i(T)=0
parent_covered_by_i=False
parent_covered_by_any=False
coords=[
  180,644,579,1350,96,
  57,1366,322,777,924,
  1209,220,111,1400,880
]

C2-CE2
p=47, k=6, M=3008, d=3
i=0, w_i=456, w'=57, T=2361
L=376, ||Tw'||_L=31
h_i(T)=0
parent_covered_by_i=False
parent_covered_by_any=False
coords=[
  456,138,241,1998,727,
  1201,1166,1042,3005,2553,
  956,1247,641,2751,314
]

C2-CE3
p=47, k=7, M=6016, d=4
i=0, w_i=648, w'=81, T=5421
L=752, ||Tw'||_L=67
h_i(T)=0
parent_covered_by_i=False
parent_covered_by_any=False
coords=[
  648,4284,1242,2697,5861,
  1320,4262,3749,5122,1717,
  3029,1013,3047,1642,4016
]

```

FACT｜限定解释

这些反例不推翻 C2 第一部分。

如果额外规定节点在父层完全覆盖全部所需时间（parent-full-coverage），则 unit time 的父层覆盖必然来自 \\(i\\)。以上三个随机节点不满足该附加假设，因此不能用来反驳附带此假设的版本。

## FACT｜C5：八个完整反例

令

\\[ Q=2^{d+1}p,\qquad T_n=T_0+nQ,\qquad 0\le n\<N=M/Q. \\]

以直接覆盖判定式计算同余类全部奇数 lifts。

下面列出本轮发现的 全部 8 个反例，包括完整参数与实际 reached times。

```

C5-CE1
p=31, k=7, M=3968
d=3, dj=5, w'=413, w=1652
Q=496, T0=333, N=8
expected=2, actual=0
reached_T=[]

C5-CE2
p=31, k=5, M=992
d=1, dj=3, w'=157, w=628
Q=124, T0=85, N=8
expected=2, actual=0
reached_T=[]

C5-CE3
p=37, k=7, M=4736
d=3, dj=5, w'=1157, w=4628
Q=592, T0=35, N=8
expected=2, actual=0
reached_T=[]

C5-CE4
p=29, k=8, M=7424
d=4, dj=6, w'=1043, w=4172
Q=928, T0=467, N=8
expected=2, actual=4
reached_T=[1395,3251,5107,6963]

C5-CE5
p=19, k=5, M=608
d=1, dj=3, w'=149, w=596
Q=76, T0=73, N=8
expected=2, actual=4
reached_T=[149,301,453,605]

C5-CE6
p=41, k=5, M=1312
d=2, dj=4, w'=395, w=790
Q=328, T0=123, N=4
expected=1, actual=2
reached_T=[123,779]

C5-CE7
p=37, k=5, M=1184
d=1, dj=3, w'=159, w=636
Q=148, T0=73, N=8
expected=2, actual=0
reached_T=[]

C5-CE8
p=37, k=4, M=592
d=1, dj=3, w'=49, w=98
Q=148, T0=63, N=4
expected=1, actual=2
reached_T=[211,507]

```

C5 实际覆盖比例

# 4/8

达到 0%

# 4/8

达到 50%

# 0/8

恰好 25%

FACT｜分层对照： 上述八例全部满足 \\(d_j=d+2\\)。另外 20 个满足 \\(d_j\ge d+3\\) 的随机样本，实际比例均恰为 \\(1/4\\)，未发现反例。

IDEA｜给 Argon 的精确修订方向

原本的 \\(d_j\ge d+2\\) 对精确四分之一规律而言过弱。建议将 \\(d_j\ge d+3\\) 作为下一轮候选假设，同时明确同余类必须包含完整的 lift 周期。本轮采样支持这一修订，但尚未给予证明地位（PROVED）。

## FACT｜测试代码与可复算记录

以下是此次实际使用的核心判定代码。所有计算采用整数模运算，无浮点误差。

```
import randomSEED = 47002rng = random.Random(SEED)def D(x, m):    r = x % m    return min(r, m-r)def covered(T, w, M):    return 16 * D(T*w, M) < Mdef reached(T, w, M):    return any(        16 * D(T*(w+b*M), 2*M) < 2*M        for b in (0, 1)    )def bit(T, w, M):    hits = [        b for b in (0, 1)        if 16 * D(T*(w+b*M), 2*M) < 2*M    ]    assert len(hits) <= 1    return hits[0] if hits else None# C1: reduced reach criteriondef check_C1(p, k, d, wp, T):    M = 2**k * p    L = 2**d * p    w = 2**(k-d) * wp    return (        reached(T, w, M)        == (8 * D(T*wp, L) < L)
```

完整脚本包含全部随机生成、C2 的 15 坐标节点测试、C3 的整除性分层、C4 的非对跖双时间筛选、C5 的逐同余类计算，以及全部反例输出。

完整独立测试代码 · seed 47002

原始运行输出 · 全部反例

Final verdict｜FACT： C1、C3、C4 在本轮样本内成立；C2 的父层蕴含成立但 unit-time 推论需要补充假设；C5 的精确四分之一规律在 \\(d_j=d+2\\) 被反例否定。C6 保持为合理的研究限制判断，尚非独立形式证明。

Chair-facing status: 11 counterexamples reported in full; no web search; no enumeration proof claimed.