# Opus: compare a re-run of the p=223 core certificate (cores.jsonl) with the chair's (PT005 chair note 29).
import json, sys
mine = {tuple(d["core"]): d for d in map(json.loads, open(sys.argv[1]))}
ref = {tuple(d["core"]): d for d in map(json.loads, open(sys.argv[2]))}
diff = [c for c in ref if c not in mine or (mine[c]["rows"], mine[c]["l16_lifts"], mine[c]["unhandled"]) !=
        (ref[c]["rows"], ref[c]["l16_lifts"], ref[c]["unhandled"])]
extra = [c for c in mine if c not in ref]
print("cores: mine", len(mine), "chair", len(ref), "differing/missing", len(diff), "extra", len(extra))
print("mine totals: rows", sum(d["rows"] for d in mine.values()), "l16_lifts", sum(d["l16_lifts"] for d in mine.values()),
      "unhandled", sum(d["unhandled"] for d in mine.values()))
print("VERDICT:", "MATCH" if not diff and not extra and len(mine) == len(ref) else "CHECK")
