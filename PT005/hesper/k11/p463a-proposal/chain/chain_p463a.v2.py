#!/usr/bin/env python3
# chain_p463a.py — Hesper's chain check for k11-p443a -> k11-p463a (Opus letter a379d43, note 106 §2).
# NOT part of the PINned k11-gate tree. Runs in Hesper's sandbox only. Uses no token itself:
# GitHub calls go through Hark's GitHub connector (apicall), only to ChinSookLing/k11-gate.
# v2 2026-10-18: job-by-job compare report-only (Opus 2012 §3, Puck objection 55af412); PIN re-hash of main SHA256SUMS before install.
# Default mode = CHECK ONLY (reads files, prints verdict, dispatches nothing).
# --arm  = after every check passes: dispatch install on main (PINned tree), then status,
#          re-check df + no active job + p443a done, then dispatch gate k11-p463a on main. Nothing else.
#
# Usage: chain_p463a.py <checkpoint_dir> <status_txt> <office_p443_dir> [--arm --pin <PIN>]
#   checkpoint_dir = results branch k11/checkpoint/<run>/checkpoint/k11-p443a/ (collected AFTER p443a ended)
#   status_txt     = status.txt of the same checkpoint run
#   office_p443_dir= together-mailbox PT005/hesper/officepc-p443/collect/p443/
import sys, os, json, re, subprocess, time

EXPECT = dict(jobs=556, rows=993, surv=1, alive16=0, km1_roots=27, km1_covers=0)
KEYS = ("r", "s", "rows", "nodes", "casc_rows", "casc_survivors", "deep", "n_survivor_lines")  # all fields except secs
MIN_FREE_G = 100
OWNER, REPO, WF = "ChinSookLing", "k11-gate", "k11-gate.yml"

def fail(msg):
    print("CHAIN: NO-GO —", msg); print("Do not start p463a. Report to chair (decides at 08:07)."); sys.exit(1)

def load_ir(p):
    rows = [json.loads(l) for l in open(p) if l.strip()]
    return rows, {(d["r"], d["s"]): tuple(json.dumps(d.get(k)) for k in KEYS) for d in rows}

def check(ck, status, office):
    # 1. p443a finished cleanly
    if not os.path.isfile(os.path.join(ck, "k11-p443a.done")): fail("k11-p443a.done missing")
    rows, K = load_ir(os.path.join(ck, "ir.jsonl"))
    if len(rows) != EXPECT["jobs"]: fail(f"ir.jsonl lines {len(rows)} != 556")
    if len(K) != EXPECT["jobs"]: fail(f"distinct (r,s) {len(K)} != 556")
    if sum(d["rows"] for d in rows) != EXPECT["rows"]: fail("sum rows != 993")
    if sum(d["casc_survivors"] for d in rows) != EXPECT["surv"]: fail("sum casc_survivors != 1")
    # 2. log tail totals + km1 line
    tail = open(os.path.join(ck, "run443.log.tail")).read()
    tot = [json.loads(l) for l in tail.splitlines() if l.startswith('{"ir_jobs_done"')]
    if not tot: fail("no totals line in run443.log.tail")
    t = tot[-1]
    if (t["ir_jobs_done"], t["of"], t["rows"], t["survivors_l2"], t["rows_alive_at_l16"]) != (556, 556, 993, 1, 0):
        fail(f"totals line differs: {t}")
    m = re.findall(r"km1: \{'roots': (\d+), 'covers': (\d+)", tail)
    if not m or tuple(map(int, m[-1])) != (27, 0): fail(f"km1 differs: {m}")
    # 3. job SET must equal office p443 (hard); line order may differ, so key by (r,s)
    _, O = load_ir(os.path.join(office, "ir.jsonl"))
    if K.keys() != O.keys(): fail("(r,s) sets differ from office")
    # job-by-job field compare = REPORT ONLY (chair ruling 2012 §3: ledger condition, not a chain stop)
    bad = [k for k in K if K[k] != O[k]]
    print(f"REPORT (not a stop): job-by-job vs office p443 on {KEYS[2:]}: {len(bad)}/556 differ" + (f", first {bad[:3]}" if bad else ""))
    machine(open(status).read())
    print("CHAIN: ALL CHECKS PASS — 556 jobs, 556 distinct, rows 993, survivors 1, alive@16 0, km1 27/0, job set = office p443")

