# Menu p467. Same kit as p383. Prime 467 only. 8 workers.
# Author: Hesper (copy of p479.sh, prime 479 -> 467), per Opus chair note 117 §"cross runs" (mailbox 3f25e558) and spec note 115 §2.
# Second run of p467 (K11 k11-p467a was first, 649/649 done 2026-10-27). census14 found 0 fourteen-class covers for 467 (note 115), so part (a) only; bgk15 467 gives 29 roots, 649 jobs.
# The command is still kcascade_run.py. One prime at a time.
# Re-dispatch starts again when this unit is not active and p467.done is absent.
# kcascade_run.py skips jobs it already finished.
# Refuses if another kcascade or bgk15 job is running.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

if [[ -f "$HOME/office-gate/state/p467.done" ]]; then
  note "p467 already finished. Use collect."
  exit 0
fi
math_menu_lock
if unit_active office-gate-p467; then
  note "p467 unit is already running."
  exit 0
fi
if pgrep -f '[k]cascade_run.py' >/dev/null 2>&1 || pgrep -f '[b]gk15' >/dev/null 2>&1; then
  note "refusing: another kcascade or bgk15 job is running"
  exit 2
fi
for unit in office-gate-p191 office-gate-p241ab office-gate-p241c office-gate-p409 office-gate-p383 office-gate-p307 office-gate-p337 office-gate-p397 office-gate-p431 office-gate-p443 office-gate-p463 office-gate-p461 office-gate-p439 office-gate-p433 office-gate-p449 office-gate-p479 office-gate-p487; do
  if unit_active "$unit"; then
    note "refusing: ${unit} is active"
    exit 2
  fi
done
install -d "$HOME/office-gate/state"
check_hash "$HOME/kit/kcascade_run.py" scouting/LR16/opus/officepc/kcascade_run.py
printf '%s  %s\n' "$(want_hash scouting/LR16/opus/officepc/kcascade_run.py)" "$HOME/kit/kcascade_run.py" \
  > "$HOME/office-gate/state/p467-pc-kit.sha256"
math_menu_detach office-gate-p467 "$ROOT/gates/p467-run.sh"
