# Hesper R38 k=5 layer (empirical): for each prime, every exact k=5 tiling with a k=6 lift (Puck smallest_mixed.solve),
# mapped to its abstract footprint config (c_i,v_i); check membership in the 8,704 doublable table; degree class; first prime per class.
import sys,json,collections
sys.path.insert(0,'together-mailbox/PT005/puck/r36/checks')
from smallest_mixed import solve
D=set(tuple(sorted(tuple(x) for x in r)) for r in json.load(open('r38_doublable_only.json')))
def canon(c,v):
    v%=32; return (c%32, min(v,32-v)) 
Dc=set(tuple(sorted(canon(c,v) for c,v in r)) for r in D)
def U(c,v): return frozenset((c+d*v)%32 for d in (1,-1,3,-3))
def degs(r):
    E=set()
    for s in range(1,32,2):
        ij=[i for i,f in enumerate(r) if s in U(*f)]
        E.add(tuple(sorted(ij)))
    g=[0]*8
    for i,j in E:
        if i!=j: g[i]+=1;g[j]+=1
    return tuple(sorted(g))
def bal(x,p):
    x%=p; return x if x<=p//2 else x-p
first={}; out=[]
for p in map(int,sys.argv[1:]):
    seen=set(); bad=0; cnt=collections.Counter()
    for b in range(1,(p+1)//2):
        for mixed,r in solve(p,b):
            if not mixed: continue
            conf=[]
            for w,e in r:
                d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32); c=(-2*m*v)%32
                conf.append(canon(c,v))
            key=tuple(sorted(conf))
            if key not in Dc: bad+=1
            seen.add(key); dg=degs(key); cnt[dg]+=1
            first.setdefault(dg,p)
    print(f"p={p} mixed-doublings={sum(cnt.values())} distinct-configs={len(seen)} not-in-table={bad} classes={dict(cnt)}",flush=True)
print("first prime per degree class:",first)
