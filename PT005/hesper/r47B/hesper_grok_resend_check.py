import itertools
def cov(w,T,N): r=(T*w)%N; return 16*min(r,N-r)<N
def clauses(ws,M):
    N=2*M; out=[]
    for T in range(1,M+1,2):
        cl=[];drop=False
        for i,w in enumerate(ws):
            C=[b for b in (0,1) if cov(w+b*M,T,N)]
            if len(C)==2: drop=True;break
            if C: cl.append((i,C[0]))
        if not drop: out.append(cl)
    return out
def dead2(ws,M):
    cls=[c for c in clauses(ws,M) if len(c)<=2]
    if any(len(c)==0 for c in cls): return True
    n=len(ws); g={v:[] for v in range(2*n)}
    lit=lambda i,x:2*i+x
    for c in cls:
        if len(c)==1: (i,x),=c; g[lit(i,1-x)].append(lit(i,x))
        else:
            (i,x),(j,y)=c; g[lit(i,1-x)].append(lit(j,y)); g[lit(j,1-y)].append(lit(i,x))
    def reach(s):
        seen={s};st=[s]
        while st:
            u=st.pop()
            for v in g[u]:
                if v not in seen: seen.add(v);st.append(v)
        return seen
    R={v:reach(v) for v in g}
    return any(lit(i,1) in R[lit(i,0)] and lit(i,0) in R[lit(i,1)] for i in range(n))
ws=[23,8,31,29,0,3,15,7,14,25,17,32,22,2,10]
path=[(1,0,1,0,0,0,0,0,0,0,1,0,0,1,1),(1,0,0,1,0,1,0,0,1,1,1,1,0,1,0),(1,0,1,1,0,0,1,1,0,1,0,1,0,1,1),(1,1,0,1,0,0,1,1,1,0,0,1,1,0,1),(0,0,0,0,0,0,1,1,1,1,1,0,0,0,1),(1,1,1,1,0,1,0,0,0,1,1,0,0,1,0)]
M=38
# zero coord: odd T clause literal check
print("w=0 lit in every clause at M=38:", all(any(i==4 and x==0 for i,x in c) for c in clauses(ws,M)), "nclauses",len(clauses(ws,M)))
cur=ws[:]
for b in path:
    full=dead2(cur,M); no0=dead2([w for i,w in enumerate(cur) if i!=4],M)
    print("M",M,"with0 dead2",full,"without0 dead2",no0, "uncovered-free-T (clause empty) w/o0:", sum(1 for c in clauses([w for i,w in enumerate(cur) if i!=4],M) if not c))
    cur=[w+bi*M for w,bi in zip(cur,b)]; M*=2
print("M",M,dead2(cur,M),dead2([w for i,w in enumerate(cur) if i!=4],M))
