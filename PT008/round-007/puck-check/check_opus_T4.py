# Puck independent exact check of Opus R007 Track A theorem T4 (nine-piece F4). Own code, Fractions only.
from fractions import Fraction as F
import math, random
Q=F(1,4)
def d(u): u=u-math.floor(u); return min(u,1-u)
def ok(a,b,c,t): return t>0 and min(d(a*t),d(b*t),d(c*t))>=Q
def F3(a,b): return F(math.ceil((a+b)/(3*a)))/(a+b)
def nudge(a,b,c):
    t0=F3(a,b); X=c*t0
    if d(X)>=Q: return t0
    k=math.floor(X+F(1,2)); e=X-k; s=1 if e>=0 else -1
    return (k+F(s,4))/c
def pls(p,q,r):
    th=p/(p+q); k0=math.ceil((p+q)/(4*r)); x0=k0*th-math.floor(k0*th)
    if Q<=x0<=3*Q: j=0
    else:
        D=Q-x0; D=D-math.floor(D); j=math.ceil(D/th)
    return F(k0+j)/(p+q)
def F4(a,b,c):
    if c<=3*a: return "S1",1/(4*a)
    if c>=3*b: return "S2",nudge(a,b,c)
    if b>=3*a: return "S3",pls(b,c,a)
    r=c/b; s=(b+c)/a
    if r<=F(7,5): return "B3",F(3)/(b+c)
    if r>=F(5,3) and s<=8: return "B2",F(2)/(b+c)
    if F(9,7)<=r<=F(11,5) and s>=F(16,3): return "B4",F(4)/(b+c)
    if r>=F(13,7) and s>=F(20,3): return "B5",F(5)/(b+c)
    # fallback must lie in G and in S6-A
    assert F(7,5)<r<F(5,3) and s<F(16,3), ("fallback outside G",a,b,c)
    assert 3*a<=c<=11*a and F(5,12)*(a+c)<=b<=F(7,12)*(a+c), ("G not in S6-A",a,b,c)
    return "S6A",F(3)/(a+c)
stats={};bad=[]
def test(a,b,c):
    if not (0<a<b<c): return
    nm,t=F4(a,b,c); stats[nm]=stats.get(nm,0)+1
    if not ok(a,b,c,t): bad.append((nm,a,b,c,t))
random.seed(2026)
def rq(lo,hi,den): return F(random.randint(math.ceil(lo*den),math.floor(hi*den)),den)
N=0
for _ in range(20000):   # whole space, x in (1,40], y-x in (0,400]
    x=rq(1,40,random.choice([7,97,1009])); y=x+rq(0,400,random.choice([3,101,997])); test(F(1),x,y); N+=1
for _ in range(20000):   # dense region D: 1<x<3, 3<y<3x
    x=rq(1,3,random.choice([11,101,1013])); y=rq(3,3*x,random.choice([13,103,1019])); test(F(1),x,y); N+=1
# boundary lines (own choice): r in {7/5,5/3,9/7,11/5,13/7,3}, s in {16/3,8,20/3,4,12}, x=3, y=3, y=3x
eps=[F(0),F(1,10**6),F(-1,10**6)]
for _ in range(1500):
    x=rq(1,3,997)
    for r in [F(7,5),F(5,3),F(9,7),F(11,5),F(13,7),F(3)]:
        for e in eps: test(F(1),x,x*(r+e)); N+=1
    for s in [F(16,3),F(8),F(20,3),F(4),F(12)]:
        for e in eps: test(F(1),x,s+e-x); N+=1
    for e in eps: test(F(1),x,F(3)+e); test(F(1),x,3*x+e); test(F(1),F(3)+e,x+F(3)); N+=9
# G vertices neighbourhood: r=7/5,5/3 with s=16/3, and D-corner points
for (r,s) in [(F(7,5),F(16,3)),(F(5,3),F(16,3)),(F(7,5),3+F(3)/F(7,5)),(F(5,3),3+F(3)/F(5,3))]:
    for dr in [F(0),F(1,10**5),F(-1,10**5)]:
        for ds in [F(0),F(1,10**5),F(-1,10**5)]:
            rr,ss=r+dr,s+ds; b=ss/(1+rr); test(F(1),b,b*rr); N+=1
# Opus C2 examples
for a,b,c in [(1,2,3),(2,4,7),(F(1),F(12,5),F(4)),(F(1),F(2),F(16,5)),(1,3,4)]:
    a,b,c=F(a),F(b),F(c); nm,t=F4(a,b,c); print("  example",(a,b,c),nm,"t=",t,[d(v*t) for v in (a,b,c)],ok(a,b,c,t))
print("T4 tested",N,"cases; rule use",stats,"; failures",len(bad),bad[:3])
# scale invariance spot check (a not 1)
bad2=0
for _ in range(3000):
    a=rq(F(1,50),50,89); x=rq(1,6,101); y=x+rq(0,30,103); nm,t=F4(a,a*x,a*y); bad2+= not ok(a,a*x,a*y,t)
print("T4 with a!=1: 3000 cases, failures",bad2)
# Opus S5 definition check
bad5=0
for _ in range(5000):
    x=rq(1,3,211); y=rq(F(5,4)*(1+x),F(7,4)*(1+x),223)
    if y<=x: continue
    bad5+= not ok(F(1),x,y,1/(1+x))
print("Opus S5 (x<=3, 5(1+x)/4<=y<=7(1+x)/4, t=1/(a+b)): failures",bad5)
