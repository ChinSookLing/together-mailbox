# Forced-family count: 64 x sum over rows of #(13-position subsets whose classes cover all time classes). Compare with lift checker.
import sys, itertools
p=int(sys.argv[1]); f=sys.argv[2]; n=(p-1)//2
cov={v:sum(1<<t for t in range(1,n+1) if 16*min(v*t%p,p-v*t%p)<p) for v in range(1,n+1)}
ALL=sum(1<<t for t in range(1,n+1)); tot=0
for l in open(f):
    r=list(map(int,l.split()[2:17]))
    for drop in itertools.combinations(range(15),2):
        u=0
        for i in range(15):
            if i not in drop: u|=cov[r[i]]
        tot+= (u==ALL)
print(p,f,"forced lifts predicted =",64*tot)
