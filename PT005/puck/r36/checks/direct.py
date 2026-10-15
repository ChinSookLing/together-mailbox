import sys
from collections import defaultdict, Counter
from lem import hit
def test(p,b,W):
    n5,n6=32*p,64*p
    c5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
    c6=[t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
    cov5=Counter(t for w in W for t in c5 if hit(t,w,n5))
    k5=len(c5)==16 and all(cov5[t]==1 for t in c5)
    hitby=defaultdict(list)
    for i,w in enumerate(W):
        for e in (0,1):
            for t in c6:
                if hit(t,w+e*n5,n6): hitby[t].append((i,e))
    k6=len(c6)==32 and all(len(hitby[t])==2 and hitby[t][0][0]!=hitby[t][1][0] for t in c6)
    if not (k5 and k6): return dict(k5=k5,k6=k6)
    adj=defaultdict(list)
    for t,((i,ei),(j,ej)) in hitby.items():
        l=1^ei^ej; adj[i].append((j,l)); adj[j].append((i,l))
    g={};ok=True
    for r in range(8):
        if r in g: continue
        g[r]=0; st=[r]
        while st:
            x=st.pop()
            for y,l in adj[x]:
                if y not in g: g[y]=g[x]^l; st.append(y)
                elif g[y]!=g[x]^l: ok=False
    m8={w%8 for w in W}; mixed=not any(m8<={c,8-c} for c in (1,3))
    return dict(k5=k5,k6=k6,mixed=mixed,doublable=ok,lifts=[g[i] for i in range(8)], m8=sorted(m8))
for args in [(19,1,[175,165,241,219,79,27,271,45]),(23,8,[113,225,99,239,193,271,237,159]),(29,1,[397,47,443,335,123,81,197,207])]:
    print(args[0],args[1],test(*args))
