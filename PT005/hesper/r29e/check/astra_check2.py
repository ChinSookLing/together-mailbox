import re,sys
sys.path.insert(0,'together-mailbox/PT005/puck/verify')
from common import *
exec(open('r29e/astra_check.py').read().split("print(len(cases))")[0])
n5,n6=N(5),N(6)
tot=0;match=0;summ=0;cycok=0;rows=[]
for b,c,ws,m4,cyc in cases:
    wn=[w if (b*w)%17==7 else 544-w for w in ws]
    c6=C(6,(2*b)%17)
    def hits(w):
        return {t:e for e in (0,1) for t in c6 if covers(t,(w+e*n5)%n6,n6)}
    H=[hits(w) for w in wn]   # labels with original ws (the data's)
    for path,lab in cyc:
        a=[wn[i]%32 for i in path]
        if a[1]!=(7*a[0])%32: path=path[::-1]
        lsum=0; fsum=0
        for k in range(4):
            i,j=path[k],path[(k+1)%4]
            sh=set(H[i])&set(H[j])
            labs={H[i][t]^H[j][t]^1 for t in sh}
            assert len(labs)==1; L=labs.pop(); lsum+=L
            wj,wj1=wn[i],wn[j]; M=(wj1-7*wj)//32
            fs=set()
            for t in sh:
                tp=t if t%17==(2*b)%17 else -t
                for T in (tp,tp+544,tp-544):
                  if (T*M-8)%17==0: fs.add((T%32==(-5*wj)%32-1 or (T-(-5*wj-1))%32==0, (1+(T*M-8)//17)%2))
            rows.append((b,c,k,L,sorted(fs)))
        summ+= lsum%2
print('cycles with odd true sum',summ,'of 28')
for r in rows[:16]: print(r)
