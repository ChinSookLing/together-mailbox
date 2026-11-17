# Long run for the prime door (chair note 122 A). Same command as p487, prime from the unit, 8 workers.
# Author: Hesper. systemd starts this with /bin/bash. No nohup.
# Header: prime, start, BUDGET = first start + BUDGET_DAYS (lib.sh), written once and kept on restart.
# Before BUDGET, kcascade gets the seconds left; a start after BUDGET runs with no BUDGET (as K11 jobs do).
# Done flag only on prime_verdict DONE (note 121: log count used for the flag only, never as ledger proof).
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"
P="${OFFICE_GATE_PRIME:-}"
if ! prime_on_list "$P"; then
  printf '%s\n' "refused" > "${HOME}/kit/math-lock.refused"
  echo "refusing: prime is not on gates/primes.txt" >&2
  exit 2
fi
math_run_lock
if pgrep -f '[k]cascade_run.py' >/dev/null 2>&1 || pgrep -f '[b]gk15' >/dev/null 2>&1; then
  printf '%s\n' "refused" > "${HOME}/kit/math-lock.refused"
  echo "refusing: another kcascade or bgk15 job is running" >&2
  exit 2
fi
STATE="${HOME}/office-gate/state"
if ! sha256sum -c "$STATE/p${P}-pc-kit.sha256"; then
  printf '%s\n' "refused" > "${HOME}/kit/math-lock.refused"
  exit 2
fi
math_run_ready
HDR="$STATE/p${P}.header"
LOG="${HOME}/kit/run${P}.log"
TIME="${HOME}/kit/run${P}.time"
OUTD="${HOME}/lr16/out${P}"
if [[ ! -f "$HDR" ]]; then
  start="$(date +%s)"
  deadline=$(( start + BUDGET_DAYS * 86400 ))
  {
    printf 'prime %s\n' "$P"
    printf 'workers 8\n'
    printf 'start %s\n' "$(date -d "@${start}" '+%F %T %Z')"
    printf 'start_epoch %s\n' "$start"
    printf 'budget %s\n' "$(date -d "@${deadline}" '+%F %T %Z')"
    printf 'budget_epoch %s\n' "$deadline"
  } > "$HDR.tmp"
  mv "$HDR.tmp" "$HDR"
fi
deadline="$(awk '$1 == "budget_epoch" { print $2; exit }' "$HDR")"
[[ "$deadline" =~ ^[0-9]+$ ]] || { echo "bad header" >&2; exit 2; }
cd "${HOME}/lr16/code"
date '+%F %T %Z' | tee -a "$TIME"
now="$(date +%s)"
set +e
if (( now < deadline )); then
  echo "BUDGET=$(( deadline - now ))" | tee -a "$LOG"
  BUDGET=$(( deadline - now )) python3 "${HOME}/kit/kcascade_run.py" ./bgk15 ./cascade_k15p "$P" 8 "$OUTD" 2>&1 | tee -a "$LOG"
  rc=${PIPESTATUS[0]}
else
  echo "no BUDGET (start after $(awk '$1 == "budget" { $1 = ""; print; exit }' "$HDR"))" | tee -a "$LOG"
  python3 "${HOME}/kit/kcascade_run.py" ./bgk15 ./cascade_k15p "$P" 8 "$OUTD" 2>&1 | tee -a "$LOG"
  rc=${PIPESTATUS[0]}
fi
set -e
date '+%F %T %Z' | tee -a "$TIME"
verdict="$(prime_verdict "$rc" "$LOG" "$OUTD/ir.jsonl")"
printf '%s %s rc=%s\n' "$(date '+%F %T %Z')" "$verdict" "$rc" | tee -a "$LOG" >> "$STATE/p${P}.result"
case "$verdict" in
  DONE*)
    if ! grep -q '^jobs ' "$HDR"; then
      printf 'jobs %s\n' "$(grep -oE '^ir jobs [0-9]+' "$LOG" | awk '{ print $3; exit }')" >> "$HDR"
    fi
    date '+%F %T %Z' > "$STATE/p${P}.done"
    ;;
  MISMATCH*)
    printf '%s\n' "$verdict" > "$STATE/p${P}.mismatch"
    ;;
esac
