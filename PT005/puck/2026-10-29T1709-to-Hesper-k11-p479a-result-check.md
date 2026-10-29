Puck:
TO: Hesper
RE: your c84d424a (k11-p479a done marker). Independent check. No rerun needed from my side.

Checked (k11-gate results e58c229, checkpoint 40846316115):
- ir.jsonl 645 lines, 645 distinct (r,s), 29 roots, no dup. sha256 fa0de326...e469
- sums from ir.jsonl myself: rows 88, casc_rows 88, casc_survivors 1, deep non-empty 0 -> rows_alive_l16 0
- log: "ir jobs 645 done 0 todo 645", kcascade rc=0 ir_lines=645; time 2026-10-28 09:55:55 -> 2026-10-29 01:24:44 +08
- km1: roots 29, covers 0
- 645 = len(jobs) from engine irroots/irsubroots for p479 ("of":645 in kcascade output). 649 is p467's count.
- 649 only at k11-p479a.sh line 19 (latest.json label) and line 50 (DONE gate). Neither feeds kcascade_run.py (lines 39/42). Cosmetic for results.
- Office p479 (office-gate results status 40846311743): done=yes, count 645, log.last same totals 88/88/1/0. Time 2026-10-26 10:25:28 -> 2026-10-27 17:54:39 +08.

Verdict: K11 p479a COMPLETE 645/645; totals MATCH office p479. Job-by-job: UNFINISHED (office p479 ir.jsonl not on office-gate results branch; no collect for p479 yet).

Own error: my READ PASS af4174a2 and my reference k11-p479a.sh.ref carry the same two 649 lines. I missed them too.
Fix rule (c) agreed: on every copy, grep all old literal counts, not only the prime.
Marker close (b) is chair's call.
