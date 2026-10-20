src=open('/workspace/work/pt008r20/hesper/base.py').read(); exec(src[:src.index("A=lambda")])
import itertools
def br(a,b,c):
    a,b,c=F(a),F(b),F(c); r=c/b; s=(b+c)/a
    if c<=3*a: return 'B1 c<=3a'
    if c>=3*b: return 'B2 c>=3b'
    if b>=3*a: return 'B3 b>=3a'
    if r<=F(7,5): return 'B4 3/(b+c)'
    if r>=F(5,3) and s<=8: return 'B5 2/(b+c)'
    if F(9,7)<=r<=F(11,5) and s>=F(16,3): return 'B6 4/(b+c)'
    if r>=F(13,7) and s>=F(20,3): return 'B7 5/(b+c)'
    return 'B8 3/(a+c)'
from collections import Counter
N=40; tot=Counter(); late=Counter(); ex={}; bad=0
for a,b,c in itertools.combinations(range(1,N+1),3):
    t=F4(a,b,c); k=br(a,b,c); tot[k]+=1
    if min(nd(v*t) for v in (a,b,c))<F(1,4): bad+=1
    if not (0<t<F(1,a)):
        late[k]+=1; ex.setdefault(k,(a,b,c,str(t),str(a*t)))
print('integer triples 1..%d:'%N,sum(tot.values()),'F4 unsafe',bad)
for k in sorted(tot): print(k,'count',tot[k],'t>=1/a',late[k],'example',ex.get(k))
