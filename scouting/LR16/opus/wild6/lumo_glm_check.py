# Chair check: GLM T1/T5 + Lumo steps 1-2 (combined, as Tuzi asked 15:00). p = 223.
import json, cmath, collections
p=223; n=111
def is_prim(g): return all(pow(g,(p-1)//q,p)!=1 for q in (2,3,37))
print("g=3 primitive root:", is_prim(3))
lg={pow(3,k,p):k for k in range(p-1)}
ball=[r for r in range(1,p) if 16*min(r,p-r)<p]
S=sorted(lg[r] for r in ball)                         # shape in Z/222
Dbar=sorted({x%111 for x in S})
print("|ball|",len(ball),"S in Z/222:",S)
print("Dbar_223 (mod 111):",Dbar, " GLM's:", Dbar==[0,1,2,27,28,36,47,69,70,89,96,99,107])
Sset=set(S)
for order in (2,3,6,37,74,111):
    step=222//order
    print(f"S periodic under subgroup of order {order}:", all((x+step)%222 in Sset for x in S))
# character spectrum of Dbar on Z/111
mx=0; co=[]
for k in range(1,111):
    c=abs(sum(cmath.exp(2j*cmath.pi*k*x/111) for x in Dbar)); co.append((round(c,4),k))
co.sort(reverse=True); print("largest |chi_k(Dbar)|:",co[:4]," (0.4*13 =",0.4*13,")")
print("order-3 characters k=37,74:",[c for c in co if c[1] in (37,74)])
# fold the 65 cores mod 111 and check cover; histograms
cs=[json.loads(l)["core"] for l in open("/home/claude/lr16/core223/cores.jsonl")]
ok=0; H=collections.Counter()
for C in cs:
    m=collections.Counter()
    for s in C:
        for d in Dbar: m[(d-lg[s])%111]+=1   # speed s covers t iff s*t in ball: log t = d - log s
    if len(m)==111: ok+=1
    H[tuple(sorted(collections.Counter(m.values()).items()))]+=1
print("cores covering Z_111 after fold:",ok,"of",len(cs))
print("distinct multiplicity histograms (Z_111):",len(H)); [print("  ",h,c) for h,c in H.items()]
