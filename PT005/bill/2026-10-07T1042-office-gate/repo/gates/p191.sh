# Menu p191. Prepares the pinned files, then detaches the run sheet.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

if [[ -f "$HOME/office-gate/state/p191.done" ]]; then
  note "p191 already finished. Use collect."
  exit 0
fi
if [[ -f "$HOME/office-gate/state/p191.stopped" ]]; then
  note "p191 stopped earlier. Not starting again. See collect."
  exit 0
fi
if unit_active office-gate-p191; then
  note "p191 unit is already running."
  exit 0
fi

pin="${HOME}/office-gate/pin/p191"
fetch_pin "$pin"
install -d "$HOME/core191" "$HOME/office-gate/state"
cp "$pin/scouting/LR16/opus/gate233/run_cores.py" "$HOME/core191/"
cp "$pin/scouting/LR16/opus/gate233/shift_rows.cpp" "$HOME/core191/"
cp "$pin/scouting/LR16/opus/core223/compare_cores.py" "$HOME/core191/"
check_hash "$HOME/core191/run_cores.py" scouting/LR16/opus/gate233/run_cores.py
check_hash "$HOME/core191/shift_rows.cpp" scouting/LR16/opus/gate233/shift_rows.cpp
check_hash "$HOME/core191/compare_cores.py" scouting/LR16/opus/core223/compare_cores.py
check_hash "$pin/scouting/LR16/opus/gate191/chair_cores191.jsonl" scouting/LR16/opus/gate191/chair_cores191.jsonl
check_hash "$pin/scouting/LR16/opus/gate191/ir_K15_p191.jsonl" scouting/LR16/opus/gate191/ir_K15_p191.jsonl
check_hash "$pin/scouting/LR16/opus/gate191/km1_K15_p191.json" scouting/LR16/opus/gate191/km1_K15_p191.json
check_hash "$HOME/kit/kcascade_run.py" scouting/LR16/opus/officepc/kcascade_run.py
check_hash "$HOME/kit/compare_239.py" scouting/LR16/opus/officepc/compare_239.py

{
  printf '%s  run_cores.py\n' "$(want_hash scouting/LR16/opus/gate233/run_cores.py)"
  printf '%s  shift_rows.cpp\n' "$(want_hash scouting/LR16/opus/gate233/shift_rows.cpp)"
  printf '%s  compare_cores.py\n' "$(want_hash scouting/LR16/opus/core223/compare_cores.py)"
} > "$HOME/office-gate/state/p191-kit.sha256"
{
  printf '%s  %s\n' "$(want_hash scouting/LR16/opus/officepc/kcascade_run.py)" "$HOME/kit/kcascade_run.py"
  printf '%s  %s\n' "$(want_hash scouting/LR16/opus/officepc/compare_239.py)" "$HOME/kit/compare_239.py"
} > "$HOME/office-gate/state/p191-pc-kit.sha256"
( cd "$HOME/core191" && sha256sum run_cores.py shift_rows.cpp compare_cores.py ) > "$STAGE/kit.sha256"

detach office-gate-p191 "$ROOT/gates/p191-run.sh"
