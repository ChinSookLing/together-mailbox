# Long-enough run for menu p241c. Part (c) only, with shift_rows_early.cpp.
# Commands are that block of scouting/LR16/opus/gate241/RUN-SHEET-p241.md
# at mailbox pin 92c31a73cbcda6e4a00893bf2116aca66c5546b7.
set +x
set -euo pipefail
PIN="${HOME}/office-gate/pin/p241c"
STATE="${HOME}/office-gate/state"
fail() { printf '%s\n' "$*" | tee "$STATE/p241c.stopped" >/dev/null; exit 2; }

cd "${HOME}/core241"
sha256sum -c "$STATE/p241c-kit.sha256"
g++ -O2 -std=c++17 -DPP=241 -o shift_rows241 shift_rows_early.cpp
"${HOME}/lr16/code/bgk15" 241 km1low 13 km1low13_p241.txt | tee km1low.log
sha256sum km1low13_p241.txt | tee km1low13.sha256
got="$(sha256sum km1low13_p241.txt | awk '{ print $1 }')"
want="312d59273a32a6fcc9b12766e047a29dce266ab30b6121b31a8406b7443c1108"
[[ "$got" == "$want" ]] || fail "STOP km1low13 sha256 ${got} want ${want}"
grep -q 'canonical=936' km1low.log || fail "STOP km1low.log did not say canonical=936"
date '+%F %T %Z' | tee run.time
P=241 WORKERS=12 python3 run_cores.py km1low13_p241.txt | tee run.log
date '+%F %T %Z' | tee -a run.time
cp "$PIN/scouting/LR16/opus/gate241/chair_cores241_early.jsonl" .
python3 compare_cores.py cores.jsonl chair_cores241_early.jsonl | tee compare.txt
date '+%F %T %Z' > "$STATE/p241c.done"
