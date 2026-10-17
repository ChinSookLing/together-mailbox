from own import *
import sys,time
p=int(sys.argv[1]); row=list(map(int,sys.argv[2].split(',')))
M=p; lvl=[sorted(row)] if is_open(row,p) else []
viol=[]; t0=time.time(); thr={}
while lvl:
    st=[fstats(w,M,p) for w in lvl]
    nxt=set(); nF3=0
    for w,s in zip(lvl,st):
        ch=open_children(w,M)
        f3=s['F3']; thr[f3]=thr.get(f3,[0,0]); thr[f3][0]+=1; thr[f3][1]+= (len(ch)>0)
        if f3>=9:
            nF3+=1
            if ch: viol.append((M,w,len(ch)))
        nxt|=set(map(tuple,ch))
    print(f"p={p} M={M} open={len(lvl)} maxE={max(s['E'] for s in st)} maxF3={max(s['F3'] for s in st)} F3>=9:{nF3} t={time.time()-t0:.0f}s",flush=True)
    M*=2; lvl=[list(x) for x in sorted(nxt)]
print(f"p={p} VIOLATIONS:",len(viol)); [print(v) for v in viol[:3]]
print(f"p={p} by F3: [nodes, nodes with open child]",dict(sorted(thr.items())))
