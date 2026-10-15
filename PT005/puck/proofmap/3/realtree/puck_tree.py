# Puck independent re-implementation (not a copy of Hesper tree.py) for chair note 95 checks.
# Node w (15 ints) at modulus M: open = improper at M (>=2 odd coords, every t in 1..M/2 covered) and fails L7.
# Children at 2M: w_i or w_i+M. Coverage of even t at 2M is inherited; new t are odd t<=M, grouped in fibres r=min(t%p,p-t%p).
import sys, json, itertools, collections, numpy as np
from math import gcd
def cov(t,x,N):
    r=(t*x)%N; return 16*min(r,N-r)<N
def odd_count(w): return sum(1 for x in w if x&1)
def L7(w,M):
    for D in range(2,M+1,2):
        if M%D: continue
        nz=[x for x in w if x%D]
        if len(nz)<2: continue
        tot=0
        for x in nz:
            g=gcd(D,x); tot+=g*(-(-(D//g)//8))
        if tot<D: return D
    return None
def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c
MASKS=np.arange(1<<15,dtype=np.int64)
def fibre_ok(w,M,p):
    N=2*M; fib=collections.defaultdict(list)
    for t in range(1,M+1,2): fib[min(t%p,p-t%p)].append(t)
    res={}
    for r,ts in fib.items():
        # bitmask over ts, as list of python ints per (i,b); evaluate by splitting masks into low7/high8 halves
        cv=[[sum(1<<j for j,t in enumerate(ts) if cov(t,x+b*M,N)) for b in (0,1)] for x in w]
        full=(1<<len(ts))-1
        lo=[0]*(1<<7)
        for m in range(1<<7):
            a=0
            for i in range(7): a|=cv[i][(m>>i)&1]
            lo[m]=a
        hi=[0]*(1<<8)
        for m in range(1<<8):
            a=0
            for i in range(8): a|=cv[7+i][(m>>i)&1]
            hi[m]=a
        ok=np.zeros(1<<15,dtype=bool)
        for h in range(1<<8):
            hv=hi[h]
            ok[h<<7:(h+1)<<7]=[ (lo[l]|hv)==full for l in range(1<<7)]
        if not ok.all(): res[r]=ok
    return res
def min_dead_set(oks,cap=8):
    rs=sorted(oks,key=lambda r:oks[r].sum())
    for s in range(1,cap+1):
        for c in itertools.combinations(rs,s):
            a=oks[c[0]].copy()
            for r in c[1:]: a&=oks[r]
            if not a.any(): return s,list(c)
    return None,None
def canon(w,M): return tuple(sorted(min(x%M,(-x)%M) for x in w))
def run(label,w,M,p,maxM,frozen_cut=9,Scap=4,detail=None):
    assert odd_count(w)>=2
    lev=[list(w)]; first9={}  # canon -> level index where f>=9 first reached on its branch
    depth_after9=collections.Counter()
    lvl=0
    while lev and M<=maxM:
        nxt={}; stats=collections.Counter(); Sh=collections.Counter(); deadlist=[]
        for u in lev:
            k=v2(M); f=sum(1 for x in u if v2(x)<k)
            oks=fibre_ok(u,M,p); alive=np.ones(1<<15,dtype=bool)
            for o in oks.values(): alive&=o
            kids=[[int(u[i])+((int(m)>>i)&1)*M for i in range(15)] for m in np.nonzero(alive)[0]]
            par_bad=0; nkid=0
            for s in kids:
                if odd_count(s)<2: par_bad+=1; continue
                c=canon(s,2*M)
                if c in nxt: continue
                if L7(s,2*M) is None: nxt[c]=(s,f); nkid+=1
                else: stats['closedL7']+=1
            stats['parity_bad_kids']+=par_bad
            if not kids:
                S,Ss=min_dead_set(oks,Scap); Sh[S]+=1
                deadlist.append({"w":u,"f":f,"S":S,"Sset":Ss})
                stats['died']+=1
                if f>=9: stats['died_f>=9']+=1
        print(json.dumps({"label":label,"level_p":M//p,"open":len(lev),**stats,"S_hist":{str(k):v for k,v in Sh.items()},
                          "kids_open":len(nxt)}),flush=True)
        if detail is not None: detail.extend([dict(d,level_p=M//p) for d in deadlist])
        lev=[v[0] for v in nxt.values()]; M*=2
    print(json.dumps({"label":label,"END":"no open nodes" if not lev else f"{len(lev)} open at {M//p}p"}),flush=True)
if __name__=="__main__":
    which=sys.argv[1]; det=[]
    if which=="p47": run("Astra R p=47",[1,2,3,5,6,8,9,10,11,12,13,14,15,20,21],47,47,128*47,detail=det)
    if which=="p17": run("W5 p=17",[189,224,72,447,176,500,144,128,384,266,80,64,48,32,16],32*17,17,512*17,detail=det)
    if which in("p131a","p131b"):
        r=[1,1,1,2,8,11,18,38,40,46,47,48,56,58,1 if which=="p131a" else 2]
        run("p131 row "+which[-1],r,131,131,32*131,detail=det)
    json.dump(det,open(f"/workspace/pt5_r95/dead_{which}.json","w"))
