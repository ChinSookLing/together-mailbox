# Gate repair-tail (Opus chair note 127, 36315df8). Reusable. Input JOB = a K11 job name on the menu.
# Refuses if: JOB malformed or not on the menu; any k11-job-* unit active; JOB already DONE; ir.jsonl missing.
# Then runs gates/repair_tail.py on $WORK/$JOB/out<prime>/ir.jsonl: keeps the leading complete JSON lines,
# moves the rest to a timestamped side file (never overwritten), atomic replace; tail only (mid-file bad line = refuse).
# Publishes sha256 + bytes of before / kept / side, kept line count and kept (r, s), plus copies of the kept file and
# side file. No compute, no delete, no job start.
set +x
set -uo pipefail
source "$(dirname "$0")/lib.sh"
need_bus
J="${JOB:-}"
[[ "$J" =~ ^k11-p([0-9]+)a$ ]] || { note "refusing: job '$J' is not of the form k11-p<prime>a"; exit 2; }
P="${BASH_REMATCH[1]}"
known_job "$J" || { note "refusing: $J has no job file"; exit 2; }
grep -qE "^  ${J}\) " "${D}/gates/entry.sh" || { note "refusing: $J not on the menu"; exit 2; }
for u in $(systemctl --user list-units --plain --no-legend 'k11-job-*' 2>/dev/null | awk '{print $1}'); do
  note "refusing: $u is active"; exit 2
done
[[ -f "$STATE/$J.done" ]] && { note "refusing: $J already DONE"; exit 2; }
grep -qF "R=\"\$W/out${P}\"" "${D}/jobs/$J.sh" || { note "refusing: job file does not use out${P}"; exit 2; }
IR="$WORK/$J/out${P}/ir.jsonl"
[[ -f "$IR" ]] || { note "refusing: $IR missing"; exit 2; }
printf 'job=%s\n' "$J" >> "$OUT/menu.txt"
python3 "${D}/gates/repair_tail.py" "$IR" "$OUT"; rc=$?
note "repair_tail.py rc=$rc"
cp -f "$IR" "$OUT/ir.jsonl.after" 2>/dev/null
side=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("side_file",""))' "$OUT/repair-tail.json" 2>/dev/null)
[[ -n "$side" && -f "$side" ]] && cp -f "$side" "$OUT/$(basename "$side")"
exit "$rc"
