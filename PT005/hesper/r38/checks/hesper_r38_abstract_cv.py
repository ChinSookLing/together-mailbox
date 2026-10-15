# Abstract enumeration: multisets of 8 footprints (c,v), c even, v odd mod 32, (c,v)~(c,-v),
# whose position sets U=c+{+-v,+-3v} form an exact 2-cover of the 16 odd residues mod 32.
# Parity per Argon R37: lift bit k_i(s)=(s-c-delta v)/32 (integers, s in 1..31, c in 0..30, v in 1..31).
# Doublable <=> labels lambda=1+k_i+k_j admit a vertex potential (all cycles even).
from collections import Counter
fps=[]
seen=set()
for c in range(0,32,2):
    for v in range(1,32,2):
        key=(c,min(v,32-v))
        if key in seen: continue
        seen.add(key); fps.append((c,min(v,32-v)))
def U(c,v): return frozenset((c+d*v)%32 for d in (1,-1,3,-3))
def kk(c,v,s):
    for d in (1,-1,3,-3):
        if (c+d*v)%32==s: return (s-c-d*v)//32
fps=[f for f in fps if len(U(*f))==4]
res=[]
odds=list(range(1,32,2))
cover={s:[i for i,f in enumerate(fps) if s in U(*f)] for s in odds}
def rec(cnt,chosen,minidx):
    if len(chosen)==8:
        if all(cnt[s]==2 for s in odds): res.append(tuple(sorted(fps[i] for i in chosen)))
        return
    s0=next(s for s in odds if cnt[s]<2)
    for i in cover[s0]:
        u=U(*fps[i])
        if any(cnt[s]>=2 for s in u): continue
        for s in u: cnt[s]+=1
        chosen.append(i); rec(cnt,chosen,i); chosen.pop()
        for s in u: cnt[s]-=1
rec(Counter(),[],0)
res=sorted(set(res))
def doublable(conf):
    edges={}
    for i,(c,v) in enumerate(conf):
        for s in U(c,v): edges.setdefault(s,[]).append(i)
    pot={}
    adj={i:[] for i in range(8)}
    for s,(i,j) in edges.items():
        lam=(1+kk(*conf[i],s)+kk(*conf[j],s))%2
        adj[i].append((j,lam)); adj[j].append((i,lam))
    for r in range(8):
        if r in pot: continue
        pot[r]=0; st=[r]
        while st:
            x=st.pop()
            for y,l in adj[x]:
                if y not in pot: pot[y]=pot[x]^l; st.append(y)
                elif pot[y]!=pot[x]^l: return False
    return True
def mixed(conf): return len(set(v%8 for c,v in conf if True) | set())>0 and len(set(min(v%8,8-v%8) if False else v%8 for c,v in conf))>1
tot=len(res); D=[r for r in res if doublable(r)]
import collections
mx=lambda r: len(set(v%8 in (1,7) for c,v in r))>1
print('mixed covers',sum(map(mx,res)),'mixed doublable',sum(mx(r) for r in D))
ham=[]
print('exact 2-covers (multisets, v~-v):',tot,' doublable:',len(D))
