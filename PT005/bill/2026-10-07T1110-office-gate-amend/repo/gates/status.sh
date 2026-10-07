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
for unit in office-gate-p191 office-gate-p241ab office-gate-p241c; do
  if [[ -S "${XDG_RUNTIME_DIR:-/nonexistent}/bus" ]]; then
    systemctl --user is-active "${unit}.service" > "$STAGE/${unit}.active" 2>/dev/null || true
  fi
  for mark in done stopped; do
    if [[ -f "$HOME/office-gate/state/${unit#office-gate-}.${mark}" ]]; then
      echo yes > "$STAGE/${unit}.${mark}"
    fi
  done
done
printf '%s\n' "$MAILBOX_PIN" > "$STAGE/mailbox_pin.txt"
