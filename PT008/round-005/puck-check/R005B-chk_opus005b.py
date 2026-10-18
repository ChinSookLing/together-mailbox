# Exact-Fraction checks of Opus PT-008 R005B reply. Fractions only for pass/fail. CHECKED != PROVED.
import random, math, sys
from fractions import Fraction as Fr
from math import floor, ceil, gcd
Q=Fr(1,4)
def nd(x):
    r=x-floor(x); return min(r,1-r)
def g(t,a,b,c): return min(nd(a*t),nd(b*t),nd(c*t))
def good(t,*v): return all(nd(u*t)>=Q for u in v)
def cl(x): return ceil(x)
def PC(p,q):
    k=cl(Fr(p+q)/(4*p)); return k,Fr(k)/(p+q)
def F(a,b): return Fr(cl(Fr(a+b)/(3*a)))/(a+b)
def nudge_near(t0,c):
    # nearest point at distance>=1/4 for c (boundary), either direction, t>=0
    if nd(c*t0)>=Q: return t0
    m=round(c*t0); cands=[(m+Q)/c,(m-Q)/c]
    cands=[x for x in cands if x>=0]
    return min(cands,key=lambda x:abs(x-t0))
def nudge_fwd(t0,c):
    if nd(c*t0)>=Q: return t0
    return (cl(c*t0-Q)+Q)/c
def R1(a,b,c):
    if not c>=3*b: return None
    return nudge_near(F(a,b),c)
def R2(a,b,c):
    if not b>=3*a: return None
    k=cl(Fr(b)/(4*a)-Q); L=c*(k+Q)/b
    X=L if nd(L)>=Q else cl(L-Q)+Q
    return X/c, k, L, X
def R3(a,b,c):
    k,t=PC(a,c); return t if nd(b*t)>=Q else None
def R4(a,b,c):
    return Fr(1,a+b) if nd(c*Fr(1,a+b))>=Q else None
def F4(a,b,c):
    if c>=3*b: return 'R1',R1(a,b,c)
    if b>=3*a: return 'R2',R2(a,b,c)[0]
    t=R3(a,b,c)
    if t is not None: return 'R3',t
    t=R4(a,b,c)
    if t is not None: return 'R4',t
    return None,None
def solvable(a,b,c):
    # exact: safe set closed, comps start at (m+1/4)/u. Integer speeds only.
    gg=gcd(gcd(a,b),c); per=Fr(1,gg)
    for u in (a,b,c):
        m=0
        while True:
            t=(m+Q)/u
            if t>per: break
            if good(t,a,b,c): return t
            m+=1
    return None
def solvableQ(a,b,c):  # rational speeds: scale to ints
    L=1
    for x in (a,b,c): L=L*x.denominator//gcd(L,x.denominator)
    A,B,C=(int(x*L) for x in (a,b,c)); t=solvable(A,B,C)
    return None if t is None else t*L
out=[]
def P(*s):
    line=' '.join(str(x) for x in s); print(line); out.append(line)
N=int(sys.argv[1]) if len(sys.argv)>1 else 40
random.seed(5)
def triples(N):
    for a in range(1,N+1):
        for b in range(a+1,N+1):
            for c in range(b+1,N+1): yield a,b,c
def rrat(wide=True):
    # wide ratio log-uniform rationals
    return Fr(random.randint(1,60),random.randint(1,60))*Fr(10)**random.randint(-1,2) if False else Fr(random.randint(1,400),random.randint(1,40))
def rtriple():
    while True:
        sc=Fr(10)**random.randint(-2,3)
        v=sorted({Fr(random.randint(1,500),random.randint(1,50))*(sc if random.random()<.5 else 1) for _ in range(3)})
        if len(v)==3: return tuple(v)
nrand=int(sys.argv[2]) if len(sys.argv)>2 else 20000
IT=list(triples(N)); RT=[rtriple() for _ in range(nrand)]
P(f"integer triples 0<a<b<c<={N}: {len(IT)}; random rational triples: {len(RT)}")

# Lemma PC
bad=0;n=0;viol=[]
for p in range(1,61):
  for q in range(p+1,121):
    k,t=PC(p,q); n+=1
    if not (nd(p*t)==nd(q*t) and Q<=nd(p*t)<Fr(1,2)): bad+=1; viol.append((p,q))
for _ in range(nrand):
    p,q=sorted([Fr(random.randint(1,999),random.randint(1,99)) for _ in range(2)])
    if p==q: continue
    k,t=PC(p,q); n+=1
    if not (nd(p*t)==nd(q*t) and Q<=nd(p*t)<Fr(1,2)): bad+=1; viol.append((p,q))
