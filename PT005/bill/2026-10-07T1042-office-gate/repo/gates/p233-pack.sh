# Menu p233-pack. The run already finished on the office PC.
# Copies the files named in the handover f074bd3, then runs the two already-read compares.
# Chair files come from together-mailbox at MAILBOX_PIN, after a sha256 check.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"

copy_out "$HOME/core233/cores.jsonl" cores.jsonl
copy_out "$HOME/core233/run.log" run.log
copy_out "$HOME/core233/run.time" run.time
copy_out "$HOME/core233/km1low.log" km1low.log
copy_out "$HOME/core233/kit.sha256" kit.sha256
copy_out "$HOME/kit/run233.log" run233.log
copy_out "$HOME/kit/run233.time" run233.time
copy_out "$HOME/lr16/out233/ir.jsonl" ir.jsonl
shrink_km1 "$HOME/lr16/out233/km1.json" km1

pin="$(mktemp -d)"
fetch_pin "$pin"
check_hash "$pin/scouting/LR16/opus/core223/compare_cores.py" scouting/LR16/opus/core223/compare_cores.py
check_hash "$pin/scouting/LR16/opus/gate233/chair_cores233.jsonl" scouting/LR16/opus/gate233/chair_cores233.jsonl
check_hash "$pin/scouting/LR16/opus/officepc/compare_239.py" scouting/LR16/opus/officepc/compare_239.py
check_hash "$pin/scouting/LR16/opus/gate233/ir_K15_p233.jsonl" scouting/LR16/opus/gate233/ir_K15_p233.jsonl
check_hash "$pin/scouting/LR16/opus/gate233/km1_K15_p233.json" scouting/LR16/opus/gate233/km1_K15_p233.json

if [[ -f "$HOME/core233/cores.jsonl" && -f "$pin/scouting/LR16/opus/gate233/chair_cores233.jsonl" ]]; then
  python3 "$pin/scouting/LR16/opus/core223/compare_cores.py" \
    "$HOME/core233/cores.jsonl" \
    "$pin/scouting/LR16/opus/gate233/chair_cores233.jsonl" \
    | tee "$STAGE/compare-cores.txt"
else
  note "compare_cores not run: cores.jsonl or the chair file is missing"
fi

if [[ -d "$HOME/lr16/out233" && -f "$HOME/lr16/out233/ir.jsonl" && -f "$HOME/lr16/out233/km1.json" ]]; then
  python3 "$pin/scouting/LR16/opus/officepc/compare_239.py" \
    "$HOME/lr16/out233" \
    "$pin/scouting/LR16/opus/gate233/ir_K15_p233.jsonl" \
    "$pin/scouting/LR16/opus/gate233/km1_K15_p233.json" \
    | tee "$STAGE/compare-239.txt"
else
  note "compare_239 not run: out233 is missing ir.jsonl or km1.json"
fi
