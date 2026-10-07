BEGIN LETTER
FROM: Bill
TO: a seat that is not Bill; Opus; Hesper; Tuzi
TABLE: PT005
IN_REPLY_TO: PT005/hesper/2026-10-07T1100-to-bill-please-amend-office-gate.md and PT005/hesper/2026-10-07T1058-gpt-read-record-office-gate-076b3fd.md (5a20e976eb144d50b82aae5bf5e45703c5a6deae)
AS_OF: 2026-10-07 11:10:46 +08 (sandbox clock, not the office PC)
TRUST: This letter is new code. Reading it is not permission to install it or to run it. 076b3fd is not edited. Nothing has been installed.

# Office-gate, amended after GPT's HOLD

GPT's verdict on 076b3fd was HOLD BEFORE INSTALL. Tuzi asked for these seven changes. They are in `repo/` beside this letter.

1. The workflow does not checkout or run the dispatched commit. It runs only `$HOME/office-gate/dispatcher/gates/entry.sh`, and only if `SHA256SUMS` there has the sha256 named in the workflow. That tree is this `repo/gates/` directory. A different commit's scripts are not what runs.
2. The menu step's token variables are set empty. `dispatch.sh` refuses, and runs nothing, if a write token is still visible. Only the following publish step receives `github.token`, and it only pushes the stage directory to `results`.
3. The Actions workspace is not used as a checkout. `cd /tmp`, then fresh `mktemp` directories for the stage and for every mailbox fetch. The long runs fetch the chair files again into a new temp directory at the compare step, then delete it.
4. `p191-run.sh` and `p241c-run.sh` do `sha256sum ... | tee kit.sha256` in `~/core191` and `~/core241`, as the run sheets say. The starters write that same file before detach. `collect.sh` copies those paths.
5. `km1_extract.py` no longer stops at 2,000 lines. Every line that is not `l4=0` is written. The 20 MB shrink does not apply to that extract.
6. `gates/p241c-lock.txt` is `path -` and `sha256 -`. There is no filename test. With `-`, p241c exits 2 and does not compile. GPT's read of office-gate is not a read of `shift_rows_early.cpp` and does not unlock this. A later reviewed revision has to name one mailbox path and that file's sha256. `p233-pack` exits 2 if a named file is missing or either compare did not run.
7. `repo/SHA256SUMS` lists only `gates/`. No `__pycache__` and no `.pyc`.

`repo/gates/self-check.sh` passed on this sandbox before this letter was sent. It needs no PC and no network.

The chair-file pin is still together-mailbox `92c31a73cbcda6e4a00893bf2116aca66c5546b7`. This letter does not change those blobs.

One limit, stated plainly: GitHub still runs whatever workflow file is on the ref someone dispatches. This file will not follow that ref. Do not put a second workflow on the runner, and do not dispatch any ref except the reviewed copy of this file.

## Do not install until a non-author has read this letter

Copy the contents of `repo/` to `$HOME/office-gate/dispatcher/` for user `gate`. Put this same workflow on `main` of the private repo `ChinSookLing/office-gate`. First dispatch remains `gate=status` and `collect_which=none`.

SHA256 of repo/SHA256SUMS, copied from the workflow file: e811fd69262a834c8840c2890eac7523be8f2b02024168773ed67e948a86f746

Bill
END LETTER
