# PT005 pre-R43 real lift trees (Hesper, 2026-10-16). Same node rule as tree2.py (parity filter on children:
# a child is kept only with >=2 odd coords). FULL trees: no sampling, no node cap (cap only on modulus maxM).
# Per node also: first level where its branch reached f>=9 (min over merged parents), to get depth after f>=9.
# Death classes: S=k exact least jointly dead fibre set (search up to SMAX); "parity" = some mask survives all fibres
# but every such child has <2 odd coords; ">SMAX" = not resolved within SMAX.
import sys, json, random, itertools, collections, numpy as np
from math import gcd, ceil
from multiprocessing import Pool
SMAX=int(__import__('os').environ.get('SMAX','6'))
def v2(x):
    c=0
    while x and x%2==0: x//=2; c+=1
    return c
def covered(t,x,N): r=(t*x)%N; return 16*min(r,N-r)<N
def improper(w,M):
    return sum(x%2 for x in w)>=2 and all(any(covered(t,x,M) for x in w) for t in range(1,M//2+1))
def Lb(D,w): return sum(gcd(D,x)*ceil((D//gcd(D,x))/8) for x in w if x%D)
def l7(w,M):
    for D in range(2,M+1,2):
        if M%D==0 and len([x for x in w if x%D])>=2 and Lb(D,w)<D: return D
    return None
def canon(w,M): return tuple(sorted(min(x%M,(-x)%M) for x in w))
BITS=np.arange(1<<15,dtype=np.int64)
def analyse(w,M,p):
    k=v2(M); N=2*M
    f=sum(1 for x in w if v2(x)<k)
    pairs={}
    for t in range(1,N//2+1,2):
        r=t%p; pairs.setdefault(min(r,p-r),[]).append(t)
    oks={}; alive=np.ones(1<<15,dtype=bool)
    for r,ts in sorted(pairs.items()):
        nw=(len(ts)+63)//64
        acc=np.zeros((1<<15,nw),dtype=np.uint64); full=np.zeros(nw,dtype=np.uint64)
        for j in range(len(ts)): full[j//64]|=np.uint64(1)<<np.uint64(j%64)
        for i,x in enumerate(w):
            tab=np.zeros((2,nw),dtype=np.uint64)
            for b in (0,1):
                y=x+b*M
                for j,t in enumerate(ts):
                    if covered(t,y,N): tab[b,j//64]|=np.uint64(1)<<np.uint64(j%64)
            acc|=tab[(BITS>>i)&1]
        ok=np.all(acc==full,axis=1)
        if not ok.all(): oks[r]=ok
        alive&=ok
    raw=[[w[i]+((m>>i)&1)*M for i in range(15)] for m in np.nonzero(alive)[0]]
    surv=[s for s in raw if sum(x%2 for x in s)>=2]
    S=None
    if not surv:
        if raw: S="parity"
        else:
            rs=list(oks); S=f">{SMAX}"
            for size in range(1,SMAX+1):
                hit=False
                for c in itertools.combinations(rs,size):
                    a=oks[c[0]].copy()
                    for r in c[1:]: a&=oks[r]
                    if not a.any(): hit=True; break
                if hit: S=size; break
    return f,S,surv
def run(label,w,p,maxM):
    M=p; lev={canon(w,M):(w,None)}; L=0; maxdepth=-1; tot=0; rows=[]
    assert improper(w,M), "start not improper"
    while lev and M<=maxM:
        items=list(lev.values())
        with Pool(2) as pool: res=pool.starmap(analyse,[(u,M,p) for u,_ in items])
        nxt={}; closed=0; fh=collections.Counter(); Sh=collections.Counter(); died=0; died9=0
        for (u,first9),(f,S,surv) in zip(items,res):
            tot+=1; fh[f]+=1
            if first9 is None and f>=9: first9=L
            if first9 is not None: maxdepth=max(maxdepth,L-first9)
            if not surv: died+=1; Sh[str(S)]+=1; died9+= f>=9
            for s in surv:
                c=canon(s,2*M)
                if l7(s,2*M) is not None: closed+=1; continue
                if c in nxt:
                    o=nxt[c][1]
                    if first9 is not None and (o is None or first9<o): nxt[c]=(nxt[c][0],first9)
                else: nxt[c]=(s,first9)
        rec={"label":label,"level_p":M//p,"open":len(items),"f_hist":dict(sorted(fh.items())),"died":died,
             "died_f>=9":died9,"S_hist":dict(Sh),"children_L7_closed":closed,"children_open":len(nxt)}
        print(json.dumps(rec),flush=True); rows.append(rec)
        lev=nxt; M*=2; L+=1
    end={"label":label,"END":"no open nodes" if not lev else f"stopped at {M//p}p with {len(lev)} open",
         "nodes":tot,"max_depth_after_first_f>=9":maxdepth}
    print(json.dumps(end),flush=True); return rows,end
def pick(p,seed,n):
    rnd=random.Random(seed); out=[]; tries=0
    while len(out)<n:
        tries+=1
        w=sorted(rnd.randrange(1,(p+1)//2) for _ in range(15))
        if improper(w,p) and canon(w,p) not in [canon(x,p) for x in out]: out.append(w)
    return out,tries
if __name__=="__main__":
    a=sys.argv[1]
    if a=="p47": run("Astra R p=47",[1,2,3,5,6,8,9,10,11,12,13,14,15,20,21],47,128*47)
    elif a=="p17": 
        # W5 p=17 starts at 32p
        pass
    elif a=="pick":
        p=int(sys.argv[2]); seed=int(sys.argv[3]); n=int(sys.argv[4])
        rows,tries=pick(p,seed,n); print(json.dumps({"p":p,"seed":seed,"tries":tries,"rows":rows}))
    elif a=="row":
        p=int(sys.argv[2]); w=json.loads(sys.argv[3]); run(sys.argv[4],w,p,int(sys.argv[5])*p)
