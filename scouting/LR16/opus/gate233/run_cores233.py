# p=233 core certificate (as chair note 29, P=233): every 15-row containing a canonical 13-class core,
# lifted to level 16 (Astra's lift), each improper lift tested with L7 (shift_ok d=2..16); records the residue pattern.
import subprocess, os, sys, json, time
from concurrent.futures import ThreadPoolExecutor, as_completed
P = 233; n = (P - 1) // 2
rows = [[int(h[2*i:2*i+2], 16) for i in range(14)] for h in open("km1low13_p233.txt").read().split()]
cores = sorted({tuple(sorted(set(r))) for r in rows})
assert all(len(c) == 13 for c in cores)
done = {}
if os.path.exists("cores.jsonl"):
    for l in open("cores.jsonl"):
        try: d = json.loads(l); done[tuple(d["core"])] = d
        except Exception: pass
def job(C):
    inp = "".join("SURVIVOR base: " + " ".join(map(str, sorted(list(C) + [a, b]))) + " l2=0\n" for a in range(1, n+1) for b in range(a, n+1))
    t0 = time.time(); out = subprocess.run(["./pattern233"], input=inp, capture_output=True, text=True).stdout
    tot = [l for l in out.splitlines() if l.startswith("TOTAL")][0].split()
    return dict(core=list(C), rows=int(tot[2]), l16_lifts=int(tot[4]), unhandled=int(tot[6]), rows_unhandled=int(tot[8]),
                patterns=[l for l in out.splitlines() if l.startswith("PATTERN")],
                first_unhandled=[l for l in out.splitlines() if l.startswith("UNHANDLED")][:2], secs=round(time.time()-t0, 1))
todo = [C for C in cores if C not in done]
print("cores", len(cores), "todo", len(todo), flush=True)
with ThreadPoolExecutor(int(os.environ.get("WORKERS", "1"))) as ex:
    for f in as_completed([ex.submit(job, C) for C in todo]):
        r = f.result()
        with open("cores.jsonl", "a") as fh: fh.write(json.dumps(r) + "\n")
