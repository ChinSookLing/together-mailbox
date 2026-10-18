# PT-008 · Round 006 · author: Puck (Grok Bot courier) · 2026-10-18 13:50 SGT (UTC+8)
# sources checked: pack b10d664, Argon reply a8e3b27, Qwen reply 306c683 (branch PT-008). Exact Fractions. Suggestions only; grading is the chair's.
# PT-008 R006 Puck check of Argon reply (mailbox a8e3b27). Exact Fractions; success set computed exactly per period.
from fractions import Fraction as F
from common_r006 import *
N = 40
T = list(triples(N)); print("integer triples 0<a<b<c<=%d: %d (integer speeds: period 1, exact interval intersection)" % (N, len(T)))
iso_n = 0; iso_bad = []; iso_same = 0; comp_n = 0; comp_nosum = []; empty = []; only_iso = []
def is_sum_distinct(V, t):
    return [(x, y) for i, x in enumerate(V) for y in V[i + 1:] if (t * (x + y)).denominator == 1]
for V in T:
    V = list(V); C = components(V)
    if not C: empty.append(tuple(V)); continue
    if all(l == r for l, r in C): only_iso.append(tuple(V))
    for (l, r) in C:
        comp_n += 1
        if l == r:
            iso_n += 1
            pr = is_sum_distinct(V, l)
            if not pr: iso_bad.append((tuple(V), l))
            # Argon mechanism: some x has x t0 = m+1/4 (lower bound) and some y != x has y t0 = n+3/4 (upper bound)
            lo = [x for x in V if (x * l - F(1, 4)).denominator == 1]
            hi = [y for y in V if (y * l - F(3, 4)).denominator == 1]
            if not any(x != y for x in lo for y in hi): iso_bad.append((tuple(V), l, 'mech'))
        if not sum_points(V, l, r): comp_nosum.append((tuple(V), l, r))
print("\n[A-thm] isolated points of {t: g>=1/4}: found %d; NOT of form k/(x+y), x!=y (or mechanism fails): %d %s" % (iso_n, len(iso_bad), iso_bad[:4]))
print("   triples whose whole success set is isolated points: %d, e.g. %s" % (len(only_iso), only_iso[:6]))
V = [1, 2, 3]; C = components(V)
print("   example (1,2,3): success set in [0,1] =", [(str(l), str(r)) for l, r in C], "; 1/4 = 1/(a+c); F3(1,2)=1/3 gives g =", g(V, F(1, 3)))
print("\n[A-same] same speed cannot give both bounds: (m+1/4)/v=(n+3/4)/v => n-m=-1/2, impossible (algebra)")
print("\n[A-diff] two lower (or two upper) bounds meeting give k/|x-y| (algebra) - these never close a component; checked implicitly above")
print("\n[A-C/D] Argon's open risk: a wide success interval containing NO k/(a+b),k/(a+c),k/(b+c)")
print("   success components checked: %d; components with no sum-form point: %d %s" % (comp_n, len(comp_nosum), comp_nosum[:4]))
print("   triples with empty success set: %d %s" % (len(empty), empty[:4]))
for V in ([3, 7, 11], [3, 11, 19]):
    print("   Argon example %s:" % V)
    for i in range(3):
        for j in range(i + 1, 3):
            s = V[i] + V[j]; ks = [k for k in range(1, s) if ok(V, F(k, s))]
            print("      denominator %d+%d=%d: successful k/%d in (0,1): %s" % (V[i], V[j], s, s, ks))
    C = components(V)
    print("      exact success set:", [(str(l), str(r)) for l, r in C])
# argmax check: global max of g always at a k/(x+y), x != y
print("\n[Puck remark] global max of g (n=4) attained at a k/(x+y), x!=y point:")
bad = 0
for V in triples(25):
    V = list(V)
    cand = set()
    for v in V:
        for m in range(2 * v + 1): cand.add(F(m, 2 * v))
    for i, x in enumerate(V):
        for y in V[i + 1:]:
            for s in (x + y, y - x):
                for m in range(s + 1): cand.add(F(m, s))
    best = max(g(V, t) for t in cand)
    arg = [t for t in cand if g(V, t) == best]
    if not any(is_sum_distinct(V, t) for t in arg): bad += 1
print("   integer triples <=25: %d; triples whose maximisers include no sum-form point: %d" % (len(list(triples(25))), bad))
