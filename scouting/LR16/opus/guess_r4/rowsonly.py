# Part (a) row count only (no cascade): sum over engine jobs of raw_irred count. usage: rowsonly.py P WORKERS
import subprocess, re, sys, os, json, time
from concurrent.futures import ThreadPoolExecutor
E="code15/code/bgk15"; P=sys.argv[1]; W=int(sys.argv[2])
run=lambda a: subprocess.run(a,capture_output=True,text=True)
roots=[int(l.split()[0]) for l in run([E,P,"irroots"]).stdout.splitlines()[1:]]
jobs=[(r,int(l.split()[0])) for r in roots for l in run([E,P,"irsubroots",str(r)]).stdout.splitlines()[1:]]
def job(j):
    r,s=j; f=f"/tmp/claude-0/ro_{P}_{r}_{s}.txt"
    o=run([E,P,"irsubrootrawc",str(r),str(s),f]); 
    if o.returncode!=0: raise SystemExit("engine error "+o.stderr[:200])
    m=re.search(r"raw_irred\d+=(\d+) rawscan=(\d+) nodes=(\d+)",o.stdout); os.remove(f) if os.path.exists(f) else None
    return int(m[1]),int(m[3])
t0=time.time()
with ThreadPoolExecutor(W) as ex: res=list(ex.map(job,jobs))
print(json.dumps(dict(p=int(P),jobs=len(jobs),rows=sum(a for a,_ in res),nodes=sum(b for _,b in res),wall=round(time.time()-t0,1))),flush=True)
