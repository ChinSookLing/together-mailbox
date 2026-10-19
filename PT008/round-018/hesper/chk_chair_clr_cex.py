from fractions import Fraction as F
from math import floor, ceil, gcd
import random
def nd(z): return min(z-floor(z), floor(z)+1-z)
d5=F(1,5)
def ok(V,t): return min(nd(u*t) for u in V)>=d5
# chair counterexample
m,Q,th0,w0,R=2,7,F(2,7),F(6,7),[4]
print('periods: Qth0/m',Q*th0/m,'Qw0/m',Q*w0/m,'Q/m',F(Q,m))
tau=F(4,m);print('ref k=4 dists',[str(nd(tau*x)) for x in (th0,1-th0,w0)])
V=(F(7,20),F(2),F(5),F(6)); s=(V[1]+V[2])/V[0]; print('s',s,'theta',V[1]/(V[1]+V[2]),'w',V[3]/(V[1]+V[2]))
k0=ceil(m*s/5);k=k0+min((r-k0)%Q for r in R);tau=F(k,m);t=tau/(V[1]+V[2])
print('k0',k0,'k',k,'tau',tau,'t',t,'dists',[str(nd(u*t)) for u in V])
print('G=7 cond s>=5G/(3m)=',F(35,6))
# repaired CLR v2 random test: rational shapes, conditions Qth0/m, Qw0/m, Q/m integers
random.seed(18); tested=bad=0; cases=0
while cases<300:
    q1=random.randint(2,12);p1=random.randint(1,q1-1);th0=F(p1,q1)
    if not th0<F(1,2): continue
    q2=random.randint(1,12);p2=random.randint(q2//2+1,3*q2);w0=F(p2,q2)
    if not w0>1-th0: continue
    m=random.randint(1,4)
    L=1
    for x in (th0/m,w0/m,F(1,m)): L=L*x.denominator//gcd(L,x.denominator)
    Q=L*random.randint(1,2)
    R=[];mus=[]
    for r in range(Q):
        tau=F(r,m); dd=[nd(tau*th0),nd(tau*(1-th0)),nd(tau*w0)]
        if min(dd)>d5: R.append(r);mus.append(dd)
    if not R: continue
    cases+=1
    mbc=min(min(x[0],x[1]) for x in mus)-d5; md=min(x[2] for x in mus)-d5
    Rs=sorted(R);G=max(((Rs[(i+1)%len(Rs)]-Rs[i])%Q or Q) for i in range(len(Rs)))
    smin=F(5*G,3*m)
    for _ in range(60):
        s=smin+F(random.randint(0,10**5),10**5)*300
        k0=ceil(m*s/5);k=k0+min((r-k0)%Q for r in R);tau=F(k,m)
        th=th0+(2*F(random.random())-1)*mbc/tau; w=w0+(2*F(random.random())-1)*md/tau
        a=F(1);b=th*s;c=s-b;d=w*s
        if not(a<b<c<d): continue
        tested+=1
        if not ok((a,b,c,d),tau/s): bad+=1
print('CLR v2 (with Q/m in Z, uniform margins over R) random: shapes',cases,'points',tested,'fail',bad)
