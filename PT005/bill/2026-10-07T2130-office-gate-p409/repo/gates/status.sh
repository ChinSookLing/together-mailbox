# Menu status. No gate run. No environment dump.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"
{
  printf 'user %s\n' "$(id -un)"
  printf 'host %s\n' "$(hostname)"
  uname -a
} > "$STAGE/host.txt"
df -h "$HOME" > "$STAGE/disk.txt" || true
if user_bus; then
  echo yes > "$STAGE/user_bus.txt"
else
  echo no > "$STAGE/user_bus.txt"
fi
for unit in office-gate-p191 office-gate-p241ab office-gate-p241c office-gate-p409; do
  if [[ -S "${XDG_RUNTIME_DIR:-/nonexistent}/bus" ]]; then
    systemctl --user is-active "${unit}.service" > "$STAGE/${unit}.active" 2>/dev/null || true
  fi
  for mark in done stopped; do
    if [[ -f "$HOME/office-gate/state/${unit#office-gate-}.${mark}" ]]; then
      echo yes > "$STAGE/${unit}.${mark}"
    fi
  done
done
if [[ -f "$HOME/lr16/out409/ir.jsonl" ]]; then
  wc -l < "$HOME/lr16/out409/ir.jsonl" > "$STAGE/out409-ir.count"
else
  echo 0 > "$STAGE/out409-ir.count"
fi
printf '%s\n' "$MAILBOX_PIN" > "$STAGE/mailbox_pin.txt"
