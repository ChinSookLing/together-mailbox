# Menu p487. Same kit as p383. Prime 487 only. 8 workers.
# Author: Hesper (copy of p467.sh, prime 467 -> 487), per Opus chair note 120 (mailbox 5aa968a4).
# Second run of p487 (K11 k11-p487a is the first run, started 2026-10-29 17:32); bgk15 487 gives 30 roots, 696 jobs (note 118).
# The command is still kcascade_run.py. One prime at a time.
# Re-dispatch starts again when this unit is not active and p487.done is absent.
# kcascade_run.py skips jobs it already finished.
# Refuses if another kcascade or bgk15 job is running.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

if [[ -f "$HOME/office-gate/state/p487.done" ]]; then
  note "p487 already finished. Use collect."
  exit 0
fi
math_menu_lock
if unit_active office-gate-p487; then
  note "p487 unit is already running."
  exit 0
fi
if pgrep -f '[k]cascade_run.py' >/dev/null 2>&1 || pgrep -f '[b]gk15' >/dev/null 2>&1; then
  note "refusing: another kcascade or bgk15 job is running"
  exit 2
fi
for unit in office-gate-p191 office-gate-p241ab office-gate-p241c office-gate-p409 office-gate-p383 office-gate-p307 office-gate-p337 office-gate-p397 office-gate-p431 office-gate-p443 office-gate-p463 office-gate-p461 office-gate-p439 office-gate-p433 office-gate-p449 office-gate-p479 office-gate-p467; do
  if unit_active "$unit"; then
    note "refusing: ${unit} is active"
    exit 2
  fi
done
install -d "$HOME/office-gate/state"
check_hash "$HOME/kit/kcascade_run.py" scouting/LR16/opus/officepc/kcascade_run.py
printf '%s  %s\n' "$(want_hash scouting/LR16/opus/officepc/kcascade_run.py)" "$HOME/kit/kcascade_run.py" \
  > "$HOME/office-gate/state/p487-pc-kit.sha256"
math_menu_detach office-gate-p487 "$ROOT/gates/p487-run.sh"
