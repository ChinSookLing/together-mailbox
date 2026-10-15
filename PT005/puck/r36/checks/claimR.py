# Puck check of Hesper's Claim R (a45c953): every cycle parity of the XOR graph is
# determined by (w mod 64, c, positions) alone, i.e. p-independent.
# Test: labels predicted from reduced data (m16 = m mod 16 from 2m == -c w mod 32, w64 = w mod 64,
# s in [0,32)) must differ from the actual labels by a vertex gauge (=> same parity on every cycle).
import sys
from collections import defaultdict, Counter
from lem import hit, bal
P=int(sys.argv[1]); res=Counter(); bad=[]
def onecls(ws):
    m8={w%8 for w in ws}; return any(m8<= {c,8-c} for c in (1,3))
def b32(x): return ((x+16)%32)-16
for b in range(1,(P+1)//2):
    n5,n6=32*P,64*P
    c5=[t for t in range(1,n5//2+1,2) if t%P in (b,P-b)]
    c6=[t for t in range(1,n5+1,2) if t%P in ((2*b)%P,(-2*b)%P)]
    mem={}
    for t in c6:
        for eps in (1,-1):
            if (t-eps*2*b)%P==0: mem[t]=(eps*((t-eps*2*b)//P))%32; break
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
        ws=[cls[k] for k in cand]; mixed=not onecls(ws)
        red=[]
        for w in ws:
            d=bal(b*w,P); m=(b*w-d)//P; v=pow(w,-1,32); c=(-2*m*v)%32
            m16=((-c*w)//2)%16 if True else None
            assert (2*m16+c*w)%32==0 and m16==m%16
            red.append((m16,w%64))
        def zred(i,s):
            m16,w64=red[i]; q=2*m16+s*w64; r=b32(q); assert abs(r)<=3; return ((q-r)//32)%2
        hitby=defaultdict(list)
        for i,(s,A) in enumerate(cand):
            for e in (0,1):
                for t in A[e]: hitby[t].append((i,e))
        adj=defaultdict(list); pairs=defaultdict(int)
        for t,h in hitby.items():
            (i,ei),(j,ej)=h; lam_act=1^ei^ej; s=mem[t]
            lam_pred=1^zred(i,s)^zred(j,s)
            diff=lam_act^lam_pred
            adj[i].append((j,diff)); adj[j].append((i,diff)); pairs[tuple(sorted((i,j)))]+=1
        g={}; ok=True
        for root in range(8):
            if root in g: continue
            g[root]=0; st=[root]
            while st:
                x=st.pop()
                for y,l in adj[x]:
                    if y not in g: g[y]=g[x]^l; st.append(y)
                    elif g[y]!=g[x]^l: ok=False
        deg=[len({j for j,_ in adj[i]}) for i in range(8)]
        ham=len(pairs)==8 and all(d==2 for d in deg)
        cat=('mixed' if mixed else 'single')+('-ham8' if ham else '-nonham')
        res[(cat,'MATCH' if ok else 'FAIL')]+=1
        if not ok and len(bad)<3: bad.append((b,ws))
for k,v in sorted(res.items()): print(P,k,v)
print(P,'fail examples',bad)
