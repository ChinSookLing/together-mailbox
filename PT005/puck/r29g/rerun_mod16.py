import sys; sys.path.insert(0,'/workspace/mbx_pt5/PT005/puck/verify')
from common import *
from collections import Counter, defaultdict, deque
def onecls(ws):
    m8={w%8 for w in ws}
    for c in (1,3):
        if m8<={c,8-c}: return c
    return None
tot=Counter(); mixed=[]
for b in range(1,9):
    n5,n6=N(5),N(6); c5=C(5,b); c6=C(6,(2*b)%P)
    cls=defaultdict(list)
    for w in legal(5):
        s=frozenset(t for t in c5 if covers(t,w,n5))
        A=tuple(frozenset(t for t in c6 if covers(t,(w+e*n5)%n6,n6)) for e in (0,1))
        if s: cls[(s,A)].append(w)
    bym=defaultdict(list)
    for key in cls: bym[min(key[0])].append(key)
    cands=[]
    def rec(rem,acc,hits):
        if not rem:
            if all(hits[t]==2 for t in c6): cands.append(list(acc))
            return
        for key in bym[min(rem)]:
            s,A=key
            if not s<=rem or (A[0]&A[1]): continue
            h=hits.copy(); ok=True
            for t in A[0]|A[1]:
                h[t]+=1
                if h[t]>2: ok=False;break
            if ok: acc.append(key); rec(rem-s,acc,h); acc.pop()
    rec(frozenset(c5),[],Counter())
    for cand in cands:
        ws=[cls[k][0] for k in cand]; c=onecls(ws)
        hitby=defaultdict(list)
        for i,(s,A) in enumerate(cand):
            for e in (0,1):
                for t in A[e]: hitby[t].append((i,e))
        edges=[(h[0][0],h[1][0],h[0][1]^h[1][1]^1) for h in hitby.values()]
        adj=defaultdict(list)
        for k,(i,j,l) in enumerate(edges): adj[i].append((j,l,k)); adj[j].append((i,l,k))
        # shortest odd cycle via BFS on (node,parity) from each start
        best=None
        for s0 in range(8):
            dist={(s0,0,-1):0}; q=deque([(s0,0,-1)])
            while q:
                x,p,le=q.popleft(); d=dist[(x,p,le)]
                if best is not None and d>=best: break
                for y,l,k in adj[x]:
                    if k==le: continue
                    st=(y,p^l,k)
                    if y==s0 and p^l==1:
                        best=d+1 if best is None else min(best,d+1)
                    if st not in dist: dist[st]=d+1; q.append(st)
        key=('single' if c is not None else 'mixed', b)
        tot[(key, 'solvable' if best is None else 'unsolvable')]+=1
        if c is None: mixed.append((b,ws,best,{w%8 for w in ws}))
for k,v in sorted(tot.items()): print(k,v)
L=Counter(m[2] for m in mixed); print('mixed shortest odd cycle lengths',dict(L))
print('mixed total',len(mixed),'mod8 sets',Counter(tuple(sorted(m[3])) for m in mixed))
print('by b x shortest', sorted(Counter((m[0],m[2]) for m in mixed).items()))
T=Counter((m[2], len({w%16 for w in m[1]})==8 and all(w%2 for w in m[1])) for m in mixed)
print('m16 table',sorted(T.items()))
