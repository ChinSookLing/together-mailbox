# TEST (Opus) scouting: full level-one generation + binary-lifting cascade for K=15 at one prime,
# with the author's engine (unmodified) and the cascade (scouting copy: only the K<=14 static_assert relaxed).
# Resumable; stops starting new jobs after BUDGET seconds. Usage: kcascade_run.py ENGINE CASCADE P WORKERS OUT
import subprocess, sys, os, re, time, json
from concurrent.futures import ThreadPoolExecutor
E, C, P, W, OUT = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5]
os.makedirs(OUT, exist_ok=True); DEAD = time.time() + float(os.environ.get('BUDGET', '1e9'))
def run(a): return subprocess.run(a, capture_output=True, text=True)
def surv_lines(err_out):
    return [l for l in err_out.splitlines() if l.startswith("SURVIVOR")]
# --- reducible branch (decomposition variant): km1root jobs, dedupe, filterext ---
if os.environ.get("SKIP_KM1") != "1" and not os.path.exists(f"{OUT}/km1.json"):
    roots = [int(l.split()[0]) for l in run([E, P, "km1roots"]).stdout.splitlines()[1:]]
    covers = set(); secs = 0.0
    for r in roots:
        o = run([E, P, "km1root", str(r), f"{OUT}/km1_{r}.txt"]).stdout
        secs += float(re.search(r"secs=([\d.]+)", o)[1])
        covers.update(l.strip() for l in open(f"{OUT}/km1_{r}.txt") if l.strip()); os.remove(f"{OUT}/km1_{r}.txt")
    open(f"{OUT}/km1_dedup.txt", "w").write("\n".join(sorted(covers)) + "\n")
    c = run([C, P, "filterext", f"{OUT}/km1_dedup.txt"])
    tot = re.search(r"TOTAL rows=(\d+) survivors=(\d+)", c.stderr + c.stdout)
    json.dump(dict(roots=len(roots), covers=len(covers), gen_secs=secs, ext_rows=int(tot[1]), ext_survivors=int(tot[2]),
                   survivor_lines=surv_lines(c.stdout + c.stderr)), open(f"{OUT}/km1.json", "w"))
if os.path.exists(f"{OUT}/km1.json"): print("km1:", {k: v for k, v in json.load(open(f"{OUT}/km1.json")).items() if k != "survivor_lines"}, flush=True)
# --- irredundant branch: generate + cascade per job ---
roots = [int(l.split()[0]) for l in run([E, P, "irroots"]).stdout.splitlines()[1:]]
jobs = [(r, int(l.split()[0])) for r in roots for l in run([E, P, "irsubroots", str(r)]).stdout.splitlines()[1:]]
done = set()
if os.path.exists(f"{OUT}/ir.jsonl"):
    for l in open(f"{OUT}/ir.jsonl"): d = json.loads(l); done.add((d["r"], d["s"]))
todo = [j for j in jobs if j not in done]
print(f"ir jobs {len(jobs)} done {len(done)} todo {len(todo)}", flush=True)
def job(j):
    if time.time() > DEAD: return
    r, s = j; f = f"{OUT}/ir_{r}_{s}.txt"
    g = run([E, P, "irsubrootrawc", str(r), str(s), f]).stdout
    m = re.search(r"raw_irred\d+=(\d+) rawscan=(\d+) nodes=(\d+) .*secs=([\d.]+)", g)
    c = run([C, P, "filter", f]); os.remove(f)
    tot = re.search(r"TOTAL rows=(\d+) survivors=(\d+)", c.stderr + c.stdout)
    sl = surv_lines(c.stdout + c.stderr)
    rec = dict(r=r, s=s, rows=int(m[1]), nodes=int(m[3]), secs=float(m[4]), casc_rows=int(tot[1]), casc_survivors=int(tot[2]),
               deep=[l for l in sl if " l16=" in l and " l16=0" not in l], n_survivor_lines=len(sl))
    with open(f"{OUT}/ir.jsonl", "a") as fh: fh.write(json.dumps(rec) + "\n")
with ThreadPoolExecutor(W) as ex: list(ex.map(job, todo))
R = [json.loads(l) for l in open(f"{OUT}/ir.jsonl")]
print(json.dumps(dict(ir_jobs_done=len(R), of=len(jobs), rows=sum(x["rows"] for x in R), casc_rows=sum(x["casc_rows"] for x in R),
      survivors_l2=sum(x["casc_survivors"] for x in R), rows_alive_at_l16=sum(len(x["deep"]) for x in R))), flush=True)
