src=open('/workspace/work/pt008r20/hesper/base.py').read()
exec(src[:src.index("ok=lambda")] if "ok=lambda" in src else src)
from fractions import Fraction as F
from math import ceil,sqrt
def cf(x,Q0):
    # convergents of rational x, last with q<=Q0
    p0,q0,p1,q1=0,1,1,0; y=x; conv=[]
    while True:
        a=floor(y); p0,q0,p1,q1=p1,q1,a*p1+p0,a*q1+q0; conv.append((p1,q1))
        if y==a: break
        y=1/(y-a)
    best=[c for c in conv if c[1]<=Q0][-1]
    return conv,F(*best)
print("== Ex1 V=(1,12,24,32)")
a,b,c,d=map(F,(1,12,24,32)); S=b+c; th=b/S; w=d/S; M=max(1-th,w); Q0=ceil(20*M)
t0=F4(b,c,d); ts=S*t0; conv,tau=cf(ts,Q0)
print("S",S,"s",S/a,"theta",th,"w",w,"Q0",Q0,"t0",t0,"tau*",ts,"tau0",tau)
print("cluster nd",nd(tau*th),nd(tau*(1-th)),nd(tau*w),"a nd",nd(tau/(S/a)))
from math import lcm
L=lcm(th.denominator,w.denominator); print("L",L,"frac(L/s)",fr(L/(S/a)))
print("== Ex rescheck family (1,N,2N+1,3N), N=10")
for N in [2,5,10,20]:
    a,b,c,d=map(F,(1,N,2*N+1,3*N)); S=b+c; s=S/a; th=b/S; w=d/S; M=max(1-th,w); Q0=ceil(20*M)
    t0=F4(b,c,d); ts=S*t0; conv,tau=cf(ts,Q0); L=lcm(th.denominator,w.denominator)
    print(N,"t0",t0,"tau*",ts,"Q0",Q0,"tau0",tau,"conv",conv,"cl",nd(tau*th),nd(tau*(1-th)),nd(tau*w),"a phase",fr(tau/s),"L",L,"x",fr(L/s))
t=F(7,31); print("t=7/31 nd",[nd(v*t) for v in (1,10,21,30)])
print("F4(1,21,30)",F4(1,21,30))
print("== Ex2 irrational (float)")
b,c,d=30.,60.,30+30*sqrt(2); t0=1/(4*b); print("d",d,"d<=3b",d<=3*b,"tau*",90*t0,"Q0",ceil(20*d/90),"a nd",t0,"d nd", min((d*t0)%1,1-(d*t0)%1), "b",b*t0,"c",c*t0)
