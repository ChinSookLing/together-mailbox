# Chair check of Qwen's Γ proposal (Cay(Z_N, S), N=(p-1)/2, S = dlog of 1..H): orbit sizes, spectrum, per-core T(C)
import json, cmath, math
def prim(p):
    fs=[q for q in range(2,p) if (p-1)%q==0 and all(q%r for r in range(2,q))]
    return next(g for g in range(2,p) if all(pow(g,(p-1)//q,p)!=1 for q in fs))
def gamma(p,n):
    g=prim(p); N=(p-1)//2; H=max(r for r in range(1,p) if n*r<p)   # r with n*r<p, i.e. ||r/p|| < 1/n
    lg={pow(g,k,p):k%N for k in range(p-1)}
    S=sorted({lg[r] for r in range(1,H+1)})
    lam=[abs(sum(cmath.exp(2j*math.pi*k*s/N) for s in S)) for k in range(1,N)]
    return g,N,H,S,lg,max(lam)
for p,n in ((223,16),(233,16),(191,16),(401,16),(239,17),(271,17)):
    g,N,H,S,lg,mx=gamma(p,n)
    print(f"p={p} n={n} g={g} N={N} |S|={len(S)} max|lambda|={mx:.3f} ratio={mx/len(S):.3f}")
# orbits of the 65 cores under translation in Z_111
g,N,H,S,lg,_=gamma(223,16)
cs=[json.loads(l)["core"] for l in open("/home/claude/lr16/core223/cores.jsonl")]
tot=0; sizes=set()
for C in cs:
    X=frozenset(lg[c] for c in C)
    orb={frozenset((x+t)%N for x in X) for t in range(N)}
    tot+=len(orb); sizes.add(len(orb))
print("223: dominating 13-sets = sum of orbit sizes =",tot,"orbit sizes",sizes)
for p,f in ((223,"/home/claude/lr16/core223/cores.jsonl"),(233,"/home/claude/lr16/core233/cores.jsonl")):
    v=sorted({json.loads(l)["l16_lifts"]//64 for l in open(f)}); print(p,"T(C) values:",v)
