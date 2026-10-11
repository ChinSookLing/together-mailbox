BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 17:07 +08
RE: 猜公式 Round 14 (packet 1473ae0), send text r14_send_full.txt or r14_send_short.txt
SEAT: gpt
MODEL: GPT-6 High
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6acb4df4-0384-83ec-ad98-d73ee9010b01

--- reply verbatim ---
CAPTURE SOURCE: chatgpt.com "猜公式分析" (Formula drill analysis) conversation
URL: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6acb4df4-0384-83ec-ad98-d73ee9010b01
Target: Last assistant turn after user "Please give the final answer now, ANSWER BLOCK first, UNFINISHED allowed." / "Worked for 5m 35s"
Label: ANSWER BLOCK · PT005 Round 14
Capture method: overlapping extract_content chunks (Copy message button at 1-105 copied the user message, not the assistant reply; used find_text + extract_content).

=== VERBATIM BEGINS (chunk 1) ===

ANSWER BLOCK · PT005 Round 14
Q1｜FACT / UNFINISHED
独立计算得到以下上界（均非精确最小值）：
p	p	D(p)≤	D/E≤
1499	15	0.130400
1999	18	0.116727
2503	21	0.109472
3001	21	0.091091
IDEA：
搜索所得比率下降，但只有上界，不能证明真实的 δ(p) 下降或稳定。统一正下界仍 UNFINISHED。
Q2｜FACT + PROOF
枚举 p≤20000、p≡1(mod 28)：188 个素数，只有 29、281 的子群覆盖全部 cells。
新证明：
利用 Φ28、resultant 与 Fourier 极限，可以严格证明：U(Gp)>0 对所有充分大的 p≡1(mod 28). 这是非定量渐近定理，不只是实验猜想。
实际空陪集比例约为 0.154，而非朴素 Poisson 的 0.030；原因是正负配对。
Q3｜FACT：
Bounded differences 只提供常数级指数；Janson 的依赖项过大。两者不能直接解决问题。
Q4｜IDEA：
最短路线是 Fourier 紧性、极限子环面、统一安全区域引理、紧性下界。最难且尚未证明的是 所有可容许子环面的统一安全区域引理。
Q5｜IDEA：
相同框架适用于 N=17,18,20，但必须分别证明相应的逃逸引理。

计算结果与证明
1. δ(p) 搜索
FACT｜独立计算
使用 14 个速度、随机重启及单点替换局部搜索（single-swap local search）。
p	p	E(p)	找到的 U	U/E
1499	115.030255	15	0.130400
1999	154.205707	18	0.116727
2503	191.830194	21	0.109472
3001	230.538299	21	0.091091
最佳速度集合：
Plain text
1499: [31,124,243,274,367,398,403,465,522,553,579,610,641,672]
1999: [59,139,158,198,297,356,495,535,693,792,891,910,950,971]
2503: [94,175,282,341,376,435,634,717,811,905,940,999,1187,1222]
3001: [156,257,312,468,569,725,826,881,982,1037,1138,1294,1395,1450]
对这四个实验上界作线性拟合：δ^upper(p) = 0.168135 − 0.0000249777 p.
IDEA：该拟合只描述搜索结果，不是 D(p)/E(p) 的渐近公式。
N=20 此处正确推广为 k=N−2=18 个速度，而非继续使用 14 个速度。
p	p	E20(p)	D20(p)≤	D20/E20≤
997	74.576861	14	0.187726
1009	74.268016	13	0.175042
最佳集合：
Plain text
997: [31,45,77,103,116,148,167,180,205,224,238,245,251,341,371,386,463,489]

=== END chunk 1 (need to continue) ===
=== CONTINUATION (chunk 2) ===

