from itertools import product
def cov(t,w,N):
    r=t*w%N; return 16*min(r,N-r)<N
p,b,W=29,1,[3,97,125,151,413,191,285,385]
N5=32*p;N6=64*p
print('p',p,'b',b,'legal',all(w%2 and w%p not in(0,1,p-1) and w<16*p for w in W),'distinct',len(set(W))==8,'mod8',[w%8 for w in W])
T5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
print(' k5 members',len(T5),'counts',set(sum(cov(t,w,N5) for w in W) for t in T5))
T6=[t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
print(' k6 2-cover counts',sorted(set(sum(cov(t,w,N6)+cov(t,w+32*p,N6) for w in W) for t in T6)))
sols=[E for E in product((0,1),repeat=8) if all(sum(cov(t,w+32*p*e,N6) for w,e in zip(W,E))==1 for t in T6)]
print(' k6 members',len(T6),'exact lifts',len(sols),sols)
# XOR graph degrees: edge between coords sharing a member
hits={t:[(i,e) for i,w in enumerate(W) for e in (0,1) if cov(t,w+32*p*e,N6)] for t in T6}
deg=[0]*8;E=set()
for t,h in hits.items():
    if len(h)==2: E.add((min(h[0][0],h[1][0]),max(h[0][0],h[1][0]),t))
import collections
pairs=collections.Counter((a,c) for a,c,_ in E)
for a,c in pairs: deg[a]+=1;deg[c]+=1
print(' XOR graph edges',len(pairs),'deg',deg)
