exec(open('/workspace/work/pt008r20/hesper/base.py').read().split('A=lambda')[0])
import random; random.seed(29001)
fifth=F(1,5)
def ok(V,t): return 0<t<1/V[0] and min(nd(v*t) for v in V)>=fifth
def SO(a,b,c,d): return F4(b,c,d)
def placed(tau,d):
    return tau if nd(d*tau)>=fifth else tau+fr(fifth-d*tau)/d
def R2(a,b,c,d):
    t0=F3(a,b); h=F(2,15)/b; m=ceil(c*(t0-h)-fifth); tau=(m+fifth)/c; return placed(tau,d)
def R2p(a,b,c,d):
    t0=F3(a,b); h=F(2,15)/b; s=t0-h; ph=fr(c*s)
    if ph<=fifth: A=s+(fifth-ph)/c; L=F(3,5)/c
    elif ph>=F(4,5): A=s+(1+fifth-ph)/c; L=F(3,5)/c
    else:
        l1=(F(4,5)-ph)/c; l2=(ph-fifth)/c
        if l1>=l2: A=s; L=l1
        else: A=s+(1+fifth-ph)/c; L=l2
    return placed(A,d)
cnt={'SO':[0,0],'R2':[0,0],'R2p':[0,0]}
def rnd(): return F(random.randint(1,10**4),random.randint(1,300))
for _ in range(40000):
    V=sorted({rnd() for _ in range(4)})
    if len(V)<4: continue
    a,b,c,d=V
    if b<=F(5,4)*a: cnt['SO'][0]+=1; cnt['SO'][1]+= not ok(V,SO(*V))
    if c>=6*b: cnt['R2'][0]+=1; cnt['R2'][1]+= not ok(V,R2(*V))
    if c>=F(15,4)*b and d>=F(4,3)*c: cnt['R2p'][0]+=1; cnt['R2p'][1]+= not ok(V,R2p(*V))
# targeted near-boundary
for _ in range(20000):
    a=F(1); b=a*(1+F(random.randint(1,10**4),10**4)*F(1,4)); c=b*F(15,4)*(1+F(random.randint(0,10**4),10**5)); d=c*F(4,3)*(1+F(random.randint(0,10**4),10**5))
    V=(a,b,c,d); cnt['R2p'][0]+=1; cnt['R2p'][1]+= not ok(V,R2p(*V))
    b2=a*F(5,4)*(1-F(random.randint(0,10**4),10**6)); c2=b2*(1+F(random.randint(1,10**4),10**3)); d2=c2*(1+F(random.randint(1,3*10**4),10**4))
    V=(a,b2,c2,d2); cnt['SO'][0]+=1; cnt['SO'][1]+= not ok(V,SO(*V))
print('random+boundary (applicable, fails):',cnt)
n=s1=s2=s3=rest=0; ex=[]
for a in range(1,25):
 for b in range(a+1,25):
  for c in range(b+1,25):
   for d in range(c+1,25):
    if not(d>4*a and d<4*c): continue
    n+=1; V=(a,b,c,d)
    if 4*b<=5*a and ok(V,SO(*V)): s1+=1; continue
    if c>=6*b and ok(V,R2(*V)): s2+=1; continue
    if any(ok(V,F(k,5*a)) for k in range(1,5)): s3+=1; continue
    rest+=1; ex.append(V)
print('int<=24 region',n,'SO',s1,'R2',s2,'k/(5a)',s3,'uncovered',rest,ex[:3])
# variant: SO output tried without its hypothesis
n=s1=s2=s3=rest=0; s1c=0
for a in range(1,25):
 for b in range(a+1,25):
  for c in range(b+1,25):
   for d in range(c+1,25):
    if not(d>4*a and d<4*c): continue
    V=(a,b,c,d); n+=1
    if 4*b<=5*a: s1c+=1
    if ok(V,SO(*V)): s1+=1; continue
    if c>=6*b and ok(V,R2(*V)): s2+=1; continue
    if any(ok(V,F(k,5*a)) for k in range(1,5)): s3+=1; continue
    rest+=1
print('variant (T4(b,c,d) tried on all):',n,'SO-output works',s1,'R2',s2,'k/(5a)',s3,'uncovered',rest,'| quads meeting b<=5a/4:',s1c)
kk=sum(1 for a in range(1,25) for b in range(a+1,25) for c in range(b+1,25) for d in range(c+1,25) if d>4*a and d<4*c and any(ok((a,b,c,d),F(k,5*a)) for k in range(1,5)))
print('k/(5a) family alone covers',kk)
# hand facts
print('a/b>=4/5 <-> b<=5a/4; R2 8/(5c)<=4/(15b) iff c>=6b:', F(8,5)/6 == F(4,15)); print('R2p 1/c<=4/(15b) iff c>=15b/4; 2/(5d)<=3/(10c) iff d>=4c/3:', F(2,5)/F(4,3)==F(3,10)); print('5/6+2/15=',F(5,6)+F(2,15),' 1/3-2/15=',F(1,3)-F(2,15))
