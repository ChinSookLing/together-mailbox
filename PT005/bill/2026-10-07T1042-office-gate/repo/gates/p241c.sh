# Menu p241c. Refuses to compile unless a non-author read record exists.
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

main="$(mktemp -d)"
fetch_mailbox_main "$main"
records="$(find_read_records "$main" || true)"
if [[ -z "$records" ]]; then
  note "REFUSED. No read record for shift_rows_early.cpp ${HASH_EARLY}."
  note "Need a PT005 file outside PT005/bill and PT005/opus, whose filename contains read, and whose text contains that sha256."
  exit 0
fi
printf '%s\n' "$records" > "$STAGE/read_record_paths.txt"

pin="${HOME}/office-gate/pin/p241c"
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
detach office-gate-p241c "$ROOT/gates/p241c-run.sh"
