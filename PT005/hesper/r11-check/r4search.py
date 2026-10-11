import numpy as np, math, random, sys, json
def setup(p,K=4):
    H=(p-1)//16
    def bh(k):
        if k==0: return 1-(2*H+1)/p
        return -(1/p)*math.sin(math.pi*(2*H+1)*k/p)/math.sin(math.pi*k/p)
    x=np.arange(p)
    f=sum(bh(k)*np.cos(2*np.pi*k*x/p) for k in range(-K,K+1))
    M=p/2*bh(0)**14
    T=np.array([[ (v*t)%p for t in range(p)] for v in range(p)])
    L=np.log(np.abs(f).astype(complex)+0j) # unused
    F=f[T]  # F[v,t]
    return F,M
def R(F,M,S): return 0.5*np.prod(F[S],axis=0).sum()-M
def anneal(p,iters=20000,seed=0,F=None,M=None):
    rng=random.Random(seed); n=(p-1)//2
    S=rng.sample(range(1,n+1),14); cur=R(F,M,S); best=(cur,sorted(S))
    for i in range(iters):
        T=1.0*(1-i/iters)+0.01
        j=rng.randrange(14); v=rng.randrange(1,n+1)
        if v in S: continue
        S2=S[:]; S2[j]=v; r=R(F,M,S2)
        if r<cur or rng.random()<math.exp((cur-r)/T):
            S,cur=S2,r
            if cur<best[0]: best=(cur,sorted(S))
    return best
p=int(sys.argv[1]); F,M=setup(p)
res=[anneal(p,30000,s,F,M) for s in range(int(sys.argv[2]))]
res.sort()
print(json.dumps({"p":p,"M":M,"best":[(round(r,4),S) for r,S in res[:5]]}))
