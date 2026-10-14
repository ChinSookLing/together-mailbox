# Puck independent check of Astra R33 (c)-counterexample.
from collections import defaultdict, Counter
p,b=1009,500
W=[449,3161,1353,1167,917,1571,45,699]
N=32*p
def hit(t,w,M):
    r=t*w%M
    return 16*min(r,M-r)<M
assert all(p%d for d in (2,3,5,7,11,13,17,19,23,29,31))
assert all(w%2 and 0<w<N//2 and w%p not in (0,1,p-1) for w in W)
C5=[t for t in range(1,N//2+1,2) if t%p in (b,p-b)]
C6=[t for t in range(1,N+1,2) if t%p in (2*b%p,(-2*b)%p)]
for t in C5:
    assert sum(hit(t,w,N) for w in W)==1
pair=defaultdict(list)
for t in C6:
    h=[(i,e) for i,w in enumerate(W) for e in (0,1) if hit(t,w+e*N,2*N)]
    assert len(h)==2 and h[0][0]!=h[1][0]
    (i,ei),(j,ej)=h
    pair[tuple(sorted((i,j)))].append(ei^ej^1)
assert len(pair)==8
adj=defaultdict(set)
for (i,j) in pair: adj[i].add(j); adj[j].add(i)
order=[0]; prev=None; seen={0}
while len(order)<8:
    x=order[-1]
    y=[z for z in adj[x] if z!=prev and z not in seen][0]
    prev=x; order.append(y); seen.add(y)
assert 0 in adj[order[-1]]
r=[(W[order[(k+1)%8]]*pow(W[order[k]],-1,32))%32 for k in range(8)]
assert all(x in (3,29,11,21) for x in r)
labs=[pair[tuple(sorted((order[k],order[(k+1)%8])))][0] for k in range(8)]
H=sum(labs)%2
mod8=Counter(w%8 for w in W)
def q(w): return 1 if (w%16) in (3,5,9,15) else 0
Q=sum(q(w) for w in W)%2
print("MATCH tiling+Ham8+mixed")
print("order", order)
print("ratios", r)
print("labels", labs, "H", H)
print("mod8", dict(mod8), "expect n1=3 n3=2 n5=2 n7=1")
print("Q", Q, "unsigned", sorted({min(w%32,32-w%32) for w in W}))
assert mod8[1]==3 and mod8[3]==2 and mod8[5]==2 and mod8[7]==1
assert H==1 and Q==1
print("CHECKED: (c) FALSE on this mixed Ham-8; H still 1")
