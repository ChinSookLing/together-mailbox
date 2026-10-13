from math import gcd, ceil
p=37
W16=[112,2,336,448,5,80,192,8,416,528,48,160,13,236,16]
def covint(u,N):
    m=0
    for t in range(1,N//2+1):
        r=(t*u)%N
        if 16*min(r,N-r)<N: m|=1<<t
    return m
def L(D,w): return sum(gcd(D,x)*ceil((D//gcd(D,x))/8) for x in w if x%D)
def l7(w,M):
    for D in range(2,M+1,2):
        if M%D==0 and len([x for x in w if x%D])>=2 and L(D,w)<D: return D
    return None
def children(w,M):
    N=2*M; full=(1<<(N//2+1))-2
    cv=[(covint(x,N),covint(x+M,N)) for x in w]
    out=[]
    for mask in range(1<<15):
        c=0;ww=[]
        for i in range(15):
            b=(mask>>i)&1;c|=cv[i][b];ww.append(w[i]+b*M)
        if c==full and sum(x%2 for x in ww)>=2: out.append(ww)
    return out
c32=children(W16,16*p); f32=[w for w in c32 if l7(w,32*p) is None]
print("32p children",len(c32),"fail",len(f32))
tot=0;fail=0;Ds={}
for w in f32:
    for g in children(w,32*p):
        tot+=1;d=l7(g,64*p)
        if d is None: fail+=1
        else: Ds[d]=Ds.get(d,0)+1
print("64p descendants",tot,"fail L7",fail,"closing D counts",Ds)
