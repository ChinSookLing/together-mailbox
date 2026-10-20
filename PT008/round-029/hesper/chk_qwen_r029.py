exec(open('/workspace/work/pt008r20/hesper/base.py').read().split('A=lambda')[0])
import random; random.seed(29002)
f5=F(1,5)
def ok(V,t): return 0<t<1/V[0] and min(nd(v*t) for v in V)>=f5
def cands(V):
    a,b,c,d=V
    return [F4(a,b,c),F4(a,b,d),F4(a,c,d),F4(b,c,d)]
# reduction counterexample: ||x|| vs x
print('x=9/10: ||x||=',nd(F(9,10)))
n=t4=t4k=0; first=[];fails=[]; bcdx=0
for a in range(1,25):
 for b in range(a+1,25):
  for c in range(b+1,25):
   for d in range(c+1,25):
    if not(d>4*a and d<4*c): continue
    V=(a,b,c,d); n+=1; cs=cands(V)
    tb=cs[3]
    if a*tb>F(4,5): bcdx+=1
    if any(ok(V,t) for t in cs): t4+=1
    if any(ok(V,t) for t in cs+[F(k,5*a) for k in range(1,5)]): t4k+=1
    else: fails.append(V)
print('int<=24 region',n,'4 T4 cands cover',t4,'| +k/(5a) cover',t4k,'uncovered',len(fails),fails[:5])
print('quads with a*T4(b,c,d)>4/5 (x in (4/5,1)):',bcdx)
def rnd(): return F(random.randint(1,10**4),random.randint(1,300))
m=u=0; ex=[]
while m<20000:
    V=sorted({rnd() for _ in range(4)})
    if len(V)<4: continue
    a,b,c,d=V
    if not(d>4*a and d<4*c): continue
    m+=1
    if not any(ok(V,t) for t in cands(V)+[F(k,5*a) for k in range(1,5)]): u+=1; ex.append(V)
print('random rational in region',m,'selector uncovered',u,[tuple(str(x) for x in e) for e in ex[:2]])
