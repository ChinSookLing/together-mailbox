# Puck exact check of formulas stated in GPT-6 R010 chair ruling. Exact Fractions only.
from fractions import Fraction as F
import itertools, random
def nd(x): x=x-(x.numerator//x.denominator); return min(x,1-x)
def fr(x): return x-(x.numerator//x.denominator)
fails=0; n=0
# 1) LN: d>=4c, t0 with ||u t0||>=1/4 (u=a,b,c); nudge to nearest t with ||dt||=1/5; check |t-t0|<=1/(5d)<=1/(20c) and ||ut||>=1/5
random.seed(8)
def nudge(d,t0):
    x=d*t0; k=x.numerator//x.denominator; f=x-k
    if F(1,5)<=f<=F(4,5): return t0
    if f<F(1,5):
        cand=[ (k-F(1,5))/d, (k+F(1,5))/d ]
    else:
        cand=[ (k+F(4,5))/d, (k+1+F(1,5))/d ]
    cand=[c for c in cand if c>=0]
    return min(cand,key=lambda c:(abs(c-t0),-c))
ln=0
for _ in range(40000):
    # random t0 and a<b<c with ||u t0||>=1/4 by construction: pick u t0 frac in [1/4,3/4]
    t0=F(random.randint(1,4000),random.randint(1,400))
    us=sorted(set((random.randint(0,30)+F(random.randint(250,750),1000))/t0 for _ in range(3)))
    if len(us)<3: continue
    a,b,c=us
    d=4*c+F(random.randint(0,4000),random.randint(1,97))
    t=nudge(d,t0); n+=1; ln+=1
    ok = t>=0 and abs(t-t0)<=F(1,5)/d<=F(1,20)/c and all(nd(u*t)>=F(1,5) for u in (a,b,c,d))
    if not ok: fails+=1; print("LN FAIL",a,b,c,d,t0,t)
print("LN checks",ln)
# 2) C1 two-branch rule as stated by chair (s=(b+c)/a, r=c/b, w=d/(b+c))
c1=0; b2set=[]
S=[F(15,8)+F(i,40)*(5-F(15,8)) for i in range(41)]
Rr=[1+F(i,60)*F(1,7) for i in range(1,61)]
W=[F(4,5)+F(i,200) for i in range(201)]
for s,r,w in itertools.product(S,Rr,W):
    a=F(1); b=s/(1+r); c=r*b; d=w*(b+c)
    if fr(w)>=F(1,5) and fr(w)<=F(4,5): t=1/(b+c); br=1
    else: t=F(3,2)/(b+c); br=2; b2set.append(w)
    n+=1; c1+=1
    if not all(nd(u*t)>=F(1,5) for u in (a,b,c,d)): fails+=1; print("C1 FAIL",s,r,w)
    if br==1:
        assert F(1,5)<=1/s<=F(8,15) and F(7,15)<=b*t<=F(8,15) and F(7,15)<=c*t<=F(8,15)
    else:
        assert F(3,10)<=F(3,2)/s<=F(4,5) and F(7,10)<=b*t<=F(4,5) and F(7,10)<=c*t<=F(4,5)
print("C1 checks",c1,"branch2 w range",min(b2set),max(b2set),"w=4/5 in branch2:",F(4,5) in b2set,"w=1 in branch2:",F(1) in b2set)
# 3) integer-lock obstruction d=j(b+c)
ob=0
for j in (1,2,3):
  for k in range(1,50):
    for (b,c) in [(F(3),F(4)),(F(216,100),F(234,100)),(F(7),F(9))]:
      t=F(k)/(b+c); d=j*(b+c); n+=1; ob+=1
      if nd(d*t)!=0: fails+=1; print("OBS FAIL")
print("obstruction checks",ob)
print("TOTAL",n,"FAILURES",fails)
