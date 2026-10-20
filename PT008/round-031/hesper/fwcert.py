from fractions import Fraction as F
from math import floor, ceil
from itertools import combinations
import random
d5=F(1,5)
def nd(x): return min(x-floor(x),floor(x)+1-x)
def comps(V,lo,hi,d):
    bps={lo,hi}
    for v in V:
        for m in range(floor(v*lo)-1,ceil(v*hi)+2):
            for s in (d,-d):
                x=(m+s)/v
                if lo<=x<=hi: bps.add(x)
    bps=sorted(bps); out=[]
    ok=lambda t: all(nd(v*t)>=d for v in V)
    cur=None
    for i,x in enumerate(bps):
        if ok(x):
            if cur is None: cur=[x,x]
            cur[1]=x
            if i+1<len(bps) and not ok((x+bps[i+1])/2):
                out.append(tuple(cur)); cur=None
        else:
            if cur: out.append(tuple(cur)); cur=None
    if cur: out.append(tuple(cur))
    return out
def cert(a,b,c,dd,d=d5):
    J=(1/(5*F(a)),4/(5*F(a)))
    for L,R in comps([a,b,c],J[0],J[1],d):
        q=ceil(dd*L-(1-d))
        if q<=floor(dd*R-d):
            t=max(L,(q+d)/dd)
            assert L<=t<=R and all(nd(v*t)>=d for v in (a,b,c,dd)) and 0<t<1/F(a)
            return t
    return None
if __name__=="__main__":
    N=0;bad=[]
    for a,b,c,dd in combinations(range(1,25),4):
        N+=1
        if cert(a,b,c,dd) is None: bad.append((a,b,c,dd))
    print("int quads <=24:",N,"no witness:",len(bad),bad[:5])
    random.seed(31);M=0;bad2=0
    for _ in range(3000):
        xs=sorted({F(random.randint(1,400),random.randint(1,40)) for _ in range(4)})
        if len(xs)<4: continue
        M+=1
        if cert(*xs) is None: bad2+=1
    print("random rational quads:",M,"no witness:",bad2)
