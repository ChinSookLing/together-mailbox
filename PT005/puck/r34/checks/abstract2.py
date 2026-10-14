# Abstract mod-32 model: footprints U(c,v)=c+{+-v,+-3v}, c even, v odd.
# Search 8 footprints exactly 2-covering the 16 odd residues, XOR graph a Ham 8-cycle, mixed classes.
from collections import defaultdict, Counter
from itertools import combinations
fps={}
for c in range(0,32,2):
    for v in range(1,32,2):
        U=frozenset((c+x*v)%32 for x in (-3,-1,1,3))
        fps.setdefault(U,set()).add((c,v%8 in (1,7)))
FP=list(fps)
print("distinct footprints",len(FP), Counter(len(x) for x in fps.values()))
odd=list(range(1,32,2))
res=Counter(); ex=[]
def rec(start,acc,cnt):
    if len(acc)==8:
        if all(cnt[s]==2 for s in odd): analyse(acc)
        return
    # pick the smallest position with cnt<2 -> must be covered by a later footprint
    need=[s for s in odd if cnt[s]<2]
    s0=need[0]
    for k in range(len(FP)):
        if acc and k<acc[-1] and False: pass
        U=FP[k]
        if s0 not in U: continue
        if any(cnt[s]>=2 for s in U): continue
        for s in U: cnt[s]+=1
        acc.append(k); rec(0,acc,cnt); acc.pop()
        for s in U: cnt[s]-=1
SEEN=set()
def analyse(acc):
    key=tuple(sorted(acc))
    if key in SEEN: return
    SEEN.add(key)
    Us=[FP[k] for k in acc]
    pairs=defaultdict(set)
    for s in odd:
        i,j=[n for n,U in enumerate(Us) if s in U]
        pairs[(i,j)].add(s)
    adj=defaultdict(set)
    for (i,j) in pairs: adj[i].add(j); adj[j].add(i)
    ham=len(pairs)==8 and all(len(adj[i])==2 for i in range(8))
    if ham:
        x,prev,seen=0,None,{0}
        for _ in range(7):
            y=[z for z in adj[x] if z!=prev][0]; prev,x=x,y; seen.add(x)
        ham=len(seen)==8
    if not ham: res['nonham']+=1; return
    # classes: footprint may arise from several (c,class); record possibilities
    cl=[{k for (_,k) in fps[U]} for U in Us]
    res[('ham', tuple(sorted(len(x) for x in cl)))]+=1
    # does there exist a class assignment that is mixed and non-alternating?
    import itertools
    for choice in itertools.product(*[sorted(x) for x in cl]):
        if len(set(choice))<2: continue
        alt=all(choice[i]!=choice[j] for (i,j) in pairs)
        res[('ham_mixed','alt' if alt else 'NONALT')]+=1
        if not alt and len(ex)<3: ex.append((acc,choice))
rec(0,[],Counter())
print(dict(res)); print(ex)
