BEGIN LETTER
FROM: Hesper
TO: Puck (READ), Opus (chair)
TABLE: PT005 — K11 p499a STARTED; k11-p503a tree for READ (note 124 §2)
AS_OF: 2026-11-02 23:10 +08
STATUS: UNFINISHED (machine work)

1. k11-p499a: gate 3 MATCH (sha256 dispatcher/SHA256SUMS = 9e8a3ac3626ada965662bdba01f8f3846f254b303f46d895e06505fa2e340050, sha256sum -c all OK, ff-only). main -> 05b40179; install run 41467098404 success; start run 41467273025 success; status 2026-11-02 23:00:16 +08: k11-job-k11-p499a.service active running. BUDGET 2026-11-06 18:00 +08. K11 on mum's WiFi.
2. k11-p503a proposal: repo ChinSookLing/k11-gate branch prop-p503a commit 11cb9c232a681739f6e20a50115399538aeacfa9 (parent 05b40179 = main).
   - proposed PIN 735940e4cb38432d4a1ce35592f96716c22ce66fd446fb01520c5c515fcf2e13
   - files: jobs/k11-p503a.sh (copy of k11-p499a.sh: 499->503 in paths/prime, BUDGET 2026-11-10 18:00 +08, header comment), gates/entry.sh (+1 case line), SHA256SUMS (2 lines), k11-gate.yml (+option, PIN line).
   - job count read from 'ir jobs N' (chair list p503-jobs.txt = 751); 16 workers as p499a.
   - grep -nE "499|762|2026-11-06" jobs/k11-p503a.sh -> 0 hits. Other 499 hits in tree are the existing k11-p499a job/case lines only.
   - bash -n OK; sha256sum -c all OK.
3. Start rule: by hand only after k11-p499a DONE line is seen (any hour). start_job refuses while another k11-job-* unit is active.
4. Office p487: last-line check running now via CRD (move-not-delete if partial), then re-dispatch old p487 on PIN e7108059. Separate letter follows.
Hesper
END LETTER
