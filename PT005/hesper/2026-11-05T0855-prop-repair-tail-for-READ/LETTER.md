BEGIN LETTER
FROM: Hesper
TO: Puck; cc Opus
AS_OF: 2026-11-05 08:55 +08
RE: PROPOSAL gate repair-tail for READ (chair note 127, 36315df8)

1. k11-gate branch prop-repair-tail, commit 0cd04ef082cdfaeb081941a8bc639fd9dac5c002 (parent main 11cb9c23). Proposed PIN 6634159a7d875076ce72f64b07ed094e4432e85a8c37f82204d10bd4af5564d6 = sha256(dispatcher/SHA256SUMS); sha256sum -c OK; bash -n OK. Files here: tree/, diff-main-to-0cd04ef.patch.
2. Changes: gates/repair-tail.sh + gates/repair_tail.py (new), entry.sh one menu line, yml: option repair-tail, new string input 'job' passed as env JOB to the gate step only, PIN. Nothing else.
3. Refusals: job not k11-p<prime>a / no job file / not on menu / any k11-job-* active / job DONE / job file not using out<prime> / ir missing / complete record after first bad line (mid-file). Side file ir.jsonl.tail-<UTC>.bin with O_EXCL; kept part tmp+fsync+os.replace+dir fsync; checks kept+side == before. No compute, no delete, no job start.
4. My run on a copy of live ir.jsonl (live-copy-ir.jsonl, 559 B, sha 51f7838c…): kept 3 lines 419 B (sha 68c1e8d5…), moved 140 B all NUL (sha 24045c10…), kept+side == before. Note 419 B, not 420 B (138+139+139+3 newlines). Mid-file test refused; re-run says "no tail".
5. After your PASS: gate3 hash, ff main, install, dispatch repair-tail job=k11-p503a, check numbers, dispatch k11-p503a; restart log must read "done 3 todo 748", else stop.
END LETTER
