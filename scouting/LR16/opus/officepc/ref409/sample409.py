# Chair side only: run a fixed sample of p=409 irredundant jobs with the same commands as kcascade_run.py
# (job index i in the engine's own job order with i % 77 == 0 -> 7 jobs), same record format, for cross-check.
import subprocess, re, json, os, time, sys
from concurrent.futures import ThreadPoolExecutor
E, C, P, OUT = "code15/code/bgk15", "code15/code/cascade_k15p", "409", "s409"
os.makedirs(OUT, exist_ok=True); DEAD = time.time() + float(os.environ.get("BUDGET", "1e9"))
def run(a): return subprocess.run(a, capture_output=True, text=True)
roots = [int(l.split()[0]) for l in run([E, P, "irroots"]).stdout.splitlines()[1:]]
jobs = [(r, int(l.split()[0])) for r in roots for l in run([E, P, "irsubroots", str(r)]).stdout.splitlines()[1:]]
sample = [jobs[i] for i in range(len(jobs)) if i % 77 == 0]
print("jobs", len(jobs), "sample", sample, flush=True)
done = set()
if os.path.exists(f"{OUT}/ir.jsonl"):
    for l in open(f"{OUT}/ir.jsonl"): d = json.loads(l); done.add((d["r"], d["s"]))
def job(j):
    if j in done or time.time() > DEAD: return
    r, s = j; f = f"{OUT}/ir_{r}_{s}.txt"
    g = run([E, P, "irsubrootrawc", str(r), str(s), f]).stdout
    m = re.search(r"raw_irred\d+=(\d+) rawscan=(\d+) nodes=(\d+) .*secs=([\d.]+)", g)
    c = run([C, P, "filter", f]); os.remove(f)
    tot = re.search(r"TOTAL rows=(\d+) survivors=(\d+)", c.stderr + c.stdout)
    sl = [l for l in (c.stdout + c.stderr).splitlines() if l.startswith("SURVIVOR")]
    rec = dict(r=r, s=s, rows=int(m[1]), nodes=int(m[3]), secs=float(m[4]), casc_rows=int(tot[1]), casc_survivors=int(tot[2]),
               deep=[l for l in sl if " l16=" in l and " l16=0" not in l], n_survivor_lines=len(sl))
    with open(f"{OUT}/ir.jsonl", "a") as fh: fh.write(json.dumps(rec) + "\n")
    print("done", j, rec["rows"], rec["secs"], flush=True)
with ThreadPoolExecutor(2) as ex: list(ex.map(job, sample))
