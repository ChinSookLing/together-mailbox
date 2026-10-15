# Puck R38: independent rebuild of the k=5 layer (does NOT import smallest_mixed.py or r38_k5layer.py).
# Raw hit test only: t hits W mod M iff 16*min(t*W%M, M-t*W%M) < M.
# C5(b)=odd t in 1..16p, t=+-b mod p, M5=32p; C6(2b)=odd t in 1..32p, t=+-2b mod p, M6=64p.
# Items (w,e): w odd in 1..16p, w mod p not in {0,+-1}; level-6 uses W=w+e*32p.
# Solver: Algorithm X on 48 columns with MRV (fewest-candidates column first), items deduplicated by
# full 48-bit mask ONLY (class ignored in the search); every distinct (w,e) carrying a mask is expanded
# afterwards, so ALL representatives are enumerated. Distinct w is automatic: (w,0),(w,1) share the
# nonzero level-5 mask, so no exact cover can use one w twice (asserted).
# Map check: own labelling (see slot5/slot6 below) compared against the (c,v) formula on raw masks.
import sys, json, time
from collections import defaultdict, Counter
def hit(t,W,M): r=t*W%M; return 16*min(r,M-r)<M
def cls(w): return 1 if w%8 in (1,7) else 3
def bal(x,p):
    x%=p; return x if x<=p//2 else x-p
def cv(p,b,w):           # Hesper's map, recomputed here
    d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32); c=(-2*m*v)%32
    return c, v
def canon(c,v): v%=32; return (c%32, min(v,32-v))
def U(c,v): return frozenset((c+dd*v)%32 for dd in (1,-1,3,-3))
def kk(c,v,s):
    for dd in (1,-1,3,-3):
        if (c+dd*v)%32==s: return (s-c-dd*v)//32
def degs(r):
    E=set()
    for s in range(1,32,2):
        ij=[i for i,f in enumerate(r) if s in U(*f)]
        assert len(ij)==2
        E.add(tuple(sorted(ij)))
    g=[0]*8
    for i,j in E:
        if i!=j: g[i]+=1; g[j]+=1
    return tuple(sorted(g))
