from fractions import Fraction as F
from math import floor, ceil
def nd(z): return min(z-floor(z), ceil(z)-z)
def lam(u,N):
    d=F(1,N); k=len(u); L=[None]*(k-1); L[k-2]=u[k-2]/u[k-1]*2*d
    for i in range(k-3,-1,-1): L[i]=u[i]/u[i+1]*(1+L[i+1])
    return L
def nw(u,N):
    d=F(1,N); L=lam(u,N); Lft=d/u[0]
    for i in range(1,len(u)-1):
        X=u[i]*Lft; f=X-floor(X)
        p= X if d<=f<=1-d-L[i] else ceil(X-d)+d
        Lft=p/u[i]
    X=u[-1]*Lft
    if nd(X)>=d: return Lft
    k=floor(X+F(1,2)); return (k+d)/u[-1]
print('Argon V2 lambdas',lam([F(1),F(2),F(3),F(9,2)],5),'limit 3/5')
print('DS NW old (1,3,16/5) N=4',lam([F(1),F(3),F(16,5)],4))
print('DS NW new +1000 N=5',[str(x) for x in lam([F(1),F(3),F(16,5),F(1000)],5)], float(lam([F(1),F(3),F(16,5),F(1000)],5)[1]))
u=[F(1),F(3),F(21,5)]; print('DS window ex lambdas',lam(u,4)); t=nw(u,4); print(' t',t,[str(nd(x*t)) for x in u])
e=F(1,10**6); print(' t+e',[str(nd(x*(t+e))) for x in u],' t-e',[str(nd(x*(t-e))) for x in u])
V=[F(1),F(3),F(4),F(7)]; print('Argon V3 at 2/(a+d)=1/4',[str(nd(x*F(1,4))) for x in V])
# Argon Qwen-region review: slip "a<c/4 (if c<4a)": c<4a gives a>c/4; bound ct>=1/5 still follows from a<c, d<4c -> a+d<5c
