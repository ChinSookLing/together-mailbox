import sys
from collections import defaultdict, Counter
from lem import check, hit
P=int(sys.argv[1])
def onecls(ws):
    m8={w%8 for w in ws}
    return any(m8<= {c,8-c} for c in (1,3))
res=Counter(); bad=[]
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
        if onecls(ws): res['single']+=1; continue
        r=check(P,b,ws)
        key=('mixed','ham8' if r.get('ham8') else 'nonham','alt' if r.get('alternating') else 'nonalt')
        res[key]+=1
        if r.get('ham8'):
            if not r['consistent']: res['ham8_oddDigon']+=1
            else:
                allok=all(r[x] for x in ('L1','L2','L3','L4','sumK_odd')) and r['H']==1 and r['prod_sigma']==1
                res['ham8_consistent_allok' if allok else 'ham8_consistent_FAIL']+=1
                if not allok: bad.append((b,ws,r))
            if not (r['L1'] and r['L2'] and r['L3']): bad.append((b,ws,r))
        else:
            # record graph shape: vertex degrees in simple graph
            res[('nonham_L1',r['L1'],r.get('exact2cover'))]+=1
            bad.append(('nonham',b,ws))
print("P",P,dict(res)); print("bad/nonham",bad[:6])
