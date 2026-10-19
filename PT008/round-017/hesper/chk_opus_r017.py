from fractions import Fraction as F
from math import floor, ceil
import random
def nd(z): return min(z-floor(z), floor(z)+1-z)
d5=F(1,5); A=lambda z: d5<=z-floor(z)<=F(4,5)
def ok(V,t): return min(nd(u*t) for u in V)>=d5
def U(lo,hi): return lo+(hi-lo)*F(random.randint(0,10**6),10**6)
random.seed(17)
# B4+
bad=0
for _ in range(20000):
    x=U(F(31,4),F(31)); r=U(F(61,31),F(64,31)); q=U(F(81,31),F(84,31))
    a=F(1);b=x;c=r*b;d=q*b
    if not ok((a,b,c,d),F(31,5)/b): bad+=1
print('B4+ 20000 pts fail',bad)
V4=tuple(map(F,(1,30,60,80))); print('V4 t=31/150',[str(nd(u*F(31,150))) for u in V4])
# inclusion points
def inNF(s,th,w): return 25<=s<=100 and F(31,100)<=th<=F(34,100) and F(86,100)<=w<=F(89,100)
def inR20(s,th,w): return 80<=s<=100 and F(32,100)<=th<=F(34,100) and F(88,100)<=w<=F(89,100)
def inB4p(x,r,q): return F(31,4)<=x<=31 and F(61,31)<=r<=F(64,31) and F(81,31)<=q<=F(84,31)
def inB4(x,r,q): return 29<x<31 and F(61,31)<=r<=F(64,31) and F(81,31)<=q<=F(84,31)
def xrq2s(x,r,q): return x*(1+r),1/(1+r),q/(1+r)
def s2xrq(s,th,w): r=1/th-1; return s*th,r,w*(1+r)
P1=(F(30),F(2),F(83,31)); print('P1 in B4',inB4(*P1),'in NF',inNF(*xrq2s(*P1)))
P2=(F(30),F(2),F(81,31)); print('P2 in B4',inB4(*P2),'in R20',inR20(*xrq2s(*P2)),'in NF',inNF(*xrq2s(*P2)))
for nm,pt,f in [('NF pt s50 th.31 w.87',(F(50),F(31,100),F(87,100)),inNF),('R20 pt s90 th.32 w.885',(F(90),F(32,100),F(885,1000)),inR20),('NF pt s50 th1/3 w7/8',(F(50),F(1,3),F(7,8)),inNF)]:
    print(nm,'in own',f(*pt),'in B4+',inB4p(*s2xrq(*pt)),'in B4',inB4(*s2xrq(*pt)))
# CLR instances
def clr(s,m,Q,R):
    k0=ceil(m*s/5); k=k0+min((rho-k0)%Q for rho in R); return F(k,m)
for nm,th0,w0,m,Q,R,muc,mud,smin in [('V4shape',F(1,3),F(8,9),1,9,[4,5],F(2,15),F(11,45),F(40,3)),('V5shape',F(1,3),F(1),4,12,[3,9],F(1,20),F(1,20),F(5,2))]:
    # residue table check
    for k in range(Q):
        tau=F(k,m); good=A(tau*th0) and A(tau*(1-th0)) and A(tau*w0)
        if (k in R)!=good: print(nm,'residue mismatch',k)
    print(nm,'R margins',[(str(nd(F(k,m)*th0)),str(nd(F(k,m)*w0))) for k in R])
    bad=0
    for _ in range(20000):
        s=U(smin,F(2000)); tau=clr(s,m,Q,R)
        th=th0+(2*F(random.random())-1)*muc/tau; w=w0+(2*F(random.random())-1)*mud/tau
        S=s; b=th*S; c=S-b; d=w*S
        if not (1<b<c): continue
        if not ok((F(1),b,c,d),tau/S): bad+=1
    print(nm,'CLR random fail',bad)
print('V4 CLR tau',clr(F(90),1,9,[4,5]),[str(nd(u*F(22,90))) for u in V4])
V5=(F(1),F(5,2),F(5),F(15,2)); print('V5 CLR tau',clr(F(15,2),4,12,[3,9]))
print('V4 nbhd: s in (85,95] tau', {clr(F(s,10),1,9,[4,5]) for s in range(851,951)})
