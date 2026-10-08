# km1census.py v2 · 14-cover census (the covers of gate part (b)) for the primes given on the command line.
# Same engine calls as the reducible branch of kcascade_run.py (km1roots, then km1root per root), without filterext.
# v2 (after GPT's read FAIL, 2026-10-09): every engine call is checked; per-root line count must equal the engine's
# own "canonical14=" count; temp files are fresh; results are written atomically and re-verified on restart;
# 401 -> 6 and 409 -> 1 are hard assertions. Any failure stops the whole run with a message (exit code 2).
# usage: python3 km1census.py ./bgk15 WORKERS OUTDIR p1 p2 ...
import subprocess, json, os, sys, time, re, hashlib, tempfile
from concurrent.futures import ThreadPoolExecutor

E, W, OUT, PS = sys.argv[1], int(sys.argv[2]), sys.argv[3], [int(x) for x in sys.argv[4:]]
EXPECT = {401: 6, 409: 1}            # from the gate runs (office PC, chair note 43)
if not (1 <= W <= 10): sys.exit("WORKERS must be 1..10")
os.makedirs(OUT, exist_ok=True)
JL = os.path.join(OUT, "census14.jsonl")

class Stop(Exception): pass
def die(msg):
    raise Stop(msg)

def run(args):
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode != 0:
        die(f"engine exit {r.returncode}: {' '.join(args)} | {r.stderr.strip()[:300]}")
    return r.stdout

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()

def atomic_write(path, text):
    d = os.path.dirname(path) or "."
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".tmp_")
    with os.fdopen(fd, "w") as f:
        f.write(text); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)

def load_done():
    """Primes whose JSON line is valid AND whose dedup file still has the recorded sha256 and line count."""
    done = {}
    if not os.path.exists(JL): return done
    for line in open(JL):
        try: d = json.loads(line)
        except Exception: continue                       # a truncated last line is ignored, never fatal
        f = os.path.join(OUT, f"km1_{d.get('p')}_dedup.txt")
        if os.path.exists(f) and sha(f) == d.get("dedup_sha256"):
            n = sum(1 for l in open(f) if l.strip())
            if n == d.get("covers"): done[d["p"]] = d
    return done

def roots_of(P):
    lines = run([E, str(P), "km1roots"]).splitlines()
    m = re.search(r"roots=(\d+)", lines[0]) if lines else None
    if not m: die(f"p={P}: km1roots header not understood: {lines[:1]}")
    roots = [int(l.split()[0]) for l in lines[1:] if l.strip()]
    if len(roots) != int(m[1]) or len(set(roots)) != len(roots):
        die(f"p={P}: km1roots says {m[1]} roots, parsed {len(roots)} ({len(set(roots))} distinct)")
    return roots

def one(P, r):
    fd, f = tempfile.mkstemp(dir=OUT, prefix=f".km1_{P}_{r}_"); os.close(fd); os.remove(f)   # fresh, never reused
    out = run([E, str(P), "km1root", str(r), f])
    m = re.search(r"canonical14=(\d+)", out)
    if not m: die(f"p={P} root={r}: no canonical14= in engine output: {out.strip()[:200]}")
    if not os.path.exists(f):
        if int(m[1]) == 0: return set(), 0
        die(f"p={P} root={r}: engine reports {m[1]} covers but wrote no file")
    s = [l.strip() for l in open(f) if l.strip()]; os.remove(f)
    if len(s) != int(m[1]): die(f"p={P} root={r}: file has {len(s)} lines, engine says {m[1]}")
    return set(s), int(m[1])

def main():
  done = load_done()
  for P in PS:
      if P in done:
          print("skip (verified)", json.dumps(done[P]), flush=True); continue
      t0 = time.time(); roots = roots_of(P)
      with ThreadPoolExecutor(W) as ex:
          parts = list(ex.map(lambda r: one(P, r), roots))
      covers = set().union(*[s for s, _ in parts]) if parts else set()
      if P in EXPECT and len(covers) != EXPECT[P]:
          die(f"p={P}: {len(covers)} covers, but the gate run gave {EXPECT[P]}")
      f = os.path.join(OUT, f"km1_{P}_dedup.txt")
      atomic_write(f, "\n".join(sorted(covers)) + ("\n" if covers else ""))
      rec = dict(p=P, roots=len(roots), covers=len(covers), per_root_sum=sum(n for _, n in parts),
                 dedup_sha256=sha(f), wall_secs=round(time.time() - t0, 1), first=sorted(covers)[:3])
      sep = ""
      if os.path.exists(JL) and os.path.getsize(JL) > 0:
          with open(JL, "rb") as fh:
              fh.seek(-1, 2); sep = "" if fh.read(1) == b"\n" else "\n"    # never glue onto a truncated line
      with open(JL, "a") as fh:
          fh.write(sep + json.dumps(rec) + "\n"); fh.flush(); os.fsync(fh.fileno())
      print(json.dumps(rec), flush=True)
  print("ALL DONE", flush=True)

try:
    main()
except Stop as e:
    print("STOP:", e, flush=True); sys.exit(2)
