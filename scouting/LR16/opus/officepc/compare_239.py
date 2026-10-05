# PT005 office PC kit (Opus): compare an office-PC p=239 K=15 run with the chair's run (ledger L2).
# Usage: python3 compare_239.py OUTDIR CHAIR_ir_K15_p239.jsonl CHAIR_km1_K15_p239.json
import json, sys
out, chair_ir, chair_km1 = sys.argv[1:4]
mine = {(d["r"], d["s"]): d for d in map(json.loads, open(f"{out}/ir.jsonl"))}
ref = {(d["r"], d["s"]): d for d in map(json.loads, open(chair_ir))}
diff = [k for k in ref if k not in mine or (mine[k]["rows"], mine[k]["nodes"], mine[k]["casc_survivors"]) !=
        (ref[k]["rows"], ref[k]["nodes"], ref[k]["casc_survivors"])]
print("irredundant jobs: mine", len(mine), "chair", len(ref), "differing or missing", len(diff), diff[:5])
print("rows", sum(d["rows"] for d in mine.values()), "level-2 survivors", sum(d["casc_survivors"] for d in mine.values()),
      "alive at level 16", sum(len(d["deep"]) for d in mine.values()))
print("generation CPU-s (sum over jobs):", round(sum(d["secs"] for d in mine.values()), 1))
a, b = json.load(open(f"{out}/km1.json")), json.load(open(chair_km1))
for k in ("roots", "covers", "ext_rows", "ext_survivors"):
    print("reducible", k, "mine", a[k], "chair", b[k], "OK" if a[k] == b[k] else "DIFFERENT")
print("VERDICT:", "MATCH" if not diff and all(a[k] == b[k] for k in ("roots", "covers", "ext_rows", "ext_survivors"))
      and len(mine) == len(ref) else "CHECK")
