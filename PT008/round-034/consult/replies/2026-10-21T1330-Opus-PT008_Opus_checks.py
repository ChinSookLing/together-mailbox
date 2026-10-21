# PT008_Opus_checks.py — PT-008 · Opus 席 · 精确有理验证脚本（2026-10-21）
# 只用 Python 标准库；全部判定用 fractions.Fraction 精确比较，不用浮点判等。
# 用法: python3 PT008_Opus_checks.py            # 全部
#       python3 PT008_Opus_checks.py s1 s9      # 指定小节
from fractions import Fraction as F
from math import floor, ceil, gcd
from functools import reduce
import itertools, random, sys, time

# ================= 基本工具 =================
def nint(x):                       # 最近整数（坏判定时 |x-q|<δ≤1/2，唯一）
    return floor(x + F(1, 2))

def dist(x):                       # ‖x‖：到最近整数的距离
    return abs(x - nint(x))

def is_safe(V, t, d):
    return all(dist(v * t) >= d for v in V)

def tau(V, d, max_steps=10**6):
    """最左安全时间 τ(V,δ) = min{t>0 : ‖v t‖ ≥ δ ∀v}，跳跃迭代（jump iteration）。
    返回 (t, path)；path 每步记 (速度序号从1起, q)。终点 t=(q+δ)/v_i 是一个地标（landmark）。"""
    t, path = F(0), []
    while True:
        best = None
        for i, v in enumerate(V):
            x = v * t
            q = nint(x)
            if abs(x - q) < d:                 # 跑者 i 在坏区 ((q-δ)/v, (q+δ)/v)
                e = (q + d) / v                # 坏区右端 = 地标
                if best is None or e > best[0]:
                    best = (e, i + 1, q)
        if best is None:
            return t, path
        t = best[0]
        path.append(best[1:])
        if len(path) > max_steps:
            return None, path

def bad_intervals(V, d, lo, hi):
    out = []
    for v in V:
        for q in range(floor(v * lo - d), ceil(v * hi + d) + 1):
            a, b = (q - d) / v, (q + d) / v
            if b > lo and a < hi:
                out.append((a, b))
    return out

def good_components(V, d, lo, hi):
    """[lo,hi] 内安全集的闭连通分量——与 tau 独立的扫描法实现，用作交叉检验。"""
    merged = []
    for a, b in sorted(bad_intervals(V, d, lo, hi)):
        if merged and a < merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    comps, cur = [], lo
    for a, b in merged:
        if a >= cur:
            comps.append((cur, a))
        cur = max(cur, b)
        if cur > hi:
            break
    if cur <= hi:
        comps.append((cur, hi))
    return comps

def tight_points(V, d):
    """整数速度紧实例：[0,1) 内全部孤立安全点，及每点的上紧(≡+δ)/下紧(≡−δ)速度。"""
    out = []
    for c0, c1 in good_components(V, d, F(0), F(1)):
        assert c0 == c1, "不是紧实例"
        t = c0
        up = [int(v) for v in V if v * t - nint(v * t) == d]
        dn = [int(v) for v in V if v * t - nint(v * t) == -d]
        out.append((t, up, dn))
    return out

def coprime_tuples(k, N):
    for V in itertools.combinations(range(1, N + 1), k):
        if reduce(gcd, V) == 1:
            yield V

# ================= S1 征询稿内部测试输入 =================
def s1():
    print("== S1 征询稿内部测试输入（精确）==")
    tests = [((1, 2, 3), F(1, 4)), ((1, 2, 3), F(1, 5)), ((1, 3, 4), F(1, 4)), ((1, 3, 4), F(1, 5)),
             ((1, 2, 3, F(41, 10)), F(1, 5)), ((1, F(19, 10), 2, 3), F(1, 5))]
    for V, d in tests:
        V = tuple(F(v) for v in V)
        t, path = tau(V, d)
        sweep = good_components(V, d, F(0), t + 2)[0][0]
        print(f"V={tuple(str(v) for v in V)} δ={d}: τ={t} 路径={path} "
              f"距离={[str(dist(v * t)) for v in V]} 扫描法一致={sweep == t}")
    V = (F(1), F(19, 10), F(2), F(3))
    print("核对 (1,19/10,2,3): t=3/5 各距离", [str(dist(v * F(3, 5))) for v in V],
          "; t=1/4 安全:", is_safe(V, F(1, 4), F(1, 5)))
    V = (F(1), F(2), F(3), F(41, 10))
    print("核对 (1,2,3,41/10): t=2/5 安全:", is_safe(V, F(2, 5), F(1, 5)))

