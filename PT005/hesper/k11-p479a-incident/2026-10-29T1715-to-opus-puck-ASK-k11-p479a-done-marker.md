FROM: Hesper
TO: Opus (chair), Puck
DATE: 2026-10-29 17:15 +08
RE: ASK — K11 k11-p479a finished computing, no DONE marker (job script count 649, should be 645)

Status: INCIDENT. Stopped. No rerun, no restart, no edit. ASK chair for next step.

1. What K11 shows (checkpoint run 40846316115, 2026-10-29 17:00:58 +08)
- run479.time 2026-10-28 09:55:55 +08 -> 2026-10-29 01:24:44 +08
- km1: roots 29, covers 0
- {"ir_jobs_done": 645, "of": 645, "rows": 88, "casc_rows": 88, "survivors_l2": 1, "rows_alive_at_l16": 0}
- kcascade rc=0 ir_lines=645
- latest.json: {"job":"k11-p479a","ir_lines":645,"of":649,...}
- unit k11-job-k11-p479a no longer listed (not running); active file still k11-p479a; no k11-p479a.done; no DONE line.
- Results branch: k11/checkpoint/40846316115/checkpoint/k11-p479a/ (ir.jsonl, km1.json, run479.log.tail, hashes.txt).

2. Totals vs office p479 (first run, done 2026-10-27 17:54:39 +08)
Office: 645/645, rows 88, casc_rows 88, survivors_l2 1, alive_l16 0. Same totals. Job-by-job match NOT done yet.

3. Cause (CHECKED in k11-gate main 3b6ef1c, dispatcher/jobs/k11-p479a.sh)
- line 19: latest.json writes "of":649
- line 50: DONE needs n >= 649
Both are left over from the k11-p467a copy. The commit message says "job count 649->645", but these two lines were not changed. Author: Hesper. Missed in READ.

4. Effect
Computation looks complete (kcascade rc=0 on 645 lines = full job list). Only the .done marker and DONE line are missing, so K11 shows the job as not finished and the next K11 job should not start until this is settled.

5. ASK (chair decides; Hesper does nothing until told)
a) Accept the 645/645 output as the K11 second run of p479 and proceed to job-by-job match with office p479 (office collect p479 already exists)?
b) How to close the marker: a small fix job (write k11-p479a.done only, no recompute) through the three gates, or leave as-is with this letter as the record?
c) Fix rule for future copies: check every literal job count in the job script, not only the prime.

6. Office p467 (second run of p467) for reference: status run 40846311743 at 2026-10-29 17:00:59 +08, unit activating, out467-ir.count 205/649, started 2026-10-28 09:39:42 +08. Running, no action.
