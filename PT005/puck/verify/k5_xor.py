# Claims (2) F1 Kimi criterion and (3) F2 odd digons, k=5 -> 6, p=17, b=1..8.
# Coordinate = legal odd w mod 544 up to sign. Lift covers: A_e(w) = members of C_6(2b) covered by w+e*544 mod 1088.
# Class (interpretation): coords with identical (cover5 in C_5(b), A_0, A_1) are one class; tilings counted by class.
# Candidate = 8 classes tiling C_5(b) whose lifts 2-cover C_6(2b): every member hit exactly twice, by two different coords.
# XOR: member hit by (i,a),(j,c) => exactly one of [e_i=a],[e_j=c] holds => e_i^e_j = a^c^1 (edge label).
import sys
from collections import Counter, defaultdict
from common import *
def leg(a): a%=P; return 1 if pow(a,(P-1)//2,P)==1 else -1
def solve(edges):
    par={};
    adj=defaultdict(list)
    for i,j,l,t in edges: adj[i].append((j,l)); adj[j].append((i,l))
    val={}
    for s in range(8):
        if s in val: continue
        val[s]=0; st=[s]
        while st:
            x=st.pop()
            for y,l in adj[x]:
                if y not in val: val[y]=val[x]^l; st.append(y)
                elif val[y]!=val[x]^l: return False
    return True
def kimi(ws):
    m8={w%8 for w in ws}
    for c in (1,3):
        if m8<= {c,8-c}:
            sig=sum(1 for w in ws if w%16 in (c,16-c)); return sig%2==1
    return False
tot=0; rows=[]; dig=Counter(); allb=Counter(); mism=0; invar_bad=0
for b in range(1,9):
    n5,n6=N(5),N(6); c5=C(5,b); c6=C(6,(2*b)%P)
    cls=defaultdict(list)
    for w in legal(5):
        s=frozenset(t for t in c5 if covers(t,w,n5))
        A=tuple(frozenset(t for t in c6 if covers(t,(w+e*n5)%n6,n6)) for e in (0,1))
        if s: cls[(s,A)].append(w)
    for key,ws in cls.items():
        if len({kimi_key for kimi_key in [(tuple(sorted({w%8 for w in ws})))]})>1: pass
    bym=defaultdict(list)
    for key in cls: bym[min(key[0])].append(key)
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
    stat=Counter(); nsolv=0
    for cand in cands:
        hitby=defaultdict(list)
        for i,(s,A) in enumerate(cand):
            for e in (0,1):
                for t in A[e]: hitby[t].append((i,e))
        edges=[]
        for t,h in hitby.items():
            (i,a),(j,c)=h; edges.append((i,j,a^c^1,t))
        sol=solve(edges)
        # Kimi criterion evaluated on every representative choice -> must be class-invariant
        kv={kimi([cls[k][0] for k in cand])}
        for idx in range(8):
            for w in cls[cand[idx]][1:]:
                ws=[cls[k][0] for k in cand]; ws[idx]=w; kv.add(kimi(ws))
        if len(kv)>1: invar_bad+=1
        kv=kv.pop()
        if kv!=sol: mism+=1
        L=1
        for k_ in cand: L*=leg(cls[k_][0])
        lv={leg(w) for k_ in cand for w in [cls[k_][0]]}
        stat[(sol,L)]+=1; nsolv+=sol
        if (not sol) and L==-1:
            pairs=defaultdict(set)
            for i,j,l,t in edges: pairs[frozenset((i,j))].add(l)
            d=sum(1 for v in pairs.values() if len(v)==2)
            dig[d>0]+=1; allb[b]+=1
            rows.append((b,[cls[k_][0] for k_ in cand],d))
    tot+=len(cands)
    print(f"b={b} candidates={len(cands)} classes={len(cls)} (solvable,legendre_prod)->{dict(stat)} solvable={nsolv}")
print("TOTAL candidates",tot,"kimi mismatches",mism,"kimi non-class-invariant",invar_bad)
print("odd-Legendre dead:",sum(dig.values()),"by b",dict(allb),"with odd digon:",dig[True],"without:",dig[False])
print("odd-digon pairs per dead tiling:",dict(Counter(r[2] for r in rows)))
for r in rows[:5]: print("example",r)
