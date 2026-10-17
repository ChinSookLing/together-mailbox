# Extract partial info for deferred/capped roots into partial_info.jsonl, then drop their memo-only entries.
import pickle,time,os,json,sys
sys.path.insert(0,'/workspace/work/r45')
from hesper_r45 import fvec
t=time.time(); st=pickle.load(open('state_widen.pkl','rb')); ch=st['children']
have=set()
if os.path.exists('partial_info.jsonl'):
    for l in open('partial_info.jsonl'): have.add(json.loads(l)['label'])
done_reach=set()
for lab,p,M,w in st['roots']:
    if st['status'].get(lab)=='done':
        stack=[(p,M,tuple(sorted(w)))]
        while stack:
            k=stack.pop()
            if k in done_reach: continue
            done_reach.add(k); stack.extend(ch[k])
out=open('partial_info.jsonl','a'); drop=0
for lab,p,M,w in st['roots']:
    s=st['status'].get(lab)
    if s not in ('deferred','capped'): continue
    lev=[(p,M,tuple(sorted(w)))]; sizes=[]; withkids=[]; vis=[]
    while lev and all(k in ch for k in lev):
        vis+=lev
        for k in lev:
            if ch[k]: withkids.append((k, len(ch[k])))
        nxt=set()
        for k in lev: nxt.update(ch[k])
        lev=sorted(nxt); sizes.append((lev[0][1]//p if lev else None, len(lev)))
    if lab not in have:
        rec={'label':lab,'status':s,'p':p,'M':M,'levels_after_root':sizes,
             'nodes_with_open_child':[[k[1],' '.join(map(str,k[2])),n,fvec(list(k[2]),k[1],p)] for k,n in withkids]}
        out.write(json.dumps(rec)+'\n')
    for k in vis:
        if k not in done_reach and k in ch: del ch[k]; drop+=1
out.close()
canon={k:k for k in ch}
for k in list(ch): ch[k]=[canon.get(c,c) for c in ch[k]]
with open('state_widen.pkl.prune.tmp','wb') as f: pickle.dump(st,f,protocol=4)
os.replace('state_widen.pkl.prune.tmp','state_widen.pkl'); print('dropped',drop,len(ch),round(time.time()-t,1))
