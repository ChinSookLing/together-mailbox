from fractions import Fraction as F
from math import floor
import random
random.seed(1717)
def nd(z): return min(z-floor(z), floor(z)+1-z)
d5=F(1,5)
def ok(V,t,dl=d5): return min(nd(u*t) for u in V)>=dl
def U(lo,hi): return lo+(hi-lo)*F(random.randint(0,10**6),10**6)
# Q-B2
bad=tried=0
while tried<20000:
    r=U(F(3,2),F(9)); s=U(F(1),F(10)); w=U(F(3,5),F(9,10))
    S=s; b=S/(1+r); c=S-b; d=w*S
    if not (1<b<c<d): continue
    tried+=1
    if not ok((F(1),b,c,d),2/S): bad+=1
print('Q-B2 20000 valid pts fail',bad)
print('V2 t=2/5',[str(nd(u*F(2,5))) for u in (F(1),F(2),F(3),F(9,2))])
# R20
bad=0
for _ in range(20000):
    s=U(F(80),F(100)); th=U(F(32,100),F(34,100)); w=U(F(88,100),F(89,100))
    if not ok((F(1),th*s,(1-th)*s,w*s),20/s): bad+=1
print('R20 fail',bad)
inAL=lambda x:1<=x%5<=4
inAU=lambda x:1<=(4*x)%5<=4
for s,th,w in [(F(80),F(34,100),F(89,100)),(F(80),F(32,100),F(88,100))]:
    u=(th*s,(1-th)*s,w*s); print('pt',[float(x) for x in u],'TE-AL',all(inAL(x) for x in u),'TE-AU',all(inAU(x) for x in u))
lam=lambda th,w: th/(1-th)*(1+2*(1-th)/(5*w))
print('NW lambda2 min (th .32,w .89)',float(lam(F(32,100),F(89,100))))
for nm,V,t,dl in [('V2',(1,2,3,F(9,2)),F(2,5),d5),('V4',(1,30,60,80),F(2,9),d5),('NW4',(1,3,F(21,5)),F(5,12),F(1,4))]:
    print(nm,[str(nd(F(u)*t)) for u in V])
