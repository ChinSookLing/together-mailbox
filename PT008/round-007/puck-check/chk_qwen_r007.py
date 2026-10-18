# PT-008 · Round 007 · author: Puck (Grok Bot courier) · 2026-10-18 SGT (UTC+8)
# Puck check of QWEN R007 reply (PT008/round-007/2026-10-18T1452-reply-Qwen-R007.md, commit 5771a10). Exact Fractions.
# Suggestions only; grading is the chair's.
from common_r007 import *
random.seed(1452)
def show(V, t): return "t=%s  ||at||,||bt||,||ct|| = %s  g=%s" % (t, ", ".join(str(nd(v * t)) for v in V), g(V, t))

print("== [A.1] Pairing reduction: t=k/(p+q) => ||pt||=||qt|| ==")
bad = 0
for i in range(30000):
    p = rq(F(1, 100), 100); q = p + rq(F(1, 10**6), 100); k = random.randint(1, 10**4); t = F(k) / (p + q)
    if nd(p * t) != nd(q * t): bad += 1
print("  30000 random (p,q,k): mismatches %d" % bad)

print("\n== [A.2] R1 ==")
V = (F(1), F(2), F(73, 10)); print("  header form 5x/3<=y<=8-x/3 contains (1,2,7.3):", in_R1_typo(F(2), F(73, 10)), "->", show(V, t_R1(*V)), "(FAILS); correct form y<=8-x excludes it:", in_R1(F(2), F(73, 10)))
n = bad = 0
for i in range(60000):
    p = rand_xy(1, 3, lambda x: F(5, 3) * x, lambda x: 8 - x)
    if p is None: continue
    x, y = p; V = (F(1), x, y); n += 1
    if not ok(V, t_R1(*V)): bad += 1
print("  random points in R1 (y<=8-x, the form Qwen's proof uses): %d, failures %d" % (n, bad))
print("  R1 nonempty only for x<=3 (5x/3<=8-x): corner (1,3,5):", show((F(1), F(3), F(5)), t_R1(F(1), F(3), F(5))))

print("\n== [A.3] S6-A equality boundaries as worded by Qwen ==")
V = (F(1), F(2), F(3)); print("  y=3 (x=2): at=%s, ||at||=%s  (Qwen writes '||at||=3/4'; the value 3/4 is at itself, the distance is 1/4)" % (3 * V[0] / (1 + V[2]), nd(F(3, 4))))
V = (F(1), F(5), F(11)); print("  y=11 (x=5):", show(V, t_S6(*V)))
V = (F(1), F(5, 3), F(3)); print("  x=5(1+y)/12 at y=3:", show(V, t_S6(*V)))

print("\n== [A.4] N1: 1<x<y<=3, t=1/(a+c) ==")
n = bad = 0
for i in range(60000):
    p = rand_xy(1, 3, lambda x: x, lambda x: F(3))
    if p is None: continue
    x, y = p; V = (F(1), x, y); n += 1
    if not ok(V, t_N1(*V)): bad += 1
print("  random: %d, failures %d; exactness: t=1/(a+c) needs ||1/(1+y)||>=1/4 <=> y<=3" % (n, bad))
V = (F(1), F(1999, 1000), F(2)); print("  remark 'x->y- gives ||bt||->1/4' checked at (1,1.999,2):", show(V, t_N1(*V)), "-> limit is 1/(1+y), =1/4 only when y=3")
V = (F(1), F(3) - F(1, 10**6), F(3)); print("  at y=3, x->3-:", show(V, t_N1(*V)))

print("\n== [B.1] no finite y-independent k set ==")
print("  k/(a+c) family: least k with ||k/(1+y)||>=1/4 is ceil((1+y)/4) for y>=3:",
      all(min(k for k in range(1, 400) if nd(F(k) / (1 + y)) >= Q) == ce((1 + y) / 4) for y in [F(3), F(7, 2), F(10), F(101, 3), F(1000)]))
bad = 0
for m in range(2, 41):
    V = (1, 2, 3 * m); K = (3 * m) // 4
    if 3 * m + 1 <= 4 * K: K -= 1
    if any(ok(V, F(k, s)) for k in range(1, K + 1) for s in (3, 3 * m + 1, 3 * m + 2)): bad += 1
print("  all three families: (1,2,3m), m=2..40: some k<=K with 4K<3m+1 succeeds in %d cases (0 => no fixed bound on k works; R006 Puck D.3 family)" % bad)

