import math,cmath
def go(p,S,K=4):
    H=(p-1)//16
    def bh(k):
        if k==0: return 1-(2*H+1)/p
        return -(1/p)*math.sin(math.pi*(2*H+1)*k/p)/math.sin(math.pi*k/p)
    q=bh(0); M=p/2*q**len(S)
    tot=0
    for t in range(p):
        pr=1
        for v in S:
            pr*=sum(bh(k)*math.cos(2*math.pi*k*v*t/p) for k in range(-K,K+1))
        tot+=pr
    return M, tot/2-M  # (p/2)*(1/p)*sum_t ... = sum_t/2 ; minus k=0 term
for n,p,S in [("457cover",457,[1,2,55,60,68,111,112,113,114,115,116,117,169,221]),("337cover",337,[1,7,15,40,43,58,63,65,83,101,106,108,115,164])]:
    print(n,go(p,S))
