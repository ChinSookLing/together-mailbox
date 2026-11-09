#!/usr/bin/env python3
"""Compare our per-job ir.jsonl (K11 and office) with Allikvere's evidence15_<p>_s0 packages.
Per job (r,s): rows, nodes, survivors. His side:
  rows_ir/ir_r_s.txt.log  -> raw_irred15=<rows> nodes=<nodes>
  rows_ir/ir_r_s.txt      -> line count (rows)
  filt/ir_r_s.stats       -> rows=<rows> survivors=<survivors>
Ours: rows, nodes, casc_survivors.
Also his SUMMARY*.json base_family totals and status."""
import json, os, re, sys, glob

EV = sys.argv[1]      # dir holding x<p>/
OURS = sys.argv[2]    # dir holding k11_<p>.jsonl, off_<p>.jsonl
primes = [int(x) for x in sys.argv[3].split(',')]

def his(p):
    base = os.path.join(EV, f"x{p}", f"out15_{p}")
    jobs = {}
    for lg in glob.glob(os.path.join(base, "rows_ir", "ir_*_*.txt.log")):
        m = re.search(r"ir_(\d+)_(\d+)\.txt\.log$", lg)
        r, s = int(m.group(1)), int(m.group(2))
        t = open(lg).read()
        mm = re.search(r"raw_irred15=(\d+).*?nodes=(\d+)", t)
        txt = lg[:-4]
        nlines = sum(1 for l in open(txt) if l.strip()) if os.path.exists(txt) else None
        st = os.path.join(base, "filt", f"ir_{r}_{s}.stats")
        surv = srows = None
        if os.path.exists(st):
            m2 = re.search(r"done: rows=(\d+) survivors=(\d+)", open(st).read())
            if m2:
                srows, surv = int(m2.group(1)), int(m2.group(2))
        jobs[(r, s)] = dict(rows=int(mm.group(1)), nodes=int(mm.group(2)), lines=nlines,
                            srows=srows, surv=surv)
    summ = {}
    for name in ("SUMMARY.json", "SUMMARY_nokill.json"):
        f = os.path.join(base, name)
        if os.path.exists(f):
            summ[name] = json.load(open(f))
    return jobs, summ

def ours(path):
    d = {}
    for l in open(path):
        if not l.strip():
            continue
        j = json.loads(l)
        k = (j["r"], j["s"])
        if k in d:
            raise SystemExit(f"duplicate {k} in {path}")
        d[k] = dict(rows=j["rows"], nodes=j["nodes"], surv=j["casc_survivors"])
    return d

out = []
allok = True
for p in primes:
    H, summ = his(p)
    bf = summ.get("SUMMARY.json", summ.get("SUMMARY_nokill.json", {})).get("base_family", {})
    status = summ.get("SUMMARY.json", {}).get("status")
    # internal consistency of his package
    inner = sum(1 for v in H.values() if not (v["rows"] == v["lines"] == v["srows"]))
    line = dict(p=p, his_jobs=len(H), his_status=status,
                his_bf_jobs=bf.get("irredundant_jobs"), his_bf_rows=bf.get("irredundant_rows"),
                his_bf_nodes=bf.get("irredundant_nodes"),
                his_sum_rows=sum(v["rows"] for v in H.values()),
                his_sum_nodes=sum(v["nodes"] for v in H.values()),
                his_sum_surv=sum(v["surv"] or 0 for v in H.values()),
                his_inner_mismatch=inner)
    for tag in ("k11", "off"):
        f = os.path.join(OURS, f"{tag}_{p}.jsonl")
        if not os.path.exists(f):
            line[tag] = "absent"
            continue
        O = ours(f)
        diff = []
        if set(O) != set(H):
            diff.append(f"jobset ours-his={len(set(O)-set(H))} his-ours={len(set(H)-set(O))}")
        for k in sorted(set(O) & set(H)):
            for fld in ("rows", "nodes", "surv"):
                if O[k][fld] != H[k][fld]:
                    diff.append(f"{k} {fld} ours={O[k][fld]} his={H[k][fld]}")
        line[tag] = dict(jobs=len(O), sum_rows=sum(v["rows"] for v in O.values()),
                         sum_nodes=sum(v["nodes"] for v in O.values()),
                         sum_surv=sum(v["surv"] for v in O.values()),
                         ndiff=len(diff), first_diffs=diff[:5])
        if diff:
            allok = False
    out.append(line)
    k = line.get("k11", {}); o = line.get("off", {})
    print(p, "his", line["his_jobs"], line["his_sum_rows"], line["his_sum_nodes"], line["his_sum_surv"],
          "status", status, "inner", inner,
          "| k11", k if isinstance(k, str) else (k["jobs"], k["ndiff"]),
          "| off", o if isinstance(o, str) else (o["jobs"], o["ndiff"]))
json.dump(out, open(os.path.join(OURS, "..", "cmp_allik_result.json"), "w"), indent=1)
print("ALL_MATCH" if allok else "DIFFS_FOUND")
