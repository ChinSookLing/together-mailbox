# Puck independent check of GLM R47B final (Hesper 3607751). Own code, own seed.
# Tests: Q1 (no C={0,1} for odd T), ARL (C_l(M-t) = complement if w_l odd else same),
# Q2 (two-reacher clause bits x,y => Delta=T(wj-wi) mod 2M within M/4 of 0 if x==y, of M if x!=y),
# pair-kill closure (odd pair: patterns closed under complement; kill <=> all 4 patterns <=> 2 non-complementary patterns),
# g>=k frozen (v2(wj-wi)>=k: x^y constant over two-reacher T in one class T mod p).
import gzip,csv,random,sys
from collections import defaultdict
rows=[r for r in csv.DictReader(gzip.open('PT005/hesper/r45/widen/nodes_widen.csv.gz','rt')) if int(r['k'])>=1]
random.seed(20261018+1624); S=random.sample(rows,min(2000,len(rows)))
def cov(t,w,M):
    N=2*M; return [b for b in (0,1) if 16*min((t*(w+b*M))%N,N-(t*(w+b*M))%N)<N]
def v2(n):
    n=abs(n); c=0
    if n==0: return 99
    while n%2==0: n//=2; c+=1
    return c
q1=arl=q2=nq2=clos=nclos=frz=nfrz=0; ntest=0; pairkill=0; pairkill_bad=0; oddpairs=0
for r in S:
    M=int(r['M']); W=list(map(int,r['coords'].split())); k=int(r['k']); p=int(r['p']); N=2*M
    pats=defaultdict(dict)  # (i,j)->{t:(x,y)}
    for t in range(1,M+1,2):
        C=[cov(t,w,M) for w in W]; Cm=[cov(M-t,w,M) for w in W]; ntest+=1
        for w,c,cm in zip(W,C,Cm):
            if len(c)==2: q1+=1
            if sorted(cm)!=sorted(([1-b for b in c]) if w%2 else c): arl+=1
        R=[i for i,c in enumerate(C) if c]
        if len(R)==2:
            i,j=R; x,y=C[i][0],C[j][0]; nq2+=1
            D=(t*(W[j]-W[i]))%N
            d=min(D,N-D) if x==y else abs(D-M)
            if not 4*d<M: q2+=1
            pats[(i,j)][t]=(x,y)
    for (i,j),tp in pats.items():
        if W[i]%2 and W[j]%2:
            oddpairs+=1
            for t,(x,y) in tp.items():
                nclos+=1
                if tp.get(M-t)!=(1-x,1-y): clos+=1
            P=set(tp.values())
            kill = len(P)==4
            alt = any((a[0]==b[0])!=(a[1]==b[1]) for a in P for b in P)
            pairkill+=kill
            if kill!=alt: pairkill_bad+=1
        if v2(W[j]-W[i])>=k:
            cls=defaultdict(set)
            for t,(x,y) in tp.items(): cls[t%p].add(x^y)
            for s in cls.values():
                nfrz+=1
                if len(s)>1: frz+=1
print(f"nodes {len(S)} odd-t {ntest} | Q1 fails {q1} | ARL fails {arl} | Q2 clauses {nq2} fails {q2}")
print(f"odd pairs with 2-reacher clauses {oddpairs} | closure tests {nclos} fails {clos} | pair kills {pairkill} kill-vs-2pattern mismatches {pairkill_bad}")
print(f"g>=k classes {nfrz} non-constant x^y {frz}")
