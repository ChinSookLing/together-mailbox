# Hesper exact-Fraction check of Opus R014 1/4 (FNW, persistence, A5, Qwen review)
from fractions import Fraction as F
from math import floor, ceil
import random, itertools
def nd(z): return min(z-floor(z), ceil(z)-z)
def fr(z): return z-floor(z)
def rnd(x): return floor(x+F(1,2))
def fnw(V,N,trace=False):
    d=F(1,N); k=len(V); out=[]
    for p in range(1,k):
        if V[p-1]>(N-1)*V[0]: break
        lo=d/V[0]; hi=(1-d)/V[p-1]; ok=True
        for i in range(p,k-1):
            u=V[i]; L=u*(hi-lo); X=u*lo
            if L<=1: ok=False;break
            lam=min(1-2*d,L-1)
            q = X if d<=fr(X)<=1-d-lam else ceil(X-d)+d
            lo=q/u; hi=lo+lam/u
        if not ok: out.append((p,'mid-fail')); continue
        u=V[-1]; X=u*lo
        if nd(X)>=d: return p,lo,out
        if u*(hi-lo)>=2*d: return p,(rnd(X)+d)/u,out
        out.append((p,'last-fail'))
    return None,None,out
def good(V,t,N): return t>0 and all(nd(u*t)>=F(1,N) for u in V)
W={'V1':[F(1),F(11,10),F(3),F(41,10)],'V2':[F(1),F(2),F(3),F(9,2)],'V3':[F(1),F(3),F(4),F(7)],'V4':[F(1),F(30),F(60),F(80)]}
for n,V in W.items():
    p,t,fails=fnw(V,5); print(n,'p=',p,'t=',t,'fails',fails, 'dists',[str(nd(u*t)) for u in V] if t else '', 'ok',good(V,t,5) if t else None)
# random test FNW N=4..7
random.seed(19); bad=0; cov=0; tot=0
for N in range(4,8):
    for _ in range(3000):
        V=sorted(set(F(random.randint(1,400),random.randint(1,40)) for _ in range(N-1)))
        if len(V)<N-1: continue
        tot+=1; p,t,_=fnw(V,N)
        if t is not None:
            cov+=1
            if not good(V,t,N): bad+=1; print('FAIL',V,t)
print('FNW random: sets',tot,'covered',cov,'failures',bad)
# A5: {1..N-1} successful t in [0,1) on fine grid all in (1/N)Z
for N in range(3,9):
    den=N*60; S=[F(j,den) for j in range(1,den) if good(list(range(1,N)),F(j,den),N)]
    print('A5 N',N,'successes on grid 1/%d:'%den,[str(x) for x in S], 'all in (1/N)Z', all((x*N).denominator==1 for x in S))
# A4 thresholds
for N in [5]: d=F(1,N); print('N/(N-2)',1/(1-2*d),'2(N-1)/(N-2)',(2-2*d)/(1-2*d))
# Qwen region, closed, random exact + Opus examples
bad=0;tot=0
for _ in range(40000):
    a=F(1); c=F(random.randint(67,399),100)   # c>2a/3.. c<4
    b=a+(c-a)*F(random.randint(1,999),1000) if c>a else None
    if b is None or not a<b<c: continue
    lo=max(4*a,(5*c-2*a)/2,c); hi=min(9*a,4*c)
    if lo>hi: continue
    d=lo+(hi-lo)*F(random.randint(0,1000),1000)
    if d<=c: continue
    tot+=1; t=2/(a+d)
    if not good([a,b,c,d],t,5): bad+=1; print('QFAIL',(a,b,c,d))
print('Qwen closed region random:',tot,'failures',bad)
for V in [(1,2,F(7,2),8),(1,2,F(7,2),9),(1,F(3,2),F(7,2),F(31,4))]:
    V=[F(x) for x in V]; t=2/(V[0]+V[3]); print('example',V,'t',t,[str(nd(u*t)) for u in V],good(V,t,5))
a=F(1);c=F(36,11); print('36/11 WL bound',2*a*c/(4*a-c))
