# Menu p337. Same kit as p409. Prime 337 only.
# Re-dispatch starts again when this unit is not active and p337.done is absent.
# kcascade_run.py skips jobs it already finished.
# Refuses if another kcascade or bgk15 job is running.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

if [[ -f "$HOME/office-gate/state/p337.done" ]]; then
  note "p337 already finished. Use collect."
  exit 0
fi
math_menu_lock
if unit_active office-gate-p337; then
  note "p337 unit is already running."
  exit 0
fi
if pgrep -f '[k]cascade_run.py' >/dev/null 2>&1 || pgrep -f '[b]gk15' >/dev/null 2>&1; then
  note "refusing: another kcascade or bgk15 job is running"
  exit 2
fi
for unit in office-gate-p191 office-gate-p241ab office-gate-p241c office-gate-p409 office-gate-p383 office-gate-p307; do
  if unit_active "$unit"; then
    note "refusing: ${unit} is active"
    exit 2
  fi
done
install -d "$HOME/office-gate/state"
check_hash "$HOME/kit/kcascade_run.py" scouting/LR16/opus/officepc/kcascade_run.py
printf '%s  %s\n' "$(want_hash scouting/LR16/opus/officepc/kcascade_run.py)" "$HOME/kit/kcascade_run.py" \
  > "$HOME/office-gate/state/p337-pc-kit.sha256"
math_menu_detach office-gate-p337 "$ROOT/gates/p337-run.sh"
