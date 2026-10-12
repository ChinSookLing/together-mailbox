import sys,json,glob,random
def fold(x,p): x%=p; return min(x,p-x)
def prof(S,p,B=20,Q=8):
    out=[]
    for v in S:
        q=next((q for q in range(1,Q+1) if fold(q*v,p)<=B),None)
        out.append(q)
    return out
def dec(h,w=2): return [int(h[i:i+w],16) for i in range(0,len(h),w)]
p=int(sys.argv[1]); files=sys.argv[2:]
rows=[dec(l.strip()) for f in files for l in open(f) if l.strip()]
from collections import Counter
C=Counter(); allq=Counter()
for S in rows:
    pr=prof(S,p); C[tuple(sorted(Counter(pr).items(),key=str))]+=1; allq.update(pr)
print('rows',len(rows),' q-histogram over all classes (None = no q<=8 with |q v| <= 20):',dict(sorted(allq.items(),key=str)))
random.seed(2); n=(p-1)//2; rq=Counter()
for _ in range(2000): rq.update(prof(random.sample(range(1,n+1),15),p))
print('random 15-sets, same histogram per', 2000*15,'classes:',dict(sorted(rq.items(),key=str)))
