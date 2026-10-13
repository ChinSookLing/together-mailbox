import re,sys
from fractions import Fraction as F
def solve(ks,ys):
    A=[[F(16)**(k-1),F(8)**(k-1),F(4)**(k-1),F(y)] for k,y in zip(ks,ys)]
    for i in range(3):
        piv=A[i][i]; A[i]=[x/piv for x in A[i]]
        for j in range(3):
            if j!=i: f=A[j][i]; A[j]=[a-f*b for a,b in zip(A[j],A[i])]
    return [A[i][3] for i in range(3)]
pred_ok=0; k4int=0; fail=[]; n=0
for l in open(sys.argv[1]):
    d={int(k):int(v) for k,v in re.findall(r'l(\d+)=(\d+)',l)}
    if 64 not in d: continue
    n+=1
    a,b,c=solve((3,4,5),(d[8],d[16],d[32]))
    if a*16**5+b*8**5+c*4**5==d[64]: pred_ok+=1; continue
    a,b,c=solve((4,5,6),(d[16],d[32],d[64]))
    if all(x.denominator==1 for x in (a,b,c)): k4int+=1
    else: fail.append((d,(a,b,c)))
print('rows with l64:',n,'| l64 predicted exactly from l8,l16,l32 (lock-in by 8):',pred_ok,'| integer fit only from level 16:',k4int,'| no integer fit:',len(fail))
for f in fail[:5]: print(f)
