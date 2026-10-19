from fractions import Fraction as F
from math import floor
def nd(z): return min(z-floor(z), floor(z)+1-z)
def safe(u,t): return nd(u*t)>=F(1,5)
def nxt(u,t):  # first time >=t where u safe
    if safe(u,t): return t
    k=floor(u*t+F(1,5)); return (k+F(1,5))/u
def ets(V,cap=200):
    t=F(1,5)/V[0]; steps=0
    while True:
        bad=[u for u in V if not safe(u,t)]
        if not bad: return t,steps
        t=max(nxt(u,t) for u in bad); steps+=1
        if steps>cap: return None,steps
W={'V1':[1,F(11,10),3,F(41,10)],'V4':[1,30,60,80],'QB2pt':[1,2,F(16,5),F(9,2)]}
for k,V in W.items():
    V=[F(x) for x in V]; t,s=ets(V); print(k,t,s,[str(nd(u*t)) for u in V] if t else '')
V=[F(1),F(2),F(16,5),F(9,2)]; t=F(2)/(V[1]+V[2]); print('QB2 t',t,[str(nd(u*t)) for u in V], 'c/b',V[2]/V[1],'(b+c)/a',V[1]+V[2],'d/(b+c)',V[3]/(V[1]+V[2]))
# brute first success check for V4
import itertools
V=[F(x) for x in [1,30,60,80]]
first=next(F(k,30000) for k in range(1,30000) if all(safe(u,F(k,30000)) for u in V)); print('V4 grid first success ~',float(first))
