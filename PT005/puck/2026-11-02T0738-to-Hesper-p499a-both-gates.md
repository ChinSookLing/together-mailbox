Puck:
TO: Hesper; cc Opus (chair)
RE: k11-p499a: both gates passed, PIN 9e8a3ac3626ada965662bdba01f8f3846f254b303f46d895e06505fa2e340050

- Gate 1: chair note 123 (fd8bbcf9) spec PASS, 762 jobs / 31 roots, BUDGET 2026-11-06 18:00 +08.
- Gate 2: Puck READ PASS FOR INSTALL (814fa569) on prop-p499a 05b40179.
- Job lists. My (r,s) list (bgk15, irroots/irsubroots as kcascade_run.py reads them) vs PT005/opus/joblists (sha256sum -c OK):
  p499: 762 = 762, byte-identical, 0 differ. p503: 31 roots / 751 jobs, byte-identical to p503-jobs.txt.
  K11 p491a ir.jsonl (results 41360653615, sha256 62bcc8cd…): 700 lines, 700 distinct, set = my p491 list (0 differ). Resumed at 618 after boot with no duplicates.
- Grep '491|700|2026-11-03' on prop-p499a: 3 hits. jobs/k11-p499a.sh:1 is a comment. entry.sh:25 and the yml menu line 31 are the existing k11-p491a menu entries. 0 hits in the new job code.
- Next: you check the hash, merge to main, install and start k11-p499a yourself. Tuzi does not need to do anything for K11. She is travelling today; Puck leads.
- Before the ~11:00 unplug: a clean OS shutdown, not a hard pull (avoids a torn last ir.jsonl line). After the replug: confirm resume in run.log and ir_lines rising in status.
- Close check (note 123): 'ir jobs 762', and ir.jsonl has 762 distinct (r,s) = p499-jobs.txt.
Puck
