# PT-008 · Round 006 · author: Puck (Grok Bot courier) · 2026-10-18 13:50 SGT (UTC+8)
# sources checked: pack b10d664, Argon reply a8e3b27, Qwen reply 306c683 (branch PT-008). Exact Fractions. Suggestions only; grading is the chair's.
# PT-008 R006 Puck check of Qwen reply (mailbox 306c683). Exact Fractions; N=60 integer triples.
import random
from fractions import Fraction as F
from decimal import Decimal as D, getcontext
from common_r006 import *
random.seed(6)
N = 60
T = list(triples(N)); print("integer triples 0<a<b<c<=%d: %d" % (N, len(T)))
def R1(a, b, c):  # Qwen region as written
    return F(8 * a, 3) <= b + c <= 8 * a and F(5 * b, 3) <= c <= 7 * b
def R1s(a, b, c):  # Puck simplification
    return F(5 * b, 3) <= c <= 8 * a - b
def fam2(a, b, c): return c <= 3 * a
print("\n[A1] pair-sum lemma ||ut||=||vt|| at t=k/(u+v) (Qwen wrote ||ct||=||k-ut||; should read ||vt||)")
bad = 0
for _ in range(20000):
    u, v = F(random.randint(1, 500), random.randint(1, 50)), F(random.randint(1, 500), random.randint(1, 50))
    k = random.randint(1, 30); t = k / (u + v)
    bad += nd(u * t) != nd(v * t)
print("   20000 random rational pairs, mismatches:", bad)
print("\n[A3] (2,4,7) at t=2/11:", [str(nd(v * F(2, 11))) for v in (2, 4, 7)], "g =", g((2, 4, 7), F(2, 11)), "R1:", R1(2, 4, 7))
print("\n[B] claim: R1 => t=2/(b+c) succeeds; plus converse (is R1 exact?)")
viol = []; conv = []; n1 = 0
for (a, b, c) in T:
    t = F(2, b + c); s = ok((a, b, c), t); r = R1(a, b, c); n1 += r
    if r and not s: viol.append((a, b, c))
    if s and not r: conv.append((a, b, c))
print("   R1 members %d (%.2f%%); violations R1 & fail: %d %s; succeed but outside R1: %d %s" % (n1, 100 * n1 / len(T), len(viol), viol[:5], len(conv), conv[:5]))
viol = 0; conv = 0; n = 0
for _ in range(100000):
    a, b, c = sorted(F(random.randint(1, 10**6), random.randint(1, 10**4)) for _ in range(3))
    if not a < b < c: continue
    # bias half the samples into the region: choose c in [5b/3, 8a-b] when possible
    if random.random() < 0.5 and F(5, 3) * b < 8 * a - b:
        c = F(5, 3) * b + (8 * a - 2 * b - F(5, 3) * b + b) * F(random.randint(0, 10**6), 10**6)
        if not b < c: continue
    n += 1; t = 2 / (b + c); s = ok((a, b, c), t); r = R1(a, b, c)
    viol += (r and not s); conv += (s and not r)
print("   %d random rational triples (half biased into R1): violations %d, succeed-outside-R1 %d" % (n, viol, conv))
print("   boundary points: (1,3,5) [b=3a,c=5b/3=8a-b]:", g((1, 3, 5), F(2, 8)), " (3,6,10) c=5b/3:", R1(3, 6, 10), g((3, 6, 10), F(2, 16)))
print("\n[B'] redundancy: R1 == {5b/3 <= c <= 8a-b} (lower bound b+c>=8a/3 and c<=7b implied)")
mm = [x for x in T if R1(*x) != R1s(*x)]
print("   integer mismatches:", len(mm))
mm = 0
for _ in range(100000):
    a, b, c = sorted(F(random.randint(1, 10**5), random.randint(1, 999)) for _ in range(3))
    if a < b < c: mm += R1(a, b, c) != R1s(a, b, c)
