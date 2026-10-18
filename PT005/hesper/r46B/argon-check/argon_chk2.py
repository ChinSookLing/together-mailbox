import itertools
def setup(p,M,w):
    N=2*M; T=list(range(1,N//2+1,2))
    def cov(x): 
        m=0
        for j,t in enumerate(T):
            r=(t*x)%N; d=min(r,N-r)
            if 16*d<N: m|=1<<j
        return m
    fm=lambda a: sum(1<<j for j,t in enumerate(T) if t%p in (a%p,(p-a)%p))
    return N,T,cov,fm
def run(lab,p,M,w,extra=None):
    N,T,cov,fm=setup(p,M,w); full=(1<<len(T))-1
    C=[(cov(x),cov(x+M)) for x in w]; F1=fm(1)
    nopen=0;nf1=0;opens=[]
    for bits in itertools.product((0,1),repeat=len(w)):
        c=0
        for i,b in enumerate(bits): c|=C[i][b]
        if c==full: nopen+=1; opens.append(bits)
        if c&F1==F1: nf1+=1
        if extra: extra(bits,c)
    print(lab,'covered children',nopen,'fibre1-covered',nf1)
    for b in opens: print('  ',{w[i]:w[i]+M*b[i] for i in range(len(w))})
    return C,T,F1,cov
A=[1,3,3,5,7,8,18,22,40,55,69,75,87,105,110]
cnt={'t':0,'f':0}
def ex(bits,c):pass
C,T,F1,cov=run('A',17,136,A)
# fibre1 positions, as index t=(T-1)/2? print T values
for x in [1,3,5,7,55,69,75,87,105,18,22,110,8,40]:
    print(' A f1',x,[T[j] for j in range(len(T)) if (cov(x)>>j)&1 and (F1>>j)&1],'|',[T[j] for j in range(len(T)) if (cov(x+136)>>j)&1 and (F1>>j)&1])
print('A fibre1 T list',[T[j] for j in range(len(T)) if (F1>>j)&1])
run('B',17,136,[1,3,8,11,13,15,37,49,73,75,79,84,113,117,118])
run('G',19,152,[39,59,41,61,43,101,121,8,47,125,145,15,73,55,37])
