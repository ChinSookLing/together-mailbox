# Puck R36: smallest prime p with a MIXED exact k=5 tiling that has a k=6 lift ("mixed doubling").
# Type-free direct search: for every (p,b) solve the joint exact-cover problem on 48 cells
# (16 members of C5(b) + 32 members of C6(2b)) with items (w,e): k5 footprint of w | k6 footprint of w+e*32p.
# A solution = 8 items with distinct w covering each cell exactly once = exact k5 tiling W + lift mask.
# Uses ONLY the raw test 16*min(t*w%M, M-t*w%M) < M. Counts all footprint-level solutions, split mixed/single.
import sys
from collections import defaultdict
def hit(t,w,M): r=t*w%M; return 16*min(r,M-r)<M
def cls(w): return 1 if w%8 in (1,7) else 3
def solve(p,b,stop_first_mixed=False):
    n5,n6=32*p,64*p
    c5=[t for t in range(1,16*p+1,2) if t%p in (b%p,(-b)%p)]
    c6=[t for t in range(1,32*p+1,2) if t%p in ((2*b)%p,(-2*b)%p)]
    assert len(c5)==16 and len(c6)==32
    groups=defaultdict(list)          # (mask,class) -> list of (w,e)
    for w in range(1,16*p,2):
        if w%p in (0,1,p-1): continue
        m5=sum(1<<i for i,t in enumerate(c5) if hit(t,w,n5))
        for e in (0,1):
            we=w+e*n5
            m6=sum(1<<(16+i) for i,t in enumerate(c6) if hit(t,we,n6))
            m=m5|m6
            if m: groups[(m,cls(w))].append((w,e))
    keys=list(groups)
    bybit=defaultdict(list)
    for k in keys:
        m=k[0]; low=(m&-m).bit_length()-1; bybit[low].append(k)   # index by lowest set bit
    FULL=(1<<48)-1
    sols=[]
    def rec(cov,sel):
        if cov==FULL:
            if len(sel)==8: sols.append(list(sel))
            return
        if len(sel)>=8: return
        free=~cov&FULL; low=(free&-free).bit_length()-1
        for k in bybit[low]:
            if k[0]&cov: continue
            sel.append(k); rec(cov|k[0],sel); sel.pop()
            if stop_first_mixed and any(len({x[1] for x in s})==2 for s in sols): return
    rec(0,[])
    out=[]
    for s in sols:
        # distinct representatives (w must be distinct)
        def pick(i,used,acc):
            if i==8: return acc
            for (w,e) in groups[s[i]]:
                if w in used: continue
                r=pick(i+1,used|{w},acc+[(w,e)])
                if r: return r
            return None
        r=pick(0,set(),[])
        if r: out.append((len({x[1] for x in s})==2,r))
    return out
if __name__=="__main__":
    ps=[int(x) for x in sys.argv[1:]]
    for p in ps:
        nm=ns=0; first=None
        for b in range(1,(p+1)//2):        # b and p-b give identical C5/C6 sets
            for mixed,r in solve(p,b):
                if mixed:
                    nm+=1
                    if first is None: first=(b,[w for w,_ in r],[w+e*32*p for w,e in r])
                else: ns+=1
        print(f"p={p} footprint-solutions: mixed={nm} single={ns} first_mixed={first}",flush=True)
