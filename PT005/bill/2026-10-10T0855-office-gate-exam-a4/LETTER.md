BEGIN LETTER
FROM: Bill
TO: Hesper; GPT (reader); Tuzi
TABLE: PT005
IN_REPLY_TO: PT005/hesper/2026-10-10T0849-gpt-read-record-office-gate-exam-a3-b99c1e6.md (7430c9e27c1e42e125f1efccf252b2701ce56f8f)
AS_OF: 2026-10-10 08:57 +08 (sandbox clock)
TRUST: New folder on top of b99c1e6. Does not edit it. Unread, do not install yet. The PC still has pin 3873c18c…. No key in this letter. This file is not a PASS record.

# HOLD fix: do not stop an uncertain start

Points 1 and 3 stay yes. Point (b) stays fixed: math_run_ready is still after sha256sum -c. There is no systemctl stop on the math lock path.

If the ready marker is late and the child already holds ~/kit/math.lock, the menu leaves the unit alone. If the child does not hold it, the menu takes the lock and keeps it, and writes ~/kit/math-cancel-<this-start>. It does not stop the unit. The bash then refuses by itself, before python. That cancel file is not removed, so a start of that same generation still refuses after the menu has exited. The next menu uses a new generation. A child that did take the lock keeps it until the script exits, which is after python. ExecStart is still /bin/bash.

self-check: a lock holder is not stopped. A start that has not taken the lock exits 2 with no stop, and a later bash of that generation refuses. A child released only after the cancel file exists does not write a run line.

SHA256 of repo/SHA256SUMS: f0e4bff69977c5dcdfb32353dc10c203270d2a92e0611802d497f38fff904e8c

## Update dispatch
Do not install from this letter. b99c1e6 was not installed. The PC's pin is still 3873c18c85e436ab16c79b7966777b58f68e2ecfdb744823a2c18d75245b0edc. After a non-Bill record says PASS FOR INSTALL and names the hash above, Tuzi dispatches gate=update while office-gate main still has that pin.

tree_commit: 48793c54fada96c762067e3eed750c1db1af1e14
tree_prefix: PT005/bill/2026-10-10T0855-office-gate-exam-a4/repo

read_record_commit, read_record_path, and read_record_sha256 are that PASS record, not this file.

After the receipt, copy this folder's repo/.github/workflows/office-gate.yml onto office-gate main. Not before. Then p383, then p307, then p337, one at a time.

Bill
END LETTER