# ================= S2 NO-CONT′：极值点单侧扰动 =================
def s2():
    print("== S2 NO-CONT′：极值点 V*=(1..n-1) 的单侧扰动（ε=1e-6）==")
    eps = F(1, 10**6)
    for k in list(range(2, 11)) + [20, 46]:
        Vs = [F(i) for i in range(1, k + 1)]; d = F(1, k + 1)
        t0, _ = tau(Vs, d)
        a = next(i for i, v in enumerate(Vs) if v * t0 - nint(v * t0) == d)
        b = next(i for i, v in enumerate(Vs) if v * t0 - nint(v * t0) == -d)
        W = list(Vs); W[a] -= eps
        near = good_components(W, d, t0 - d / 4, t0 + d / 4)
        tm, _ = tau(W, d)
        U = list(Vs); U[a] += eps
        tp, _ = tau(U, d)
        print(f"n={k + 1}: τ(V*)={t0}，上紧 v{a + 1}、下紧 v{b + 1} | v{a + 1}−ε：t0±δ/4 内安全分量={len(near)}，"
              f"τ={tm} | v{a + 1}+ε：τ={float(tp):.10f}")

# ================= S3 紧实例普查 =================
def s3():
    print("== S3 紧实例普查：门槛 1/n 下安全集全为孤立点（整数速度，gcd=1）==")
    for k, N in [(2, 60), (3, 40), (4, 34), (5, 22), (6, 17), (7, 15), (8, 13)]:
        d = F(1, k + 1); tight = []; tot = 0; t0 = time.time()
        for V in coprime_tuples(k, N):
            tot += 1
            comps = good_components([F(v) for v in V], d, F(0), F(1))
            if not comps:
                print("!!! 空安全集（若出现须立即复核）:", V); continue
            if all(c[0] == c[1] for c in comps):
                tight.append(V)
        print(f"n={k + 1}，速度≤{N}：检查 {tot} 组，紧实例 {len(tight)} 组：{tight}  ({time.time() - t0:.1f}s)")

# ================= S4 穷举 τ =================
def s4():
    print("== S4 穷举：整数速度（gcd=1）在门槛 1/n 的最左安全时间 τ ==")
    for k, N in [(2, 60), (3, 40), (4, 34), (5, 22), (6, 17), (7, 15), (8, 13), (9, 12), (10, 12)]:
        d = F(1, k + 1); worst = (F(0), None); ms = 0; tot = 0; t0 = time.time()
        for V in coprime_tuples(k, N):
            Vf = [F(v) for v in V]
            t, path = tau(Vf, d)
            assert t is not None and is_safe(Vf, t, d)
            tot += 1
            if t * V[0] > worst[0]:
                worst = (t * V[0], V)
            ms = max(ms, len(path))
        print(f"n={k + 1}，速度≤{N}：{tot} 组全部找到；max τ·v_min={worst[0]}≈{float(worst[0]):.3f} 于 {worst[1]}；"
              f"最多跳跃 {ms} 步  ({time.time() - t0:.1f}s)")

