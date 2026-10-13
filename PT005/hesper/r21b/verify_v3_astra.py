from math import gcd, ceil
import numpy as np
p=37
R=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]
W16=[112,2,336,448,5,80,192,8,416,528,48,160,13,236,16]
W32=[704,2,928,448,5,80,192,8,416,1120,640,160,13,236,608]
print("mod p ±R W16:",all(min(w%p,p-w%p)==r for w,r in zip(W16,R)))
print("mod p ±R W32:",all(min(w%p,p-w%p)==r for w,r in zip(W32,R)))
def improper(w,N):
    w=[x%N for x in w]
    if sum(x%2 for x in w)<2: return False
    T=np.arange(1,N//2+1); c=np.zeros(len(T),bool)
    for u in w:
        r=(T*u)%N; c|=16*np.minimum(r,N-r)<N
    return bool(c.all())
for k in (1,2,3,4): print("W16 improper @",k*0+2**k*p, improper(W16,2**k*p))
print("W32 improper @1184", improper(W32,32*p))
print("child relation:", all(b-a in (0,16*p) for a,b in zip(W16,W32)))
def L(D,w): return sum(gcd(D,x)*ceil((D//gcd(D,x))/8) for x in w if x%D)
def l7any(w,M):
    ok=[]
    for D in range(2,M+1,2):
        if M%D==0:
            E=[x for x in w if x%D]
            if len(E)>=2 and L(D,w)<D: ok.append(D)
            elif len(E)<2 and L(D,w)<D: ok.append(("E<2",D))
    return ok
print("W16 L7 passing D @592:", l7any(W16,592))
print("W32 L7 passing D @1184:", l7any(W32,1184))
for D in [d for d in range(2,1185,2) if 1184%d==0]: print(D, L(D,W32), L(D,W32)<D)
# all children
M=16*p;N2=32*p;T=np.arange(1,N2//2+1)
cv=[[16*np.minimum((T*u)%N2,N2-(T*u)%N2)<N2 for u in (x,x+M)] for x in W16]
ch=[];fails=[]
for mask in range(1<<15):
    c=np.zeros(len(T),bool);w=[]
    for i in range(15):
        b=(mask>>i)&1;c|=cv[i][b];w.append(W16[i]+b*M)
    if c.all() and sum(x%2 for x in w)>=2:
        ch.append(w)
        if not l7any(w,N2): fails.append(w)
print("children",len(ch),"L7-failing",len(fails),"W32 in fails:",W32 in fails)
