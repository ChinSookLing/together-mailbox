# Test only (not a proof): exact rational checks of PT-008 Q^3 (N=4) and the N=5 a+d=b+c construction.
from fractions import Fraction as F
from math import ceil, floor
import random
def dist(x): x=x-floor(x); return min(x,1-x)
def safe(V,t,d): return all(dist(v*t)>=d for v in V)
def cl(x): return -((-x.numerator)//x.denominator)
def Q(V,t,d):
    return max([t]+[(cl(v*t-(1-d))+d)/v for v in V])
rng=random.Random(20261023); bad=0; worst=F(0); n=0
grid=[F(i,j) for j in range(1,41) for i in range(j,30*j+1)]
cases=[]
for _ in range(200000):
    b=F(rng.randint(10,300),rng.randint(10,100)); c=F(rng.randint(10,2000),rng.randint(1,100))
    if b<1: b=1+b
    if c<b: b,c=c,b
    if b<1: continue
    cases.append((b,c))
for b in [F(1),F(9,5),F(2),F(3),F(301,100)]:
    for c in [F(3)+F(1,1000),F(5)-F(1,1000),F(7),F(9)-F(1,10**6),F(4),F(11,2)]:
        if c>=b: cases.append((b,c))
for b,c in cases:
    V=(F(1),b,c); d=F(1,4); t=F(1,4)
    for _ in range(3): t=Q(V,t,d)
    n+=1
    if not safe(V,t,d): bad+=1; print("Q3 FAIL",b,c,t)
    worst=max(worst,t)
print("Q3 cases",n,"fail",bad,"max t3",float(worst),"(claimed < 3/4)")
# N=5 a+d=b+c
bad=0;n=0
for _ in range(200000):
    D=F(rng.randint(2,4000),rng.randint(1,50))
    a=D*F(rng.randint(1,1000),2001); b=D*F(rng.randint(1,1000),2001)
    if a>b: a,b=b,a
    if a<=0: continue
    c=D-b; dd=D-a; V=(a,b,c,dd); x=a/D; y=b/D
    K=cl(1/(5*x)); J=cl(y*K-F(4,5)); k=max(K,cl((J+F(1,5))/y)); t=k/D
    n+=1
    if not safe(V,t,F(1,5)): bad+=1; print("N5 FAIL",V,t)
print("N5 cases",n,"fail",bad)
