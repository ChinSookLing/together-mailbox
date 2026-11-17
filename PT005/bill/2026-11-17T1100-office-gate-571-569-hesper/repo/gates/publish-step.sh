# The only step that receives the write token. It does not run a gate.
set +x
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
sha256sum -c SHA256SUMS
pathfile="${HOME}/office-gate/state/stage-${RUN_ID:?}.path"
if [[ ! -f "$pathfile" ]]; then
  stage="$(mktemp -d)"
  printf '%s\n' "no stage from the menu step" > "$stage/NOTE.txt"
  printf '%s\n' "3" > "$stage/exit_code.txt"
  date '+%F %T %Z' > "$stage/DATE.txt"
  (
    cd "$stage"
    find . -type f ! -name SHA256SUMS | sort | while IFS= read -r file; do
      sha256sum "$file"
    done
  ) > "$stage/SHA256SUMS"
else
  stage="$(cat "$pathfile")"
fi
bash "$ROOT/gates/publish.sh" "$stage"
rm -rf "$stage"
rm -f "$pathfile"
