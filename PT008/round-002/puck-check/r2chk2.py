from fractions import Fraction as F
def nd(x): return abs(x-round(x))
def ok(V,t,th): return all(nd(u*t)>=th for u in V)
# Qwen B1
V=[1,3];t0=F(4,9);n=3;d=F(1,4)
assert ok(V,t0,F(1,3))
H=min((nd(u*t0)-d)/abs(u) for u in V);print("H",H)
lo,hi=t0-H,t0+H;print("window",lo,hi)
print("w=2 any safe in window (dense 5000):",any(nd(2*(lo+(hi-lo)*F(i,5000)))>=d for i in range(5001)))
print("max ||2t|| on window ~", max(nd(2*(lo+(hi-lo)*F(i,5000))) for i in range(5001)))
print("global t=1/4:",ok(V+[2],F(1,4),d))
# Qwen A3 : V={1..n-1}, t1=1/(n+1), integer w not divisible
bad=0;cnt=0
for n in range(2,12):
  V=list(range(1,n));th=F(1,n+1)
  for w in range(-60,61):
    if w==0 or w in V: continue
    t1=F(1,n+1);cnt+=1
    good=ok(V+[w],t1,th)
    if good!=((n+1)%1==0 and w%(n+1)!=0): bad+=1
print("A3 cases",cnt,"mismatch",bad)
# Qwen B2 safe set for {1,3,4}
S=[t for t in (F(i,960) for i in range(0,961)) if ok([1,3,4],t,F(1,4))]
print("safe pts {1,3,4} within [0,1]:",float(min(S)),float(max(S)),len(S)," 5/12 ok?",ok([1,3,4],F(5,12),F(1,4)),"1/2:",ok([1,3,4],F(1,2),F(1,4)))
print("claimed [5/12,7/16] sample 0.42:",ok([1,3,4],F(21,50),F(1,4)),"0.43:",ok([1,3,4],F(43,100),F(1,4)))
# Qwen section C: w=(n+1)q, t1=1/(2(n+1)), q odd, V={1..n-1}
cc=bad2=0
for n in range(2,10):
  for q in (1,3,5):
    V=list(range(1,n));w=(n+1)*q;cc+=1
    if not ok(V+[w],F(1,2*(n+1)),F(1,n+1)): bad2+=1
print("Qwen C claim cases",cc,"fail",bad2)
# Argon
print("Argon V={1},w=.4,window[1/3,2/3]: max||0.4t||",max(nd(F(2,5)*(F(1,3)+F(1,3)*F(i,1000))) for i in range(1001)),"global 3/2:",ok([1,F(2,5)],F(3,2),F(1,3)))
# hopping: u* distance invariant
print("hop invariance",all(nd(3*(F(1,7)+F(k,3)))==nd(3*F(1,7)) for k in range(20)))
