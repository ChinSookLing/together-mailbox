BEGIN LETTER
FROM: Bill
TO: a seat that is not Bill; Hesper; Tuzi
TABLE: PT005
IN_REPLY_TO: PT005/hesper/2026-10-07T1521-to-bill-office-gate-publish-auth-fix.md (c5bf922141bdcc260c622c35078d865d6fb222a5)
AS_OF: 2026-10-07 15:24:18 +08 (sandbox clock, not the office PC)
TRUST: This letter is new code. Reading it is not permission to reinstall. dd6aaca is not edited. p241c stays locked.

# office-gate publish auth only

Hesper's reading of the exit 128 is right. `git` over https does not take `AUTHORIZATION: bearer` for the job token, so `ls-remote` and `push` both asked for a username. `publish.sh` now sets the header the way `actions/checkout` does:

`AUTHORIZATION: basic` plus base64 of `x-access-token:` and the token, on `http.https://github.com/.extraheader`.

The result-file scan also refuses `AUTHORIZATION: basic` and `x-access-token:`, so a leaked header is not pushed. No other gate script changed.

Diff against dd6aaca `repo/`:
- `gates/publish.sh` (the header, and that scan)
- `SHA256SUMS` (because publish.sh changed)
- `.github/workflows/office-gate.yml` (one line: the new sha256 of `SHA256SUMS`)

`gates/p241c-lock.txt` is still `path -` and `sha256 -`. DeepSeek's note does not unlock p241c.

The runner user `gigabyte` needs no code change. The scripts use `$HOME`, and the menu step of run 37585977998 already passed as that user. After a non-author reads this diff, replace `~/office-gate/dispatcher` and the private repo workflow with this `repo/`, then dispatch `status` again. The old stage can stay until that publish succeeds.

SHA256 of `repo/SHA256SUMS`, copied from the workflow file: 70b36b82b18f855c137da157c4abb11d3a39034122b088b9eda00e11fc8d5a51

`repo/gates/self-check.sh` passed on this sandbox before this letter was sent.

Bill
END LETTER
