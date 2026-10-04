#!/usr/bin/env python3
"""
TOGETHER - PROOF TABLE 004 - Round 3 - Turn 11 - item L3-C, stage 2 (second implementation)
Seat: Fable-A (testing seat).

A second, separate implementation of level-one generation, in Python, to compare with
the list written by the C program (pt004_l3c level1 P K FILE).

Level one (arXiv:2609.02604v2, Section 4): speed classes and time classes are 1..n,
n = (p-1)/2; class v covers time a when (k+1)*d_p(a*v) < p; I(k,p,1) is the family of
k-multisets of classes that cover every time class.  Units u act by v -> fold(u*v).
Orbit representative used here and in the C program: the lexicographically smallest
sorted k-tuple of the orbit.

Differences from the C program, on purpose:
  * the search branches on the LOWEST uncovered time (the C program takes the time with
    the fewest available classes), so the search tree is a different one;
  * supports are canonicalised by an integer comparison over the member-inverse units,
    multisets by sorted tuples; nothing is shared with the C code.

Standard library only.  Reads the C program's orbit file, writes nothing.
Usage:  python3 pt004_l3c_level1_check.py P K ORBITFILE        exit code 0 if identical
"""
import sys
from itertools import combinations


def main():
    p, k, fname = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    n = (p - 1) // 2
    fold = lambda x: min(x % p, p - x % p)
    full = (1 << n) - 1
    cover = [0] * (n + 1)                       # cover[v]: bit a-1 set if v covers time a
    covby = [[] for _ in range(n + 1)]          # covby[a]: classes covering time a
    for v in range(1, n + 1):
        for a in range(1, n + 1):
            if (k + 1) * fold(a * v) < p:
                cover[v] |= 1 << (a - 1)
                covby[a].append(v)
    m = bin(cover[1]).count("1")
    mul = [[fold(u * x) for x in range(n + 1)] for u in range(n + 1)]
    inv = [0] * (n + 1)
    for u in range(1, n + 1):
        for x in range(1, n + 1):
            if mul[u][x] == 1:
                inv[u] = x

    # ---- every covering set of distinct classes that contains class 1, size <= k ----
    found = []

    def extend(S, free, idx, slots):
        found.append(S)
        if slots:
            for i in range(idx, len(free)):
                extend(S | (1 << (free[i] - 1)), free, i + 1, slots - 1)

    def rec(depth, covered, excl, chosen):
        if covered == full:
            free = [c for c in range(1, n + 1)
                    if not (excl >> (c - 1)) & 1 and not (chosen >> (c - 1)) & 1]
            extend(chosen, free, 0, k - depth)
            return
        if depth == k:
            return
        unc = full & ~covered
        if (k - depth) * m < bin(unc).count("1"):
            return
        a = (unc & -unc).bit_length()           # the lowest uncovered time
        e = excl
        for c in covby[a]:
            if (excl >> (c - 1)) & 1:
                continue
            rec(depth + 1, covered | cover[c], e, chosen | (1 << (c - 1)))
            e |= 1 << (c - 1)

    if m:
        rec(1, cover[1], 0, 1)
    by_size = {}
    for S in found:
        s = bin(S).count("1")
        by_size[s] = by_size.get(s, 0) + 1
    print(f"p={p} k={k}: covering sets with at most {k} classes that contain class 1: {len(found)}")
    for s in sorted(by_size):
        print(f"  size {s}: {by_size[s]}")
    if len(set(found)) != len(found):
        print("  ERROR: a set was produced twice")
        return 1

    # ---- canonical supports: class c gets weight 2^(n-c), so the lexicographically
    #      smallest sorted tuple is the set with the LARGEST weight ----
    weight = [0] + [1 << (n - c) for c in range(1, n + 1)]
    supports = set()
    for S in found:
        cls = [c for c in range(1, n + 1) if (S >> (c - 1)) & 1]
        best = 0
        for c in cls:
            row = mul[inv[c]]
            w = 0
            for x in cls:
                w += weight[row[x]]
            if w > best:
                best = w
        supports.add(best)
    print(f"  unit orbits of covering sets: {len(supports)}")

    # ---- all k-multisets on each canonical support, canonicalised as sorted tuples ----
    orbits = set()
    for w in supports:
        cls = [c for c in range(1, n + 1) if w & weight[c]]
        s = len(cls)
        for bars in combinations(range(1, k), s - 1):
            cuts = (0,) + bars + (k,)
            multi = []
            for i in range(s):
                multi += [cls[i]] * (cuts[i + 1] - cuts[i])
            best = tuple(multi)
            for c in cls:
                row = mul[inv[c]]
                t = tuple(sorted(row[x] for x in multi))
                if t < best:
                    best = t
            orbits.add(best)
    mine = sorted(orbits)
    print(f"  unit orbits of covering {k}-multisets (this script): {len(mine)}")

    theirs = [tuple(int(x) for x in ln.split()) for ln in open(fname)]
    print(f"  rows in {fname}: {len(theirs)}")
    same = (mine == theirs)
    print(f"RESULT: {'the two lists are identical, row for row' if same else 'THE LISTS DIFFER'}")
    return 0 if same else 1


if __name__ == "__main__":
    sys.exit(main())
