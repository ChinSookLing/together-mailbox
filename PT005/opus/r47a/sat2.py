import gzip,csv,numpy as np,collections,sys
from multiprocessing import Pool
def analyze(args):
    p,M,W=args
    W=np.array(W,dtype=np.int64); N=2*M
    T=np.arange(1,M+1,2,dtype=np.int64)                 # odd T <= N/2 at child level
    A0=((16*np.minimum((T[:,None]*W[None,:])%N, N-(T[:,None]*W[None,:])%N))<N)        # bit 0
    W1=W+M
    A1=((16*np.minimum((T[:,None]*W1[None,:])%N, N-(T[:,None]*W1[None,:])%N))<N)       # bit 1
    both=(A0&A1).any(axis=1)
    keep=~both
    a0=A0[keep]; a1=A1[keep]
    k=(a0|a1).sum(axis=1)
    if (k==0).any(): return 'empty'
    # unit + binary clauses -> 2-SAT
    lits=[]  # clause as list of (var,val)
    for r0,r1,kk in zip(a0,a1,k):
        if kk<=2:
            cl=[(i,0) for i in np.nonzero(r0)[0]]+[(i,1) for i in np.nonzero(r1)[0]]
            lits.append(cl)
    # brute force over 2^15 restricted to clauses of size<=2 (bitmask vectorised)
    asg=np.arange(1<<15,dtype=np.int64)
    ok=np.ones(1<<15,bool)
    for cl in lits:
        s=np.zeros(1<<15,bool)
        for i,v in cl: s|=(((asg>>int(i))&1)==v)
        ok&=s
        if not ok.any(): return 'sat2'
    return 'none'
def main():
    rows=list(csv.DictReader(gzip.open(sys.argv[1],'rt')))
    jobs=[(int(r['p']),int(r['M']),list(map(int,r['coords'].split()))) for r in rows]
    dead=np.array([int(r['n_open_children'])==0 for r in rows]); kk=np.array([int(r['k']) for r in rows]); pp=np.array([int(r['p']) for r in rows])
    with Pool(2) as pool: res=pool.map(analyze,jobs,chunksize=2000)
    res=np.array(res)
    tab=collections.Counter(zip(res,dead,kk>=1,pp==17))
    for key in sorted(tab): print("cert=%s dead=%s k>=1=%s p17=%s : %d"%(key+(tab[key],)))
    np.save("sat2_res.npy",res)
main()
