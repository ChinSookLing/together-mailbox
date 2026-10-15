# Puck check of GPT R42 counterexample claim (2026-10-15)
import json, itertools
from collections import Counter
mixed=lambda k: not (all(v%8 in (1,7) for c,v in k) or all(v%8 in (3,5) for c,v in k))
def canon(c,v): v%=32; return (c%32,min(v,32-v))
D=set(tuple(sorted(canon(c,v) for c,v in r)) for r in json.load(open('/workspace/work/r38_doublable_only.json')))
MD=[k for k in D if mixed(k)]
def r16(k,beta):
    opts=[]
    for c,v in k:
        h=(c//2)%16
        if h%2==beta: opts.append([((h-v)%16,(h+v)%16)])
        else: opts.append([(h,(h+2*v)%16),(h,(h-2*v)%16)])
    for ch in itertools.product(*opts):
        cnt=Counter(x for dom in ch for x in dom)
        if all(cnt[r]==2 for r in range(16) if r%2!=beta) and sum(cnt.values())==16: return True
    return False
def two_cover(k):
    cnt=Counter()
    for c,v in k:
        for s in (v,-v,3*v,-3*v):
            cnt[(c+s)%32]+=1
    odds=[r for r in range(32) if r%2==1]
    return all(cnt[r]==2 for r in odds)
def tau1(k):
    return tuple(sorted(canon(c+2,v) for c,v in k))
k=tuple(sorted(canon(c,v) for c,v in [(4,5),(6,3),(6,5),(14,3),(16,3),(22,5),(30,1),(30,5)]))
print('k',k)
print('mixed',mixed(k),'2cover',two_cover(k),'inD',k in D,'inMD',k in MD)
print('R16(k,0/1)',r16(k,0),r16(k,1))
k1=tau1(k)
print('tau1',k1,'R16',r16(k1,0),r16(k1,1))
bad=sum(1 for kk in MD for beta in (0,1) if r16(kk,beta)!=r16(tau1(kk),beta))
print('MD same-beta mismatches',bad,'of',len(MD)*2)
