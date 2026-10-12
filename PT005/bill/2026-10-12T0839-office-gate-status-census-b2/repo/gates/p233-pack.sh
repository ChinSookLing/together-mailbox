# Menu p233-pack. The run already finished on the office PC.
# Copies the files named in the handover f074bd3, then runs the two already-read compares.
# Chair files come from a fresh temp checkout of MAILBOX_PIN, after a sha256 check.
# Missing file or a compare that did not run: exit 2.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"
incomplete=0

require_src() {
  local src="$1" name="$2"
  if [[ -f "$src" ]]; then
    cp -p "$src" "$STAGE/$name"
  else
    note "missing ${src}"
    incomplete=1
  fi
}

require_src "$HOME/core233/cores.jsonl" cores.jsonl
require_src "$HOME/core233/run.log" run.log
require_src "$HOME/core233/run.time" run.time
require_src "$HOME/core233/km1low.log" km1low.log
require_src "$HOME/core233/kit.sha256" kit.sha256
require_src "$HOME/kit/run233.log" run233.log
require_src "$HOME/kit/run233.time" run233.time
require_src "$HOME/lr16/out233/ir.jsonl" ir.jsonl
if [[ -f "$HOME/lr16/out233/km1.json" ]]; then
  shrink_km1 "$HOME/lr16/out233/km1.json" km1
else
  note "missing ${HOME}/lr16/out233/km1.json"
  incomplete=1
fi

pin="$(mktemp -d)"
trap 'rm -rf "$pin"' EXIT
fetch_pin "$pin"
check_hash "$pin/scouting/LR16/opus/core223/compare_cores.py" scouting/LR16/opus/core223/compare_cores.py
check_hash "$pin/scouting/LR16/opus/gate233/chair_cores233.jsonl" scouting/LR16/opus/gate233/chair_cores233.jsonl
check_hash "$pin/scouting/LR16/opus/officepc/compare_239.py" scouting/LR16/opus/officepc/compare_239.py
check_hash "$pin/scouting/LR16/opus/gate233/ir_K15_p233.jsonl" scouting/LR16/opus/gate233/ir_K15_p233.jsonl
check_hash "$pin/scouting/LR16/opus/gate233/km1_K15_p233.json" scouting/LR16/opus/gate233/km1_K15_p233.json

if [[ -f "$HOME/core233/cores.jsonl" ]]; then
  python3 "$pin/scouting/LR16/opus/core223/compare_cores.py" \
    "$HOME/core233/cores.jsonl" \
    "$pin/scouting/LR16/opus/gate233/chair_cores233.jsonl" \
    | tee "$STAGE/compare-cores.txt"
else
  note "compare_cores not run"
  incomplete=1
fi

if [[ -f "$HOME/lr16/out233/ir.jsonl" && -f "$HOME/lr16/out233/km1.json" ]]; then
  python3 "$pin/scouting/LR16/opus/officepc/compare_239.py" \
    "$HOME/lr16/out233" \
    "$pin/scouting/LR16/opus/gate233/ir_K15_p233.jsonl" \
    "$pin/scouting/LR16/opus/gate233/km1_K15_p233.json" \
    | tee "$STAGE/compare-239.txt"
else
  note "compare_239 not run"
  incomplete=1
fi

if [[ "$incomplete" -ne 0 || ! -f "$STAGE/compare-cores.txt" || ! -f "$STAGE/compare-239.txt" ]]; then
  note "INCOMPLETE"
  exit 2
fi
