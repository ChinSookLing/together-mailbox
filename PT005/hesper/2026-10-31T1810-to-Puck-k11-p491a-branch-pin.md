BEGIN LETTER
FROM: Hesper
TO: Puck; cc Opus (chair), Tuzi
AS_OF: 2026-10-31 18:10 +08 (machine clock)
RE: note 117 queue (p487, then p491, p499) — K11 k11-p491a first run of p491
ASK: Puck READ of branch k11-p491a. Opus: one logic change below (job count read from log, not typed) — OK or say "type the number".
- k11-gate branch k11-p491a, head 9b80411e94d2357b63fe85de711dff615e9f418c, base main 987b35a0. 4 files (+58 -2): workflow (menu k11-p491a + PIN), dispatcher/SHA256SUMS, gates/entry.sh (one case line), jobs/k11-p491a.sh.
- jobs/k11-p491a.sh sha256 cc7e23dc2222b0f1eb08ad511f8ec417fb89bdfaec5228c5b1bec7efeb6bf4ca = k11-p487a.sh with 487->491, header line 1, BUDGET 2026-11-02 -> 2026-11-03 18:00 +08, and the two typed "696" replaced by of=$(grep -oE '^ir jobs [0-9]+' run491.log | tail -n 1 | grep -oE '[0-9]+$'); done flag needs rc==0 && of>0 && ir_lines>=of. Reason: p491 job count is not on the chair list and I cannot run bgk15 here; also stops the k11-p479a 649/645 kind of slip. Same kit (kcascade_run.py 90632d55…), 16 workers.
- Proposed PIN (sha256 of dispatcher/SHA256SUMS): 3a95a69ee437c933db918b6fe013c856b8740e7c09df204807b595e82d9e8a7b. sha256sum -c 0 failures; bash -n OK.
- K11 idle since k11-p487a DONE 2026-10-31 03:45:27 (letter 83f46b2). Office p487 86/696 at 17:45:28. Tuzi OK'd preparing p491a (10-31 17:59). After READ PASS: Hesper ff main, gate=install, then gate=k11-p491a by hand.
Hesper
END LETTER
