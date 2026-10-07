# Menu p241c. Refuses unless gates/p241c-lock.txt names one file and its sha256.
# This revision's lock is chair note 38. A dash would refuse and would not compile.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

if [[ -f "$HOME/office-gate/state/p241c.done" ]]; then
  note "p241c already finished. Use collect."
  exit 0
fi
if [[ -f "$HOME/office-gate/state/p241c.stopped" ]]; then
  note "p241c stopped earlier. Not starting again. See collect."
  exit 0
fi
if unit_active office-gate-p241c; then
  note "p241c unit is already running."
  exit 0
fi

set +e
decision="$(p241c_decide "$ROOT/gates/p241c-lock.txt")"
dec_rc=$?
set -e
printf '%s\n' "$decision" > "$STAGE/p241c-lock.txt"
if [[ "$dec_rc" -ne 0 ]]; then
  note "REFUSED. p241c-lock.txt has no specific read-record path and sha256. Not compiling."
  exit 2
fi

main="$(mktemp -d)"
pin=""
trap 'rm -rf "$main" ${pin:+"$pin"}' EXIT
fetch_mailbox_main "$main"
set +e
decision="$(p241c_decide "$ROOT/gates/p241c-lock.txt" "$main")"
dec_rc=$?
set -e
printf '%s\n' "$decision" > "$STAGE/p241c-lock.txt"
if [[ "$dec_rc" -ne 0 ]]; then
  note "REFUSED. The locked read record is missing or its sha256 does not match. Not compiling."
  exit 2
fi

pin="$(mktemp -d)"
fetch_pin "$pin"
install -d "$HOME/core241" "$HOME/office-gate/state"
cp "$pin/scouting/LR16/opus/gate233/run_cores.py" "$HOME/core241/"
cp "$pin/scouting/LR16/opus/gate241/shift_rows_early.cpp" "$HOME/core241/"
cp "$pin/scouting/LR16/opus/core223/compare_cores.py" "$HOME/core241/"
check_hash "$HOME/core241/run_cores.py" scouting/LR16/opus/gate233/run_cores.py
check_hash "$HOME/core241/shift_rows_early.cpp" scouting/LR16/opus/gate241/shift_rows_early.cpp
check_hash "$HOME/core241/compare_cores.py" scouting/LR16/opus/core223/compare_cores.py
check_hash "$pin/scouting/LR16/opus/gate241/chair_cores241_early.jsonl" scouting/LR16/opus/gate241/chair_cores241_early.jsonl
{
  printf '%s  run_cores.py\n' "$(want_hash scouting/LR16/opus/gate233/run_cores.py)"
  printf '%s  shift_rows_early.cpp\n' "$(want_hash scouting/LR16/opus/gate241/shift_rows_early.cpp)"
  printf '%s  compare_cores.py\n' "$(want_hash scouting/LR16/opus/core223/compare_cores.py)"
} > "$HOME/office-gate/state/p241c-kit.sha256"
( cd "$HOME/core241" && sha256sum run_cores.py shift_rows_early.cpp compare_cores.py | tee kit.sha256 ) > "$STAGE/kit.sha256"
rm -rf "$pin"
detach office-gate-p241c "$ROOT/gates/p241c-run.sh"
