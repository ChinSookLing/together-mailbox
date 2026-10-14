exec(open('glm_dump2.py').read().split('k=5\nfor b')[0])
k=5
for b in (3,6):
    N=17*2**k;T=cls(N,b);T2=cls(2*N,2*b%17);n2=len(T2)
    sig={}
    for w in range(1,N,2):
        if not legal(w): continue
        c=cov(w,N,T);a=cov(w,2*N,T2);bb=cov(w+N,2*N,T2)
        if a&bb: continue
        sig.setdefault((c,frozenset([a,bb])),[]).append(w)
    items=list(sig.items());full=frozenset(range(len(T)));out=[]
    def dfs(used,mult,acc):
        if out: return
        if len(acc)==8:
            if used==full and all(v==2 for v in mult.values()) and len(mult)==n2:
                ws=[x[1][0] for x in acc]
                ok=any(len(frozenset().union(*[cov(w+e*N,2*N,T2) for w,e in zip(ws,es)]))==n2 for es in itertools.product((0,1),repeat=8))
                if ok==(b==6): out.append(ws)
            return
        i=min(full-used)
        for key,ws in items:
            c,pr=key
            if i in c and not(c&used):
                m=mult.copy();o=True
                for s in pr:
                    for x in s:
                        m[x]+=1; o=o and m[x]<=2
                if o: dfs(used|c,m,acc+[(key,ws)])
    dfs(frozenset(),Counter(),[])
    ws=out[0];print('b',b,'ws',ws,'C5',T,'C6',T2)
    for w in ws: print(' w',w,'L5',[T[i] for i in sorted(cov(w,N,T))],'eps0',[T2[i] for i in sorted(cov(w,2*N,T2))],'eps1',[T2[i] for i in sorted(cov(w+N,2*N,T2))])
