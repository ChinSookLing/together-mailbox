from common import *
random.seed(8)
out=[]
def P(*a):
    s=" ".join(str(x) for x in a); print(s); out.append(s)
# Q-A: T1 classification: every local max is type A (peak, g=1/2) or type C (t=(k+l+1)/(u+v) w/ ||ut||=||vt||=g)
bad=0; tot=0
for trial in range(400):
    V=rnd_speeds(random.randint(2,5),12,rat=(trial%2==1)); T=F(3)
    for t in locmaxes(V,T):
        tot+=1
        isA=any(t==F(2*k+1)/(2*u) for u in V for k in range(0,200)) and g(V,t)==F(1,2)
        isC=any(((t*(u+v)).denominator==1 and nd(u*t)==nd(v*t)==g(V,t)) for u in V for v in V if u!=v)
        if not(isA or isC): bad+=1; P("  A/C classification fails",V,t)
P("Q1 completeness (every local max is A or C form): maxima tested",tot,"failures",bad)
# converse as literally stated: t=(k+l+1)/(u+v) integer-sum, ||ut||=||vt||=g(t)  => local max ?
cnt=0;nm=0;ex=None
for trial in range(400):
    V=rnd_speeds(random.randint(2,5),12,rat=(trial%2==1)); T=F(3)
    for i,u in enumerate(V):
        for v in V[i+1:]:
            k=1
            while F(k)/(u+v)<=T:
                t=F(k)/(u+v)
                if nd(u*t)==nd(v*t)==g(V,t) and g(V,t)>0:
                    cnt+=1
                    if not is_locmax(V,t): nm+=1; ex=ex or (V,t)
                k+=1
P("Q1 converse as literally stated (on-envelope sum-crossing => local max): cases",cnt,"not local max",nm,"example",ex)
# does Opus T1' (with branch-type condition) agree: local maxima == sum-form points with up/down branch check & on envelope
dis=0;tot=0
for trial in range(300):
    V=rnd_speeds(random.randint(2,5),12,rat=(trial%2==1)); T=F(3)
    L=set(locmaxes(V,T)); O=set()
    for i,a in enumerate(V):
        for b in V[i:]:
            k=1
            while F(k)/(a+b)<=T:
                t=F(k)/(a+b)
                # exists p,q with b t-p in (0,1/2], q-a t in (0,1/2] , equal, on envelope
                for (aa,bb) in ((a,b),(b,a)):
                    p=math.floor(bb*t); 
                    for pp in (p,p-1):
                        q=k-pp; v1=bb*t-pp; v2=q-aa*t
                        if 0<v1<=F(1,2) and 0<v2<=F(1,2) and v1==v2 and all(nd(e*t)>=v1 for e in V): O.add(t)
                k+=1
    tot+=1
    if L!=O: dis+=1
P("Opus T1' set vs brute-force local-max set: V sets",tot,"disagreements",dis)
# Q2 two-speed theorem
bad=0; firstbad=0; multi=0; tot=0; ex=None
for trial in range(600):
    u,v=sorted(rnd_speeds(2,15,rat=(trial%2==1)))
    V=[u,v]; T=1/(2*u)
    lm=locmaxes(V,T)
    tot+=1
    if not lm or lm[0]!=1/(u+v) or g(V,lm[0])!=u/(u+v): firstbad+=1
    # theorem: unique max on [0,1/(2u)] at t*=1/(u+v)
    best=max([g(V,t) for t in all_candidates(V,T)]+[g(V,T)])
    if len(lm)>1 or best!=u/(u+v):
        bad+=1; ex=ex or (u,v,[str(x) for x in lm[:4]],best)
        if v<=2*u: multi+=1
