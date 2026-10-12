# Chair exploration: 14-sets with >= 2 speeds > 30. Float measure for search; exact recheck of the best.
import random, sys
from fractions import Fraction as Fr
def meas(K):
    I=[(0.0,1.0)]
    for k in sorted(K):
        out=[]
        for a,b in I:
            j0=int(a*k)
            for j in range(j0, int(b*k)+1):
                lo=max(a,(j+1/16)/k); hi=min(b,(j+15/16)/k)
                if lo<hi: out.append((lo,hi))
        I=out
        if not I: return 0.0
    return sum(b-a for a,b in I)
def measx(K):
    I=[(Fr(0),Fr(1))]
    for k in sorted(K):
        out=[]
        for a,b in I:
            for j in range(int(a*k), int(b*k)+1):
                lo=max(a,Fr(16*j+1,16*k)); hi=min(b,Fr(16*j+15,16*k))
                if lo<hi: out.append((lo,hi))
        I=out
    return sum(b-a for a,b in I)
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
VMAX=int(sys.argv[2]) if len(sys.argv)>2 else 120
best={}
def ok(K): return len(K)==14 and sum(1 for k in K if k>30)>=2
for trial in range(300):
    # start: random 12-subset of 1..30 plus 2 large, or perturbation of K*
    if trial%2==0:
        K=set(random.sample(range(1,31),12))|set(random.sample(range(31,VMAX+1),2))
    else:
        K=set(range(1,16))-{6}; K-=set(random.sample(sorted(K),2)); K|=set(random.sample(range(31,VMAX+1),2))
    if not ok(K): continue
    m=meas(K); improved=True
    while improved:
        improved=False
        for out in list(K):
            for _ in range(25):
                new=random.randint(1,VMAX)
                if new in K: continue
                K2=(K-{out})|{new}
                if not ok(K2): continue
                m2=meas(K2)
                if m2<m-1e-12: K,m,improved=K2,m2,True; break
            if improved: break
    key=tuple(sorted(K))
    best[key]=m
top=sorted(best.items(), key=lambda t:t[1])[:8]
for K,m in top:
    print(round(m,6), K, "exact", measx(K))
