from fractions import Fraction as F
import random, math
def nd(x): return abs(x-round(x))
random.seed(1); bad=0; tested=0
for _ in range(20000):
    n1=random.randint(1,6); n=n1+1
    V=set()
    while len(V)<n1: V.add(random.choice([-1,1])*random.randint(1,12))
    V=list(V); M=max(abs(u) for u in V)
    # find t0 safe (grid)
    cands=[F(random.randint(1,4000),random.randint(1,300)) for _ in range(300)]
    t0=next((t for t in cands if all(nd(u*t)>=F(1,n) for u in V)),None)
    if t0 is None: continue
    w=random.choice([-1,1])*random.randint(n*M,n*M+30)
    if w in V or w==0: continue
    d=F(1,n+1); h=F(1,n*(n+1)*M)
    if nd(w*t0)>=d: t1=t0
    else:
        k=round(w*t0); best=None
        for s in(-1,1):
            c=(k+s*d)/w
            if best is None or abs(c-t0)<abs(best-t0): best=c
        t1=best
    tested+=1
    ok=t1>=0 and abs(t1-t0)<=h and all(nd(u*t1)>=d for u in V+[w])
    if not ok: bad+=1
print(tested,bad)
