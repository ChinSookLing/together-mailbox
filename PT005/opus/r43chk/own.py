import numpy as np, itertools
from math import gcd
def is_open(w,M):
    w=np.array(w,dtype=np.int64)
    if (w%2).sum()<2: return False
    T=np.arange(1,M//2+1,dtype=np.int64)[:,None]
    r=(T*w[None,:])%M; d=np.minimum(r,M-r)
    if not (16*d<M).any(axis=1).all(): return False
    for D in range(2,M+1,2):
        if M%D: continue
        E=[int(x) for x in w if x%D]
        if len(E)>=2 and sum(gcd(D,x)*(-(-(D//gcd(D,x))//8)) for x in E)<D: return False
    return True
def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c
def fstats(w,M,p):
    k=(M//p).bit_length()-1
    gaps=[k-v2(x) for x in w if v2(x)<k]
    return dict(E=len(gaps),F3=sum(g>=3 for g in gaps),F5=sum(g>=5 for g in gaps))
def open_children(w,M):
    # all 2^15 lifts, vectorised coverage on odd T (even T inherited); then L7 per survivor
    w=np.array(w,dtype=np.int64); N=2*M
    bits=((np.arange(1<<15)[:,None]>>np.arange(15)[None,:])&1).astype(np.int64)
    C=w[None,:]+bits*M
    ok=(C%2).sum(axis=1)>=2
    for T in range(1,N//2+1,2):
        r=(T*C)%N; d=np.minimum(r,N-r)
        ok&=(16*d<N).any(axis=1)
        if not ok.any(): break
    res=[]
    for row in C[ok]:
        if is_open(list(row),N): res.append(sorted(int(x) for x in row))
    uniq=sorted(set(map(tuple,res)))
    return [list(u) for u in uniq]
