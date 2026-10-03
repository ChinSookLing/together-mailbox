# TEST (Opus) · PT004 L3-C · stage (1b): unit orbits, and the support-weight count used for p = 83.
from itertools import combinations_with_replacement, combinations
from math import comb
exec(open('stage1_test.py').read().split('ok = True')[0])
def unit_orbits(ms_list, p):
    def fold(x): x %= p; return min(x, p - x)
    seen, orbits = set(), []
    for ms in ms_list:
        if ms in seen: continue
        orb = {tuple(sorted(fold(u * v) for v in ms)) for u in range(1, p)}
        seen |= orb; orbits.append(min(orb))
    return orbits
def count_via_supports(k, p):
    """Improper level-1 multisets = sum over covering supports T (|T| <= k) of C(k-1, |T|-1)."""
    n = (p - 1) // 2
    def d(x): r = x % p; return min(r, p - r)
    cov = {v: frozenset(a for a in range(1, n + 1) if (k + 1) * d(a * v) < p) for v in range(1, n + 1)}
    allt = frozenset(range(1, n + 1)); total = 0
    for s in range(1, k + 1):
        for T in combinations(range(1, n + 1), s):
            if frozenset().union(*(cov[v] for v in T)) == allt: total += comb(k - 1, s - 1)
    return total
ok = True
for k, p in [(3, 11), (4, 11), (4, 13), (5, 13), (5, 17), (6, 17), (6, 23), (7, 23)]:
    A = improper_level1_direct(k, p) if p < 20 else improper_level1_cover(k, p)
    o = unit_orbits(A, p); s = count_via_supports(k, p)
    good = s == len(A); ok &= good
    print(f"k={k} p={p}: multisets {len(A)} support-count {s} {'OK' if good else 'MISMATCH'}; unit orbits {len(o)}; n={(p-1)//2}")
print("ALL OK" if ok else "FAIL")
