# Hesper: list every (node, even coord) with depth d>=4 and |U|>=2 (Opus note 109 rule, unit_halves.py logic, full set).
import gzip,csv,numpy as np
def v2(x):
    c=0
    while x%2==0: x//=2;c+=1
    return c
out=csv.writer(open("r47d_82rows.csv","w")); out.writerow(["csv_row","p","k","M","coords","n_open_children","i","w_i","depth","nU","n_bit0","n_bit1","U_bit0_T","U_bit1_T"])
row=0
with gzip.open("/workspace/work/r45/widen/nodes_widen.csv.gz","rt") as f:
    rd=csv.reader(f); next(rd)
    for r in rd:
        row+=1
        p,k,M=int(r[0]),int(r[1]),int(r[2])
        if k<4: continue   # depth>=4 needs k>=4
        w=np.array([int(x) for x in r[3].split()],dtype=np.int64); N=2*M
        ev=[(i,int(x)) for i,x in enumerate(w) if x%2==0 and k-v2(int(x))>=4]
        if not ev: continue
        T=np.arange(1,M+1,2,dtype=np.int64)[:,None]
        r0=(T*w)%N; c0=16*np.minimum(r0,N-r0)<N
        r1=(T*(w+M))%N; c1=16*np.minimum(r1,N-r1)<N
        reach=c0|c1; unit=reach.sum(axis=1)==1
        for i,x in ev:
            U=unit&reach[:,i]; b0=U&c0[:,i]; b1=U&c1[:,i]
            n0,n1=int(b0.sum()),int(b1.sum())
            if n0+n1>=2:
                Tv=T[:,0]
                out.writerow([row,p,k,M,r[3],r[10],i,x,k-v2(x),n0+n1,n0,n1," ".join(map(str,Tv[b0])), " ".join(map(str,Tv[b1]))])
