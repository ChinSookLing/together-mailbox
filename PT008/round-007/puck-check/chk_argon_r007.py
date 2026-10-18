# PT-008 · Round 007 · author: Puck (Grok Bot courier) · 2026-10-18 SGT (UTC+8)
# Puck check of ARGON R007 reply (PT008/round-007/2026-10-18T1446-reply-Argon-R007.md, commit 306da35). Exact Fractions.
# Suggestions only; grading is the chair's.
from common_r007 import *
random.seed(20261018)
def show(V, t): return "t=%s  ||at||,||bt||,||ct|| = %s  g=%s" % (t, ", ".join(str(nd(v * t)) for v in V), g(V, t))

print("== [B.2] Argon formula: x=b/a>=7/3, m=floor(x/2), k=ceil((m+1/4)(b+c)/b), t=k/(b+c) ==")
# (i) exhaustive integer triples c<=80 with 3b>=7a
n = bad = 0; lem = 0
for a in range(1, 81):
    for b in range(a + 1, 81):
        if 3 * b < 7 * a: continue
        for c in range(b + 1, 81):
            n += 1; V = (a, b, c); t = t_AB(*V)
            if not ok(V, t): bad += 1
            x = F(b, a); m = fl(x / 2)
            if not (m + Q <= b * t < m + 3 * Q and Q <= a * t < 3 * Q): lem += 1
