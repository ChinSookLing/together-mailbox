import itertools
from collections import Counter
mix=[]
for line in open("covers.txt"):
    a=list(map(int,line.split())); mix.append(tuple(sorted(zip(a[0::2],a[1::2]))))
def r16(k,b):
    doms=[]
    for c,v in k:
        h=(c//2)%16
        if h%2==b%2: doms.append([((h-v)%16,(h+v)%16)])
        else: doms.append([(h,(h+2*v)%16),(h,(h-2*v)%16)])
    target=[x for x in range(16) if x%2!=b%2]
    for ch in itertools.product(*doms):
        C=Counter(x for d in ch for x in d)
        if all(C[x]==2 for x in target): return True
    return False
def lift32(k,b):
    opts=[]
    for c,v in k:
        h=(c//2)%16; o=set()
        for L in (0,1):
            H=h+16*L
            if h%2==b%2: o.add(frozenset({(H-v)%32,(H+v)%32}))
            else:
                for e in (1,-1): o.add(frozenset({H%32,(H+2*e*v)%32}))
        opts.append([x for x in o if len(x)==2])
    target=frozenset(x for x in range(32) if x%2!=b%2)
    def go(i,used):
        if i==8: return used==target
        return any(go(i+1,used|d) for d in opts[i] if not d&used)
    return go(0,frozenset())
R0=[k for k in mix if r16(k,0)]; R1=[k for k in mix if r16(k,1)]
print("mixed doublable",len(mix),"R16 beta0",len(R0),"beta1",len(R1),"beta-agree on all",all(r16(k,0)==r16(k,1) for k in mix))
print("mod32 lift where R16 holds:",sum(lift32(k,b) for k in R0 for b in (0,1)),"of",2*len(R0))
print("mod32 lift where R16 fails (should be 0):",sum(lift32(k,b) for k in mix if k not in set(R0) for b in (0,1)))
def canon(k):
    best=None
    for a in range(1,32,2):
        for t in range(16):
            kk=tuple(sorted(((a*c+2*t)%32,min((a*v)%32,32-(a*v)%32)) for c,v in k))
            if best is None or kk<best: best=kk
    return best
print("orbits of R16-true:",sorted(Counter(canon(k) for k in R0).values()))
print("orbits of all mixed doublable:",len(set(canon(k) for k in mix)))
tests=["(0,1)(0,1)(6,11)(6,11)(12,1)(12,1)(22,1)(22,1)","(0,1)(0,1)(8,1)(14,3)(16,1)(16,3)(18,3)(24,1)","(0,1)(0,5)(2,5)(4,5)(8,1)(24,1)(28,5)(30,5)","(0,1)(0,7)(2,11)(6,11)(12,1)(20,1)(26,11)(30,11)","(0,1)(2,1)(8,11)(10,1)(14,1)(16,11)(22,1)(24,1)","(0,1)(0,1)(0,5)(0,5)(6,15)(6,15)(10,1)(10,1)","(0,1)(0,3)(0,7)(0,15)(6,11)(12,11)(20,11)(26,11)"]
S=set(mix)
for t in tests:
    k=tuple(sorted(tuple(map(int,x.split(","))) for x in t.strip("()").split(")(")))
    print(t, "in7168",k in S, "R16",r16(k,0),r16(k,1),"lift",lift32(k,0),lift32(k,1))
