# Seed rows exactly as r43pre tree3.py pick(): random.Random(seed); w=sorted(15 x randrange(1,(p+1)//2));
# keep first rows improper at level p (>=2 odd, all t in 1..(p-1)/2 covered), distinct up to canon(+/-).
# Improper test done with precomputed bitmasks (identical predicate). At level p (odd) no even D, so improper == open.
import random, sys, json
def canon(w,M): return tuple(sorted(min(x%M,(-x)%M) for x in w))
def pick(p,seed,n):
    h=p//2
    mask=[0]*(p)
    for x in range(1,p):
        m=0
        for t in range(1,h+1):
            r=(t*x)%p
            if 16*min(r,p-r)<p: m|=1<<t
        mask[x]=m
    full=sum(1<<t for t in range(1,h+1))
    rnd=random.Random(seed); out=[]; cs=[]; tries=[]; t=0
    rr=rnd.randrange; top=(p+1)//2
    while len(out)<n:
        t+=1
        w=sorted(rr(1,top) for _ in range(15))
        m=0
        for x in w: m|=mask[x]
        if m==full and sum(x%2 for x in w)>=2:
            c=canon(w,p)
            if c not in cs: out.append(w); cs.append(c); tries.append(t)
    return out,tries
if __name__=='__main__':
    n=int(sys.argv[1]); ps=[int(a) for a in sys.argv[2:]]
    res=json.load(open('picks.json')) if len(sys.argv)>2 and __import__('os').path.exists('picks.json') else {}
    for p in ps:
        rows,tries=pick(p,20261016,n)
        res[str(p)]={'seed':20261016,'rows':rows,'tries':tries}
        print(p,tries,flush=True)
    json.dump(res,open('picks.json','w'))
