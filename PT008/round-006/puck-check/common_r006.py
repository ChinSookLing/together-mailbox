# PT-008 · Round 006 · author: Puck (Grok Bot courier) · 2026-10-18 13:50 SGT (UTC+8)
# sources checked: pack b10d664, Argon reply a8e3b27, Qwen reply 306c683 (branch PT-008). Exact Fractions. Suggestions only; grading is the chair's.
# PT-008 R006 Puck check - shared exact helpers (Fractions only)
from fractions import Fraction as F
from math import floor, gcd
from functools import reduce
Q = F(1, 4)
def nd(x):
    r = x - floor(x); return min(r, 1 - r)
def g(V, t): return min(nd(v * t) for v in V)
def ok(V, t): return g(V, t) >= Q
def triples(N):
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            for c in range(b + 1, N + 1):
                yield (a, b, c)
def to_int(V):
    """scale rational speeds to integers (time scales by 1/lam)"""
    L = reduce(lambda x, y: x * y // gcd(x, y), [F(v).denominator for v in V], 1)
    W = [int(F(v) * L) for v in V]; return W, L
def components(V):
    """exact success set {t in [0,1]: g>=1/4} for INTEGER speeds (period 1), as closed [L,R] list"""
    cur = [(F(0), F(1))]
    for v in V:
        iv = [(F(4 * m + 1, 4 * v), F(4 * m + 3, 4 * v)) for m in range(v)]
        new = []
        for (l1, r1) in cur:
            for (l2, r2) in iv:
                l, r = max(l1, l2), min(r1, r2)
                if l <= r: new.append((l, r))
        cur = sorted(new)
    return cur
def sum_points(V, L, R):
    """all k/(x+y), x<y in V, with L<=t<=R"""
    out = []
    for i in range(3):
        for j in range(i + 1, 3):
            s = V[i] + V[j]
            k0 = floor(L * s)
            for k in range(k0, floor(R * s) + 1):
                t = F(k, s)
                if L <= t <= R: out.append((t, V[i], V[j]))
    return out
