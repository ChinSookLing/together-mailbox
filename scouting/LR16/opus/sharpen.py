import math
from sympy import primerange
e=5.91
T0=497.03-math.log(720720)
print(f"target sum log p (R_15<1/2 assumed): {T0:.4f}")
def setfor(T,p0):
    s=0;ps=[]
    for p in primerange(p0,3000):
        ps.append(p); s+=math.log(p)
        if s>T: return ps
for p0 in (89,131,199):
    base=sum(p**e for p in setfor(T0,p0))
    out=[]
    for d in (0,10,30,50,80):
        ps=setfor(T0-d,p0); c=sum(p**e for p in ps)/base
        out.append(f"-{d}: {len(ps)} primes, max {ps[-1]}, cost {c:.2f}")
    print(f"from {p0}: "+" | ".join(out))
