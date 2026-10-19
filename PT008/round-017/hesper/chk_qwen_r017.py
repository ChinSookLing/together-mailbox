from fractions import Fraction as F
from math import floor, ceil
import random
random.seed(1718)
def nd(z): return min(z-floor(z), floor(z)+1-z)
d5=F(1,5)
def ok(V,t): return min(nd(u*t) for u in V)>=d5
def U(lo,hi): return lo+(hi-lo)*F(random.randint(0,10**6),10**6)
V=(F(6),F(30),F(60),F(80)); print('(6,30,60,80) t=2/9',[str(nd(u*F(2,9))) for u in V])
# a-never-active: u/a=5q -> a-edge times fail
print('a-never V4 edges fail all j<50:', all(not ok((F(1),F(30),F(60),F(80)),(j+c)) for j in range(50) for c in (F(1,5),F(4,5))))
# Q-FSR j=1 box with NF-20 shape, k=20: s in [100/9,100/6]
bad=tried=0
while tried<20000:
    s=U(F(100,9),F(100,6)); th=U(F(31,100),F(34,100)); w=U(F(86,100),F(89,100))
    a=F(1);b=th*s;c=(1-th)*s;d=w*s
    if not(a<b<c<d): continue
    tried+=1
    if not ok((a,b,c,d),20/s): bad+=1
print('Q-FSR k=20 j=1 x NF-20 shape: fail',bad,'of',tried)
# exact equivalence (C3) segments, k=20
k=20
for s in [F(25),F(100),F(100,9),F(100,6),F(24),F(17)]:
    print('s',s,'frac(k/s) in A',d5<=(k/s)%1<=F(4,5), 'in union', any(F(5*k,5*j+4)<=s<=F(5*k,5*j+1) for j in range(0,4*k//5+1)))
# Opus CLR V4 shape also covers s=15?
s=F(15);k0=ceil(s/5);kk=k0+min((r-k0)%9 for r in (4,5));print('CLR at s=15 tau',kk, ok(V,F(kk)/90))
