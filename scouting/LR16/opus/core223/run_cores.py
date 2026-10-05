# Opus: GPT's core certificate U(C) at p = 223 (PT005 brainstorm): for every canonical core C (a support of
# <= 13 classes that covers all time classes; from `bgk15 223 km1low 13`), check every 15-row containing C with
# Astra's level-16 enumeration + L7 criterion (shift_rows223 = Astra's lift/shift_ok, p = 223). Resumable.
import subprocess, os, sys, json, time
from concurrent.futures import ThreadPoolExecutor
P = 223; n = (P - 1) // 2
S = sys.argv[1]; DEAD = time.time() + float(os.environ.get("BUDGET", "1e9"))
rows = [[int(h[2*i:2*i+2], 16) for i in range(14)] for h in open(S).read().split()]
cores = sorted({tuple(sorted(set(r))) for r in rows})
done = {}
if os.path.exists("cores.jsonl"):
    for l in open("cores.jsonl"): d = json.loads(l); done[tuple(d["core"])] = d
def job(C):
    if C in done or time.time() > DEAD: return
    lines = ["SURVIVOR base: " + " ".join(map(str, sorted(list(C) + [a, b]))) + " l2=0"
             for a in range(1, n + 1) for b in range(a, n + 1)]
    t0 = time.time()
    out = subprocess.run(["./shift_rows223"], input="\n".join(lines) + "\n", capture_output=True, text=True).stdout
    tot = [l for l in out.splitlines() if l.startswith("TOTAL")][0].split()
    rec = dict(core=list(C), rows=int(tot[2]), l16_lifts=int(tot[4]), unhandled=int(tot[6]),
               rows_unhandled=int(tot[8]), secs=round(time.time() - t0, 1),
               first_unhandled=[l for l in out.splitlines() if l.startswith("UNHANDLED")][:2])
    with open("cores.jsonl", "a") as f: f.write(json.dumps(rec) + "\n")
with ThreadPoolExecutor(2) as ex: list(ex.map(job, cores))
R = [json.loads(l) for l in open("cores.jsonl")]
print(json.dumps(dict(cores_done=len(R), of=len(cores), rows=sum(r["rows"] for r in R),
      l16_lifts=sum(r["l16_lifts"] for r in R), unhandled=sum(r["unhandled"] for r in R),
      secs=round(sum(r["secs"] for r in R), 1))))
