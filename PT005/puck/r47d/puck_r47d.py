# Puck (Grok Bot) four-eyes rerun, R47D/R47B: Puck's own code (built on Puck's puck_r47c.py).
# Does NOT import or copy PT005/opus/r47d/unit_halves.py or PT005/opus/r47b_grade/*.py.
# Definitions: R47B packet f6b6c50 COMMON; L7 as in nodes_widen's generator (PT005/hesper/r45/hesper_r45.py, open_children):
#   child at N=2M: c_i = w_i + b_i*M. covers odd T<=M iff 16*||T*c_i||_N < N (even T inherited from the improper parent).
#   improper = every T covered and >=2 odd coords. L7-closed: some even D|N with |E_D|>=2 (E_D = coords with c mod D != 0,
#   with multiplicity) and sum_{E_D} g*ceil((D/g)/8) < D, g=gcd(D,c). open = improper and not L7-closed.
# PASS 1 (all k>=1 nodes): 2-SAT flag (short clauses, Warshall closure) + note 109 table:
#   even coord i with v2(w_i)<k, depth d=k-v2(w_i). reach(i,T) = some bit covers T. unit time = odd T<=M reached by i and by
#   no other coordinate (by index). U_i = unit times, h_i(T)= the covering bit. classify |U|=0, |U|=1, |U|>=2 one bit, both bits.
# PASS 2 (CSV-dead nodes that are not 2-SAT-dead): enumerate ALL 2^15 bit choices, list covering children, classify each.
import gzip,csv,sys,collections,json,time,math
import numpy as np
from multiprocessing import Pool
def dist(R,N): R=R%N; return np.minimum(R,N-R)
def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c
def unsat(pairs):
    adj=[0]*30
    for a,b in pairs: adj[a^1]|=1<<b; adj[b^1]|=1<<a
    for k in range(30):
        bk=1<<k; rk=adj[k]
        for i in range(30):
            if adj[i]&bk: adj[i]|=rk
    return any((adj[2*i]>>(2*i+1))&1 and (adj[2*i+1]>>(2*i))&1 for i in range(15))
def pass1(a):
    M,k,ids,W,dead=a; W=np.array(W,dtype=np.int64); N=2*M
    T=np.arange(1,M+1,2,dtype=np.int64)
    A0=16*dist(W[:,None,:]*T[None,:,None],N)<N; A1=16*dist((W[:,None,:]+M)*T[None,:,None],N)<N
    both=(A0&A1); R=A0|A1; cnt=R.sum(2)
    taut=int(both.any(2).sum())
    # 2-SAT
    keep=(~both.any(2))&(cnt<=2)
    first=R.argmax(2); last=14-R[:,:,::-1].argmax(2)
    b1=np.take_along_axis(A1,first[:,:,None],2)[:,:,0]; b2=np.take_along_axis(A1,last[:,:,None],2)[:,:,0]
    l1=2*first+b1; l2=2*last+b2
    # unit times
    unit=R&(cnt==1)[:,:,None]            # (n,T,15)
    nU=unit.sum(1)                        # (n,15)
    has1=(unit&A1).any(1); has0=(unit&A0&~A1).any(1)
    tab=collections.Counter(); oddU=0; selfboth=int((unit&both).sum())
    out=[]
    for j in range(len(ids)):
        kj=keep[j]; pr=set(zip(l1[j][kj].tolist(),l2[j][kj].tolist()))
        s2=unsat(pr)
        for i in range(15):
            w=int(W[j,i])
            if w%2==0:
                vv=v2(w)
                if vv<k:
                    d=k-vv; n=int(nU[j,i])
                    if n%2: oddU+=1
                    cls='U0' if n==0 else 'U1' if n==1 else ('both' if (has0[j,i] and has1[j,i]) else 'one')
                    tab[(dead[j],d,cls)]+=1
        out.append((ids[j],s2))
    return out,tab,oddU,taut,selfboth
