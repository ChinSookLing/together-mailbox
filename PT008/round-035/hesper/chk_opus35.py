from fractions import Fraction as F
from itertools import combinations
from math import gcd, ceil
from functools import reduce
def dist(x): return abs(x-round(x))
def argmax(W):
    C=set()
    for i in W:
        for j in W:
            s=i+j
            for k in range(1,s+1): C.add(F(k,s))
    return max(C,key=lambda t:(min(dist(w*t) for w in W),-t))
def primes(n):
    out=[];d=2
    while d*d<=n:
        while n%d==0: out.append(d); n//=d
        d+=1
    if n>1: out.append(n)
    return set(out)
d=F(1,5); tot=modc=descc=cls=0; fails=0; mism=0
for V in combinations(range(1,41),4):
    if reduce(gcd,V)!=1: continue
    tot+=1
    N=next((N for N in (2,3,4,5) if all(v%N for v in V)),None)
    if N:
        modc+=1
        if min(dist(F(v,N)) for v in V)<d: fails+=1
        continue
    ok=False
    for p in sorted(set().union(*[primes(v) for v in V])):
        Vp=[v for v in V if v%p==0]; s=len(Vp)
        if 1<=s<=3 and (4-s)*ceil(F(2*p,5))<p:
            W=[v//p for v in Vp]; y=argmax(W)
            assert min(dist(w*y) for w in W)>=d
            for j in range(p):
                t=(j+y)/p
                if all(dist(v*t)>=d for v in V): ok=True; break
            if ok: break
    if ok: descc+=1; continue
    cls+=1
    m5=sum(v%5==0 for v in V); m4=sum(v%4==0 for v in V); ev=sum(v%2==0 for v in V); m3=sum(v%3==0 for v in V)
    pairs_ok=all(primes(gcd(a,b))<= {2,3} for a,b in combinations(V,2))
    if not (m5==1 and m4>=1 and ev<=2 and m3 in (1,2) and pairs_ok): mism+=1
print("total",tot,"MOD",modc,"DESC",descc,"class",cls,"MODfails",fails,"class-criteria-mismatch",mism)