def machine(st):
    if re.search(r"k11-job-\S+\s+loaded\s+active", st): fail("a k11-job unit is still active")
    df = re.search(r"\S+\s+\S+\s+\S+\s+(\d+(?:\.\d+)?)([GT])\s+\d+%\s+/", st)
    if not df: fail("df line not found in status.txt")
    free = float(df.group(1)) * (1024 if df.group(2) == "T" else 1)
    if free < MIN_FREE_G: fail(f"free disk {free}G < {MIN_FREE_G}G")
    print(f"machine: no active k11-job unit, free {free:.0f}G")

def gh(*a):
    out = subprocess.run(["apicall", "github", *a], capture_output=True, text=True).stdout
    try: return json.loads(out)
    except Exception: return out

def dispatch_and_wait(gate):
    t0 = time.time()
    gh("workflow_dispatch", f"owner={OWNER}", f"repo={REPO}", f"workflow_id={WF}", "ref=main",
       "inputs=" + json.dumps({"gate": gate}))
    time.sleep(20)
    for _ in range(60):
        runs = gh("workflow_runs_list", f"owner={OWNER}", f"repo={REPO}", "branch=main", "per_page=5")
        for r in runs.get("workflow_runs", []):
            if r.get("event") == "workflow_dispatch" and time.mktime(time.strptime(r["created_at"], "%Y-%m-%dT%H:%M:%SZ")) - time.timezone >= t0 - 60:
                if r["status"] == "completed":
                    print(f"{gate}: run {r['id']} {r['conclusion']}"); return r
        time.sleep(30)
    fail(f"{gate} run did not complete in 30 min")

if __name__ == "__main__":
    ck, status, office = sys.argv[1:4]
    check(ck, status, office)
    if "--arm" not in sys.argv:
        print("CHECK ONLY (not armed): nothing dispatched."); sys.exit(0)
    pin = sys.argv[sys.argv.index("--pin") + 1]
    wf = gh("contents_get", f"owner={OWNER}", f"repo={REPO}", f"path=.github/workflows/{WF}", "ref=main")
    import base64
    body = base64.b64decode(wf["content"]).decode() if isinstance(wf, dict) and "content" in wf else ""
    if f"PIN: {pin}" not in body or "- k11-p463a" not in body: fail("main does not carry the Puck PIN / p463a menu line")
    import hashlib
    sf = gh("contents_get", f"owner={OWNER}", f"repo={REPO}", "path=dispatcher/SHA256SUMS", "ref=main")
    sums = base64.b64decode(sf["content"]) if isinstance(sf, dict) and "content" in sf else b""
    if hashlib.sha256(sums).hexdigest() != pin: fail("main dispatcher/SHA256SUMS hash != PIN")
    if dispatch_and_wait("install")["conclusion"] != "success": fail("install failed")
    r = dispatch_and_wait("status")
    if r["conclusion"] != "success": fail("status failed")
    import base64
    f = gh("contents_get", f"owner={OWNER}", f"repo={REPO}", f"path=k11/status/{r['id']}/status.txt", "ref=results")
    st = base64.b64decode(f["content"]).decode() if isinstance(f, dict) and "content" in f else ""
    if "installed" not in st and pin[:8] not in st: print("note: status.txt does not print the PIN; relying on install run success")
    machine(st)   # fresh df + no active job, right before start (start_job also refuses if any k11-job unit is active)
    r = dispatch_and_wait("k11-p463a")
    print("k11-p463a dispatched:", r["id"], r["conclusion"])
