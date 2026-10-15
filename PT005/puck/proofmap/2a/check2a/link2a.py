# Puck: empirical test of Link 2a (6->7 doublability of doubled k=5 mixed tilings; p-independence of reduced data).
# Own code. Level 5: M5=32p, C5(b); level 6: M6=64p, C6(2b), W=w+32p*e5; level 7: M7=128p, C7(4b) = odd t in 1..64p, t=+-4b mod p
# (64 members), lift W' = W + 64p*x. Hit test raw: 16*min(tW mod M, M - tW mod M) < M.
import os, sys, json, time, random, itertools
from collections import defaultdict, Counter
import numpy as np
from multiprocessing import Pool
def bal(x,p):
    x%=p; return x if x<=p//2 else x-p
def cls(w): return 1 if w%8 in (1,7) else 3
def hitv(t,W,M):
    r=(t*W)%M; return 16*np.minimum(r,M-r)<M
def red7(p,b,W):
    """reduced level-6->7 data of coordinate W (mod 64p): (c mod 64, v canonical in 1..31, sgn d7 [canonicalised with v])"""
    d=bal(4*b*W,p); M=(4*b*W-d)//p; v=pow(W,-1,64); c=(-M*v)%64; sg=1 if d>0 else -1
    if v>32: v=64-v; sg=-sg
    return (c,v,sg), M, d
def work(args):
    p,b,deadline_s,maxsol,reps_per_sol,seed=args
    rnd=random.Random(seed*1000003+p*7919+b)
    n5,n6,n7=32*p,64*p,128*p
    c5=np.array([t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)])
    c6=np.array([t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)])
    c7=np.array([t for t in range(1,64*p+1,2) if t%p in ((4*b)%p,(-4*b)%p)])
    assert len(c5)==16 and len(c6)==32 and len(c7)==64
    ws=[w for w in range(1,16*p,2) if w%p not in (0,1,p-1)]
    wa=np.array(ws)
    # level-5 and level-6 masks
    M5=hitv(c5[None,:],wa[:,None],n5)             # (n,16)
    pw=(1<<np.arange(16,dtype=np.int64)); pw6=(1<<np.arange(32,dtype=np.int64))
    m5=(M5*pw[None,:]).sum(1)
    items=defaultdict(list)
    for e in (0,1):
        W=wa+e*n5
        M6=hitv(c6[None,:],W[:,None],n6)
        m6=(M6*pw6[None,:]).sum(1)
        for k,w in enumerate(ws):
            items[int(m5[k])|(int(m6[k])<<16)].append((w,e))
    col=defaultdict(list)
    for mk in items:
        x=mk
        while x:
            i=(x&-x).bit_length()-1; x&=x-1; col[i].append(mk)
    for i in col: rnd.shuffle(col[i])
    FULL=(1<<48)-1; sols=[]; t0=time.time(); timed_out=[False]
    def rec(cov,sel):
        if len(sols)>=maxsol or timed_out[0]: return
        if time.time()-t0>deadline_s: timed_out[0]=True; return
        if cov==FULL: sols.append(tuple(sel)); return
        free=FULL&~cov; best=None; x=free
        while x:
            i=(x&-x).bit_length()-1; x&=x-1
            L=[mk for mk in col[i] if not mk&cov]
            if best is None or len(L)<len(best):
                best=L
                if not L: return
        for mk in best:
            sel.append(mk); rec(cov|mk,sel); sel.pop()
    rec(0,[])
    # level-7 masks cache
    cache={}
    def l7(W):
        W%=n6
        if W not in cache:
            r=hitv(c7,W,n7); r2=hitv(c7,W+n6,n7)
            a=sum(1<<int(i) for i in np.nonzero(r)[0])
            a2=sum(1<<int(i) for i in np.nonzero(r2)[0])
            cache[W]=(a,a2,red7(p,b,W))
        return cache[W]
    out=[]; n_sol=len(sols); n_mixed=0
    for s in sols:
        combos=list(itertools.product(*[items[mk] for mk in s]))
        if len(combos)>reps_per_sol: combos=rnd.sample(combos,reps_per_sol)
        for combo in combos:
            wsel=[x[0] for x in combo]
            if os.environ.get("ALLCLASS")!="1" and len({cls(w) for w in wsel})!=2: continue
            n_mixed+=1
            Ws=[w+e*n5 for w,e in combo]
            L=[l7(W) for W in Ws]
            # XOR graph: member -> list of (i,e)
            hb=defaultdict(list)
            for i,(a,a2,_) in enumerate(L):
                for e,mm in ((0,a),(1,a2)):
                    x=mm
                    while x:
                        j=(x&-x).bit_length()-1; x&=x-1; hb[j].append((i,e))
            okstruct=all(len(hb[j])==2 for j in range(64)) and len(hb)==64
            hd=tuple(sorted(Counter(len(hb[j]) if j in hb else 0 for j in range(64)).items()))
            two=sum(1 for j in range(64) if j in hb and len(hb[j])==2)
            # XOR criterion
            adj=defaultdict(list)
            for j,h in hb.items():
                if len(h)!=2: continue
                (i,ei),(k,ek)=h; lam=1^ei^ek
                adj[i].append((k,lam)); adj[k].append((i,lam))
            g={}; dbl=okstruct
            for r0 in range(8):
                if r0 in g: continue
                g[r0]=0; st=[r0]
                while st:
                    u=st.pop()
                    for y,l in adj[u]:
                        if y not in g: g[y]=g[u]^l; st.append(y)
                        elif g[y]!=g[u]^l: dbl=False
            # brute force exact cover over 256 lift choices (verifies criterion)
            full=(1<<64)-1; bf=False
            for x in range(256):
                cov=0; ok=True
                for i in range(8):
                    mm=L[i][1] if (x>>i)&1 else L[i][0]
                    if cov&mm: ok=False;break
                    cov|=mm
                if ok and cov==full: bf=True;break
            keyf=tuple(sorted(l[2][0] for l in L))
            conf5=None
            out.append((p,b,keyf,dbl,bf,okstruct,tuple(sorted(wsel)),hd,two,len({cls(w) for w in wsel})==2,tuple(sorted(Ws))))
    return dict(p=p,b=b,nsol=n_sol,timed_out=timed_out[0],nmixed=n_mixed,rows=out)
if __name__=="__main__":
    p=int(sys.argv[1]); blist=json.loads(sys.argv[2]); dl=float(sys.argv[3]); maxsol=int(sys.argv[4]); reps=int(sys.argv[5])
    t=time.time()
    with Pool(8) as pool:
        res=pool.map(work,[(p,b,dl,maxsol,reps,1) for b in blist],chunksize=1)
    rows=[r for x in res for r in x['rows']]
    summ=dict(p=p,nb=len(blist),sols=sum(x['nsol'] for x in res),timed_out_b=sum(x['timed_out'] for x in res),
      level6_tilings_tested=len(rows),doublable_crit=sum(r[3] for r in rows),doublable_brute=sum(r[4] for r in rows),
      crit_vs_brute_mismatch=sum(r[3]!=r[4] for r in rows),struct_bad=sum(not r[5] for r in rows),struct_ok=sum(r[5] for r in rows),max_members_hit_twice=max([r[8] for r in rows] or [0]),sec=round(time.time()-t,1))
    print(json.dumps(summ),flush=True)
    json.dump([[r[0],r[1],r[2],r[3],r[4],r[9],r[10],r[5]] for r in rows],open(f'rows_p{p}.json','w'))
