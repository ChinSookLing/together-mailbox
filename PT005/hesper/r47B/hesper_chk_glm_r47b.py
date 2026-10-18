# Hesper check of GLM R47B final (Q1 no {0,1}; ARL: C_l(M-t)=complement if w odd else same; Q2 pair diagnostic) on 3000 random dataset nodes, all odd t<=M.
import gzip,csv,random
rows=[r for r in csv.DictReader(gzip.open('/workspace/work/together-mailbox/PT005/hesper/r45/widen/nodes_widen.csv.gz','rt')) if int(r['k'])>=1]
random.seed(4718); S=random.sample(rows,3000)
def C(t,w,M):
    N=2*M; out=set()
    for b in (0,1):
        r=(t*(w+b*M))%N
        if 16*min(r,N-r)<N: out.add(b)
    return out
bad01=badARL=badQ2=npair=0; ntests=0
for r in S:
    M=int(r['M']); W=list(map(int,r['coords'].split())); k=int(r['k']); p=int(r['p'])
    for t in range(1,M+1,2):
        Cs=[C(t,w,M) for w in W]; Cm=[C(M-t,w,M) for w in W]; ntests+=1
        for w,c,cm in zip(W,Cs,Cm):
            if len(c)==2: bad01+=1
            exp = {1-b for b in c} if w%2 else c
            if cm!=exp: badARL+=1
        reach=[i for i,c in enumerate(Cs) if c]
        if len(reach)==2:
            i,j=reach; x=next(iter(Cs[i])); y=next(iter(Cs[j])); npair+=1
            # Delta = t(wj-wi)/p mod 2^{k+1}; check in V_{x^y}: compare 4p*dist
            D=(t*(W[j]-W[i]))%(2**(k+1)*p); m=2**(k+1)*p
            c0=min(D,m-D); c1=abs(D-2**k*p)
            ok = (c0 < 2**(k-2)*p) if x==y else (c1 < 2**(k-2)*p)
            if not ok: badQ2+=1
print("nodes",len(S),"odd-t tests",ntests,"| Q1 {0,1} cases",bad01,"| ARL mismatches",badARL,"| two-reacher clauses",npair,"Q2 diagnostic failures",badQ2)
