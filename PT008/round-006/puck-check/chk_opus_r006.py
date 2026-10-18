# PT-008 · Round 006 · author: Puck (Grok Bot courier) · 2026-10-18 SGT (UTC+8)
# sources checked: pack b10d664, Opus reply 84e34c6 (branch PT-008). Exact Fractions only (no floats in any verdict).
# PT-008 R006 Puck check of OPUS reply (PLS = Phase-Lock Sweep). Uses common_r006.py helpers.
import random, sys
from fractions import Fraction as F
from math import ceil, floor
from collections import Counter
from common_r006 import nd, g, ok, triples, Q
random.seed(2026_10_18)
def cl(x): return -((-x.numerator) // x.denominator)          # exact ceil of Fraction
def fr(x): return x - (x.numerator // x.denominator)           # exact frac
def PLS(p, q, r):
    """Opus A1 exactly as written. returns (t, kstar, k0, x0, j, eta)"""
    p, q, r = F(p), F(q), F(r); s = p + q; th = p / s; eta = r / s
    k0 = cl(s / (4 * r)); x0 = fr(k0 * th)
    if Q <= x0 <= 3 * Q: j = 0
    else:
        Dl = fr(Q - x0); j = cl(Dl / th)
    k = k0 + j; return F(k) / s, k, k0, x0, j, eta
def crit(p, q, r):
    t, k, k0, x0, j, eta = PLS(p, q, r); return k * eta <= 3 * Q
def guar(p, q, r): return F(r) * (5 * F(p) + F(q)) <= F(p) * (F(p) + F(q))
def B1_test(p, q, r, stats):
    t, k, k0, x0, j, eta = PLS(p, q, r); th = F(p) / (F(p) + F(q))
    stats['n'] += 1
    # (ii) pair phase
    fx = fr(k * th)
    if j == 0: assert Q <= fx <= 3 * Q
    else:
        assert Q <= fx < Q + th, (p, q, r)
        stats['x0<1/4' if x0 < Q else 'x0>3/4'] += 1
    assert nd(F(p) * t) >= Q and nd(F(q) * t) >= Q, (p, q, r)
    # (iii) k*eta >= 1/4 always
    assert k * eta >= Q
    c = k * eta <= 3 * Q; G = guar(p, q, r)
    if c:
        stats['crit'] += 1
        if not nd(F(r) * t) >= Q: stats['CRIT_FAIL'] += 1; print("  CRITERION FAIL", p, q, r)
    else:
        stats['crit_false'] += 1
        if nd(F(r) * t) >= Q: stats['crit_false_but_t_ok'] += 1   # e.g. k*eta in [5/4,7/4]
    if G:
        stats['guar'] += 1
        if not c: stats['GUAR_FAIL'] += 1; print("  GUARANTEE FAIL", p, q, r)
    if F(r) > F(p): stats['r>p'] += 1; stats['r>p&guar'] += G; stats['r>p&crit'] += c; stats['r>p&crit&fail'] += c and not nd(F(r)*t) >= Q
    if F(r) == F(p): stats['r=p'] += 1
print("="*70); print("[B1] PLS theorem: criterion => success, guarantee => criterion; steps (ii),(iii) asserted")
st = Counter(); N = 40
for p in range(1, N + 1):
    for q in range(p + 1, N + 1):
        for r in range(1, N + 1): B1_test(p, q, r, st)
print("  exhaustive integers 1<=p<q<=%d, 1<=r<=%d:" % (N, N), dict(st))
st = Counter(); vals = sorted({F(n, d) for n in range(1, 13) for d in range(1, 13)})
for p in vals:
    for q in vals:
        if q <= p: continue
        for r in vals[::3]: B1_test(p, q, r, st)
print("  rationals n/d, n,d<=12 (%d values; r every 3rd value):" % len(vals), dict(st))
st = Counter()
for _ in range(200000):
    p, q = sorted(F(random.randint(1, 10**6), random.randint(1, 10**4)) for _ in range(2))
    if p == q: continue
    r = F(random.randint(1, 10**6), random.randint(1, 10**4)) if random.random() < .5 else p * F(random.randint(1, 10**4), 10**4)
    B1_test(p, q, r, st)
print("  200000 random rationals (half with r<p):", dict(st))
print("  note: guarantee r(5p+q)<=p(p+q) forces r < p(p+q)/(5p+q) < p, so the 'r>p' case of the guarantee is vacuous;")
print("        the criterion part needs no r<p.")
print("="*70); print("[B2] b>=3a => PLS guarantee for (b,c;a); example {2,5,10}")
bad = 0; n = 0
for (a, b, c) in triples(60):
    if b >= 3 * a: n += 1; bad += not guar(b, c, a)
for _ in range(100000):
    a = F(random.randint(1, 10**5), random.randint(1, 999)); b = a * (3 + F(random.randint(0, 10**5), 10**3)); c = b * (1 + F(random.randint(1, 10**5), 10**3))
    n += 1; bad += not guar(b, c, a)
print("  triples with b>=3a tested: %d, guarantee false: %d" % (n, bad))
t, k, k0, x0, j, eta = PLS(5, 10, 2)
print("  {2,5,10}: b<3a:", 5 < 6, " c<3b:", 10 < 15, " c>3a:", 10 > 6, " a(5b+c)=%d <= b(b+c)=%d:" % (2*35, 5*15), guar(5, 10, 2))
print("  PLS(5,10;2): k0=%s x0=%s j=%s t=%s distances %s" % (k0, x0, j, t, [str(nd(v * t)) for v in (2, 5, 10)]))
print("="*70); print("[B3] c<=3a => t=1/(4a)")
bad = 0; n = 0
for (a, b, c) in triples(80):
    if c <= 3 * a: n += 1; bad += not ok((a, b, c), F(1, 4 * a))
print("  integer triples c<=80 with c<=3a: %d, failures %d; endpoint (2,5,6): %s ; (1,2,3): %s" % (n, bad,
      [str(nd(v * F(1, 8))) for v in (2, 5, 6)], [str(nd(v * F(1, 4))) for v in (1, 2, 3)]))
print("="*70); print("[B4] (2,4,7) PLS(4,7;2)")
t, k, k0, x0, j, eta = PLS(4, 7, 2)
print("  k0=%s x0=%s j=%s k*=%s t=%s k*eta=%s distances %s; guarantee: a(5b+c)=%d vs b(b+c)=%d -> %s" % (
      k0, x0, j, k, t, k * eta, [str(nd(v * t)) for v in (2, 4, 7)], 2 * 27, 4 * 11, guar(4, 7, 2)))
print("  old pair-ceiling k=ceil((b+c)/(4b))=%s: t=1/11 distances %s" % (cl(F(11, 16)), [str(nd(v * F(1, 11))) for v in (2, 4, 7)]))
print("="*70); print("[A2] piecewise rules")
def kac(a, c): return cl((F(a) + F(c)) / (4 * F(a)))
def S1(a, b, c): return F(c) <= 3 * F(a), F(1) / (4 * F(a))
def S3(a, b, c):
    t = PLS(b, c, a)[0]; return (guar(b, c, a) or crit(b, c, a)), t
def S4(a, b, c):
    t = F(kac(a, c)) / (F(a) + F(c)); return nd(F(b) * t) >= Q, t
def S5(a, b, c):
    s = F(a) + F(b); return F(5, 4) * s <= c <= F(7, 4) * s, 1 / s
def R1q(a, b, c): return F(5 * b, 3) <= c <= 8 * a - b, F(2) / (F(b) + F(c))   # Qwen R006 region (Puck form)
viol = Counter(); cnt = Counter(); T = list(triples(60))
for x in T:
    for nm, R in (('S1', S1), ('S3', S3), ('S4', S4), ('S5', S5)):
        c, t = R(*x)
        if c:
            cnt[nm] += 1
            if not ok(x, t): viol[nm] += 1; viol[nm + '_ex'] = viol.get(nm + '_ex') or x
print("  integer triples c<=60 (%d): members %s ; violations %s" % (len(T), dict(cnt), dict(viol)))
s5bad = [x for x in T if S5(*x)[0] and not ok(x, S5(*x)[1])]
print("  S5 failures all have b>3a:", all(x[1] > 3 * x[0] for x in s5bad), "; first:", s5bad[:3],
      " (1,4,7) t=1/5:", [str(nd(v * F(1, 5))) for v in (1, 4, 7)])
print("  S5 with b<=3a added: violations", sum(1 for x in T if S5(*x)[0] and x[1] <= 3 * x[0] and not ok(x, S5(*x)[1])))
print("  S4 note: with k_ac=ceil((a+c)/(4a)), k_ac*a/(a+c) in [1/4, 1/4+a/(a+c)) subset [1/4,3/4) so a,c always safe; only b is tested")
print("="*70); print("[C] coverage on dense region D = {b<3a, 3a<c<3b}, a=1, b=1+i/H, c=3+j/H (open bounds)")
H = int(sys.argv[1]) if len(sys.argv) > 1 else 200
tot = 0; unc = []; unc34 = 0; uncR1 = 0; swap = 0; rem_after_R1 = []
for i in range(1, 2 * H):
    b = 1 + F(i, H)
    for jj in range(1, 6 * H):
        c = 3 + F(jj, H)
        if not c < 3 * b: break
        tot += 1; V = (1, b, c)
        c3, c4, c5 = S3(*V)[0], S4(*V)[0], S5(*V)[0]
        if not (c4 or c5): unc34 += 1
        if c3 or c4 or c5: continue
        unc.append((b, c))
        # role swaps
        for (p, q, r) in ((1, c, b), (1, b, c)):
            tt = PLS(p, q, r)[0]
            if crit(p, q, r) and ok(V, tt): swap += 1; break
        if R1q(*V)[0]: uncR1 += 1
        else: rem_after_R1.append((b, c))
print("  grid H=%d: points in D: %d ; uncovered by S3uS4uS5: %d = %s%% ; (old R3uR4 = S4uS5 uncovered: %d = %s%%)" % (
      H, tot, len(unc), round(F(100 * len(unc), tot), 3).__float__() if False else "%.3f" % (100 * len(unc) / tot), unc34, "%.2f" % (100 * unc34 / tot)))
print("  role swaps PLS(a,c;b), PLS(a,b;c) with criterion true and success, on uncovered points:", swap)
print("  uncovered points inside Qwen R1 (t=2/(b+c)): %d ; remaining after adding R1: %d (%.3f%%)" % (uncR1, len(rem_after_R1), 100 * len(rem_after_R1) / tot))
def hist(L, nm):
    cb = Counter(); cc = Counter()
    for (b, c) in L: cb[floor(b * 10) / 10] += 1; cc[floor(c * 20) / 20] += 1
    print("  %s: b/a range [%s, %s], c/a range [%s, %s]" % (nm, min(b for b, c in L), max(b for b, c in L), min(c for b, c in L), max(c for b, c in L)))
    print("    by b/a (bins of 0.1):", sorted(cb.items()))
    print("    by c/a (bins of 0.05):", sorted(cc.items()))
if unc: hist(unc, "uncovered by S3uS4uS5")
if rem_after_R1: hist(rem_after_R1, "uncovered by S3uS4uS5uR1")
print("="*70); print("[C'] explicit remainder points, success time by SMALL EXACT SEARCH over k/(x+y), k<=60 (search, not construction)")
picks = []
L = rem_after_R1 if rem_after_R1 else unc
for P in (unc[:1] + unc[len(unc)//3:len(unc)//3+1] + unc[len(unc)//2:len(unc)//2+1] + unc[-1:] + L[:1] + L[-1:]):
    if P not in picks: picks.append(P)
for (b, c) in picks:
    V = (1, b, c); found = None
    for k in range(1, 61):
        for s in (1 + b, 1 + c, b + c):
            t = F(k) / s
            if ok(V, t) and (found is None or t < found[0]): found = (t, k, s)
        if found: break
    tt = found[0]
    nm = {1 + b: 'a+b', 1 + c: 'a+c', b + c: 'b+c'}[found[2]]
    print("  (a,b,c)=(1,%s,%s) (x%d: integers (%d,%d,%d)): S3/S4/S5/R1 = %s/%s/%s/%s ; k_ac=%d ; search found t=%d/(%s)=%s, distances %s" % (
          b, c, H, H, b * H, c * H, S3(*V)[0], S4(*V)[0], S5(*V)[0], R1q(*V)[0], kac(1, c), found[1], nm, tt, [str(nd(v * tt)) for v in V]))

print("="*70); print("[X] Puck extras")
# X1 boundary cases of B1: guarantee with equality, x0 exactly 1/4 or 3/4
st = Counter(); eq = 0
for p in range(1, 41):
    for q in range(p + 1, 81):
        r = F(p * (p + q), 5 * p + q); eq += 1; B1_test(p, q, r, st)
print("  X1 guarantee equality r=p(p+q)/(5p+q), 1<=p<=40, p<q<=80: %d cases, criterion fails %d, criterion=>success fails %d" % (eq, st['GUAR_FAIL'], st['CRIT_FAIL']))
bx = Counter()
for p in range(1, 41):
    for q in range(p + 1, 41):
        for r in range(1, 41):
            t, k, k0, x0, j, eta = PLS(p, q, r)
            if x0 in (Q, 3 * Q): bx[str(x0)] += 1; assert ok((p, q, r), t) or k * eta > 3 * Q
print("  X1 x0 exactly on 1/4 or 3/4 (j=0 branch), integers <=40:", dict(bx), "all consistent")
# X2 Qwen R1 subset of PLS criterion (b,c;a)?
T = list(triples(60)); m = [x for x in T if R1q(*x)[0] and not crit(x[1], x[2], x[0])]
print("  X2 Qwen R1 members not in PLS criterion region (c<=60):", len(m), m[:5])
bad = 0
for _ in range(100000):
    a = F(random.randint(1, 10**5), random.randint(1, 999)); b = a * (1 + F(random.randint(1, 2 * 10**5), 10**5))
    lo, hi = F(5, 3) * b, 8 * a - b
    if lo > hi: continue
    c = lo + (hi - lo) * F(random.randint(0, 10**5), 10**5)
    bad += not crit(b, c, a)
print("  X2 100000 random rationals in R1: not in PLS criterion:", bad)
# X3 exact-iff version of the criterion: ||k* r/(p+q)|| >= 1/4 (t already pair-safe), on the D grid remainder
rem_iff = [(b, c) for (b, c) in unc if not nd(PLS(b, c, 1)[0]) >= Q]
print("  X3 remainder points where PLS time t still works via ||a t||>=1/4 (k*eta>3/4 allowed):", len(unc) - len(rem_iff))
# X4 next sweep step on pair (a,c): t=(k_ac+1)/(a+c)
cov = [(b, c) for (b, c) in unc if ok((1, b, c), F(kac(1, c) + 1) / (1 + c))]
print("  X4 remainder points solved by t=(k_ac+1)/(a+c): %d of %d" % (len(cov), len(unc)))
left = [(b, c) for (b, c) in unc if (b, c) not in set(cov)]
print("     not solved by it:", len(left), left[:5])
lt31 = sum(1 for (b, c) in unc if c < F(31, 10)); print("  share of remainder with c/a<3.1: %d/%d = %.1f%%" % (lt31, len(unc), 100 * lt31 / len(unc)))
