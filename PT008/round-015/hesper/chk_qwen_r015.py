from fractions import Fraction as F
from math import floor, ceil
import random
def nd(z): return min(z-floor(z), ceil(z)-z)
def ok(V,t): return all(nd(v*t)>=F(1,5) for v in V)
def QB2(a,b,c,d):
    S=b+c; return F(3,2)<=c/b<=9 and S/a<=10 and F(3,5)<=d/S<=F(9,10)
W={'V1':(1,F(11,10),3,F(41,10)),'V2':(1,2,3,F(9,2)),'V3':(1,3,4,7),'V4':(1,30,60,80)}
for k,v in W.items():
    a,b,c,d=map(F,v); S=b+c
    print(k,'c/b',c/b,'s',S/a,'w',d/S,'QB2',QB2(a,b,c,d), [str(nd(x*2/S)) for x in (a,b,c,d)])
random.seed(152); tot=bad=0
for _ in range(80000):
    a=F(1); b=a+F(random.randint(1,4000),1000); c=b*(F(3,2)+F(random.randint(0,7500),1000))
    S=b+c
    if S/a>10: continue
    d=S*(F(3,5)+F(random.randint(0,300),1000))
    if not (d>c and QB2(a,b,c,d)): continue
    tot+=1
    if not ok((a,b,c,d),2/S): bad+=1; print('FAIL',a,b,c,d)
print('QB2 closed-region random',tot,'fail',bad)
# endpoint cases exact
for v in [(1,2,3,F(9,2)),(1,F(1,2)*1+F(1,2),F(9,1),F(9,1))]: pass
