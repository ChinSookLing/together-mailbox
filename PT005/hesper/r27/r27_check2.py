p=17
def cls(N,b): return [t for t in range(1,N//2+1,2) if t%p in(b%p,(-b)%p)]
def covset(w,N,T): return [t for t in T if 16*min(t*w%N,N-t*w%N)<N]
def orep(x):  # odd signed rep in [-15,15] of x mod 17
    x%=17
    for c in range(-15,16,2):
        if c%17==x: return c
def m(c): return (c-(1 if c>0 else -1))//2
def signed(t,b,N): return t if t%17==b%17 else -t   # orient T ≡ b
legal=lambda w: w%2==1 and w%17 not in (0,1,16)
# per-coordinate lemma at k=5 and the analogous sum at k=6,7
for k in (5,6):
  N=17*2**k; M=2**k
  bad=0; tot=0
  for b in (2,3,5):
    T=cls(N,b)
    for w in range(1,N,2):
      if w%17==0: continue
      S=covset(w,N,T)
      if not S: continue
      tot+=1
      s=sum(signed(t,b,N) for t in S)%M
      A=pow(w,-1,M); c=orep(b*w)
      pred=(2**(k-3))*A*m(c)%M
      if s!=pred: bad+=1
  print("k",k,"coords",tot,"lemma sum ≡ 2^(k-3)·A·m(c) mod 2^k fails:",bad)
# full S1 over all exact tilings at k=5, b=2 (legal coords)
import itertools
k=5;N=544;b=2;T=cls(N,b);idx={t:i for i,t in enumerate(T)}
sets={}
for w in range(1,N,2):
  if not legal(w): continue
  S=frozenset(idx[t] for t in covset(w,N,T))
  sets.setdefault(S,set()).add(w)
print("distinct cover pairs",len(sets),"sizes",{len(s) for s in sets})
pairs=list(sets)
def tilings(rem,acc):
  if not rem: yield list(acc);return
  i=min(rem)
  for P in pairs:
    if i in P and P<=rem: yield from tilings(rem-P,acc+[P])
vals={P:{pow(w,-1,32)*m(orep(b*w))%8 for w in ws} for P,ws in sets.items()}
dv={P:{pow(w,-1,32)*m(orep(2*b*w))%8 for w in ws} for P,ws in sets.items()}
print("value const per pair:",all(len(v)==1 for v in vals.values()), "doubled const:",all(len(v)==1 for v in dv.values()))
cnt=0;viol=0;dd=[0]*8
for til in tilings(frozenset(range(16)),[]):
  cnt+=1
  if sum(next(iter(vals[P])) for P in til)%8: viol+=1
  dd[sum(next(iter(dv[P])) for P in til)%8]+=1
print("k5 b2 pair-tilings",cnt,"S1 violations",viol,"doubled dist",dd)
u=(9,29,49,67,73,93,105,125)
print("u mod17",[x%17 for x in u])
print("u doubled terms",[pow(w,-1,32)*m(orep(4*w)) for w in u],sum(pow(w,-1,32)*m(orep(4*w)) for w in u))
a=(53,207,39,59,27,11,63,81); print("Astra mod17",[x%17 for x in a])
