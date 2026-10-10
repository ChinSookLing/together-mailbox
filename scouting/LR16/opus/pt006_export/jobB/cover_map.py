import sys, json
def near(v,t,p):
    r=(v*t)%p; return 16*min(r,p-r)<p
def cmap(p,S):
    n=(p-1)//2
    rows={v:[t for t in range(1,n+1) if near(v,t,p)] for v in S}
    mult={t:sum(near(v,t,p) for v in S) for t in range(1,n+1)}
    sole={v:[t for t in rows[v] if mult[t]==1] for v in S}
    holes=[t for t in range(1,n+1) if mult[t]==0]
    hist={}
    for t in mult: hist[mult[t]]=hist.get(mult[t],0)+1
    return rows,mult,sole,holes,dict(sorted(hist.items()))
cases=[(457,[1,2,55,60,68,111,112,113,114,115,116,117,169,221]),
       (383,[1,10,11,21,32,39,43,54,74,75,85,106,107,157]),
       (397,[1,6,39,54,59,60,125,137,138,139,141,142,143,168])]
for p,S in cases:
    rows,mult,sole,holes,hist=cmap(p,S)
    print(f"p={p} n={(p-1)//2} H={(p-1)//16} holes={holes}")
    print("  multiplicity histogram:",hist, " sum of row sizes:",sum(len(r) for r in rows.values()))
    for v in S: print(f"  v={v:4d} covers {len(rows[v]):3d} cells, sole {len(sole[v]):3d}")
print("--- high-multiplicity cells (>=4) ---")
for p,S in cases:
    rows,mult,sole,holes,hist=cmap(p,S)
    hi=[(t,mult[t],[v for v in S if near(v,t,p)]) for t in mult if mult[t]>=4]
    print(p,hi)
    print("  checksum: sum over cells of t*mult[t] =",sum(t*m for t,m in mult.items()))
