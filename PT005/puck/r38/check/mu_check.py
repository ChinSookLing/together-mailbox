# Puck R38: Hesper's side condition (repeated full data) — check that the level-5 mask is a function of
# Argon's full data (m mod 32, w mod 32, sgn d) for fixed (p,b). Then two coordinates with identical full data
# have identical nonempty level-5 masks, impossible in an exact tiling (level-5 cells covered exactly once) => mu=1.
from collections import defaultdict
def hit(t,W,M): r=t*W%M; return 16*min(r,M-r)<M
def bal(x,p):
    x%=p; return x if x<=p//2 else x-p
tot=bad=0
for p in (29,31,37,41,43,47,53,59,61,67,71,769):
    n5=32*p
    for b in range(1,(p+1)//2):
        c5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
        g=defaultdict(set)
        for w in range(1,16*p,2):
            if w%p in (0,1,p-1): continue
            d=bal(b*w,p); m=(b*w-d)//p
            # level-5 mask in signed-slot form so it is comparable across w (slot of t, not index)
            pinv=pow(p,-1,64)
            T=[t if t%p==b%p else n5-t for t in c5]
            mk=frozenset(((T[i]-b)*pinv)%32 for i,t in enumerate(c5) if hit(t,w,n5))
            g[(m%32,w%32,d>0)].add(mk)
        for k,S in g.items():
            tot+=1
            if len(S)!=1: bad+=1
    print(p,'groups so far',tot,'bad',bad,flush=True)
print('RESULT groups',tot,'non-function',bad)
