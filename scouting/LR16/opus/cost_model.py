import json, math
from sympy import primerange
g = json.load(open('ms15/inputs/gates.json'))
# per-prime total CPU (k=14) from gates.json timing where available
rows=[]
for p,d in g.items():
    t=d.get('timing',{})
    cpu=sum(v for kk,v in t.items() if kk.endswith('cpu_secs'))+t.get('precondition_secs',0)+d.get('kills_cpu_secs',0)
    rows.append((int(p),cpu))
rows.sort()
tot=sum(c for _,c in rows)
print("k=14 primes in gates.json:",len(rows),"sum CPU-s (gen+precond+kill, excl. binary lifting):",round(tot))
big=[(p,c) for p,c in rows if p>=307]
# fit c = A p^e on p>=307
import numpy as np
x=np.log([p for p,_ in big]); y=np.log([max(c,1) for _,c in big]); e,lnA=np.polyfit(x,y,1)
print(f"fit on p>=307: CPU ~ p^{e:.2f}")
P14=[p for p,_ in rows]
def model(ps): return sum(math.exp(lnA)*p**e for p in ps)
base=model(P14)
print("model total for actual k=14 set:", round(base))
T=497.03-math.log(720720)
for p0 in (89,131,199,239):
    s=0; ps=[]
    for p in primerange(p0,2000):
        ps.append(p); s+=math.log(p)
        if s>T: break
    r=model(ps)/base
    print(f"k=15 set from {p0} to {ps[-1]} ({len(ps)} primes): p^e-model cost = {r:.2f} x the 15-runner run (before k-factor F)")
