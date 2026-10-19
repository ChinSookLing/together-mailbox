from fractions import Fraction as F
from math import floor, ceil, gcd
import random
random.seed(1818)
def nd(z): return min(z-floor(z), floor(z)+1-z)
d5=F(1,5)
def ok(V,t): return min(nd(u*t) for u in V)>=d5
def qpsr(th,w):
    L=th.denominator*w.denominator//gcd(th.denominator,w.denominator)
    R=[r for r in range(L) if nd(r*th)>=d5 and nd(r*w)>=d5]
    if not R: return L,R,None
    G=max((R[(i+1)%len(R)]-R[i])%L or L for i in range(len(R)))
    return L,R,G
L,R,G=qpsr(F(1,3),F(8,9));print('V4 shape L',L,'R',R,'G',G)
for S in (90,36):
    k0=ceil(F(S,5));k=k0+min((r-k0)%L for r in R);V=(F(1),F(S,3),F(2*S,3),F(8*S,9));t=F(k,S)
    print('S',S,'k',k,[str(nd(u*t)) for u in V])
# random rational shapes, s>=5G/3
shapes=pts=bad=nores=0
while shapes<500:
    q=random.randint(3,30);p=random.randint(1,(q-1)//2);th=F(p,q)
    if not 0<th<F(1,2): continue
    q2=random.randint(1,30);w=F(random.randint(1,4*q2),q2)
    if w<=1-th: continue
    L,R,G=qpsr(th,w)
    if not R: nores+=1; continue
    shapes+=1
    for _ in range(20):
        s=F(5*G,3)+F(random.randint(0,10**5),10**4)
        a=F(1);b=th*s;c=s-b;d=w*s
        if not a<b: continue
        pts+=1
        k0=ceil(s/5);k=k0+min((r-k0)%L for r in R)
        if not ok((a,b,c,d),k/s): bad+=1
print('Q-PSR random: shapes',shapes,'points',pts,'fail',bad,'(shapes with empty R skipped:',nores,')')
