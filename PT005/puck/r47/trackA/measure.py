# Puck R47 Track A: singleton (antipodal) certificate, min |E_M(t)|, survival depth, over all Track A nodes.
# E_M(t) = coords i (multiset, duplicates count) with 8*||t*w_i||_M < M, t odd in [1,M), 2t != M.
# Certificate: some such t with |E_M(t)| = 1 and that w_i odd (GPT Antipodal Singleton Lemma, note 102 sec 3).
import gzip, collections, numpy as np, sys
base='/workspace/mbx_pt5/PT005/hesper'
rows=[]
with gzip.open(base+'/r45/widen/nodes_widen.csv.gz','rt') as f:
    hdr=next(f).rstrip().split(',')
    for i,line in enumerate(f):
      a=line.rstrip('\n').split(',')
      rows.append((i+2,int(a[0]),int(a[2]),tuple(map(int,a[3].split())),int(a[10]),int(a[11])))
pn={}
with gzip.open(base+'/r46/trackA/per_node_trackA.csv.gz','rt') as f:
    next(f)
    for line in f:
      a=list(map(int,line.split(',')))
      pn[a[0]]=a
bym=collections.defaultdict(list)
for r in rows: bym[r[2]].append(r)
out=open('per_node_r47.tsv','w'); out.write('csv_line\tp\tM\tsurv\tn_open\tcert\tn_cert_t\tminE\tminE_t\tE0\tpair_t\tchildren_all_ge1\tchildren_covered\n')
def chunks(rs,n=4000):
    for i in range(0,len(rs),n): yield rs[i:i+n]
for M,rs_all in sorted(bym.items()):
  if M%2: 
    for r in rs_all: out.write(f'{r[0]}\t{r[1]}\t{M}\t{r[4]}\t{r[5]}\tNA\tNA\tNA\tNA\tNA\tNA\t-1\t-1\n')
    continue
  for rs in chunks(rs_all):
    W=np.array([r[3] for r in rs],dtype=np.int64)            # n x 15
    ts=np.array([t for t in range(1,M,2) if 2*t!=M],dtype=np.int64)
    r_=(W[:,None,:]*ts[None,:,None])%M                       # n x T x 15
    d=np.minimum(r_,M-r_)
    inE=(8*d<M)
    sz=inE.sum(2)                                            # n x T
    odd=(W%2==1)
    one=(sz==1)
    idx=inE.argmax(2)
    wi_odd=np.take_along_axis(np.broadcast_to(odd[:,None,:],inE.shape),idx[:,:,None],2)[:,:,0]
    cert=one&wi_odd
    ncert=cert.sum(1); minE=sz.min(1); minEt=ts[sz.argmin(1)]; E0=(sz==0).any(1); pair=(sz==2).sum(1)
    for k,r in enumerate(rs):
        a=pn.get(r[0]); ca=a[4] if a else -1; cc=a[5] if a else -1
        out.write(f'{r[0]}\t{r[1]}\t{M}\t{r[4]}\t{r[5]}\t{int(ncert[k]>0)}\t{ncert[k]}\t{minE[k]}\t{minEt[k]}\t{int(E0[k])}\t{pair[k]}\t{ca}\t{cc}\n')
out.close()
print('header',hdr)
