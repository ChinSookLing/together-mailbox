exec(open('chain.py').read().split('for k in map')[0])
import sys,collections
legal2=lambda w: w%17 not in (0,1,16)
def runm(k,b,levels):
    Ns=[17*2**(k+j) for j in range(levels)]; bs=[b*2**j%17 for j in range(levels)]
    Ts=[cls(Ns[j],bs[j]) for j in range(levels)]; top=levels-1
    sig={}
    for w in range(1,Ns[top]):
        if not legal2(w): continue
        cs=tuple(cov(w%Ns[j],Ns[j],Ts[j]) for j in range(levels))
        if any(len(c)==0 for c in cs): continue
        sig.setdefault(cs,[]).append(w)
    coords=[(ws[0],cs) for cs,ws in sig.items()]
    full=[frozenset(range(len(Ts[j]))) for j in range(levels)]
    found=[]
    def dfs(used,acc):
        if all(used[j]==full[j] for j in range(levels)):
            if len(acc)<=8: found.append([w for w,_ in acc])
            return
        if len(acc)==8: return
        rem=full[top]-used[top]; i=min(rem)
        for w,cs in coords:
            if i in cs[top] and all(not(cs[j]&used[j]) for j in range(levels)):
                dfs([used[j]|cs[j] for j in range(levels)],acc+[(w,cs)])
    dfs([frozenset()]*levels,[])
    return len(coords),found
k=int(sys.argv[1])
# Grok's cover count at k
N=17*2**k
for b in range(1,9):
    T=cls(N,b)
    odd={cov(w,N,T) for w in range(1,N,2) if legal2(w)}; ev={cov(w,N,T) for w in range(2,N,2) if legal2(w)}
    o4={c for c in odd if len(c)==4}; e4={c for c in ev if len(c)==4}
    nc,f=runm(k,b,2)
    print(f"k={k} b={b} odd size4={len(o4)} even size4={len(e4)} overlap={len(o4&e4)} even sizes={sorted(collections.Counter(len(c) for c in ev).items())} mixed doublings={len(f)} ex={f[:1]}",flush=True)
