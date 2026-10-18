# Puck independent reproduction of chair note 103 (PT005 R47 Track A) sec 1 and sec 2.
# Written from the note's definitions + Puck's R43 COMMON engine definition of "covered" (16*||T*w||_N < N).
# Does NOT import or copy Opus r47a.py / sat2.py. 2-SAT decided by implication-graph transitive closure
# (Warshall on 30 literal bitmasks), not by 2^15 brute force.
# Node at level M (k>=1, M even), child level N=2M, lift coords w_i + b_i*M.
# Clause for odd T in [1,M]: OR over (i,b) with 16*||T*(w_i+b*M)||_N < N. Drop clause if some i works for both b.
# Keep clauses with <=2 literals. 2-SAT-dead iff kept clauses unsatisfiable. Empty clause -> 'empty' (also dead certificate).
# Sec 1: singleton cert at level M: odd t in [1,M), 2t!=M, E={i: 8*||t*w_i||_M < M} has |E|=1 and that w_i odd.
import gzip,csv,sys,collections,numpy as np
from multiprocessing import Pool
def dist(R,N): R=R%N; return np.minimum(R,N-R)
def closure_unsat(pairs):
    # literal id = 2*i+b ; negation = id^1
    adj=[0]*30
    for a,b in pairs:
        adj[a^1]|=1<<b; adj[b^1]|=1<<a
    for k in range(30):
        bk=1<<k; rk=adj[k]
        for i in range(30):
            if adj[i]&bk: adj[i]|=rk
    for i in range(15):
        p,n=2*i,2*i+1
        if (adj[p]>>n)&1 and (adj[n]>>p)&1: return True
    return False
def job(args):
    p,M,ids,W=args
    W=np.array(W,dtype=np.int64); out=[]
    # sec 1 singleton certificate (level M)
    t=np.arange(1,M,2,dtype=np.int64); t=t[2*t!=M]
    near=8*dist(W[:,None,:]*t[None,:,None],M)<M          # n,t,15
    single=near.sum(2)==1
    oddsing=(near&(W%2==1)[:,None,:]).any(2)&single
    cert1=oddsing.any(1)
    if M%2==1:
        return [(ids[j],bool(cert1[j]),'NA') for j in range(len(ids))]
    N=2*M; T=np.arange(1,M+1,2,dtype=np.int64)
    A0=16*dist(W[:,None,:]*T[None,:,None],N)<N           # n,T,15
    A1=16*dist((W[:,None,:]+M)*T[None,:,None],N)<N
    both=(A0&A1).any(2)
    L=A0|A1; sz=L.sum(2)
    keep=(~both)&(sz<=2)
    first=L.argmax(2); last=14-L[:,:,::-1].argmax(2)
    b1=np.take_along_axis(A1,first[:,:,None],2)[:,:,0]; b2=np.take_along_axis(A1,last[:,:,None],2)[:,:,0]
    l1=2*first+b1; l2=2*last+b2
    for j in range(len(ids)):
        kj=keep[j]
        if (kj&(sz[j]==0)).any(): out.append((ids[j],bool(cert1[j]),'empty')); continue
        pr=set(zip(l1[j][kj].tolist(),l2[j][kj].tolist()))
        out.append((ids[j],bool(cert1[j]),'sat2' if closure_unsat(pr) else 'none'))
    return out
def gen(rows):
    g=collections.defaultdict(list)
    for i,r in enumerate(rows): g[(r[0],r[2])].append(i)
    for (p,M),idx in sorted(g.items()):
        nT=M//2+1; B=max(50,min(2000,12_000_000//(nT*15)))
        for s in range(0,len(idx),B):
            ii=idx[s:s+B]; yield (p,M,ii,[rows[i][3] for i in ii])
def main():
    rows=[]
    for r in csv.DictReader(gzip.open(sys.argv[1],'rt')):
        rows.append((int(r['p']),int(r['k']),int(r['M']),list(map(int,r['coords'].split())),int(r['n_open_children'])))
    res=[None]*len(rows)
    with Pool(int(sys.argv[2]) if len(sys.argv)>2 else 3) as pool:
        for out in pool.imap_unordered(job,gen(rows)):
            for i,c1,c2 in out: res[i]=(c1,c2)
    tab1=collections.Counter(); tab2=collections.Counter()
    with gzip.open('per_node_2sat.tsv.gz','wt') as f:
        f.write('row\tp\tk\tM\tn_open_children\tsingleton_cert\tsat2\n')
        for i,(r,(c1,c2)) in enumerate(zip(rows,res)):
            dead=r[4]==0; grp='p17' if r[0]==17 else 'p>=19'
            tab1[('k>=1' if r[1]>=1 else 'k=0',c1,dead)]+=1
            tab2[(c2,dead,grp)]+=1
            f.write('%d\t%d\t%d\t%d\t%d\t%d\t%s\n'%(i,r[0],r[1],r[2],r[4],c1,c2))
    print('nodes',len(rows))
    print('SEC1 singleton cert (level k, cert, dead): count')
    for k in sorted(tab1): print(' ',k,tab1[k])
    print('SEC2 2-SAT (result, dead, group): count')
    for k in sorted(tab2): print(' ',k,tab2[k])
main()
