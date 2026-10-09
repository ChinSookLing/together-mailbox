# Long run for menu p337. Same command as p409, prime 337.
# systemd starts this with /bin/bash. No nohup.
# Run sheet: scouting/LR16/opus/officepc/RUN-SHEET-weekend-a-307-337-383.md
# tee -a so a restart does not truncate the log or the time file.
# kcascade_run.py skips jobs it already finished.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"
math_run_lock
if pgrep -f '[k]cascade_run.py' >/dev/null 2>&1 || pgrep -f '[b]gk15' >/dev/null 2>&1; then
  printf '%s\n' "refused" > "${HOME}/kit/math-lock.refused"
  echo "refusing: another kcascade or bgk15 job is running" >&2
  exit 2
fi
math_run_ready
STATE="${HOME}/office-gate/state"
sha256sum -c "$STATE/p337-pc-kit.sha256"
cd "${HOME}/lr16/code"
date '+%F %T %Z' | tee -a "${HOME}/kit/run337.time"
python3 "${HOME}/kit/kcascade_run.py" ./bgk15 ./cascade_k15p 337 12 "${HOME}/lr16/out337" 2>&1 | tee -a "${HOME}/kit/run337.log"
date '+%F %T %Z' | tee -a "${HOME}/kit/run337.time"
date '+%F %T %Z' > "$STATE/p337.done"
