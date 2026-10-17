from fractions import Fraction as F
import math
def nn(x): x=x-math.floor(x); return min(x,1-x)
V=[F(1),F(2)]; d=F(1,4); w=F(1,3)
def win(t0):
    l=min(((u*t0)%1-d)/u for u in V); r=min((1-d-(u*t0)%1)/u for u in V); return t0-l,t0+r
Wa=win(F(1,3)); Wb=win(F(2,3)); print("Wa",Wa,"Wb",Wb)
for t in [F(1,3),F(2,3),F(3,4),F(5,4)]:
    print(t,[nn(u*t) for u in V+[w]], all(nn(u*t)>=d for u in V+[w]))
ka=round(w*F(1,3)); t1=(ka+d)/w; print("step3 t1",t1, Wb[0]<=t1<=Wb[1])
# scan Wb for safe points
import itertools
N=2400; safe=[Wb[0]+(Wb[1]-Wb[0])*i/N for i in range(N+1) if nn(w*(Wb[0]+(Wb[1]-Wb[0])*F(i,N)))>=d]
print("safe in Wb:",[str(s) for s in safe][:5])
