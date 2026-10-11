BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 18:58 +08
RE: 猜公式 Round 16 (packet d712a00), send text r16_send_full.txt or r16_send_short.txt
SEAT: gpt
MODEL: GPT-6 Thinking High (4m33s)
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ac97e4e-95c0-83ec-bfde-afaf19d7ade8

--- reply verbatim ---
[GPT-6 seat chat 'PT005 - Big Picture' (reply self-labels Astra). Worked for 4m 33s, finished 18:52 +08. Read verbatim from page text in 4 anchored chunks; Copy button did not reach the agent clipboard.]

=== ANSWER BLOCK · PT005 Round 16 · Astra (finished 6:52 PM; read verbatim from chatgpt.com conversation PT005 - Big Picture, 2026-10-11) ===

ANSWER BLOCK · PT005 Round 16 · Astra
Q1 [PROOF]： 单个大速度不等式成立，且可加强为 m(K ∪ {v}) ≥ 7/8 m(K) − 7 c(K)/(64 v).
[FACT] 对 K* = {1,…,15} ∖ {6}，独立精确计算得到 m(K*) = 97/6864。其全部删一核心 K′ = K* ∖ {a}，添加任意 v > 30，均满足 m(K′ ∪ {v}) ≥ 97/6864。证明由有限有理数检查与解析不等式结合完成。
Q2 [PROOF]： 多个大速度存在递推下界，但区间数 c(K) 可能随新增速度增长，误差无法保证趋于零。因此不能直接归纳证明所有 14-sets。
Q3 [IDEA]： 全局 C-floor 尚未证明。上述特殊无限家族成立，但 m(K) ≥ 97/6864 对所有 14-sets：UNFINISHED。无条件的统一正下界亦未由本轮证明。
Q4 [PROOF，条件性]： 若 C-floor 成立，可推出 P₀ = 991¹⁴ + 1。若仅采用 L17 中依赖 F5 的弱测度下界，也能改进其截止界。两者均远高于计算目标；无条件的新截止界：UNFINISHED。
Q5 [IDEA]： 距离实用的 Terminal Formula，主要缺少两个引理：全局测度下界（Uniform Measure Floor），以及不要求全部速度同时缩小的离散转移（Partial-Compression Transfer）。

Line A · 证明与计算
1. 单个大速度的尖锐不等式
[PROOF] 令 B_v = {x ∈ [0,1) : ‖vx‖ < 1/16}.
其周期为 1/v，每周期坏区间占比 1/8。
考虑零均值周期函数 f_v(x) = 1_{B_v}(x) − 1/8.
在一个周期内，其原函数的最大值与最小值之差恰为 (1/v)·(1/8)·(7/8) = 7/(64v).
因此，对任意区间 I，
|I ∩ B_v| ≤ |I|/8 + 7/(64v).
将此应用到 K 的全部 c(K) 个安全区间，并从 m(K) 扣除坏部分：
m(K ∪ {v}) ≥ 7/8 m(K) − 7 c(K)/(64 v).
原题要求的 c(K)/(4v) 误差界因此也成立。

2. 对 K* 的完整删一核心验证
[FACT] 用下方代码精确求出所有删一核心的 m(K′)、c(K′)，以及解析下界开始保证 C-floor 的速度阈值。
独立计算结果
删除速度 a    c(K′)    对所有 v ≥ 此值，解析下界足够
1            6        13
2            6        30
3            8        20
4            8        49
5            12       41
7            16       68
8            8        25
9            10       22
10           8        34
11           12       24
12           6        19
13           14       34
14           10       92
15           12       90
[PROOF] 因此： v ≥ 92：全部这些核心均由解析下界保证。 31 ≤ v < 92：用精确有理数逐项检验。 所有检查通过；最小结果为 14867/960960，发生于删除 14、添加 56。 它超过 C-floor 候选值，差为 3/2240。 这证明了一个真正的无限子家族，而不只是有限样本。 但该证明尚未涵盖任意 13-set 核心。

3. 为什么不能直接扩大到所有小核心？
[FACT] 举例取 K′ = K* ∖ {14}，添加 v = 31。 实际测度为 m(K′ ∪ {31}) = 128197/6383520，高于候选 floor；但尖锐解析下界却是 −234493/25534080。 因此，尽管真正的安全测度足够大，区间误差界本身仍可能完全失效。
[IDEA] 必须利用区间端点与新增周期之间的算术关系，而不只是区间数量。

Line A · 多个大速度
[PROOF] 设依次添加 v_1, …, v_r，并记 K_j = K_0 ∪ {v_1, …, v_j}.
反复应用单速度不等式得到
m(K_r) ≥ (7/8)^r m(K_0) − (7/64) · Σ_{j=1}^r (7/8)^{r−j} · c(K_{j−1}) / v_j.
同时有 c(K_j) ≤ c(K_0) + Σ_{i=1}^j v_i.
问题在于：当多个大速度处于相近尺度时，c(K_{j−1}) / v_j 未必变小。 这正是简单归纳法失效的位置。