P(f"[PC] Pair-Ceiling: pairs tested {n}, violations {bad} {viol[:3]}  -> {'CHECKED' if not bad else 'VIOLATED'}")

# F with threshold 1/3 (Round 004 B5, used by R1)
bad=0;n=0
for a in range(1,81):
  for b in range(a+1,161):
    t=F(a,b);n+=1
    if nd(a*t)<Fr(1,3) or nd(b*t)<Fr(1,3): bad+=1
for _ in range(nrand):
    a,b=sorted([Fr(random.randint(1,999),random.randint(1,99)) for _ in range(2)])
    if a==b: continue
    t=F(a,b);n+=1
    if nd(a*t)<Fr(1,3) or nd(b*t)<Fr(1,3): bad+=1
P(f"[F-1/3] F(a,b)=ceil((a+b)/3a)/(a+b) gives ||at||,||bt||>=1/3: tested {n}, violations {bad} -> {'CHECKED' if not bad else 'VIOLATED'}")
P(f"   F(1,2)={F(1,2)} F(1,3)={F(1,3)} F(2,3)={F(2,3)} F(1,4)={F(1,4)}")

def run_rule(name,fn,cond,sets,label):
    tot=0;app=0;viol=[]
    for (a,b,c) in sets:
        tot+=1
        if not cond(a,b,c): continue
        app+=1
        r=fn(a,b,c)
        t=r[0] if isinstance(r,tuple) else r
        if t is None or t<0 or not good(t,a,b,c): viol.append((a,b,c,t))
    return tot,app,viol
# R1
for label,S in (('int',IT),('rat',RT)):
    tot,app,v=run_rule('R1',R1,lambda a,b,c:c>=3*b,S,label)
    P(f"[R1/{label}] c>=3b applies {app}/{tot} ({100*app/tot:.1f}%), violations (nearest-boundary nudge) {len(v)} {v[:2]} -> {'CHECKED' if not v else 'VIOLATED'}")
    # nudge distance claims
    far=0;fwdfar=0;fwdfail=0
    for (a,b,c) in S:
        if c<3*b: continue
        t0=F(a,b);h=1/(12*Fr(b))
        t=nudge_near(t0,c)
        if abs(t-t0)>h: far+=1
        tf=nudge_fwd(t0,c)
        if tf-t0>h: fwdfar+=1
        if not good(tf,a,b,c): fwdfail+=1
    P(f"   nearest nudge farther than h=1/(12b): {far}; forward-only nudge exceeding h: {fwdfar} (of which g<1/4: {fwdfail})")
P(f"   example {{1,2,6}}: F=1/3 ->forward nudge t={nudge_fwd(F(1,2),6)} (claim 3/8), g={g(Fr(3,8),1,2,6)}, dists {nd(Fr(3,8)) ,nd(6*Fr(3,8)),nd(2*Fr(3,8)*0+Fr(18,8))}  (claim ||1*t||,||2t||,||6t||: 3/8,3/4->1/4,1/4 ; note b=2 so ||2t||=||3/4||=1/4, c=6 gives 1/4, and Opus lists '18/8' = 3*(3/8)? ) ")
t=Fr(3,8); P(f"   actual {{1,2,6}} at 3/8: ||t||={nd(t)}, ||2t||={nd(2*t)}, ||6t||={nd(6*t)}, 18/8=3*6/8 is not a runner term (typo: runners are 1,2,6; Opus's listed ||18/8|| is spurious but value 1/4 true for 6t=9/4)")
# R2
for label,S in (('int',IT),('rat',RT)):
    tot,app,v=run_rule('R2',R2,lambda a,b,c:b>=3*a,S,label)
    sub=0;ksub=0;lenfail=0;kneg=0
    for (a,b,c) in S:
        if b<3*a: continue
        t,k,L,X=R2(a,b,c)
        J=(Fr(1,4)/a,Fr(3,4)/a); I=((k+Q)/b,(k+Fr(3,4))/b)
        if not(J[0]<=I[0] and I[1]<=J[1]): sub+=1
        if not(I[0]<=t<=I[1]): ksub+=1
        if k<1: kneg+=1
    P(f"[R2/{label}] b>=3a applies {app}/{tot} ({100*app/tot:.1f}%), violations {len(v)} {v[:2]}; I not subset J: {sub}; t not in I: {ksub}; k<1: {kneg} -> {'CHECKED' if not v and not sub and not ksub else 'VIOLATED'}")
