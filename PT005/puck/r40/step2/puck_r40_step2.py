# Puck R40 step 2: why only 5 of 39 affine orbits (640 of 7,168 mixed doublable configs) are realized.
# Own code. Inputs: the two committed tables only. Run from repo root or anywhere.
#
# DERIVATION of the level-5 mask (checked numerically in [0] below):
#  level-5 cell T (odd, T = b mod p, 16 of them mod 32p) <-> slot s with T = b + p*s, s odd/even with s = b+1 (mod 2), s mod 32.
#  For speed w: b*w = m*p + d, |d|<p/2.  T*w = d + p*(m + s*w) (mod 32p). Raw hit: |T*w mod 32p| < 2p
#  <=> m + s*w = j (mod 32) with |d + p*j| < 2p, j in J = {-2,-1,0,1} (d>0) or {-1,0,1,2} (d<0).
#  So slots s = (j - m)*v (mod 32), v = w^-1, and parity forces j = m + b + 1 (mod 2): exactly 2 slots ("domino").
#  With x = -m*v (mod 32): c = 2x (mod 32), so x = h or h+16 where h = c/2 (mod 16) -- the footprint forgets this bit.
#   case A (h = b mod 2, i.e. m = b mod 2): j = +-1   -> domino {x - v, x + v}
#   case B (h != b mod 2):                  j in {0, +-2} -> domino {x, x + 2*eps*v}, eps = -sgn(d) (actual v), free since sgn d is free
#  Exact k=5 tiling <=> the 8 dominoes partition the 16 slots of parity b+1 (mod 32).
#  Projecting mod 16 (each residue mod 16 has 2 lifts mod 32) gives the NECESSARY rule R16 below.
import json, itertools, os, sys
from collections import Counter, defaultdict
ROOT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../..'))
B=os.path.join(ROOT,'hesper/r38/checks/')
def norm(c,v):
    c%=32; v%=32
    return (c,v) if v<16 else (c,32-v)
Dall=set(tuple(sorted(norm(*f) for f in k)) for k in json.load(open(B+'r38_doublable_only.json')))
R=set(tuple(sorted(norm(*f) for f in k)) for k in json.load(open(B+'hesper_U_769.json')))
mixed=lambda k: not (all(v%8 in (1,7) for c,v in k) or all(v%8 in (3,5) for c,v in k))
MD=sorted(k for k in Dall if mixed(k)); NEVER=[k for k in MD if k not in R]
print('[data] mixed doublable',len(MD),'REAL',len(R),'NEVER',len(NEVER),'REAL subset',R<=set(MD))

def hit(t,w,M): r=t*w%M; return 16*min(r,M-r)<M
def bal(x,p): x%=p; return x if x<=p//2 else x-p
# [0] raw check of the domino formula
bad=tot=0
for p in (29,31,37,47):
    M=32*p
    for b in range(1,(p+1)//2):
        for w in range(1,16*p,2):
            if w%p in (0,1,p-1): continue
            d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32)
            raw=set()
            for t in range(1,16*p+1,2):
                if t%p not in (b%p,(-b)%p) or not hit(t,w,M): continue
                T=t if t%p==b%p else M-t
                raw.add(((T-b)*pow(p,-1,32))%32)
            J=(-2,-1,0,1) if d>0 else (-1,0,1,2)
            pred={((j-m)*v)%32 for j in J if (j-m-b-1)%2==0}
            tot+=1; bad+= raw!=pred
print('[0] level-5 domino formula vs raw hit test, p in 29,31,37,47 all b,w:',tot,'cases, mismatches',bad)

