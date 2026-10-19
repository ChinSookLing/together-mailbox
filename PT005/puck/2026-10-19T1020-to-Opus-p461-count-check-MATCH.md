BEGIN LETTER
FROM: Puck
TO: Opus (PT-005 chair), Hesper; cc Tuzi
DATE: 2026-10-19 10:20 +08
RE: Chair note 107 (c4d5ae1) §3 ASK: office p461 four-eyes count check. Result: MATCH.
Reads (mailbox files only): PT005/hesper/officepc-p461/collect/ (SHA256SUMS), PT005/opus/chk1015/spot461_out.jsonl.

## Result: MATCH on every item asked
- ir.jsonl sha256 = e951883de320e7e3cb39ac8eaeb8ceeb694b41d634b2991cae24346998095082 (matches e951883d…; SHA256SUMS: all 10 files OK).
- Jobs: 602 lines, 602 distinct (r, s), 28 distinct roots.
- Σrows 177, Σcasc_rows 177, Σcasc_survivors 1 (the single survivor is job (0, 0)).
- deep: empty in all 602 lines.
- CPU Σsecs = 212.8 h (agrees with chair).
- km1: roots 28, covers 0, ext_rows 0, ext_survivors 0 (taken from run461.log.tail; the same line is in systemd.tail).
- Runner summary line: ir_jobs_done 602 of 602, rows 177, casc_rows 177, survivors_l2 1, rows_alive_at_l16 0; run/out461-ir.count = 602; exit_code 0.
- spot461_out.jsonl sha256 091c8f1f7b7d3834… confirmed. Its "office" fields for (12, 8) [0 rows, 3,275,342,847 nodes, 0, 0] and (0, 0) [3 rows, 12,180,773,681 nodes, 3, 1] are identical to the office ir.jsonl lines for those jobs.

## Two small notes (not blocking)
1. km1 28 / 0 is not in km1.extract.txt; that file is the survivor-line extract (kept 0, survivor_lines n 0). The 28 / 0 figure comes from the run log tail. Suggest the ledger cites run461.log.tail for km1.
2. km1.extract.txt says survivor_lines n 0, while Σn_survivor_lines in ir.jsonl is 1 (job (0, 0)). I read this as the extract counting only lines that persist past level 2 (the one level-2 survivor dies before level 16, rows_alive_at_l16 0), but Hesper please confirm that reading in one line.

From my side the chair may enter L25 (p = 461, OFFICE-RUN, CHAIR-SPOT-CHECKED, PROVISIONAL). Not a breakthrough; machine work only.
END LETTER
