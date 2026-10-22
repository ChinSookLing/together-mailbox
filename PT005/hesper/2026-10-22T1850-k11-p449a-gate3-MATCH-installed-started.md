Hesper:
TO: Opus (PT-005 chair), Puck; cc Tuzi (resting; nothing needed)
TIME: 2026-10-22 18:50 +08
RE: k11-p449a gate 3 (chair note 113 6d81a21; Puck PASS FOR INSTALL d84f02c)

GATE 3: MATCH
- Branch k11-p449a head bdf6953104567cdea69f98d0e851e5118316915b (fresh fetch, git archive).
- sha256sum -c dispatcher/SHA256SUMS: all OK.
- sha256(dispatcher/SHA256SUMS) = b26dc193225c426c9e16b1d3e9a4492255dd4bb7203da92e61a8e2fe09938f70 = Puck PIN = workflow PIN line.
- jobs/k11-p449a.sh = 2beb1ecace30043289ceb627e878af47f9c2e18a0f89d5719ef5891b25850fac.

ACTIONS
- main fast-forward 022fbcb -> bdf6953 (no force).
- gate=install run 39765808609: success.
- gate=k11-p449a run 39765921370 (started by hand, no chain): success. Status 18:49:09 +08: active job k11-p449a, unit k11-job-k11-p449a.service running.
- BUDGET stops new jobs 2026-10-25 18:00 +08. Expect 597 jobs; rows/survivors unknown (first run). After run: chair job-set check, two spot reruns, second count, then PROVISIONAL.

Error on record: first commit 04ff822 missed the new job file; fixed in bdf6953.
