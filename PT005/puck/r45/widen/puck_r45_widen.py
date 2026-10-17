# Puck independent rerun of Hesper R45 Track A widen table. Engine: Puck's r43f3 puck_f3_check.open_children (no Hesper code).
# Roots: roots_widen.txt (label p M coords). Roots with status capped/deferred in summary_widen.txt are skipped (statuses taken from his log).
import sys, os, re, time, hashlib, multiprocessing as mp
sys.path.insert(0,'/workspace/mbx_pt5/PT005/puck/r43f3/check')
from puck_f3_check import open_children, open_direct, v2
W='/workspace/mbx_pt5/PT005/hesper/r45/widen/'
OUT='/workspace/r45_widen_puck/'
def work(k):
    kids,_=open_children(list(k[2]),k[1]); return k,[(k[0],2*k[1],c) for c in kids]
def fvec(w,M,p):
    k=(M//p).bit_length()-1
    d=[k-v2(x) if v2(x)<k else 0 for x in w]
    return [sum(1 for x in w if v2(x)>=k)]+[sum(1 for t in d if t>=j) for j in range(1,6)]
if __name__=='__main__':
    t0=time.time()
    skip=set(re.findall(r'^  (?:CAPPED|DEFERRED) root (\S+) ',open(W+'summary_widen.txt').read(),re.M))
    print('skip',len(skip),flush=True)
    roots=[]
    for line in open(W+'roots_widen.txt'):
        f=line.split()
        if not f: continue
        roots.append((f[0],int(f[1]),int(f[2]),tuple(sorted(map(int,f[3:])))))
    print('roots',len(roots),flush=True)
    live=[(lab,(p,M,w)) for lab,p,M,w in roots if lab not in skip]
    print('live',len(live),flush=True)
    ch={}
    level=sorted(set(k for _,k in live))
    # root openness check
    bad=[l for l,k in live if not open_direct(list(k[2]),k[1])]
    print('roots not open:',len(bad),flush=True)
    with mp.get_context('fork').Pool(8) as pool:
        while level:
            need=[k for k in level if k not in ch]
            for k,v in pool.imap_unordered(work,need,chunksize=16): ch[k]=v
            nxt=set()
            for k in level: nxt.update(ch[k])
            print('level done',level[0][1]//level[0][0] if level else 0,len(level),'->',len(nxt),round(time.time()-t0),flush=True)
            level=sorted(nxt)
    # all nodes
    nodes=set(ch)
    # survival
    surv={}
    for k in sorted(nodes,key=lambda k:-(k[1]//k[0])):
        surv[k]=0 if not ch[k] else 1+max(surv[c] for c in ch[k])
    # sources: first root (in roots order) reaching node, and full set
    src={}
    for lab,k in live:
        st=[k]
        while st:
            x=st.pop(); s=src.setdefault(x,[])
            if s and s[-1]==lab: continue
            s.append(lab); st.extend(ch[x])
    rows=sorted(nodes,key=lambda k:(k[0],k[1],k[2]))
    nl=''.join(f"{p} {M} {' '.join(map(str,w))}\n" for p,M,w in rows)
    open(OUT+'puck_nodelist_widen.txt','w').write(nl)
    print('NODES',len(rows),'SHA256_NODELIST',hashlib.sha256(nl.encode()).hexdigest(),flush=True)
    with open(OUT+'puck_nodes_widen.csv','w') as f:
        f.write('p,k,M,coords,F0,F1,F2,F3,F4,F5,n_open_children,survival_depth,first_source\n')
        for k in rows:
            p,M,w=k
            f.write(f"{p},{(M//p).bit_length()-1},{M},{' '.join(map(str,w))},{','.join(map(str,fvec(w,M,p)))},{len(ch[k])},{surv[k]},{src[k][0]}\n")
    W5=(17,544,tuple(sorted([189,224,72,447,176,500,144,128,384,266,80,64,48,32,16])))
    ex=[];f0z=0;spos=0
    for k in rows:
        p,M,w=k; kk=(M//p).bit_length()-1; F=fvec(w,M,p)
        if surv[k]>0:
            spos+=1
            if F[0]==0: f0z+=1
        if kk>=1 and surv[k]>0 and k!=W5:
            z=(1 if F[0]>0 else 0)+F[4]/8
            if F[4]>=1 or z>1: ex.append(k)
    with open(OUT+'puck_exceptions_widen.tsv','w') as f:
        f.write('p\tlevel\tM\tcoords\tF0..F5\tn_open_children\tsurvival\tZ\tsources\n')
        for k in ex:
            p,M,w=k;F=fvec(w,M,p);z=(1 if F[0]>0 else 0)+F[4]/8
            f.write(f"{p}\t{M//p}p\t{M}\t{' '.join(map(str,w))}\t{','.join(map(str,F))}\t{len(ch[k])}\t{surv[k]}\t{z}\t{src[k][0]}\n")
    print('SURV>0',spos,'F0=0 among them',f0z,'EXCEPTIONS',len(ex),flush=True)
    import collections
    print(collections.Counter((k[0],k[1]//k[0]) for k in ex),flush=True)
    print('W5 in nodes',W5 in nodes,'SECS',round(time.time()-t0),flush=True)
