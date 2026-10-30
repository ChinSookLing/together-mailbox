# Long run for menu p241ab. Parts (a) and (b) only.
# Commands are that block of scouting/LR16/opus/gate241/RUN-SHEET-p241.md
# at mailbox pin 92c31a73cbcda6e4a00893bf2116aca66c5546b7.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"
math_run_lock
math_run_ready
STATE="${HOME}/office-gate/state"
sha256sum -c "$STATE/p241ab-pc-kit.sha256"
cd "${HOME}/lr16/code"
date '+%F %T %Z' | tee "${HOME}/kit/run241.time"
python3 "${HOME}/kit/kcascade_run.py" ./bgk15 ./cascade_k15p 241 12 "${HOME}/lr16/out241" 2>&1 | tee "${HOME}/kit/run241.log"
date '+%F %T %Z' | tee -a "${HOME}/kit/run241.time"
date '+%F %T %Z' > "$STATE/p241ab.done"
