src=open('/workspace/work/pt008r20/hesper/base.py').read(); exec(src[:src.index("A=lambda")])
exec(open('/workspace/work/pt008r28/hesper/chk_fw3_t4.py').read().split('from collections')[0].split('import itertools')[1])
import random, itertools
random.seed(28028)
def br2(a,b,c):
    k=br(a,b,c)
    if k.startswith('B2'):
        a,b,c=map(F,(a,b,c)); t0=F3(a,b); return 'B2a' if nd(c*t0)>=F(1,4) else 'B2b'
    return k
bound={'B1 c<=3a':F(1,4),'B2a':F(5,6),'B2b':F(11,12),'B3 b>=3a':F(3,4),'B4 3/(b+c)':F(3,4),'B5 2/(b+c)':F(1,2),'B6 4/(b+c)':F(3,4),'B7 5/(b+c)':F(3,4),'B8 3/(a+c)':F(3,4)}
mx={};viol=0;unsafe=0;cnt={}
for it in range(80000):
    xs=sorted({F(random.randint(1,10**4),random.randint(1,300)) for _ in range(3)})
    if len(xs)<3: continue
    a,b,c=xs; t=F4(a,b,c); k=br2(a,b,c); at=a*t; cnt[k]=cnt.get(k,0)+1
    if min(nd(v*t) for v in xs)<F(1,4): unsafe+=1
    ok=(at<=bound[k]) if k in('B1 c<=3a','B6 4/(b+c)','B7 5/(b+c)') else (at<bound[k])
    if not ok or t<=0: viol+=1
    mx[k]=max(mx.get(k,0),at)
print('random rational triples',sum(cnt.values()),'unsafe',unsafe,'bound violations',viol)
for k in sorted(cnt): print(k,cnt[k],'max a*t',float(mx[k]),'claimed',bound[k])
# PS example
V=(F(1),F(4,3),F(2),F(4)); t0=F4(*V[1:]); print('t0',t0,br(*V[1:]))
t=t0+F(3,2); print('PS t',t,[str(nd(v*t)) for v in V])
t=F(1,3); print('t=1/3',[str(nd(v*t)) for v in V])
# skeleton C1 in (0,1]
T=F(1); Cm=[]
for i,j in itertools.combinations(V,2):
    s=i+j; m=1
    while F(m)/s<=T: Cm.append(F(m)/s); m+=1
for v in V:
    m=0
    while F(2*m+1,2*v)<=T: Cm.append(F(2*m+1,2*v)); m+=1
g=lambda t:min(nd(v*t) for v in V)
C=sorted(set(Cm)); best=max(g(x) for x in C); sel=min(x for x in C if g(x)==best)
print('C1 counted',len(Cm),'distinct',len(C),'F^FW',sel,'g',best)
k=4; print('FWS(i) bound', k*sum(V)/V[0]+F(k,2))
