# Road Report v2 (Opus): prime selection for 16 runners under the L6 generation-cost model (ESTIMATE).
# T15(p) = exp(-34.17 + 6 log p + 13 x15(p)) CPU-s on the chair's machine (Xeon 2.8 GHz, 1 core), generation only;
# total per large prime taken as 1.10 x T15 (reducible branch + cascade, from p = 239: 278 + small vs 5,751).
import math
def isprime(n): return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
def x15(p): n = (p-1)/2; m = (p-1)//16; return (15*m - n)/n
def T(p): return 1.10 * math.exp(-34.17 + 6*math.log(p) + 13*x15(p))
TARGET = 494.922 - math.log(720720)          # Astra's dual-step bound minus forced divisor
SMALL_K14 = [89,131,149,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,241]   # author's small block (K=14)
def plan(target, cands, step=0.001):
    # 0/1 knapsack: minimise sum T(p) subject to sum log p >= target (DP over value in units of `step`)
    J = math.ceil(target/step); INF = float('inf')
    best = [INF]*(J+1); best[0] = 0.0; choice = [None]*(J+1)
    # dp over items, value capped at J
    import array
    keep = []
    for p in cands:
        v = int(math.log(p)/step); w = T(p); new = best[:]; nc = choice[:]
        for j in range(J, -1, -1):
            if best[j] < INF:
                k = min(J, j + v)
                if best[j] + w < new[k]: new[k] = best[j] + w; nc[k] = (p, j)
        best, choice = new, nc; keep.append(None)
    # backtrack: rebuild via storing chains
    return best[J]
def greedy(target, cands):
    tot = 0; s = 0; used = []
    for p in sorted(cands, key=lambda q: T(q)/math.log(q)):
        if s >= target: break
        used.append(p); s += math.log(p); tot += T(p)
    return tot, sorted(used), s
def consecutive(target, start):
    tot = 0; s = 0; used = []; p = start
    while s < target:
        if isprime(p): used.append(p); s += math.log(p); tot += T(p)
        p += 1
    return tot, used, s
large = [p for p in range(239, 1400) if isprime(p)]
print(f"TARGET sum log p > {TARGET:.3f}")
for name, tgt in (("L  large primes only (p >= 239)", TARGET),
                  ("S  author's 19 small primes also close (sum log 98.82), rest large", TARGET - sum(math.log(p) for p in SMALL_K14))):
    pool = [p for p in large if not (name.startswith("S") and p == 241)]
    c_tot, c_used, c_s = consecutive(tgt, 239 if name.startswith("L") else 239)
    if name.startswith("S"): c_tot, c_used, c_s = consecutive_s = (lambda: None)() or consecutive(tgt, 239)
    g_tot, g_used, g_s = greedy(tgt, pool)
    print(f"\n{name}: need {tgt:.2f}")
    print(f"  consecutive primes from 239: {len(c_used)} primes up to {c_used[-1]}, cost {c_tot/3600:,.0f} CPU-h")
    print(f"  greedy by cost per log p : {len(g_used)} primes up to {max(g_used)}, cost {g_tot/3600:,.0f} CPU-h")
    print(f"  greedy list: {g_used}")
for p in (239, 307, 367, 401, 499, 569, 607, 701, 797, 887):
    print(p, f"x15={x15(p):.3f}", f"T={T(p)/3600:,.1f} CPU-h")
