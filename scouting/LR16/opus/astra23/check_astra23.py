# Chair check of Astra turn 23: family lemma tiers, failing distributions, 16^4 completion test, p=17 example
from itertools import product
from math import gcd, ceil
def S(ws, D):
    E=[w for w in ws if w%D]; return len(E), sum(gcd(D,w)*ceil((D//gcd(D,w))/8) for w in E)
def handled(ws):
    if sum(w%2 for w in ws)<=1: return "gcd"
    for D in (2,4,8,16):
        e,s=S(ws,D)
        if e>=2 and s<D: return f"L7 D={D}"
    return None
rep={'a':1,'b':2,'c':4,'d':8,'z':16}
fails=[]
for a in range(16):
  for b in range(16-a):
    for c in range(16-a-b):
      for d in range(16-a-b-c):
        z=15-a-b-c-d
        ws=[1]*a+[2]*b+[4]*c+[8]*d+[16]*z   # class representatives; S depends only on gcd with 16
        if handled(ws) is None: fails.append((a,b,c,d,z))
print("failing distributions:",len(fails),"max z:",max(f[4] for f in fails))
print("with z=10:",[f for f in fails if f[4]==10])
print("tier13 (>=13 div by 4) fails:",[f for f in fails if f[2]+f[3]+f[4]>=13])
print("tier12 (>=12 div by 8) fails:",[f for f in fails if f[3]+f[4]>=12])
print("tier11 (>=11 div by 16) fails:",[f for f in fails if f[4]>=11])
# 16^4 completion test: 11 coordinates = 0 mod 16, 4 free residues
unc=0
for r in product(range(16),repeat=4):
    ws=[16]*11+[x if x else 16 for x in r]
    if handled(ws) is None: unc+=1
print("UNCERTIFIED_COMPLETIONS:",unc)
# includes D=2: does D=2 ever matter? S_2 = a (each odd: g=1,ceil(2/8)=1) -> a<2 means a<=1, gcd branch anyway
# p=17 example
w=[2,28,39,44,46,64,65,76,84,93,95,107,121,124,126]; p=17; M=16*p
print("distinct",len(set(w))==15,"nonzero mod17",all(x%p for x in w))
print("sign classes mod17:",sorted({min(x%p,p-x%p) for x in w}))
cls=sorted({min(x%p,p-x%p) for x in w})
print("classes cover all nonzero t mod 17:",all(any(16*min(s*t%p,p-s*t%p)<p for s in cls) for t in range(1,p)))
good=[T for T in range(M) if all(16*min(T*x%M,M-T*x%M)>=M for x in w)]
print("grid-good T on 16p grid:",good)
print("odd count",sum(x%2 for x in w),"L7 budgets",[S(w,D)[1] for D in (2,4,8,16)],"handled:",handled(w))
from fractions import Fraction as F
dist=min(min((F(1,10)*x)%1,1-(F(1,10)*x)%1) for x in w); print("min distance at t=1/10:",dist)
