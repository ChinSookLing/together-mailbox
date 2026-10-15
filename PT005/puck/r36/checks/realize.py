# Try to realise the 96 abstract mixed DOUBLABLE k5-compatible configurations for real (p,b).
import sys
from collections import defaultdict, Counter
import jointR as J
A=J.A
from lem import hit, bal
targets=[]
for key in A.SEEN:
    Us=[A.FP[k] for k in key]
    cnt=Counter(s for U in Us for s in U)
    if not all(cnt[s]==2 for s in A.odd): continue
    ok,ham,mixed=A.analyse(key)
    if ok and mixed:
        for beta in (0,1):
            if J.k5ok(Us,beta): targets.append((key,beta))
print('targets',len(targets),file=sys.stderr)
def realise(p):
    found=[]
    for b in range(1,(p+1)//2):
        beta=b%2
        av=defaultdict(list)   # (v,m32,sg) -> list of w
        for w in range(1,16*p,2):
            if w%p in (0,1,p-1): continue
            d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32)
            av[(v,m%32,1 if d>0 else -1)].append(w)
        for key,bt in targets:
            if bt!=beta: continue
            Us=[A.FP[k] for k in key]
            opts=[[t for t in J.types(U) if t in av] for U in Us]
            def rec(i,used,pick):
                if i==8: return list(pick)
                for t in opts[i]:
                    f=J.F5(*t,beta)
                    if f&used: continue
                    r=rec(i+1,used|f,pick+[t])
                    if r: return r
                return None
            r=rec(0,frozenset(),[])
            if r:
                W=[av[t][0] for t in r]
                found.append((b,W)); break
        if found: break
    return found
for p in map(int,sys.argv[1:]):
    print(p,realise(p),flush=True)
