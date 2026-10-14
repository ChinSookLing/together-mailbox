# Puck independent check, PT005 R29d, p=17, N=544, k=5->6, one class.
# Model: real covers via CRT. Odd residue x mod 32 <-> member t' (t' = x mod 32, t' = +-b mod 17, |t'|<=271).
# Coordinate w covers member at level 5 iff t'w = v (mod 544), v odd, |v|<=33; at level 6 (2b) iff |v|<=67, lift bit = parity of the quotient.
N=544; X=list(range(1,32,2))
def rep(a,x):            # t' in (-272,272), t' = x mod 32, t' = a mod 17
    for t in range(-271,272):
        if t%32==x and (t-a)%17==0: return t
def cover(w,a,lim):
    out=[]
    for j,x in enumerate(X):
        t=rep(a,x); v=t*w; q=round(v/N); r=v-N*q
        if abs(r)<=lim: out.append((j,q&1))
    return out
import itertools
def solvable(n,edges):
    col={}
    for s in range(n):
        if s in col: continue
        col[s]=0; st=[s]
        while st:
            u=st.pop()
            for (a,b,l) in edges:
                for p,q in ((a,b),(b,a)):
                    if p==u:
                        want=col[u]^l
                        if q not in col: col[q]=want; st.append(q)
                        elif col[q]!=want: return False
    return True

SOC={}
from collections import deque
def soc(edges):
    best=99
    for s in range(8):
        d={(s,0):0};q=deque([(s,0)])
        while q:
            u,p=q.popleft()
            for a,b,l in edges:
                for x,y in ((a,b),(b,a)):
                    if x==u:
                        st=(y,p^l)
                        if st not in d: d[st]=d[(u,p)]+1; q.append(st)
        if (s,1) in d: best=min(best,d[(s,1)])
    return best
tot={}
for b in range(1,9):
  for c0 in (0,):
    W=[]
    for w in range(1,272,2):
        if w%17 in (0,1,16): continue
        L=cover(w,b,33); U=cover(w,2*b,67)
        if len(L)!=2: continue
        W.append((w,sum(1<<j for j,_ in L),U))
    sols=[]
    def dfs(start,cov,Uc,S):
        if cov==65535:
            if all(v==2 for v in Uc): sols.append(list(S))
            return
        x=next(i for i in range(16) if not cov>>i&1)
        for k,(w,m,U) in enumerate(W):
            if m>>x&1 and not m&cov:
                U2=list(Uc)
                for j,_ in U: U2[j]+=1
                if max(U2)>2: continue
                S.append(k); dfs(0,cov|m,U2,S); S.pop()
    dfs(0,0,[0]*16,[])
    for S in sols:
        ws=[W[k][0] for k in S]
        cls=frozenset(min(w%8,8-w%8) for w in ws); sig=('mixed' if len(cls)>1 else 'one')
        hit={}
        for i,k in enumerate(S):
            for j,a in W[k][2]: hit.setdefault(j,[]).append((i,a))
        # each residue = members t', N-t' ; both members get the same label (lift bits flip together)
        edges=[]
        for j,h in hit.items():
            (i1,a1),(i2,a2)=h
            if i1==i2: edges=None; break
            edges += [(i1,i2,a1^a2^1)]*2
        if edges is None: continue
        mult={}
        for a,c,l in edges: mult.setdefault(tuple(sorted((a,c))),[]).append(l)
        odddig=any(len(set(v))>1 for v in mult.values())
        ok=solvable(8,edges)
        if sig=='mixed': SOC[soc(edges)]=SOC.get(soc(edges),0)+1
        key=(sig,odddig,ok)
        tot[key]=tot.get(key,0)+1
        if False:
            m4=[p for p,v in mult.items() if len(v)==4]; m2=[(p,v[0]) for p,v in mult.items() if len(v)==2]
            # split m2 into components, check each is a 4-cycle with odd label sum
            adj={}
            for (a,c),l in m2: adj.setdefault(a,[]).append(c); adj.setdefault(c,[]).append(a)
            comps=[];seen=set()
            for s in adj:
                if s in seen: continue
                comp={s};st=[s]
                while st:
                    u=st.pop()
                    for v in adj[u]:
                        if v not in comp: comp.add(v); st.append(v)
                seen|=comp; comps.append(comp)
            cyc=[(len(c),sum(l for (a,d),l in m2 if a in c)%2) for c in comps]
            pm=len(m4)==4 and len({x for p in m4 for x in p})==8
            print('b',b,'c0',c0,'ws',sorted(ws),'m4 perfect matching:',pm,'#m2',len(m2),'m2 comps (size,labelsum):',cyc)
print('totals (sigma odd?, odd digon?, solvable?):',tot)

print('mixed shortest odd closed walk:',sorted(SOC.items()))