print("\n== [B.2] k=ceil((1+y)/4), t=k/(a+c): k/(1+y) in [1/4, 1/4+1/(1+y)) within [1/4,1/2] for y>=3 ==")
bad = 0
for i in range(30000):
    y = 3 + rq(0, 10**4); k = ce((1 + y) / 4); u = F(k) / (1 + y)
    if not (Q <= u < Q + 1 / (1 + y) and u <= F(1, 2)): bad += 1
print("  30000 random y: violations %d" % bad)
print("  -> Qwen leaves the x-condition open. Puck: for x<3 a simple sufficient condition is x <= 3(1+y)/(5+y) (region P1, chk_cover_r007.py: 0 failures)")

print("\n== [B.3] N2: t=2/(a+b) for 5/3<=x<=7 ==")
n = bad = 0
for i in range(30000):
    x = rq(F(5, 3), 7); t = F(2) / (1 + x)
    if not (nd(t) >= Q and nd(x * t) >= Q): bad += 1
print("  pair condition ||at||=||bt||>=1/4 on [5/3,7]: 30000 random x, failures %d; just outside: x=1.66 -> %s, x=7.01 -> %s" % (bad, nd(F(2) / F(266, 100)), nd(F(2) / F(801, 100))))
V = (F(1), F(7, 2), F(4)); print("  Qwen's numeric example (x,y)=(3.5,4):", show(V, t_N2(*V)), "-> ||16/9||=2/9 < 1/4: FAILS (Qwen wrote all >= 1/4)")
xs = [F(35, 12) + F(k, 1000) * (4 - F(35, 12)) for k in range(1, 1000)]
good = [x for x in xs if ok((F(1), x, F(4)), t_N2(F(1), x, F(4)))]
print("  y=4, x in (35/12,4): N2 works on %d/%d grid points; smallest working x = %s (~%.4f); exact threshold x>=25/7=%.4f: %s" % (
    len(good), len(xs), min(good), float(min(good)), 25 / 7, all((x >= F(25, 7)) == (x in good) for x in xs)))
V = (F(1), F(3), F(4)); print("  e.g. (1,3,4):", show(V, t_N2(*V)), " -- covered instead by Argon B.2 (x>=7/3):", show(V, t_AB(*V)))

print("\n== [C.2] gaps ==")
print("  G1 (y=4): R1 covers x<=12/5:", in_R1(F(12, 5), F(4)), not in_R1(F(12, 5) + F(1, 10**6), F(4)), "| S6-A covers [25/12,35/12]:", in_S6(F(25, 12), F(4)), in_S6(F(35, 12), F(4)), not in_S6(F(35, 12) + F(1, 10**6), F(4)))
print("     with Argon B.2 (x>=7/3) the y=4 slice is fully covered: grid x in (1,4), 3000 pts, uncovered:",
      sum(1 for k in range(1, 3000) if not (lambda x: in_R1(x, F(4)) or in_S6(x, F(4)) or in_AB(x, F(4)))(1 + F(3 * k, 3000))))
V = (F(1), F(3), F(27, 2)); print("  G2 'y>11 no coverage' vs Qwen's own N2 at (1,3,13.5):", show(V, t_N2(*V)), "| and Argon B.2 covers all x>=7/3")
V = (F(1), F(3, 2), F(7, 2)); print("  G3 example (1.5,3.5): in R1 =", in_R1(F(3, 2), F(7, 2)), "->", show(V, t_R1(*V)), "(so NOT a gap)")
n = 0
for i in range(200000):
    x = rq(1, 11); y = rq(3, 11)
    if 3 < y < 11 and x < y and x < F(5, 12) * (1 + y) and y < F(5, 3) * x: n += 1
print("  G3 as defined {3<y<11, x<5(1+y)/12, y<5x/3}: 200000 random (x,y), points found: %d (algebra: needs x<15/11 and x>9/5 -> empty)" % n)

print("\n== [C.3] example a=1,b=2,c=100, t=25/102 ==")
V = (1, 2, 100); print("  ", show(V, F(25, 102)), "-> ||at||=25/102<1/4: NOT a success time")
print("   k<=3 over all three sums succeeds?", [(k, s) for s in (3, 101, 102) for k in range(1, 4) if ok(V, F(k, s))])
print("   successes k/(a+c), k<=40:", [k for k in range(1, 41) if ok(V, F(k, 101))], "| k/(b+c), k<=40:", [k for k in range(1, 41) if ok(V, F(k, 102))], "| k/(a+b), k<=3:", [k for k in range(1, 4) if ok(V, F(k, 3))])
print("   e.g. Qwen's own B.2 rule k=ceil(101/4)=26:", show(V, F(26, 101)))
