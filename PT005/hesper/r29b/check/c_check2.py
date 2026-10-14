# Hesper independent check of Astra R29b (C), memoized over covered sets
from functools import lru_cache
from collections import Counter
ODD=list(range(1,32,2)); idx={x:i for i,x in enumerate(ODD)}
out={}
for c0 in (1,3):
    opts={}
    for w in ODD:
        if w%8 not in (c0,8-c0): continue
        iw=pow(w,-1,32); fl=1 if w%16 in (c0,16-c0) else 0
        for c in range(-15,16,2):
            s=1 if c>0 else -1
            a,b=(iw*c)%32,(iw*(c-2*s))%32
            if a==b: continue
            m=(1<<idx[a])|(1<<idx[b])
            opts.setdefault(m,set()).add((fl,abs(c)))
    @lru_cache(None)
    def f(cov):
        if cov==(1<<16)-1: return frozenset([(0,frozenset())])
        x=next(i for i in range(16) if not cov>>i&1)
        r=set()
        for m,os in opts.items():
            if m>>x&1 and not m&cov:
                for par,S in f(cov|m):
                    for fl,ac in os: r.add((par^fl,S|{ac}))
        return frozenset(r)
    out[c0]=f(0)
for c0,R in out.items():
    odd=[sorted(S) for p,S in R if p==1]; even=[sorted(S) for p,S in R if p==0]
    print('c0',c0,'#absets sigma-odd',len(odd),'sigma-even',len(even))
    if odd:
        common=set(range(1,16,2))
        for S in odd: common&=set(S)
        never=set(range(1,16,2))
        for S in odd: never-=set(S)
        print('  |c| in EVERY odd solution:',sorted(common),' |c| in NO odd solution:',sorted(never))
        print('  sample odd absets:',odd[:5])
forb={b:sorted({abs(c) for c in range(-15,16,2) if c%17 in (b%17,(-b)%17)}) for b in range(1,9)}
print('forbidden |c| by b:',forb)
for b,F in forb.items():
    ok=any(p==1 and not (S&set(F)) for c0 in out for p,S in out[c0])
    print('b',b,'sigma-odd one-class possible in mod-32 model:',ok)
# explicit witness for b=1 (avoid |c|=1), c0=3
c0=3
items=[]
for w in ODD:
    if w%8 not in (c0,8-c0): continue
    iw=pow(w,-1,32)
    for c in range(-15,16,2):
        if abs(c)==1: continue
        s=1 if c>0 else -1
        a,b=(iw*c)%32,(iw*(c-2*s))%32
        if a!=b: items.append((w,c,(1<<idx[a])|(1<<idx[b])))
def g(cov,acc):
    if cov==(1<<16)-1:
        sig=sum(1 for w,c,_ in acc if w%16 in (c0,16-c0))
        if sig%2: return acc
        return None
    x=next(i for i in range(16) if not cov>>i&1)
    for it in items:
        if it[2]>>x&1 and not it[2]&cov:
            r=g(cov|it[2],acc+[it])
            if r: return r
print('b=1 witness (w mod 32, c):',[(w,c) for w,c,_ in g(0,[])])
