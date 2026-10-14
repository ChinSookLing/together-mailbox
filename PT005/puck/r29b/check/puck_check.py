# Puck check of Astra R29b (C): low layer covers each odd residue mod 32 once, AND high layer (U) covers each exactly twice
from functools import lru_cache
ODD=list(range(1,32,2)); idx={x:i for i,x in enumerate(ODD)}
res={}
for c0 in (1,3):
    items=[]
    for w in ODD:
        if w%8 not in (c0,8-c0): continue
        A=pow(w,-1,32); fl=1 if w%16 in (c0,16-c0) else 0
        for c in range(-15,16,2):
            s=1 if c>0 else -1; e=2*c-17*s
            lo=[A*x%32 for x in (c,c-2*s)]
            if lo[0]==lo[1]: continue
            hi=[A*x%32 for x in ([e-4,e-2,e,e+2] if e>0 else [e-2,e,e+2,e+4])]
            m=(1<<idx[lo[0]])|(1<<idx[lo[1]])
            h=[0]*16
            for x in hi: h[idx[x]]+=1
            items.append((m,tuple(h),fl,abs(c)))
    @lru_cache(None)
    def f(cov,H):
        if cov==65535: return frozenset([(0,frozenset())]) if all(v==2 for v in H) else frozenset()
        x=next(i for i in range(16) if not cov>>i&1); r=set()
        for m,h,fl,ac in items:
            if m>>x&1 and not m&cov:
                H2=tuple(a+b for a,b in zip(H,h))
                if max(H2)>2: continue
                for p,S in f(cov|m,H2): r.add((p^fl,S|{ac}))
        return frozenset(r)
    res[c0]=f(0,(0,)*16)
    odd=[S for p,S in res[c0] if p]
    print('c0',c0,'odd absets',len(odd),'even',sum(1 for p,S in res[c0] if not p))
    if odd:
        com=set(range(1,16,2))
        for S in odd: com&=S
        nev=set(range(1,16,2))
        for S in odd: nev-=S
        print('  in every odd:',sorted(com),'in none:',sorted(nev))
for b in range(1,9):
    F={abs(c) for c in range(-15,16,2) if c%17 in (b,17-b)}
    print('b',b,'forbid',sorted(F),'odd possible:',any(p and not S&F for c0 in res for p,S in res[c0]))
