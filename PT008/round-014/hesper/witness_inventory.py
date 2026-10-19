# Hesper R014 P2: recheck V1..V4 against the certified PT-008 five-runner inventory (exact Fractions)
from fractions import Fraction as F
from math import floor, ceil
def nd(z): return min(z-floor(z), ceil(z)-z)
def fr(z): return z-floor(z)
D=F(1,5)
def ok(t,V): return all(nd(u*t)>=D for u in V)
W={'V1':(F(1),F(11,10),F(3),F(41,10)),'V2':(F(1),F(2),F(3),F(9,2)),'V3':(F(1),F(3),F(4),F(7)),'V4':(F(1),F(30),F(60),F(80))}
for name,(a,b,c,d) in W.items():
    s=(b+c)/a; r=c/b; w=d/(b+c); th=b/(b+c)
    om = 4*a<d<4*c
    TN = d<=4*a
    LN = d>=4*c
    WL = c<4*a and d>=2*a*c/(4*a-c)       # = GW(5) with m=a,M=c,w=d
    K5 = c<=F(8,3)*a                       # = K_5 cluster condition (N=5)
    HB = F(15,8)<=s<=F(15,2) and ((1<r<=F(8,7)) or (4<=r<=F(13,2))) and F(4,5)<=w<=F(6,5)
    C1 = om and F(15,8)<=s<=5 and 1<r<=F(8,7) and F(4,5)<=w<=F(9,5)
    K5ii = d>=4*c   # script-K_5 (ii) needs w>=(n-1)M = 4c (then {a,b,c} in K_4)
    cert = dict(TN=TN,LN=LN,WL_GW5=WL,K5=K5,HB=HB,C1=C1,scriptK5_ii=K5ii)
    # R013 PROOF CANDIDATES (not certified)
    l3=2*c/(5*d); l2=(b/c)*(1+l3); l1=(a/b)*(1+l2); NW = max(l1,l2,l3)<=F(3,5)
    mu=c/(5*d); eps=a/(5*d); k0=ceil(s*(D+eps))
    S1 = th<=F(3,5)-2*mu
    if S1:
        x0=fr(k0*th); T=(D+mu,F(4,5)-mu)
        j=0 if T[0]<=x0<=T[1] else ceil(fr(D+mu-x0)/th); ks=k0+j
        SLN1 = ks<=s*(F(4,5)-eps)
    else: SLN1=False
    k=k0 if k0%2 else k0+1; phi=1-2*th
    SLNodd = k<=s*(F(4,5)-eps) and k*phi<=F(3,5)-2*mu
    QW = c<4*a and max(4*a,(5*c-2*a)/2)<d<min(9*a,4*c)
    cand=dict(NW5=NW,SLN1=SLN1,SLNodd=SLNodd,Qwen_ad2=QW)
    print(name,(a,b,c,d),'s=%s r=%s w=%s theta=%s Omega=%s'%(s,r,w,th,om))
    print('  certified:',cert,'-> covered' if any(cert.values()) else '-> NOT covered by any certified rule')
    print('  R013 candidates:',cand, ' lambdas',(l1,l2,l3),' WL bound',(2*a*c/(4*a-c) if c<4*a else 'c>=4a'))
    # integer locks LB(k)=k/(b+c), k=1..12 (finite listing, CHECKED only)
    print('  LB(k) k<=12 successes:',[kk for kk in range(1,13) if ok(F(kk)/(b+c),(a,b,c,d))])
    for p,q,lab in [(a,c,'a+c'),(b,d,'b+d'),(a,d,'a+d'),(c,d,'c+d'),(a,b,'a+b'),(b,c,'b+c')]:
        hits=[str(F(j,4)) for j in range(1,25) if ok(F(j,4)/(p+q),(a,b,c,d))]
        print('   anchor',lab,'tau in (1/4)Z, tau<=6 successes:',hits[:8])

# V1 through SLN1 criterion, full algorithm
a,b,c,d=W['V1']; s=(b+c)/a; th=b/(b+c); mu=c/(5*d); eps=a/(5*d); k0=ceil(s*(D+eps))
x0=fr(k0*th); j=0 if D+mu<=x0<=F(4,5)-mu else ceil(fr(D+mu-x0)/th); ks=k0+j; ts=F(ks)/(b+c)
X=d*ts
if nd(X)>=D: t=ts
else:
    kp=floor(X+F(1,2)); e=X-kp; sg=1 if e>=0 else -1; t=(kp+F(sg,5))/d
print('V1 SLN1: k0',k0,'x0',x0,'T',(D+mu,F(4,5)-mu),'j',j,'k*',ks,'bound s(4/5-eps)',s*(F(4,5)-eps),'t*',ts,'X',X,'t',t,'dists',[str(nd(u*t)) for u in W['V1']],'ok',ok(t,W['V1']))
