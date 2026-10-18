import gzip,csv
def cov(w,T,N): r=(T*w)%N; return 16*min(r,N-r)<N
n=0;single=0;ex=[]
for row in csv.DictReader(gzip.open('/workspace/work/together-mailbox/PT005/hesper/r45/widen/nodes_widen.csv.gz','rt')):
    if row['k']!='1': continue
    p=int(row['p']);M=int(row['M']);ws=list(map(int,row['coords'].split()));t=M//2;N=2*M
    n+=1
    C=[[b for b in (0,1) if cov(w+b*M,t,N)] for w in ws]
    if any(len(c)==2 for c in C): continue
    r=[i for i,c in enumerate(C) if c]
    if len(r)==1 and ws[r[0]]%2==1:
        single+=1
        if len(ex)<2: ex.append((p,M,ws,r,C[r[0]]))
print("k=1 nodes",n,"t=p single-reacher (unit only, no antipodal partner)",single,ex)
