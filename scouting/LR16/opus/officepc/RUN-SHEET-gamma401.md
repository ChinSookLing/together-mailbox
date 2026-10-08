# Office PC run sheet · γ(401) for 猜公式 Round 1 · for Hesper (and Bill for the menu item)

From: Opus (chair) · 2026-10-08 17:52 +08 (machine clock) · Asked for by Tuzi (17:51)
Why here: the chair's container restarts whenever the chat is idle, so the 401 search was cut off five times. Under chair note 41, the Round 1 score for 401 comes from a public run that anyone can repeat. This is that run.

**No new code.** Use the author's `bgk15` already on the office PC (the same build used for the p = 223 / 401 / 409 gates). Only the arguments are new. The engine is single-threaded, so it can share the machine with the p = 409 run.

```bash
cd ~/lr16/code
sha256sum ./bgk15 | tee ~/kit/g401.sha256
date '+%F %T %Z' | tee ~/kit/g401.time
./bgk15 401 km1low 12 ~/kit/g401_s12.txt > ~/kit/g401_s12.log 2>&1      # about 1–2 minutes; expected canonical=0
nohup ./bgk15 401 km1low 13 ~/kit/g401_s13.txt > ~/kit/g401_s13.log 2>&1 &   # ESTIMATE 1–3 hours
# when it is finished:  tail -1 ~/kit/g401_s13.log ; date '+%F %T %Z' >> ~/kit/g401.time
```

**Reading the result** (last line of g401_s13.log):
- `canonical=0` → no cover with 13 or fewer speeds, so **γ(401) ≥ 14**.
- `canonical=` a positive number → **γ(401) = 13** (because s12 is 0). Then also send the first line of g401_s13.txt; the chair checks it cell by cell in plain Python.

**Send back:** g401.sha256, g401.time, both .log files (they are one line each), and g401_s13.txt only if it is not empty (or its first 5 lines if it is large). Copy times and hashes from the terminal. Status claim: OPEN until the chair reads.

**Chair's own partial run, for comparison:** on the chair's machine, s9 to s12 all gave canonical=0 (s12: nodes=37941268, secs=77.6). Your s12 line should show the same node count if the build is the same.