print("  integer triples c<=80 with b>=7a/3: %d, failures: %d, violations of the proof's bounds (m+1/4<=bt<m+3/4, 1/4<=at<3/4): %d" % (n, bad, lem))
# (ii) random exact rationals, wide ranges
n = bad = lem = 0
for i in range(100000):
    x = rq(F(7, 3), [10, 100, 10**4][i % 3]); y = x + rq(F(1, 10**6), [1, 100, 10**6][(i // 3) % 3])
    V = (F(1), x, y); t = t_AB(*V); n += 1
    if not ok(V, t): bad += 1
    m = fl(x / 2)
    if not (m + Q <= x * t < m + 3 * Q and Q <= t < 3 * Q): lem += 1
print("  random rational (1,x,y), x in [7/3,10^4], y-x in (0,10^6]: %d, failures: %d, bound violations: %d" % (n, bad, lem))
# (iii) targeted boundaries: x=7/3 exactly, x at/just below even integers (m jumps), y-x tiny, y huge
tg = []
for x in [F(7, 3), F(7, 3) + F(1, 10**9), F(4) - F(1, 10**9), F(4), F(6) - F(1, 10**9), F(6), F(10**5), F(10**5) - F(1, 10**9)]:
    for y in [x + F(1, 10**9), x + F(1, 3), 2 * x, 3 * x, 7 * x, x + 10**9]:
        V = (F(1), x, y); t = t_AB(*V); tg.append((x, y, g(V, t)))
print("  targeted boundary points: %d, failures: %d, min g = %s" % (len(tg), sum(1 for z in tg if z[2] < Q), min(z[2] for z in tg)))
V = (F(1), F(7, 3), F(7, 3) + F(1, 10**9)); print("  example x=7/3, y=x+1e-9:", show(V, t_AB(*V)))
V = (F(3), F(7), F(100)); print("  example (3,7,100):", show(V, t_AB(*V)))
# (iv) irrational spot checks (60-digit rational approximations of sqrt)
from decimal import Decimal, getcontext
getcontext().prec = 60
def sq(n): return F(Decimal(n).sqrt())
irr = [(F(1), sq(7), sq(50)), (F(1), sq(6), F(1) + sq(30)), (sq(2), sq(11), sq(2000)), (F(1), sq(26), sq(27))]
print("  irrational spot checks:", [str(round(float(g(V, t_AB(*V))), 4)) for V in irr])

print("\n== [B.2 threshold] is x>=7/3 needed? Argon formula for 1<x<7/3 ==")
cnt = bad = 0; ex = None
for i in range(40000):
    x = rq(1, F(7, 3)); y = x + rq(F(1, 10**6), 50); V = (F(1), x, y); cnt += 1
    if not ok(V, t_AB(*V)):
        bad += 1
        if ex is None or V[2] < ex[2]: ex = V
print("  random (1,x,y), 1<x<7/3: %d, formula fails at %d" % (cnt, bad))
for V in [(F(1), F(2), F(3)), (F(2), F(3), F(8)), (F(1), F(17, 10), F(20))]:
    print("  witness %s [x<7/3]:" % (tuple(str(v) for v in V),), show(V, t_AB(*V)), "-> FAILS" if not ok(V, t_AB(*V)) else "-> ok")
V = (F(1), F(2), F(5)); print("  (1,2,5) for contrast (formula happens to work):", show(V, t_AB(*V)))

print("\n== [Puck extension E] same formula with m=1 for 5/3<x<7/3 and y >= 4x/(3x-5) - x ==")
n = bad = 0
for i in range(60000):
    x = rq(F(5, 3) + F(1, 10**6), F(7, 3) - F(1, 10**6)); lo = 4 * x / (3 * x - 5) - x
    y = max(lo, x + F(1, 10**6)) + [F(0), rq(0, 1), rq(0, 10**4)][i % 3]; V = (F(1), x, y); n += 1
    if not ok(V, t_AB1(*V)): bad += 1
print("  random points in E (incl. %d exactly on the curve y=4x/(3x-5)-x): %d, failures: %d" % (20000, n, bad))
x = F(2); y = F(6); V = (F(1), x, y); print("  on-curve example (1,2,6):", show(V, t_AB1(*V)))
x = F(2); y = F(6) - F(1, 1000); V = (F(1), x, y); print("  just below curve (1,2,5.999):", show(V, t_AB1(*V)))

print("\n== [A, R1 as written by Argon] 5x/3 <= y <= 8 - x/3 (correct pack form is y <= 8 - x) ==")
V = (F(1), F(2), F(73, 10)); x, y = V[1], V[2]
print("  (1,2,7.3): in Argon's written R1? %s; in true R1 (c<=8a-b)? %s;" % (in_R1_typo(x, y), in_R1(x, y)), show(V, t_R1(*V)))
n = bad = 0
for i in range(50000):
    p = rand_xy(1, 3, lambda x: F(5, 3) * x, lambda x: 8 - x / 3)
    if p is None: continue
    x, y = p; V = (F(1), x, y); n += 1
    if not ok(V, t_R1(*V)): bad += 1
print("  random points in the 8-x/3 version: %d, failures of t=2/(b+c): %d (all failures lie in 8-x < y <= 8-x/3)" % (n, bad))
n = bad = 0
for i in range(50000):
    p = rand_xy(1, 3, lambda x: F(5, 3) * x, lambda x: 8 - x)
    if p is None: continue
    x, y = p; V = (F(1), x, y); n += 1
    if not ok(V, t_R1(*V)): bad += 1
print("  random points in true R1 (y<=8-x): %d, failures: %d" % (n, bad))

print("\n== [B.1] S6-A with equality boundaries ==")
corners = [(F(5, 3), F(3)), (F(7, 3), F(3)), (F(5), F(11)), (F(7), F(11)), (F(2), F(19, 5)), (F(35, 12), F(4)), (F(25, 12), F(4))]
for x, y in corners:
    V = (F(1), x, y); print("  (1,%s,%s) in S6-A=%s:" % (x, y, in_S6(x, y)), show(V, t_S6(*V)))
n = bad = 0
for i in range(50000):
    p = rand_xy(F(5, 3), 7, lambda x: max(F(3), 12 * x / 7 - 1), lambda x: min(F(11), 12 * x / 5 - 1))
    if p is None: continue
    x, y = p
    if not in_S6(x, y): continue
    V = (F(1), x, y); n += 1
    if not ok(V, t_S6(*V)): bad += 1
print("  random points in S6-A: %d, failures: %d" % (n, bad))

print("\n== [Q2 hidden phase branch] t=3/(a+c) also works OUTSIDE S6-A ==")
print("  exact condition: 3<=y<=11 and 3x/(1+y) mod 1 in [1/4,3/4], i.e. x/(1+y) in [1/12,1/4] U [5/12,7/12] U [3/4,11/12]")
for V in [(F(1), F(3, 2), F(7)), (F(1), F(2), F(11)), (F(1), F(8), F(10))]:
    x, y = V[1], V[2]; print("  (1,%s,%s) in S6-A=%s:" % (x, y, in_S6(x, y)), show(V, t_S6(*V)))

print("\n== [A, S2-Nudge] y<=3: I_ac=[1/(4a),3/(4c)] nonempty and contains t=1/(a+c), which succeeds ==")
n = bad = 0
for i in range(50000):
    p = rand_xy(1, 3, lambda x: x, lambda x: F(3))
    if p is None: continue
    x, y = p; V = (F(1), x, y); t = t_N1(*V); n += 1
    if not (F(1, 4) <= t <= F(3, 4) / y and ok(V, t)): bad += 1
print("  random 1<x<y<=3: %d, exceptions: %d" % (n, bad))

print("\n== [C] Argon G_1 example 10:22:33 (x=2.2, y=3.3) ==")
V = (F(10), F(22), F(33)); print("  in S6-A:", in_S6(F(22, 10), F(33, 10)), "; t=3/(a+c):", show(V, F(3, 43)))
print("  t=k/(a+b), k=1..12 successes:", [k for k in range(1, 13) if ok(V, F(k, 32))])
print("  t=k/(a+c), k=1..12 successes:", [k for k in range(1, 13) if ok(V, F(k, 43))])
print("  t=k/(b+c), k=1..12 successes:", [k for k in range(1, 13) if ok(V, F(k, 55))])
print("  note: G_1 as written (x in (1.8,2.33), 1.4x<y<1.66x) contains y<=3 points, e.g. (1,1.9,2.7) in N1:", in_N1(F(19, 10), F(27, 10)))

print("\n== [C/D closure] 'union = whole region, no remaining gap' ==")
print("  Using ONLY the formulas Argon actually defines (y<=3 [S2/N1], R1, S6-A, B.2; 'S5-Nudge' and G_m are not defined):")
n = unc = mism = 0; wit = []
for i in range(200000):
    x = rq(1, 6); y = x + rq(F(1, 10**6), [5, 50, 5000][i % 3]); n += 1
    cov = in_N1(x, y) or in_R1(x, y) or in_S6(x, y) or in_AB(x, y)
    if not cov:
        unc += 1
        if len(wit) < 3: wit.append((float(x), float(y)))
    if cov != (not in_U(x, y)): mism += 1
print("  random (x,y): %d, uncovered: %d, mismatches vs Puck's exact set U={1<x<7/3, y>8-x}: %d" % (n, unc, mism))
print("  Stronger: points of U where all four TIMES (1/(a+c), 2/(b+c), 3/(a+c), B.2) actually fail:")
cnt = 0
for a in range(1, 13):
    for b in range(a + 1, 40):
        for c in range(b + 1, 60):
            V = (a, b, c)
            if in_U(F(b, a), F(c, a)) and not any(ok(V, f(*V)) for f in (t_N1, t_R1, t_S6, t_AB)): cnt += 1
print("  integer triples a<=12, b<40, c<60 in U with all four times failing: %d" % cnt)
for V, t, name in [((5, 6, 56), t_P1((5, 6, 56)[0], 6, 56), "k=ceil((a+c)/4a)=4, t=4/61 (Puck P1)"), ((7, 13, 44), F(3, 57), "t=3/(b+c)=1/19 (Puck R2)")]:
    print("  witness %s: N1 %s | R1 %s | S6 %s | B.2 %s" % (V, g(V, t_N1(*V)), g(V, t_R1(*V)), g(V, t_S6(*V)), g(V, t_AB(*V))))
    print("     -> 'specified formulas fail', NOT a conjecture counterexample:", name, show(V, t))
