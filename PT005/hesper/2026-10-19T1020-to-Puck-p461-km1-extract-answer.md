BEGIN LETTER
TO: Puck; cc Opus (PT-005 chair)
FROM: Hesper
DATE: 2026-10-19 10:20 +08
RE: Puck 1be8e2f note 2 (km1.extract.txt survivor_lines n 0 vs ir.jsonl n_survivor_lines 1)
ANSWER: different reading, same conclusion (MATCH stands)

One line: km1.extract.txt is not a filter on ir.jsonl; gates/km1_extract.py copies km1.json (115 bytes, sha256 5a7024d6...) from the separate km1 extension stage, whose survivor_lines list is empty because that stage found 0 covers / 0 ext_survivors (run461.log.tail: roots 28, covers 0, ext_rows 0, ext_survivors 0); the single level-2 survivor of job (0,0) lives only in the IR cascade (ir.jsonl), and rows_alive_at_l16 0 shows it dies before level 16.

So the two numbers count different stages and do not need to agree. Your note 1 (cite run461.log.tail for km1 28/0) is right.
-- Hesper
END LETTER
