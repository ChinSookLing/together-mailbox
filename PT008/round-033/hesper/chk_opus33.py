from fractions import Fraction as F
from math import floor, ceil
import itertools,sys
sys.argv=['x']
from fwcert import comps, nd
from copus import badset
def S(V,d): a=V[0]; return comps(V,d/a,(1-d)/a,d)
def W(K,d,b,top):
    L,R=K; out=[]
    q=0
    while True:
        lo=(q-d)/L if L>0 else None
        hi=(q+d)/R
        if lo is not None and lo>top: break
        if lo<hi: out.append((max(lo,F(0)),hi))
        q+=1
        if R==L and q>2000: break
    return out
def inter(A,B):
    o=[]
    for a in A:
        for c in B:
            lo,hi=max(a[0],c[0]),min(a[1],c[1])
            if lo<hi:o.append((lo,hi))
    return o
d=F(1,5);V=[F(1),F(3),F(4)]
C=S(V,d);print('S(1,3,4)=',C)
# lock points
pts=[]
for K in C:
    pts.append(K)
locks=[]
def inS(t): return any(L<=t<=R for L,R in C)
cand=set()
for L,R in C:
    for m in (2,3,4):
        # tau in [L,R], m tau in S
        for L2,R2 in C:
            lo=max(L,L2/m); hi=min(R,R2/m)
            if lo<=hi: locks.append((m,lo,hi))
print('lock tau ranges',locks)
K1,K2=(F(2,5),F(9,20)),(F(11,20),F(3,5))
w1=W(K1,d,4,F(100));w2=W(K2,d,4,F(100));print('W1',w1);print('W2',w2)
print('W1∩W2∩(4,∞)',[x for x in inter(w1,w2) if x[1]>4])
B,_=badset(V,d,F(200));print('B(1,3,4) on (0,200)',B)