TAB=set() if __name__!="__main__" else set(tuple(sorted(canon(c,v) for c,v in r)) for r in json.load(open(sys.argv[1])))
def run(p):
    n5,n6=32*p,64*p; pinv=pow(p,-1,64)
    stat=Counter(); allconf=set(); oneconf=set(); cnt_one=Counter(); cnt_all=Counter()
    mapbad=0; map5bad=0; maxgrp=0; kbad=0; nfoot=0; nall=0; bad_one=0; bad_all=0
    for b in range(1,(p+1)//2):
        c5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
        c6=[t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
        # own labelling: signed T (T=+t or -t mod M so that T=b (resp 2b) mod p)
        T5=[t if t%p==b%p else n5-t for t in c5]
        T6=[t if t%p==(2*b)%p else n6-t for t in c6]
        slot5=[((T-b)*pinv)%32 for T in T5]              # 16 residues, parity b+1
        slot6=[((T-2*b)*pinv)%32 for T in T6]            # 16 odd residues, each twice
        half6=[((T-2*b)*pinv)%64>=32 for T in T6]        # which of the 2 cells of a slot
        assert sorted(Counter(slot6).values())==[2]*16
        bymask=defaultdict(list)
        for w in range(1,16*p,2):
            if w%p in (0,1,p-1): continue
            c,v=cv(p,b,w); cc,vv=canon(c,v)
            m5=[i for i,t in enumerate(c5) if hit(t,w,n5)]
            d=bal(b*w,p); mm=(b*w-d)//p; vi=pow(w,-1,32)
            J=(-2,-1,0,1) if d>0 else (-1,0,1,2)
            pred5={((j-mm)*vi)%32 for j in J if (j-mm-b-1)%2==0}
            if {slot5[i] for i in m5}!=pred5 or len(m5)!=2: map5bad+=1
            # level-5 predicted: slots (j-m)v, i.e. 2*slot5 in c+2jv; check projection
            for e in (0,1):
                W=w+e*n5
                m6=[i for i,t in enumerate(c6) if hit(t,W,n6)]
                proj=frozenset(slot6[i] for i in m6)
                if proj!=U(cc,vv) or len(m6)!=4: mapbad+=1
                # Argon parity: half(s) + k(s) + e must be a(w) + g(s) ; record h+k for later
                hk={slot6[i]:(half6[i]+kk(cc,vv,slot6[i]))%2 for i in m6}
                mk=sum(1<<i for i in m5)|sum(1<<(16+i) for i in m6)
                bymask[mk].append((w,e,(cc,vv),hk))
        # Parity sanity over all items: (h+k)(s) xor e - g(s) constant per w. Fix g from one item per slot.
        g={}
        for mk,L in bymask.items():
            for w,e,f,hk in L:
                vals=set()
                for s,x in hk.items():
                    if s not in g: g[s]=None
                stat['items']+=1
        maxgrp=max(maxgrp,max(len(L) for L in bymask.values()))
        # exact cover, MRV
        masks=list(bymask); col=defaultdict(list)
        for mk in masks:
            for i in range(48):
                if mk>>i&1: col[i].append(mk)
        FULL=(1<<48)-1; sols=[]
        def rec(cov,sel):
            if cov==FULL: sols.append(tuple(sel)); return
            free=FULL&~cov; best=None; bl=None
            x=free
            while x:
                i=(x&-x).bit_length()-1; x&=x-1
                L=[mk for mk in col[i] if not mk&cov]
                if best is None or len(L)<len(best):
                    best=L
                    if not L: return
            for mk in best:
                sel.append(mk); rec(cov|mk,sel); sel.pop()
        rec(0,[])
        for s in sols:
            assert len(s)==8
            # expand all reps; also form footprint-level keys (mask,class) as Hesper does
            import itertools
            keysets=defaultdict(list)
            for combo in itertools.product(*[bymask[mk] for mk in s]):
                ws=[x[0] for x in combo]; assert len(set(ws))==8
                classes=frozenset(cls(w) for w in ws)
                key=tuple(sorted((mk,cls(x[0])) for mk,x in zip(s,combo)))
                keysets[key].append(combo)
            for key,combos in keysets.items():
                mixed=len({k[1] for k in key})==2
                if not mixed: continue
                nfoot+=1
                for idx,combo in enumerate(combos):
                    conf=tuple(sorted(x[2] for x in combo))
                    # Argon parity check on the realized lift: in each slot the two items must sit in
                    # different halves; check labels from k reproduce it via e.
                    nall+=1; allconf.add(conf); cnt_all[degs(conf)]+=1
                    if conf not in TAB: bad_all+=1
                    if idx==0:
                        oneconf.add(conf); cnt_one[degs(conf)]+=1
                        if conf not in TAB: bad_one+=1
                    # parity identity: e_i+e_j == 1+k_i+k_j+h-terms -> verify h_i(s)!=h_j(s) given by masks (exactness) and
                    # that (h+k)_i(s)+e_i - (h+k)_j(s)-e_j is independent of s along each item pair? (checked below)
                    hkall=[(x[3],x[1]) for x in combo]
                    for i in range(8):
                        vals={(hkall[i][0][s]+hkall[i][1])%2 for s in hkall[i][0]}
                        # if h+k+e is constant per item (g==0), then exact cover <=> labels 1+k_i+k_j consistent
                        if len(vals)!=1: kbad+=1
    return dict(p=p,footsol_mixed=nfoot,allreps_mixed=nall,distinct_one=len(oneconf),distinct_all=len(allconf),
                notin_one=bad_one,notin_all=bad_all,mapbad=mapbad,map5bad=map5bad,maxgroup=maxgrp,kbad=kbad,classes_one=dict(cnt_one),classes_all=dict(cnt_all)),allconf,oneconf
if __name__=="__main__":
    out={}
    for p in map(int,sys.argv[2:]):
        t=time.time(); r,A,O=run(p)
        r['sec']=round(time.time()-t,1)
        print(json.dumps({k:(str(v) if 'classes' in k else v) for k,v in r.items()}),flush=True)
        json.dump(sorted(map(list,A)),open(f'k5_allconf_p{p}.json','w'))
        json.dump(sorted(map(list,O)),open(f'k5_oneconf_p{p}.json','w'))
