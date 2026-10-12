# Long run for menu p191. Started by systemd, not by the Actions job.
# Commands are the bash block of scouting/LR16/opus/gate191/RUN-SHEET-p191.md
# at mailbox pin 92c31a73cbcda6e4a00893bf2116aca66c5546b7.
# Chair files are fetched into a fresh temp directory at the compare step.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"
math_run_lock
math_run_ready
export STAGE="$(mktemp -d)"
pin=""
trap 'rm -rf "$STAGE" ${pin:+"$pin"}' EXIT
STATE="${HOME}/office-gate/state"
mkdir -p "$STATE"
fail() { printf '%s\n' "$*" | tee "$STATE/p191.stopped" >/dev/null; exit 2; }

cd "${HOME}/core191"
sha256sum run_cores.py shift_rows.cpp compare_cores.py | tee kit.sha256
sha256sum -c "$STATE/p191-kit.sha256"
g++ -O2 -std=c++17 -DPP=191 -o shift_rows191 shift_rows.cpp
"${HOME}/lr16/code/bgk15" 191 km1low 13 km1low13_p191.txt | tee km1low.log
sha256sum km1low13_p191.txt | tee km1low13.sha256
got="$(sha256sum km1low13_p191.txt | awk '{ print $1 }')"
want="6fce3acbe19b1a19b67f08cfce318880cca2a68fd41193d0414a22bb07c39c13"
[[ "$got" == "$want" ]] || fail "STOP km1low13 sha256 ${got} want ${want}"
grep -q 'canonical=260' km1low.log || fail "STOP km1low.log did not say canonical=260"
date '+%F %T %Z' | tee run.time
P=191 WORKERS=12 python3 run_cores.py km1low13_p191.txt | tee run.log
date '+%F %T %Z' | tee -a run.time
pin="$(mktemp -d)"
fetch_pin "$pin"
cp "$pin/scouting/LR16/opus/gate191/chair_cores191.jsonl" .
check_hash chair_cores191.jsonl scouting/LR16/opus/gate191/chair_cores191.jsonl
rm -rf "$pin"
pin=""
python3 compare_cores.py cores.jsonl chair_cores191.jsonl | tee compare.txt

sha256sum -c "$STATE/p191-pc-kit.sha256"
pin="$(mktemp -d)"
fetch_pin "$pin"
mkdir -p "${HOME}/kit/ref191"
cp "$pin/scouting/LR16/opus/gate191/ir_K15_p191.jsonl" "${HOME}/kit/ref191/"
cp "$pin/scouting/LR16/opus/gate191/km1_K15_p191.json" "${HOME}/kit/ref191/"
check_hash "${HOME}/kit/ref191/ir_K15_p191.jsonl" scouting/LR16/opus/gate191/ir_K15_p191.jsonl
check_hash "${HOME}/kit/ref191/km1_K15_p191.json" scouting/LR16/opus/gate191/km1_K15_p191.json
rm -rf "$pin"
pin=""
cd "${HOME}/lr16/code"
date '+%F %T %Z' | tee "${HOME}/kit/run191.time"
python3 "${HOME}/kit/kcascade_run.py" ./bgk15 ./cascade_k15p 191 12 "${HOME}/lr16/out191" 2>&1 | tee "${HOME}/kit/run191.log"
date '+%F %T %Z' | tee -a "${HOME}/kit/run191.time"
python3 "${HOME}/kit/compare_239.py" "${HOME}/lr16/out191" \
  "${HOME}/kit/ref191/ir_K15_p191.jsonl" "${HOME}/kit/ref191/km1_K15_p191.json" \
  | tee "${HOME}/kit/compare191.txt"
date '+%F %T %Z' > "$STATE/p191.done"