r=R2(1,3,10); P(f"   example {{1,3,10}}: k={r[1]}, I=[{(r[1]+Q)/3},{(r[1]+Fr(3,4))/3}] L={r[2]}, ||L||={nd(r[2])}, X={r[3]} t={r[0]}={float(r[0])}; ||t||={nd(r[0])},||3t||={nd(3*r[0])},||10t||={nd(10*r[0])} (claim .425,.275,.25)")
# R3, R4 standalone
for label,S in (('int',IT),('rat',RT)):
    tot,app,v=run_rule('R3',lambda a,b,c:R3(a,b,c),lambda a,b,c:R3(a,b,c) is not None,S,label)
    P(f"[R3/{label}] condition holds {app}/{tot} ({100*app/tot:.2f}%), violations {len(v)} -> {'CHECKED' if not v else 'VIOLATED'}")
    # c<=3a auto
    n=0;bad=[]
    for (a,b,c) in S:
        if c<=3*a:
            n+=1
            k,t=PC(a,c)
            if k!=1 or t!=Fr(1,a+c) or nd(b*t)<Q or not (Q<b*t<Fr(3,4)) and not (Q<b*t<=Fr(3,4)): bad.append((a,b,c))
    P(f"   [R3 special c<=3a: k=1,t=1/(a+c), automatic] cases {n}, violations {len(bad)} {bad[:2]} -> {'CHECKED' if not bad else 'VIOLATED'}")
    tot,app,v=run_rule('R4',R4,lambda a,b,c:R4(a,b,c) is not None,S,label)
    P(f"[R4 standalone/{label}] cond ||c/(a+b)||>=1/4 holds {app}/{tot}; t=1/(a+b) yields g>=1/4 in {app-len(v)}; FAILS {len(v)} e.g. {v[:2]}")
    vb=[x for x in v if x[1]<=3*x[0]]
    P(f"   of those failures with b<=3a (i.e. reachable in ordered table): {len(vb)}")
    # dense band
    n=0;bad=[]
    for (a,b,c) in S:
        if b<3*a and 3*a<c<3*b:
            n+=1
            band=(Fr(5,4)*(a+b)<=c<=Fr(7,4)*(a+b))
            if band!=(nd(Fr(c)/(a+b))>=Q): bad.append((a,b,c))
    P(f"   [R4 dense-region band 5(a+b)/4<=c<=7(a+b)/4 iff cond] in D: {n}, mismatches {len(bad)} {bad[:2]} -> {'CHECKED' if not bad else 'VIOLATED'}")
# B5
for label,S in (('int',IT),('rat',RT)):
    n=0;bad=[]
    for (a,b,c) in S:
        if b<3*a and 3*a<c<3*b:
            n+=1
            k,t=PC(b,c)
            if k!=1 or nd(a*t)>=Q: bad.append((a,b,c))
    P(f"[B5/{label}] D: k_bc=1 and ||a t||<1/4 at t=1/(b+c): D size {n}, violations {len(bad)} {bad[:2]} -> {'CHECKED' if not bad else 'VIOLATED'}")
# whole F4 coverage
for label,S in (('int',IT),('rat',RT)):
    cnt={};viol=[];unc=[];uncsolv=0;uncunsolv=[]
    for (a,b,c) in S:
        r,t=F4(a,b,c)
        cnt[r]=cnt.get(r,0)+1
        if r is None:
            unc.append((a,b,c))
        elif t is None or t<0 or not good(t,a,b,c): viol.append((r,a,b,c,t))
    tot=len(S)
    P(f"[F4 ordered table/{label}] total {tot}: "+', '.join(f"{k}:{v} ({100*v/tot:.1f}%)" for k,v in sorted(cnt.items(),key=lambda x:str(x[0]))))
    P(f"   violations (outputs with g<1/4): {len(viol)} {viol[:3]} -> {'CHECKED' if not viol else 'VIOLATED'}; uncovered {len(unc)} ({100*len(unc)/tot:.1f}%)")
    if label=='int':
        ns=[u for u in unc if solvable(*u) is None]
        P(f"   uncovered triples with NO safe time at all: {len(ns)} {ns[:3]}")
        P(f"   all triples have a safe time? failures: {sum(1 for u in IT if solvable(*u) is None)}")
        gc=[(a,b,c) for (a,b,c) in unc if gcd(gcd(a,b),c)==1]
        P(f"   uncovered primitive triples: {len(gc)}; smallest few {unc[:8]}")
# C1
P("[C1] {1,2,3}:", {p:(nd(p[0]*F(*p)),nd(p[1]*F(*p)) ) for p in ((1,2),(1,3),(2,3))})
for (p,q,third) in ((1,2,3),(1,3,2),(2,3,1)):
    t=F(p,q); P(f"   F{(p,q)}={t}; ||{p}t||={nd(p*t)} ||{q}t||={nd(q*t)} ||{third}t||={nd(third*t)}; g={g(t,1,2,3)}  fails 1/4: {g(t,1,2,3)<Q}")
