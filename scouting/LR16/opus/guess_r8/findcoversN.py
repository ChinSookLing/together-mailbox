# Random-restart local search for (N-2)-covers at prime p with threshold 1/N:
# speed v is too near at cell t iff N*min(vt mod p, p - vt mod p) < p.
import random, sys, time
p=int(sys.argv[1]); N=int(sys.argv[2]); trials=int(sys.argv[3]); seed=int(sys.argv[4]); budget=float(sys.argv[5]) if len(sys.argv)>5 else 1e9
random.seed(seed); k=N-2; n=(p-1)//2; f=lambda x:min(x%p,p-x%p)
C=[None]+[frozenset(t for t in range(1,n+1) if N*f(v*t)<p) for v in range(1,n+1)]
cand={t:[v for v in range(1,n+1) if t in C[v]] for t in range(1,n+1)}
def search():
    S=random.sample(range(1,n+1),k); c=[0]*(n+1)
    for v in S:
        for t in C[v]: c[t]+=1
    unc=sum(1 for t in range(1,n+1) if c[t]==0)
    for it in range(6000):
        if unc==0: return sorted(S)
        holes=[t for t in range(1,n+1) if c[t]==0]; t0=random.choice(holes)
        pool=[v for v in cand[t0] if v not in S]; best=None
        for vin in random.sample(pool,min(8,len(pool))):
            for vout in S:
                lost=sum(1 for t in C[vout] if c[t]==1 and t not in C[vin])
                gain=sum(1 for t in C[vin] if c[t]==0)
                d=lost-gain
                if best is None or d<best[0] or (d==best[0] and random.random()<.3): best=(d,vin,vout)
        d,vin,vout=best
        if d<=0 or random.random()<0.1:
            S.remove(vout); S.append(vin)
            for t in C[vout]: c[t]-=1
            for t in C[vin]: c[t]+=1
            unc=sum(1 for t in range(1,n+1) if c[t]==0)
    return None
def canon(S): return min(tuple(sorted(f(u*v) for v in S)) for u in range(1,n+1))
seen=set(); t0=time.time()
for i in range(trials):
    if time.time()-t0>budget: break
    S=search()
    if S:
        key=canon(S)
        if key not in seen: seen.add(key); print('cover',p,N,i,key,flush=True)
print('done',p,N,'restarts',i+1,'distinct',len(seen),'secs',round(time.time()-t0),flush=True)
