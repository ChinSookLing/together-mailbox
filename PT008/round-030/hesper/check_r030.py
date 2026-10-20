from fractions import Fraction as F
import random, math
random.seed(20261020)
def nd(x): x=x-math.floor(x); return min(x,1-x)
# Route A interval formula
bad=0;app=0
for _ in range(20000):
    d=F(1,random.randint(3,12)); u=F(random.randint(1,400),random.randint(1,40))
    L=F(random.randint(0,4000),random.randint(1,400)); R=L+F(random.randint(0,400),random.randint(1,400))
    m=math.ceil(u*L-(1-d))
    if m<=math.floor(u*R-d):
        app+=1; t=max(L,(m+d)/u)
        if not (L<=t<=R and nd(u*t)>=d): bad+=1
print('A: applicable',app,'fail',bad)
# Route B: q=floor(v t) from a safe t satisfies pair inequalities; output t safe
badB=0;tested=0
for _ in range(3000):
    n=random.randint(3,7); d=F(1,n)
    v=[F(random.randint(1,60),random.randint(1,6)) for _ in range(n-1)]
    # find a safe t by rational grid on a window
    found=None
    for k in range(1,4000):
        t=F(k,997)
        if all(nd(x*t)>=d for x in v): found=t;break
    if found is None: continue
    tested+=1
    q=[math.floor(x*found) for x in v]
    ok=all(v[j]*q[i]-v[i]*q[j] <= (1-d)*v[i]-d*v[j] for i in range(n-1) for j in range(n-1))
    t2=max((q[i]+d)/v[i] for i in range(n-1))
    ok2= t2>0 and all(nd(x*t2)>=d for x in v)
    if not(ok and ok2): badB+=1
print('B: tested',tested,'fail',badB)
