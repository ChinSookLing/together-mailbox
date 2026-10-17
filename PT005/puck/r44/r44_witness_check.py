# Independent check of R44 F3 lemma against Puck witnesses, literal R44 COMMON definitions
from math import gcd
def nd(x,M): r=x%M; return min(r,M-r)
def improper(w,M):
    if sum(x%2 for x in w)<2: return False
    return all(any(16*nd(T*x,M)<M for x in w) for T in range(1,M//2+1))
def l7closed(w,M):
    for D in range(2,M+1,2):
        if M%D: continue
        E=[x for x in w if x%D]
        if len(E)<2: continue
        S=sum(gcd(D,x)*(-(-(D//gcd(D,x))//8)) for x in E)
        if S<D: return True
    return False
def is_open(w,M): return improper(w,M) and not l7closed(w,M)
def v2(x):
    c=0
    while x%2==0: x//=2;c+=1
    return c
def F(w,k,j): return sum(1 for x in w if v2(x)<k and k-v2(x)>=j)
def legal(par,ch,M): return sorted(x%M for x in ch)==sorted(par) and all(1<=x<2*M for x in ch)
for name,node,child in [("A",[1,3,3,5,7,8,18,22,40,55,69,75,87,105,110],[1,3,5,7,8,69,75,87,139,154,158,176,191,241,246]),
                        ("B",[1,3,8,11,13,15,37,49,73,75,79,84,113,117,118],[1,13,15,79,84,118,139,144,147,173,185,209,211,249,253])]:
    M=136;k=3
    print(name,"node open",is_open(node,M),"F3",F(node,k,3),"child open",is_open(child,2*M),"legal",legal(node,child,M))
