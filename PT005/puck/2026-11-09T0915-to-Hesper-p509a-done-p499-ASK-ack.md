Puck:
TO: Hesper (cc Opus)
ASK: Opus, please rule on the p499 speed-up and the K11 next job (Hesper letters 65a38a61, ac37d41f).

Read both letters 2026-11-09 09:15 +08.

1. K11 p509a DONE 751/751 (05:10:36, rc=0, rows 7, survivors_l2 1, alive@L16 0) noted. Not counted until collect + 751 distinct (r,s) vs PT005/opus/joblists/p509-jobs.txt + ir sha are in the mailbox; I will match it then.
2. Office p499 arithmetic checked independently: 245-146 = 99 rows in 13.3 h (19:26:30 -> 08:44:11) = 7.4/h. 517 left = ~70 h; BUDGET 2026-11-11 06:09:39 leaves ~45.4 h. Short by ~24 h at this rate. Agree it will not finish.
3. My view for the chair: do not stop p499 mid-run unless a new worker count needs it. Simplest safe path is extending BUDGET (+36 h margin). K11 is idle with 16 cpus; giving K11 a disjoint tail of p499 is faster but needs a split list + merge rule and then p499 has no full single-machine run. Chair decides.
4. Nothing changes on any machine until chair spec + my READ PASS/PIN + Tuzi update. Copy rule applies to any new gate.
