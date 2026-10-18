# PT-008 R009 Puck exact-Fraction check (no floats). Puck, 2026-10-18.
from fractions import Fraction as F
from math import floor, ceil
import itertools
def d(x): x=x-floor(x); return min(x,1-x)
fails=[]; n_checks=0
def chk(name,cond):
    global n_checks; n_checks+=1
    if not cond: fails.append(name)
grid=[F(p,q) for q in range(1,13) for p in range(q,12*q+1)]
# Track D: n-runner lemma b<=(n-1)a, t=1/(a+b): all v in [a,b] get >=1/n
for n in range(2,9):
  for a in [F(1),F(3,2),F(7,3)]:
    for bb in [a, a*(n-1), (a+a*(n-1))/2]:
      t=1/(a+bb)
      for j in range(0,41):
        v=a+(bb-a)*F(j,40)
        chk(f"D n={n} a={a} b={bb} v={v}", d(v*t)>=F(1,n))
# Qwen Region 1: z<=4, t=1/(1+z)
for z in [F(k,7) for k in range(8,29)]:
  t=1/(1+z)
  for x in [1+(z-1)*F(j,9) for j in range(1,9)]:
    for y in [x+(z-x)*F(j,5) for j in range(1,5)]:
      chk(f"Q1 {x},{y},{z}", min(d(t),d(x*t),d(y*t),d(z*t))>=F(1,5))
# Qwen Region 2: 1<x<5/2, x<y<z<5-x, t=1/(x+z); also verify it lies inside Region 1 (z<4)
sub=True
for x in [1+F(3,2)*F(j,12) for j in range(1,12)]:
  for z in [x+(5-2*x)*F(j,10) for j in range(1,10)]:
    if z>=4: sub=False
    t=1/(x+z)
    for y in [x+(z-x)*F(j,6) for j in range(1,6)]:
      chk(f"Q2 {x},{y},{z}", min(d(t),d(x*t),d(y*t),d(z*t))>=F(1,5))
chk("Q2 subset of Q1 (z<5-x<4)", sub)
# Qwen candidate Region 3: 4<z<=9, t=2/(1+z), x,y outside open (2(1+z)/5,3(1+z)/5)
for z in [4+F(5,1)*F(j,10) for j in range(1,11)]:
  t=2/(1+z); lo,hi=2*(1+z)/5,3*(1+z)/5
  xs=[1+(z-1)*F(j,30) for j in range(1,30)]+[lo,hi]
  for x in xs:
    if 1<x<z:
      bad = lo<x<hi
      chk(f"Q3 iff x={x} z={z}", (d(x*t)>=F(1,5))==(not bad))
  chk(f"Q3 z={z} ref&z", d(t)>=F(1,5) and d(z*t)>=F(1,5))
# Qwen Sec.4 IDEA numerics: forbidden band width & period for x with k=ceil((1+z)/5)
z=F(24); k=ceil((1+z)/5); t=F(k)/(1+z)
xs=[1+(z-1)*F(j,2300) for j in range(1,2300)]
badfrac=F(sum(1 for x in xs if d(x*t)<F(1,5)),len(xs))
q_sec4=(k, t, badfrac)   # Qwen claimed width ~2/5, bad ~8%
# Qwen Sec.5 layer claim: k=ceil((1+z)/5)=k iff 5k-6<z<=5k-1 (Qwen wrote (5k-1,5k+4])
layer_ok=all(ceil((1+z)/5)==k for k in range(2,6) for z in [5*k-6+F(1,3),5*k-1])
layer_qwen=all(ceil((1+z)/5)==k for k in range(2,6) for z in [5*k-1+F(1,3),5*k+4])
chk("layer formula 5k-6<z<=5k-1", layer_ok)
# Argon CE1 (1,2,3,5)
v=[1,2,3,5]
chk("A1 t=k/5 kills d", all(d(F(5*k,5))==0 for k in range(5)))
chk("A1 t=k/6 all fail", all(min(d(x*F(k,6)) for x in v)<F(1,5) for k in range(6)))
chk("A1 t=1/4 works", min(d(x*F(1,4)) for x in v)>=F(1,5))
a_plus_c_lock = F(1,4)==F(1,1+3)  # t=1/4 is the a+c lock 1/(a+c)
# Argon CE2 (1,2,4,5)
v=[1,2,4,5]
chk("A2 t=1/3 works", min(d(x*F(1,3)) for x in v)>=F(1,5))
t0=F(1,5); chk("A2 t0 phases", [d(x*t0) for x in v]==[F(1,5),F(2,5),F(1,5),0])
for e in [F(j,1000) for j in range(1,100)]:
  chk(f"A2 +eps {e} c fails", d(4*(t0+e))<F(1,5))
for e in [F(j,1000) for j in range(1,400)]:
  chk(f"A2 -eps {e} a fails", d(1*(t0-e))<F(1,5))
# exact local window: smallest working t>1/5 for (1,2,4,5) on grid 1/600
first=min(F(j,600) for j in range(121,600) if min(d(x*F(j,600)) for x in v)>=F(1,5))
print("checks",n_checks,"failures",len(fails)); print(fails[:10])
print("Q2 inside Q1:",sub)
print("Qwen sec4 z=24: k=",q_sec4[0],"t=",q_sec4[1],"bad x fraction=",q_sec4[2],"~",float(q_sec4[2]))
print("layer 5k-6<z<=5k-1 correct:",layer_ok,"; Qwen's (5k-1,5k+4] correct:",layer_qwen)
print("Argon CE1 t=1/4 equals a+c lock 1/(1+3):",a_plus_c_lock)
print("Argon CE2 first working t>1/5 on 1/600 grid:",first)
