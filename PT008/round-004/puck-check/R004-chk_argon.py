from common import *
random.seed(9)
out=[]
def P(*a):
    s=" ".join(str(x) for x in a); print(s); out.append(s)
V=[F(1),F(3),F(4)]
t=F(1,4); P("CE1 V={1,3,4}: ||1/4||",nd(t),"||3/4||",nd(3*t),"||4/4||",nd(4*t),"g=",g(V,t),"local max?",is_locmax(V,t),"local min?",is_locmin(V,t))
t=F(1,5); P("t=1/5: ||1/5||",nd(t),"||3/5||",nd(3*t),"||4/5||",nd(4*t),"g",g(V,t),"local max?",is_locmax(V,t))
P("  but n=4 threshold 1/4: g(1/5)=1/5 <1/4, not success; best local max of {1,3,4} on [0,3]:",max((g(V,t),str(t)) for t in locmaxes(V,F(3))))
V2=[F(1)]; P("CE2 V={1,-1} -> |.|={1}: maxima in (0,3]:",[str(t) for t in locmaxes(V2,F(3))],"(only peaks k+1/2)")
# necessity: all local maxima in C = Cpeak U Ccross(sum or diff)
bad=0;tot=0
for trial in range(400):
    W=rnd_speeds(random.randint(2,5),12,rat=(trial%2==1)); T=F(3)
    for t in locmaxes(W,T):
        tot+=1
        inC=any(t==F(2*k+1)/(2*u) for u in W for k in range(0,300)) or any(((t*(u+v)).denominator==1) or ((u!=v) and (t*abs(u-v)).denominator==1) for u in W for v in W)
        if not inC: bad+=1
P("Necessity (all local maxima in C=Cpeak U Ccross): maxima tested",tot,"outside C",bad)
# do difference-type times ever give a max that is not ALSO sum/peak type?
diffonly=0
for trial in range(400):
    W=rnd_speeds(random.randint(2,5),12,rat=(trial%2==1))
    for t in locmaxes(W,F(3)):
        if not any((t*(u+v)).denominator==1 for u in W for v in W): diffonly+=1
P("Local maxima that are of difference form only (not sum/peak):",diffonly,"  => Argon's 'k/|ui-uj|' term in Ccross never needed; derivation 'ui t-k1 = -(uj t-k2) => t=k/(ui+uj) or k/|ui-uj|' only yields the sum form.")
# ghost statistics: opposite-slope valid branch crossings (sum form) not on envelope
for m in (3,4):
    tot=0;ghost=0;ghostmin=0;ghostzero=0
    for trial in range(300):
        W=rnd_speeds(m,12); T=F(2)
        for i,a in enumerate(W):
            for b in W[i+1:]:
                k=1
                while F(k)/(a+b)<=T:
                    t=F(k)/(a+b)
                    for (aa,bb) in ((a,b),(b,a)):
                        pp=math.floor(bb*t)
                        for p in (pp,pp-1):
                            q=k-p; v1=bb*t-p; v2=q-aa*t
                            if 0<v1<=F(1,2) and v1==v2:
                                tot+=1
                                if g(W,t)<v1:
                                    ghost+=1
                                    if g(W,t)==0: ghostzero+=1
                                    if is_locmin(W,t): ghostmin+=1
                    k+=1
    P("m=%d integer speeds: opposite-slope valid crossings"%m,tot,"ghost (not on envelope)",ghost,"=%.1f%%"%(100*ghost/tot),"; ghosts that are g=0",ghostzero,"; ghosts that are local minima",ghostmin,"=%.1f%% of ghosts"%(100*ghostmin/max(ghost,1)))
# complexity count |C ∩ [0,1]|
for m in (3,5,8):
    for mx in (10,20,40):
        W=sorted(random.sample(range(1,mx+1),m)); W=[F(x) for x in W]
        C=set()
        for a in W:
            for k in range(0,a.numerator*2+2):
                if F(2*k+1,2*a)<=1: C.add(F(2*k+1,2*a))
        for i,a in enumerate(W):
            for b in W[i+1:]:
                for den in (a+b,b-a):
                    for k in range(1,int(den)+1): C.add(F(k)/den)
        P("|C∩[0,1]| m=%d max=%d : %d ; m^2*max=%d"%(m,mx,len(C),m*m*mx))
# Argon: t=1/5 true peak etc in concrete. Also: does enumeration beat? check m=2 Opus F no enumeration (contradicts Q2 'DISPROVED' as generic)
bad=0
for trial in range(2000):
    u,v=sorted(rnd_speeds(2,30,rat=True)); c=math.ceil((u+v)/(3*u)); 
    if g([u,v],F(c)/(u+v))<F(1,3): bad+=1
P("For |V|=2 explicit enumeration-free success time exists (Opus F): failures",bad,"/2000 -- so Argon's blanket 'Q2 DISPROVED' is not supported at m=2 (Argon's claim concerns general F(V) via critical-time selection only)")
open("argon_out.txt","w").write("\n".join(out))
