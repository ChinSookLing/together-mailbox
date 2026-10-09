# Long run for menu p307. Same command as p409, prime 307.
# systemd starts this with /bin/bash. No nohup.
# Run sheet: scouting/LR16/opus/officepc/RUN-SHEET-weekend-a-307-337-383.md
# tee -a so a restart does not truncate the log or the time file.
# kcascade_run.py skips jobs it already finished.
set +x
set -euo pipefail
STATE="${HOME}/office-gate/state"
sha256sum -c "$STATE/p307-pc-kit.sha256"
if pgrep -f '[k]cascade_run.py' >/dev/null 2>&1 || pgrep -f '[b]gk15' >/dev/null 2>&1; then
  echo "refusing: another kcascade or bgk15 job is running" >&2
  exit 2
fi
cd "${HOME}/lr16/code"
date '+%F %T %Z' | tee -a "${HOME}/kit/run307.time"
python3 "${HOME}/kit/kcascade_run.py" ./bgk15 ./cascade_k15p 307 12 "${HOME}/lr16/out307" 2>&1 | tee -a "${HOME}/kit/run307.log"
date '+%F %T %Z' | tee -a "${HOME}/kit/run307.time"
date '+%F %T %Z' > "$STATE/p307.done"
