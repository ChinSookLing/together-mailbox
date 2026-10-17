from fractions import Fraction as F
import random, math
def nd(x): return abs(x-round(x))
def fr(x): return x-math.floor(x)
def rho(V,t,d): return min((nd(abs(u)*t)-d)/abs(u) for u in V)
def K(V,t,d):
    lam=min((fr(abs(u)*t)-d)/abs(u) for u in V); mu=min((1-d-fr(abs(u)*t))/abs(u) for u in V); return t-lam,t+mu
V=[F(1),F(3)]; n=3; d=F(1,4); ta=F(5,11); tb=F(1,2); w=F(1,100)
print("1 old successes (>=1/n):",[ (nd(u*ta)>=F(1,n), nd(u*tb)>=F(1,n)) for u in V], [nd(u*ta) for u in V],[nd(u*tb) for u in V])
print("2 island: K_a",K(V,ta,d),"K_b",K(V,tb,d))
# island by grid
g=[F(i,2520) for i in range(2520) if all(nd(u*F(i,2520))>=d for u in V)]
print("2b grid S_4 intervals (min,max) in [0,1):",g[0],g[-1],[x for x in g if F(5,12)<=x<=F(7,12)][0::1][:1], len(g))
# components
comps=[];s=g[0];p=g[0]
for x in g[1:]:
    if x-p>F(1,2520): comps.append((s,p)); s=x
    p=x
comps.append((s,p)); print("   comps",[(str(a),str(b)) for a,b in comps])
D=tb-ta; print("3 Dt",D)
t3=ta+3*D; print("4 t3",t3,"|t3|",nd(t3),"|3t3|",nd(3*t3),nd(3*t3)<d, nd(3*t3)==F(5,22))
# sequence
for k in range(0,8): t=ta+k*D; print("  k",k,"t",t,"old safe(>=1/4)",all(nd(u*t)>=d for u in V))
first_w=next(k for k in range(10**6) if nd(w*(ta+k*D))>=d); print("5 first k with w safe",first_w)
fo=next(k for k in range(100) if not all(nd(u*(ta+k*D))>=d for u in V)); print("  first k old unsafe",fo)
print("  old safe at first_w?",all(nd(u*(ta+first_w*D))>=d for u in V))
# hypothesis of Two-Window Lemma
ra,rb=rho(V,ta,d),rho(V,tb,d)
lhs=nd(w*(ta-tb)); rhs=2*d-abs(w)*(ra+rb)
print("6 rho",ra,rb,"lhs",float(lhs),"rhs",float(rhs),"hyp holds:",lhs>=rhs)
print("  windows fail:", nd(w*ta)<d-w*ra, nd(w*tb)<d-w*rb, "exact comps fail?",)
for t in (ta,tb):
    L,R=K(V,t,d); A,B=w*L,w*R
    print("   K",L,R,"max nd on K approx",max(nd(w*(L+(R-L)*F(i,1000))) for i in range(1001))<d)
# Is the lemma still ok (random test, V={1,3} and random)
random.seed(1);bad=0;cnt=0
for _ in range(20000):
    m=random.randint(1,3);Vr=[F(random.randint(1,6),random.randint(1,3)) for _ in range(m)];nn=m+1;dd=F(1,nn+1)
    cand=[F(random.randint(1,2000),random.randint(1,40)) for _ in range(300)]
    S=[t for t in cand if all(nd(u*t)>=F(1,nn) for u in Vr)]
    if len(S)<2: continue
    a,b=random.sample(S,2); ww=F(random.randint(1,200),random.randint(1,20))
    ra,rb=rho(Vr,a,dd),rho(Vr,b,dd)
    if nd(ww*(a-b))>=2*dd-ww*(ra+rb):
        cnt+=1
        ok=any(nd(ww*(t))>=dd for t in [a+(ra*s)/100 for s in range(-100,101)]+[b+(rb*s)/100 for s in range(-100,101)])
        if not ok: bad+=1
print("7 lemma hyp-satisfying tests",cnt,"fails",bad)
# Q3: freeze v_i by Dt=1/v
print("8 freeze:", all(nd(F(3)*(ta+k*F(1,3))) == nd(F(3)*ta) for k in range(20)), "but v=1 drifts:",[str(nd(ta+k*F(1,3))) for k in range(4)])
# Q1 general claim: local failure iff max over window < delta; check example w tiny: max on J
print("9 Q1 example max w t on K_a:",float(w*K(V,ta,d)[1]))
