import re,random
from math import comb
from itertools import combinations
t=open('r19b_send.txt').read()
def block(name):
    s=t.split('=== '+name+' ===')[1].split('===')[0]
    return [l.strip() for l in s.splitlines() if re.fullmatch(r'[0-9a-f]{30}',l.strip())]
dec=lambda h:[int(h[i:i+2],16) for i in range(0,30,2)]
G0=[dec(x) for x in block('rows_383_0_10.txt')]; G1=[dec(x) for x in block('rows_383_14_4.txt')]
rows=G0+G1; print(len(G0),len(G1),len(set(map(tuple,rows))))
p=383;n=191;m=23
fold=lambda x:min(x%p,p-x%p)
# cover/irredundancy check
def check(S,p):
    n=(p-1)//2;m=(p-1)//16
    cov={t:[v for v in S if 16*fold2(v*t,p)>=p] for t in range(1,n+1)}
    return all(cov[t] for t in cov) and all(any(cov[t]==[v] for t in cov) for v in S)
def fold2(x,p): x%=p; return min(x,p-x)
print('cover+irr', sum(check(S,383) for S in rows))
core=lambda S:sum(v<=30 or v>=161 for v in S)
print('Grok core min',min(core(S) for S in rows),'row0 core',core(G0[0]),sorted(G0[0]))
print('core>=9',sum(core(S)>=9 for S in rows), 'argmin', [S for S in rows if core(S)==4][:2])
sm=lambda S:sum(min(v,p-v)<=20 for v in S)
print('DS >=5',sum(sm(S)>=5 for S in rows),'min',min(sm(S) for S in rows),'rows<5',sum(sm(S)<5 for S in rows),'row0',sm(G0[0]))
print('Lumo v<=20 >=8',sum(sum(v<=20 for v in S)>=8 for S in rows))
print('row0 >=170',sum(v>=170 for v in G0[0]),'>=176',sum(176<=v<=187 for v in G0[0]))
# GLM |H_t|
H={tt:frozenset(v for v in range(2,n+1) if 16*fold(v*tt)<p) for tt in range(24,192)}
print('Ht sizes',set(map(len,H.values())),'distinct',len(set(H.values())))
# GLM bijection sanity: every row minus 1 hits every H_t and is minimal
ok=0
for S in rows:
    K=set(S)-{1}
    hits=all(K&H[tt] for tt in H)
    minimal=all(any(H[tt]&K=={k} for tt in H) for k in K)
    ok+=hits and minimal and 1 in S
print('bijection rows ok',ok)
print('25930', sum(comb(15,k)*2**k for k in range(1,5)))
print(comb(190,14), 119533557199390425945315/comb(190,14))
# dilation
S457=[1,2,55,60,68,111,112,113,114,115,116,117,169,221]
print(sorted(min(8*v%457,457-8*v%457) for v in S457))
# GLM Kimi spot: row index2
S=G0[2];print(sorted(S),[fold(18*v) for v in S])
# Lumo counterexample from Gemini near p/2: count of 7 near p/2 (>=170)
print('rows with >=7 classes >=170',sum(sum(v>=170 for v in S)>=7 for S in rows))
# random DS short relation and AP3 rates
random.seed(1)
def ap3(S):z=set(S);return any(2*b-a in z for a in S for b in S if a<b)
R=[random.sample(range(2,n+1),14)+[1] for _ in range(2000)]
print('AP3 random',sum(ap3(S) for S in R)/2000)
