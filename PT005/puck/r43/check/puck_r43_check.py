# Puck independent R43 checker: verifies claimed chains from COMMON definitions only.
from math import gcd
def dist(x,M):
    r=x%M; return min(r,M-r)
def covered_all(w,M):
    return all(any(16*dist(T*x,M)<M for x in w) for T in range(1,M//2+1))
def odd(w): return sum(x%2 for x in w)
def improper(w,M): return covered_all(w,M) and odd(w)>=2
def l7(w,M):
    out=[]
    for D in range(2,M+1,2):
        if M%D: continue
        E=[x for x in w if x%D]
        s=sum(gcd(D,x)*(-(-(D//gcd(D,x))//8)) for x in E)
        out.append((D,len(E),s,len(E)>=2 and s<D))
    return out
def isopen(w,M):
    return improper(w,M) and not any(c for *_,c in l7(w,M))
def frozen(w,M,p):
    k=(M//p).bit_length()-1; return sum(1 for x in w if x%(2**k))
def lift_ok(a,b,M):
    # multiset b must be obtainable from a by +0/+M per coordinate (bijection by residue mod M)
    if len(a)!=15 or len(b)!=15: return False
    if any(not(1<=x<2*M) for x in b): return False
    return sorted(x%M for x in b)==sorted(a)
def chain(name,p,vecs):
    print("==",name,"p=",p)
    M=p; ok=True
    for i,w in enumerate(vecs):
        if i>0:
            lk=lift_ok(vecs[i-1],w,M//2) if False else lift_ok(vecs[i-1],w,M//2)
        o=isopen(w,M)
        print(f" M={M} f={frozen(w,M,p)} odd={odd(w)} cov={covered_all(w,M)} open={o}" + (f" lift={lk}" if i>0 else ""))
        if not o or (i>0 and not lk): ok=False
        if i==len(vecs)-1:
            for D,e,s,c in l7(w,M): print(f"   D={D} |E|={e} S={s} closed={c}")
        M*=2
    print(" CHAIN VALID:",ok)
# Grok p=17
g0=[8,11,11,15,3,5,15,11,7,16,1,15,16,3,13]
chain("Grok",17,[g0,g0,[8,11,11,49,37,5,15,11,7,50,1,15,16,3,13],[8,113,11,49,37,73,83,11,75,50,1,15,16,3,13]])
# GPT p=47
r=[2,4,5,6,7,8,10,11,13,15,17,18,19,22,23]
chain("GPT",47,[r,[49,51,5,6,7,55,57,11,13,62,17,18,19,69,23],[143,51,5,6,7,149,57,11,107,62,17,112,113,163,23],[143,51,193,194,195,149,245,199,295,62,205,112,113,351,23]])
# Astra p=43
chain("Astra43",43,[[2,5,5,6,8,9,13,14,16,16,17,18,19,20,21],[2,5,9,13,16,19,48,49,51,57,59,60,61,63,64],[2,13,16,48,49,51,91,95,105,143,145,146,147,149,150],[2,13,16,49,91,105,143,146,220,223,267,317,319,321,322]])
# Astra p=17 (X and Y only; intermediate not given)
R=[1,1,1,2,3,3,3,4,5,5,6,7,7,8,8]; X=[1,1,3,3,3,5,6,7,7,8,8,18,19,21,22]; Y=[1,3,8,21,22,35,37,41,42,71,73,74,75,86,87]
print("== Astra17"); print(" root open",isopen(R,17)," X lift",lift_ok(R,X,17)," X open",isopen(X,34)," f",frozen(X,34,17))
print(" Y open",isopen(Y,136)," f",frozen(Y,136,17)," Y mod34 == X:",sorted(y%34 for y in Y)==sorted(X))
# find an intermediate Z at 68
import itertools
from collections import Counter
# match Y to X: each y%34 maps to an x; Z = y%68
Z=sorted(y%68 for y in Y); print(" Z(68)=",Z," Z mod34==X",sorted(z%34 for z in Z)==sorted(X)," Z open",isopen(Z,68)," f",frozen(Z,68,17))
print("== Grok repair: 136-node via its own mod-68 parent")
G=[8,113,11,49,37,73,83,11,75,50,1,15,16,3,13]
Zg=sorted(y%68 for y in G); print(" Z(68)=",Zg," Z mod34==X",sorted(z%34 for z in Zg)==sorted(g0)," Z open",isopen(Zg,68)," f",frozen(Zg,68,17))
