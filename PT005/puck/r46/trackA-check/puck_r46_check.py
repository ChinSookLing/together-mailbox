# PT005 R46 Track A - Puck independent recheck (own code; imports nothing from Hesper; uses only node lists as input).
# Node w (15 ints) at M=2^k p; children = all 2^15 ORDERED lift vectors (w_i or w_i+M) at N=2M.
# covered(T) at N: some i with 16*||T x_i||_N < N. Only odd T<=M are tested (even T inherit from the open parent).
# Fibre a (0..(p-1)/2): odd T<=M with min(T mod p, p - T mod p)=a. Share of x on fibre a = (#covered T in fibre)/(fibre size),
# computed DIRECTLY (no table). "all sums>=1": for every fibre, sum over coords of covered counts >= fibre size.
# open = covered all odd T<=M, >=2 odd coords, not L7-closed at N (L7 as in Puck r43f3).
# Also: table check = Puck's own GLM/Lemma Z formula (from r45 glm-argon-check/chk.py and lemmaz) vs the direct counts.
import sys, gzip, numpy as np, random, collections
from math import gcd
from multiprocessing import Pool
def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c
def nrm(x,m): x%=m; return min(x,m-x)
def formula_share8(p,K,x,a):
    # Puck's GLM (a!=0) + Lemma Z (a=0) formula at level N=2^K p, returned in eighths of the fibre.
    v=v2(x); u=x>>v; d=K-v
    if a==0:
        if v>=K: return 8
        return 1 if d>=5 else 0
    al=(a*u)%p
    if d>=5: return 1
    if d<=0:
        t=(pow(2,v-K,p)*al)%p
        return 8 if 16*nrm(t,p)<p else 0
    n=(1 if (al%2==1 and 16*al<2**d*p) else 0)+(1 if (al%2==0 and al>=1 and 16*(p-al)<2**d*p) else 0)
    return 16*n//2**d  # count 2^(K-d)*n over fibre size 2^(K-1) = n*2^(1-d) = 16n/2^d eighths
def l7_closed_vec(S,N):
    closed=np.zeros(len(S),bool)
    for D in range(2,N+1,2):
        if N%D: continue
        nz=(S%D)!=0; g=np.gcd(S,D); term=g*(-(-(D//g)//8))
        closed|=(nz.sum(1)>=2)&(np.where(nz,term,0).sum(1)<D)
    return closed
def node(args):
    line,p,M,w=args
    N=2*M; K=(N//p).bit_length()-1
    w=np.array(w,np.int64); X=np.stack([w,w+M],1)            # 15,2
    T=np.arange(1,M+1,2,dtype=np.int64)
    R=(X[:,:,None]*T)%N; C=16*np.minimum(R,N-R)<N             # 15,2,nT
    fa=np.minimum(T%p,p-T%p); F=(p+1)//2
    OH=np.zeros((len(T),F),np.int64); OH[np.arange(len(T)),fa]=1; sz=OH.sum(0)
    cnt=C.astype(np.int64)@OH                                  # 15,2,F
    # table check
    tm=0
    for i in range(15):
        for b in range(2):
            for a in range(F):
                if cnt[i,b,a]*8!=formula_share8(p,K,int(X[i,b]),a)*sz[a]: tm+=1
    # all 32768 children, index m = sum b_i 2^i
    lo=np.zeros((1,F),np.int64); loC=np.zeros((1,C.shape[2]),bool)
    for i in range(7): lo=np.concatenate([lo+cnt[i,0],lo+cnt[i,1]]); loC=np.concatenate([loC|C[i,0],loC|C[i,1]])
    hi=np.zeros((1,F),np.int64); hiC=np.zeros((1,C.shape[2]),bool)
    for i in range(7,15): hi=np.concatenate([hi+cnt[i,0],hi+cnt[i,1]]); hiC=np.concatenate([hiC|C[i,0],hiC|C[i,1]])
    # m = h*128 + l
    Ssum=(hi[:,None,:]+lo[None,:,:]).reshape(-1,F)
    ge1=(Ssum>=sz).all(1)
    minsh8=(Ssum*8//sz).min(1)
    exact=((Ssum*8)%sz==0).all()
    Pl=np.packbits(loC,axis=1); Ph=np.packbits(hiC,axis=1); full=np.packbits(np.ones(C.shape[2],bool))
    cov=np.all((Ph[:,None,:]|Pl[None,:,:])==full,axis=2).reshape(-1)
    m=np.nonzero(cov)[0]
    bits=(m[:,None]>>np.arange(15))&1; S=w[None,:]+bits*M
    odd2=(S&1).sum(1)>=2
    l7=np.zeros(len(m),bool)
    if odd2.any(): l7[odd2]=l7_closed_vec(S[odd2],N)
    op=odd2&~l7
    opd=len(np.unique(np.sort(S[op],1),axis=0)) if op.any() else 0
    return dict(line=line,p=p,ge1=int(ge1.sum()),lt1=int((~ge1).sum()),lt1_cov=int((cov&~ge1).sum()),cov=int(cov.sum()),
                open=int(op.sum()),opd=opd,cov_par=int((~odd2).sum()),cov_l7=int(l7.sum()),
                mn=int(minsh8.min()),mx=int(minsh8.max()),exact=bool(exact),tm=tm,trip=15*2*F)
if __name__=='__main__':
    which=sys.argv[1]
    rows=[]
    for ln,l in enumerate(gzip.open('/workspace/mbx_pt5/PT005/hesper/r45/widen/nodes_widen.csv.gz','rt')):
        if ln==0: continue
        f=l.split(','); rows.append((ln+1,int(f[0]),int(f[2]),[int(z) for z in f[3].split()]))
    H={}
    for ln,l in enumerate(gzip.open('/workspace/mbx_pt5/PT005/hesper/r46/trackA/per_node_trackA.csv.gz','rt')):
        if ln==0: continue
        f=[int(z) for z in l.split(',')]; H[f[0]]=f
    if which=='all': sel=rows
    else:
        random.seed(20261017); sel=random.sample(rows,int(which))
        dead=[r for r in rows if H[r[0]][4]==32768 and H[r[0]][6]==0]
        sel=sel+dead
    with Pool(8) as P: res=P.map(node,sel,chunksize=64)
    agg=collections.Counter(); mism=collections.Counter(); byp=collections.defaultdict(collections.Counter)
    for r in res:
        h=H[r['line']]
        for k,j in [('ge1',4),('cov',5),('open',6),('opd',7),('mn',8),('mx',9)]:
            if r[k]!=h[j]: mism[k]+=1
        for k in ['ge1','lt1','lt1_cov','cov','open','cov_par','cov_l7','tm','trip']: agg[k]+=r[k]; byp[r['p']][k]+=r[k]
        agg['nodes']+=1; agg['not_exact']+=not r['exact']
        agg['dead_all']+= (r['ge1']==32768 and r['open']==0)
    agg['ovdeath']=agg['ge1']-agg['open']
    print('selected',which,'nodes',len(sel)); print('AGG',dict(agg)); print('MISMATCH vs Hesper per_node',dict(mism))
    for p in sorted(byp): print(p,dict(byp[p]))
