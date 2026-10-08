import re,sys
from sympy import factorint
HOLD={199,227,257,271,283}; FAR=[311,313,401]
g={}
for l in open("gamma.txt"):
    m=re.match(r"(\d+) GAMMA(=|>=)(\d+)",l); 
    if m: g[int(m[1])]=("≥" if m[2]==">=" else "")+m[3]
def fac(x): return " · ".join(f"{q}^{e}" if e>1 else str(q) for q,e in sorted(factorint(x).items()))
rows=["| p | p mod 16 | n=(p−1)/2 | H=⌊(p−1)/16⌋ | ⌈n/H⌉ | p−1 | γ(p) |","|---|---|---|---|---|---|---|"]
for p in sorted(x for x in g if x not in FAR):
    n=(p-1)//2;H=(p-1)//16
    rows.append(f"| {p} | {p%16} | {n} | {H} | {-(-n//H)} | {fac(p-1)} | {'**EXAM**' if p in HOLD else g[p]} |")
for p in FAR:
    n=(p-1)//2;H=(p-1)//16; rows.append(f"| {p} | {p%16} | {n} | {H} | {-(-n//H)} | {fac(p-1)} | **EXAM (far)** |")
print("\n".join(rows))
key=[f"{p} {g[p]}" for p in sorted(HOLD)]
open(sys.argv[1] if len(sys.argv)>1 else "/dev/null","w").write("\n".join(key)+"\n")
