# TEST (Opus): sampled k-factor. Same seed picks a uniform random sample of irredundant jobs for K=14 and K=15 at prime P;
# estimate total = mean(per-job engine secs) * number of jobs. Resumable; BUDGET seconds per chunk.
import subprocess, sys, os, re, time, json, random
from concurrent.futures import ThreadPoolExecutor
E, P, N, W, OUT = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
os.makedirs(OUT, exist_ok=True); DEAD = time.time() + float(os.environ.get('BUDGET', '1e9'))
def run(a): return subprocess.run([E, P] + a, capture_output=True, text=True).stdout
jf = f"{OUT}/joblist.json"
if not os.path.exists(jf):
    roots = [int(l.split()[0]) for l in run(["irroots"]).splitlines()[1:]]
    jobs = [(r, int(l.split()[0])) for r in roots for l in run(["irsubroots", str(r)]).splitlines()[1:]]
    json.dump(jobs, open(jf, "w"))
jobs = [tuple(j) for j in json.load(open(jf))]
sample = random.Random(20261004).sample(jobs, min(N, len(jobs)))
done = set()
if os.path.exists(f"{OUT}/jobs.jsonl"):
    for l in open(f"{OUT}/jobs.jsonl"): d = json.loads(l); done.add((d["r"], d["s"]))
def job(j):
    if time.time() > DEAD: return
    r, s = j; f = f"{OUT}/ir_{r}_{s}.txt"
    out = run(["irsubrootrawc", str(r), str(s), f]); os.remove(f)
    m = re.search(r"raw_irred\d+=(\d+) rawscan=(\d+) nodes=(\d+) .*secs=([\d.]+)", out)
    with open(f"{OUT}/jobs.jsonl", "a") as fh: fh.write(json.dumps(dict(r=r, s=s, rows=int(m[1]), nodes=int(m[3]), secs=float(m[4]))) + "\n")
with ThreadPoolExecutor(W) as ex: list(ex.map(job, [j for j in sample if j not in done]))
R = [json.loads(l) for l in open(f"{OUT}/jobs.jsonl")]
ms = sum(x["secs"] for x in R) / len(R) if R else 0
print(json.dumps(dict(engine=E, p=int(P), jobs_total=len(jobs), sampled=len(R), of=len(sample),
      mean_secs=round(ms, 2), est_total_secs=round(ms * len(jobs)), mean_nodes=round(sum(x["nodes"] for x in R)/max(1,len(R))))), flush=True)
