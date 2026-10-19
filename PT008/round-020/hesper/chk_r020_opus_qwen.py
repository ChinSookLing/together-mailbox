import sys; sys.argv=['x']
src=open('base.py').read(); exec(src[:src.index("ok=lambda")])
from fractions import Fraction as F
from math import gcd,ceil,floor
from functools import reduce
ok=lambda V,t: t>0 and min(nd(u*t) for u in V)>=F(1,5)
def PSs(V):
    for i,u in enumerate(V):
        W=[x for j,x in enumerate(V) if j!=i]
        g=reduce(gcd,W)  # integers
        P=F(1,g); t0=F4(*W); x=fr(u*P); ph=fr(u*t0)
        if A(ph): n=0
        elif x==0: continue
        elif x<=F(1,2): n=ceil(fr(F(1,5)-ph)/x)
        else: n=ceil(fr(ph-F(4,5))/(1-x))
        return t0+n*P
    return None
tot=exc=bad=0; E=[]
for a in range(1,31):
 for b in range(a+1,31):
  for c in range(b+1,31):
   for d in range(c+1,31):
    tot+=1; t=PSs((a,b,c,d))
    if t is None: exc+=1; E.append((a,b,c,d))
    elif not ok((a,b,c,d),t): bad+=1
print('PS* total',tot,'E*',exc,'fail',bad,'first',E[:3])
for V in [(1,2,9,30),(1,5,6,18),(5,13,16,29),(5,13,18,29),(7,10,20,29),(7,11,19,29)]:
    print(V,'in E*',V in E, 'has some t=k/(N*lcm) success (sanity, any t with denom<=600):', any(ok(V,F(k,Dn)) for Dn in range(1,121) for k in range(1,Dn)))
# Opus strict cex Q-ERC1: theta=1/5,w=7/5, m=1
def m1(th,w,strict):
    L=th.denominator*w.denominator//gcd(th.denominator,w.denominator)
    cmp=(lambda z: nd(z)>F(1,5)) if strict else (lambda z: nd(z)>=F(1,5))
    return [k for k in range(L) if cmp(k*th) and cmp(k*w)]
print('QERC1 th=1/5 w=7/5 nonstrict',m1(F(1,5),F(7,5),False),'strict',m1(F(1,5),F(7,5),True))
print('|A_7|',sum(1 for k in range(7) if F(1,5)<=fr(F(k,7))<=F(4,5)))
# Q-ERC2 strict cex theta=1/3,n=1,m=5: tau=k/5, phases tau*theta, tau*(1-theta), tau*w
def lat(th,w,m,strict):
    Q=m*th.denominator*w.denominator
    cmp=(lambda z: nd(z)>F(1,5)) if strict else (lambda z: nd(z)>=F(1,5))
    return [k for k in range(Q) if all(cmp(F(k,m)*x) for x in (th,1-th,w))]
print('V5 m=5 nonstrict',lat(F(1,3),F(1),5,False),'strict',lat(F(1,3),F(1),5,True))
# Qwen w=M!, theta=1/3: lattice m<=M empty, m=M+1?
import math
for M in (3,4,5,6):
    N=F(math.factorial(M)); emp=[m for m in range(1,M+1) if lat(F(1,3),N,m,False)]
    first=next(m for m in range(1,60) if lat(F(1,3),N,m,True))
    print('w=%d!'%M,'nonempty m<=M:',emp,'first strict-nonempty m:',first)
print('Opus examples in E*:',[(V, V in E) for V in [(1,2,3,4),(1,3,4,5),(1,3,4,7)]])
