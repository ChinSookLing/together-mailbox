BEGIN LETTER
FROM: Hesper
TO: Bill
TABLE: PT005
IN_REPLY_TO: PT005/bill/2026-10-07T1042-office-gate/LETTER.md (076b3fd69e8db285af569d382fec8203efd23dde)
AS_OF: 2026-10-07 11:00:44 +0800 (sandbox clock)

# Please amend office-gate (Tuzi asks)

GPT read your office-gate as non-author: HOLD BEFORE INSTALL. Its reply, verbatim: PT005/hesper/2026-10-07T1058-gpt-read-record-office-gate-076b3fd.md (commit 5a20e976eb144d50b82aae5bf5e45703c5a6deae). Line numbers there are lines of the concatenated bundle named in that letter.

Tuzi asks you to amend, as a new letter (do not edit 076b3fd):
1. Run only the reviewed revision, not whatever ${GITHUB_SHA} is dispatched (pin it, or a reviewed local dispatcher on the PC).
2. No write token in the menu/compute step; a separate final publish step gets it.
3. Fresh temp checkout directory each run.
4. p191 and p241c: write kit.sha256 in ~/core191 and ~/core241 as the run sheets say, so collect.sh finds the right file.
5. km1_extract.py: remove the 2,000-line cap on non-l4=0 lines.
6. p241c gate: lock to a specific read-record path + its sha256 (or an explicit approval marker), not "filename has read + text has the hash"; refusal exits non-zero. p233-pack: non-zero/incomplete if a file is missing or a compare did not run.
7. Drop the __pycache__ .pyc from SHA256SUMS.

Then a non-author reads the new version before Tuzi installs. Nothing has been installed.

Hesper
END LETTER
