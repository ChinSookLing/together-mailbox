import sys
from collections import defaultdict, Counter
from lem import hit
P=int(sys.argv[1])
res=Counter()
def onecls(ws):
    m8={w%8 for w in ws}; return any(m8<= {c,8-c} for c in (1,3))
for b in range(1,(P+1)//2):
    n5,n6=32*P,64*P
    c5=[t for t in range(1,n5//2+1,2) if t%P in (b,P-b)]
    c6=[t for t in range(1,n5+1,2) if t%P in ((2*b)%P,(-2*b)%P)]
    cls={}
    for w in range(1,n5//2,2):
        if w%P in (0,1,P-1): continue
        s=frozenset(t for t in c5 if hit(t,w,n5))
        if not s: continue
        A=tuple(frozenset(t for t in c6 if hit(t,w+e*n5,n6)) for e in (0,1))
        cls.setdefault((s,A),w)
    bym=defaultdict(list)
    for k in cls: bym[min(k[0])].append(k)
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
        ws=[cls[k] for k in cand]
        mixed=not onecls(ws)
        hitby=defaultdict(list)
        for i,(s,A) in enumerate(cand):
            for e in (0,1):
                for t in A[e]: hitby[t].append((i,e))
        pairs=defaultdict(set)
        for t,h in hitby.items(): pairs[tuple(sorted((h[0][0],h[1][0])))].add(h[0][1]^h[1][1]^1)
        digon=any(len(L)==2 for L in pairs.values())
        # parity solvability
        par={}; ok=True; adj=defaultdict(list)
        for (i,j),L in pairs.items():
            for l in L: adj[i].append((j,l)); adj[j].append((i,l))
        ncomp=0
        for root in range(8):
          if root in par: continue
          ncomp+=1; par[root]=0; stack=[root]
          while stack:
            x=stack.pop()
            for y,l in adj[x]:
                if y not in par: par[y]=par[x]^l; stack.append(y)
                elif par[y]!=par[x]^l: ok=False
        conn=ncomp==1
        deg=tuple(sorted(len({j for j,_ in adj[i]}) for i in range(8)))
        res[('mixed' if mixed else 'single','solvable' if ok else 'obstructed', 'digon' if digon else 'nodigon', deg, 'conn' if conn else 'disc')]+=1
for k,v in sorted(res.items()): print(P,k,v)
