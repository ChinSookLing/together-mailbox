import numpy as np, math, itertools, sys
def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c
def covered_all(w,M):
    T=np.arange(1,M//2+1)
    cov=np.zeros(len(T),bool)
    for x in w:
        r=(T*x)%M; d=np.minimum(r,M-r); cov|=16*d<M
    return cov.all()
def l7_closed(w,M):
    for D in range(2,M+1,2):
        if M%D: continue
        E=[x for x in w if x%D]
        if len(E)<2: continue
        s=sum(math.gcd(D,x)*(-(-(D//math.gcd(D,x))//8)) for x in E)
        if s<D: return True
    return False
def is_open(w,M):
    return sum(x%2 for x in w)>=2 and covered_all(w,M) and not l7_closed(w,M)
def F(w,M,j):
    k=v2(M//p) if False else None
def Fj(w,M,p,j):
    k=v2(M//p) if (M//p)>0 else 0
    k=int(round(math.log2(M//p)))
    c=0
    for x in w:
        v=v2(x)
        d=k-v if v<k else 0
        if d>=j: c+=1
    return c
def open_children(w,M,limit=None):
    w=list(w); res=[]
    # vectorised coverage over all 2^15 lifts
    n=len(w); M2=2*M
    T=np.arange(1,M2//2+1)
    bits=((np.arange(1<<n)[:,None]>>np.arange(n))&1).astype(np.int64)
    W=np.array(w)[None,:]+bits*M  # (32768,15)
    ok=np.ones(1<<n,bool)
    # odd count
    ok&=(W%2).sum(1)>=2
    covall=np.ones(1<<n,bool)
    for t in T:
        r=(W*t)%M2; d=np.minimum(r,M2-r)
        covall&=(16*d<M2).any(1)
    ok&=covall
    for idx in np.nonzero(ok)[0]:
        c=list(map(int,W[idx]))
        if not l7_closed(c,M2): res.append(c)
    return res
