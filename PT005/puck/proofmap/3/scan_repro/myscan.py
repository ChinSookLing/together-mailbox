# Puck independent scan: improper 15-vectors at M=32p, f>=9 (f=#coords with v2<5), >=2 odd; then exact child test at 64p.
import sys, random, json, numpy as np
def v2(x):
    c=0
    while x and x%2==0: x//=2; c+=1
    return c
def covmat(M):
    H=M//2; t=np.arange(1,H+1); X=np.arange(0,H+1)
    r=(np.outer(X,t))%M; d=np.minimum(r,M-r)
    return (16*d<M)   # [x, t-1]
def search(p,fmin,fmax,want,seed,tries=3000):
    M=32*p; H=M//2; C=covmat(M); rnd=np.random.default_rng(seed)
    V=np.array([min(v2(x),9) if x else 99 for x in range(H+1)]); fr=(V<5).astype(int); od=(np.arange(H+1)%2)
    found=[];seen=set()
    for _ in range(tries):
        w=list(rnd.integers(1,H+1,15))
        for it in range(400):
            i=int(rnd.integers(15))
            rest=np.zeros(H,bool)
            for j in range(15):
                if j!=i: rest|=C[w[j],:]
            unc=(~rest)
            score=(C[:,:].astype(np.int32)@unc.astype(np.int32))  # covered among uncovered
            f0=sum(fr[w[j]] for j in range(15) if j!=i); o0=sum(od[w[j]] for j in range(15) if j!=i)
            f=f0+fr; o=o0+od
            pen=np.maximum(0,fmin-f)*40+np.maximum(0,f-fmax)*40+np.maximum(0,2-o)*40
            obj=-score+pen+rnd.random(H+1)*0.5
            obj[0]=1e9
            w[i]=int(np.argmin(obj))
            tot=np.zeros(H,bool)
            for x in w: tot|=C[x,:]
            f=sum(fr[x] for x in w)
            if tot.all() and fmin<=f<=fmax and sum(od[x] for x in w)>=2:
                c=tuple(sorted(w))
                if c not in seen: seen.add(c); found.append(list(map(int,w)))
                break
        if len(found)>=want: break
    return found
def child_test(w,p):
    M=32*p; N=2*M; Hn=N//2
    tt=np.arange(1,Hn+1,2)             # odd t at 2M
    nt=len(tt)
    def cov(y): r=(tt*y)%N; return 16*np.minimum(r,N-r)<N
    tab=[[cov(w[i]+b*M) for b in (0,1)] for i in range(15)]
    # sanity: even t at 2M are covered by inheritance? check
    te=np.arange(2,Hn+1,2)
    # per-fibre existence: choose bits for 15 coords, via numpy over 2^15
    bits=np.arange(1<<15)
    def exist(mask):
        idx=np.nonzero(mask)[0]
        if len(idx)==0: return 1<<15
        ok=np.ones(1<<15,bool)
        # accumulate coverage count per t
        acc=np.zeros((1<<15,len(idx)),bool)
        for i in range(15):
            T0=tab[i][0][idx]; T1=tab[i][1][idx]
            acc|=np.where(((bits>>i)&1)[:,None]==1,T1[None,:],T0[None,:])
        return acc.all(axis=1)
    fib={}
    for j,t in enumerate(tt):
        r=int(t%p); r=min(r,p-r); fib.setdefault(r,[]).append(j)
    fibok={}
    alive=np.ones(1<<15,bool)
    for r,js in fib.items():
        m=np.zeros(nt,bool); m[js]=True
        ok=exist(m); 
        if isinstance(ok,int): continue
        fibok[r]=int(ok.sum()); alive&=ok
    # even t check: covered at 2M by every lift?
    ev_ok=True
    for t in te:
        for b in (0,1):pass
    dead=[r for r,c in fibok.items() if c==0]
    return int(alive.sum()), len(dead), sorted(dead)
if __name__=="__main__":
    p=int(sys.argv[1]); fmin=int(sys.argv[2]); fmax=int(sys.argv[3]); want=int(sys.argv[4]); seed=int(sys.argv[5])
    out=[]
    for w in search(p,fmin,fmax,want,seed):
        f=sum(1 for x in w if v2(x)<5)
        ch,nd,dead=child_test(w,p)
        out.append({"p":p,"w":w,"f":f,"children":ch,"ndead":nd,"dead":dead}); print(json.dumps(out[-1]),flush=True)
    json.dump(out,open(f"my_p{p}_{fmin}_{fmax}_s{seed}.json","w"))
