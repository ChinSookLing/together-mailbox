# Long run for menu p487. Same command as p307, prime 487, 8 workers.
# Author: Hesper (copy of p467-run.sh, prime 467 -> 487), per Opus chair note 120 (mailbox 5aa968a4).
# systemd starts this with /bin/bash. No nohup.
# kcascade_run.py skips jobs it already finished.
# If km1.json is absent it writes that file first, then the ir jobs.
# tee -a so a restart does not truncate the log or the time file.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"
math_run_lock
if pgrep -f '[k]cascade_run.py' >/dev/null 2>&1 || pgrep -f '[b]gk15' >/dev/null 2>&1; then
  printf '%s\n' "refused" > "${HOME}/kit/math-lock.refused"
  echo "refusing: another kcascade or bgk15 job is running" >&2
  exit 2
fi
STATE="${HOME}/office-gate/state"
if ! sha256sum -c "$STATE/p487-pc-kit.sha256"; then
  printf '%s\n' "refused" > "${HOME}/kit/math-lock.refused"
  exit 2
fi
math_run_ready
cd "${HOME}/lr16/code"
date '+%F %T %Z' | tee -a "${HOME}/kit/run487.time"
python3 "${HOME}/kit/kcascade_run.py" ./bgk15 ./cascade_k15p 487 8 "${HOME}/lr16/out487" 2>&1 | tee -a "${HOME}/kit/run487.log"
date '+%F %T %Z' | tee -a "${HOME}/kit/run487.time"
date '+%F %T %Z' > "$STATE/p487.done"
