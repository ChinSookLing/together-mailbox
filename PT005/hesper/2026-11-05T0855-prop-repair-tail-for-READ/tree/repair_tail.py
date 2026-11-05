# repair_tail.py (Opus chair note 127, 36315df8). Computes nothing, deletes nothing, starts nothing.
# Usage: python3 repair_tail.py IR_JSONL OUTDIR [--dry-run]
# Keeps the leading run of complete lines: each ends with b"\n" and is one JSON object with integer "r" and "s".
# Everything after that run (the tail) is moved byte for byte to IR_JSONL.tail-<UTC stamp>.bin (created with O_EXCL,
# never overwritten); the kept part is written back to IR_JSONL by atomic replace (tmp + fsync + os.replace + dir fsync).
# Refuses (exit 2, file untouched) if any complete line after the first bad one parses as a record: bad line mid-file.
# Exit 0 with nothing written if there is no tail. --dry-run writes nothing on the input side, only the report in OUTDIR.
import sys, os, json, hashlib, time
def rec(seg):
    if not seg.endswith(b"\n"): return None
    try: d = json.loads(seg.decode("utf-8"))
    except Exception: return None
    if isinstance(d, dict) and type(d.get("r")) is int and type(d.get("s")) is int: return (d["r"], d["s"])
    return None
def info(b): return {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}
def main():
    a = sys.argv[1:]; dry = "--dry-run" in a; a = [x for x in a if x != "--dry-run"]
    if len(a) != 2: print("usage: repair_tail.py IR_JSONL OUTDIR [--dry-run]"); return 2
    ir, out = a; os.makedirs(out, exist_ok=True)
    rep = {"ir": ir, "dry_run": dry, "time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    def done(code, why):
        rep["result"] = why; rep["exit"] = code
        open(os.path.join(out, "repair-tail.json"), "w").write(json.dumps(rep, indent=1) + "\n")
        print(json.dumps(rep, indent=1)); return code
    if not os.path.isfile(ir): return done(2, "refused: ir file missing")
    data = open(ir, "rb").read(); rep["before"] = info(data)
    segs = data.splitlines(keepends=True)
    kept, rs, i = 0, [], 0
    while i < len(segs):
        k = rec(segs[i])
        if k is None: break
        rs.append(k); kept += len(segs[i]); i += 1
    later = [j for j in range(i + 1, len(segs)) if rec(segs[j]) is not None]
    rep["kept_lines"] = len(rs); rep["kept_rs"] = [list(x) for x in rs]
    rep["kept_distinct_rs"] = len(set(rs)); rep["kept_duplicate_rs"] = len(rs) - len(set(rs))
    keep, tail = data[:kept], data[kept:]
    rep["kept"] = info(keep); rep["tail"] = info(tail)
    rep["tail_nul_bytes"] = tail.count(b"\x00"); rep["tail_first_bytes_hex"] = tail[:32].hex()
    if later:
        rep["mid_file_good_lines_after_bad"] = len(later)
        return done(2, "refused: bad line mid-file (complete records follow the first bad line); nothing changed")
    if not tail: return done(0, "no tail: file already all complete lines; nothing changed")
    assert keep + tail == data
    if dry: return done(0, "dry-run: would move tail to side file and keep the leading complete lines")
    side = f"{ir}.tail-{time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())}.bin"
    fd = os.open(side, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    with os.fdopen(fd, "wb") as fh: fh.write(tail); fh.flush(); os.fsync(fh.fileno())
    if open(side, "rb").read() != tail: return done(2, "refused: side file read-back mismatch; ir.jsonl untouched")
    tmp = f"{ir}.repair-tmp"
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    with os.fdopen(fd, "wb") as fh: fh.write(keep); fh.flush(); os.fsync(fh.fileno())
    os.replace(tmp, ir)
    dfd = os.open(os.path.dirname(os.path.abspath(ir)), os.O_RDONLY); os.fsync(dfd); os.close(dfd)
    after, sb = open(ir, "rb").read(), open(side, "rb").read()
    rep["side_file"] = side; rep["after"] = info(after); rep["side"] = info(sb)
    rep["after_plus_side_equals_before"] = hashlib.sha256(after + sb).hexdigest() == rep["before"]["sha256"]
    return done(0, "repaired: tail moved to side file, kept part written back by atomic replace")
if __name__ == "__main__": sys.exit(main())
