# Faster corrected joint p-free search (Puck). Effective type = (c, v mod 32 up to the gauge v->-v handled by listing all,
# level-6 footprint U(c,v), level-5 F5). Search 8 types: F5 tiles the 16 level-5 positions (parity 1-b) exactly once,
# level-6 footprints 2-cover the 16 odd positions exactly; then test cycle parity with true (v, m16).
import sys
from collections import defaultdict, Counter
def b32(x): return ((x+16)%32)-16
def zf(v,m,s):
    w=pow(v,-1,32); q=2*m+s*w; r=b32(q); assert abs(r)<=3; return ((q-r)//32)%2
odd=list(range(1,32,2))
res=Counter(); ex=[]
for beta in (0,1):        # beta = b mod 2
    pos5=[s for s in range(32) if s%2==(1-beta)%2]
    T={}
    for v in range(1,32,2):
        for m in range(32):
            for sg in (1,-1):
                R=(1,-1) if (m-beta)%2==0 else (0,-2*sg)
                F=frozenset((v*(r-m))%32 for r in R)
                c=(-2*m*v)%32; U=frozenset((c+x*v)%32 for x in (-3,-1,1,3))
                zp=tuple(zf(v,m%16,s) for s in sorted(U))
                key=(F,U,zp,v%8 in (1,7))
                T.setdefault(key,(v,m,sg))
    types=list(T)
    by5=defaultdict(list)
    for k in types:
        for s in k[0]: by5[s].append(k)
    seen=set()
    def finish(sel):
        key=tuple(sorted(map(repr,sel)))
        if key in seen: return
        seen.add(key)
        Us=[k[1] for k in sel]
        zmap=[dict(zip(sorted(k[1]),k[2])) for k in sel]
        adj=defaultdict(list); pairs=Counter()
        for s in odd:
            i,j=[n for n,U in enumerate(Us) if s in U]
            l=1^zmap[i][s]^zmap[j][s]; adj[i].append((j,l)); adj[j].append((i,l)); pairs[(i,j)]+=1
        g={};ok=True
        for r in range(8):
            if r in g: continue
            g[r]=0; st=[r]
            while st:
                x=st.pop()
                for y,l in adj[x]:
                    if y not in g: g[y]=g[x]^l; st.append(y)
                    elif g[y]!=g[x]^l: ok=False
        mixed=len({k[3] for k in sel})==2
        deg=[len({j for j,_ in adj[i]}) for i in range(8)]
        ham=len(pairs)==8 and all(d==2 for d in deg)
        res[(beta,'mixed' if mixed else 'single','ham8' if ham else 'nonham','DOUBLABLE' if ok else 'obstructed')]+=1
        if ok and mixed and len(ex)<5: ex.append((beta,[T[k] for k in sel]))
    def rec(used5,cnt6,sel):
        if len(sel)==8:
            if all(cnt6[s]==2 for s in odd): finish(sel)
            return
        s0=min(s for s in pos5 if s not in used5)
        for k in by5[s0]:
            F,U=k[0],k[1]
            if F&used5 or any(cnt6[s]>=2 for s in U): continue
            for s in U: cnt6[s]+=1
            sel.append(k); rec(used5|F,cnt6,sel); sel.pop()
            for s in U: cnt6[s]-=1
    rec(frozenset(),Counter(),[])
    print('beta',beta,'types',len(types),'configs',len(seen),flush=True)
for k,v in sorted(res.items()): print(k,v)
print('mixed DOUBLABLE examples (beta, [(v,m32,sgn d)...])'); [print(e) for e in ex]