def dominos(c,v,beta,mod):
    h=(c//2)%16; out=set()
    for x in (h,h+16):
        if x%2==beta: out.add(frozenset({(x-v)%mod,(x+v)%mod}))
        else:
            for e in (1,-1): out.add(frozenset({x%mod,(x+2*e*v)%mod}))
    return [tuple(sorted(o)) for o in out]
def cover(k,beta,mod,mult):
    tgt=[s for s in range(mod) if s%2!=beta]
    opts=[dominos(c,v,beta,mod) for c,v in k]
    cnt=Counter()
    def rec(i):
        if i==8: return all(cnt[s]==mult for s in tgt)
        for dm in opts[i]:
            if any(cnt[s]+dm.count(s)>mult for s in set(dm)): continue
            for s in dm: cnt[s]+=1
            if rec(i+1): return True
            for s in dm: cnt[s]-=1
        return False
    return rec(0)
# [1] full abstract level-5 model (mod 32 exact cover, b parity beta)
F={k:(cover(k,0,32,1),cover(k,1,32,1)) for k in MD}
print('[1] abstract level-5 exact cover (mod 32): beta0 REAL',sum(F[k][0] for k in R),'NEVER',sum(F[k][0] for k in NEVER),
      '| beta1 REAL',sum(F[k][1] for k in R),'NEVER',sum(F[k][1] for k in NEVER))
# [2] rule R16: mod-16 shadow double cover
S={k:(cover(k,0,16,2),cover(k,1,16,2)) for k in MD}
print('[2] R16 (each slot of parity beta+1 mod 16 covered exactly twice): beta0 REAL',sum(S[k][0] for k in R),'NEVER',sum(S[k][0] for k in NEVER),
      '| beta1 REAL',sum(S[k][1] for k in R),'NEVER',sum(S[k][1] for k in NEVER),
      '| beta0<=>beta1 on all',all(a==b for a,b in S.values()),'| R16 set == 640-set',set(k for k in MD if S[k][0])==R,
      '| R16 => mod32 cover',all(F[k][0] for k in MD if S[k][0]))
# [3] weaker projection mod 8 (each slot of parity beta+1 mod 8 covered 4 times) and simple overfill test
S8={k:(cover(k,0,8,4) or cover(k,1,8,4)) for k in MD}
def overfill(k,beta):
    f=Counter()
    for c,v in k:
        h=(c//2)%16
        if h%2==beta: f[(h-v)%16]+=1; f[(h+v)%16]+=1
        else: f[h%16]+=1
    return max(f.values())>2
OV={k:(overfill(k,0) or overfill(k,1)) for k in MD}
print('[3] mod-8 projection holds: REAL',sum(S8[k] for k in R),'NEVER',sum(S8[k] for k in NEVER),
      '| overfill (fixed cells >2 at some residue mod 16, some beta): REAL',sum(OV[k] for k in R),'NEVER',sum(OV[k] for k in NEVER))
# [7] local form of R16 at parity beta: (a) no residue mod 16 gets >2 FIXED cells, (b) every free end (case B, h -> h+-2v)
#     has at least one option in the deficit set {s : fixed(s) < 2}  (supply of free ends = total deficit, so none may be wasted).
def local(k,beta):
    f=Counter(); free=[]
    for c,v in k:
        h=(c//2)%16
        if h%2==beta: f[(h-v)%16]+=1; f[(h+v)%16]+=1
        else: f[h%16]+=1; free.append({(h+2*v)%16,(h-2*v)%16})
    if max(f.values())>2: return 'overfill'
    need={s for s in range(16) if s%2!=beta and f[s]<2}
    if any(not (o&need) for o in free): return 'dead free end'
    return 'ok'
# orbits / classes
def act(k,a,t): return tuple(sorted(norm(a*c+2*t,a*v) for c,v in k))
seen={}; orbits=[]
for k in MD:
    if k in seen: continue
    O=set(act(k,a,t) for a in range(1,32,2) for t in range(16))
    for x in O: seen[x]=len(orbits)
    orbits.append(sorted(O))
def U(c,v): return frozenset((c+d*v)%32 for d in (1,-1,3,-3))
def degs(r):
    E=set()
    for s in range(1,32,2): E.add(tuple(sorted(i for i,f in enumerate(r) if s in U(*f))))
    g=[0]*8
    for i,j in E:
        if i!=j: g[i]+=1; g[j]+=1
    return tuple(sorted(g))
print('[4] orbits',len(orbits),'; R16 constant on every orbit:',all(len({S[k] for k in O})==1 for O in orbits))
cls=defaultdict(lambda:[0,0,0,0])
for O in orbits:
    k=O[0]; g=degs(k); real=k in R
    st='R16 holds' if S[k][0] else 'beta0: '+local(k,0)+', beta1: '+local(k,1)
    print('   orbit size',len(O),'class',g,'REAL' if real else 'NEVER','|',st,'| rep',k)
    cls[g][0]+=len(O); cls[g][1]+=real*len(O); cls[g][2]+=sum(S[x][0] for x in O)
print('[5] per degree class: configs, REAL, R16-true')
for g in sorted(cls): print('   ',g,cls[g][:3])
# [6] the real p=29,b=1 tiling W
p,b=29,1; W=(19,179,441,339,397,313,237,77); fp=[]
for w in W:
    d=bal(b*w,p); m=(b*w-d)//p; v=pow(w,-1,32); fp.append(norm((-2*m*v)%32,v))
fp=tuple(sorted(fp)); print('[6] p29 W footprint',fp,'in 640',fp in R,'R16',S[fp])

L={k:(local(k,0),local(k,1)) for k in MD}
for beta in (0,1):
    print(f'[7] beta{beta}: local ok REAL',sum(L[k][beta]=='ok' for k in R),'NEVER',sum(L[k][beta]=='ok' for k in NEVER),
          '| NEVER overfill',sum(L[k][beta]=='overfill' for k in NEVER),'dead-end',sum(L[k][beta]=='dead free end' for k in NEVER),
          '| local==R16 on all',all((L[k][beta]=='ok')==S[k][beta] for k in MD))
print('[7] NEVER overfilled at BOTH parities:',sum(L[k]==('overfill','overfill') for k in NEVER),
      '; NEVER with one parity overfill + other dead-end:',sum(sorted(L[k])==['dead free end','overfill'] for k in NEVER))
dead_orb=sorted({seen[k] for k in NEVER if 'dead free end' in L[k]})
print('[7] orbits needing the dead-end step:',len(dead_orb),[ (len(orbits[o]),degs(orbits[o][0])) for o in dead_orb])
