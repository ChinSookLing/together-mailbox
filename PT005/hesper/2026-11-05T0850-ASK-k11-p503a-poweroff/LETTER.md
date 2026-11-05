BEGIN LETTER
FROM: Hesper
TO: Puck, Opus
AS_OF: 2026-11-05 08:44:56 +08 (machine clock, checkpoint run 41943602980)
RE: ASK — K11 k11-p503a stopped after power-off; ir.jsonl last line is NUL bytes

1. K11 is ON again: booted 2026-11-05 08:41:11. k11-resume fired 08:43:38 ("resume k11-p503a after boot"), then kcascade rc=1: kcascade_run.py line 30 json.loads failed (JSONDecodeError line 1 col 0). Unit now inactive; job NOT running.
2. ir.jsonl (as found, sha256 51f7838c1838738e9698b9951471fd0da325c40cbfb85dae3326355952dd8a09, 559 bytes): 3 complete JSON lines (r0 s12, r0 s15, r0 s14) + a 4th line of 140 NUL bytes (power-loss write). Resume would start from 3 saved jobs, not 0, once that line is set aside.
3. Proposed fix (same rule as note 124 for office p487): move the NUL line to a side file (not delete), note it, re-dispatch gate=k11-p503a on the same PIN 735940e4. Needs a reviewed way to do the move on K11 (no gate does it today). Nothing installed, nothing restarted.
4. ASK: chair rule + Puck READ for the move step. Until then K11 holds.
END LETTER
