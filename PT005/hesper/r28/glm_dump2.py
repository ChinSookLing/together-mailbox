import itertools,sys
from collections import Counter
p=17
def cls(N,b): return [t for t in range(1,N//2+1,2) if t%p in(b%p,(-b)%p)]
def cov(w,N,T): return frozenset(i for i,t in enumerate(T) if 16*min(t*w%N,N-t*w%N)<N)
legal=lambda w: w%2==1 and w%17 not in (0,1,16)
QR={1,2,4,8,9,13,15,16}
k=5
for b in range(1,9):
    N=17*2**k;T=cls(N,b);T2=cls(2*N,2*b%17);n2=len(T2)
    sig={}
    for w in range(1,N,2):
        if not legal(w): continue
        c=cov(w,N,T);a=cov(w,2*N,T2);bb=cov(w+N,2*N,T2)
        if a&bb: continue
        sig.setdefault((c,frozenset([a,bb])),[]).append(w)
    items=list(sig.items());full=frozenset(range(len(T)))
    res=[0,0];qr=Counter();rs=Counter()
    def dfs(used,mult,acc):
        if len(acc)==8:
            if used==full and all(v==2 for v in mult.values()) and len(mult)==n2:
                res[0]+=1
                pairs=[tuple(x[0][1]) for x in acc]
                ok=any(len(frozenset().union(*[pr[e] if len(pr)>1 else pr[0] for pr,e in zip(pairs,es)]))==n2 and sum(len(pr[e] if len(pr)>1 else pr[0]) for pr,e in zip(pairs,es))==n2 for es in itertools.product((0,1),repeat=8))
                if ok:
                    res[1]+=1; ws=[x[1][0] for x in acc]
                    qr[sum(w%17 in QR for w in ws)]+=1; rs[tuple(sorted(w%17 for w in ws))]+=1
            return
        i=min(full-used)
        for key,ws in items:
            c,pr=key
            if i in c and not(c&used):
                m=mult.copy();ok=True
                for s in pr:
                    for x in s:
                        m[x]+=1
                        if m[x]>2: ok=False
                if ok: dfs(used|c,m,acc+[(key,ws)])
    dfs(frozenset(),Counter(),[])
    print(f"b={b} classes={len(items)} proj_exact2cover={res[0]} doubling={res[1]} QR={dict(qr)} res={rs.most_common(3)}",flush=True)
