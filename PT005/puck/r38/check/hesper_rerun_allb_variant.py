# Hesper independent rerun v2: for each mixed doublable abstract config (own table), test realizability at (p,b):
# exists distinct w_i with canon(c_i,v_i) as given whose raw level-5 masks on C5(b) partition the 16 cells.
import sys,json
from collections import defaultdict
mixed=lambda k: not (all(v%8 in (1,7) for c,v in k) or all(v%8 in (3,5) for c,v in k))
def canon(c,v): v%=32; return (c%32,min(v,32-v))
D=set(tuple(sorted(canon(c,v) for c,v in r)) for r in json.load(open('r38_doublable_only.json')))
MD=[k for k in D if mixed(k)]
def bal(x,p): x%=p; return x if x<=p//2 else x-p
def hit(t,w,M): r=t*w%M; return 16*min(r,M-r)<M
def realized(p,b):
    M=32*p; c5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]; assert len(c5)==16
    G=defaultdict(set)
    for w in range(1,16*p,2):
        if w%p in (0,1,p-1): continue
        m=sum(1<<i for i,t in enumerate(c5) if hit(t,w,M))
        if not m: continue
        d=bal(b*w,p); mm=(b*w-d)//p; v=pow(w,-1,32); c=(-2*mm*v)%32
        G[canon(c,v)].add(m)
    FULL=(1<<16)-1; out=set()
    for k in MD:
        opts=[sorted(G.get(cv,())) for cv in k]
        if any(not o for o in opts): continue
        order=sorted(range(8),key=lambda i:len(opts[i]))
        def rec(j,cov):
            if j==8: return cov==FULL
            for m in opts[order[j]]:
                if not m&cov and rec(j+1,cov|m): return True
            return False
        if rec(0,0): out.add(k)
    return out
for p in map(int,sys.argv[1:]):
    U=set()
    for b in (range(1,(P:=p)//2+1) if p<100 else (2,3)):
        r=realized(p,b); U|=r; pass
    print(p,"UNION",len(U),flush=True); json.dump(sorted(U),open(f'hesper_U_{p}.json','w'))
