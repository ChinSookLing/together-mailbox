# R47D(1) measurement, chair. For each k>=1 node (sample) and each EVEN coordinate i (v2(w_i)<k):
# unit times U_i = odd T<=M where i is the ONLY coordinate reaching T at child level 2M
# (reach: 16*||T(w+bM)||_{2M} < 2M for some b  <=>  16*||T w||_{2M} < 2M or 16*||T w - M||_{2M} < 2M).
# h(T)=0 if bit 0 covers, 1 if bit 1 covers. Record depth d=k-v2(w), |U|, #h0, #h1.
import gzip,csv,random,sys,numpy as np
from collections import Counter,defaultdict
seed=int(sys.argv[1]); nsamp=int(sys.argv[2])
rows=[]
with gzip.open("/home/claude/together-mailbox/PT005/hesper/r45/widen/nodes_widen.csv.gz","rt") as f:
    rd=csv.reader(f); next(rd)
    for r in rd:
        if int(r[1])>=1: rows.append((int(r[0]),int(r[1]),int(r[2]),r[3],int(r[10])))
rng=random.Random(seed); S=rng.sample(rows,nsamp)
def v2(x):
    c=0
    while x%2==0: x//=2;c+=1
    return c
tab=defaultdict(Counter)   # (dead?, depth) -> Counter of category
for p,k,M,cs,nopen in S:
    w=np.array([int(x) for x in cs.split()],dtype=np.int64); N=2*M
    T=np.arange(1,M+1,2,dtype=np.int64)[:,None]
    r0=(T*w)%N; d0=np.minimum(r0,N-r0); c0=16*d0<N
    r1=(T*(w+M))%N; d1=np.minimum(r1,N-r1); c1=16*d1<N
    reach=c0|c1; unit=reach.sum(axis=1)==1
    dead=int(nopen==0)
    for i,x in enumerate(w):
        x=int(x)
        if x%2==1: continue
        j=v2(x)
        if j>=k: continue
        d=k-j
        U=unit & reach[:,i]
        n0=int((U & c0[:,i]).sum()); n1=int((U & c1[:,i]).sum())
        n=n0+n1
        cat = "n0" if n==0 else ("one" if n==1 else ("both" if n0 and n1 else "same"))
        tab[(dead,d)][cat]+=1
        if n>=2: tab[(dead,d)]["n>=2"]+=1; tab[(dead,d)]["rand_exp_both"]+=1-2.0**(1-n//2); tab[(dead,d)]["odd_n"]+=n%2
print("seed",seed,"nodes",nsamp)
print("dead depth | even coords | |U|=0 | |U|=1 | |U|>=2 same half | |U|>=2 both halves | both/(n>=2) | random-model E[both]/(n>=2)")
for key in sorted(tab):
    c=tab[key]; tot=c["n0"]+c["one"]+c["same"]+c["both"]; m=c["n>=2"]
    print(key, "odd|U|:",c["odd_n"], tot, c["n0"], c["one"], c["same"], c["both"], f"{c['both']/m:.4f}" if m else "-", f"{c['rand_exp_both']/m:.4f}" if m else "-")
