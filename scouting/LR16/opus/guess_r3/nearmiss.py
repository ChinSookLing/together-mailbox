# Heuristic (NOT a proof): 13 speeds (incl. speed 1, allowed by scaling) leaving as few uncovered cells as possible.
# Local search with swap moves and random restarts. Output = an upper bound on u13(p) = min uncovered cells.
import sys, random, time
p=int(sys.argv[1]); K=int(sys.argv[2]); secs=float(sys.argv[3]); seed=int(sys.argv[4]) if len(sys.argv)>4 else 1
n=(p-1)//2; rnd=random.Random(seed)
cov=[0]*(n+1)
for v in range(1,n+1):
    m=0
    for t in range(1,n+1):
        r=v*t%p
        if 16*min(r,p-r)<p: m|=1<<t
    cov[v]=m
ALL=sum(1<<t for t in range(1,n+1))
def unc(S):
    m=0
    for v in S: m|=cov[v]
    return bin(ALL&~m).count("1")
best=(10**9,None); t0=time.time()
while time.time()-t0<secs:
    S=[1]+rnd.sample(range(2,n+1),K-1); cur=unc(S)
    improved=True
    while improved and time.time()-t0<secs:
        improved=False
        for i in rnd.sample(range(1,K),K-1):
            others=0
            for j,v in enumerate(S):
                if j!=i: others|=cov[v]
            hole=ALL&~others
            # best replacement for slot i
            bv,bu=None,cur
            for w in range(2,n+1):
                if w in S: continue
                u=bin(hole&~cov[w]).count("1")
                if u<bu: bv,bu=w,u
            if bv is not None:
                S[i]=bv; cur=bu; improved=True
    if cur<best[0]:
        best=(cur,sorted(S))
        if cur==0: break
m=0
for v in best[1]: m|=cov[v]
holes=[t for t in range(1,n+1) if not (m>>t)&1]
print(f"p={p} K={K} best_uncovered={best[0]} speeds={best[1]} holes={holes} secs={time.time()-t0:.0f}")
