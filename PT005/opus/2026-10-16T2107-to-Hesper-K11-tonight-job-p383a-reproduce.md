BEGIN LETTER
FROM: Opus (chair)
TO: Hesper; cc Puck, Bill, Tuzi
AS_OF: 2026-10-16 21:07 +08 (machine clock)
RE: K11 tonight: reproduce gate p = 383, part (a), as the second machine for L20 (answers 908fa0c)

## Why this job
- L20–L23 are PROVISIONAL because only one machine ran them. A full second run on K11, compared job by job, turns L20 into REPRODUCED. This is the same standard as L10–L14.
- p383 is the smallest of the four (71.1 CPU-hours on the office PC), so it can finish tonight or early in Singapore.

## Job
- **Name:** k11-p383a
- **Build:** the office kit, unchanged.
  - scouting/LR16/opus/officepc/setup_k15.sh at commit 87325af25ed15058e5cf269a1ba96d5d7910258a, sha256 602b6f9943e6775eedd054fe919099c38651b9ea22a0f0d45d230ad7f4f6a4ae.
  - It checks the zip sha256 and the source hashes itself:
    - basegen_k_campaign.cpp 4b48224e…;
    - bgk_incremental_gain.h bd150a98…;
    - cascade_filter_k.cpp 50fa9385….
  - It applies the one-line static_assert patch (ledger L2) and builds bgk15 and cascade_k15p.
  - Record the sha256 of the two binaries and of the patched .cpp. The binaries may differ from the office ones because of -march=native. The patched .cpp must be equal.
- **Runner:** scouting/LR16/opus/officepc/kcascade_run.py, sha256 90632d553b33cfbbc4abe87276393294a450145a6a84fec8b8407db649c1faae (pins.sha256 of the office gate).
- **Command** (in the build directory):

      BUDGET=<seconds from start until 2026-10-17 05:30 +08> python3 kcascade_run.py ./bgk15 ./cascade_k15p 383 16 ~/k11/work/k11-p383a/out383

  - Workers: 16.
  - BUDGET stops new jobs at 05:30, so jobs in flight can end before the 06:00 power-off.
- **Checkpoint:** kcascade_run.py appends one line per finished job to out383/ir.jsonl and skips finished jobs on restart. After power-off, run the same command again without BUDGET (or with a new BUDGET). A job cut mid-run is simply redone; it is at most about 40 minutes. k11-resume.service should restart it after boot. Keep run383.log and run383.time with tee -a, as the office gate does.

## Expected outputs (office PC reference, collect-38060748868)
- **Log:** a km1 line with roots 23, covers 0, ext_rows 0, ext_survivors 0. This is the reducible branch: a second-machine check of γ(383) = 15.
- **out383/ir.jsonl:** 415 lines, one per (r, s) job.
- **Final summary:** {"ir_jobs_done": 415, "of": 415, "rows": 5171, "casc_rows": 5171, "survivors_l2": 2, "rows_alive_at_l16": 0}
- **Collect for the chair:** ir.jsonl, the log tail, run383.time, the binary and patch sha256 lines, and lscpu.

## Chair's comparison
- Job by job on r, s, rows, nodes, casc_rows, casc_survivors and deep, against the office ir.jsonl. Times are not compared.
- 415 of 415 equal, plus km1 covers 0 → propose L20 → REPRODUCED (Tuzi decides).

## Order after p383
p397, then p431, then p443, each as its own job with the same pattern. Office PC p463 is not affected.
END LETTER
