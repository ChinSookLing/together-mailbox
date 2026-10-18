# PT-008 · Round 007 · author: Puck (Grok Bot courier) · 2026-10-18 SGT (UTC+8)
# Shared exact helpers for the R007 checks (Fractions only). Same definitions as round-006/puck-check/common_r006.py:
# speeds 0<a<b<c (real; here exact rationals), ||u|| = distance to nearest integer, success iff min(||at||,||bt||,||ct||) >= 1/4.
# Ratios x=b/a, y=c/a (1<x<y). Times are given for general a (formulas are scale-free: t(a,b,c) = t(1,x,y)/a).
from fractions import Fraction as F
from math import floor, ceil
import random
Q = F(1, 4)
def nd(u):
    r = u - floor(u); return min(r, 1 - r)
def g(V, t): return min(nd(v * t) for v in V)
def ok(V, t): return g(V, t) >= Q
def fl(q): return floor(q)            # exact floor of a Fraction
def ce(q): return -floor(-q)          # exact ceil of a Fraction

# ---- the time formulas named in the R007 pack / replies (a,b,c exact) ----
def t_N1(a, b, c):  return F(1) / (a + c)                     # N1 (Qwen) / R006 D.1: c <= 3a
def t_R1(a, b, c):  return F(2) / (b + c)                     # R1: 5b/3 <= c <= 8a-b
def t_S6(a, b, c):  return F(3) / (a + c)                     # S6-A: 3a<=c<=11a, 5(a+c)/12 <= b <= 7(a+c)/12
def t_AB(a, b, c):                                            # Argon R007 B.2: m=floor(x/2), k=ceil((m+1/4)(b+c)/b)
    x = F(b) / a; m = fl(x / 2); k = ce((m + Q) * (b + c) / b); return F(k) / (b + c)
def t_N2(a, b, c):  return F(2) / (a + b)                     # Qwen N2: t=2/(a+b)
def t_AB1(a, b, c):                                           # Argon formula with m forced to 1 (Puck extension E)
    k = ce((1 + Q) * (b + c) / b); return F(k) / (b + c)
def t_P1(a, b, c):                                            # Qwen B.2 rule k=ceil((a+c)/(4a)), t=k/(a+c) (Puck region P1)
    k = ce(F(a + c) / (4 * a)); return F(k) / (a + c)
def t_R2(a, b, c):  return F(3) / (b + c)                     # Puck region R2: t=3/(b+c)

# ---- region predicates in ratio coordinates (x=b/a, y=c/a), exact ----
def in_N1(x, y):  return y <= 3
def in_R1(x, y):  return F(5, 3) * x <= y <= 8 - x
def in_R1_typo(x, y): return F(5, 3) * x <= y <= 8 - x / 3          # as written in Argon A and Qwen A.2 header
def in_S6(x, y):  return 3 <= y <= 11 and F(5, 12) * (1 + y) <= x <= F(7, 12) * (1 + y)
def in_AB(x, y):  return x >= F(7, 3)
def in_E(x, y):   return F(5, 3) < x < F(7, 3) and y >= 4 * x / (3 * x - 5) - x
def in_P1(x, y):  return y >= 3 and x < 3 and (1 + y) * (3 - x) >= 4 * x
def in_R2(x, y):  return 4 <= x + y <= 12 and (3 * x <= y <= 11 * x or y <= F(7, 5) * x)
def in_U(x, y):   return 1 < x < F(7, 3) and y > 8 - x                # Puck: uncovered by N1,R1,S6-A,AB

def rq(lo, hi, den=10**6):
    """random exact rational in [lo,hi]"""
    lo, hi = F(lo), F(hi); return lo + (hi - lo) * F(random.randint(0, den), den)
def rand_xy(xlo, xhi, ylo_fn, yhi_fn, den=10**6):
    x = rq(xlo, xhi, den); lo = max(F(ylo_fn(x)), x); hi = F(yhi_fn(x))
    if hi <= lo: return None
    y = rq(lo, hi, den)
    if y <= x: return None
    return x, y
