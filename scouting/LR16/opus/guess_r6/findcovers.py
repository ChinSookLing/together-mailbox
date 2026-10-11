# Random-restart local search for 14-covers at prime p; for each cover found,
# compute core capacity M15 = max over units u of #{v: min(uv mod p) <= 15}.
import random, sys
p=int(sys.argv[1]); trials=int(sys.argv[2]); seed=int(sys.argv[3]); random.seed(seed)
n=(p-1)//2; f=lambda x:min(x%p,p-x%p)
C=[None]+[frozenset(t for t in range(1,n+1) if 16*f(v*t)<p) for v in range(1,n+1)]
def cnt(S):
    c=[0]*(n+1)
    for v in S:
        for t in C[v]: c[t]+=1
    return c
def search():
    S=random.sample(range(1,n+1),14); c=cnt(S)
    unc=sum(1 for t in range(1,n+1) if c[t]==0)
    for it in range(4000):
        if unc==0: return sorted(S)
        holes=[t for t in range(1,n+1) if c[t]==0]; t0=random.choice(holes)
        best=None
        for vin in random.sample([v for v in range(1,n+1) if t0 in C[v] and v not in S], min(8,len([v for v in range(1,n+1) if t0 in C[v] and v not in S]))):
            for vout in S:
                d=0
                for t in C[vout]:
                    if c[t]==1 and t not in C[vin]: d+=1
                for t in C[vin]:
                    if c[t]==0 or (c[t]==1 and t in C[vout]): d-= (1 if c[t]==0 else 0)
                if best is None or d<best[0] or (d==best[0] and random.random()<.3): best=(d,vin,vout)
        d,vin,vout=best
        if d<=0 or random.random()<0.1:
            S.remove(vout); S.append(vin)
            for t in C[vout]: c[t]-=1
            for t in C[vin]: c[t]+=1
            unc=sum(1 for t in range(1,n+1) if c[t]==0)
    return None
def canon(S):
    best=None
    for u in range(1,n+1):
        T=tuple(sorted(f(u*v) for v in S))
        if best is None or T<best: best=T
    return best
def M15(S): return max(sum(1 for v in S if f(u*v)<=15) for u in range(1,n+1))
seen={}
for i in range(trials):
    S=search()
    if S:
        k=canon(S)
        if k not in seen:
            seen[k]=M15(S); print('cover',i,seen[k],k,flush=True)
from collections import Counter
print(p,'distinct covers',len(seen),'M15 histogram',sorted(Counter(seen.values()).items()))
for k,m in seen.items():
    if m<=4: print('low core',m,k)
