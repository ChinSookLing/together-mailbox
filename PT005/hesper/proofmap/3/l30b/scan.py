# PT005 Link 3.0b scan (Hesper): find improper f>=9 nodes at 32p for p in 19..43 by local search,
# then track descendants (all children, numpy) and record first level a fibre has empty lift-cover.
# Improper at 32p implies improper at 16p,8p,... (t at M/2 <-> 2t at M), so every hit is a real tree node.
import sys, random, json
sys.path.insert(0,'.')
from w5test import analyse, improper, canon, v2
def cov(x,M):
    m=0
    for t in range(1,M//2+1):
        r=(t*x)%M
        if 16*min(r,M-r)<M: m|=1<<t
    return m
def search(p,k=5,fmin=9,tries=400,seed=1,fmax=15,want=10):
    M=(1<<k)*p; full=(1<<(M//2+1))-2
    C=[0]+[cov(x,M) for x in range(1,M//2+1)]
    xs=list(range(1,M//2+1))
    rnd=random.Random(seed); found=[]
    for _ in range(tries):
        w=[rnd.choice(xs) for _ in range(15)]
        for sweep in range(30):
            improved=False
            for i in rnd.sample(range(15),15):
                rest=0
                for j in range(15):
                    if j!=i: rest|=C[w[j]]
                best=None
                cand=rnd.sample(xs,len(xs))
                for x in cand:
                    ww=w[:i]+[x]+w[i+1:]
                    f=sum(1 for y in ww if v2(y)<k); odd=sum(y%2 for y in ww)
                    pen=max(0,fmin-f)*50+max(0,f-fmax)*50+max(0,2-odd)*50
                    sc=bin(full&~(rest|C[x])).count('1')+pen
                    if best is None or sc<best[0]: best=(sc,x)
                if best[1]!=w[i]:
                    old=bin(full&~(rest|C[w[i]])).count('1')
                    if best[0]<old+ (max(0,fmin-sum(1 for y in w if v2(y)<k))*50+max(0,2-sum(y%2 for y in w))*50): improved=True
                    w[i]=best[1]
            unc=bin(full&~(sum(0 for _ in [0]) or 0)).count('1')
            tot=0
            for y in w: tot|=C[y]
            f=sum(1 for y in w if v2(y)<k)
            if tot==full and fmin<=f<=fmax and sum(y%2 for y in w)>=2:
                c=canon(w,M)
                if c not in [canon(z,M) for z in found]:
                    found.append(list(w)); print("FOUND",p,"f",f,w,flush=True)
                break
            if not improved: break
        if len(found)>=want: break
    return found
def track(w,M,p,maxk=8,cap=64):
    lev=[w]; out=[]; Mu=M
    while lev and Mu<=(1<<maxk)*p:
        rows=[];nxt=[];seen=set()
        for u in lev[:cap]:
            info,surv=analyse(u,Mu,p); rows.append(info)
            for s in surv:
                c=canon(s,2*Mu)
                if c not in seen: seen.add(c); nxt.append(s)
        fs=sorted({r['f'] for r in rows}); dead=[len(r['child_fibres_dead']) for r in rows]
        out.append({"level":Mu//p,"nodes":len(lev),"examined":len(rows),"f":fs,
                    "nodes_with_dead_fibre":sum(1 for d in dead if d),"dead_fibres_minmax":[min(dead),max(dead)],
                    "free_pairs_opus":sorted({len(r['node_free_pairs_opus_def']) for r in rows}),
                    "children_distinct":len(nxt)})
        print(p,json.dumps(out[-1]),flush=True)
        lev=nxt; Mu*=2
    return out
if __name__=="__main__":
    p=int(sys.argv[1]); fmax=int(sys.argv[2]) if len(sys.argv)>2 else 15; res={"p":p,"fmax":fmax,"nodes":[]}
    for w in search(p,fmax=fmax):
        res["nodes"].append({"w32p":w,"track":track(w,32*p,p)})
    json.dump(res,open(f"scan_p{p}_f{fmax}.json","w"),indent=1)
    print("DONE",p,len(res["nodes"]))
