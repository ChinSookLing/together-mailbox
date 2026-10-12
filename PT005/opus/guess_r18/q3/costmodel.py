# Chair, 2026-10-13: cost law for part (a) of the gate, fitted on the 10 gates with full node counts.
import numpy as np, math
from sympy import primerange
data={191:2.51e9,223:1.02e10,233:2.72e10,239:1.87e10,241:7.75e10,307:3.35e11,337:7.31e11,383:5.19e11,401:1.93e12,409:1.34e12}
r=lambda p:((p-1)//2)/((p-1)//16)          # n/H
P=np.array(list(data)); Y=np.log(np.array(list(data.values())))
X=np.c_[np.ones(len(P)),np.log(P),[r(p) for p in P]]
c=np.linalg.lstsq(X,Y,rcond=None)[0]; print('log nodes = %.3f + %.3f log p %+.3f (n/H)'%tuple(c))
errs=[]
for i in range(len(P)):
    m=np.ones(len(P),bool); m[i]=False; ci=np.linalg.lstsq(X[m],Y[m],rcond=None)[0]; errs.append(abs(X[i]@ci-Y[i]))
print('leave-one-out error: median x%.2f, max x%.2f'%(math.exp(np.median(errs)),math.exp(max(errs))))
cpuh=lambda p: math.exp(c[0]+c[1]*math.log(p)+c[2]*r(p))/2.5e6/3600   # office ~2.0-3.1e6 nodes per CPU-s
closed={191,223,233,239,241}; done_a={307,337,383,401,409}
need=481.07-sum(math.log(p) for p in closed); s=0; tot=0; cnt=0
for p in primerange(251,1026):
    if p in closed: continue
    s+=math.log(p); tot+=0 if p in done_a else cpuh(p); cnt+=1
    if s>=need: break
print('ascending ladder: %d more primes, up to p=%d, about %.0f office CPU-hours (%.0f days on 8 workers)'%(cnt,p,tot,tot/8/24))
