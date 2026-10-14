#!/usr/bin/env python3
# PT005 R31 — Puck independent verifier for Astra's claimed counterexample.
# Self-contained: recomputes every property from the R30/R31 definitions only.
# Does NOT import Astra's code or the census helpers.
from collections import defaultdict, deque

p, b = 103, 35
W = [1505, 1481, 143, 263, 227, 1445, 179, 1397]
CLAIM_MOD16 = [1, 9, 15, 7, 3, 5, 3, 5]
CLAIM_CYCLE = [0, 4, 1, 5, 2, 6, 3, 7]
CLAIM_LABELS = [0, 1, 0, 1, 1, 1, 1, 0]
CLAIM_PAIRS = {1505: (35, 241), 1481: (583, 859), 143: (1407, 1613), 263: (789, 1065),
               227: (377, 653), 1445: (171, 447), 179: (995, 1271), 1397: (1201, 1477)}

results = []
def check(name, ok, detail=""):
    results.append((name, ok))
    print(f"[{'MATCH' if ok else 'MISMATCH'}] {name}" + (f" :: {detail}" if detail else ""))

def Nk(k): return (1 << k) * p
def dist(x, n): x %= n; return min(x, n - x)
def covers(t, w, n): return 16 * dist(t * w, n) < n
def Cset(k, bb):
    n = Nk(k); r = {bb % p, (-bb) % p}
    return [t for t in range(1, n // 2 + 1, 2) if t % p in r]

N5, N6 = Nk(5), Nk(6)
print(f"p={p} b={b} N5={N5} N6={N6} N5/2={N5//2}")
print("W =", W)

# 0. p prime, b in range
check("p=103 is prime", p > 1 and all(p % d for d in range(2, int(p**0.5) + 1)))
check("b in 1..(p-1)/2", 1 <= b <= (p - 1) // 2)

# 1. legality
leg = [(w, w % 2 == 1, 1 <= w < N5 // 2, w % p) for w in W]
for w, odd, rng, r in leg:
    print(f"  w={w}: odd={odd} w<N5/2={rng} w mod p={r}")
check("all 8 coordinates legal (odd, 1<=w<N5/2, w mod p not in {0,+-1})",
      all(o and g and r not in (0, 1, p - 1) for _, o, g, r in leg))
check("8 distinct coordinates", len(set(W)) == 8)

# 2. exact tiling of C5(b)
C5 = Cset(5, b)
print(f"|C5({b})| = {len(C5)}")
cov5 = {w: [t for t in C5 if covers(t, w, N5)] for w in W}
for w in W: print(f"  cover5({w}) = {cov5[w]}")
hits5 = {t: sum(covers(t, w, N5) for w in W) for t in C5}
check("exact tiling: every t in C5(b) covered exactly once",
      all(v == 1 for v in hits5.values()), f"hit counts {sorted(set(hits5.values()))}")
check("cover pairs equal Astra's printed certificate",
      all(tuple(cov5[w]) == CLAIM_PAIRS[w] for w in W))

# 3. exact 2-cover of C6(2b) by the 16 lifts w, w+N5 (mod N6)
b2 = (2 * b) % p
C6 = Cset(6, b2)
print(f"2b mod p = {b2}; |C6(2b)| = {len(C6)}")
lift = {(i, e): [t for t in C6 if covers(t, (W[i] + e * N5) % N6, N6)]
        for i in range(8) for e in (0, 1)}
hits6 = defaultdict(list)
for (i, e), ts in lift.items():
    for t in ts: hits6[t].append((i, e))
cnt6 = {t: len(hits6[t]) for t in C6}
check("exact 2-cover: every t in C6(2b) hit exactly twice by the 16 lifts",
      all(v == 2 for v in cnt6.values()), f"hit counts {sorted(set(cnt6.values()))}")
check("no coordinate's two lifts share a member (A0 & A1 empty)",
      all(not (set(lift[(i, 0)]) & set(lift[(i, 1)])) for i in range(8)))
check("no C6 member hit twice by the same coordinate (no self-loops)",
      all(hits6[t][0][0] != hits6[t][1][0] for t in C6 if len(hits6[t]) == 2))

# 4. XOR graph
edges = defaultdict(list)  # (i,j) -> labels
for t in C6:
    (i, a), (j, c) = hits6[t]
    key = (min(i, j), max(i, j))
    edges[key].append(a ^ c ^ 1)
print("XOR edges (i,j): labels per shared C6 member")
for k in sorted(edges): print(f"  {k}: {edges[k]}")
consistent = all(len(set(v)) == 1 for v in edges.values())
check("each edge's labels consistent across its shared members", consistent)
adj = defaultdict(set)
for i, j in edges: adj[i].add(j); adj[j].add(i)
deg2 = all(len(adj[i]) == 2 for i in range(8))
# connectivity
seen = {0}; q = deque([0])
while q:
    x = q.popleft()
    for y in adj[x]:
        if y not in seen: seen.add(y); q.append(y)
check("simple XOR graph is one Hamiltonian 8-cycle (8 edges, all deg 2, connected)",
      len(edges) == 8 and deg2 and len(seen) == 8, f"{len(edges)} edges, deg2={deg2}, comp={len(seen)}")
# walk the cycle from 0
cyc = [0]; prev = None
while len(cyc) < 8:
    x = cyc[-1]
    nxt = sorted(y for y in adj[x] if y != prev and y not in cyc)
    if not nxt: break
    # follow Astra's orientation if possible (0 -> 4 first)
    prev = x; cyc.append(nxt[0])
print("cycle (from 0):", cyc)
cls = lambda w: 'A' if w % 8 in (1, 7) else 'B'
print("classes along cycle:", [cls(W[i]) for i in cyc], "mod8:", [W[i] % 8 for i in cyc])
check("cycle alternates A={1,7} / B={3,5}",
      all(cls(W[cyc[k]]) != cls(W[cyc[(k + 1) % 8]]) for k in range(8)))
rev = [cyc[0]] + cyc[:0:-1]
check("cycle equals Astra's 0->4->1->5->2->6->3->7 (up to direction)",
      cyc == CLAIM_CYCLE or rev == CLAIM_CYCLE)
labs = [edges[(min(cyc[k], cyc[(k+1) % 8]), max(cyc[k], cyc[(k+1) % 8]))][0] for k in range(8)]
print("labels along cycle:", labs)
check("labels along cycle equal Astra's (0,1,0,1,1,1,1,0)", labs == CLAIM_LABELS)
H = sum(labs) % 2
check("H = sum labels = 1 (mod 2) -> XOR system unsolvable", H == 1, f"sum={sum(labs)} H={H}")

# Independent brute-force solvability: x_i in {0,1}, x_i ^ x_j == label for every member-edge
sol = [m for m in range(256)
       if all(((m >> i) & 1) ^ ((m >> j) & 1) == l
              for (i, j), ls in edges.items() for l in ls)]
check("brute force over 2^8 assignments: no solution (not doublable)", len(sol) == 0, f"{len(sol)} solutions")

# 5. mixed + mod16
m8 = [w % 8 for w in W]
check("mixed: both classes present, each odd residue mod 8 exactly twice",
      sorted(m8) == [1, 1, 3, 3, 5, 5, 7, 7], f"mod8={m8}")
m16 = [w % 16 for w in W]
print("W mod 16 =", m16)
check("W mod 16 equals claimed (1,9,15,7,3,5,3,5)", m16 == CLAIM_MOD16)
dup = sorted({r for r in m16 if m16.count(r) > 1})
check("W mod 16 NOT pairwise distinct (lemma counterexample)", len(set(m16)) < 8,
      f"{len(set(m16))} distinct; repeated {dup}")
pos = {i: k for k, i in enumerate(cyc)}
for r in dup:
    idx = [i for i in range(8) if m16[i] == r]
    print(f"  residue {r}: coords {[W[i] for i in idx]} idx {idx} cycle distance {min((pos[idx[0]]-pos[idx[1]])%8,(pos[idx[1]]-pos[idx[0]])%8)}")
# mod 32 (informational, not one of Astra's claims): Grok argued "distinct mod 32 => distinct mod 16".
m32 = [w % 32 for w in W]
print("W mod 32 =", m32, f"({len(set(m32))} distinct)")
print("  INFO: W IS distinct mod 32 yet NOT distinct mod 16 -> Grok's step 'distinct mod 32, therefore distinct mod 16' is a non-sequitur.")

# Side check of GPT's R31 footprint counterexample (p=19, b=1, w=11 vs 203): same w mod 32,
# same sign of bal_p(bw), different s-footprints -> footprint is NOT determined by w mod 32 + sign
# (this also kills Grok's rigidity premise).
def footprint_s(pp, bb, w):
    n5, n6 = 32 * pp, 64 * pp; out = set()
    for s_ in range(1, 64, 2):
        t = 2 * bb + pp * s_
        if t > n6 // 2: break
        for e in (0, 1):
            if 16 * dist(t * (w + e * n5), n6) < n6: out.add(s_ % 32)
    return sorted(out)
bal = lambda x, pp: (x % pp) if (x % pp) <= pp // 2 else (x % pp) - pp
f11, f203 = footprint_s(19, 1, 11), footprint_s(19, 1, 203)
print(f"GPT side check p=19 b=1: w=11 (mod32={11%32}, bal={bal(11,19)}) U={f11}; w=203 (mod32={203%32}, bal={bal(203,19)}) U={f203}")
check("GPT side check: footprints {3,17,23,29} vs {1,7,21,27} as GPT computed (differ despite same w mod 32 and sign)",
      f11 == [3, 17, 23, 29] and f203 == [1, 7, 21, 27])

ok = all(o for _, o in results)
print()
print(f"SUMMARY: {sum(o for _, o in results)}/{len(results)} checks MATCH -> {'MATCH' if ok else 'MISMATCH'}")
