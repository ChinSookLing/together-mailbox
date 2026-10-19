import json,random,subprocess,re,sys,os
from concurrent.futures import ThreadPoolExecutor
E_="/home/claude/lr16/code15/code/bgk15"; C="/home/claude/lr16/code15/code/cascade_k15p"
M="/home/claude/together-mailbox/"
F={461:"PT005/hesper/officepc-p461/collect/p461/ir.jsonl"}
rng=random.Random(1015); picks=[]
for p,f in F.items():
    L=[json.loads(x) for x in open(M+f)]
    s=[d for d in L if d['casc_survivors']>0]; picks.append((p,rng.choice(s)))
    picks.append((p,rng.choice([d for d in L if d['casc_survivors']==0])))
def job(a):
    p,d=a; r,s=d['r'],d['s']; f=f"/home/claude/spot461/ir_{p}_{r}_{s}.txt"
    g=subprocess.run([E_,str(p),"irsubrootrawc",str(r),str(s),f],capture_output=True,text=True).stdout
    m=re.search(r"raw_irred\d+=(\d+) rawscan=(\d+) nodes=(\d+) .*secs=([\d.]+)",g)
    c=subprocess.run([C,str(p),"filter",f],capture_output=True,text=True); os.remove(f)
    t=re.search(r"TOTAL rows=(\d+) survivors=(\d+)",c.stderr+c.stdout)
    mine=dict(rows=int(m[1]),nodes=int(m[3]),casc_rows=int(t[1]),casc_survivors=int(t[2]))
    office={k:d[k] for k in mine}
    line=json.dumps(dict(p=p,r=r,s=s,mine=mine,office=office,match=mine==office,my_secs=float(m[4])))
    open("/home/claude/spot461/out.jsonl","a").write(line+"\n")
for p,d in picks: print(p,d['r'],d['s'],d['secs'],d['casc_survivors'])
sys.stdout.flush()
import os
done=set()
if os.path.exists("/home/claude/spot461/out.jsonl"):
    for l in open("/home/claude/spot461/out.jsonl"):
        d=json.loads(l); done.add((d['p'],d['r'],d['s']))
todo=sorted([(p,d) for p,d in picks if (p,d['r'],d['s']) not in done], key=lambda x:x[1]['secs'])
print("todo",[(p,d['r'],d['s']) for p,d in todo]); sys.stdout.flush()
with ThreadPoolExecutor(2) as ex: list(ex.map(job,todo))
print("DONE")