P("Two-speed: FIRST local max =1/(u+v), value u/(u+v): pairs",tot,"failures",firstbad)
P("Two-speed: 'unique max on [0,1/(2u)] at 1/(u+v)' stated theorem: pairs failing",bad,"of",tot,"; of these with v<=2u:",multi,"example (u,v,maxima,true max)",ex)
u,v=F(1),F(10); t=F(1,4); P("Exact counterexample u=1,v=10: t*=1/11 value 1/11 but g(1/4)=",g([u,v],t),">1/11; 1/4 <=1/(2u)=1/2 so max on [0,1/2] is not at t*")
# numeric examples
for (u,v) in ((2,3),(1,3)):
    t=F(1,u+v); P("example",u,v,"t*=",t,"||ut||",nd(u*t),"||vt||",nd(v*t),"g",g([F(u),F(v)],t))
# corollary: g(t*)>=1/3 iff v<=2u
bad=0
for trial in range(2000):
    u,v=sorted(rnd_speeds(2,30,rat=True))
    if (u/(u+v)>=F(1,3))!=(v<=2*u): bad+=1
P("Corollary g(t*)>=1/3 iff v<=2u: failures",bad,"/2000")
# But as success criterion: Opus F always succeeds for n=3
bad=0; tstar_fail=0
for trial in range(2000):
    u,v=sorted(rnd_speeds(2,30,rat=True))
    c=math.ceil((u+v)/(3*u)); t=F(c)/(u+v)
    if g([u,v],t)<F(1,3): bad+=1
    if g([u,v],1/(u+v))<F(1,3): tstar_fail+=1
P("Opus F(a,b) success failures",bad,"/2000;  Qwen t*=1/(u+v) is NOT a success time in",tstar_fail,"/2000 pairs (those with v>2u); Qwen's 'two-speed construction t=1/(u+v)' therefore is not a general success time. (Qwen itself states corollary v<=2u.)")
P("  e.g. {1,3}: Qwen t*=1/4 g=",g([F(1),F(3)],F(1,4)),"<1/3; Opus F(1,3)=1/2 g=",g([F(1),F(3)],F(1,2)))
# Three-speed prop
bad=0;tot=0;lmbad=0
for trial in range(5000):
    u1,u2,u3=sorted(rnd_speeds(3,30,rat=True)); t=1/(u1+u3); tot+=1
    if not nd(u2*t)>u1/(u1+u3): bad+=1
    if not is_locmax([u1,u2,u3],t): lmbad+=1
P("Three-speed prop ||u2 t*||>u1/(u1+u3): trials",tot,"failures",bad,"; t* local max of g_V (stated in note): failures",lmbad)
# 'u1-u2 crossing at 1/(u1+u2) later and higher' - on envelope?
off=0;tot=0;ex=None
for trial in range(5000):
    u1,u2,u3=sorted(rnd_speeds(3,30,rat=True)); t=1/(u1+u2); tot+=1
    if not is_locmax([u1,u2,u3],t): off+=1; ex=ex or (u1,u2,u3)
P("Note claim: u1-u2 crossing t=1/(u1+u2) is later+higher than 1/(u1+u3) -- numerically later/higher yes, but NOT a local max of g_V (killed by u3) in",off,"/",tot,"triples; e.g.",ex, "(Qwen's text omits the on-envelope caveat; it does say 'not necessarily global optimum')")
# Section D conjecture (UNFINISHED by Qwen): for |V|=3 local maxima on [0,1/u1] are exactly 1/(ui+uj) on envelope, max by smallest two speeds
viol=0;tot=0;ex=None
for trial in range(1500):
    V=rnd_speeds(3,12,rat=False); T=1/V[0]; tot+=1
    lm=locmaxes(V,T)
    S={1/(a+b) for a in V for b in V if a<b}
    if any(t not in S for t in lm): viol+=1; ex=ex or (V,[str(x) for x in lm if x not in S][:3])
P("Qwen UNFINISHED conjecture (maxima on [0,1/u1] are only 1/(ui+uj) types): violated in",viol,"/",tot,"integer triples; example",ex)
open("qwen_out.txt","w").write("\n".join(out))
