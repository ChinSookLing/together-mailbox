from fractions import Fraction as F
from math import floor
def nd(z): return min(z-floor(z), floor(z)+1-z)
d5=F(1,5)
def ok(V,t): return min(nd(u*t) for u in V)>=d5
# C4: menu with M (max tau), Kmax; N>5M, N>Kmax
for M,K in [(5,3),(20,10),(31,40)]:
    N=max(5*M,K)+1; V=(F(1),F(5*N),F(10*N),F(5*N*(3*N+1)))
    taus=[F(j,4) for j in range(1,4*M+1)]
    menu=[(k+c)/v for v in V for k in range(K+1) for c in (F(1,5),F(4,5))]
    menu+=[tau/(V[i]+V[j]) for i in range(4) for j in range(i+1,4) for tau in taus]
    hits=[t for t in menu if ok(V,t)]
    # find some solution by scanning t=j/(5*den)
    sol=None
    for j in range(1,20000):
        t=F(j,200)
        if ok(V,t): sol=t;break
    print('M',M,'K',K,'N',N,'menu size',len(menu),'menu successes',len(hits),'a solution t=',sol)
# NF-20 box conversion
print('r range',1/F(34,100)-1,1/F(31,100)-1)
