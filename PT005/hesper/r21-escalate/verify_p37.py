from math import gcd, ceil
from itertools import product
p=37
R=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]
W=[112,2,336,448,5,6,192,8,416,528,48,160,13,14,16]
print("mod p ±R:", all(min(w%p,p-w%p)==r for w,r in zip(W,R)))
def cov(t,u,N):
    r=(t*u)%N; return 16*min(r,N-r)<N
def improper(w,N):
    if sum(x%2 for x in w)<2: return False
    return all(any(cov(t,u,N) for u in w) for t in range(1,N//2+1))
for k in range(1,5):
    N=(2**k)*p; w=[x%N for x in W]
    print(N, improper(w,N), "odd",sum(x%2 for x in w))
def L(D,w):
    s=0
    for x in w:
        if x%D:
            g=gcd(D,x); s+=g*ceil((D//g)/8)
    return s
M=16*p
for D in [d for d in range(2,M+1,2) if M%d==0]:
    print("D",D,"L",L(D,W),"L<D",L(D,W)<D)
# children at 32p: odd T only (even inherited) -- but check full anyway
N2=32*p
opts=[]
for x in W:
    opts.append([x, x+M])
# precompute per coord per bit coverage sets over T in 1..N2/2
import numpy as np
T=np.arange(1,N2//2+1)
cv=[[ (16*np.minimum((T*u)%N2, N2-(T*u)%N2) < N2) for u in o] for o in opts]
cnt=0;first=None
for mask in range(1<<15):
    c=np.zeros(len(T),bool); w=[]
    for i in range(15):
        b=(mask>>i)&1; c|=cv[i][b]; w.append(opts[i][b])
    if c.all() and sum(x%2 for x in w)>=2:
        cnt+=1
        if first is None: first=w
print("improper children 32p:",cnt, first)
