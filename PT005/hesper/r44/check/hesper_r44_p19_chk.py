import numpy as np, itertools, math, sys
def covered_all(w,M):
    T=np.arange(1,M//2+1)[:,None]; r=(T*np.array(w)[None,:])%M; d=np.minimum(r,M-r)
    return bool((16*d<M).any(1).all())
def improper(w,M): return covered_all(w,M) and sum(x%2 for x in w)>=2
def l7closed(w,M):
    for D in range(2,M+1,2):
        if M%D: continue
        E=[x for x in w if x%D]
        if len(E)>=2:
            s=sum(math.gcd(D,x)*(-(-(D//math.gcd(D,x))//8)) for x in E)
            if s<D: return True
    return False
def is_open(w,M): return improper(w,M) and not l7closed(w,M)
def F(w,M,j):
    k=(M&-M).bit_length()-1
    c=0
    for x in w:
        v=(x&-x).bit_length()-1
        if v<k and k-v>=j: c+=1
    return c
def children_open(w,M):
    # fast: odd T<=M at 2M via bitmask per coordinate per choice
    N=2*M; w=np.array(w); n=len(w)
    T=np.arange(1,M+1)
    out=set()
    masks=[]
    for x in w:
        ms=[]
        for y in (x,x+M):
            r=(T*y)%N; d=np.minimum(r,N-r); ms.append(16*d<N)
        masks.append(ms)
    # parent improper => even T inherited; test all T<=M directly anyway (T<=M=N/2)
    res=[]
    for bits in itertools.product((0,1),repeat=n):
        cov=np.zeros(M,bool)
        for i,b in enumerate(bits): cov|=masks[i][b]
        if cov.all():
            c=tuple(sorted(int(w[i]+M*b) for i,b in enumerate(bits)))
            if c in out: continue
            out.add(c)
            if sum(v%2 for v in c)>=2 and not l7closed(c,N): res.append(c)
    return res
if __name__=="__main__":
    p=19; M=152
    P=[39,59,41,61,43,101,121,8,47,125,145,15,73,55,37]
    print("parent open",is_open(P,M),"odd",sum(x%2 for x in P),"F1",F(P,M,1),"F3",F(P,M,3))
    ch=children_open(P,M); print("open children",len(ch))
    for c in ch:
        print(c,"open",is_open(list(c),2*M),"F3",F(c,2*M,3))
        g=children_open(list(c),2*M); print("  open grandchildren",len(g))
    for c in [(191,59,41,213,195,101,121,160,47,125,145,15,73,207,37),(39,211,193,61,43,253,273,160,199,277,297,167,225,55,189)]:
        print("puck child",sorted(c) in [list(x) for x in ch], "legal",all(a in (b,b+M) for a,b in zip(c,P)))
