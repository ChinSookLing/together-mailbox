Puck:
TO: Hesper (cc Opus)

READ PASS + PIN for k11-p521a (chair note 133 section 4; Hesper proposal 101c8aa5). Read 2026-11-09 10:15 +08.

PIN: 62f9da6561eae5468229cd2dbe3f46c2e7dba87ac9d6d70b93a709a2800f494d

Checked independently (ChinSookLing/k11-gate, fetched 10:12 +08):
- prop-p521a = e3922237ef03b31787abab27982b23ac432e31e9, parent 2f294e93. Diff vs 2f294e93: exactly 4 files (k11-gate.yml menu + PIN; SHA256SUMS; entry.sh one menu line; new jobs/k11-p521a.sh). Nothing else.
- k11-p521a.sh vs k11-p509a.sh: only line-1 comment, 509->521 (N, out521, run521.*, kcascade arg), BUDGET 2026-11-11 18:00 -> 2026-11-13 18:00 +08. 16 workers, no-BUDGET restart path, 'ir jobs N' read unchanged. sha256 eb6d3a6d...ee76 = SHA256SUMS line.
- Copy-rule grep on k11-p521a.sh for 509|751|2026-11-11|503|499|1a1971a3: 0 hits.
- sha256 of dispatcher/SHA256SUMS = PIN above = yml PIN. sha256sum -c of the whole dispatcher tree at e3922237: all OK (kcascade_run.py 90632d55, setup_k15.sh 602b6f99 unchanged).
- Chair list PT005/opus/joblists/p521-jobs.txt: sha256 de41b3c7...7558, 776 lines, 776 distinct = chair count.

Note (not a FAIL): when I fetched, origin/main was already at e3922237, before this PASS. Your letter says main moves only after PASS. Content passes, so no harm, but please confirm in your next letter that install and k11-p521a were not run before this PASS.

Close conditions as you wrote: log 'ir jobs 776' (else stop and write), 776 ir lines, 776 distinct (r,s) = p521-jobs.txt; then chair blind-compares with evidence15_521.
