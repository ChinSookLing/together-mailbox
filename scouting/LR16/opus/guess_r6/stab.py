import re,glob,ast
def f(x,p): return min(x%p,p-x%p)
def cover(p,S):
    n=(p-1)//2; return all(any(16*f(v*t,p)<p for v in S) for t in range(1,n+1))
def stab(p,S):
    n=(p-1)//2; T=set(S); return [u for u in range(1,n+1) if {f(u*v,p) for v in S}==T]
# subgroup covers: order-28 subgroup (needs p = 1 mod 28)
for p in [29,113,197,281,421,449]:
    n=(p-1)//2; G=sorted({f(x,p) for x in range(1,p) if pow(x,28,p)==1})
    print('p',p,'subgroup28 size',len(G),'covers' if cover(p,G) else 'NOT cover')
# stabilizers of all known covers
files=sorted(glob.glob('out_*.txt'))
for fn in files:
    p=int(re.findall(r'\d+',fn)[0])
    if p in (353,): continue
    for line in open(fn):
        S=ast.literal_eval(line[line.index('('):])
        st=stab(p,S)
        if len(st)>1: print('p',p,'stabilizer',st,'S',S)
extra={409:[1,7,9,10,23,32,37,55,76,109,112,132,178,188],419:[1,8,9,13,14,29,38,86,115,124,143,147,150,151],421:[1,4,15,50,54,67,128,130,145,146,171,175,179,196],457:[1,2,55,60,68,111,112,113,114,115,116,117,169,221]}
for p,S in extra.items(): print(p,'stab',stab(p,S))