Line B · 一个更直接的离散截止界
4. 不用把全部速度缩到固定常数
[PROOF] 假设已证明存在统一常数 m_0 > 0，使所有 14-sets 都满足 m(K) ≥ m_0.
任意安全集合的区间数满足 c(K) ≤ Σ_{k∈K} k，
∑_{k∈K} k，因为每个单速度的安全集合在单位圆上有至多 k 个区间，取交集后新增区间端点只能来自这些区间边界。
对于素数 p，取整数 Q 满足 Q^14 < p。 应用鸽巢原理于各速度模 p 的同时倍乘，可找到非零乘数 u，使缩放后的每个速度代表元都满足 k_i < p/Q。 所以 c(K) < 14p/Q。 每个长度为 L 的安全区间至少贡献 pL − 1 个网格点的下界。结合对称性， 2D(p) ≥ p m(K) − c(K)。 因此 2D(p) > p(m_0 − 14/Q)。 只需 Q > 14/m_0，右边便为正，进而 D(p) ≥ 1。 这是条件定理。它没有自行证明 m_0 > 0。

5. 两种条件性常数
[PROOF] 若 C-floor 成立，取 m_0 = 97/6864。 独立算得 97/6864 − 14/991 = 31/6802224 > 0。 所以 P₀ = 991^14 + 1 = 881112094924532670558218167227898966848962。
[FACT] 该截止数有 42 位，依然极大。 如果只使用 L17 依赖 F5 的 m_0 = 240^{−14}，相同方法取 Q = 14·240^{14}+1 得到条件性截止界 Q^14+1。其十进制长度为 483 位，而 L17 给出的原截止表…
483 位，而 L17 给出的原截止表达式具有 487 位。 此方法改善了 Dirichlet 转移常数，但没有改变决定性的指数障碍。

可复现 Python 代码
下面的代码只处理连续测度、有理数区间和符号截止界；完全不搜索任何受保护的考试素数。

Python
Run

merged = []
for a,b in bad:
    if merged and a <= merged[-1][1]:
        x,y = merged[-1]
        merged[-1] = (x,max(y,b))
    else:
        merged.append((a,b))
good = []
left = F(0)
for a,b in merged:
    if left < a:
        good.append((left,a))
    left = max(left,b)
if left < 1:
    good.append((left,F(1)))
return good

def stats(K):
    I = safe(K)
    return sum((b-a for a,b in I),F(0)), len(I)

Kstar = tuple(k for k in range(1,16) if k != 6)
floor,cstar = stats(Kstar)
assert floor == F(97,6864)

cores = []
for a in Kstar:
    K13 = tuple(k for k in Kstar if k != a)
    m,c = stats(K13)
    delta = F(7,8)*m-floor
    assert delta > 0
    ratio = F(7*c,64)/delta
    v0 = ratio.numerator//ratio.denominator+1
    cores.append((a,K13,m,c,v0))

V = max(z[4] for z in cores)
worst = None
count = 0  # Finite exact portion.
for a,K13,m,c,v0 in cores:
    for v in range(31,V):
        mv,_ = stats((*K13,v))
        count += 1
        if worst is None or mv < worst[0]:
            worst = (mv,a,v)
        assert mv >= floor

# Infinite tail via analytic inequality.
for a,K13,m,c,v0 in cores:
    assert F(7,8)*m-F(7*c,64*V) >= floor

print("Kstar:",floor,cstar)
print("thresholds:",[(a,c,v0) for a,K,m,c,v0 in cores])
print("V, tests, worst:",V,count,worst)
print("margin:",worst[0]-floor)
print("untested cores:", comb(30,13)-len(Kstar))

# Witness: analytic bound too weak at v=31.
K13 = tuple(k for k in Kstar if k != 14)
m,c = stats(K13)
print("witness analytic:", F(7,8)*m-F(7*c,64*31))
print("witness exact:", stats((*K13,31))[0])

# Conditional discrete thresholds.

5. 哪些引理才能真正收口？
引理                    状态                                    对最终截止界的作用
单个大速度区间界         PROVED                                  已建立
K* 删一核心的无限扩展    PROVED（精确计算辅助）                  只覆盖特殊家族
全局 C-floor             OPEN                                    建立固定正测度
多…
[overwrites the truncated "多…" and completes the lemmas table + closing]
多尺度相关性的统一误差界    OPEN                                  控制多个大速度
部分压缩的模网格转移       OPEN                                  避开全部速度的 Dirichlet 指数
剩余有限素数的认证检验     OPEN                                  依赖前述截止界
[FACT] 在目标量级 p ≈ 10^4，普通 14 维鸽巢法甚至无法保证 Q = 2，因为 2^14 > 10^4。
[IDEA] 因此，仅改良当前 Dirichlet 常数，不太可能把证明推进到目标量级。 真正可能改变局面的，是证明：不必同时压缩所有速度，也能控制剩余大速度在网格安全集上的覆盖行为。
最不确定的一步： 是否存在足够强、且对所有模数和速度组合统一成立的部分压缩误差界。这是本轮距离 Terminal Formula 最大的逻辑缺口。

ROUND 16 · EXACT INFINITE SUBFAMILY PROVED · UNIFORM FLOOR OPEN · CONDITIONALLY IMPROVED THRESHOLD · EXAM UNTOUCHED
ChatGPT can make mistakes. Check important info.

=== END of Round 16 reply ===

--- end verbatim ---
END LETTER
