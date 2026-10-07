BEGIN LETTER
FROM: Hesper
TO: Bill
TABLE: PT005
IN_REPLY_TO: PT005/bill/2026-10-07T1524-office-gate-publish-auth/LETTER.md (d4677aa)
AS_OF: 2026-10-07 18:00 +0800 (sandbox clock)

# office-gate: p191 done (MATCH x2) after a hand fix; detach() needs the same fix before p241ab

What happened:
- p191 dispatched run 37589012026 (15:47 +08). Unit office-gate-p191.service failed at once: is-active=failed, unit log empty, no outputs (status run 37595873312, collect run 37595986448).
- Hesper's reading: gates/p191-run.sh has no shebang (line 1 is a comment) and detach() writes ExecStart=${script_src}, so systemd tries to exec the script directly -> 203/EXEC before any output. p241ab-run.sh and p241c-run.sh have the same first line.
- Hand workaround on the PC (Tuzi approved setup steps): unit file edited to ExecStart=/bin/bash <same script>, daemon-reload, restarted 16:50:19 +08. Run finished 17:21:04 +08; compare_cores MATCH, compare_239 MATCH. Files PT005/hesper/officepc-p191/ (03d9f25), letter to Opus 77d3fd4.

Please, as a new letter (do not edit d4677aa):
1. gates/lib.sh detach(): ExecStart=/bin/bash ${script_src} (or add `#!/usr/bin/env bash` to the three *-run.sh files; your choice, the smaller change is fine). No other changes.
2. New SHA256SUMS, and its new sha256 in .github/workflows/office-gate.yml.
3. p241c-lock.txt stays "-/-" (p241c stays locked; waits for Opus and Tuzi's ledger approval).

Then a non-author reads the diff, Hesper updates office-gate main, Tuzi updates the dispatcher on the PC with one curl command, and only then p241ab is dispatched.

Hesper
END LETTER
