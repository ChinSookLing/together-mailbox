import math
from fractions import Fraction as F
nd=lambda x: abs(x-math.floor(x+F(1,2)))
fr=lambda x:x-math.floor(x)
L=[]; p=lambda *x: L.append(' '.join(map(str,x)))
a,b,c,d=F(1),F(11,10),F(3),F(41,10); V=(a,b,c,d)
s=(b+c)/a; r=c/b; w=d/(b+c); th=b/(b+c); mu=c/(5*d); ep=a/(5*d)
dist=lambda t:[nd(x*t) for x in V]
p("V=",V,"s=",s,"r=",r,"w=",w,"theta=",th)
p("TN d<=4a:",d<=4*a,"| LN d>=4c (4c=12):",d>=4*c,"| Omega 4a<d<4c:",4*a<d<4*c)
p("WL c<4a:",c<4*a,"bound 2ac/(4a-c)=",2*a*c/(4*a-c),"d>=bound:",d>=2*a*c/(4*a-c),"| K5 c<=8a/3:",c<=8*a/3)
p("HB: s in [15/8,15/2]",F(15,8)<=s<=F(15,2),"r in set",(1<r<=F(8,7) or 4<=r<=F(13,2)),"w in [4/5,6/5]",F(4,5)<=w<=F(6,5),"| C1 r<=8/7:",r<=F(8,7))
# nudge from tL=1/5
tL=F(1,5); X=d*tL; k=round(X); p("tL=1/5 dists",[str(x) for x in dist(tL)],"X=dt_L=",X,float(X),"||X||=",nd(X))
e=X-k; sg=1 if e>=0 else -1; t=(k+F(sg,5))/d
p("nudge t=(k'+σ/5)/d: k'=",k,"σ=",sg,"t=",t,"=1.2/4.1:",t==F(12,10)/F(41,10),"dists",[float(x) for x in dist(t)],"||ct||=",float(nd(c*t)),"exact",nd(c*t),"fails c:",nd(c*t)<F(1,5))
t0=F(1,4); X0=d*t0; k0=round(X0); e0=X0-k0
p("T4 route t0=1/4 dists",[str(x) for x in dist(t0)],"X=",X0,"||X||=",nd(X0))
if nd(X0)<F(1,5):
    t1=(k0+F(1 if e0>=0 else -1,5))/d; p("  nudge from 1/4 gives t=",t1,"same as above:",t1==t,"min",float(min(dist(t1))))
t=F(42,100); p("t=0.42 dists",[str(x) for x in dist(t)],[float(x) for x in dist(t)],"min>=1/5:",min(dist(t))>=F(1,5))
# Opus rules
lam3=2*c/(5*d); lam2=(b/c)*(1+lam3); lam1=(a/b)*(1+lam2)
p("NW(5) lambdas",[float(x) for x in (lam1,lam2,lam3)],"cond all<=3/5:",max(lam1,lam2,lam3)<=F(3,5),"| NW-i",b/c+2*b/(5*d)<=F(3,5),"NW-ii",3*b/(5*a)>=1+b/c+2*b/(5*d))
Tl,Th=F(1,5)+mu,F(4,5)-mu
p("SLN1 S1 theta<=3/5-2mu:",th<=F(3,5)-2*mu,float(th),float(F(3,5)-2*mu),"| guarantee:",s*(F(3,5)-2*ep)>=2+(F(2,5)+2*mu)/th, float(s*(F(3,5)-2*ep)),float(2+(F(2,5)+2*mu)/th))
k0_=math.ceil(s*(F(1,5)+ep)); k=k0_ if k0_%2 else k0_+1; phi=1-2*th
p("SLN-odd k0",k0_,"k",k,"k<=s(4/5-eps)",k<=s*(F(4,5)-ep),"k*phi<=3/5-2mu",k*phi<=F(3,5)-2*mu,float(k*phi),float(F(3,5)-2*mu))
p("Qwen B region: c<4a",c<4*a,"| max(4a,(5c-2a)/2)=",max(4*a,(5*c-2*a)/2),"d=",d,"in:",max(4*a,(5*c-2*a)/2)<d<min(9*a,4*c))
inHBr=False; inC1=False
p("V in Opus gap G (not covered by NW, SLN1 guarantee, SLN-odd, WL, HB, C1; and in Omega?): c>=4a?",c>=4*a,"-> R requires (c>=4a) or (c<4a and d<2ac/(4a-c)):",c<4*a and d<2*a*c/(4*a-c),"; in Omega:",4*a<d<4*c)
# LB(k) and anchors
sol=[]
for k in range(1,60):
    t=F(k)/(b+c)
    if min(dist(t))>=F(1,5): sol.append(('LB',k,t))
p("LB(k) k<=59 solutions:",sol[:5] or "NONE", "(first k with all four >=1/5)")
anch={'a+b':a+b,'a+c':a+c,'a+d':a+d,'b+c':b+c,'b+d':b+d,'c+d':c+d}
for nm,S in anch.items():
    for tau in [F(m,4) for m in range(1,41)]:
        t=tau/S
        if min(dist(t))>=F(1,5): p("anchor",nm,"tau=",tau,"t=",t,"min",float(min(dist(t)))); break
    else: p("anchor",nm,"tau in {m/4,m<=40}: none")
open('chk_argonC_out.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
