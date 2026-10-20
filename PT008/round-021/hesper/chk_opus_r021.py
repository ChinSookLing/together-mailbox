import sys; sys.path.insert(0,'/workspace/work/pt008r20/hesper')
src=open('/workspace/work/pt008r20/hesper/base.py').read(); exec(src[:src.index("ok=lambda")])
from fractions import Fraction as F
from math import ceil,gcd
from functools import reduce
from itertools import combinations
import random
print('§12 F6:',[nd(F(v)*F(29,24)) for v in (F(1,2),1,30,60,80)], 'F5 base 5/24:',[nd(F(v)*F(5,24)) for v in (1,30,60,80)])
print('PartIII N=1 t=13/51:',F4(1,21,30),[nd(F(v)*F(13,51)) for v in (1,10,21,30)])
print('§7 F4(2,3,4)=',F4(2,3,4))
# FO at n=4 random check
bad=0
for _ in range(3000):
    b,c,d=sorted(F(random.randint(1,400),random.randint(1,40)) for _ in range(3))
    if len({b,c,d})<3: continue
    u=4*d+F(random.randint(0,4000),random.randint(1,60))
    t0=F4(b,c,d); de=F(1,5); ph=fr(u*t0)
    t=t0 if de<=ph<=1-de else (t0+(de-ph)/u if ph<de else t0-(ph-1+de)/u)
    if not (t>0 and min(nd(v*t) for v in (b,c,d,u))>=de): bad+=1
print('FO n=4 random fails:',bad)
# §9 counts
tot=allx0=0
for V in combinations(range(1,31),4):
    tot+=1
    if all(V[i]% reduce(gcd,[V[j] for j in range(4) if j!=i])==0 for i in range(4)): allx0+=1
print('quads',tot,'all-u x=0',allx0)
