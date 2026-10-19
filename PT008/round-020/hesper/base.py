from fractions import Fraction as F
from math import floor, ceil
import random
random.seed(19019)
def nd(z): return min(z-floor(z), floor(z)+1-z)
def fr(z): return z-floor(z)
q=F(1,4)
def F3(a,b): return F(ceil((a+b)/(3*a)))/(a+b)
def F4(a,b,c):
    a,b,c=F(a),F(b),F(c)
    r=c/b; s=(b+c)/a
    if c<=3*a: return 1/(4*a)
    if c>=3*b:
        t0=F3(a,b); X=c*t0
        if nd(X)>=q: return t0
        k=floor(X+F(1,2)); e=X-k; sg=1 if e>=0 else -1
        return (k+F(sg,4))/c
    if b>=3*a:
        p,qq,rr=b,c,a; th=p/(p+qq); k0=ceil((p+qq)/(4*rr)); x0=fr(k0*th)
        j=0 if q<=x0<=F(3,4) else ceil(fr(q-x0)/th)
        return F(k0+j)/(p+qq)
    if r<=F(7,5): return 3/(b+c)
    if r>=F(5,3) and s<=8: return 2/(b+c)
    if F(9,7)<=r<=F(11,5) and s>=F(16,3): return 4/(b+c)
    if r>=F(13,7) and s>=F(20,3): return 5/(b+c)
    return 3/(a+c)
A=lambda z: F(1,5)<=fr(z)<=F(4,5)
def PS(a,b,c,d,g):
    a,b,c,d,g=map(F,(a,b,c,d,g))
    P=1/g; t0=F4(b,c,d); x=fr(a*P); ph=fr(a*t0)
    if A(ph): n=0
    elif x==0: return None
    elif x<=F(1,2): n=ceil(fr(F(1,5)-ph)/x)
    else: n=ceil(fr(ph-F(4,5))/(1-x))
    return t0+n*P, n
ok=lambda V,t: min(nd(u*t) for u in V)>=F(1,5)
for V,g in (((1,30,60,80),10),((1,F(5,2),5,F(15,2)),F(5,2)),((F(7,20),2,5,6),1),((1,2,3,4),1)):
    r=PS(*V,g); print('PS',V,'->',None if r is None else (str(r[0]),r[1],[str(nd(u*r[0])) for u in V]))
# F4 sanity on random triples
bad4=0
for _ in range(20000):
    x=sorted(F(random.randint(1,10**4),random.randint(1,300)) for _ in range(3))
    if len(set(x))<3: continue
    t=F4(*x)
    if not (t>0 and min(nd(u*t) for u in x)>=q): bad4+=1
print('F4 random 20000 triples fail',bad4)
# PS random commensurable
pts=exc=bad=0;maxn=0
for _ in range(20000):
    B,C,E=sorted(random.sample(range(1,60),3)); g=F(random.randint(1,50),random.randint(1,20))
    b,c,d=g*B,g*C,g*E; a=b*F(random.randint(1,999),1000)
    r=PS(a,b,c,d,g)
    if r is None: exc+=1; continue
    pts+=1; maxn=max(maxn,r[1])
    if not ok((a,b,c,d),r[0]): bad+=1
print('PS random pts',pts,'exceptions',exc,'fail',bad,'max n',maxn)
# LS
for B,C,E in ((1,2,3),(3,6,8),(2,5,6)):
    ts=(B+C)*F4(B,C,E); print('LS',(B,C,E),'tau*',ts,'m',ts.denominator,'dists',[str(nd(ts*F(u,B+C))) for u in (B,C,E)])
# APS guarantee version random near V4
pts=bad=0
while pts<5000:
    b=F(30)+F(random.randint(-2000,2000),1000); a=b*F(random.randint(5,330),1000)
    c=2*b+b*F(random.randint(-300,300),10**6); d=F(8,3)*b+b*F(random.randint(-300,300),10**6)
    if not a<b<c<d: continue
    B,C,E=3,6,8; P=B/b; rc=c*P-C; rd=d*P-E; x=fr(a*P); e=min(x,1-x)
    if e==0 or (F(2,5)/e+1)*max(abs(rc),abs(rd))>F(1,20): continue
    t0=F4(b,c,d); ph=fr(a*t0)
    if A(ph): n=0
    elif x<=F(1,2): n=ceil(fr(F(1,5)-ph)/x)
    else: n=ceil(fr(ph-F(4,5))/(1-x))
    pts+=1
    if not ok((a,b,c,d),t0+n*P): bad+=1
print('APS guarantee-version pts',pts,'fail',bad)
