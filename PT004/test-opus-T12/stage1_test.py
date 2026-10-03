# TEST (Opus) · PT004 L3-C · stage (1): tiny cases, checked against the paper's Definition 2.1 directly.
# New code written from arXiv:2609.02604v2 §2 and §4 (no author code read or run). Stdlib only.
from itertools import combinations_with_replacement, product
def improper_level1_direct(k, p):
    """Multisets of k speed classes (1..(p-1)/2) with NO witness t = a/p (a = 0..p-1):
    witness means ||a*v/p|| >= 1/(k+1) for every v, i.e. (k+1)*d_p(a v) >= p.  Level 1: gcd alternative unavailable."""
    n = (p - 1) // 2
    def d(x): r = x % p; return min(r, p - r)
    out = []
    for ms in combinations_with_replacement(range(1, n + 1), k):
        if not any(all((k + 1) * d(a * v) >= p for v in ms) for a in range(p)):
            out.append(ms)
    return out
def improper_level1_cover(k, p):
    """Same family via the paper's (7): v covers time class a when (k+1) d_p(a v) < p; improper iff every folded time is covered."""
    n = (p - 1) // 2
    def d(x): r = x % p; return min(r, p - r)
    cov = {v: frozenset(a for a in range(1, n + 1) if (k + 1) * d(a * v) < p) for v in range(1, n + 1)}
    allt = frozenset(range(1, n + 1))
    return [ms for ms in combinations_with_replacement(range(1, n + 1), k)
            if frozenset().union(*(cov[v] for v in ms)) == allt]
ok = True
for k, p in [(2, 5), (2, 7), (3, 7), (3, 11), (4, 11), (4, 13), (5, 13), (5, 17), (6, 17)]:
    A = improper_level1_direct(k, p); B = improper_level1_cover(k, p)
    same = A == B; ok &= same
    print(f"k={k} p={p}: improper level-1 multisets direct={len(A)} cover={len(B)} same={same}" + (f"  e.g. {A[:3]}" if A else ""))
# hand check: k=2, p=7: n=3, classes 1,2,3; times a=1..6.  (k+1)d(av) >= 7 needs d(av) >= 3, i.e. av = ±3 mod 7.
# For speeds (1,2): a=3 -> d(3)=3, d(6)=1 fail; a=... no a gives both 3 -> improper. For (1,1): a=3 works -> proper.
A = improper_level1_direct(2, 7)
print("k=2 p=7 improper:", A, " hand check: (1,1) proper?", (1, 1) not in A, " (1,2) improper?", (1, 2) in A)
print("ALL SAME" if ok else "MISMATCH")
