import random, math
from fractions import Fraction as F
random.seed(7)
nd=lambda x: abs(x-math.floor(x+F(1,2)))
def dist(u,t): return min(nd(x*t) for x in u)
L=[]; p=lambda *x: L.append(' '.join(map(str,x)))
def inreg(a,c,d,closed):
    if not c<4*a: return False
    lo=max(4*a,(5*c-2*a)/2); hi=min(9*a,4*c)
    return (lo<=d<=hi) if closed else (lo<d<hi)
tot=fail=0; endp=0; fails=[]; empty=0
for _ in range(400000):
    a=F(random.randint(1,30),random.choice([1,2,3])); 
    b=a+F(random.randint(1,300),random.choice([1,2,3,7]))
    c=b+F(random.randint(1,300),random.choice([1,2,3,7]))
    if not c<4*a: continue
    lo=max(4*a,(5*c-2*a)/2); hi=min(9*a,4*c)
    if lo>hi: empty+=1; continue
    # candidate d: random, plus endpoints
    for d in (lo,hi,lo+(hi-lo)*F(random.randint(0,1000),1000)):
        if d<=c: continue
        if not inreg(a,c,d,True): continue
        tot+=1; endp+= d in (lo,hi)
        t=2/(a+d)
        if dist((a,b,c,d),t)<F(1,5): fail+=1; fails.append((a,b,c,d,'open' if lo<d<hi else 'endpoint'))
p(f"Qwen B claim t=2/(a+d): {tot} exact points (closed region, {endp} at endpoints) failures {fail}", fails[:5])
# examples
for u,tt in (((3,5,10,25),F(1,14)),((3,5,10,27),None),((3,5,10,22),None),((1,3,4,5),F(4,9))):
    a,b,c,d=map(F,u); t=2/(a+d)
    p(f"{u}: t=2/(a+d)={t} dists={[str(nd(x*t)) for x in (a,b,c,d)]} min={dist((a,b,c,d),t)}; t matches claim: {tt is None or t==tt}; in open region {inreg(a,c,d,False)} closed {inreg(a,c,d,True)}; c<4a {c<4*a}")
a,b,c,d=map(F,(3,5,10,25)); s=(b+c)/a;r=c/b;w=d/(b+c)
p("(3,5,10,25) coverage: TN d<=4a",d<=4*a,"| LN d>=4c",d>=4*c,"| K5 c<=8a/3",c<=8*a/3,"| WL needs d>=",2*a*c/(4*a-c),d>=2*a*c/(4*a-c),"| HB r=",r,(1<r<=F(8,7) or 4<=r<=F(13,2)) and F(15,8)<=s<=F(15,2) and F(4,5)<=w<=F(6,5),"s,w",s,w,"| C1 r>8/7",r>F(8,7))
# s7
ok=True; 
for _ in range(100000):
    a=F(random.randint(1,50)); c=a*(F(1)+F(random.randint(1,3000),1000))
    if not c<4*a: continue
    bound=2*a*c/(4*a-c)
    if (bound<=9*a)!=(c<=F(36,11)*a): ok=False
    if F(36,11)*a<c<4*a and not bound>9*a: ok=False
p("§7: WL bound 2ac/(4a-c)<=9a iff c<=36a/11 (random exact):",ok,"; for 36a/11<c<4a bound>9a>=d so outside WL")
# region nonempty for c>36a/11?
a=F(1); c=F(37,10); lo=max(4*a,(5*c-2*a)/2); hi=min(9*a,4*c); p("a=1,c=3.7: d range",lo,hi,"nonempty",lo<hi)
open('chk_qwenB_out.txt','w').write('\n'.join(L)+'\n'); print('\n'.join(L))
