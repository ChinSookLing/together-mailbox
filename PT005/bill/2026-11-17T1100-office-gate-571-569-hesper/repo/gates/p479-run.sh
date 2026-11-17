# Long run for menu p479. Same command as p307, prime 479, 8 workers.
# Author: Hesper (copy of p449-run.sh, prime 449 -> 479), per Opus chair note 117 (mailbox 3f25e558, 2026-10-26).
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
if ! sha256sum -c "$STATE/p479-pc-kit.sha256"; then
  printf '%s\n' "refused" > "${HOME}/kit/math-lock.refused"
  exit 2
fi
math_run_ready
cd "${HOME}/lr16/code"
date '+%F %T %Z' | tee -a "${HOME}/kit/run479.time"
python3 "${HOME}/kit/kcascade_run.py" ./bgk15 ./cascade_k15p 479 8 "${HOME}/lr16/out479" 2>&1 | tee -a "${HOME}/kit/run479.log"
date '+%F %T %Z' | tee -a "${HOME}/kit/run479.time"
date '+%F %T %Z' > "$STATE/p479.done"
