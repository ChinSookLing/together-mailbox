#!/usr/bin/env python3
"""
TOGETHER - PROOF TABLE 004 - Round 3 - Turn 11 - item L3-C, stage 1
Seat: Fable-A (testing seat).

Tests of the C program pt004_l3c on tiny cases, against a brute-force oracle that
follows Definition 2.1 of arXiv:2609.02604v2 word by word.

  Z_{p,l} = residues mod p*l not divisible by p.
  v in Z_{p,l}^k is (k,p,l)-proper if
    (a) for some i, gcd(l, v_1, .., v_i omitted, .., v_k) > 1, or
    (b) for some t in (l*p)^(-1) Z, ||t*v_i|| >= 1/(k+1) for every i.
  I(k,p,l) = the vectors for which neither holds.

The oracle looks at EVERY vector of Z_{p,l}^k and EVERY time j/(l*p), j = 0 .. l*p - 1.
It uses no folding, no orbits, no covers and no lifting.

What is compared, for each tiny case (k, p, L):
  * |I(k,p,L)| counted by the oracle, against the C program's total, for every way of
    writing L as an ordered product of lift factors (for example 12 = 2*2*3 = 3*4 = 12);
  * at level one, the set of unit orbits (the oracle folds and canonicalises each
    improper vector itself, trying all units).
The C program also computes every lift twice (with and without its counting bound)
and stops with an error if the two differ.

Standard library only.  Runs ./pt004_l3c (must be built first).  Writes no file.
Usage:  python3 pt004_l3c_tests.py           exit code 0 if every test passed
"""
import itertools
import subprocess
import sys
from math import gcd

BINARY = "./pt004_l3c"


def dist(x, m):
    r = x % m
    return min(r, m - r)


def improper_literal(v, k, p, l):
    """Definition 2.1, literally."""
    lp = l * p
    for i in range(k):                       # alternative (a)
        g = l
        for j in range(k):
            if j != i:
                g = gcd(g, v[j])
        if g > 1:
            return False
    for j in range(lp):                      # alternative (b): t = j/(l*p)
        if all((k + 1) * dist(j * x, lp) >= lp for x in v):
            return False
    return True


def oracle(k, p, l, literal=False):
    """All improper vectors of Z_{p,l}^k.  Returns (count, set of level-one orbits)."""
    lp = l * p
    residues = [x for x in range(lp) if x % p]
    full = (1 << lp) - 1
    blocked = {}                             # blocked[x]: bit j set if x blocks time j/(lp)
    for x in residues:
        mask = 0
        for j in range(lp):
            if (k + 1) * dist(j * x, lp) < lp:
                mask |= 1 << j
        blocked[x] = mask
    n = (p - 1) // 2
    count = 0
    orbits = set()
    for v in itertools.product(residues, repeat=k):
        if literal:
            bad = improper_literal(v, k, p, l)
        else:
            m = 0
            for x in v:
                m |= blocked[x]
            bad = (m == full)                # no witness at all
            if bad:                          # then test alternative (a)
                for i in range(k):
                    g = l
                    for j in range(k):
                        if j != i:
                            g = gcd(g, v[j])
                    if g > 1:
                        bad = False
                        break
        if bad:
            count += 1
            if l == 1:
                folded = [dist(x, p) for x in v]
                orbits.add(min(tuple(sorted(dist(u * x, p) for x in folded))
                               for u in range(1, n + 1)))
    return count, orbits


