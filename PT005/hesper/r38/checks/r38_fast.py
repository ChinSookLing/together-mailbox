import sys
exec(open('hesper_r38_abstract_cv.py').read().split('res=[]')[0])
odds=list(range(1,32,2))
Us=[U(*f) for f in fps]
cover={s:[i for i in range(len(fps)) if s in Us[i]] for s in odds}
res=[]
sys.setrecursionlimit(10000)
def rec(cnt,chosen,excl,n):
    if n==8:
        if all(cnt[s]==2 for s in odds): res.append(tuple(sorted(chosen)))
        return
    s0=next((s for s in odds if cnt[s]<2),None)
    if s0 is None: return
    cands=[i for i in cover[s0] if i not in excl and all(cnt[s]<2 for s in Us[i])]
    # branch: choose first candidate i (include) or exclude it
    for k,i in enumerate(cands):
        for s in Us[i]: cnt[s]+=1
        rec(cnt,chosen+[i],excl|set(cands[:k]),n+1)
        for s in Us[i]: cnt[s]-=1
from collections import Counter
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

rec(Counter(),[],frozenset(),0)
res=sorted(set(res)); confs=[tuple(fps[i] for i in r) for r in res]
D=[r for r in confs if doublable(r)]
mx=lambda r: len(set(v%8 in (1,7) for c,v in r))>1
print('exact 2-covers (multisets, v~-v):',len(confs),'doublable:',len(D))
print('mixed covers',sum(map(mx,confs)),'mixed doublable',sum(mx(r) for r in D))
import json; json.dump({'all':confs,'doublable':D},open('r38_abstract.json','w'))
