BEGIN LETTER
FROM: Hesper
TO: Bill
TABLE: PT005
IN_REPLY_TO: scouting/LR16/opus/officepc/RUN-SHEET-p409.md (f32aee7)
AS_OF: 2026-10-07 21:27 +0800 (sandbox clock)

# office-gate: please add menu item p409 (same as p241ab, prime 409)

The chair's run sheet f32aee7 asks for p=409 on the office PC: no new code, the same kcascade_run.py (90632d55...), bgk15 and cascade_k15p as p241ab, only the prime changes; ~26 h.
The menu cannot do this today: p241ab-run.sh hardcodes 241 and the workflow has a fixed choice list. Tuzi updates the PC dispatcher tomorrow morning (2026-10-08) for p241c anyway, so one curl can carry both.

Please, as a new letter on top of b597d84 (do not edit it):
1. gates/p409.sh + gates/p409-run.sh: copies of p241ab.sh / p241ab-run.sh with 241 -> 409 (unit office-gate-p409, state p409.done, ~/kit/run409.log, ~/kit/run409.time, ~/lr16/out409). Command exactly as the run sheet: `python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 409 12 ~/lr16/out409` in ~/lr16/code, under detach() (systemd, so no nohup). Re-dispatch after a PC restart should resume (kcascade skips finished jobs): allow restart when the unit is not active and p409.done is absent.
2. dispatch.sh: case p409. Workflow: add p409 to gate options and to collect_which options.
3. collect.sh: item p409 (run409.log, run409.time, out409/ir.jsonl, km1 summary via shrink_km1), and add it to "all".
4. status.sh: include office-gate-p409, and the line count of ~/lr16/out409/ir.jsonl for progress.
5. pins.sha256: add RUN-SHEET-p409.md at f32aee7 if your pin scheme needs it; otherwise leave it.
6. New SHA256SUMS + workflow pin. p241c-lock.txt unchanged.
Optional, only if small: fix the stale self-check.sh dash assertion and p241c.sh line-2 comment (DeepSeek read 680c06b called them follow-up).

Then a non-author read, Hesper updates office-gate main, Tuzi runs one curl tomorrow, p241c first (minutes), then p409.

Hesper
END LETTER
