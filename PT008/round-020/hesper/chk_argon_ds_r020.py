src=open('base.py').read(); exec(src[:src.index("ok=lambda")])
from fractions import Fraction as F
from math import ceil,gcd
from functools import reduce
ok=lambda V,t: t>0 and min(nd(u*t) for u in V)>=F(1,5)
def PSs(V):
    for i,u in enumerate(V):
        W=[x for j,x in enumerate(V) if j!=i]; g=reduce(gcd,W); P=F(1,g); t0=F4(*W); x=fr(u*P); ph=fr(u*t0)
        if A(ph): n=0
        elif x==0: continue
        elif x<=F(1,2): n=ceil(fr(F(1,5)-ph)/x)
        else: n=ceil(fr(ph-F(4,5))/(1-x))
        return t0+n*P,i
    return None
def CLR_LS(a,B,C,E):
    S=B+C; ts=S*F4(B,C,E); m=ts.denominator; Q=m*S
    th=F(B,S); w=F(E,S)
    R=[k for k in range(Q) if all(nd(F(k,m)*u)>F(1,5) for u in (th,1-th,w))]
    gaps=[(R[(i+1)%len(R)]-R[i])%Q or Q for i in range(len(R))]; G=max(gaps)
    s=F(S,a); cond=s>=F(5*G,3*m)
    k0=ceil(m*s/5); k=k0+min((r-k0)%Q for r in R); t=F(k,m)/S
    return m,Q,len(R),G,cond,ok((a,B,C,E),t),t
for N in (1,2,3,5,10):
    V=(1,10*N,20*N+1,30*N)
    t0=F4(10*N,20*N+1,30*N); print('Argon fam N=%d'%N,'t0',t0,'phi0',fr(t0),'in E_PS(a outsider)',not A(fr(t0)),'PS*',PSs(V),'CLR+LS (m,Q,|R|,G,s-cond,ok,t)',CLR_LS(*V))
th,w=F(1,3),F(4,3); print('Argon QERC1 cex (1/3,4/3) R1:',[k for k in range(3) if nd(k*th)>=F(1,5) and nd(k*w)>=F(1,5)])
ts=3*F4(1,2,3); print('DeepSeek V5 LS tau*',ts,'m',ts.denominator,'rho*',ts.denominator*ts%12)
