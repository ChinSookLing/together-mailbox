def nrm(x,N): x%=N; return min(x,N-x)
def unc(ws,k,a,p=17):
    N=2**k*p; cls=[];U=[]
    for T in range(1,N//2+1,2):
        if T%p in (a%p,(-a)%p):
            cls.append(T)
            if not any(16*nrm(T*w,N)<N for w in ws): U.append(T)
    return len(cls),len(U)
print("m3 k6 a2",unc([72,200,360],6,2))
print("m4 k6 a2",unc([72,200,56,40],6,2))
print("m4 k7 a2",unc([72,200,56,40],7,2), "k7 a=4 (rotated)",unc([72,200,56,40],7,4))
# per-coordinate coverage count lemma
k=8;N=2**k*17
for w in [72,200,19,1069,3*2**5]:
  c=sum(1 for T in range(1,N//2+1,2) if T%17 in(2,15) and 16*nrm(T*w,N)<N)
  print("lemma k8 w",w,c,"expect",2**(k-4))
