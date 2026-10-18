# PT-008 · Round 007 · author: Puck (Grok Bot courier) · 2026-10-18 SGT (UTC+8)
# Puck addition (for the chair's independent check; NOT a PROVED claim): can the gap U = {1<x<7/3, y>8-x}
# left by N1, R1, S6-A and Argon B.2 be closed by three more short lemmas?  Exact Fractions.
#   R2: t=3/(b+c) works if 4<=x+y<=12 and (3x<=y<=11x or y<=7x/5)  (iff, once x+y>12/5; extra small branch 12/7<=x+y<=12/5)
#   P1: y>=3, x<3, (1+y)(3-x)>=4x  ->  k=ceil((a+c)/(4a)), t=k/(a+c)
#   E : 5/3<x<7/3, y>=4x/(3x-5)-x  ->  k=ceil(5(b+c)/(4b)), t=k/(b+c)   (Argon B.2 with m=1)
# Candidate piecewise rule F4 (first matching case):
#   1 c<=3a: 1/(a+c) | 2 b>=7a/3: Argon B.2 | 3 c<=8a-b: (3c>=5b ? 2/(b+c) : 3/(a+c))
#   4 b<=2a: (b+c<=12a ? 3/(b+c) : ceil((a+c)/4a)/(a+c)) | 5 else (2a<b<7a/3, c>8a-b): ceil(5(b+c)/4b)/(b+c)
from common_r007 import *
random.seed(718)
def F4(a, b, c):
    a, b, c = F(a), F(b), F(c)
    if c <= 3 * a: return 1, t_N1(a, b, c)
    if 3 * b >= 7 * a: return 2, t_AB(a, b, c)
    if c <= 8 * a - b: return (3, t_R1(a, b, c)) if 3 * c >= 5 * b else (3.5, t_S6(a, b, c))
    if b <= 2 * a: return (4, t_R2(a, b, c)) if b + c <= 12 * a else (4.5, t_P1(a, b, c))
    return 5, t_AB1(a, b, c)
def region_ok(case, x, y):   # the case's region condition (used in its proof) must hold
    return {1: in_N1, 2: in_AB, 3: in_R1, 3.5: in_S6, 4: in_R2, 4.5: in_P1, 5: in_E}[case](x, y)

print("== Lemma R2: t=3/(b+c), exact region ==")
n = inbad = outok = outok_big = 0
for i in range(100000):
    x = rq(1, 12); y = x + rq(F(1, 10**6), 30); V = (F(1), x, y); n += 1; w = ok(V, t_R2(*V)); r = in_R2(x, y)
    if r and not w: inbad += 1
    if w and not r:
        outok += 1
        if x + y > F(12, 5): outok_big += 1
print("  random (1,x,y): %d | in R2 but formula fails: %d | formula works outside R2: %d (of which with x+y>12/5: %d; the rest is the at in [5/4,7/4] branch, not needed)" % (n, inbad, outok, outok_big))
print("== Lemma P1: k=ceil((a+c)/4a), t=k/(a+c) on {y>=3, x<3, (1+y)(3-x)>=4x} ==")
n = bad = lem = 0
for i in range(100000):
    x = rq(1, 3 - F(1, 10**4)); lo = max(F(3), 4 * x / (3 - x) - 1, x + F(1, 10**6))
    y = lo + [F(0), rq(0, 2), rq(0, 10**5)][i % 3]; V = (F(1), x, y); n += 1; t = t_P1(*V)
    if not ok(V, t): bad += 1
    if not (Q <= t <= F(1, 2) and Q < x * t <= 3 * Q): lem += 1
print("  random points (1/3 exactly on the curve): %d, failures: %d, violations of 1/4<=at<=1/2, 1/4<bt<=3/4: %d" % (n, bad, lem))
print("== Lemma E: Argon formula with m=1 on {5/3<x<7/3, y>=4x/(3x-5)-x}: see chk_argon_r007.py (60000 pts, 0 failures) ==")

print("\n== Coverage algebra: every 1<x<y lies in one case region (random + boundaries) ==")
n = bad = notreg = 0; hist = {}
for i in range(300000):
    x = rq(1, [3, 10, 1000][i % 3]); y = x + rq(F(1, 10**8), [3, 30, 10**5][(i // 3) % 3]); V = (F(1), x, y); n += 1
    case, t = F4(*V); hist[case] = hist.get(case, 0) + 1
    if not region_ok(case, x, y): notreg += 1
    if not ok(V, t): bad += 1
print("  random rational (1,x,y): %d, F4 failures: %d, case chosen outside its proven region: %d, case counts: %s" % (n, bad, notreg, dict(sorted(hist.items()))))
# exact boundary curves and corners
pts = set(); e = F(1, 10**9)
xs = [F(1) + e, F(9, 5), F(15, 11), F(5, 3), F(5, 3) + e, F(19, 10), F(2) - e, F(2), F(2) + e, F(21, 10), F(7, 3) - e, F(7, 3), F(7, 3) + e, F(3), F(4), F(10)]
for x in xs:
    curves = [x + e, F(3), F(3) + e, F(5, 3) * x, F(5, 3) * x - e, 8 - x, 8 - x + e, 12 - x, 12 - x + e, 12 * x / 5 - 1, 12 * x / 7 - 1, F(11), F(11) + e, 3 * x, 11 * x, 10**9]
    if x < 3: curves += [4 * x / (3 - x) - 1, 4 * x / (3 - x) - 1 - e]
    if x > F(5, 3): curves += [4 * x / (3 * x - 5) - x, 4 * x / (3 * x - 5) - x - e]
    for y in curves:
        if y > x: pts.add((x, y))
bb = [(x, y) for x, y in pts if not ok((F(1), x, y), F4(1, x, y)[1])]
print("  exact boundary/corner points: %d, F4 failures: %d %s" % (len(pts), len(bb), bb[:3]))
n = bad = 0; minc = None
for a in range(1, 121):
    for b in range(a + 1, 121):
        for c in range(b + 1, 121):
            n += 1; case, t = F4(a, b, c)
            if not ok((a, b, c), t): bad += 1
print("  ALL integer triples 0<a<b<c<=120: %d, F4 failures: %d" % (n, bad))
for V in [(1, 2, 3), (1, 2, 10), (5, 6, 56), (7, 13, 44), (10, 22, 33), (2, 3, 7), (1, 2, 3 * 40)]:
    case, t = F4(*V); print("  example %s: case %s, t=%s, g=%s" % (V, case, t, g(V, t)))
