# TEST (Opus) of Kimi turn 15 (PT005), p=239, K=15, one generation job.
# Ground truth: the author's cascade (cascade_k15p filter) SURVIVOR lines at level 2; cross-checked here by exact
# enumeration of all 2^15 lifts for every survivor and a sample of dying rows.
import sys, random, itertools
import numpy as np
P = 239; K = 15; TWO_P = 2 * P
rows_file, casc_out = sys.argv[1], sys.argv[2]
rows = [tuple(int(h[2*i:2*i+2], 16) for i in range(K)) for h in open(rows_file).read().split()]
surv = set()
for l in open(casc_out):
    if l.startswith("SURVIVOR base:"):
        surv.add(tuple(sorted(int(x) for x in l.split("base:")[1].split("l2=")[0].split())))
rowset = set(tuple(sorted(r)) for r in rows)
print("rows", len(rows), "survivors", len(surv), "survivors found among rows", len(surv & rowset))
def dp(x, m): x %= m; return min(x, m - x)
def covers1(a0, v): return 16 * dp(a0 * v, P) < P                     # level-1 cover, a0 in 1..p-1
def wit2(a, w): return 8 * dp(a * w, TWO_P) >= P                       # ||a*w/(2p)|| >= 1/16, exact
def E(a, v): return tuple(e for e in (0, 1) if wit2(a, v + e * P))     # allowed lift bits at odd time a
ODD = [a for a in range(1, TWO_P) if a % 2 == 1]                       # all odd level-2 time numerators (incl. a=p)
EPS = np.arange(1 << K, dtype=np.int64)
def dies_level2(r):
    # exact: every lift eps has a witness among odd a (even a = level-1 times, never witnesses) or <=1 odd coordinate
    covered = np.zeros(1 << K, dtype=bool)
    par = np.zeros(1 << K, dtype=np.int64)
    for i, v in enumerate(r):
        bit = (EPS >> i) & 1
        par += (v + bit) % 2
    covered |= par <= 1
    for a in ODD:
        fixed = 0; val = 0; ok = True
        for i, v in enumerate(r):
            e = E(a, v)
            if len(e) == 0: ok = False; break
            if len(e) == 1: fixed |= 1 << i; val |= e[0] << i
        if ok: covered |= (EPS & fixed) == val
    return bool(covered.all())
def odd_rep(a0): return a0 if a0 % 2 else a0 + P
# --- Kimi's Lemma B, literal (level-1 privacy, bit = floor(a*v/p) mod 2) ---
def kimi_literal(r):
    for i, v in enumerate(r):
        bits = set()
        for a0 in range(1, P):
            if covers1(a0, v) and not any(covers1(a0, u) for j, u in enumerate(r) if j != i):
                a = odd_rep(a0); bits.add((a * v // P) % 2)
        if len(bits) == 2: return True
    return False
# --- bit fixed only: level-1 privacy, but the true witness bit from Lemma A ---
def bitfix_only(r):
    for i, v in enumerate(r):
        bits = set()
        for a0 in range(1, P):
            if covers1(a0, v) and not any(covers1(a0, u) for j, u in enumerate(r) if j != i):
                e = E(odd_rep(a0), v); assert len(e) == 1; bits.add(e[0])
        if len(bits) == 2: return True
    return False
# --- corrected: true witness bit, and every other speed allows BOTH bits at that time (8*d_p >= p) ---
def corrected(r):
    for i, v in enumerate(r):
        bits = set()
        for a in ODD:
            e = E(a, v)
            if len(e) == 1 and all(len(E(a, u)) == 2 for j, u in enumerate(r) if j != i): bits.add(e[0])
        if len(bits) == 2: return True
    return False
# Lemma A check over all v, all covered a0
bad = sum(1 for v in range(1, P) for a0 in range(1, P) if covers1(a0, v) and len(E(odd_rep(a0), v)) != 1)
print("Lemma A (singleton) violations over all v, covered a0:", bad)
flo = sum(1 for v in range(1, P) for a0 in range(1, P) if covers1(a0, v) and E(odd_rep(a0), v)[0] != (odd_rep(a0) * v // P) % 2)
tot = sum(1 for v in range(1, P) for a0 in range(1, P) if covers1(a0, v))
print(f"forced bit != floor(a*v/p) mod 2 in {flo} of {tot} covered pairs")
random.seed(20261004)
S = sorted(surv & rowset); D = random.sample([r for r in map(lambda r: tuple(sorted(r)), rows) if r not in surv], 2000)
for name, f in (("kimi_literal", kimi_literal), ("bitfix_only", bitfix_only), ("corrected", corrected)):
    ks = sum(f(r) for r in S); kd = sum(f(r) for r in D)
    print(f"{name}: marks {ks}/{len(S)} survivors (must be 0), {kd}/{len(D)} sampled dying rows")
ex_s = sum(dies_level2(r) for r in S[:200]); ex_d = sum(dies_level2(r) for r in D[:200])
print(f"exact enumeration check: survivors that die by enumeration {ex_s}/{min(200,len(S))} (must be 0); dying rows confirmed {ex_d}/{min(200,len(D))} (must be all)")
