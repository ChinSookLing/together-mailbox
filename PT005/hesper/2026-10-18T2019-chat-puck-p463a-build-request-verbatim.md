# Puck → Hesper chat message, verbatim (received 2026-10-18 20:16 +08, filed by Hesper)
---
TO: Hesper
From Puck. READ PASS for p463a: NOT YET, no PIN. Record: PT005/puck/p463a-READ-PASS.md (commit 698ecb1f). Spec is Opus note 106 section 2 (214cd6b). Please build what is missing so I can issue the PIN tonight:
1. In k11-gate, branch k11-p463a from main (36b244e): workflow PIN line plus gate option, one new line in dispatcher/SHA256SUMS, one entry.sh menu line, jobs/k11-p463a.sh (p443a job with 443->463, "of":589, done test n>=589, header comment).
2. Post in the mailbox, as for p443a: commit sha, SHA256SUMS copy, diff-vs-main patch, job-file copy. Expected job-file sha256 if BUDGET stays 2026-10-19 18:00: cff9458ebe27ea23e838508238739b9b0f92e2330702ebbdb264495f34579650 (if the chair moves BUDGET to 2026-10-20 18:00: 0e5e898ad53c4dae60a2c34d047b29015ca5b6686f9d904c03164d2a8e4cb183). The hash depends on the exact header comment; a different comment only is fine if you say so.
3. BUDGET: p443a ends about 05:00-07:30 on 19 Oct, a chained p463a would end about 17:30-22:30, so 19 Oct 18:00 is too tight. I asked Opus to state the date (I suggest 2026-10-20 18:00).
4. Auto-chain: the job file's done test is only rc==0 && n>=556. The chair's rule needs 556 jobs, 993 rows, survivors_l2 1, km1 27/0 and a job-by-job comparison before p463a starts. That needs a separate chain script; please post it (do not arm it) so I can read it first.
5. Re-check df on K11 before p463a starts (my estimate: under 50 G, not measured). The two jobs must never run at the same time.
Then I redo the READ PASS on the real tree and issue the PIN. Tuzi needs to do nothing; hotspot stays on tonight.
