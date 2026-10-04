"""Flag bound (Allikvere arXiv:2609.02604 v2, Thm 3.8) recomputed for n = 13, 14, 15, 16.
n = number of speeds; n+1 runners.  16 runners  <=>  n = 15.
Reproduces the paper's n=13 and n=14 constants first, then extends.
Shape factor r_n: the paper proves R_13 < 101/200, R_14 < 1/2 (Lemma 3.7).
For n >= 15 we only ESTIMATE sup R_n numerically (not a proof).
"""
from fractions import Fraction as Fr
import mpmath as mp
import numpy as np
from scipy.optimize import minimize
mp.mp.dps = 50

def consts(n):
    d = n - 1
    B = [Fr(0)] + [Fr(2 * r, (n + 1) * (n + 1 - r)) ** 2 for r in range(1, d + 1)]
    c = [B[i] - B[i - 1] for i in range(1, d + 1)]
    ratios = [c[i + 1] / c[i] for i in range(d - 1)]
    K = Fr(1)
    for x in c:
        K *= x
    A = mp.mpf(K.denominator) ** 0.5 / mp.mpf(K.numerator) ** 0.5
    return K, A, min(ratios)

def H_slice(t, n):
    q = 1 + 2 * t - t * t
    return (0.5 + (n - 1) * t * t / q) * 2 * q ** (n - 1) / t ** (2 * (n - 1) / n)

def H_general(u, n):
    u = np.clip(u, 1e-9, 1.0)
    q = 1 + 2 * u - u * u
    a = q / u ** (2 / n)
    w = u * u / q
    return (0.5 + w.sum()) * 2 * np.prod(a)   # one extra coordinate fixed at 1: w=1/2, a=2

def shape_sup(n):
    ts = np.linspace(1e-4, 0.5, 200001)
    hs = H_slice(ts, n)
    i = hs.argmin()
    Hmin_slice = hs[i]
    # general check: random starts, n-1 free coordinates
    rng = np.random.default_rng(1)
    best = np.inf
    for _ in range(60):
        x0 = rng.uniform(0.02, 1.0, n - 1)
        r = minimize(lambda u: H_general(u, n), x0, bounds=[(1e-6, 1)] * (n - 1), method="L-BFGS-B")
        best = min(best, r.fun)
    return ts[i], Hmin_slice, best, n / np.sqrt(min(Hmin_slice, best))

paper_r = {13: Fr(101, 200), 14: Fr(1, 2)}
K14_paper = Fr(2289670297, 97243124257250844122250000000000000000)

for n in (13, 14, 15, 16):
    K, A, mr = consts(n)
    t0, Hs, Hg, rsup = shape_sup(n)
    print(f"n={n} ({n+1} runners)")
    print(f"  min c_(i+1)/c_i = {mr} = {float(mr):.4f}  (>4/3: {mr > Fr(4,3)})")
    print(f"  K_n = {K}")
    if n == 14:
        print(f"  K_14 matches paper: {K == K14_paper}")
    print(f"  A_n = {mp.nstr(A, 20)}")
    print(f"  shape: slice t0={t0:.5f} Hmin_slice={Hs:.4f} Hmin_general={Hg:.4f} sup R_n ~ {rsup:.6f}")
    for label, r in (("paper r_n", paper_r.get(n)), ("numeric sup R_n", rsup)):
        if r is None:
            continue
        rr = mp.mpf(r.numerator) / r.denominator if isinstance(r, Fr) else mp.mpf(r)
        L = n * mp.log(A * rr / n)
        print(f"  bound log(v1..vn) < {mp.nstr(L, 12)}   [{label} = {float(rr):.6f}]")
    lcm = 1
    from math import lcm as _l
    for m in range(2, n + 2):
        lcm = _l(lcm, m)
    print(f"  lcm(2..{n+1}) = {lcm}, log = {mp.nstr(mp.log(lcm), 10)}")
    print()
