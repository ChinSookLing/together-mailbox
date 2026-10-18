# PT-008 R009 Puck exact-Fraction check of chair ruling (TN statement; LN with chair's nearest-boundary + nonnegative rule, both tie choices). Puck 2026-10-18.
from fractions import Fraction as F
from math import floor
import random
pub=open("/workspace/r8pub/publish/T4-PUBLICATION.md").read()
code=pub[pub.index("```python")+9:pub.index("```",pub.index("```python")+9)]
ns={}; exec(code,ns); F4=ns["F4"]; d=ns["d"]
fails=[]; n=0
def chk(name,c):
    global n; n+=1
    if not c: fails.append(name)
random.seed(1835)
def rq(lo,hi,den=211): return F(random.randint(int(lo*den)+1,int(hi*den)),den)
# TN: n>=2, speeds |v| in [a,b], b<=(n-1)a (incl. negatives, equality b=(n-1)a)
for _ in range(4000):
    nn=random.randint(2,10); a=rq(F(1,3),5); b=a*(nn-1) if random.random()<0.3 else a+(a*(nn-1)-a)*F(random.randint(0,50),50)
    vs=[a,b]+[a+(b-a)*F(random.randint(0,99),99) for _ in range(nn-3)] if nn>2 else [a]
    vs=[v*random.choice([1,-1]) for v in vs]
    t=1/(a+b)
    chk(f"TN n={nn} a={a} b={b}", all(d(v*t)>=F(1,nn) for v in vs))
# LN per chair: t0=F4(a,b,c); if ||d t0||>=1/5 keep; else move to nearest boundary of d's forbidden arc,
# never left of zero (if k=0 go right); ties tried both ways. Check t>=0, |t-t0|<=1/(5d)<=1/(20c), all four >=1/5.
D=F(1,5)
for _ in range(6000):
    a=F(1); b=rq(F(1001,1000),6); c=rq(b+F(1,211),12) if b<12 else b+1
    if c<=b: continue
    dd=4*c if random.random()<0.2 else rq(4*c,40*c+1)
    t0=F4(a,b,c)
    chk("F4 ok",min(d(a*t0),d(b*t0),d(c*t0))>=F(1,4))
    x=dd*t0
    if d(x)>=D: cands=[t0]
    else:
        k=floor(x+F(1,2)); left=(k-D)/dd; right=(k+D)/dd
        dl,dr=t0-left,right-t0
        if k==0: cands=[right]
        elif dl<dr: cands=[left]
        elif dr<dl: cands=[right]
        else: cands=[left,right]
    for t in cands:
        chk(f"LN t>=0 {(b,c,dd)}", t>=0)
        chk(f"LN shift {(b,c,dd)}", abs(t-t0)<=1/(5*dd)<=1/(20*c))
        chk(f"LN safe {(b,c,dd)} t={t}", min(d(v*t) for v in (a,b,c,dd))>=D)
print("checks",n,"failures",len(fails)); print(fails[:5])
