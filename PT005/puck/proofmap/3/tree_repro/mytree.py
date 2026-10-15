# Puck independent lift-tree for the fibre lemma (own code; definitions only). Meet-in-the-middle over 2^15 lift masks.
import sys, json, random, itertools, collections, numpy as np
from math import gcd
def v2(x):
    c=0
    while x and x%2==0: x//=2; c+=1
    return c
def cov_all(t,x,M):            # numpy: t array
    r=(t*x)%M; return 16*np.minimum(r,M-r)<M
def improper(w,M):
    if sum(x&1 for x in w)<2: return False
    t=np.arange(1,M//2+1); a=np.zeros(len(t),bool)
    for x in w: a|=cov_all(t,x,M)
    return bool(a.all())
def l7closed(w,M):             # exists even D|M, >=2 coords not divisible by D, sum gcd*ceil(D/g/8) < D
    for D in range(2,M+1,2):
        if M%D: continue
        nz=[x for x in w if x%D]
        if len(nz)>=2:
            s=0
            for x in nz:
                g=gcd(D,x); q=D//g; s+=g*((q+7)//8)
            if s<D: return True
    return False
def canon(w,M): return tuple(sorted(min(x%M,M-x%M) for x in w))
def pack(ts,N,x):
    m=cov_all(np.array(ts),x,N)
    nw=(len(ts)+63)//64
    out=np.zeros(nw,np.uint64)
    for j in np.nonzero(m)[0]: out[j>>6]|=np.uint64(1)<<np.uint64(j&63)
    return out
LO=np.arange(256); HI=np.arange(128)
def fibre_ok(tab):             # tab[i][b] -> uint64[nw]; returns bool[2^15], index = mask (bit i = lift of coord i)
    nw=len(tab[0][0])
    def half(idx):
        n=len(idx); R=np.zeros((1<<n,nw),np.uint64)
        for m in range(1<<n):
            a=np.zeros(nw,np.uint64)
            for j,i in enumerate(idx): a|=tab[i][(m>>j)&1]
            R[m]=a
        return R
    A=half(range(8)); B=half(range(8,15))
    full=np.zeros(nw,np.uint64)
    return A,B
def analyse(w,M,p,fullmask_cache={}):
    N=2*M; k=v2(M)
    f=sum(1 for x in w if v2(x)<k)
    odd=np.arange(1,N//2+1,2)
    fib=collections.defaultdict(list)
    for t in odd: r=int(t)%p; fib[min(r,p-r)].append(int(t))
    oks={}; alive=np.ones(1<<15,bool)
    for r,ts in sorted(fib.items()):
        nw=(len(ts)+63)//64
        full=np.zeros(nw,np.uint64)
        for j in range(len(ts)): full[j>>6]|=np.uint64(1)<<np.uint64(j&63)
        tab=[[pack(ts,N,w[i]+b*M) for b in (0,1)] for i in range(15)]
        A=np.zeros((256,nw),np.uint64); B=np.zeros((128,nw),np.uint64)
        for m in range(256):
            a=np.zeros(nw,np.uint64)
            for i in range(8): a|=tab[i][(m>>i)&1]
            A[m]=a
        for m in range(128):
            a=np.zeros(nw,np.uint64)
            for i in range(7): a|=tab[8+i][(m>>i)&1]
            B[m]=a
        U=(B[:,None,:]|A[None,:,:])==full   # [hi,lo,nw]
        ok=U.all(axis=2).reshape(-1)       # index hi*256+lo = mask
        if not ok.all(): oks[r]=ok
        alive&=ok
        if not alive.any() and False: break
    nodd=sum(x&1 for x in w)
    surv=np.nonzero(alive)[0] if nodd>=2 else []
    S=None;Sset=None
    if len(surv)==0:
        rs=list(oks); packed={r:np.packbits(oks[r]) for r in rs}
        for size in (1,2,3,4):
            for c in itertools.combinations(rs,size):
                a=packed[c[0]]
                for r in c[1:]: a=a&packed[r]
                if not a.any(): S=size;Sset=c;break
            if S: break
    dead1=sum(1 for r in oks if not oks[r].any())
    return {"f":f,"children":int(len(surv)),"S":S,"dead_single":dead1,"nfib_constrained":len(oks)},[[w[i]+((int(m)>>i)&1)*M for i in range(15)] for m in surv]
def run(label,w,M,p,maxM,cap,seed):
    rnd=random.Random(seed); assert improper(w,M); lev=[w]; res=[]
    while lev and M<=maxM:
        sample=lev if len(lev)<=cap else rnd.sample(lev,cap)
        rows=[]; nxt={}; closed=0
        for u in sample:
            info,surv=analyse(u,M,p); rows.append(info)
            for s in surv:
                c=canon(s,2*M)
                if c in nxt: continue
                if l7closed(s,2*M): closed+=1   # counted per distinct? (approx: counts first-seen only)
                else: nxt[c]=s
        died=[r for r in rows if r['children']==0]
        rec={"label":label,"level_p":M//p,"open":len(lev),"examined":len(rows),
         "f_hist":dict(sorted(collections.Counter(r['f'] for r in rows).items())),
         "died":len(died),"S_hist":{str(k):v for k,v in collections.Counter(r['S'] for r in died).items()},
         "maxS":max([r['S'] or 0 for r in died],default=0),
         "died_f>=9":sum(1 for r in died if r['f']>=9),
         "died_no_dead_single":sum(1 for r in died if r['dead_single']==0),
         "children_closed_L7":closed,"children_open":len(nxt)}
        print(json.dumps(rec),flush=True); res.append(rec)
        lev=list(nxt.values()); M*=2
    print(json.dumps({"label":label,"END":"no open nodes" if not lev else f"stopped {M//p}p {len(lev)} open"}),flush=True)
if __name__=="__main__":
    which=sys.argv[1]; cap=int(sys.argv[2]) if len(sys.argv)>2 else 100; seed=int(sys.argv[3]) if len(sys.argv)>3 else 7
    if which=="p17": run("W5 p=17",[189,224,72,447,176,500,144,128,384,266,80,64,48,32,16],32*17,17,512*17,cap,seed)
    if which=="p37A": run("A p=37",[112,2,336,448,5,80,192,8,416,528,48,160,13,236,16],16*37,37,256*37,cap,seed)
    if which=="p37B": run("B p=37",[112,2,336,448,5,6,192,8,416,528,48,160,13,14,16],16*37,37,256*37,cap,seed)
    if which=="p47": run("Astra p=47",[1,2,3,5,6,8,9,10,11,12,13,14,15,20,21],47,47,128*47,cap,seed)
    if which in("p131a","p131b"): run("p131 "+which[-1],[1,1,1,2,8,11,18,38,40,46,47,48,56,58,1 if which=="p131a" else 2],131,131,32*131,cap,seed)
