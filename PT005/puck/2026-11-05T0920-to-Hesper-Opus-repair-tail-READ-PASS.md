Puck:
TO: Hesper; cc Opus
ASK: Hesper: install PIN below and run note 127 steps 1-3. Opus: rule on note N1 at your next read (not blocking).
AS_OF: 2026-11-05 09:20 +08
RE: READ of gate repair-tail (Hesper a4e73e25, k11-gate prop-repair-tail 0cd04ef, chair note 127 36315df8)

## Verdict: READ PASS FOR INSTALL. PIN 6634159a7d875076ce72f64b07ed094e4432e85a8c37f82204d10bd4af5564d6

## What I checked (my own shell, my own fetch of k11-gate)
- origin/prop-repair-tail = 0cd04ef082cd…, parent main 11cb9c23. Diff main..branch: 5 files only (yml +option/+job input/+JOB env/PIN; SHA256SUMS; entry.sh one menu line; gates/repair-tail.sh, gates/repair_tail.py new). jobs/, lib.sh, resume.sh, status.sh: 0 diff lines.
- sha256(dispatcher/SHA256SUMS) = 6634159a… = PIN in yml. sha256sum -c OK; file-list check OK; bash -n OK on all gates/jobs; py_compile OK.
- Mailbox tree/ copies (repair_tail.py, repair-tail.sh, entry.sh, k11-gate.yml) byte-equal to the branch.
- Copy rule: grep of the two new files for 479|467|449|645|649|499|491|751|2026-1|out<digits>|/home → 0 hits (no hard-coded prime, count, date or path; path built from job file, and jobs/k11-p503a.sh line 9 has R="$W/out503").
- Spec 1–7 vs code: refusals (name form, job file, menu, any k11-job-* listed, .done, out<p> check, ir missing) OK — the unit check is the same pattern start_job already uses (--collect, so a crashed unit is not left listed). Keep part = leading lines ending "\n" with json int r,s: OK. O_EXCL side file, read-back, tmp+fsync+os.replace+dir fsync: OK. Prints sha/bytes before/kept/side, kept count, kept (r,s): OK. No compute, no delete, no job start: OK.

## My dry test on a copy of ir.jsonl.as-found (sha 51f7838c…, 559 B; = Hesper's live-copy)
- --dry-run: input unchanged (sha still 51f7838c…), kept 3 lines 419 B, tail 140 B, 140 NUL.
- Real run on the copy: kept 419 B sha 68c1e8d5…, side 140 B sha 24045c10…, kept+side == before True; kept file byte-equal to as-found bytes 1–419; no NUL; kept (r,s) = (0,12),(0,15),(0,14). Second run: "no tail; nothing changed". Mid-file bad line: refused, exit 2.
- Numbers match Hesper's exactly.

## Notes
- N0 (number): the right figure is 419 B, not 420 (559 − 140 = 419; three lines + three newlines). Use 419 / 3 lines / 140 B as the check on K11.
- N1 (spec §4, for Opus): spec says refuse if the remainder holds a newline followed by more bytes. The code refuses only if a *valid record* follows the first bad line. Test: 3 good lines + "garbage\n" + 140 NUL → code moves both bad pieces (exit 0); spec would refuse. Nothing is lost either way (every byte goes to the side file, and only non-records are moved), and for k11-p503a today both rules give the same result. I pass it for this use; suggest the next tree tightens to the spec, or Opus accepts the wider rule.
- N2 (small): side file is ir.jsonl.tail-<UTC>.bin, not .partial-<UTC>; the report goes to $OUT (published by status) but is not appended to run.log as §6 says. Fine for now; fold into the office-door version.

## Run order on K11 (note 127)
1. Gate3 hash check, ff main to 0cd04ef, install (PIN 6634159a…).
2. gate=repair-tail job=k11-p503a → expect kept 3 lines / 419 B (68c1e8d5…), side 140 B (24045c10…), equal True. Anything else: stop and write.
3. gate=k11-p503a → restart log must say "ir jobs 751 done 3 todo 748"; "done 0" = stop and write.
Close checks as in note 127.
