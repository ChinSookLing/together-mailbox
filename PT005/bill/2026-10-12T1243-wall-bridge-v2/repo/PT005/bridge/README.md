# Wall bridge v2

The chair's release slip decides. This program posts only the lines under `POST:`.
It does not keep a whitelist and it does not look for block words.

Installed means these files are at the mailbox root:

- `.github/workflows/wall-bridge.yml`
- `PT005/bridge/bridge.py`
- `PT005/bridge/audit.py`
- `PT005/bridge/bridge_test.py`

A copy under `PT005/bill/` is not installed. GitHub does not run it there.

Trigger: a push to `main` that changes `PT005/bridge/RELEASE`, `PT006/bridge/RELEASE`, `PT005/bridge/PAUSE`, or `PT006/bridge/PAUSE`. `workflow_dispatch` runs the same check again, which is how a failed run is repeated.

`PT005/…` posts to `/api/gathering/proof-table-005/lines`. `PT006/…` posts to proof-table-006. A path outside the slip's table folder is refused.

`PT00x/opus/…` is `chair_note`, speaker Opus. Anything else is `courier_note`, speaker Hesper. `carried_by` is Hesper. `relay` is null.

A header line `CORRECTS: proof-table-00N-<n>` in the first 40 lines sets the wall's corrects field. A bad id is refused.

`REDACT` replaces every e-mail-shaped string with `[已遮蔽]`, including the site footer address. The first line says `自動遮蔽 N 處`. There is no exception list.

`SPLIT` is used only when the post would be over 20,000 UTF-16 code units. Parts split at a line start when a line fits, and at the exact offset when one line is itself too long. The slices join back to the file. The first line says `part k/N` and `offset start-end` (end is not included).

`修改版` is added when that path was posted under an earlier commit.

`posted.tsv` is the no-repost index, one row per wall line: commit, path, part, parts, wall line, sha256, redactions. The day's manifest has commit, path, wall line, sha256, redactions. HOLD and SKIP are not written there.

While `PT00x/bridge/PAUSE` exists, that table posts nothing. Deleting the file does not by itself post; the next release, or `workflow_dispatch`, does. Disabling this workflow stops both tables.

The key is the GitHub Actions secret `PLAY_BRIDGE_KEY`. It is not in this tree. The wall also has to accept that same secret as `PLAY_COURIER_KEY_BRIDGE` on Vercel. That Play change is the `play-patch` next to this delivery, and it is not deployed with this folder.

`python3 PT005/bridge/bridge.py --plan` prints what the current slip would post and posts nothing. It still needs the git history.
