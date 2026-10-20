import sys; sys.path.insert(0,'/workspace/work/pt008r20/hesper')
from fractions import Fraction as F
from math import floor, ceil
exec(open('/workspace/work/pt008r20/hesper/base.py').read().split('A=lambda')[0]+'\n')
def nd(z): return min(z-floor(z), floor(z)+1-z)
fifth=F(1,5)
print('T4(1,2,3)=',F4(1,2,3))
rho=min(F(1,20)/v for v in (1,2,3)); print('rho',rho,'J',F(1,4)-rho,F(1,4)+rho,'4J',4*(F(1,4)-rho),4*(F(1,4)+rho))
print('max ||4t|| on J endpoints', nd(4*(F(1,4)-rho)), nd(4*(F(1,4)+rho)))
print('t=1/5 dists',[str(nd(v*F(1,5))) for v in (1,2,3,4)])
def fw4(V):
    a=V[0]; best=None
    pts=set()
    for v in V:
        j=0
        while (j-fifth)/v < 1/a:
            for x in (j+fifth,j-fifth):
                t=x/v
                if 0<t<1/a: pts.add(t)
            j+=1
    for t in sorted(pts):
        if min(nd(v*t) for v in V)>=fifth: return t
    return None
n=fails=0; worst=None
N=24
for a in range(1,N+1):
 for b in range(a+1,N+1):
  for c in range(b+1,N+1):
   for d in range(c+1,N+1):
    if d>4*a and d<4*c:
      n+=1; t=fw4((a,b,c,d))
      if t is None: fails+=1; print('NO first-window t',a,b,c,d)
print('remaining-region integer quadruples <=',N,':',n,'with no first-window safe t:',fails)
