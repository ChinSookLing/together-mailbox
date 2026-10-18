# Puck: check GPT R47B claim: CSV row 1069130 (0-based data row) labelled n_open_children=0 but has covering children.
import gzip,csv,numpy as np,sys
rows=list(csv.DictReader(gzip.open('/workspace/mbx_pt5/PT005/hesper/r45/widen/nodes_widen.csv.gz','rt')))
def count(r):
    M=int(r['M']); W=np.array(list(map(int,r['coords'].split())),dtype=np.int64); N=2*M
    T=np.arange(1,M+1,2,dtype=np.int64)
    def cov(w): R=(w*T)%N; return 16*np.minimum(R,N-R)<N
    A0=np.array([cov(w) for w in W]); A1=np.array([cov(w+M) for w in W])   # 15 x nT
    masks=np.arange(1<<15)
    bits=((masks[:,None]>>np.arange(15)[None,:])&1).astype(bool)          # 32768 x 15
    good=[]
    # covered[m,T] = OR_i (bit? A1 : A0)
    C=np.zeros((1<<15,len(T)),dtype=bool)
    for i in range(15):
        C|=np.where(bits[:,i:i+1],A1[i][None,:],A0[i][None,:])
    ok=C.all(1)
    return M,W,int(ok.sum()),np.nonzero(ok)[0]
for idx in map(int,sys.argv[1:]):
    r=rows[idx]; M,W,n,good=count(r)
    print(idx,'p',r['p'],'k',r['k'],'M',M,'coords',r['coords'],'csv n_open',r['n_open_children'],'source',r['source'],'| Puck covering children (odd T<=M):',n, 'masks',good[:20].tolist())
    if 17625 in good: print('  mask 17625 child:',[int(w+((17625>>i)&1)*M) for i,w in enumerate(W)])
