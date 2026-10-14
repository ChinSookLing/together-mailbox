# Independent PT005 reimplementation from definitions only (Puck). p=17, v=0.
import os
P=int(os.environ.get("PP","17"))
def N(k): return (1<<k)*P
def dist(x,n): x%=n; return min(x,n-x)
def covers(t,w,n): return 16*dist(t*w,n)<n
def C(k,b):
    n=N(k); return [t for t in range(1,n//2+1,2) if t%P in (b%P,(-b)%P)]
def legal(k):  # odd w mod N up to sign w~N-w, rep in 1..N/2
    n=N(k); return [w for w in range(1,n//2,2) if w%P not in (0,1,P-1)]
def cov(w,k,b):
    n=N(k); return frozenset(t for t in C(k,b) if covers(t,w,n))
def tilings(k,b,coords):
    """all sets of 8 coords (by distinct cover set) whose cover sets partition C_k(b)"""
    cs=C(k,b); full=frozenset(cs)
    sets={}
    for w in coords:
        s=cov(w,k,b)
        if s: sets.setdefault(s,[]).append(w)
    by_min={}
    for s in sets: by_min.setdefault(min(s),[]).append(s)
    out=[]
    def rec(rem,acc):
        if not rem: out.append(list(acc)); return
        m=min(rem)
        for s in by_min.get(m,[]):
            if s<=rem: acc.append(s); rec(rem-s,acc); acc.pop()
    rec(full,[])
    return out,sets
