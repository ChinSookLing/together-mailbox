# Puck exact check of Opus R011 Track A (PT-008-R011-OPUS-TrackA.md). Exact Fractions, seeded random + edge cases.
from fractions import Fraction as F
import math, random
random.seed(20261018)
def nd(x): x=x-math.floor(x); return min(x,1-x)
def rnd(x): return math.floor(x+F(1,2))
def allok(speeds,t,dl): return all(nd(u*t)>=dl for u in speeds)
def rf(lo,hi,den=10**6):  # random fraction strictly inside (lo,hi)
    return lo+(hi-lo)*F(random.randint(1,den-1),den)
def WL(m,M,w,n):
    dl=F(1,n); tL=dl/m; X=w*tL
    return tL if nd(X)>=dl else (rnd(X)+dl)/w
def TN(m,w): return 1/(m+w)
res={}
def rec(k,ok):
    a=res.setdefault(k,[0,0,None]); a[0]+=1
    if not ok: a[1]+=1; 
    return ok
# 1) WL (A1) n=5 on its stated domain c<4a, d>=2ac/(4a-c)
for _ in range(40000):
    a=rf(F(1,10),F(10)); c=rf(a,4*a); b=rf(a,c); thr=2*a*c/(4*a-c)
    d=max(c,thr)*(1+F(random.choice([0,1,2,10,1000]))*rf(F(0),F(1))) if random.random()<.9 else max(c,thr)
    if d<=c: d=c+F(1,10**6)
    if d<thr: d=thr
    t=WL(a,c,d,5); rec("WL n=5 domain",allok((a,b,c,d),t,F(1,5)) and t>0)
# 2) K5 (A2): c<=8a/3, any d>c
for _ in range(60000):
    a=rf(F(1,10),F(10)); c=rf(a,F(8,3)*a) if random.random()<.9 else F(8,3)*a; b=rf(a,c)
    r=random.random()
    d = rf(c,4*a) if r<.4 else (4*a if r<.45 else (4*a+F(1,10**9) if r<.5 else rf(4*a,4*a*random.choice([2,10,10**4]))))
    t=TN(a,d) if d<=4*a else WL(a,c,d,5); rec("K5 c<=8a/3",allok((a,b,c,d),t,F(1,5)) and t>0)
# 3) GW(n) and K_n, n=4..8 (A3,A4); threshold values
for n in range(4,9):
    print(f"n={n}: (n-1)^2/(n+1) = {F((n-1)**2,n+1)}")
    for _ in range(15000):
        m=rf(F(1,10),F(10)); M=rf(m,F((n-1)**2,n+1)*m) if random.random()<.95 else F((n-1)**2,n+1)*m
        mids=sorted(rf(m,M) for _ in range(n-4))  # n-1 nonzero speeds: m, mids(n-4), M, w
        r=random.random()
        w = rf(M,(n-1)*m) if r<.4 else ((n-1)*m if r<.45 else rf((n-1)*m,(n-1)*m*random.choice([2,50,10**5])))
        t=TN(m,w) if w<=(n-1)*m else WL(m,M,w,n)
        rec(f"K_n n={n}",allok([m]+mids+[M,w],t,F(1,n)) and t>0)
    for _ in range(8000):  # GW on its own domain M<(n-1)m, w>=2mM/((n-1)m-M)
        m=rf(F(1,10),F(10)); M=rf(m,(n-1)*m); thr=2*m*M/((n-1)*m-M)
        w=max(thr,M+F(1,10**6))*(1+rf(F(0),F(3))) if random.random()<.9 else max(thr,M+F(1,10**6))
        mids=sorted(rf(m,M) for _ in range(n-4))
        rec(f"GW n={n} domain",allok([m]+mids+[M,w],WL(m,M,w,n),F(1,n)))
# 4) AC1 (A6)
for _ in range(30000):
    a=rf(F(1,10),F(10)); c=rf(a,4*a) if random.random()<.95 else 4*a; b=rf(a,c)
    S=a+c; j=random.randint(1,50); d=S*(j+rf(F(1,5),F(4,5)))
    if d<=c: continue
    rec("AC1",allok((a,b,c,d),1/S,F(1,5)))
# 5) A7 obstruction at c=4a: tau grid in (0,3], which tau work for ALL b in (a,c)? (b/(a+c) ranges (1/5,4/5))
good=[]
for tn in range(1,3001):
    tau=F(tn,1000)
    # image tau*(1/5,4/5) must stay in safe set: check open interval via endpoints + no unsafe point inside
    lo,hi=tau/5,4*tau/5; ok=True
    # unsafe set is union (j-1/5, j+1/5); interval (lo,hi) avoids it iff no j with (j-1/5,j+1/5) meeting (lo,hi)
    for j in range(0,4):
        if max(lo,F(j)-F(1,5))<min(hi,F(j)+F(1,5)): ok=False
    if ok: good.append(tau)
print("A7: tau in (0,3] (step 1/1000) safe for all b at c=4a:", good)
a=F(1); c=F(4); d=F(11,2); b=F(5,2)  # frac(d/5a)=0.1 not in A
print("A7 example (1,5/2,4,11/2), tau=1: min dist", min(nd(u/(a+c)) for u in (a,b,c,d)))
# 6) B7 shown computations
for s in [(F(1),F(3,2),F(2),F(5)),(F(1),F(2),F(8,3),F(5)),(F(1),F(5,4),F(7,4),F(41,10))]:
    a,b,c,d=s; t=WL(a,c,d,5); print("B7",tuple(map(str,s)),"t=",t,"dists",[str(nd(u*t)) for u in s], "ok",allok(s,t,F(1,5)))
# 7) algebra: d>4a >= 2ac/(4a-c) iff c<=8a/3 (check on grid)
bad=0
for cn in range(101,400):
    c=F(cn,100); bad += ((4>=2*c/(4-c))!=(c<=F(8,3)))
print("B2 equivalence 4a>=2ac/(4a-c) <=> c<=8a/3 (a=1, c grid in (1,4)): mismatches",bad)
for k,v in res.items(): print(f"{k}: {v[0]} cases, {v[1]} failures")
