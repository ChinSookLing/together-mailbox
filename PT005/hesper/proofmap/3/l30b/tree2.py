# PT005 fibre lemma on REAL lift-tree nodes (Hesper). Open node = improper at its modulus M and fails L7 (l7 None);
# children x->x or x+M at 2M; improper children that pass L7 are closed; open ones continue.
# Per open node: f (frozen v2<k), node free pairs, and if it has 0 improper children: |S| = least number of
# fibres (odd t at 2M, by +-t mod p) whose lift-covers jointly fail for every one of the 2^15 masks.
import sys, json, random, itertools, numpy as np
from math import gcd, ceil
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
DO_S=False
BITS=np.arange(1<<15,dtype=np.int64)
def analyse(w,M,p):
    k=v2(M); N=2*M
    frozen=[i for i,x in enumerate(w) if v2(x)<k]; nonfz=[i for i in range(15) if i not in frozen]
    nodefree=sorted({min(t%p,p-t%p) for t in range(1,M//2+1,2) if not any(covered(t,w[i],M) for i in nonfz)})
    pairs={}
    for t in range(1,N//2+1,2):
        r=t%p; pairs.setdefault(min(r,p-r),[]).append(t)
    oks={}
    alive=np.ones(1<<15,dtype=bool)
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
    surv=[[w[i]+((m>>i)&1)*M for i in range(15)] for m in np.nonzero(alive)[0]]
    surv=[s for s in surv if sum(x%2 for x in s)>=2]  # parity re-check on children (Puck 22:40)
    S=None; Sset=None
    if not surv and DO_S:
        rs=list(oks)
        for size in (1,2,3,4):
            for c in itertools.combinations(rs,size):
                a=np.ones(1<<15,dtype=bool)
                for r in c: a&=oks[r]
                if not a.any(): S=size; Sset=list(c); break
            if S: break
    return {"f":len(frozen),"free":len(nodefree),"dead_single":sum(1 for r in oks if not oks[r].any()),
            "children":len(surv),"S":S,"Sset":Sset}, surv
def run(label,w,M,p,maxM,cap,seed=0):
    rnd=random.Random(seed); lev=[w]; out=[]
    assert improper(w,M), "start not improper"
    while lev and M<=maxM:
        sample=lev if len(lev)<=cap else rnd.sample(lev,cap)
        rows=[];nxt={};closed=0
        from multiprocessing import Pool
        with Pool(2) as pool: res=pool.starmap(analyse,[(u,M,p) for u in sample])
        for info,surv in res:
            rows.append(info)
            for s in surv:
                c=canon(s,2*M)
                if c in nxt: continue
                if l7(s,2*M) is None: nxt[c]=s
                else: closed+=1
        died=[r for r in rows if r['children']==0]
        rec={"label":label,"level_p":M//p,"open_nodes":len(lev),"examined":len(rows),
             "f_hist":dict(sorted(__import__('collections').Counter(r['f'] for r in rows).items())),
             "died_here":len(died),"S_hist":dict(__import__('collections').Counter(r['S'] for r in died)),
             "maxS":max([r['S'] or 0 for r in died],default=0),
             "f>=9_died":sum(1 for r in died if r['f']>=9),
             "children_closed_by_L7":closed,"children_open":len(nxt)}
        print(json.dumps(rec),flush=True); out.append(rec)
        lev=list(nxt.values()); M*=2
    print(json.dumps({"label":label,"END":"no open nodes" if not lev else f"stopped at level {M//p}p with {len(lev)} open"}),flush=True)
    return out
if __name__=="__main__":
    which=sys.argv[1]
    if which=="p17":  run("W5 p=17",[189,224,72,447,176,500,144,128,384,266,80,64,48,32,16],32*17,17,512*17,200)
    if which=="p37A": run("A p=37",[112,2,336,448,5,80,192,8,416,528,48,160,13,236,16],16*37,37,256*37,100)
    if which=="p37B": run("B p=37",[112,2,336,448,5,6,192,8,416,528,48,160,13,14,16],16*37,37,256*37,100)
    if which=="p47":  run("Astra R p=47",[1,2,3,5,6,8,9,10,11,12,13,14,15,20,21],47,47,128*47,10**9)
    if which in("p131a","p131b"):
        r=[1,1,1,2,8,11,18,38,40,46,47,48,56,58,1 if which=="p131a" else 2]
        run("p131 row "+which[-1],r,131,131,32*131,60)
