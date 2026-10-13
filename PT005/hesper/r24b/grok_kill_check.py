import numpy as np, math
v=[1241704,16610357,19741875,6226020,23726552,24987200,3615232,16539132,21692574,27829418,35651584,35389320,31852632,7434320,524584]
W5=[189,224,72,447,176,500,144,128,384,266,80,64,48,32,16]
p=17;k=21;N=2**k*p
print("mod17",[x%17 for x in v])
print("expected row",[x%17 for x in W5])
print("descends from W5 (x ≡ W5 mod 32p)?",[ (x-w)%(32*p)==0 for x,w in zip(v,W5)])
print("in range [1,N)?",[0<x<N for x in v])
def v2(x): return (x&-x).bit_length()-1 if x else 99
print("v2",[v2(x) for x in v],"frozen",sum(v2(x)<k for x in v),"odd",sum(x%2 for x in v))
# improper check with actual values
T=np.arange(1,N//2+1,dtype=np.int64)
cov=np.zeros(len(T),bool)
for w in v:
    r=(T*w)%N; m=np.minimum(r,N-r); cov|=16*m<N
print("all covered:",cov.all(),"uncovered count",(~cov).sum())
