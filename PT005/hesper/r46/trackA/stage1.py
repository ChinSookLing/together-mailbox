# PT005 R46 Track A stage 1 (Hesper). For every Track A node (level M) and every lift child (level N=2M):
#  - exact per-coordinate share (in eighths) of each fibre a=0..(p-1)/2 at N from the GLM Theorem NZ/§4 table
#    and Lemma Z (zero fibre), for both lifts x and x+M of every coordinate;
#  - DIRECT per-coordinate covered counts on the actual fibre (T odd, 1<=T<=N/2, T = +-a mod p; covered iff 16||Tx||_N < N),
#    compared to the table (validation of every coordinate-lift-fibre triple used);
#  - per child share sums (they depend only on the lift bits of the depth-0 coordinates), number of children with all sums>=1.
import sys, os, pickle, numpy as np, time
from multiprocessing import Pool
OUT='/workspace/work/r46/s1'+os.environ.get('R46SUF','')
def v2a(x):
    v=np.zeros(x.shape,np.int64); y=x.copy()
    while True:
        m=(y%2==0)&(y>0)
        if not m.any(): break
        v[m]+=1; y[m]//=2
    return v,y
def share8(X,p,kp):
    """X int array (...), level N=2^kp p. returns (..., F) shares in eighths, F=(p+1)//2 (index 0 = zero fibre)."""
    F=(p+1)//2; a=np.arange(F)
    v,u=v2a(X); d=np.where(v<kp,kp-v,0)
    al=(a*u[...,None])%p
    odd=(al%2==1); even=~odd
    S=np.zeros(X.shape+(F,),np.int64)
    dd=d[...,None]+0*a
    nz=(a>0)
    # d>=5: 1 for every fibre
    S=np.where(dd>=5,1,S)
    S=np.where((dd==4)&nz&(al!=0),1,S)
    S=np.where((dd==3)&nz&((odd&(2*al<p))|(even&(2*al>p))),2,S)
    S=np.where((dd==2)&nz&((odd&(4*al<p))|(even&(4*al>3*p))),4,S)
    S=np.where((dd==1)&nz&((odd&(8*al<p))|(even&(8*al>7*p))),8,S)
    j=X>>kp  # depth 0: X=2^kp*j
    t=(a*j[...,None])%p; nrm=np.minimum(t,p-t)
    S=np.where((dd==0)&nz&(16*nrm<p),8,S)
    S=np.where((dd==0)&~nz,8,S)
    return S,d
def run_group(key):
    p,M=key; fn=f"{OUT}/{p}_{M}.pkl"
    if os.path.exists(fn): return key,'cached'
    t0=time.time()
    D=pickle.load(open(os.environ.get('R46NODES','/workspace/work/r46/nodes.pkl'),'rb')); W,_=D[key]
    N=2*M; kp=(N//p).bit_length()-1; F=(p+1)//2
    L=np.stack([W,W+M],axis=2)  # n,15,2
    S,d=share8(L,p,kp)           # n,15,2,F
    Ts=np.arange(1,M+1,2,dtype=np.int64); fT=np.minimum(Ts%p,p-Ts%p)
    OH=np.zeros((len(Ts),F),np.int64); OH[np.arange(len(Ts)),fT]=1
    sz=OH.sum(0)
    n=len(W); chunk=max(1,int(2e7//(30*len(Ts))))
    mism=0; ex=[]
    for s in range(0,n,chunk):
        X=L[s:s+chunk]
        r=(X[...,None]*Ts)%N; r=np.minimum(r,N-r)
        cov=(16*r<N).astype(np.int64)
        C=cov@OH  # c,15,2,F
        bad=(C*8!=S[s:s+chunk]*sz)
        if bad.any():
            mism+=int(bad.sum())
            for idx in np.argwhere(bad)[:5]: ex.append((s+idx[0],)+tuple(int(z) for z in idx[1:])+(int(C[tuple(idx)]),))
    # depth-0 coords at M are those with v2>=k ; at N their two lifts differ in depth (0 vs 1). Others: lifts share depth & alpha.
    same=(S[:,:,0,:]==S[:,:,1,:]).all(axis=2)  # n,15
    res=[]
    for i in range(n):
        Dz=np.nonzero(~same[i])[0]
        base=S[i,same[i],0,:].sum(0)
        A=base[None,:]
        for j in Dz:  # bit order of j in child index preserved by enumerating in increasing j
            A=np.concatenate([A+S[i,j,0],A+S[i,j,1]],axis=0)
        mn=A.min(1)
        good=np.nonzero(mn>=8)[0]
        res.append((tuple(int(z) for z in Dz), good.astype(np.int32), int(mn.min()), int(mn.max())))
    pickle.dump({'key':key,'kp':kp,'n':n,'mism':mism,'ex':ex,'res':res,'sz':sz.tolist(),
                 'checked_triples':int(n*15*2*F),'secs':time.time()-t0},open(fn+'.tmp','wb'))
    os.replace(fn+'.tmp',fn)
    return key,time.time()-t0
if __name__=='__main__':
    os.makedirs(OUT,exist_ok=True)
    D=pickle.load(open(os.environ.get('R46NODES','/workspace/work/r46/nodes.pkl'),'rb'))
    keys=sorted(D,key=lambda k:len(D[k][0]))
    if len(sys.argv)>1: keys=[k for k in keys if len(D[k][0])<=int(sys.argv[1])]
    with Pool(2) as P:
        for r in P.imap_unordered(run_group,keys): print(r,flush=True)
