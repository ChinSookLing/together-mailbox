# Puck independent check of Argon R38 concrete claims (uses puck/f1prime/check/f1check.py)
import sys; sys.path.insert(0,'../../f1prime/check')
from f1check import *
import numpy as np
cases=[('p29_typeA',29,1,[3,97,125,151,413,191,285,385]),
       ('p29_typeB',29,1,[19,179,441,339,397,313,237,77]),
       ('p89',89,36,[1345,545,1089,129,673,587,139,1035])]
def is_tiling(p,b,W):
    M=members(p,b,5); N=32*p; M6=members(p,b,6); N6=64*p
    cnt=[0]*len(M); u=[0]*len(M6); pairs=[]
    for w in W:
        if w%p in (0,1,p-1): return False,None
        cv=[t for t in M if cov(t,w,N)]
        if len(cv)!=2: return False,None
        pairs.append(tuple(cv))
        for t in cv: cnt[M.index(t)]+=1
        for e in (0,1):
            for i,t in enumerate(M6):
                if cov(t,w+e*N,N6): u[i]+=1
    return all(c==1 for c in cnt) and all(x==2 for x in u), pairs
def signedL(C):
    # Argon F1'': L=4I-sum Q_r, L0=4I-sum|Q_r| ; labels from coboundary edges via raw convention
    E=edges(C); L=4*np.eye(8); L0=4*np.eye(8)
    for s,(i,j) in E:
        qi,qj=gpt_h(C[i],s,'raw'),gpt_h(C[j],s,'raw')
        lam=1^qi^qj; sg=(-1)**lam
        # each s is one edge; four colours r share; sum over all 16 edges /2 per colour-> use edge-level Laplacian
        L[i,j]-=sg; L[j,i]-=sg; L0[i,j]-=1; L0[j,i]-=1
    return L,L0
for name,p,b,W in cases:
    C=coords(p,b,W)
    inT,pairs = is_tiling(p,b,W)
    print(name,'exact_k5_tiling',inT,'mixed',not oneclass(W),'doublable(brute)',doublable(p,b,W),
          'F1prime(raw)',crit(C,'raw'),'degs',graphinfo(C),'pairs',pairs,flush=True)
    L,L0=signedL(C)
    k=lambda M: int(sum(abs(np.linalg.eigvalsh(M))<1e-9))
    print('   dimker L',k(L),'dimker L0',k(L0),'F1pp',k(L)==k(L0))
print('simple-graph degree sequences (distinct neighbours):')
for name,p,b,W in cases:
    C=coords(p,b,W); nb=[set() for _ in range(8)]
    for s,(i,j) in edges(C):
        if i!=j: nb[i].add(j); nb[j].add(i)
    print(name, tuple(sorted(len(x) for x in nb)), flush=True)
