# Opus: GPT's core certificate U(C) at p = 223 (PT005 brainstorm): for every canonical core C (a support of
# <= 13 classes that covers all time classes; from `bgk15 223 km1low 13`), check every 15-row containing C with
# Astra's level-16 enumeration + L7 criterion (shift_rows223 = Astra's lift/shift_ok, p = 223). Resumable.
# v3 (2026-10-05 22:24): P from the environment, checker ./shift_rows{P}; nothing else changed.
# v2 (2026-10-05, after DeepSeek's read, wall 111-114): stray indent removed; every core is checked to have exactly
# 13 distinct classes in 1..n before anything runs; only the main thread writes cores.jsonl (no interleaved appends);
# a damaged last line of cores.jsonl (interrupted run) is reported and that core is simply redone.
# Rows are MULTISETS of classes on purpose: a, b may repeat each other or a core class (two different integer speeds
# can share a class mod p, e.g. 5 and 218); the author's own filterext extension also adds every class 1..n.
import subprocess, os, sys, json, time
from concurrent.futures import ThreadPoolExecutor, as_completed
P = int(os.environ.get("P", "223")); n = (P - 1) // 2   # v3: prime from the environment (default 223)
S = sys.argv[1]  # canonical <=13-class covers from `bgk15 223 km1low 13 FILE`
DEAD = time.time() + float(os.environ.get("BUDGET", "1e9"))
rows = [[int(h[2*i:2*i+2], 16) for i in range(14)] for h in open(S).read().split()]
cores = sorted({tuple(sorted(set(r))) for r in rows})
bad = [c for c in cores if len(c) != 13 or not all(1 <= x <= n for x in c)]
if bad: sys.exit(f"STOP: {len(bad)} cores are not 13 distinct classes in 1..{n}, e.g. {bad[0]}")
print(f"cores {len(cores)} (expected 65), all 13 distinct classes", flush=True)
done = {}
if os.path.exists("cores.jsonl"):
    for k, l in enumerate(open("cores.jsonl")):
        try: d = json.loads(l); done[tuple(d["core"])] = d
        except Exception: print(f"NOTE: cores.jsonl line {k+1} unreadable (interrupted?); that core will be redone", flush=True)
def job(C):
    if time.time() > DEAD: return None
    lines = ["SURVIVOR base: " + " ".join(map(str, sorted(list(C) + [a, b]))) + " l2=0"
             for a in range(1, n + 1) for b in range(a, n + 1)]
    t0 = time.time()
    out = subprocess.run([f"./shift_rows{P}"], input="\n".join(lines) + "\n", capture_output=True, text=True).stdout
    tot = [l for l in out.splitlines() if l.startswith("TOTAL")][0].split()
    return dict(core=list(C), rows=int(tot[2]), l16_lifts=int(tot[4]), unhandled=int(tot[6]),
                rows_unhandled=int(tot[8]), secs=round(time.time() - t0, 1),
                first_unhandled=[l for l in out.splitlines() if l.startswith("UNHANDLED")][:2])
todo = [C for C in cores if C not in done]
with ThreadPoolExecutor(int(os.environ.get("WORKERS", "2"))) as ex:
    futs = [ex.submit(job, C) for C in todo]
    for f in as_completed(futs):
        rec = f.result()
        if rec is None: continue
        with open("cores.jsonl", "a") as fh: fh.write(json.dumps(rec) + "\n")   # main thread only
        done[tuple(rec["core"])] = rec
R = list(done.values())
print(json.dumps(dict(cores_done=len(R), of=len(cores), rows=sum(r["rows"] for r in R),
      l16_lifts=sum(r["l16_lifts"] for r in R), unhandled=sum(r["unhandled"] for r in R),
      rows_unhandled=sum(r["rows_unhandled"] for r in R), secs=round(sum(r["secs"] for r in R), 1))))
