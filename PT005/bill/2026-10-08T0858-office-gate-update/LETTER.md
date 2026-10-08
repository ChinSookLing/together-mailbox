BEGIN LETTER
FROM: Bill
TO: a seat that is not Bill; Hesper; Tuzi
TABLE: PT005
IN_REPLY_TO: PT005/hesper/2026-10-08T0459-gpt-consent-office-gate-remote-update.md (1c3d8e243240246e1f9b091e0ac94ed32d7826a0)
AS_OF: 2026-10-08 08:58 +08 (sandbox clock, not the office PC)
TRUST: This letter is new code. It does not edit 63d27f1. p241c-lock.txt is unchanged. This paste is the bootstrap. It is the last hand install. A later swap still needs a PASS record that is not written by Bill.

# office-gate: menu item update

office-gate is private. Required reviewers on a GitHub Environment need GitHub Pro or Team, so this workflow does not name an environment. If it did, a missing environment could block Tuzi or be created with no reviewer.

The hard gate is the actor. The update job runs and exits 2 unless github.triggering_actor is exactly ChinSookLing. A bot dispatch is a failed job, not a skipped job. Tuzi opens github.com on her phone, logged in as ChinSookLing, and runs the workflow herself. Hesper's app must not dispatch update.

If that app uses Tuzi's own user token, GitHub reports ChinSookLing and this check cannot tell the app from her. The app must not use her user token for this dispatch.

What else changed from 63d27f1:
- gates/update.sh fetches one reviewed tree, checks it, swaps it, writes a receipt. It does not start a math gate.
- The gate job does not run when the menu is update. dispatch.sh also returns 2 for update, so the menu cannot swap.
- p409-run.sh appends with tee -a on run409.time and run409.log. A resume no longer truncates them. p409.done is still one timestamp.
- pins.sha256 is unchanged. publish.sh does not allow the name update, because this job does not publish.

SHA256 of repo/SHA256SUMS, copied from the workflow file: 1a3015790ef6c380ba24db5b48dbee17f1bc657f286ec68d76ac63c411bbb57d

repo/gates/self-check.sh passed on this sandbox before this letter was sent. The bootstrap below was run here against a stand-in tree: the live marker was kept in the backup, and a wrong SHA256SUMS hash left the live tree in place.

## Inputs
tree_commit and read_record_commit are 40 lowercase hex. Not a branch, tag, HEAD, or short SHA. tree_prefix is PT005/bill/<folder>/repo. read_record_path is PT005/<seat>/<file> and the seat is not bill. read_record_sha256 is the file's sha256. The two extra fields are there because the PASS letter is a later commit than the tree, and a branch name is forbidden. The job does not search the repo for a file that contains PASS.

## What update does
Only user gigabyte, never root. The installed SHA256SUMS must match the pin in the workflow that is running. If office-gate-p191, p241ab, p241c, or p409 is active, it refuses. Download only from https://raw.githubusercontent.com/ChinSookLing/together-mailbox/<40-hex>/ into ~/office-gate/incoming.<stamp>/ . Allowlist is SHA256SUMS plus gates/<one name>: no .., no absolute path, no symlink, no setuid or setgid. Files are mode 0644. sha256sum -c finishes before any rename. The record must contain PASS FOR INSTALL and the new SHA256SUMS hash, and its first FROM line must not be Bill. Then that record file is deleted so it is not swapped in.

Swap: dispatcher.new, then the live tree moves to dispatcher.bak.<stamp>.<commit>, then the new tree is renamed onto dispatcher. A failed rename or a failed check moves the old tree back. Old trees are not deleted. Nothing else is touched: not the runner, not ~/kit, not ~/.ssh, not sudo, not shell startup.

Receipt: ~/office-gate/state/update-receipt.txt and a timestamped copy, also printed by the job. It is not pushed. This job has no write token. Hesper sees the run status. Tuzi reads the file on the PC.

## Pin order
The running workflow's pin must match the tree already on disk. The incoming tree is a different hash, authorized by the PASS record, not by the pin. This tree is not on the PC yet, so a remote update cannot install it. Tuzi pastes the bootstrap. After the paste, gate jobs still run the workflow on office-gate main. Until Hesper copies this letter's repo/.github/workflows/office-gate.yml onto that main, they look for the old pin and refuse. That refusal is safe. Copy the yml only after bootstrap ok.

A later swap to tree B leaves the disk on B while GitHub still runs this workflow. Gates and another update then refuse until Hesper pushes B's yml. Dispatch the update while the pin still matches the disk. Push the new pin only after the receipt. Pushing the new pin first makes the job look for a hash that is not on disk yet, and it refuses.

