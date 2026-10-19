from fractions import Fraction as F
from math import floor, ceil
d5=F(1,5)
def nd(z): return min(z-floor(z), ceil(z)-z)
def g(V,t): return min(nd(v*t) for v in V)
def comp(V,t0,span):
    # edges near t0, find component containing t0 exactly
    lo,hi=t0-span,t0+span; E=set()
    for v in V:
        for j in range(floor(v*lo)-1,ceil(v*hi)+1):
            for ph in (d5,1-d5):
                e=(j+ph)/v
                if lo<=e<=hi: E.add(e)
    E=sorted(E|{t0}); i=E.index(t0)
    L=t0
    for k in range(i-1,-1,-1):
        m=(E[k]+E[k+1])/2
        if g(V,m)>=d5 and g(V,E[k])>=d5: L=E[k]
        else: break
    R=t0
    for k in range(i+1,len(E)):
        m=(E[k-1]+E[k])/2
        if g(V,m)>=d5 and g(V,E[k])>=d5: R=E[k]
        else: break
    return L,R
W={'V1':(1,F(11,10),3,F(41,10)),'V2':(1,2,3,F(9,2)),'V3':(1,3,4,7),'V4':(1,30,60,80)}
W={k:tuple(F(x) for x in v) for k,v in W.items()}
for k,t in [('V2',F(2,5)),('V2',F(4,5)),('V3',F(1,5)),('V3',F(4,5)),('V4',F(2,9))]:
    V=W[k]; print(k,t,[str(nd(v*t)) for v in V],'component',[str(x) for x in comp(V,t,F(1,10))])
for t in (F(11,50),F(89,400)): print('V4 end',t,[str(nd(v*t)) for v in W['V4']])
def inb(r,lo,hi,step):  # r in union [step*m+lo, step*m+hi] scaled
    return any(lo<= r*1 - 0 for _ in [0]) 
def AL(V): a=V[0]; return all(1<= (u/a)%5 <=4 for u in V[1:])
def AU(V): a=V[0]; return all(1<= (4*u/a)%5 <=4 for u in V[1:])
for k,V in W.items(): print(k,'AL',AL(V),'AU',AU(V), 'g(1/5a)',g(V,1/(5*V[0])),'g(4/5a)',g(V,4/(5*V[0])))
# random: AL/AU predicate == success at that t
import random; random.seed(15); bad=0
for _ in range(20000):
    V=sorted({F(random.randint(100,3000),100) for _ in range(4)})
    if len(V)<4: continue
    a=V[0]
    if AL(V)!=(g(V,1/(5*a))>=d5) or AU(V)!=(g(V,4/(5*a))>=d5): bad+=1
print('TE predicate mismatches',bad)
# obstruction: u/a in 5Z => every edge of a fails
V=W['V4']; print('V4 a-edges fail', all(g(V,(j+ph)/V[0])<d5 for j in range(0,200) for ph in (d5,1-d5)))
