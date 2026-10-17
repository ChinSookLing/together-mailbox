# Puck independent brute-force check of chair note 99 Lemma Z (zero fibre).
# Level M=2^k p, T=p*t (t odd, T<=M/2). Coordinate w covers T iff 16*||T*w||_M < M.
def dist(x,m):
    x%=m; return min(x,m-x)
bad=0; cases=0
for p in [17,19,23,29,31,61,101]:
    for k in range(1,10):
        M=(2**k)*p
        Ts=[p*t for t in range(1,2**(k-1)+1,2)]
        for w in range(1,M):
            pass  # all w, including multiples of p
            v=(w & -w).bit_length()-1
            d=0 if v>=k else k-v
            c=sum(1 for T in Ts if 16*dist(T*w,M)<M)
            n=len(Ts)
            if d==0: ok=(c==n)
            elif d<=4: ok=(c==0)
            else: ok=(8*c==n)
            cases+=1
            if not ok:
                bad+=1
                if bad<10: print("FAIL",p,k,w,d,c,n)
print("cases",cases,"fails",bad)
