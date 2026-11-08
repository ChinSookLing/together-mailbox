# Independent count of the filtered set, no enumeration of tuples.
# Filter "for each i, gcd(other four, M)=1" with M=6p and no element divisible by p
# <=> at most 3 of the 5 values are even AND at most 3 are multiples of 3.
from math import comb
import itertools,sys
def count(p):
    A=[x for x in range(1,3*p+1) if x%p]
    n={}
    for x in A: n[(x%2==0,x%3==0)]=n.get((x%2==0,x%3==0),0)+1
    cls=list(n); tot=0; allm=0
    for ks in itertools.product(range(6),repeat=len(cls)):
        if sum(ks)!=5: continue
        m=1
        for c,k in zip(cls,ks): m*=comb(n[c]+k-1,k)
        allm+=m
        ev=sum(k for c,k in zip(cls,ks) if c[0]); m3=sum(k for c,k in zip(cls,ks) if c[1])
        if ev<=3 and m3<=3: tot+=m
    return allm,tot
for p in map(int,sys.argv[1:]): print(p,*count(p))
