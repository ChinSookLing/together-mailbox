# Menu p241ab. No new code. Detaches parts (a) and (b) only.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

if [[ -f "$HOME/office-gate/state/p241ab.done" ]]; then
  note "p241ab already finished. Use collect."
  exit 0
fi
if unit_active office-gate-p241ab; then
  note "p241ab unit is already running."
  exit 0
fi
install -d "$HOME/office-gate/state"
check_hash "$HOME/kit/kcascade_run.py" scouting/LR16/opus/officepc/kcascade_run.py
printf '%s  %s\n' "$(want_hash scouting/LR16/opus/officepc/kcascade_run.py)" "$HOME/kit/kcascade_run.py" \
  > "$HOME/office-gate/state/p241ab-pc-kit.sha256"
detach office-gate-p241ab "$ROOT/gates/p241ab-run.sh"
