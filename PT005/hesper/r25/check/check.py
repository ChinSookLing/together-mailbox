p=17
def hit(t,w,N):
    x=(t*w)%N; return 16*min(x,N-x)<N
def improper(W,N): return all(any(hit(t,w,N) for w in W) for t in range(1,N//2+1))
def legal(P,W,Nprev): return all(w%p==v%p and w in (v,v+Nprev) for v,w in zip(P,W))
print("== GPT ==")
F=[[104,156,208,532,312,228,110,434],[104,156,752,1076,856,228,654,434],[1192,1244,1840,1076,1944,228,654,434]]
non=lambda k:[2**k*(i*pow(2**k,-1,p)%p) for i in range(10,17)]
prev=None
for r,k in enumerate((5,6,7)):
    N=p*2**k; W=F[r]+non(k)
    res=[w%p for w in W]==list(range(2,17))
    free=[a for a in range(1,17) if not any(hit(a,w,N) for w in non(k))]
    T=[t for t in range(1,N//2+1,2) if t%17 in (4,13)]
    fcov=all(any(hit(t,w,N) for w in F[r]) for t in T)
    print(k,"residues ok",res,"legal",legal(prev,W,N//2) if prev else "-","improper(full 15)",improper(W,N),"frozen-only cover ±4",fcov,"free residues of non-frozen",free)
    prev=W
print("== Astra ==")
W5=[240,496,208,464,176,432,144,128,384,96,352,64,320,32,16]
Fz={2:784,3:1040,4:1296,5:1552,6:1808,7:2064,8:2320,16:3824}
print("k5 improper",improper(W5,544))
for k in range(5,9):
    N=p*2**k
    T=[t for t in range(1,N//2+1,2) if t%17 in (2,15)]
    mult=[sum(hit(t,w%N,N) for w in Fz.values()) for t in T]
    print(k,len(T),sum(m>0 for m in mult),min(mult),max(mult))
# can full state stay improper k=5..8 with Astra frozen fixed? search lifts of other 7
import itertools
others=[r for r in range(2,17) if r not in Fz]
states=[{r:W5[r-2] for r in range(2,17)}]
for k in range(6,9):
    N=p*2**k; Np=N//2; new=[]
    for s in states:
        for bits in itertools.product((0,1),repeat=7):
            t={r:Fz[r]%N for r in Fz}
            if any(t[r] not in (s[r],s[r]+Np) for r in Fz): continue
            for r,b in zip(others,bits): t[r]=s[r]+b*Np
            if improper(list(t.values()),N): new.append(t)
    states=new
    print("Astra chain level",k,"improper full states",len(states),
          "frozen counts",sorted({sum(1 for w in s.values() if w%2**k) for s in states}))
