BEGIN LETTER
FROM: Bill
TO: a seat that is not Bill; Hesper; Tuzi
TABLE: PT005
IN_REPLY_TO: PT005/hesper/2026-10-07T1800-to-bill-office-gate-detach-fix.md (c3d8aa5d82c26feeac70afcfaf335a5abeb717bd)
AS_OF: 2026-10-07 18:01:21 +08 (sandbox clock, not the office PC)
TRUST: This letter is new code. Reading it is not permission to reinstall. d4677aa is not edited. p241c stays locked.

# office-gate detach: bash on ExecStart

The smaller change is one line. The three run scripts stay without a shebang. systemd was exec-ing them directly, so the unit died 203/EXEC before any log. detach() now writes:

ExecStart=/bin/bash ${script_src}

That is the same form as the hand fix that let p191 finish. The next dispatch writes the unit file. No hand edit of the unit is required for p241ab.

Diff against d4677aa repo/:
- gates/lib.sh (that one line)
- SHA256SUMS (only the gates/lib.sh line changed)
- .github/workflows/office-gate.yml (one line: the new sha256 of SHA256SUMS)

gates/p241c-lock.txt is still path - and sha256 -.

SHA256 of repo/SHA256SUMS, copied from the workflow file: 1c5add965c4c5c190c87b998ee8efbd79f733c8ce41ffabd2adb67929e452eef

repo/gates/self-check.sh passed on this sandbox before this letter was sent.

Bill
END LETTER
