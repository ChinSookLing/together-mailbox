# Claim (1): chains of exact tilings over L consecutive levels (target b at level k, 2b at k+1, 4b at k+2...).
# A chain = 8 legal odd coords taken at the TOP level k+L-1 (mod N_top, up to sign) whose reductions
# mod N_j tile C_j(2^(j-k) b) for every j=k..k+L-1. Exact cover over the disjoint union of the L targets.
# Reported: keys = distinct tilings by per-level cover-set signature; chains = coordinate 8-sets.
import sys
from common import *
from math import prod
def run(k,b,L):
    top=k+L-1; elems=[]; 
    for j in range(k,top+1):
        elems+= [(j,t) for t in C(j,(b<<(j-k))%P)]
    full=frozenset(elems); groups={}
    for w in legal(top):
        s=frozenset((j,t) for j in range(k,top+1) for t in C(j,(b<<(j-k))%P) if covers(t,w%N(j),N(j)))
        groups.setdefault(s,[]).append(w)
    keys=[s for s in groups if s and len([e for e in s if e[0]==k])>0]
    bym={}
    for s in keys:
        for e in s: bym.setdefault(e,[]).append(s)
    nk=0; nc=0; ex=None
    def rec(rem,acc):
        nonlocal nk,nc,ex
        if not rem:
            if len(acc)==8:
                nk+=1; nc+=prod(len(groups[s]) for s in acc)
                if ex is None: ex=[groups[s][0] for s in acc]
            return
        if len(acc)>=8: return
        m=min(rem)
        for s in bym.get(m,[]):
            if s<=rem: acc.append(s); rec(rem-s,acc); acc.pop()
    rec(full,[])
    return nk,nc,ex
if __name__=="__main__":
    k=int(sys.argv[1]);L=int(sys.argv[2])
    for b in range(1,9):
        print(f"k={k} L={L} b={b} keytilings={{}} chains={{}} ex={{}}".format(*run(k,b,L)),flush=True)
