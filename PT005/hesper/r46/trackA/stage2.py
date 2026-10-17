# PT005 R46 Track A stage 2 (Hesper): DIRECT coverage of all 2^15 lift children of a node (bitset over odd T<=M at N=2M;
# even T inherit from the open parent), compared with the stage-1 share-sum prediction; for covered children the
# parity (>=2 odd) and L7 rules (as hesper_r45.py) decide open vs dead.
import sys, os, pickle, numpy as np, time
from multiprocessing import Pool
OUT='/tmp/r46w/s2'+os.environ.get('R46SUF','')
BITS=((np.arange(1<<15)[:,None]>>np.arange(15)[None,:])&1).astype(np.int64)
def node_direct(w,M,Dz,good):
    N=2*M; Ts=np.arange(1,M+1,2,dtype=np.int64); nb=len(Ts); W64=(nb+63)//64
    def mask(y):
        r=(Ts*y)%N; d=np.minimum(r,N-r); b=np.ones(W64*64,bool); b[:nb]=16*d<N
        return np.packbits(b,bitorder='little').view(np.uint64)
    cov=np.zeros((1,W64),np.uint64)
    for x in w:
        cov=np.concatenate([cov|mask(x),cov|mask(x+M)],axis=0)
    covered=(cov==np.uint64(0xFFFFFFFFFFFFFFFF)).all(axis=1)
    del cov
    gp=np.zeros(1<<len(Dz),bool); gp[good]=True
    pidx=np.zeros(1<<15,np.int64)
    for b,j in enumerate(Dz): pidx|=BITS[:,j]<<b
    G=gp[pidx]
    r={'viol':int((covered&~G).sum()),'ovcov':int((G&~covered).sum()),'cand':int(G.sum())}
    idx=np.nonzero(covered&G)[0]
    wa=np.array(w,np.int64); C=wa[None,:]+BITS[idx]*M
    par=(C%2).sum(1)>=2
    alive=par.copy()
    for D in range(2,N+1,2):
        if N%D: continue
        nz=(C%D)!=0; g=np.gcd(C,D); s=(g*(-(-(D//g)//8))*nz).sum(1)
        alive&=~((nz.sum(1)>=2)&(s<D))
    r['covdie_par']=int((~par).sum()); r['covdie_L7']=int((par&~alive).sum()); r['open']=int(alive.sum())
    r['open_distinct']=len(set(tuple(sorted(int(v) for v in row)) for row in C[alive]))
    r['covered']=int(covered.sum())
    return r
def run_chunk(arg):
    key,s,e=arg; p,M=key; fn=f"{OUT}/{p}_{M}_{s}.pkl"
    if os.path.exists(fn): return arg,'cached'
    t0=time.time()
    W,O=NODES[key]; res=S1[key]['res']; out=[]
    for i in range(s,e):
        Dz,good,mn,mx=res[i]
        r=node_direct([int(z) for z in W[i]],M,Dz,good); r['i']=i; r['nopen_csv']=int(O[i]); out.append(r)
    pickle.dump(out,open(fn+'.tmp','wb')); os.replace(fn+'.tmp',fn)
    return arg,time.time()-t0
NODES=pickle.load(open(os.environ.get('R46NODES','/workspace/work/r46/nodes.pkl'),'rb'))
S1={}
import glob
for f in glob.glob('/workspace/work/r46/s1'+os.environ.get('R46SUF','')+'/*.pkl'):
    d=pickle.load(open(f,'rb')); S1[d['key']]=d
if __name__=='__main__':
    os.makedirs(OUT,exist_ok=True)
    tl=float(sys.argv[1]); CH=int(sys.argv[2]) if len(sys.argv)>2 else 500
    keys=sys.argv[3].split(';') if len(sys.argv)>3 else None
    jobs=[]
    for key in sorted(NODES,key=lambda k:(k[1]//k[0],k)):
        if keys and f"{key[0]},{key[1]}" not in keys: continue
        n=len(NODES[key][0])
        for s in range(0,n,CH):
            if not os.path.exists(f"{OUT}/{key[0]}_{key[1]}_{s}.pkl"): jobs.append((key,s,min(n,s+CH)))
    print('jobs left',len(jobs),flush=True)
    t0=time.time()
    with Pool(2) as P:
        for r in P.imap_unordered(run_chunk,jobs):
            print(r,flush=True)
            if time.time()-t0>tl: P.terminate(); break
