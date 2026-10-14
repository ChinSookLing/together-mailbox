# Hesper: does every legal coordinate's real cover data project onto Astra's (L,U)? p=17, k=5->6, b=1..8
import sys; sys.path.insert(0,'/workspace/work/together-mailbox/PT005/puck/verify')
from common import *
from collections import Counter
def signed(t,k,b):  # member label t' = +-t with t' = b mod 17, as residue mod N_k
    n=N(k); return t%n if t%P==b%P else (-t)%n
def astra(w,b):
    a=w%32; A=pow(a,-1,32)
    c=(b*w)%P
    if c%2==0: c-=P
    s=1 if c>0 else -1; e=2*c-17*s
    L=Counter(A*x%32 for x in (c,c-2*s))
    U=Counter(A*x%32 for x in ([e-4,e-2,e,e+2] if e>0 else [e-2,e,e+2,e+4]))
    return L,U,c
bad=0; tot=0; Ush=Counter()
for b in range(1,9):
    c5=C(5,b); b6=(2*b)%P; c6=C(6,b6)
    for w in legal(5):
        s=[t for t in c5 if covers(t,w,N(5))]
        A=[t for e in (0,1) for t in c6 if covers(t,(w+e*N(5))%N(6),N(6))]
        La=Counter(signed(t,5,b)%32 for t in s)
        Ua=Counter(signed(t,6,b6)%32 for t in A)
        L,U,c=astra(w,b)
        tot+=1; Ush[(len(s),len(A))]+=1
        U2=Counter({k:2*v for k,v in U.items()})
        if La!=L or Ua!=U2:
            bad+=1
            if bad<=5: print('MISMATCH b',b,'w',w,'c',c,'La',sorted(La.elements()),'L',sorted(L.elements()),'Ua',sorted(Ua.elements()),'U',sorted(U.elements()))
print('compare: real L == Astra L, real lift multiset == 2 x Astra U')
print('coords checked',tot,'mismatches',bad,'(|cover5|,|A0+A1|) shapes',dict(Ush))
