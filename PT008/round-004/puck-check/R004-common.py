from fractions import Fraction as F
import math, random
def nd(x):
    f = x - math.floor(x)
    return min(f, 1-f)
def g(V,t): return min(nd(abs(u)*t) for u in V)
def slopes(a,t):
    x=abs(a)*t; f=x-math.floor(x)
    right = a if f<F(1,2) else -a   # a>0
    left = a if (F(0)<f<=F(1,2)) else -a
    return left,right
def is_locmax(V,t):
    gt=g(V,t)
    if gt==0: return False
    act=[a for a in V if nd(a*t)==gt]
    L=max(slopes(a,t)[0] for a in act); R=min(slopes(a,t)[1] for a in act)
    return L>0 and R<0
def is_locmin(V,t):
    gt=g(V,t)
    act=[a for a in V if nd(a*t)==gt]
    L=min(slopes(a,t)[0] for a in act); R=max(slopes(a,t)[1] for a in act)
    # g left slope = max over active left slopes ; right = min over active right slopes
    L=max(slopes(a,t)[0] for a in act); R=min(slopes(a,t)[1] for a in act)
    return L<0 and R>0
def all_candidates(V,T):
    """every breakpoint of g in (0,T]: peaks, zeros, sum & diff crossings"""
    S=set()
    for a in V:
        k=1
        while F(k,2*a)<=T: S.add(F(k,2*a)); k+=1
    for i,a in enumerate(V):
        for b in V[i+1:]:
            for den in (a+b,abs(a-b)):
                k=1
                while F(k)/den<=T: S.add(F(k)/den); k+=1
    return sorted(S)
def locmaxes(V,T): return [t for t in all_candidates(V,T) if is_locmax(V,t)]
def rnd_speeds(m,mx=12,rat=False):
    s=set()
    while len(s)<m:
        s.add(F(random.randint(1,mx*(4 if rat else 1)),random.randint(1,4) if rat else 1))
    return sorted(s)
