# PT-008 R009 Puck exact-Fraction check of Opus Track A (LB, LN, PLS_delta). Puck 2026-10-18.
from fractions import Fraction as F
import random
pub=open("/workspace/r8pub/publish/T4-PUBLICATION.md").read()
code=pub[pub.index("```python")+9:pub.index("```",pub.index("```python")+9)]
ns={}; exec(code,ns); F4=ns["F4"]; d=ns["d"]; fl=ns["fl"]; ce=ns["ce"]
D=F(1,5); fails=[]; n=0
def chk(name,c):
    global n; n+=1
    if not c: fails.append(name)
def ok5(v,t): return t>0 and min(d(x*t) for x in v)>=D
random.seed(9009)
def rq(lo,hi,den=97): return F(random.randint(int(lo*den)+1,int(hi*den)),den)
# LB(k;ma,mb,md): sample s,r,w inside the box AND order constraints, check t=k/(b+c)
inbox=0
for _ in range(60000):
    k=random.randint(1,8); ma=random.randint(0,k); mb=random.randint(0,k); md=random.randint(0,3*k)
    slo,shi=k/(ma+F(4,5)),k/(ma+F(1,5)); rlo,rhi=k/(mb+F(4,5))-1,k/(mb+F(1,5))-1
    wlo,whi=(md+F(1,5))/k,(md+F(4,5))/k
    if rhi<=1 or shi<=slo: continue
    s=slo+(shi-slo)*F(random.randint(0,60),60); r=max(rlo,1)+(rhi-max(rlo,1))*F(random.randint(1,60),60)
    w=wlo+(whi-wlo)*F(random.randint(0,60),60)
    if not (r>1 and s>1+r and w>r/(1+r)): continue
    a=F(1); b=s/(1+r); c=r*s/(1+r); dd=w*s
    if not (a<b<c<dd): continue
    inbox+=1; chk(f"LB k={k} m={(ma,mb,md)} s={s} r={r} w={w}", ok5([a,b,c,dd],F(k)/(b+c)))
# A2: LB(1;0,0,0) lies inside known d<=4a region (s<=5, w<=4/5 => d=w*s*a<=4a)
sub=True
for _ in range(20000):
    s=rq(F(5,4),5); r=rq(1,4); w=rq(F(1,2),F(4,5))
    if r>1 and s>1+r and w>r/(1+r) and r<=4 and w<=F(4,5) and s<=5:
        if w*s>4: sub=False
chk("A2 box inside d<=4a",sub)
# B2 examples
chk("{1,2,3,4} t=1/5",ok5([1,2,3,4],F(1,5)))
chk("(1,2,5/2,7/2) t=2/9",ok5([1,2,F(5,2),F(7,2)],F(2,9)) and [d(x*F(2,9)) for x in [1,2,F(5,2),F(7,2)]]==[F(2,9),F(4,9),F(4,9),F(2,9)])
# LN: d>=4c, t=Nudge(F4(a,b,c); d)
def LN(a,b,c,dd):
    t0=F4(a,b,c); X=dd*t0
    if d(X)>=D: return t0
    k=fl(X+F(1,2)); e=X-k; s=1 if e>=0 else -1
    return (k+F(s,5))/dd
chk("LN (1,2,3,12) -> 4/15",LN(F(1),F(2),F(3),F(12))==F(4,15) and ok5([1,2,3,12],F(4,15)))
for _ in range(30000):
    xs=sorted({F(random.randint(1,3000),random.randint(1,200)) for _ in range(3)})
    if len(xs)<3: continue
    a,b,c=xs
    dd=4*c+ (0 if random.random()<0.2 else F(random.randint(0,5000),random.randint(1,50)))
    chk(f"LN {a},{b},{c},{dd}",ok5([a,b,c,dd],LN(a,b,c,dd)))
# PLS_delta with delta=1/5,(p,q,r)=(b,c,a) under a(12b+2c)<=3b(b+c): check a,b,c distances >=1/5
def PLS(p,q,r,dl):
    th=p/(p+q); k0=ce(dl*(p+q)/r); x0=k0*th-fl(k0*th)
    j=0 if dl<=x0<=1-dl else ce(((dl-x0)-fl(dl-x0))/th)
    return F(k0+j)/(p+q)
cnt=0
for _ in range(40000):
    a,b,c=sorted(F(random.randint(1,4000),random.randint(1,100)) for _ in range(3))
    if not a<b<c: continue
    if a*(12*b+2*c)<=3*b*(b+c):
        cnt+=1; t=PLS(b,c,a,D); chk(f"PLS {a},{b},{c}",t>0 and min(d(a*t),d(b*t),d(c*t))>=D)
# condition algebra: delta=1/4 reduces to T4 S3 condition; delta=1/5 form
import itertools
for a,b,c in [(F(1),F(4),F(5)),(F(2),F(9),F(11)),(F(1),F(3),F(7))]:
    for dl in [F(1,4),F(1,5)]:
        gen = a*(2+2*dl*(b+c)/b) <= (1-2*dl)*(b+c)
        spec = (a*(5*b+c)<=b*(b+c)) if dl==F(1,4) else (a*(12*b+2*c)<=3*b*(b+c))
        chk(f"cond algebra {a},{b},{c},{dl}",gen==spec)
print("checks",n,"failures",len(fails),fails[:5]); print("LB samples in box",inbox,"; PLS samples",cnt)
print("A2 box LB(1;0,0,0) inside known d<=4a region:",sub)