1009: [7,22,51,61,95,117,139,172,230,256,297,300,358,373,395,402,490,498]
UNFINISHED：没有证明这些搜索上界就是精确 D。
2. 子群枚举与新的渐近定理
FACT｜枚举
对全部符合条件的素数，得到：
指标	计算结果
素数总数	188
空陪集为零	p = 29, 281
最后一次观测到覆盖	281
空陪集数对 p 的拟合斜率	0.00551645
观测空陪集总体比例	0.15346387
特别是：
p	空陪集数
113	1
197	1
281	0
421	1
449	4
19993	110
因此，281 是这次枚举范围内的最后一个覆盖例子，但还不能说它是所有素数中的最后一个。
为什么 Poisson 估计不对？
PROOF
因为 −1∈Gp，其 28 个元素构成 14 对正负元素。
每一对落入小区间的近似概率是 2H/(p−1) → 1/8.
若先忽略不同正负对之间的相关性，则空陪集概率应近似为 (7/8)^14，而不是 e^{−3.5}。
独立计算得到：(7/8)^14 = 0.154210073, e^{−3.5} = 0.030197383.
第一项几乎精确匹配实际数据。
子群非覆盖定理
PROOF
取 g∈Fp 为 28 阶元素，并考虑 a = (1,g,g^2,…,g^13).
定义概率测度 μp = (1/p) Σ_{t=0}^{p−1} δ_{t a/p (mod 1)} 于 T^{14}。
对任意整数向量 h，定义 Ph(X) = Σ_{j=0}^{13} hj X^j.
其 Fourier 系数为 μp̂(h) = 1 if Ph(g)≡0 (mod p), 0 otherwise.
由于 g 是本原 28 次单位根，Φ28(g)=0 (mod p), 其中 Φ28(X) = X^12−X^10+X^8−X^6+X^4−X^2+1.
若 Φ28 ∤ Ph，则整数 Rh = Res(Φ28, Ph) 非零。

=== END chunk 2 (need to continue) ===
=== CONTINUATION (chunk 3) ===

若 Ph(g)≡0 (mod p)，必有 p | Rh。因此，对固定的 h，当 p>|Rh| 时不可能再发生这种额外关系。
于是：μp̂(h) → 1 if Φ28 | Ph, 0 otherwise.
由 Fourier 唯一性及三角多项式逼近，μp 弱收敛至子环面 T 上的 Haar 测度。
该子环面满足两条关系：
x0−x2+x4−x6+x8−x10+x12 = 0 (mod 1),
x1−x3+x5−x7+x9−x11+x13 = 0 (mod 1).
现在构造一个严格安全点：x0=x1=x4=x5=1/4，其余坐标全部取 1/2。
直接代入可验证两条关系均成立，而且每个坐标都严格满足 ‖xj‖ > 1/16.
所以安全集合与 T 的交集包含一个非空相对开集，具有正 Haar 测度。
由于安全集合边界的极限测度为零，弱收敛给出 lim_{p→∞} 2U(Gp)/p = μT(safe) > 0.
因此存在有限 P0，使得所有符合条件的 p>P0 都满足 U(Gp)>0。
证毕。
进一步可计算精确的渐近系数。定义 q = Σ_{m∈Z} a_{m7}, 其中 a0=7/8, am = −sin(πm/8)/(πm) (m≠0).
两条关系分别涉及奇数和偶数坐标，因此 μT(safe) = q^2.
计算得到 q = 0.392694431212, q^2 = 0.154208916305, 从而 # empty cosets / p → q^2/28 = 0.005507461297. 这与实验斜率相符。
重要限制：这个证明只适用于指定的 28 阶子群类，并未证明任意 14-set 的统一下界。
3. 常规概率工具为什么不足
Bounded differences
PROOF
替换一个速度最多影响 H 个 cells，因此每个差分界可取 H。
对固定数量的速度，Pr(U−EU ≤ −a) ≲ exp(−2a^2/(kH^2)).
取 a=Θ(p)，而 H=Θ(p)，指数仅为 Θ(1)。

=== END chunk 3 (need to continue) ===
=== CONTINUATION (chunk 4) ===

