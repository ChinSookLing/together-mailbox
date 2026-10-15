# Puck R38/R39 prep: realized k=5 mixed-doublable configs at one prime P>768, b in {2,3} only.
# Logic: Argon stability recipe (PROVED, side condition automatic, see mu_check.py) transports any realized
# config at any prime to P with b*=3 (b odd) or b*=2 (b even). Hence U (union over all primes) = realized(P,b in{2,3}).
# Same raw hit test and solver as puck_r38_k5layer.py; masks deduped; per mask keep the set of labels
# (canon(c,v), class) instead of expanding every w, so configs are enumerated exactly at footprint level.
import sys, json, itertools, time
from collections import defaultdict, Counter
sys.argv=[sys.argv[0]]
from puck_r38_k5layer import hit, cls, bal, cv, canon, U, degs
def run(p,bs):
    n5,n6=32*p,64*p; conf=set(); nsol=0; nmix=0
    for b in bs:
        c5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
        c6=[t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
        lab=defaultdict(set)
        for w in range(1,16*p,2):
            if w%p in (0,1,p-1): continue
            c,v=cv(p,b,w); f=canon(c,v)
            m5=[i for i,t in enumerate(c5) if hit(t,w,n5)]
            assert len(m5)==2
            for e in (0,1):
                m6=[i for i,t in enumerate(c6) if hit(t,w+e*n5,n6)]
                assert len(m6)==4
                mk=sum(1<<i for i in m5)|sum(1<<(16+i) for i in m6)
                lab[mk].add((f,cls(w)))
        masks=list(lab); col=defaultdict(list)
        for mk in masks:
            for i in range(48):
                if mk>>i&1: col[i].append(mk)
        FULL=(1<<48)-1; sols=[]
        def rec(cov,sel):
            if cov==FULL: sols.append(tuple(sel)); return
            free=FULL&~cov; best=None; x=free
            while x:
                i=(x&-x).bit_length()-1; x&=x-1
                L=[mk for mk in col[i] if not mk&cov]
                if best is None or len(L)<len(best):
                    best=L
                    if not L: return
            for mk in best:
                sel.append(mk); rec(cov|mk,sel); sel.pop()
        rec(0,[])
        print('P',p,'b',b,'masks',len(masks),'cover sols',len(sols),'max labels/mask',max(len(s) for s in lab.values()),flush=True)
        for s in sols:
            nsol+=1
            for combo in itertools.product(*[sorted(lab[mk]) for mk in s]):
                if len({x[1] for x in combo})<2: continue
                nmix+=1; conf.add(tuple(sorted(x[0] for x in combo)))
    return conf,nsol,nmix
if __name__=="__main__":
    ref=set(tuple(map(tuple,c)) for c in json.load(open('k5_sets.json'))['61']['all'])
    for P in (769,773):
        t=time.time(); A,ns,nm=run(P,(2,3))
        cl=Counter(degs(c) for c in A)
        print(json.dumps(dict(P=P,cover_sols=ns,mixed_label_combos=nm,distinct=len(A),equal_to_p61_set=A==ref,
              new_vs_p61=len(A-ref),missing_vs_p61=len(ref-A),classes=str(dict(cl)),sec=round(time.time()-t,1))),flush=True)
