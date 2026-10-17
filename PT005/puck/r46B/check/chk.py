# Puck independent check, PT005 R46 Track B: printed runner model vs direct coverage.
# Direct: coordinate w covers T at level M=2^k p  iff  ||T*w||_M < M/16  (16*dist < M).
# Printed model: T=a+p*s (s in 0..2^k-1, T odd), d=k-v>=1, c=(a*u-alpha)/p mod 2^d, alpha=a*u mod p,
#   covered iff ||u*s+c||_{2^d} < 2^(d-4)   (strict, integer phase).
# Fixed model: covered iff ||u*s+c+alpha/p||_{2^d} < 2^(d-4)  (fractional phase).
import random
from fractions import Fraction as F
def circ(x,n): x%=n; return min(x,n-x)
def direct(T,w,M): return 16*circ(T*w,M) < M
def printed(s,u,a,p,d):
    al=(a*u)%p; c=((a*u-al)//p)%(2**d); return 16*circ(u*s+c,2**d) < 2**d
def fixed(s,u,a,p,d):
    al=(a*u)%p; c=((a*u-al)//p)%(2**d); x=F((u*s+c)%(2**d))+F(al,p); n=2**d
    x%=n; dist=min(x,n-x); return 16*dist < n
random.seed(20261018)
tot=bad_p=bad_f=deep=bad_deep=0; ex=None
for _ in range(20000):
    p=random.choice([3,5,7,11,13,17,19,23]); k=random.randint(5,10); M=2**k*p
    v=random.randint(0,k-1); u=random.randrange(1,2**12,2); w=2**v*u; d=k-v
    a=random.randint(1,p-1)
    for s in range(2**k):
        T=a+p*s
        if T%2==0: continue
        D=direct(T,w,M); P=printed(s,u,a,p,d); X=fixed(s,u,a,p,d)
        tot+=1
        if d>=5: deep+=1
        if D!=P:
            bad_p+=1
            if d>=5:
                bad_deep+=1
                if ex is None: ex=(p,k,M,T,w,v,u,d,a,s)
        if D!=X: bad_f+=1
print("comparisons",tot,"deep(d>=5)",deep)
print("printed-model mismatches",bad_p,"of which d>=5:",bad_deep)
print("fixed-model mismatches",bad_f)
print("first d>=5 mismatch (p,k,M,T,w,v,u,d,a,s):",ex)
# Astra's example and DeepSeek's hand example
for (p,k,T,w) in [(17,7,201,228),(17,6,511,2)]:
    M=2**k*p; print("example p=%d M=%d T=%d w=%d: ||Tw||_M=%d, M/16=%s, direct covered=%s"%(p,M,T,w,circ(T*w,M),F(M,16),direct(T,w,M)))
# Counting sanity: for alpha>0, d>=5, how many x in Z/2^d does the printed rule accept? Theorem NZ says 1/8 = 2^(d-3).
for d in range(5,9):
    n=2**d; acc=sum(1 for x in range(n) if 16*circ(x,n)<n)
    print("d=%d printed-rule accepted phases=%d, 1/8 of track=%d"%(d,acc,n//8))
