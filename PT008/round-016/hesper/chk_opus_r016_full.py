from fractions import Fraction as F
from math import floor
import random
def nd(z): return min(z-floor(z), floor(z)+1-z)
def rnd(x): return floor(x+F(1,2))
d5=F(1,5)
def ets(V,maxit=10000):
    t=d5/min(V); path=[]
    for _ in range(maxit):
        U=[u for u in V if nd(u*t)<d5]
        if not U: return t,path
        tau={u:(rnd(u*t)+d5)/u for u in U}; u=max(tau,key=tau.get); path.append((u,rnd(u*t))); t=tau[u]
    return None,path
for name,V in [('V1',(1,F(11,10),3,F(41,10))),('V2',(1,2,3,F(9,2))),('V3',(1,3,4,7)),('Argon',(1,2,3,F(27,4))),('V4',(1,30,60,80)),('P',(1,2,F(16,5),F(9,2)))]:
    V=tuple(map(F,V)); t,p=ets(V); print(name,'ETS t=',t,'steps',len(p),[str(nd(u*t)) for u in V])
# Q-B2 at P
P=tuple(map(F,(1,2,F(16,5),F(9,2)))); t=F(2)/(P[1]+P[2]); print('Q-B2 P t=',t,[str(nd(u*t)) for u in P])
# B4 box
random.seed(4); bad=0; s1=0; nw=0; N=20000
def R(lo,hi,strict=False):
    x=lo+(hi-lo)*F(random.randint(1,10**6-1),10**6); return x
for _ in range(N):
    a=F(1); b=R(F(29),F(31)); c=b*R(F(61,31),F(64,31)); d=b*R(F(81,31),F(84,31))
    t=F(31,5)/b
    if min(nd(u*t) for u in (a,b,c,d))<d5: bad+=1
    th=b/(b+c); mu=c/(5*d)
    if th<=F(3,5)-2*mu: s1+=1
    if (b/c)*(1+2*c/(5*d))<=F(3,5): nw+=1
print('B4 random',N,'fail',bad,'S1 holds',s1,'NW lambda2<=3/5',nw)
# ETS vs brute first success on small integer quadruples
random.seed(1); mism=0; M=300
for _ in range(M):
    V=sorted(random.sample(range(1,40),4)); V=tuple(map(F,V)); t,p=ets(V)
    # brute: first success among candidate lower edges up to t
    cand=sorted({(k+d5)/u for u in V for k in range(0,int(u*t)+2)})
    first=next(x for x in cand if x>=d5/V[0] and min(nd(u*x) for u in V)>=d5)
    if first!=t: mism+=1
print('ETS vs brute first lower-edge success on',M,'integer quads: mismatches',mism)
