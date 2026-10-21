from fractions import Fraction as F
from math import ceil,floor
from itertools import combinations
d=F(1,5)
def nd(x): return min(x-floor(x),floor(x)+1-x)
def greedy(V,pick=min):
    al,be=d/V[0],(1-d)/V[0]
    for v in V[1:]:
        lo,hi=ceil(v*al-(1-d)),floor(v*be-d)
        if lo>hi: return None
        q=lo if pick is min else hi
        al,be=max(al,(q+d)/v),min(be,(q+1-d)/v)
    return al
V=[F(1),F(2),F(3),F(41,10)]
print("greedy-min (1,2,3,41/10):",greedy(V))
t=F(2,5);print("t=2/5 dists:",[nd(v*t) for v in V])
# q3=1 branch
al,be=max(F(1,5),(1+d)/3),min(F(2,5),(2-d)/3);print("I3' =",al,be,"J4=",F(41,10)*al-(1-d),F(41,10)*be-d)
# fact: greedy-min failures among int quads <=24
n=f=0
for Q in combinations(range(1,25),4):
    n+=1; t=greedy([F(x) for x in Q])
    if t is None: f+=1
    else: assert 0<t<F(1,Q[0]) and all(nd(x*t)>=d for x in Q)
print("int quads<=24:",n,"greedy-min fails:",f)