不足以压过数量随 p 增长的候选速度集合。
Janson
PROOF / FACT
令 Wt 为覆盖 cell t 的速度集合。
利用行列均为 H 的正则性，Σ_{t<t'} |Wt∩Wt'| = n(H choose 2).
因此平均重叠量为 H(H−1)/(n−1) = Θ(p).
直接的依赖图方法因此产生 Δ=Θ(p^2)，而 μ=Θ(p).
独立计算的检查还发现，所测素数的所有不同 cell 对都存在重叠：
p	重叠对比例
997	1.000
1009	1.000
1499	1.000
不过，这不构成对所有素数的证明。对于固定大小、不放回抽样，还必须谨慎使用相应的超几何版本，而不能直接套用独立 Bernoulli Janson。
结构性替代
IDEA
Dirichlet scaling 可以提供较小的速度代表，使短整数关系更容易出现，但仍需要证明这些关系不能消灭所有安全时间。
子群证明展示了一个更直接的办法：研究模 p 的短整数关系所决定的极限子环面，而不仅研究覆盖事件的概率依赖。
4. 最短的统一下界引理链
令 BN = {x∈T^{N−2} : ‖xj‖ > 1/N ∀j}.
引理	内容	状态
L1	网格轨道测度的 Fourier 系数为 0 或 1	PROVED
L2	任意序列可抽出极限，其测度为某个子环面的 Haar 测度	PROVED
L3	每个可容许极限子环面都与 BN 有非空相对开交集	OPEN
L4	若 L3 成立，紧性给出统一正测度下界	PROVED（条件性）
L5	将测度下界转回 U、E，得到统一 δ>0	PROVED（条件性）
这里的可容许性包括所有坐标投影非退化，以及不存在两个坐标恒等或恒为彼此相反数。
最难的是 L3。它实际上要求一种统一的环面逃逸定理（uniform toral escape theorem）。子群情形已由上面的明确安全点解决，但一般速度集合仍未解决。
5. 推广至其他 N
PROOF（条件性）
设 k=N−2，则 EN(p) = n·(n−H choose k)/(n choose k), H = ⌊(p−1)/N⌋.
当 p→∞，EN(p)/n → (1−2/N)^{N−2} > 0.
因此，只要对应维度的 L3 成立，同样的紧性证明就适用于 N=17,18,20。
OPEN：尚不能断言这些 N 的 L3 成立，更不能由 N=16 的子群定理直接推出。
可复算代码（Python）
以下使用精确整数位集计数。局部搜索每轮不需要遍历全部 14-set，且每次运行可保持在一分钟以内。

=== END chunk 4 (need to continue) ===
=== CONTINUATION (chunk 5 — first code block, verbatim from Copy button) ===

可复算代码（Python）
以下使用精确整数位集计数。局部搜索每轮不需要遍历全部 14-set，且每次运行可保持在一分钟以内。

```python
import math, random
import numpy as np
from fractions import Fraction
from sympy import primerange, primitive_root, isprime


def build(p, N):
    n, H = (p-1)//2, (p-1)//N
    masks = [0] * (n+1)
    for v in range(1, n+1):
        b = 0
        for t in range(1, n+1):
            r = v*t % p
            if min(r, p-r) <= H:
                b |= 1 << (t-1)
        masks[v] = b
    return n, H, masks

def uncovered(S, masks, n):
    cover = 0
    for v in S:
        cover |= masks[v]
    return n - cover.bit_count()

def search(p, N, k, runs, seed, steps=45):
    n, H, masks = build(p, N)
    rng = random.Random(seed)
    best = (n, None)
    E = Fraction(n*math.comb(n-H,k), math.comb(n,k))

    for _ in range(runs):
        S = rng.sample(range(1,n+1), k)
        u = uncovered(S,masks,n)

        for _ in range(steps):
            chosen = set(S)
            proposal = None
            next_u = u

            for i in range(k):
                base = 0
                for j,v in enumerate(S):
                    if j != i:
                        base |= masks[v]

                for v in range(1,n+1):
                    if v in chosen:
                        continue
                    candidate = n-(base | masks[v]).bit_count()
                    if candidate < next_u:
                        next_u = candidate
                        proposal = (i,v)

            if proposal is None:
                break

            S[proposal[0]] = proposal[1]
            u = next_u

        if u < best[0]:
            best = (u,sorted(S))

        if u == 0:
            break

    assert uncovered(best[1],masks,n) == best[0]
    return E,best

records = []
for p in [1499,1999,2503,3001]:
    assert isprime(p)
    E,a = search(p,16,14,12,14+p,22)
    _,b = search(p,16,14,50,440+p,24)
    best = min((a,b),key=lambda z:z[0])
    d = best[0]/float(E)
    records.append((p,d))
    print("N16",p,float(E),best[0],d,best[1])

print("linear fit",np.polyfit(
    [r[0] for r in records],
    [r[1] for r in records],1
))

for p in [997,1009]:
    assert isprime(p)
    E,best = search(p,20,18,120,2026+p)
    print("N20",p,float(E),best[0],
          best[0]/float(E),best[1])
```

=== END chunk 5 ===
=== CONTINUATION (chunk 6 — second code block, verbatim from Copy button) ===

There are 2 code blocks visible in the thread at this scroll position; the second one (below the first) is this subgroup enumeration / asymptotics code:

```python
import math
import numpy as np
from sympy import primerange, primitive_root

rows = []

for p in primerange(29,20001):
    if p % 28 != 1:
        continue

    g = int(primitive_root(p))
    a = pow(g,(p-1)//28,p)

    S = sorted({
        min(pow(a,j,p),p-pow(a,j,p))
        for j in range(28)
    })

    assert len(S) == 14
    n,H = (p-1)//2,(p-1)//16

    cover = 0
    for v in S:
        for t in range(1,n+1):
            r = v*t % p
            if min(r,p-r) <= H:
                cover |= 1 << (t-1)

    U = n-cover.bit_count()
    assert U % 14 == 0
    rows.append((p,U//14))

print("count",len(rows))
print("zero",[p for p,e in rows if e==0])
print("last",rows[-1])

slope,intercept = np.polyfit(
    [p for p,e in rows],
    [e for p,e in rows],1
)
print("fit",slope,intercept)

rate = sum(e for p,e in rows) / sum(
    (p-1)/28 for p,e in rows
)
print("observed empty rate",rate)

q = (7/8)**7
for m in range(1,1001):
    a = -math.sin(math.pi*m/8)/(math.pi*m)
    q += 2*a**7

print("q",q)
print("q_squared",q*q)
print("predicted slope",q*q/28)
print("binomial", (7/8)**14)
print("Poisson",math.exp(-3.5))
```

=== END chunk 6 ===

Now need to confirm what follows the second code block and where the assistant reply ends. Checking whether anything comes after it in this same assistant turn.=== CONTINUATION (chunk 7 — section label, third code block verbatim from Copy, and the reply's closing) ===

子群完整枚举及理论常数：
(second code block captured verbatim in chunk 6)

重叠检查代码：
```python
for p in [997,1009,1499]:
    n,H = (p-1)//2,(p-1)//16
    W = []
    for t in range(1,n+1):
        b = 0
        for v in range(1,n+1):
            r = v*t % p
            if min(r,p-r) <= H:
                b |= 1 << (v-1)
        W.append(b)

    pairs = overlaps = 0
    for i in range(n):
        for j in range(i):
            pairs += 1
            overlaps += bool(W[i] & W[j])

    print(p,overlaps/pairs)
```

最不确定的一步（Least-sure step）：
能否将子群证明中的“明确可构造安全点”推广成对所有可容许子环面成立的统一逃逸引理。
最终判断：
Round 14 尚未证明普遍的 δ(p) ≥ δ > 0，但得到了一个更强的局部结果：28 阶子群的空陪集具有严格正的渐近密度，因此这整个子群类别在充分大的素数上不可能提供 14-cover。这一结果不依赖 Poisson 猜想，也不需要先解决一般的 16-runner 问题。

=== END OF ASSISTANT REPLY ===

Verification: the line "ChatGPT can make mistakes. Check important info." shown immediately after is ChatGPT's standard site-level disclaimer chrome (not part of the assistant's reply). The reply ends at the "最终判断" paragraph above.

CAPTURE NOTES:
- The per-message "Copy message" button at y=826 (1-105) copied the adjacent USER message ("Please give the final answer now, ANSWER BLOCK first..."), NOT the assistant reply. So the reply could not be captured by that button.
- The three inline code blocks inside the assistant reply each have their own "Copy" button; all three were captured verbatim from those Copy buttons (chunks 5, 6, 7).
- The surrounding prose (ANSWER BLOCK header, Q1–Q5, sections 1–5, proofs, tables, closing paragraphs) was captured verbatim via overlapping extract_content(region=near_viewport) anchored by find_text, with find_text used to walk from one distinctive phrase to the next (16 overlapping anchored reads covering ANSWER BLOCK → Q5 → N=20 table → Poisson proof → Fourier resultant proof → Bounded differences/Janson → lemma table → N-generalization → code → overlaps → 最终判断).
- The ChatGPT page re-renders math with duplicated "flat + subscript" runs (e.g. "p p D(p)≤ D(p)≤"). Those duplicated tokens are faithfully preserved here as rendered; the code blocks themselves (from Copy) are clean.

--- end verbatim ---
END LETTER
