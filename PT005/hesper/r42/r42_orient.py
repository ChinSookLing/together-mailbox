import sys
src=open('together-mailbox/PT005/hesper/r39/checks_r16.py').read().split('for beta in (0,1):\n    S=')[0]
__file__='/workspace/work/together-mailbox/PT005/hesper/r39/checks_r16.py'; exec(src)
from collections import Counter,defaultdict
def data(k,beta):
    fixed=Counter(); edges=[]
    for c,v in k:
        h=(c//2)%16
        if h%2==beta: fixed[(h-v)%16]+=1; fixed[(h+v)%16]+=1
        else: fixed[h]+=1; edges.append(((h+2*v)%16,(h-2*v)%16))
    V=[r for r in range(16) if r%2!=beta]
    d={r:2-fixed[r] for r in V}
    return fixed,edges,d,V
def comps(V,edges):
    par={r:r for r in V}
    def f(x):
        while par[x]!=x: x=par[x]
        return x
    for a,b in edges: par[f(a)]=f(b)
    g=defaultdict(list)
    for r in V: g[f(r)].append(r)
    return list(g.values())
def count_cond(k,beta):
    fixed,edges,d,V=data(k,beta)
    if any(fixed[r]>0 and r%2==beta for r in fixed): return False  # parity sanity
    if min(d.values())<0: return False
    for C in comps(V,edges):
        e=sum(1 for a,b in edges if a in C)
        if e!=sum(d[r] for r in C): return False
    return True
stat=Counter(); mism=0
for k in MD:
    for beta in (0,1):
        a=r16(k,beta); b=count_cond(k,beta)
        mism+= a!=b
        fixed,edges,d,V=data(k,beta)
        stat[(a,len(edges),tuple(sorted(Counter(d.values()).items())))]+=1
print("R16 vs component-count condition mismatches:",mism)
for x,n in sorted(stat.items()): print(x,n)
print("---")
c=Counter()
for k in MD:
    row=[]
    for beta in (0,1):
        fixed,edges,d,V=data(k,beta); row+= [r16(k,beta), min(d.values())>=0, count_cond(k,beta)]
    c[tuple(row)]+=1
for x,n in c.items(): print("R16,nonneg,count b0 | b1:",x,n)
