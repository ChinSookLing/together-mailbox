# Puck: how many coordinates does a 2-SAT death need? Same 2000-node sample/seed as puck_chk_glm_r47b.py.
# width1 = contradictory units on one coordinate; width2 = short clauses on some pair {i,j} alone UNSAT; width>=3 = rest.
import gzip,csv,random,itertools,sys
from collections import Counter
sys.setrecursionlimit(10000)
rows=[r for r in csv.DictReader(gzip.open('PT005/hesper/r45/widen/nodes_widen.csv.gz','rt')) if int(r['k'])>=1]
random.seed(20261018+1624); S=random.sample(rows,min(2000,len(rows)))
def cov(t,w,M):
    N=2*M; return [b for b in (0,1) if 16*min((t*(w+b*M))%N,N-(t*(w+b*M))%N)<N]
def sat2(n,cl):
    # literal (i,b) -> node 2i+b ; clause list of tuples of literals (1 or 2)
    G=[[] for _ in range(2*n)]
    for c in cl:
        a=c[0]; b=c[1] if len(c)==2 else c[0]
        G[2*a[0]+1-a[1]].append(2*b[0]+b[1]); G[2*b[0]+1-b[1]].append(2*a[0]+a[1])
    idx=[None]*(2*n); low=[0]*(2*n); on=[False]*(2*n); st=[]; comp=[None]*(2*n); c=[0,0]
    def dfs(v):
        idx[v]=low[v]=c[0]; c[0]+=1; st.append(v); on[v]=True
        for u in G[v]:
            if idx[u] is None: dfs(u); low[v]=min(low[v],low[u])
            elif on[u]: low[v]=min(low[v],idx[u])
        if low[v]==idx[v]:
            while True:
                u=st.pop(); on[u]=False; comp[u]=c[1]
                if u==v: break
            c[1]+=1
    for v in range(2*n):
        if idx[v] is None: dfs(v)
    return all(comp[2*i]!=comp[2*i+1] for i in range(n))
cnt=Counter()
for r in S:
    M=int(r['M']); W=list(map(int,r['coords'].split())); dead=int(r['n_open_children'])==0
    cl=[]; empty=False
    for t in range(1,M+1,2):
        C=[cov(t,w,M) for w in W]
        R=[(i,C[i][0]) for i in range(15) if C[i]]
        if not R: empty=True
        if len(R)<=2: cl.append(tuple(R))
    cl=[c for c in cl if c]
    s2dead = empty or not sat2(15,cl)
    if not s2dead: cnt['dead' if dead else 'live','2sat-ok']+=1; continue
    if empty: w='empty'
    else:
        units={c[0] for c in cl if len(c)==1}
        if any((i,1-b) in units for (i,b) in units): w='w1'
        else:
            w='w3+'
            for i,j in itertools.combinations(range(15),2):
                sub=[c for c in cl if all(l[0] in (i,j) for l in c)]
                if any(all(any(l[1]==(x if l[0]==i else y) for l in c) for c in sub) for x in (0,1) for y in (0,1)): continue
                w='w2'; break
    cnt['dead' if dead else 'live',w]+=1
for k,v in sorted(cnt.items()): print(k,v)
