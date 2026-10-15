import sys
from lem import bal
from direct import test
def primerange(a,b):
    return [n for n in range(a,b) if n>1 and all(n%k for k in range(2,int(n**.5)+1))]
EX=[(0, [(1, 0, 1), (1, 27, 1), (11, 9, 1), (1, 22, 1), (1, 18, 1), (11, 13, 1), (1, 12, 1), (1, 7, 1)]),
(0, [(1, 0, 1), (1, 28, 1), (1, 24, 1), (1, 20, 1), (1, 16, 1), (3, 13, 1), (3, 24, 1), (3, 3, -1)])]
for beta,tys in EX:
    hit=None
    for p in primerange(17,400):
        for b in range(1,p):
            if b%2!=beta: continue
            av={}
            for w in range(1,16*p,2):
                if w%p in (0,1,p-1): continue
                d=bal(b*w,p); m=(b*w-d)//p
                av.setdefault((pow(w,-1,32),m%32,1 if d>0 else -1),w)
            if all(t in av for t in tys):
                W=[av[t] for t in tys]; hit=(p,b,W,test(p,b,W)); break
        if hit: break
    print(beta,tys,'->',hit,flush=True)
