# Opus: compare a re-run of the p=223 core certificate (cores.jsonl) with the chair's (PT005 chair note 29).
# v2 (after DeepSeek's read): compares EVERY field except the timing "secs" (rows, l16_lifts, unhandled,
# rows_unhandled, first_unhandled), and reports duplicate or unreadable lines in either file instead of hiding them.
import json, sys
FIELDS = ("rows", "l16_lifts", "unhandled", "rows_unhandled", "first_unhandled")
def load(path):
    d, dup, badl = {}, 0, 0
    for l in open(path):
        if not l.strip(): continue
        try: x = json.loads(l)
        except Exception: badl += 1; continue
        k = tuple(x["core"]); dup += k in d; d[k] = x
    return d, dup, badl
mine, dm, bm = load(sys.argv[1]); ref, dr, br = load(sys.argv[2])
diff = [c for c in ref if c not in mine or any(mine[c].get(f) != ref[c].get(f) for f in FIELDS)]
extra = [c for c in mine if c not in ref]
print("cores: mine", len(mine), "chair", len(ref), "differing/missing", len(diff), "extra", len(extra),
      "| duplicates mine/chair", dm, dr, "| unreadable lines mine/chair", bm, br)
for c in diff[:3]: print("DIFF", list(c), {f: (mine.get(c, {}).get(f), ref[c].get(f)) for f in FIELDS})
print("mine totals: rows", sum(d["rows"] for d in mine.values()), "l16_lifts", sum(d["l16_lifts"] for d in mine.values()),
      "unhandled", sum(d["unhandled"] for d in mine.values()), "rows_unhandled", sum(d["rows_unhandled"] for d in mine.values()))
ok = not diff and not extra and len(mine) == len(ref) and dm == dr == 0 and bm == br == 0
print("VERDICT:", "MATCH" if ok else "CHECK")
