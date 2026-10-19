from fractions import Fraction as F
from math import floor, ceil
def nd(z): return min(z-floor(z), floor(z)+1-z)
d5=F(1,5)
def ok(V,t): return min(nd(u*t) for u in V)>=d5
th,w=F(1,3),F(8,9)
# Qwen v1 rule: k0=ceil(S/(5a)), search k0..k0+q-1, q=3 (period of theta)
fails=[]
for S in range(20,400):
    a=F(1);b=th*S;c=S-b;d=w*S;V=(a,b,c,d)
    k0=ceil(F(S,5)); got=[k for k in range(k0,k0+3) if ok(V,F(k)/S)]
    if not got: fails.append((S,k0,k0%9))
print('V4-shape S=20..399, 3-step window fails:',len(fails),'first',fails[:5])
print('all fails have k0%9==8:',all(f[2]==8 for f in fails))
S=130;V=(F(1),F(130,3),F(260,3),F(1040,9));print('example (1,130/3,260/3,1040/9) solvable t?', next((F(k,130) for k in range(1,200) if ok(V,F(k,130))),None))
# d range for V4, k=20
for d in [F(774,10),F(801,10),F(773,10),F(802,10)]:
    print('d',d,'ok t=2/9',ok((F(1),F(30),F(60),d),F(2,9)))
print('LE-1 example (1,2,3,4) t=1/4',[str(nd(F(u,4))) for u in (1,2,3,4)])
