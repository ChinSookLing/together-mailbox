#!/usr/bin/env python3
"""Prove HB/C1 v3 differ from v2 (commit 5ccce35) in exactly one line (line 5) = chair text."""
import hashlib, subprocess, sys, os
NEW = ("PUBLICATION STATUS: PUBLISHED \u2014 2026-10-19T09:56:43+08:00. PT-008 internal proof certification: PROVED. "
       "Gates 1\u20133 passed; Hesper independent verification MATCH (5fde1b8). Internally verified, not externally peer-reviewed.")
D = "PT008/round-012/publication/final/"
ok = True
for n in ("HB", "C1"):
    v2 = subprocess.check_output(["git","show",f"5ccce35:{D}{n}-PUBLICATION-FINAL.md"])
    v3 = open(os.path.join(D, f"{n}-PUBLICATION-FINAL-v3.md"),"rb").read()
    a, b = v2.split(b"\n"), v3.split(b"\n")
    diff = [i+1 for i,(x,y) in enumerate(zip(a,b)) if x!=y]
    checks = {
      "same line count": len(a)==len(b),
      "exactly one differing line": len(diff)==1,
      "differing line is 5": diff==[5],
      "line 5 equals chair text": b[4]==NEW.encode("utf-8"),
      "v2 line 5 was stale": b"Not yet published" in a[4],
      "no CR": b"\r" not in v3,
      "ends with single LF": v3.endswith(b"\n") and v2.endswith(b"\n"),
      "v2 sha matches": hashlib.sha256(v2).hexdigest() == {"HB":"53d9f13aa6876b7f5d306701c5e46762030a791c7ab9e5d6fe45d13b5b184399","C1":"fd1f60fa6beac4783fcfc3607105b89af0982804369ecbbff104dde94cfc84e1"}[n],
    }
    print(n, "v3 sha256", hashlib.sha256(v3).hexdigest(), len(v3), "bytes; differing lines:", diff)
    for k,v in checks.items():
        print("  ", "OK  " if v else "FAIL", k); ok &= v
print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
