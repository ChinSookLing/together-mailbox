# Puck independent check of Hesper R47C (cdab826): odd-only SAT on the 689,581 target set + length-2 count.
# Written from Puck's own puck_2sat.py (R47 Track A, notes 103/104 definitions); does NOT import or copy hesper_r47c.py.
# Child level N=2M, lift w_i+b*M covers odd T in [1,M] iff 16*||T*(w_i+bM)||_N < N. Clause at T = OR of covering literals.
# Keep clauses with <=2 literals (drop tautological ones). 2-SAT via Warshall closure on 30 literal bitmasks.
# odd-only: keep only kept clauses whose every literal is on a coordinate with w_i odd.
# len2: some var i has two unit clauses forcing opposite bits (= shortest implication cycle of length 2).
# XOR flag: xor_flags.txt.gz = chair xor.py result (Puck r47b report: reproduced by Puck xor_indep.py, 0 per-node disagreement); also = Hesper r47c xor column (compare.py).
import gzip,csv,sys,collections,numpy as np
from multiprocessing import Pool
def dist(R,N): R=R%N; return np.minimum(R,N-R)
def unsat(pairs):
    adj=[0]*30
    for a,b in pairs: adj[a^1]|=1<<b; adj[b^1]|=1<<a
    for k in range(30):
        bk=1<<k; rk=adj[k]
        for i in range(30):
            if adj[i]&bk: adj[i]|=rk
    return any((adj[2*i]>>(2*i+1))&1 and (adj[2*i+1]>>(2*i))&1 for i in range(15))
def job(a):
    M,ids,W=a; W=np.array(W,dtype=np.int64); N=2*M
    T=np.arange(1,M+1,2,dtype=np.int64)
    A0=16*dist(W[:,None,:]*T[None,:,None],N)<N; A1=16*dist((W[:,None,:]+M)*T[None,:,None],N)<N
    both=(A0&A1).any(2); L=A0|A1; sz=L.sum(2); keep=(~both)&(sz<=2)
    first=L.argmax(2); last=14-L[:,:,::-1].argmax(2)
    b1=np.take_along_axis(A1,first[:,:,None],2)[:,:,0]; b2=np.take_along_axis(A1,last[:,:,None],2)[:,:,0]
    l1=2*first+b1; l2=2*last+b2
    odd=(W%2==1)
    out=[]
    for j in range(len(ids)):
        kj=keep[j]; ntaut=int(both[j].sum()); nempty=int((sz[j]==0).sum())
        a1=l1[j][kj]; a2=l2[j][kj]; v1=a1>>1; v2=a2>>1
        pr=list(zip(a1.tolist(),a2.tolist()))
        full=unsat(set(pr))
        oo=odd[j][v1]&odd[j][v2]
        po=set(zip(a1[oo].tolist(),a2[oo].tolist()))
        oddu=unsat(po)
        units=set(x for x,y in pr if x==y)
        len2=any((u^1) in units for u in units)
        len2even=any((u^1) in units and not odd[j][u>>1] for u in units)
        out.append((ids[j],full,oddu,len2,len2even,ntaut,nempty))
    return out
def gen(rows):
    g=collections.defaultdict(list)
    for i,r in enumerate(rows): g[r[1]].append(i)
    for M,idx in sorted(g.items()):
        B=max(50,min(2000,12_000_000//((M//2+1)*15)))
        for s in range(0,len(idx),B):
            ii=idx[s:s+B]; yield (M,ii,[rows[i][2] for i in ii])
rows=[]
for r in csv.DictReader(gzip.open(sys.argv[1],'rt')):
    if int(r['k'])>=1: rows.append((int(r['p']),int(r['M']),list(map(int,r['coords'].split())),int(r['n_open_children'])==0))
xor=(np.load(sys.argv[2])=='xor') if sys.argv[2].endswith('.npy') else np.array([c=='1' for c in gzip.open(sys.argv[2],'rt').read().strip()]); assert len(xor)==len(rows)
res=[None]*len(rows)
with Pool(3) as pool:
    for out in pool.imap_unordered(job,gen(rows)):
        for t in out: res[t[0]]=t[1:]
C=collections.Counter(); P=collections.Counter()
with gzip.open('per_node_puck_r47c.tsv.gz','wt') as f:
    f.write('row\tp\tM\tdead\txor\tsat2\toddonly_unsat\tlen2\tlen2_even\n')
    for i,(r,(full,oddu,l2,l2e,nt,ne)) in enumerate(zip(rows,res)):
        C['taut']+=nt; C['empty']+=ne
        C['dead']+=r[3]; C['sat2']+=full; C['sat2_live']+=full and not r[3]; C['xor']+=xor[i]
        C['xor_not_sat2']+=xor[i] and not full
        tgt=full and not xor[i]
        if tgt:
            C['target']+=1; C['target_oddonly_unsat']+=oddu; C['target_len2']+=l2; C['target_len2_even']+=l2e
            P[(r[0],'target')]+=1; P[(r[0],'len2')]+=l2
        if xor[i]: C['xor_oddonly_unsat']+=oddu; C['xor_len2']+=l2
        f.write('%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n'%(i,r[0],r[1],r[3],xor[i],full,oddu,l2,l2e))
print('k>=1 nodes',len(rows))
for k in sorted(C): print(k,C[k])
print('per p: p target len2')
for p in sorted({k[0] for k in P}): print(p,P[(p,'target')],P[(p,'len2')])