t=Fr(1,4); P(f"   R3 t=1/4: ||t||={nd(t)} ||2t||={nd(2*t)} ||3t||={nd(3*t)} g={g(t,1,2,3)}")
# also with true PC (delta=1/4) pairings, 3-runner optimum-ish
for (p,q) in ((1,2),(1,3),(2,3)):
    k,t=PC(p,q); P(f"   PC{(p,q)} t={t}: g(1,2,3)={g(t,1,2,3)}")
# "all three pairings fail on every tight/all triples"? count how many integer triples where no PC pairing (3 pairs, k0 only) works
cnt=0
for (a,b,c) in IT:
    ok=any(good(PC(p,q)[1],a,b,c) for (p,q) in ((a,b),(a,c),(b,c)))
    cnt+= (not ok)
P(f"   integer triples where no k0 PC pairing (3 pairs) works: {cnt}/{len(IT)} ({100*cnt/len(IT):.1f}%)")
# Q2 claim: in D, (a,c) or (a,b) pairing; fastest with slowest: R3 or R4 at k0
n=0;miss=0
for (a,b,c) in IT:
    if b<3*a and 3*a<c<3*b:
        n+=1
        if not (R3(a,b,c) is not None or R4(a,b,c) is not None): miss+=1
P(f"[Q2 in D] 'fastest pairs with slowest (R3) or (a,b) (R4)' fails in {miss}/{n} D-triples (not claimed to be complete)")
# C2
a,b,c=2,4,7
P("[C2] {2,4,7}: R1",c>=3*b,"R2",b>=3*a)
k,t=PC(a,c); P(f"   R3 k={k} t={t} ||4t||={nd(b*t)} fails={nd(b*t)<Q}")
t=Fr(1,6); P(f"   R4 t=1/6: ||7/6||={nd(c*t)} ||2/6||={nd(a*t)} ||4/6||={nd(b*t)}; g={g(t,a,b,c)}")
t=Fr(2,11); P(f"   t=2/11: ||4/11||={nd(a*t)}? (a=2 -> 4/11) {nd(a*t)}, b=4 -> 8/11: {nd(b*t)}, c=7 -> 14/11: {nd(c*t)}; g={g(t,a,b,c)}>=1/4: {g(t,a,b,c)>=Q}; PC(4,7)={PC(4,7)}; solvable t*={solvable(2,4,7)}")
# C3 grid
Ng=245; tot=0;u1=0;u2=0;u3=0;ex=None
def ge(p,q): r=p%q; return 4*r>=q and 4*r<=3*q
def pair_ok(p,q,others,ks):
    for k in ks:
        # t=k/(p+q) -> ||p t||>=1/4 and others
        if ge(p*k,p+q) and all(ge(o*k,p+q) for o in others): return True
    return False
a=Ng
for b in range(Ng+1,3*Ng):
    for c in range(3*a+1,3*b):
        tot+=1
        k0ac=-(-(a+c)//(4*a)); k0ab=-(-(a+b)//(4*a)); k0bc=-(-(b+c)//(4*b))
        s1=pair_ok(a,c,[b],[k0ac]) or pair_ok(a,b,[c],[k0ab])
        s2=s1 or pair_ok(a,c,[b],[k0ac+1]) or pair_ok(a,b,[c],[k0ab+1])
        s3=s2 or pair_ok(b,c,[a],[k0bc,k0bc+1])
        if not s1:u1+=1
        if not s2:
            u2+=1
            if ex is None and b*100>=234*a and c*100>=300*a: ex=(a,b,c)
        if not s3:u3+=1
P(f"[C3] grid a={Ng}, b in (a,3a), 3a<c<3b (D): {tot} points. uncovered by R3∪R4 (k0): {u1} ({100*u1/tot:.1f}%) [claim ~24%]; by pairings (a,c),(a,b) with k0,k0+1: {u2} ({100*u2/tot:.1f}%) [claim ~3%]; adding (b,c) k0,k0+1: {u3} ({100*u3/tot:.2f}%)")
P(f"   an uncovered point near x=2.34,y=3.01 (k0,k0+1 on (a,c),(a,b)): {ex}")
# is x=2.34,y=3.01 even solvable? scale a=100 b=234 c=301
P(f"   (100,234,301) solvable t={solvable(100,234,301)}; F4 {F4(100,234,301)}")
# Pair-ceiling uncovered region globally solvable fraction (int triples)
open('output.txt','w').write('\n'.join(out)+'\n')
