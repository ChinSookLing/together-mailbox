# Menu collect. Copies finished or still-running outputs. Does not start a run.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"
which="${COLLECT_WHICH:-none}"
case "$which" in
  none) note "collect_which is none"; exit 0 ;;
  all) items="p191 p241ab p241c p409" ;;
  p191|p241ab|p241c|p409) items="$which" ;;
  *) note "bad collect_which"; exit 2 ;;
esac

one() {
  local item="$1" unit="office-gate-$1" dir="$STAGE/$1"
  mkdir -p "$dir"
  local saved="$STAGE"
  STAGE="$dir"
  if unit_active "$unit"; then
    note "RUNNING ${unit}"
  fi
  if [[ -f "$HOME/office-gate/state/${unit}.log" ]]; then
    tail -n 40 "$HOME/office-gate/state/${unit}.log" > "$dir/systemd.tail"
  fi
  copy_out "$HOME/office-gate/state/${item}.done" "${item}.done"
  copy_out "$HOME/office-gate/state/${item}.stopped" "${item}.stopped"
  case "$item" in
    p191)
      copy_out "$HOME/core191/cores.jsonl" cores.jsonl
      copy_out "$HOME/core191/run.log" run.log
      copy_out "$HOME/core191/run.time" run.time
      copy_out "$HOME/core191/km1low.log" km1low.log
      copy_out "$HOME/core191/kit.sha256" kit.sha256
      copy_out "$HOME/core191/compare.txt" compare.txt
      copy_out "$HOME/core191/km1low13.sha256" km1low13.sha256
      copy_out "$HOME/kit/run191.log" run191.log
      copy_out "$HOME/kit/run191.time" run191.time
      copy_out "$HOME/kit/compare191.txt" compare191.txt
      copy_out "$HOME/lr16/out191/ir.jsonl" ir.jsonl
      shrink_km1 "$HOME/lr16/out191/km1.json" km1
      ;;
    p241ab)
      copy_out "$HOME/kit/run241.log" run241.log
      copy_out "$HOME/kit/run241.time" run241.time
      copy_out "$HOME/lr16/out241/ir.jsonl" ir.jsonl
      shrink_km1 "$HOME/lr16/out241/km1.json" km1
      ;;
    p241c)
      copy_out "$HOME/core241/cores.jsonl" cores.jsonl
      copy_out "$HOME/core241/run.log" run.log
      copy_out "$HOME/core241/run.time" run.time
      copy_out "$HOME/core241/km1low.log" km1low.log
      copy_out "$HOME/core241/kit.sha256" kit.sha256
      copy_out "$HOME/core241/compare.txt" compare.txt
      copy_out "$HOME/core241/km1low13.sha256" km1low13.sha256
      ;;
    p409)
      copy_out "$HOME/kit/run409.log" run409.log
      copy_out "$HOME/kit/run409.time" run409.time
      copy_out "$HOME/lr16/out409/ir.jsonl" ir.jsonl
      shrink_km1 "$HOME/lr16/out409/km1.json" km1
      ;;
  esac
  STAGE="$saved"
}

for item in $items; do
  one "$item"
done
