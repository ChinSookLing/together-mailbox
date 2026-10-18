# PT-008 · Round 006 · author: Puck (Grok Bot courier) · 2026-10-18 SGT (UTC+8)
# sources checked: Opus reply 84e34c6. Exact Fractions. Finer grid + random rationals on D for S3uS4uS5 and Puck's extra S6=3/(a+c).
import random, sys
from fractions import Fraction as F
from collections import Counter
sys.argv = sys.argv[:1]
import importlib.util
from common_r006 import nd, ok, Q
exec(open('chk_opus_r006.py').read().split('print("="*70); print("[B1]')[0])   # helper defs only (PLS, crit, guar)
def cl(x): return -((-x.numerator) // x.denominator)
def kac(a, c): return cl((F(a) + F(c)) / (4 * F(a)))
def cov(b, c):
    V = (1, b, c)
    if crit(b, c, 1): return 'S3'
    t = F(kac(1, c)) / (1 + c)
    if nd(b * t) >= Q: return 'S4'
    if F(5, 4) * (1 + b) <= c <= F(7, 4) * (1 + b): return 'S5'
    return None
def S6(b, c):
    t = F(3) / (1 + c); return 3 <= c <= 11 and nd(b * t) >= Q, t
H = 400; tot = 0; unc = 0; s6 = 0; s6bad = 0
for i in range(1, 2 * H):
    b = 1 + F(i, H)
    for j in range(1, 6 * H):
        c = 3 + F(j, H)
        if not c < 3 * b: break
        tot += 1
        if cov(b, c) is None:
            unc += 1; f, t = S6(b, c); s6 += f; s6bad += f and not ok((1, b, c), t)
print("grid H=%d on D: points %d, uncovered by S3uS4uS5 %d (%.3f%%), of those solved by S6=3/(a+c): %d, S6 claimed-but-fails %d" % (H, tot, unc, 100 * unc / tot, s6, s6bad))
random.seed(18); tot = unc = s6 = 0; ex = []
while tot < 100000:
    b = 1 + 2 * F(random.randint(1, 10**6 - 1), 10**6); c = 3 + (3 * b - 3) * F(random.randint(1, 10**6 - 1), 10**6)
    tot += 1
    if cov(b, c) is None:
        unc += 1; f, t = S6(b, c); s6 += f and ok((1, b, c), t)
        if not f: ex.append((b, c))
print("random rationals uniform on D (a=1): %d, uncovered by S3uS4uS5 %d (%.3f%%), solved by S6: %d, left: %d %s" % (tot, unc, 100 * unc / tot, s6, len(ex), ex[:3]))
# Region E = {b<3a, c>=3b} (Opus covers it by S2 = Nudge, not defined in the reply): does S3uS4uS5uS6 cover it? grid step 1/50, c/a<=30
H = 50; tot = unc = 0; L = []
for i in range(1, 2 * H):
    b = 1 + F(i, H); j = 0
    while True:
        c = 3 * b + F(j, H); j += 1
        if c > 30: break
        tot += 1
        if cov(b, c) is None and not (S6(b, c)[0]):
            unc += 1; L.append((b, c))
print("region E={b<3a, 3b<=c<=30a}, grid 1/50: points %d, uncovered by S3uS4uS5uS6: %d (%.2f%%); c/a range of uncovered: %s..%s; examples %s" % (
      tot, unc, 100 * unc / tot, min(c for b, c in L) if L else '-', max(c for b, c in L) if L else '-', [(str(b), str(c)) for b, c in L[:4]]))
