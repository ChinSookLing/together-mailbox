# Reader check. No office PC and no network.
set +x
set -euo pipefail
cd "$(dirname "$0")/.."
for file in gates/*.sh; do
  bash -n "$file"
done
python3 - << 'PY'
import json, pathlib, subprocess, tempfile, os, textwrap, sys
sys.path.insert(0, "gates")
import importlib.util
spec = importlib.util.spec_from_file_location("km1_extract", "gates/km1_extract.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
raw = {
    "roots": 1,
    "survivor_lines": [
        "SURVIVOR base: 1 l4=0",
        "SURVIVOR base: 2 l4=4 l8=0",
        "SURVIVOR base: 3 l4=4 PERSISTENT",
    ],
}
with tempfile.TemporaryDirectory() as tmp:
    src = pathlib.Path(tmp) / "km1.json"
    dest = pathlib.Path(tmp) / "out.txt"
    src.write_text(json.dumps(raw), encoding="utf-8")
    digest, nbytes, counts, kept = mod.extract(src)
    assert counts["survivor_lines"]["l4=0"] == 1
    assert counts["survivor_lines"]["l8=0"] == 1
    assert counts["survivor_lines"]["PERSISTENT"] == 1
    assert kept == ["SURVIVOR base: 2 l4=4 l8=0", "SURVIVOR base: 3 l4=4 PERSISTENT"]
    assert nbytes == src.stat().st_size
    assert len(digest) == 64
print("km1 extract ok")
PY

export STAGE="$(mktemp -d)"
# shellcheck source=gates/lib.sh
source gates/lib.sh
root="$(mktemp -d)"
mkdir -p "$root/PT005/bill" "$root/PT005/hesper" "$root/PT005/opus" "$root/scouting"
printf '%s\n' "$HASH_EARLY" > "$root/PT005/bill/office-gate-letter.md"
printf '%s\n' "$HASH_EARLY" > "$root/PT005/opus/2026-read-record.md"
printf 'no\n' > "$root/PT005/hesper/note.md"
printf '%s\n' "$HASH_EARLY" > "$root/PT005/hesper/DeepSeek-read-early.md"
printf '%s\n' "$HASH_EARLY" > "$root/scouting/SHA256SUMS"
found="$(find_read_records "$root")"
test "$found" = "PT005/hesper/DeepSeek-read-early.md"
echo "read-record predicate ok"

yml_opts="$(awk '/^          - /{print $2}' .github/workflows/office-gate.yml | head -6 | paste -sd ' ' -)"
case_opts="$(awk '/^  status\)/{f=1} f && /^  [a-z0-9-]+\)/{print $1}' gates/dispatch.sh | tr -d ')' | paste -sd ' ' -)"
test "$yml_opts" = "status p233-pack p191 p241ab p241c collect"
test "$case_opts" = "status p233-pack p191 p241ab p241c collect"
echo "menu matches"
echo "self-check ok"
