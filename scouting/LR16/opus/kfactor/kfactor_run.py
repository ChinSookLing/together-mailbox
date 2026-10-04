# Chair parallel measurement (TEST Opus): irredundant level-one generation at one prime, K=14 vs K=15,
# using the author's unmodified engine (Zenodo 22667683, code/basegen_k_campaign.cpp) built with -DK.
# Usage: python3 kfactor_run.py ENGINE P WORKERS OUTDIR
import subprocess, sys, os, re, time, json
from concurrent.futures import ThreadPoolExecutor
E, P, W, OUT = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
os.makedirs(OUT, exist_ok=True)
def run(a): return subprocess.run([E, P] + a, capture_output=True, text=True).stdout
roots = [int(l.split()[0]) for l in run(["irroots"]).splitlines()[1:]]
jobs = [(r, int(l.split()[0])) for r in roots for l in run(["irsubroots", str(r)]).splitlines()[1:]]
done=set()
if os.path.exists(f"{OUT}/jobs.jsonl"):
    for l in open(f"{OUT}/jobs.jsonl"):
        d=json.loads(l); done.add((d["r"],d["s"]))
print(f"{E} p={P}: roots={len(roots)} jobs={len(jobs)} already_done={len(done)}", flush=True)
alljobs=jobs; jobs=[j for j in jobs if j not in done]
DEADLINE = time.time() + float(os.environ.get('BUDGET', '1e9'))
def job(j):
    if time.time() > DEADLINE: return None
    r, s = j; t0 = time.time()
    out = subprocess.run([E, P, "irsubrootrawc", str(r), str(s), f"{OUT}/ir_{r}_{s}.txt"], capture_output=True, text=True).stdout
    os.remove(f"{OUT}/ir_{r}_{s}.txt")
    m = re.search(r"raw_irred\d+=(\d+) rawscan=(\d+) nodes=(\d+) .*secs=([\d.]+)", out)
    rec = dict(r=r, s=s, rows=int(m[1]), nodes=int(m[3]), secs=float(m[4]), wall=time.time()-t0)
    with open(f"{OUT}/jobs.jsonl", "a") as f: f.write(json.dumps(rec) + "\n")
    return rec
t0 = time.time()
with ThreadPoolExecutor(W) as ex: list(ex.map(job, jobs))
res=[json.loads(l) for l in open(f"{OUT}/jobs.jsonl")]
if len(res) < len(alljobs):
    print(f"PARTIAL {len(res)}/{len(alljobs)}", flush=True); sys.exit(0)
print(json.dumps(dict(engine=E, p=int(P), jobs=len(res), rows=sum(x["rows"] for x in res), nodes=sum(x["nodes"] for x in res),
      cpu_secs=round(sum(x["secs"] for x in res), 1), wall=round(time.time()-t0, 1))), flush=True)
