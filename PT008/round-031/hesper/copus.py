from fractions import Fraction as F
from math import floor, ceil
from itertools import combinations
import random,sys
sys.path.insert(0,'.')
from fwcert import comps, nd
def badset(V,d,U):
    a=min(V); C=comps(V,d/a,(1-d)/a,d)
    if not C: return None,C
    cur=[(F(0),U)]
    for L,R in C:
        iv=[]
        for m in range(0,ceil(U*R+d)+1):
            lo=(m-d)/L if m>0 else F(0); hi=(m+d)/R
            if lo<hi: iv.append((max(lo,F(0)),min(hi,U)))
        new=[]
        for x,y in cur:
            for p,q in iv:
                lo,hi=max(x,p),min(y,q)
                if lo<hi: new.append((lo,hi))
        cur=new
    return cur,C
# B(1,2,3)
B,C=badset([1,2,3],F(1,5),F(50)); print("comps(1,2,3):",C); print("B(1,2,3) within (0,50):",B)
# witness consistency for B(1,2,3)
def hasw(V,u,d):
    a=min(V); 
    for L,R in comps(V,d/a,(1-d)/a,d):
        q=ceil(u*L-(1-d))
        if q<=floor(u*R-d): return True
    return False
random.seed(1);inc=0
for _ in range(2000):
    u=F(random.randint(1,4000),random.randint(1,400))
    inB=any(x<u<y for x,y in B)
    if inB==hasw([1,2,3],u,F(1,5)): inc+=1
print("FWB consistency (1,2,3), 2000 random u<=..., inconsistent:",inc)
# C-INIT: k=2 (d=1/4, <=30), k=3 (d=1/5,<=20), k=4 (d=1/6,<=13); U=(k+1)*vmax
for k,d,N in ((2,F(1,4),30),(3,F(1,5),20),(4,F(1,6),13)):
    cnt=0;bad=[]
    for V in combinations(range(1,N+1),k):
        B,C=badset(list(V),d,F((k+1)*max(V)))
        cnt+=1
        Rmax=max(R for L,R in C)
        if B!=[(F(0),d/Rmax)]: bad.append((V,B[:3]))
    print("C-INIT k=%d d=%s <=%d: %d sets, exceptions %d"%(k,d,N,cnt,len(bad)),bad[:3])
