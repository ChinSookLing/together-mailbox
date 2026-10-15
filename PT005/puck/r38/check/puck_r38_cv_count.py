# Puck independent (c,v) 2-cover count for R38 (own code, different method from Hesper).
# Footprints: c even 0..30, v odd, (c,v)~(c,32-v) normalized v<=15; U=c+{+-v,+-3v} mod 32, |U|=4.
# Enumeration: footprints sorted by lowest covered slot, multiplicity 0/1/2 each (canonical multisets), prune by counts.
# Lift bit k(s)=(s-c-d*v)/32 for the d with c+d*v == s mod 32 (s in 1..31, c in 0..30, v in 1..15).
# Doublable test: GF(2) rank - labels lambda_e=1+k_i(s)+k_j(s) lie in the cut space of the 2-regular-on-s multigraph.
import sys, json
from collections import Counter
odds=list(range(1,32,2)); oidx={s:t for t,s in enumerate(odds)}
fps=[]
for c in range(0,32,2):
    for v in range(1,16,2):
        U=frozenset((c+d*v)%32 for d in (1,-1,3,-3))
        if len(U)==4: fps.append((c,v))
def Ub(c,v):
    m=0
    for d in (1,-1,3,-3): m|=1<<oidx[(c+d*v)%32]
    return m
def kmap(c,v):
    return {(c+d*v)%32:((c+d*v)%32-c-d*v)//32 for d in (1,-1,3,-3)}
fps.sort(key=lambda f:(min(oidx[(f[0]+d*f[1])%32] for d in (1,-1,3,-3)),f))
lows=[min(oidx[(f[0]+d*f[1])%32] for d in (1,-1,3,-3)) for f in fps]
masks=[Ub(*f) for f in fps]; K=[kmap(*f) for f in fps]
n=len(fps)
# suffix coverage capacity for pruning: remaining footprints touching s
res=[]
cnt=[0]*16
def rec(i,chosen):
    k=len(chosen)
    if k==8:
        if all(x==2 for x in cnt): res.append(tuple(chosen))
        return
    if i==n: return
    # lowest uncovered-enough slot must be hit by footprint >= i; if footprint i can't touch lowest deficient slot and
    # no later can, prune (cheap check: lowest deficient slot t)
    t=next(t for t in range(16) if cnt[t]<2)
    # footprints sorted by lowest slot: once lows[i]>t, slot t can never be filled (all lower slots are full)
    if lows[i]>t: return
    m=masks[i]
    # multiplicity 2,1,0
    for mult in (2,1):
        ok=True
        for tt in range(16):
            if m>>tt&1 and cnt[tt]+mult>2: ok=False;break
        if ok and k+mult<=8:
            for tt in range(16):
                if m>>tt&1: cnt[tt]+=mult
            rec(i+1,chosen+[i]*mult)
            for tt in range(16):
                if m>>tt&1: cnt[tt]-=mult
    # skip i only allowed if slot t still coverable later -- handled at next level
    if not (m>>t&1) or True: rec(i+1,chosen)
rec(0,[])
def doublable(conf):
    # build edge list
    occ={}
    for a,f in enumerate(conf):
        for s,kv in kmap(*f).items(): occ.setdefault(s,[]).append((a,kv))
    rows=[]
    for s,((a,ka),(b,kb)) in occ.items():
        lam=(1+ka+kb)&1
        rows.append(((1<<a)|(1<<b), lam))
    # Gaussian elimination: is system x_a+x_b=lam consistent over GF(2)?
    piv={}
    for vec,l in rows:
        while vec:
            h=vec.bit_length()-1
            if h in piv: pv,pl=piv[h]; vec^=pv; l^=pl
            else: piv[h]=(vec,l); break
        if vec==0 and l: return False
    return True
confs=[tuple(fps[i] for i in r) for r in res]
D=[c for c in confs if doublable(c)]
mx=lambda r: len({v%8 in (1,7) for c,v in r})>1
print('footprints',n)
print('exact 2-covers',len(confs),'doublable',len(D))
print('mixed',sum(map(mx,confs)),'mixed doublable',sum(map(mx,D)))
H=json.load(open(sys.argv[1]))
hd={tuple(sorted(map(tuple,x))) for x in H}
pd={tuple(sorted(x)) for x in D}
print('Hesper doublable set == Puck set:',hd==pd, len(hd), len(pd))
# degree pattern of mixed doublable (simple graph distinct neighbours)
from collections import Counter as C
pat=C()
for r in D:
    if not mx(r): continue
    occ={}
    for a,(c,v) in enumerate(r):
        for s in kmap(c,v): occ.setdefault(s,[]).append(a)
    nb={a:set() for a in range(8)}
    for s,(a,b) in occ.items(): nb[a].add(b); nb[b].add(a)
    pat[tuple(sorted(len(nb[a]) for a in range(8)))]+=1
for k,v in sorted(pat.items(),key=lambda x:-x[1]): print(k,v)
