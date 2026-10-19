# Hesper exact-Fraction check of Qwen R014 2/4 (both versions)
from fractions import Fraction as F
from math import floor, ceil
import random
def nd(z): return min(z-floor(z), ceil(z)-z)
def good(V,t): return t>0 and all(nd(u*t)>=F(1,5) for u in V)
def wl(a,b,c,d):
    tL=1/(5*a); X=d*tL
    return tL if nd(X)>=F(1,5) else (floor(X+F(1,2))+F(1,5))/d
fr=lambda V:[str(nd(u*t)) for u in V]
# (1,3,4,5) t=9/20
V=[F(1),F(3),F(4),F(5)]; t=F(9,20); print('(1,3,4,5) t=9/20',fr(V),good(V,t))
# P1 random closed: 5c/2-a <= d <= 9a, a<b<c<d
random.seed(14); tot=bad=0
for _ in range(60000):
    a=F(1); c=F(random.randint(101,400),100); b=a+(c-a)*F(random.randint(1,999),1000)
    lo=max(F(5,2)*c-a,c); hi=9*a
    if lo>hi: continue
    d=lo+(hi-lo)*F(random.randint(0,1000),1000)
    if d<=c: continue
    tot+=1; t=2/(a+d)
    if not good([a,b,c,d],t): bad+=1; print('P1 FAIL',a,b,c,d)
print('P1 closed random',tot,'fail',bad)
# P1 extension example
V=[F(1),F(6,5),F(3,2),F(3)]; t=F(1,2); print('P1 ext (1,1.2,1.5,3)',fr(V),good(V,F(1,2)))
# B1 selector random over c<=36a/11, d>=D1 (bounded d<=60a)
tot=bad=0
for _ in range(60000):
    a=F(1); c=F(random.randint(101,327),100); 
    if c>F(36,11): continue
    b=a+(c-a)*F(random.randint(1,999),1000)
    D1=F(5,2)*c-a; D2=2*a*c/(4*a-c); lo=max(D1,c)
    d=lo+F(random.randint(1,60000),1000)
    if d<=c: continue
    t= wl(a,b,c,d) if d>=D2 else 2/(a+d)
    tot+=1
    if not good([a,b,c,d],t): bad+=1; print('B1 FAIL',a,b,c,d,t)
print('B1 selector random',tot,'fail',bad)
# thresholds
import math
x0=(9+math.sqrt(41))/5; print('x0',x0,' 36/11',36/11)
for a,b,c,d in [(10,20,31,68),(11,20,36,80)]:
    V=[F(x) for x in (a,b,c,d)]; D1=F(5,2)*c-a; D2=F(2*a*c,4*a-c); t=F(2,a+d)
    cert=dict(TN=d<=4*a,LN=d>=4*c,WL=d>=D2,K5=3*c<=8*a)
    s=F(b+c,a); r=F(c,b); w=F(d,b+c)
    HB=F(15,8)<=s<=F(15,2) and ((1<r<=F(8,7)) or (4<=r<=F(13,2))) and F(4,5)<=w<=F(6,5)
    print((a,b,c,d),'D1',D1,'D2',D2,'t',t,fr(V),good(V,t),cert,'HB',HB,'C1 r<=8/7',r<=F(8,7))
# SLN-odd example (1,10,11,20) k=5 vs 6
V=[F(1),F(10),F(11),F(20)]
for k in (5,6): t=F(k,21); print('SLNodd ex k',k,fr(V),good(V,t))
# QwenA claim check: for c<x0, region lower bound >= WL bound (region inside WL)
for c in [F(11,4),F(3),F(31,10)]:
    a=F(1); print('c',c,'WL bound',2*a*c/(4*a-c),'region lower',max(4*a,(5*c-2*a)/2))