print("   random rational mismatches:", mm, "; R1 nonempty needs 5b/3<=8a-b i.e. b<=3a; then c<=8a-b<7a")
print("\n[C2] coverage with known family c<=3a (t=1/(4a)); Qwen calls that family PROVED - pack/chair grade is PROOF CANDIDATE")
c2 = sum(fam2(*x) for x in T); c1 = sum(R1(*x) for x in T)
both = sum(fam2(*x) and R1(*x) for x in T); new = sum(R1(*x) and not fam2(*x) for x in T)
print("   c<=3a: %d (%.2f%%), R1: %d, overlap: %d, R1 new (c>3a): %d, union: %d (%.2f%%)" % (c2, 100 * c2 / len(T), c1, both, new, c2 + new, 100 * (c2 + new) / len(T)))
print("   overlap example:", next(x for x in T if fam2(*x) and R1(*x)), " new examples:", [x for x in T if R1(*x) and not fam2(*x)][:6])
print("\n[C4] heuristic 'pick b+c when c-b is the closest pair'. (2,4,7): b-a=%d, c-b=%d -> c-b NOT smallest, yet 2/(b+c) works" % (4 - 2, 7 - 4))
for s, nm in ((6, 'a+b'), (9, 'a+c'), (11, 'b+c')):
    print("   (2,4,7) denominators %s=%d: k with success in 1..%d:" % (nm, s, s), [k for k in range(1, s) if ok((2, 4, 7), F(k, s))])
gap = [x for x in T if R1(*x) and (x[2] - x[1]) < (x[1] - x[0])]
print("   R1 triples where c-b < b-a (Qwen's heuristic case):", len(gap), "(proof: in R1 c-b>=2b/3>=b-a since a>=b/3)")
print("\n[D1] t=1/(a+c) works iff c<=3a (Qwen D: 'k=1 corresponds to c<=3a')")
mm = [x for x in T if ok(x, F(1, x[0] + x[2])) != fam2(*x)]
print("   integer mismatches:", len(mm), mm[:5])
print("\n[D2] Qwen IDEA k=2,3 with a+c cover new region: triples outside (c<=3a or R1) where 2/(a+c) or 3/(a+c) succeeds:")
rest = [x for x in T if not fam2(*x) and not R1(*x)]
for k in (2, 3):
    m = [x for x in rest if ok(x, F(k, x[0] + x[2]))]
    print("   k=%d: %d of %d remaining; e.g. %s" % (k, len(m), len(rest), m[:4]))
print("\n[D3] Qwen question: does some triple fail for ALL k in 1..4 and all three denominators?")
def anyk(x, K):
    a, b, c = x
    return any(ok(x, F(k, s)) for s in (a + b, a + c, b + c) for k in range(1, K + 1))
fails = [x for x in T if not anyk(x, 4)]
fails.sort(key=lambda x: (x[2], x))
print("   integer triples failing all k<=4: %d; smallest by c: %s" % (len(fails), fails[:6]))
print("   family (1,2,3m): sums 3,3m+1,3m+2; ||c k/3||=0 and ||k/(3m+1)||,||k/(3m+2)||<1/4 for k<(3m+1)/4 -> all k<=K fail when 3m+1>4K")
for m in (6, 10, 20):
    x = (1, 2, 3 * m); K = (3 * m) // 4
    fk = [K2 for K2 in range(1, 3 * m + 3) if anyk(x, K2)]
    best = max(((g(x, t), t) for (l, r) in components(list(x)) for t in [l, (l + r) / 2, r]))
    print("   (1,2,%d): fails all k<=%d? %s ; smallest K with a sum-form success: %s ; success set nonempty, e.g. t=%s g=%s" % (3 * m, K, not anyk(x, K), fk[0], best[1], best[0]))
print("\n[D4] truncated remark 'works for irrational speeds (proof uses no rationality)': proof uses only real inequalities; spot checks at 60 digits:")
getcontext().prec = 60
def ndd(x): r = x - int(x); return min(r, 1 - r)
for a, b, c in [(D(1), D(2).sqrt(), D(17).sqrt()), (D(3).sqrt(), D(5).sqrt(), D(3).sqrt() * 3 + D(1) / D(7)), (D(2), D(4), D(7) + D(2).sqrt() / 10**6)]:
    inr = D(5) * b / 3 <= c <= 8 * a - b; t = 2 / (b + c)
    print("   (%.6f,%.6f,%.6f) in R1: %s  min dist = %.12f" % (a, b, c, inr, min(ndd(a * t), ndd(b * t), ndd(c * t))))
