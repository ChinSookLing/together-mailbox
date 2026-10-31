# Menu p439. Same kit as p383. Prime 439 only. 8 workers.
# gamma 15, census covers 0, so this door is on the (a) menu.
# The command is still kcascade_run.py. One prime at a time.
# Re-dispatch starts again when this unit is not active and p439.done is absent.
# kcascade_run.py skips jobs it already finished.
# Refuses if another kcascade or bgk15 job is running.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

if [[ -f "$HOME/office-gate/state/p439.done" ]]; then
  note "p439 already finished. Use collect."
  exit 0
fi
math_menu_lock
if unit_active office-gate-p439; then
  note "p439 unit is already running."
  exit 0
fi
if pgrep -f '[k]cascade_run.py' >/dev/null 2>&1 || pgrep -f '[b]gk15' >/dev/null 2>&1; then
  note "refusing: another kcascade or bgk15 job is running"
  exit 2
fi
for unit in office-gate-p191 office-gate-p241ab office-gate-p241c office-gate-p409 office-gate-p383 office-gate-p307 office-gate-p337 office-gate-p397 office-gate-p431 office-gate-p443 office-gate-p463 office-gate-p461 office-gate-p433 office-gate-p449 office-gate-p479 office-gate-p467 office-gate-p487; do
  if unit_active "$unit"; then
    note "refusing: ${unit} is active"
    exit 2
  fi
done
install -d "$HOME/office-gate/state"
check_hash "$HOME/kit/kcascade_run.py" scouting/LR16/opus/officepc/kcascade_run.py
printf '%s  %s\n' "$(want_hash scouting/LR16/opus/officepc/kcascade_run.py)" "$HOME/kit/kcascade_run.py" \
  > "$HOME/office-gate/state/p439-pc-kit.sha256"
math_menu_detach office-gate-p439 "$ROOT/gates/p439-run.sh"
