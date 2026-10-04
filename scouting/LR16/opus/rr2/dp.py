import math, sys
exec(open('prime_plan.py').read().split("large = [")[0])   # reuse T, x15, TARGET, SMALL_K14, isprime
def dp(target, cands, step=0.01):
    J = math.ceil(target/step); INF = float('inf'); best = [INF]*(J+1); best[0] = 0.0; take = []
    for p in cands:
        v = int(math.log(p)/step); w = T(p); new = best[:]; t = bytearray(J+1)
        for j in range(J+1):
            if best[j] < INF:
                k = min(J, j+v)
                if best[j] + w < new[k]: new[k] = best[j] + w; t[k] = 1
        take.append((p, v, t, best)); best = new
    # backtrack
    j = J; chosen = []
    for p, v, t, prev in reversed(take):
        if t[j]:
            # find predecessor j0 with prev[j0] + T(p) == best value at j
            for j0 in range(max(0, j - v), j + 1):
                if prev[j0] < INF and min(J, j0+v) == j and abs(prev[j0] + T(p) - (best_at := None or 0)) >= 0: pass
            chosen.append(p)
    return best[J]
L = [p for p in range(239, 1000) if isprime(p)]
tS = TARGET - sum(math.log(p) for p in SMALL_K14)
for name, tgt, pool in (("L", TARGET, L), ("S", tS, [p for p in L if p != 241])):
    print(name, f"DP optimum cost {dp(tgt, pool)/3600:,.0f} CPU-h")
