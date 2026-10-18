# Puck: among CSV-dead nodes (n_open_children==0) that are NOT 2-SAT-dead (per Puck 2-SAT run, R47 trackA_2sat),
# test whether a covering child exists: child coords w_i+b_i*M at level N=2M, covered iff 16*||T*w'||_N < N for all odd T in [1,M].
# (Even T reduce to level-M coverage of the parent.) Meet-in-the-middle over the 2^15 bit choices. Independent of GPT's code.
import gzip,csv,sys
from multiprocessing import Pool
def one(a):
    idx,M,W=a; N=2*M; Ts=range(1,M+1,2)
    masks=[]
    for w in W:
        m0=m1=0
        for j,T in enumerate(Ts):
            r=(T*w)%N
            if 16*min(r,N-r)<N: m0|=1<<j
            r=(T*(w+M))%N
            if 16*min(r,N-r)<N: m1|=1<<j
        masks.append((m0,m1))
    full=(1<<len(Ts))-1
    def enum(ms):
        out={0:0}
        for i,(m0,m1) in enumerate(ms):
            nx={}
            for v,c in out.items():
                nx.setdefault(v|m0,c); nx.setdefault(v|m1,c|(1<<i))
            out=nx
        return out
    A=enum(masks[:7]); B=enum(masks[7:])
    n=0;ex=None
    for va,ca in A.items():
        need=full&~va
        for vb,cb in B.items():
            if need&~vb==0:
                n+=1
                if ex is None: ex=ca|(cb<<7)
    return idx,n,ex
rows=list(csv.DictReader(gzip.open('/workspace/mbx_pt5/PT005/hesper/r45/widen/nodes_widen.csv.gz','rt')))
cand=[]
for line in gzip.open('/workspace/mbx_pt5/PT005/puck/r47/trackA_2sat/per_node_2sat.tsv.gz','rt'):
    f=line.rstrip('\n').split('\t')
    if f[0]=='row': continue
    if f[4]=='0' and f[6]=='none' and int(f[3])%2==0: cand.append(int(f[0]))
print('candidates',len(cand),flush=True)
bad=[]
with Pool(7) as P:
    for k,(idx,n,ex) in enumerate(P.imap_unordered(one,[(i,int(rows[i]['M']),list(map(int,rows[i]['coords'].split()))) for i in cand],chunksize=50)):
        if n: bad.append((idx,n,ex))
        if k%10000==0: print('done',k,'bad',len(bad),flush=True)
bad.sort()
with open('mislabel_list.tsv','w') as f:
    f.write('row\tp\tk\tM\tsource\tn_covering_choices\texample_mask\n')
    for idx,n,ex in bad:
        r=rows[idx]; f.write(f"{idx}\t{r['p']}\t{r['k']}\t{r['M']}\t{r['source']}\t{n}\t{ex}\n")
print('TOTAL CSV-dead but covering child exists (pair-count of half-masks, distinct choices):',len(bad))
