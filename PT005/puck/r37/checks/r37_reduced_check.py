#!/usr/bin/env python3
"""PT005 R37 cross-check (Puck): recompute Hesper's reduced-data rows from send_R37.txt.
Reduced tuple per coordinate: (w mod 64, m mod 32, sgn d, c, v)
  d = bal_p(b*w), m = (b*w - d)/p, v = w^-1 mod 32, c = -2*m*v mod 32.
Also: exact k=5 tiling check of C5(b), level-6 doublability (brute force over 2^8 lifts),
and XOR-graph degrees (one edge per level-6 member covered by two different coordinates).
"""
from fractions import Fraction
from itertools import product
from collections import defaultdict

EX = [
 (29, 1, (3,97,125,151,413,191,285,385),
  [(3,0,'+',0,11),(33,3,'+',26,1),(61,4,'+',24,21),(23,5,'+',26,7),(29,14,'+',20,21),(63,7,'-',14,31),(29,10,'-',28,21),(1,13,'+',6,1)],
  [3,2,3,4,3,4,3,4]),
 (79, 76, (865,993,675,289,385,579,545,673),
  [(33,0,'+',0,1),(33,27,'+',10,1),(35,9,'+',26,11),(33,22,'+',20,1),(1,18,'+',28,1),(3,13,'+',2,11),(33,12,'+',8,1),(33,7,'+',18,1)],
  [2,2,3,2,2,3,2,2]),
 (89, 36, (1345,545,1089,129,673,587,139,1035),
  [(1,0,'+',0,1),(33,28,'+',8,1),(1,24,'+',16,1),(1,20,'+',24,1),(33,16,'+',0,1),(11,13,'+',18,3),(11,24,'+',16,3),(11,3,'-',14,3)],
  [1,3,3,3,1,3,3,3]),
]

def bal(x, p):
    r = x % p
    return r - p if r > p // 2 else r

def reduced(p, b, w):
    d = bal(b * w, p); m = (b * w - d) // p
    v = pow(w, -1, 32); c = (-2 * m * v) % 32
    sgn = '+' if d > 0 else ('-' if d < 0 else '0')
    return (w % 64, m % 32, sgn, c, v), d, m

def covers(t, w, N):  # 16*||t w / N|| < 1
    r = (t * w) % N
    return 16 * min(r, N - r) < N

def members(p, r, top):
    return [t for t in range(1, top + 1, 2) if t % p in (r % p, (-r) % p)]

for p, b, W, claim, claim_deg in EX:
    print(f"=== p={p} b={b} W={W}")
    allok = True
    for i, (w, cl) in enumerate(zip(W, claim)):
        got, d, m = reduced(p, b, w)
        ok = got == cl; allok &= ok
        print(f"  w={w:5d} d={d:4d} m={m:4d}  computed={got}  hesper={cl}  {'MATCH' if ok else 'MISMATCH'}")
        legal = w % 2 == 1 and 1 <= w < 16 * p and w % p not in (0, 1, p - 1)
        if not legal: print(f"    !! w={w} not a legal coordinate")
    print(f"  reduced rows: {'ALL MATCH' if allok else 'MISMATCH PRESENT'}")
    # k=5 tiling
    N5 = 32 * p; C5 = members(p, b, 16 * p)
    cnt = [sum(covers(t, w, N5) for w in W) for t in C5]
    print(f"  k=5: |C5(b)|={len(C5)}  exact tiling: {all(c == 1 for c in cnt)}  (coverage counts {sorted(set(cnt))})")
    print(f"  w mod 8 classes: {[w % 8 for w in W]}  mixed={len({min(w%8, (-w)%8) for w in W})>1}")
    # level 6
    N6 = 64 * p; C6 = members(p, 2 * b, 32 * p)
    lifts = [(w, w + 32 * p) for w in W]
    cov = defaultdict(list)  # t -> list of (coord, lift)
    for i, (l0, l1) in enumerate(lifts):
        for a, L in enumerate((l0, l1)):
            for t in C6:
                if covers(t, L, N6): cov[t].append((i, a))
    sols = []
    for choice in product((0, 1), repeat=8):
        cc = defaultdict(int)
        for i, a in enumerate(choice):
            for t in C6:
                if covers(t, lifts[i][a], N6): cc[t] += 1
        if all(cc[t] == 1 for t in C6): sols.append(choice)
    print(f"  k=6: |C6(2b)|={len(C6)}  doublable={bool(sols)}  #lift choices={len(sols)} {sols[:4]}")
    # XOR graph: edge per member covered by two distinct coordinates
    deg = [0] * 8; bad = []
    for t in C6:
        coords = sorted({i for i, a in cov[t]})
        if len(cov[t]) != 2 or len(coords) != 2:
            bad.append((t, cov[t])); continue
        deg[coords[0]] += 1; deg[coords[1]] += 1
    loops = [x for x in bad if len({i for i, a in x[1]}) == 1 and len(x[1]) == 2]
    other = [x for x in bad if x not in loops]
    print(f"  XOR degrees (edge per shared member, loops excluded): {deg}  hesper={claim_deg}  {'MATCH' if deg == claim_deg else 'MISMATCH'}")
    print(f"    self-members (same coord both lifts): {len(loops)}; irregular coverage: {other}")
    print()

# --- Alternative XOR-degree readings (to compare with Hesper's degree lists) ---
print("=== XOR degree interpretations")
for p, b, W, claim, claim_deg in EX:
    N6 = 64 * p; C6 = members(p, 2 * b, 32 * p)
    lifts = [(w, w + 32 * p) for w in W]
    mult = defaultdict(int)
    for t in C6:
        cs = [(i, a) for i in range(8) for a in (0, 1) if covers(t, lifts[i][a], N6)]
        (i, a), (j, c) = cs
        mult[(min(i, j), max(i, j))] += 1
    simple = [sum(1 for e in mult if k in e) for k in range(8)]
    print(f"p={p}: multigraph deg={[sum(m for e,m in mult.items() if k in e) for k in range(8)]}  simple deg={simple}  hesper={claim_deg}  simple {'MATCH' if simple == claim_deg else 'MISMATCH'}")
    print(f"   edge multiplicities: {dict(sorted(mult.items()))}")
    # L1 footprint check: positions s = eps*u mod 32 covered by coordinate i, vs c+{+-v,+-3v}
    l1ok = True
    for i, w in enumerate(W):
        (_, _, _, c, v), d, m = reduced(p, b, w)
        pos = set()
        for t in C6:
            if covers(t, w, N6) or covers(t, w + 32 * p, N6):
                for eps in (1, -1):
                    if (t - eps * 2 * b) % p == 0:
                        u = (t - eps * 2 * b) // p; pos.add((eps * u) % 32)
        exp = {(c + s * v) % 32 for s in (1, -1, 3, -3)}
        if pos != exp: l1ok = False; print(f"   L1 mismatch coord {i}: got {sorted(pos)} expected {sorted(exp)}")
    print(f"   L1 footprint c+{{+-v,+-3v}} check: {'OK' if l1ok else 'FAIL'}")
