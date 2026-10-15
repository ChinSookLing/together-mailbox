# Puck: consequence of Claim R. Labels depend only on (c,v) of each footprint (w mod 64 lift and v->-v are vertex gauges),
# so enumerate ALL abstract mod-32 exact 2-covers by 8 footprints and test parity solvability (doublable) vs obstructed (odd cycle).
from collections import defaultdict, Counter
fps={}
for c in range(0,32,2):
    for v in range(1,32,2):
        U=frozenset((c+x*v)%32 for x in (-3,-1,1,3))
        fps.setdefault(U,[]).append((c,v))
FP=list(fps); odd=list(range(1,32,2))
def b32(x): return ((x+16)%32)-16
def z(rep,s,lift=0,sign=1):
    c,v=rep; w=(pow(v,-1,32)+32*lift)%64; 
    if sign<0: w=(-w)%64
    m16=((-c*w)//2)%16
    q=2*m16+s*w; r=b32(q); assert abs(r)<=3,(rep,s,q); return ((q-r)//32)%2
def cls(U): return fps[U][0][1]%8 in (1,7)
SEEN=set(); res=Counter(); ex=[]
def analyse(acc,variant=(0,1)):
    Us=[FP[k] for k in acc]
    adj=defaultdict(list); pairs=defaultdict(int)
    for s in odd:
        i,j=[n for n,U in enumerate(Us) if s in U]
        lam=1^z(fps[Us[i]][0],s,*variant)^z(fps[Us[j]][0],s,*variant)
        adj[i].append((j,lam)); adj[j].append((i,lam)); pairs[(i,j)]+=1
    g={};ok=True
    for root in range(8):
        if root in g: continue
        g[root]=0; st=[root]
        while st:
            x=st.pop()
            for y,l in adj[x]:
                if y not in g: g[y]=g[x]^l; st.append(y)
                elif g[y]!=g[x]^l: ok=False
    deg=[len({j for j,_ in adj[i]}) for i in range(8)]
    ham=len(pairs)==8 and all(d==2 for d in deg)
    mixed=len({cls(U) for U in Us})==2
    return ok,ham,mixed
def rec(acc,cnt):
    if len(acc)==8:
        key=tuple(sorted(acc))
        if key in SEEN: return
        SEEN.add(key)
        if not all(cnt[s]==2 for s in odd): return
        ok,ham,mixed=analyse(key)
        # gauge sanity: other lift / sign choice gives the same verdict
        assert analyse(key,(1,1))[0]==ok and analyse(key,(0,-1))[0]==ok
        res[('mixed' if mixed else 'single','ham8' if ham else 'nonham','DOUBLABLE' if ok else 'obstructed')]+=1
        if ok and mixed and len(ex)<5: ex.append([sorted(FP[k]) for k in key])
        return
    need=[s for s in odd if cnt[s]<2]; s0=need[0]
    for k,U in enumerate(FP):
        if s0 not in U or any(cnt[s]>=2 for s in U): continue
        for s in U: cnt[s]+=1
        acc.append(k); rec(acc,cnt); acc.pop()
        for s in U: cnt[s]-=1
rec([],Counter())
for k,v in sorted(res.items()): print(k,v)
print('mixed doublable examples',ex)
