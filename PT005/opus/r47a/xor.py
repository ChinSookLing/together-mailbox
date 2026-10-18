import gzip,csv,numpy as np,collections,sys
from multiprocessing import Pool
def analyze(args):
    p,M,W=args
    W=np.array(W,dtype=np.int64); N=2*M
    T=np.arange(1,M//2+1,2,dtype=np.int64); T=T[2*T!=M]
    R=(T[:,None]*W[None,:])%N
    D=np.minimum(R%M, M-R%M)                     # parent distance ||T w||_M
    act=(8*D<M)
    h=((R+M//2)%N >= M).astype(int)              # 1 if T w mod 2M near M
    odd=(W%2==1)
    # union-find with parity
    par=list(range(15)); rel=[0]*15
    def find(x):
        if par[x]==x: return x,0
        r,pp=find(par[x]); par[x]=r; rel[x]^=pp; return r,rel[x]
    for t in range(len(T)):
        E=np.nonzero(act[t])[0]
        if len(E)==0: return 'empty'
        if not odd[E].all(): continue
        if len(E)==1: return 'xor'            # singleton antipodal
        if len(E)==2:
            i,j=E; c=h[t,i]^h[t,j]^1
            ri,pi=find(i); rj,pj=find(j)
            if ri==rj:
                if pi^pj!=c: return 'xor'
            else:
                par[ri]=rj; rel[ri]=pi^pj^c
    return 'none'
def main():
    rows=list(csv.DictReader(gzip.open(sys.argv[1],'rt')))
    jobs=[(int(r['p']),int(r['M']),list(map(int,r['coords'].split()))) for r in rows if int(r['k'])>=1]
    dead=np.array([int(r['n_open_children'])==0 for r in rows if int(r['k'])>=1]); pp=np.array([int(r['p']) for r in rows if int(r['k'])>=1])
    with Pool(2) as pool: res=np.array(pool.map(analyze,jobs,chunksize=4000))
    sat=np.load("sat2_res.npy")[[i for i,r in enumerate(rows) if int(r['k'])>=1]]
    print(collections.Counter(zip(res,dead)))
    print("xor-dead among 2SAT-dead:",int(((res=='xor')&(sat=='sat2')).sum()),"of",int((sat=='sat2').sum()))
    print("xor-dead but not 2SAT-dead:",int(((res=='xor')&(sat!='sat2')).sum()))
main()
