# Puck probe of Argon's p>768 stability recipe: transport realized configs to new primes, test exact tiling + doublability
import sys; sys.path.insert(0,'../../f1prime/check')
from f1check import *
def is_tiling(p,b,W):
    M=members(p,b,5); N=32*p; M6=members(p,b,6); N6=64*p
    cnt=[0]*len(M); u=[0]*len(M6)
    for w in W:
        if w%p in (0,1,p-1): return False
        cv=[t for t in M if cov(t,w,N)]
        if len(cv)!=2: return False
        for t in cv: cnt[M.index(t)]+=1
        for e in (0,1):
            for i,t in enumerate(M6):
                if cov(t,w+e*N,N6): u[i]+=1
    return all(c==1 for c in cnt) and all(x==2 for x in u)
src=[('p29_typeA',29,1,[3,97,125,151,413,191,285,385]),('p29_typeB',29,1,[19,179,441,339,397,313,237,77]),('p89',89,36,[1345,545,1089,129,673,587,139,1035])]
for name,p0,b0,W0 in src:
    C0=coords(p0,b0,W0)
    for P in (769,773,787,1009,2003):
        bs=3 if b0%2 else 2
        Wn=[]
        for x in C0:
            m=x['m']%32; sg=1 if x['d']>0 else -1
            if m==0 and sg<0: m=32
            cand=[w for w in range(x['w']%32,16*P,32) if w>0 and w%2 and w%P not in (0,1,P-1) and 0<sg*(bs*w-m*P)<P/2]
            if not cand: Wn=None;break
            Wn.append(cand[0])
        if Wn is None: print(name,P,'no candidate'); continue
        Cn=coords(P,bs,Wn)
        same=[(a['m']%32,a['w']%32,a['d']>0)==(b['m']%32,b['w']%32,b['d']>0) for a,b in zip(C0,Cn)]
        print(name,'P',P,'b*',bs,'W',Wn,'red_same',all(same),'tiling',is_tiling(P,bs,Wn),'doublable',doublable(P,bs,Wn),flush=True)
