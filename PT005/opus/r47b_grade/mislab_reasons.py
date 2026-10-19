import sys,gzip,csv,random
sys.path.insert(0,"/home/claude/together-mailbox/PT005/opus/r43chk")
from own import open_children,is_open
import numpy as np
rows=[l.rstrip("\n").split("\t") for l in open("puck/r47B/check/mislabel_list.tsv")][1:]
want={int(r[0]):r for r in rows}
data={}
with gzip.open("hesper/r45/widen/nodes_widen.csv.gz","rt") as f:
    rd=csv.reader(f); next(rd)
    for i,r in enumerate(rd):
        if i in want: data[i]=r
random.seed(1019); pick=random.sample(sorted(want),60)
from collections import Counter
c=Counter()
for i in pick:
    r=data[i]; M=int(r[2]); w=[int(x) for x in r[3].split()]
    oc=open_children(w,M)
    # reason covering children rejected
    N=2*M; wa=np.array(w); reasons=Counter()
    bits=((np.arange(1<<15)[:,None]>>np.arange(15)[None,:])&1)
    C=wa[None,:]+bits*M
    for row in C:
        T=np.arange(1,N//2+1)[:,None]; rr=(T*row[None,:])%N; d=np.minimum(rr,N-rr)
        if not (16*d<N).any(axis=1).all(): continue
        if (row%2).sum()<2: reasons['<2odd']+=1
        elif not is_open(list(row),N): reasons['L7']+=1
        else: reasons['open']+=1
    c[(len(oc),tuple(sorted(reasons)))]+=1
print(c)