def routes(L):
    """All ways to write L as an ordered product of factors >= 2 (the empty product for 1)."""
    if L == 1:
        return [[]]
    out = []
    for c in range(2, L + 1):
        if L % c == 0 and c <= 16:
            out.extend([c] + rest for rest in routes(L // c))
    return out


def run_c(p, k, route):
    args = [BINARY, "tiny", str(p), str(k)] + ([",".join(map(str, route))] if route else [])
    res = subprocess.run(args, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} failed: {res.stderr.strip()}")
    lines = res.stdout.strip().split("\n")
    totals = {}
    for field in lines[0].split():
        if field.startswith("L") and "=" in field:
            name, value = field.split("=")
            totals[int(name[1:])] = int(value)
    orbits = {tuple(int(x) for x in ln.split()[1:]) for ln in lines[1:] if ln.startswith("ORBIT")}
    return totals, orbits


def main():
    ok = True

    print("STAGE 1a: cases worked out by hand (see the report), oracle and C program")
    hand = [
        # (k, p, l, expected |I(k,p,l)|, comment)
        (1, 5, 1, 4, "k=1: no time j/p reaches 1/2, so all 4 vectors are improper"),
        (1, 5, 2, 0, "k=1, level 2: w odd has the witness t=1/2; w even: gcd(2, nothing)=2"),
        (2, 5, 1, 8, "classes {1,2}: 1 covers time 1, 2 covers time 2; only {1,2} covers; 1*2!*2^2"),
        (2, 5, 2, 0, "lifts of (1,2): (1,2),(6,2),(6,7) by gcd; (1,7) has witness t=1/2"),
        (2, 7, 1, 24, "covers are {1,2},{1,3},{2,3}: 3*2!*2^2"),
    ]
    for k, p, l, expected, comment in hand:
        lit, _ = oracle(k, p, l, literal=True)
        fast, _ = oracle(k, p, l)
        c_tot, _ = run_c(p, k, [l] if l > 1 else [])
        good = (lit == expected == fast == c_tot[l])
        ok = ok and good
        print(f"  k={k} p={p} l={l}: by hand {expected}, literal oracle {lit}, oracle {fast}, "
              f"C {c_tot[l]}  {'OK' if good else 'FAIL'}   ({comment})")

    print("STAGE 1b: the fast oracle against the literal oracle (definition word by word)")
    cases_lit = [(2, 5, 4), (2, 7, 2), (2, 7, 3), (2, 11, 2), (3, 7, 2), (3, 11, 1), (3, 13, 2), (4, 11, 1)]
    for k, p, l in cases_lit:
        a, _ = oracle(k, p, l, literal=True)
        b, _ = oracle(k, p, l)
        good = (a == b)
        ok = ok and good
        print(f"  k={k} p={p} l={l}: literal {a}, fast {b}  {'OK' if good else 'FAIL'}")

    print("STAGE 1c: C program against the oracle, every level and every lift route")
    grid = []
    for p in (3, 5, 7):
        grid += [(1, p, L) for L in (1, 2, 3, 4, 6)]
    for p in (5, 7, 11, 13):
        grid += [(2, p, L) for L in (1, 2, 3, 4, 6, 8, 9, 12)]
    for p in (7, 11, 13, 17):
        grid += [(3, p, L) for L in (1, 2, 3, 4, 6, 8)]
    for p in (11, 13):
        grid += [(4, p, L) for L in (1, 2, 3, 4)]
    grid += [(4, 17, 1), (4, 17, 2), (4, 19, 1), (4, 19, 2)]
    grid += [(5, 11, 1), (5, 11, 2), (5, 13, 1), (5, 13, 2), (5, 17, 1), (6, 17, 1)]
    tested = routes_tested = nonzero = 0
    for k, p, L in grid:
        count, orbits = oracle(k, p, L)
        tested += 1
        nonzero += count > 0
        details = []
        good = True
        for route in routes(L):
            totals, c_orbits = run_c(p, k, route)
            routes_tested += 1
            if totals.get(L) != count:
                good = False
                details.append(f"route {route}: C says {totals.get(L)}")
            if L == 1 and c_orbits != orbits:
                good = False
                details.append(f"orbit sets differ: oracle {sorted(orbits)}, C {sorted(c_orbits)}")
        ok = ok and good
        extra = f"  level-one orbits {len(orbits)}" if L == 1 else ""
        print(f"  k={k} p={p:2d} L={L:2d}: |I| = {count:8d}  routes {len(routes(L)):2d}{extra}  "
              f"{'OK' if good else 'FAIL ' + '; '.join(details)}")
    print(f"  cases: {tested}, of which with |I| > 0: {nonzero}; lift routes run: {routes_tested}")
    print(f"RESULT: {'all tests passed' if ok else 'A TEST FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
