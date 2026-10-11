# empty cosets of order-28 subgroup (up to sign: G = <g^((p-1)/28)> union -G, cosets of {±G}) for p≡1 mod 28
from sympy import primerange, primitive_root
import json,math
out=[]
for p in primerange(29,20001):
    if p%28!=1 or 503<=p<=599: continue
    H=(p-1)//16; g=primitive_root(p); h=pow(g,(p-1)//28,p)
    G=set(); x=1
    for _ in range(28): G.add(x); x=x*h%p
    G|={p-y for y in G}   # 28 elements already contain -1? order 28 even so -1 in G
    k=(p-1)//len(G)
    empty=0; seen=set()
    for a in range(1,p):
        if a in seen: continue
        C={a*y%p for y in G}; seen|=C
        if not any(min(c,p-c)<=H for c in C): empty+=1
    out.append((p,len(G),k,empty))
json.dump(out,open('subgroup.json','w'))
print(len(out)); print([o for o in out if o[0]<=1500])
cov=[o[0] for o in out if o[3]==0]; print("covers",cov)
import numpy as np
P=np.array([o[0] for o in out]);E=np.array([o[3] for o in out]);K=np.array([o[2] for o in out])
print("fit empty/p", np.polyfit(P,E,1), "e^-3.5 pred ratio", (E/K)[-50:].mean(), math.exp(-3.5))
