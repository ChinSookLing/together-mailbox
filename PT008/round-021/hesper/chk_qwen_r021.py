src=open('/workspace/work/pt008r20/hesper/base.py').read(); exec(src[:src.index("ok=lambda")])
from fractions import Fraction as F
from math import gcd,ceil
# Q-GATE example
a,b,c,d=F(1,7),F(1),F(101,100),F(2); S=b+c; t0=F4(b,c,d); ts=S*t0
M=max(1-b/S,d/S); Q0=ceil(20*M)
def convs(x):
    p0,q0,p1,q1=0,1,1,0; out=[]
    while True:
        ai=x.numerator//x.denominator; p0,p1=p1,ai*p1+p0; q0,q1=q1,ai*q1+q0; out.append(F(p1,q1))
        r=x-ai
        if r==0: return out
        x=1/r
cv=[c for c in convs(ts) if c.denominator<=Q0][-1]
print('Q-GATE ex: t0',t0,'tau*',ts,'Q0',Q0,'p/q',cv,'dists',[nd(cv*u) for u in (b/S,c/S,d/S)],'a dist',nd(cv/S*a))
print('(7/20,2,5,6) t=9/8:',[nd(v*F(9,8)) for v in (F(7,20),2,5,6)])
# Q-ERC1 non-strict: theta=p/q (q>=3, p<q/2? any p coprime), w=r/q' ; G1 nonempty iff q'>=2
bad=0;n=0
for q in range(3,41):
  for p in range(1,q):
    if gcd(p,q)!=1: continue
    for qq in range(1,41):
      for r in range(1,3*qq+1):
        if gcd(r,qq)!=1: continue
        n+=1; th=F(p,q); w=F(r,qq); L=q*qq//gcd(q,qq)
        ne=any(nd(k*th)>=F(1,5) and nd(k*w)>=F(1,5) for k in range(L))
        if ne!=(qq>=2): bad+=1
print('Q-ERC1 non-strict cases',n,'mismatches',bad)