# ================= S5 TF-½ 与精确门槛随机检验 =================
def s5(trials=400):
    print("== S5 TF-½：τ_{1/(2n)} ≤ (n+1)/(2n)·Σ1/v_i，随机有理速度 n=2..47 ==")
    random.seed(20261021); worst = 0; t0 = time.time(); ms = 0
    for _ in range(trials):
        k = random.randint(1, 46); n = k + 1
        spread = random.choice([2, 10, 100, 1000])
        V = [F(random.randint(1000, 1000 * spread), random.choice([1000, 997, 1024])) for _ in range(k)]
        d = F(1, 2 * n)
        t, path = tau(V, d)
        bound = F(n + 1, 2 * n) * sum(1 / v for v in V)
        assert t is not None and is_safe(V, t, d) and t <= bound
        assert len(path) <= bound * sum(V) + k
        worst = max(worst, float(t / bound)); ms = max(ms, len(path))
    print(f"{trials} 组全部满足；max τ/界 = {worst:.4f}；最多跳跃 {ms} 步  ({time.time() - t0:.1f}s)")
    print("== S5b 精确门槛 1/n：随机有理速度 n=2..47（有限检验，非证明）==")
    random.seed(47); t0 = time.time(); cnt = 0; maxr = 0; ms = 0
    for _ in range(trials // 2):
        k = random.randint(1, 46); n = k + 1
        V = [F(random.randint(1000, 10000), 1000) for _ in range(k)]
        t, path = tau(V, F(1, n))
        assert t is not None and is_safe(V, t, F(1, n))
        cnt += 1; maxr = max(maxr, float(t * min(V))); ms = max(ms, len(path))
    print(f"{cnt} 组全部找到；max τ·v_min = {maxr:.4f}；最多跳跃 {ms} 步  ({time.time() - t0:.1f}s)")

# ================= S6 极值射线附近的显式双分支公式 F_loc =================
def F_loc(v):
    """v ≈ (1,2,…,n−1)。分支线 v_{n−1} = (n−1)·v_1。"""
    k = len(v); n = k + 1
    if v[-1] <= k * v[0]:
        return 1 / (n * v[0])                 # 地标 (0 + 1/n)/v_1
    return F(k * k) / (n * v[-1])             # 地标 (n−2 + 1/n)/v_{n−1}

def s6(trials=300):
    print("== S6 F_loc：盒子 |v_i − i| ≤ 1/(2n)，n=2..47 ==")
    random.seed(6); fails = 0; tot = 0; br = [0, 0]; t0 = time.time()
    for n in [2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 20, 30, 40, 47]:
        k = n - 1; eps = F(1, 2 * n)
        for _ in range(trials):
            v = [i + eps * F(random.randint(-10**6, 10**6), 10**6) for i in range(1, k + 1)]
            br[0 if v[-1] <= k * v[0] else 1] += 1
            tot += 1
            fails += not is_safe(v, F_loc(v), F(1, n))
        if n <= 12:                             # 盒子的全部顶点
            for signs in itertools.product((-1, 1), repeat=k):
                v = [i + s * eps for i, s in zip(range(1, k + 1), signs)]
                tot += 1
                fails += not is_safe(v, F_loc(v), F(1, n))
    print(f"随机点+顶点共 {tot} 个：失败 {fails}；随机点分支使用 {br}  ({time.time() - t0:.1f}s)")
    for n in [5, 10, 47]:
        k = n - 1
        for mult in [2, 4, 8]:
            eps = F(mult, 2 * n); f = 0
            for _ in range(300):
                v = [i + eps * F(random.randint(-10**6, 10**6), 10**6) for i in range(1, k + 1)]
                f += not is_safe(v, F_loc(v), F(1, n))
            print(f"  放大检验 n={n}，半径 {mult}/(2n)：300 次失败 {f}")

# ================= S7 尺度阶梯（TF-½ 均匀复杂度）=================
def scale_ladder(V):
    V = sorted(V); k = len(V); n = k + 1
    d = F(1, 2 * n); H = 4 * k; G = 28 * k**3
    clusters = [[V[0]]]
    for v in V[1:]:
        if v >= G * clusters[-1][-1]:
            clusters.append([v])
        else:
            clusters[-1].append(v)
    x, y = F(0), None; log = []
    for C in clusters:
        Vc = C[0]; R = C[-1] / Vc; X = F(H) / Vc
        assert y is None or y - x >= X, "窗口放不下（引理失效）"
        comps = good_components(C, d, x, x + X)
        meas = sum(c[1] - c[0] for c in comps)
        p = max(comps, key=lambda c: (c[1] - c[0], -c[0]))
        assert meas > 1 / Vc, "测度下界失效"
        assert p[1] - p[0] > 1 / (Vc * k * (4 * k * R + 3)), "最长分量下界失效"
        x, y = p
        log.append((len(C), len(comps)))
    assert is_safe(V, x, d)
    return x, log

def s7(trials=200):
    print("== S7 尺度阶梯（TF-½ 的均匀复杂度构造）==")
    random.seed(7); t0 = time.time(); multi = 0; maxc = 0
    for _ in range(trials):
        k = random.randint(1, 7); G = 28 * k**3
        sizes = []; rest = k
        while rest:
            s = random.randint(1, rest); sizes.append(s); rest -= s
        V = []; base = F(random.randint(1, 50), random.randint(1, 50))
        for s in sizes:
            sp = random.choice([1, 3, 20])
            cl = sorted(base * F(random.randint(1000, 1000 * sp), 1000) for _ in range(s))
            V += cl
            base = cl[-1] * G * random.choice([1, 2, 10, 1000])
        t, log = scale_ladder(V)
        multi += len(log) > 1; maxc = max(maxc, len(log))
    for _ in range(40):                          # 单簇、较多速度
        k = random.randint(8, 20)
        scale_ladder([F(random.randint(1000, 5000), 1000) for _ in range(k)])
    print(f"{trials} 组随机分簇（多簇 {multi} 组，最多 {maxc} 簇）+ 40 组单簇 k≤20：全部安全，所有中间下界成立  "
          f"({time.time() - t0:.1f}s)")

# ================= S8 紧实例的孤立点与扰动 =================
def s8():
    print("== S8 紧实例在 [0,1) 内的孤立安全点（上紧/下紧速度）与单侧扰动 ==")
    for V in [(1, 2), (1, 2, 3), (1, 2, 3, 4), (1, 3, 4, 7), (1, 2, 3, 4, 5), (1, 3, 4, 5, 9),
              (1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 7, 12), (1, 4, 5, 6, 7, 11, 13)]:
        n = len(V) + 1; d = F(1, n); Vf = [F(v) for v in V]
        pts = tight_points(Vf, d)
        print(f"V={V}（n={n}）: " + "; ".join(f"t={t} 上紧{up} 下紧{dn}" for t, up, dn in pts))
        t0, _ = tau(Vf, d)
        a = next(i for i, v in enumerate(Vf) if v * t0 - nint(v * t0) == d)
        out = []
        for sgn in (-1, 1):
            W = list(Vf); W[a] += sgn * F(1, 10**6)
            out.append(f"v{a + 1}{'−' if sgn < 0 else '+'}ε → τ≈{float(tau(W, d)[0]):.7f}")
        print("    " + "；".join(out))

# ================= S9 (1,3,4) 门槛 1/5 与 u=7 =================
def fail_window(L, R, d, q):
    """单分量 [L,R] 在第 q 圈的完整失败窗口 ((q−δ)/L, (q+δ)/R)（征询稿公式）。"""
    return ((q - d) / L, (q + d) / R)

def s9():
    print("== S9 (1,3,4) 门槛 1/5：安全分量、u=7 处的首尾相接 ==")
    V = [F(1), F(3), F(4)]; d = F(1, 5)
    comps = good_components(V, d, F(0), F(1))
    print("(1,3,4) 在 [0,1] 的安全分量:", [(str(a), str(b)) for a, b in comps])
    K1, K2 = comps[1], comps[2]
    w1, w2 = fail_window(*K1, d, 3), fail_window(*K2, d, 4)
    print(f"  K1={tuple(map(str, K1))} 的失败窗口(q=3)=({w1[0]}, {w1[1]})；"
          f"K2={tuple(map(str, K2))} 的失败窗口(q=4)=({w2[0]}, {w2[1]})")
    for u in [F(7), F(7) - F(1, 1000), F(7) + F(1, 1000)]:
        cs = good_components(V + [u], d, F(0), F(1))
        print(f"  加入 u={u}：[0,1] 安全分量 {[(str(a), str(b)) for a, b in cs]}")

# ================= S10 紧实例附近的通用双分支公式 LOC2 =================
def loc2_builder(Vstar):
    n = len(Vstar) + 1; d = F(1, n)
    pts = tight_points([F(v) for v in Vstar], d)
    t0, (a,), (b,) = next((t, up, dn) for t, up, dn in pts if len(up) == 1 and len(dn) == 1 and t <= F(1, 2))
    ia, ib = Vstar.index(a), Vstar.index(b)
    qa, qb = floor(a * t0), floor(b * (1 - t0))
    def Floc(v):
        if v[ib] / b <= v[ia] / a:            # 相对扰动 ρ_b ≤ ρ_a：取 t0 一侧
            return (qa + d) / v[ia]
        return (qb + d) / v[ib]               # 否则取镜像点 1−t0 一侧
    return Floc, (t0, a, b)

def s10(trials=2000):
    print("== S10 LOC2：每个紧实例附近的双分支地标公式（相对扰动 ≤ 1e-3）==")
    random.seed(2)
    for Vstar in [(1, 2, 3), (1, 2, 3, 4), (1, 3, 4, 7), (1, 2, 3, 4, 5), (1, 3, 4, 5, 9),
                  (1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 7, 12), (1, 4, 5, 6, 7, 11, 13)]:
        n = len(Vstar) + 1; d = F(1, n)
        Floc, (t0, a, b) = loc2_builder(Vstar)
        fails = 0
        for _ in range(trials):
            v = [F(x) * (1 + F(random.randint(-10**6, 10**6), 10**9)) for x in Vstar]
            fails += not is_safe(v, Floc(v), d)
        print(f"V*={Vstar}: 用孤立点 t0={t0}（上紧 {a}，下紧 {b}）；{trials} 次：失败 {fails}")

if __name__ == "__main__":
    table = dict(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10)
    for s in (sys.argv[1:] or list(table)):
        table[s]()