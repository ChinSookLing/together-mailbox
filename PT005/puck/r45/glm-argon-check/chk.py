import itertools
def nrm(x,m):
    x%=m; return min(x,m-x)
def formula(p,k,v,u,a):
    d=k-v; al=(a*u)%p
    if d>=5: return 2**(k-4)
    if d<=0:
        t=(pow(2,v-k)*al)%p
        return 2**(k-1) if 16*nrm(t,p)<p else 0
    tau_num=2**d*p  # tau = 2^(d-4) p ; compare 16*alpha < 2^d p
    n=(1 if (al%2==1 and 16*al<tau_num) else 0)+(1 if (al%2==0 and al>=1 and 16*(p-al)<tau_num) else 0)
    return 2**(k-d)*n
mism=0;tot=0;d5=0;bad5=0
for p in (17,19,23,29):
  for k in range(1,8):
    M=2**k*p
    for v in range(0,k+3):
      for u in [1,3,5,7,9,11,13,15,p,3*p,p*p,-1,-3,21,25,31,33,35,37]:
        w=2**v*u
        for a in range(1,p):
          fib=[T for T in range(1,M//2+1,2) if T%p in (a,p-a)]
          assert len(fib)==2**(k-1)
          C=sum(1 for T in fib if 16*nrm(T*w,M)<M)
          d=k-v
          # half-period: GLM table: d>=1: 2^{k-d}*n where n counts per sign? check both readings
          F=formula(p,k,v,u,a)
          tot+=1
          if d>=5:
            d5+=1
            if C!=2**(k-4): bad5+=1
          if C!=F:
            mism+=1
            if mism<8: print("mism",p,k,v,u,a,d,C,F)
print("tot",tot,"mism",mism,"d>=5",d5,"bad5",bad5)