BITS=((np.arange(1<<15)[:,None]>>np.arange(15)[None,:])&1).astype(np.int64)
def l7closed(C,N):
    closed=np.zeros(len(C),bool); witness=[None]*len(C)
    for D in range(2,N+1,2):
        if N%D: continue
        nz=(C%D)!=0; g=np.gcd(C,D); s=(g*(-(-(D//g)//8))*nz).sum(1)
        hit=(nz.sum(1)>=2)&(s<D)
        for t in np.nonzero(hit&~closed)[0]: witness[t]=D
        closed|=hit
    return closed,witness
def pass2(a):
    idx,M,w=a; N=2*M; T=np.arange(1,M+1,2,dtype=np.int64)
    cov=np.zeros((1,len(T)),bool)
    for x in w:   # doubling: bit i of choice index = b_i
        m0=16*dist(T*x,N)<N; m1=16*dist(T*(x+M),N)<N
        cov=np.concatenate([cov|m0,cov|m1],0)
    ok=np.nonzero(cov.all(1))[0]
    if len(ok)==0: return idx,None
    C=np.array(w,np.int64)[None,:]+BITS[ok]*M
    nodd=(C%2).sum(1); lt2=nodd<2
    cl,wit=l7closed(C,N)
    opn=(~lt2)&(~cl)
    distinct=len(set(tuple(sorted(r)) for r in C.tolist()))
    dopen=len(set(tuple(sorted(r)) for r in C[opn].tolist()))
    return idx,dict(n_cover_choices=int(len(ok)),n_cover_distinct=distinct,n_open_choices=int(opn.sum()),n_open_distinct=dopen,
        n_lt2odd=int(lt2.sum()),n_l7=int(cl.sum()),n_l7_only=int((cl&~lt2).sum()),n_lt2_only=int((lt2&~cl).sum()),
        n_both=int((cl&lt2).sum()),min_nodd=int(nodd.min()),l7_D=sorted(set(int(x) for x in wit if x)))
if __name__=='__main__':
    t0=time.time()
    rows=[]
    for i,r in enumerate(csv.DictReader(gzip.open(sys.argv[1],'rt'))):
        rows.append((i,int(r['p']),int(r['k']),int(r['M']),list(map(int,r['coords'].split())),int(r['n_open_children'])==0))
    print('rows',len(rows),'k>=1',sum(r[2]>=1 for r in rows),flush=True)
    g=collections.defaultdict(list)
    for r in rows:
        if r[2]>=1: g[(r[3],r[2])].append(r)
    jobs=[]
    for (M,k),rs in sorted(g.items()):
        B=max(50,min(2000,10_000_000//((M//2+1)*15)))
        for s in range(0,len(rs),B):
            ch=rs[s:s+B]; jobs.append((M,k,[r[0] for r in ch],[r[4] for r in ch],[int(r[5]) for r in ch]))
    TAB=collections.Counter(); ODD=0; TAUT=0; SB=0; sat2={}
    with Pool(7) as P:
        for out,tab,oddU,taut,sb in P.imap_unordered(pass1,jobs):
            TAB.update(tab); ODD+=oddU; TAUT+=taut; SB+=sb
            for i,s in out: sat2[i]=s
    t1=time.time()
    with open('tableB.out','w') as f:
        f.write('# note 109 sec2 rerun (Puck). columns: dead depth even_coords U0 U1 U>=2_one_bit U>=2_both_bits\n')
        for dd in (0,1):
            for d in sorted({x[1] for x in TAB if x[0]==dd}):
                c=[TAB[(dd,d,x)] for x in ('U0','U1','one','both')]
                f.write(f"{'dead' if dd else 'live'} {d} {sum(c)} {c[0]} {c[1]} {c[2]} {c[3]}\n")
        f.write(f"odd |U| count: {ODD}\ntautological (coord covers T with both bits) clause count: {TAUT}\nunit cells with both bits: {SB}\n")
        tot=sum(TAB.values()); f.write(f"total even coords in scope: {tot}\n")
    print(open('tableB.out').read(),'pass1 s',round(t1-t0,1),flush=True)
    dead=[r for r in rows if r[2]>=1 and r[5]]
    s2d=sum(sat2[r[0]] for r in dead); s2l=sum(sat2[r[0]] for r in rows if r[2]>=1 and not r[5])
    cand=[r for r in dead if not sat2[r[0]]]
    print('dead',len(dead),'2sat dead',s2d,'2sat live',s2l,'candidates',len(cand),flush=True)
    res={}
    with Pool(7) as P:
        for idx,d in P.imap_unordered(pass2,[(r[0],r[3],r[4]) for r in cand],chunksize=20):
            if d: res[idx]=d
    t2=time.time()
    with open('checkA_nodes.jsonl','w') as f:
        for idx in sorted(res):
            r=rows[idx]; f.write(json.dumps(dict(row=idx,p=r[1],k=r[2],M=r[3],**res[idx]))+'\n')
    S=collections.Counter()
    for idx,d in res.items():
        S['nodes_L7_witness_D_eq_2^(k+1)_only']+=d['l7_D']==[2**(rows[idx][2]+1)]
        for kk,v in d.items():
            if kk not in('l7_D','min_nodd'): S[kk]+=v
        S['min_nodd_over_all_children']=min(S.get('min_nodd_over_all_children',99),d['min_nodd'])
        S['nodes_open_gt0']+=d['n_open_choices']>0; S['nodes_any_lt2']+=d['n_lt2odd']>0; S['nodes_all_l7']+=d['n_l7']==d['n_cover_choices']
    with open('checkA.out','w') as f:
        f.write(f"CSV-dead k>=1: {len(dead)}; 2-SAT-dead: {s2d}; 2-SAT-dead among live: {s2l}; scanned (dead, not 2-SAT-dead): {len(cand)}\n")
        f.write(f"nodes with >=1 covering child: {len(res)}\n")
        for kk in sorted(S): f.write(f"{kk}: {S[kk]}\n")
    print(open('checkA.out').read(),'pass2 s',round(t2-t1,1),'total s',round(t2-t0,1),flush=True)