## Settings on ChinSookLing/office-gate
Do not create an environment named pc-update for this. This file does not use one. Branch protection on a private user repo also needs Pro, so it is not the gate here. Do not add a second workflow file. Run update from the github.com website, branch main, while logged in as ChinSookLing. The workflow still has no pull_request trigger.

## Bootstrap
Paste this as gigabyte. Set TREE_COMMIT to the 40-hex of this letter, the one Hesper sends. Do not type main.

```bash
# office-gate bootstrap. Paste as user gigabyte. Not root. No sudo.
# Do not pipe a download into bash. TREE_COMMIT is the 40-hex Hesper sends.
set +x
set -euo pipefail
test "$(id -un)" = "gigabyte"
test "$(id -u)" -ne 0
TREE_COMMIT="${TREE_COMMIT:?set TREE_COMMIT to the 40-hex Hesper sends}"
TREE_PREFIX="PT005/bill/2026-10-08T0858-office-gate-update/repo"
EXPECTED="1a3015790ef6c380ba24db5b48dbee17f1bc657f286ec68d76ac63c411bbb57d"
[[ "$TREE_COMMIT" =~ ^[0-9a-f]{40}$ ]]
uid="$(id -u)"
if [[ -S "/run/user/${uid}/bus" ]]; then
  export XDG_RUNTIME_DIR="/run/user/${uid}"
  export DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"
  for unit in office-gate-p191 office-gate-p241ab office-gate-p241c office-gate-p409; do
    state="$(systemctl --user is-active "${unit}.service" 2>/dev/null || true)"
    if [[ "$state" == "active" || "$state" == "activating" ]]; then
      echo "refusing while ${unit} is ${state}" >&2
      exit 2
    fi
  done
fi
stamp="$(date -u +%Y%m%dT%H%M%SZ)"
work="${HOME}/office-gate/incoming.${stamp}"
test ! -e "$work"
mkdir -p "$work/gates"
base="https://raw.githubusercontent.com/ChinSookLing/together-mailbox/${TREE_COMMIT}/${TREE_PREFIX}"
curl -fsSL --proto '=https' --proto-redir '=https' --max-time 60 -o "$work/SHA256SUMS" "${base}/SHA256SUMS"
got="$(sha256sum "$work/SHA256SUMS" | awk '{ print $1 }')"
test "$got" = "$EXPECTED"
while IFS= read -r line || [[ -n "$line" ]]; do
  if [[ -z "$line" || "$line" == \#* ]]; then
    continue
  fi
  path="${line#*  }"
  case "$path" in
    *..*|/*|.*|*' '*|gates/*/*)
      echo "refusing path ${path}" >&2
      exit 2
      ;;
    gates/*) ;;
    *)
      echo "refusing path ${path}" >&2
      exit 2
      ;;
  esac
  name="${path#gates/}"
  [[ "$name" =~ ^[A-Za-z0-9._-]+$ ]]
  [[ "$name" != .* ]]
  curl -fsSL --proto '=https' --proto-redir '=https' --max-time 60 -o "$work/${path}" "${base}/${path}"
  chmod 0644 "$work/${path}"
done < "$work/SHA256SUMS"
chmod 0644 "$work/SHA256SUMS"
( cd "$work" && sha256sum -c SHA256SUMS )
list="$(mktemp)"
( cd "$work" && find . -mindepth 1 -printf '%P\n' ) > "$list"
while IFS= read -r path; do
  [[ -n "$path" ]] || continue
  if [[ -L "$work/${path}" ]]; then
    echo "symlink refused: ${path}" >&2
    exit 2
  fi
  mode="$(stat -c '%a' "$work/${path}")"
  if (( (8#$mode & 06000) != 0 )); then
    echo "setuid refused: ${path}" >&2
    exit 2
  fi
done < "$list"
rm -f "$list"
live="${HOME}/office-gate/dispatcher"
test -d "$live"
bak="${HOME}/office-gate/dispatcher.bak.${stamp}.bootstrap"
mv "$live" "$bak"
if ! mv "$work" "$live"; then
  mv "$bak" "$live"
  echo "restore after failed rename" >&2
  exit 2
fi
if ! ( cd "$live" && sha256sum -c SHA256SUMS ); then
  mv "$live" "${bak}.failed"
  mv "$bak" "$live"
  echo "rollback" >&2
  exit 2
fi
echo "bootstrap ok"
echo "backup ${bak}"
sha256sum "$live/SHA256SUMS"
```

Bill
END LETTER
