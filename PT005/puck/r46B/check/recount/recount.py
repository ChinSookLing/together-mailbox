# Puck recount of Astra R46B claim: 2,712 all-pass-but-dead nodes split by minimal number of fibres that jointly block.
import gzip, numpy as np, itertools, collections
base='/workspace/mbx_pt5/PT005/hesper'
nodes=[]
with gzip.open(base+'/r45/widen/nodes_widen.csv.gz','rt') as f:
    next(f)
    for line in f:
        a=line.rstrip('\n').split(','); nodes.append((int(a[0]),int(a[2]),list(map(int,a[3].split()))))
sel=[]
with gzip.open(base+'/r46/trackA/per_node_trackA.csv.gz','rt') as f:
    next(f)
    for line in f:
        a=line.split(',')
        if int(a[4])==32768 and int(a[5])==0: sel.append(int(a[0]))
print('selected',len(sel))
BITS=((np.arange(1<<15)[:,None]>>np.arange(15)[None,:])&1).astype(bool)
res=collections.Counter(); byp=collections.Counter(); detail=[]
for cl in sel:
    p,M,w=nodes[cl-2]  # csv_line 2 = first data row
    N=2*M; Ts=np.arange(1,M+1,2,dtype=np.int64)
    # covered matrix per coordinate per lift choice: shape (15,2,nT)
    C=np.zeros((15,2,len(Ts)),bool)
    for i,x in enumerate(w):
        for b,y in enumerate((x,x+M)):
            r=(Ts*y)%N; d=np.minimum(r,N-r); C[i,b]=16*d<N
    # coverage for all lifts: OR over coords
    cov=np.zeros((1<<15,len(Ts)),bool)
    for i in range(15):
        cov|=np.where(BITS[:,i][:,None],C[i,1][None,:],C[i,0][None,:])
    assert not cov.all(axis=1).any()
    res_mod=Ts%p; fib=np.minimum(res_mod,p-res_mod)
    fibres=sorted(set(fib.tolist()))
    okf={a:cov[:,fib==a].all(axis=1) for a in fibres}  # lifts covering fibre a
    k=None
    for r in range(1,len(fibres)+1):
        for S in itertools.combinations(fibres,r):
            m=np.ones(1<<15,bool)
            for a in S: m&=okf[a]
            if not m.any(): k=r; break
        if k: break
    res[k]+=1; byp[(p,k)]+=1
    detail.append((cl,p,M,k))
print('min blocking fibre count:',dict(sorted(res.items())))
print('by p:',dict(sorted(byp.items())))
with open('detail.tsv','w') as f:
    for d in detail: f.write('\t'.join(map(str,d))+'\n')
