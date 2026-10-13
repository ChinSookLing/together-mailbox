import re,sys,itertools
from fractions import Fraction as F
from collections import Counter
def solve(ks,ys):
    A=[[F(16)**(k-1),F(8)**(k-1),F(4)**(k-1),F(y)] for k,y in zip(ks,ys)]
    for i in range(3):
        piv=A[i][i]; A[i]=[x/piv for x in A[i]]
        for j in range(3):
            if j!=i: f=A[j][i]; A[j]=[a-f*b for a,b in zip(A[j],A[i])]
    return [A[i][3] for i in range(3)]
p=int(sys.argv[1]); files=sys.argv[2:]
n=(p-1)//2
cov={v:frozenset(t for t in range(1,n+1) if 16*min(v*t%p,p-v*t%p)<p) for v in range(1,n+1)}
ALL=frozenset(range(1,n+1))
def mincore(S):
    S=list(S)
    for k in range(1,len(S)+1):
        for sub in itertools.combinations(range(len(S)),k):
            if frozenset().union(*[cov[S[i]] for i in sub])==ALL: return k
rows=[];bases=set()
for f in files:
    for l in open(f):
        if not l.startswith('SURVIVOR'): continue
        nums=[int(x) for x in re.search(r'base: ([\d ]+?) l2',l).group(1).split()]
        d={int(k):int(v) for k,v in re.findall(r'l(\d+)=(\d+)',l)}
        rows.append((nums,d,'PERSISTENT' in l)); bases.add(tuple(nums[:14]))
pers=[r for r in rows if r[2]]
print(f'p={p}: base covers processed={len(bases)}, survivors={len(rows)}, persistent={len(pers)} ({100*len(pers)/max(1,len(rows)):.0f}%)')
held=sum(1 for _,d,_ in pers if all(k in d for k in (4,8,16,32)) and (lambda a,b,c: a*16**4+b*8**4+c*4**4==d[32])(*solve((2,3,4),(d[4],d[8],d[16]))))
print(f'GLM law, l32 predicted exactly from l4,l8,l16: {held}/{len(pers)}')
print('l32 = 4*l16 (x4 rows):',sum(1 for _,d,_ in pers if d.get(32)==4*d.get(16,-1)),'/',len(pers))
sample=pers if len(pers)<=400 else pers[::max(1,len(pers)//400)]
print('minimal cover-core size among persistent rows (sample of',len(sample),'):',sorted(Counter(mincore(r[0]) for r in sample).items()))
