# 14-cover census (part (b) covers) for primes given on the command line. Same engine calls as kcascade_run.py's
# reducible branch (km1roots, km1root), WITHOUT the filterext step. Writes one JSON line per prime.
# usage: python3 km1census.py ./bgk15 WORKERS OUTDIR p1 p2 ...
import subprocess, json, os, sys, time
from concurrent.futures import ThreadPoolExecutor
E, W, OUT, PS = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4:]
os.makedirs(OUT, exist_ok=True)
def run(a): return subprocess.run(a, capture_output=True, text=True)
done = set()
if os.path.exists(f"{OUT}/census14.jsonl"):
    for l in open(f"{OUT}/census14.jsonl"): done.add(json.loads(l)["p"])
for P in PS:
    if int(P) in done: continue
    t0 = time.time()
    roots = [int(l.split()[0]) for l in run([E, P, "km1roots"]).stdout.splitlines()[1:]]
    def one(r):
        f = f"{OUT}/km1_{P}_{r}.txt"; run([E, P, "km1root", str(r), f])
        s = set(l.strip() for l in open(f) if l.strip()); os.remove(f); return s
    covers = set()
    with ThreadPoolExecutor(W) as ex:
        for s in ex.map(one, roots): covers |= s
    open(f"{OUT}/km1_{P}_dedup.txt", "w").write("\n".join(sorted(covers)) + ("\n" if covers else ""))
    rec = dict(p=int(P), roots=len(roots), covers=len(covers), wall_secs=round(time.time() - t0, 1),
               first=sorted(covers)[:3])
    with open(f"{OUT}/census14.jsonl", "a") as fh: fh.write(json.dumps(rec) + "\n")
    print(json.dumps(rec), flush=True)
