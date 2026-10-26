# Menu p241ab. No new code. Detaches parts (a) and (b) only.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

if [[ -f "$HOME/office-gate/state/p241ab.done" ]]; then
  note "p241ab already finished. Use collect."
  exit 0
fi
math_menu_lock
if unit_active office-gate-p241ab; then
  note "p241ab unit is already running."
  exit 0
fi
for unit in office-gate-p191 office-gate-p241c office-gate-p409 office-gate-p383 office-gate-p307 office-gate-p337 office-gate-p397 office-gate-p431 office-gate-p443 office-gate-p463 office-gate-p461 office-gate-p439 office-gate-p433 office-gate-p449 office-gate-p479; do
  if unit_active "$unit"; then
    note "refusing: ${unit} is active"
    exit 2
  fi
done
install -d "$HOME/office-gate/state"
check_hash "$HOME/kit/kcascade_run.py" scouting/LR16/opus/officepc/kcascade_run.py
printf '%s  %s\n' "$(want_hash scouting/LR16/opus/officepc/kcascade_run.py)" "$HOME/kit/kcascade_run.py" \
  > "$HOME/office-gate/state/p241ab-pc-kit.sha256"
math_menu_detach office-gate-p241ab "$ROOT/gates/p241ab-run.sh"
