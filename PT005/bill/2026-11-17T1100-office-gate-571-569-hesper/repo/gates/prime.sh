# Prime door (Opus chair note 122 A, D). One door for every prime on gates/primes.txt.
# Author: Hesper. Replaces the per-prime copies (p467.sh, p479.sh, p487.sh ...) for new primes.
# The prime comes from the PRIME input and must be one whole line of primes.txt.
# Refuses: a prime not on the list, a prime already done, a prime with a mismatch mark,
# a prime whose earlier list primes are not done (list order), another math job.
# Same kit and command as p487: kcascade_run.py, 8 workers. Low CPU priority (unit_text in lib.sh).
# Re-dispatch resumes when the unit is not active and pNNN.done is absent.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

P="${PRIME:-}"
if ! prime_on_list "$P"; then
  note "refusing: prime is not on gates/primes.txt"
  exit 2
fi
S="$HOME/office-gate/state"
if [[ -f "$S/p${P}.done" ]]; then
  note "refusing: p${P} is already done. Use collect."
  exit 2
fi
if [[ -f "$S/p${P}.mismatch" ]]; then
  note "refusing: p${P} closed with a job-count mismatch. Ask the chair."
  exit 2
fi
prime_order_ok "$P" || exit 2
math_menu_lock
if unit_active "office-gate-p${P}"; then
  note "p${P} unit is already running."
  exit 0
fi
if pgrep -f '[k]cascade_run.py' >/dev/null 2>&1 || pgrep -f '[b]gk15' >/dev/null 2>&1; then
  note "refusing: another kcascade or bgk15 job is running"
  exit 2
fi
for unit in $(office_units); do
  if unit_active "$unit"; then
    note "refusing: ${unit} is active"
    exit 2
  fi
done
install -d "$S"
check_hash "$HOME/kit/kcascade_run.py" scouting/LR16/opus/officepc/kcascade_run.py
printf '%s  %s\n' "$(want_hash scouting/LR16/opus/officepc/kcascade_run.py)" "$HOME/kit/kcascade_run.py" \
  > "$S/p${P}-pc-kit.sha256"
export OFFICE_GATE_PRIME="$P"
math_menu_detach "office-gate-p${P}" "$ROOT/gates/prime-run.sh"
