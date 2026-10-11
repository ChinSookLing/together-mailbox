import numpy as np, sys, json, random, time
def C(p):
    n=(p-1)//2; H=(p-1)//16
    t=np.arange(1,n+1); v=np.arange(1,n+1)
    r=(np.outer(v,t))%p; d=np.minimum(r,p-r)
    return n,(d<=H).astype(np.int32)   # cov[v-1,t-1]
def search(p,restarts,iters,seed=0):
    rng=random.Random(seed); n,cov=C(p); best=(10**9,None)
    for r in range(restarts):
        S=rng.sample(range(n),14); cnt=cov[S].sum(0); U=int((cnt==0).sum()); T=1.0
        for it in range(iters):
            i=rng.randrange(14); v=S[i]
            c2=cnt-cov[v]; unc=(c2==0).astype(np.int32)
            gain=cov@unc  # cells newly covered by w
            Unew=int(unc.sum())-gain
            Unew[S]=10**9
            m=Unew.min()
            cands=np.flatnonzero(Unew<=m+ (1 if T>0.3 else 0))
            w=int(rng.choice(list(cands)))
            dU=int(Unew[w])-U
            if dU<=0 or rng.random()<np.exp(-dU/T):
                S[i]=w; cnt=c2+cov[w]; U=int(Unew[w])
            T*=0.999
            if U<best[0]: best=(U,sorted(x+1 for x in S))
            if best[0]==0: break
        if best[0]==0: break
    return best
P=[int(x) for x in sys.argv[1].split(',')]
for p in P:
    if 503<=p<=599: continue
    t=time.time(); b=search(p,int(sys.argv[2]),int(sys.argv[3]))
    n=(p-1)//2;H=(p-1)//16;M=(p/2)*(1-(2*H+1)/p)**14
    print(json.dumps({"p":p,"bestU":b[0],"set":b[1],"M":round(M,3),"s":n-8*H,"sec":round(time.time()-t)}),flush=True)
