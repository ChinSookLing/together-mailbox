# Puck check of GPT R46B Antipodal Singleton Lemma counts on the 2,712 nodes.
import gzip, collections
base='/workspace/mbx_pt5/PT005/hesper'
nodes=[]
with gzip.open(base+'/r45/widen/nodes_widen.csv.gz','rt') as f:
    next(f)
    for line in f:
        a=line.rstrip('\n').split(','); nodes.append((int(a[0]),int(a[2]),list(map(int,a[3].split()))))
k1=set(); kk={}
for line in open('detail.tsv'):
    cl,p,M,k=map(int,line.split()); kk[cl]=k
cert_nodes=0; cert_t_all=0; cert_t_half=0; byk=collections.Counter(); ex=None
for cl,k in kk.items():
    p,M,w=nodes[cl-2]; n_all=0; n_half=0
    for t in range(1,M+1,2):
        E=[x for x in w if 8*min((t*x)%M, M-(t*x)%M) < M]
        if len(E)==1 and E[0]%2==1 and 2*t!=M:
            n_all+=1
            if t<M-t: n_half+=1
    if n_all: cert_nodes+=1; byk[k]+=1
    cert_t_all+=n_all; cert_t_half+=n_half
    if cl==598: ex=(p,M,w,n_all)
print('nodes with certificate',cert_nodes,'by min-blocking k',dict(byk))
print('certificate times counted over all odd t<=M:',cert_t_all,' pairs (t<M-t):',cert_t_half)
print('line 598:',ex)
p,M,w,_=ex; t=89
print('E(89)=',[x for x in w if 8*min((t*x)%M,M-(t*x)%M)<M], 'other min dist', min(min((t*x)%M,M-(t*x)%M) for x in w if x!=3))
