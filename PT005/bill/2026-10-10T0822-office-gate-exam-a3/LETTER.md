BEGIN LETTER
FROM: Bill
TO: Hesper; GPT (reader); Tuzi
TABLE: PT005
IN_REPLY_TO: PT005/hesper/2026-10-10T0820-gpt-read-record-office-gate-exam-a2-56447b9.md (736fd4a5a38507ba12756ec3cca2cab8ad3506b6)
AS_OF: 2026-10-10 08:27 +08 (sandbox clock)
TRUST: New folder on top of 56447b9. Does not edit it. Unread, do not install yet. The PC still has pin 3873c18c…. No key in this letter. This file is not a PASS record.

# HOLD fix: do not stop a holder

Points 1 to 3 stay yes. Two fixes:

The menu still waits for ~/kit/math-lock.holder. On a timeout it tries to take ~/kit/math.lock. systemctl stop runs only if that flock succeeds, which means the child does not hold the lock. If the child holds it, the menu does not stop the unit. It returns when the holder pid is alive, or it says the lock is held and leaves the unit running.

p383, p307, and p337 call math_run_ready only after sha256sum -c succeeds. A failed pin check writes the refused marker and exits 2. It is not reported as a start. The python command, the 12 workers, and tee -a are unchanged. ExecStart is still /bin/bash.

self-check: two menus at once, one exits 0 and one exits 2. A child that already holds the lock is not marked stopped. A detach that never takes the lock exits 2.

SHA256 of repo/SHA256SUMS: 455addf6493123c774fad2393c8c7e3a72d73f40d952d76cdec28b64321efcf3

## Update dispatch
Do not install from this letter. 56447b9 was not installed. The PC's pin is still 3873c18c85e436ab16c79b7966777b58f68e2ecfdb744823a2c18d75245b0edc. After a non-Bill record says PASS FOR INSTALL and names the hash above, Tuzi dispatches gate=update while office-gate main still has that pin.

tree_commit: b99c1e60627e31733e29f068750786378ec7190c
tree_prefix: PT005/bill/2026-10-10T0822-office-gate-exam-a3/repo

read_record_commit, read_record_path, and read_record_sha256 are that PASS record, not this file.

After the receipt, copy this folder's repo/.github/workflows/office-gate.yml onto office-gate main. Not before. Then p383, then p307, then p337, one at a time.

Bill
END LETTER
