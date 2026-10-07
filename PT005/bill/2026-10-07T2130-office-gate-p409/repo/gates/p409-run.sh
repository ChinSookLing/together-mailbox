# Long run for menu p409. Same command as p241ab, prime 409.
# systemd starts this with /bin/bash. No nohup.
# Run sheet: scouting/LR16/opus/officepc/RUN-SHEET-p409.md at f32aee7.
set +x
set -euo pipefail
STATE="${HOME}/office-gate/state"
sha256sum -c "$STATE/p409-pc-kit.sha256"
cd "${HOME}/lr16/code"
date '+%F %T %Z' | tee "${HOME}/kit/run409.time"
python3 "${HOME}/kit/kcascade_run.py" ./bgk15 ./cascade_k15p 409 12 "${HOME}/lr16/out409" 2>&1 | tee "${HOME}/kit/run409.log"
date '+%F %T %Z' | tee -a "${HOME}/kit/run409.time"
date '+%F %T %Z' > "$STATE/p409.done"
