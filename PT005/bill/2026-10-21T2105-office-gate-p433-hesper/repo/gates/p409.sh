# Menu p409. Same kit as p241ab. Prime 409 only.
# Re-dispatch starts again when this unit is not active and p409.done is absent.
# kcascade_run.py skips jobs it already finished.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

if [[ -f "$HOME/office-gate/state/p409.done" ]]; then
  note "p409 already finished. Use collect."
  exit 0
fi
math_menu_lock
if unit_active office-gate-p409; then
  note "p409 unit is already running."
  exit 0
fi
for unit in office-gate-p191 office-gate-p241ab office-gate-p241c office-gate-p383 office-gate-p307 office-gate-p337 office-gate-p397 office-gate-p431 office-gate-p443 office-gate-p463 office-gate-p461 office-gate-p439 office-gate-p433; do
  if unit_active "$unit"; then
    note "refusing: ${unit} is active"
    exit 2
  fi
done
install -d "$HOME/office-gate/state"
check_hash "$HOME/kit/kcascade_run.py" scouting/LR16/opus/officepc/kcascade_run.py
printf '%s  %s\n' "$(want_hash scouting/LR16/opus/officepc/kcascade_run.py)" "$HOME/kit/kcascade_run.py" \
  > "$HOME/office-gate/state/p409-pc-kit.sha256"
math_menu_detach office-gate-p409 "$ROOT/gates/p409-run.sh"
