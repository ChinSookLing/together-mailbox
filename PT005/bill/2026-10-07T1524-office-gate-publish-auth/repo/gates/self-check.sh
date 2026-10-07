# Reader check. No office PC and no network.
set +x
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
cd "$(dirname "$0")/.."
if find . -name '*.pyc' -o -name '__pycache__' | grep -q .; then
  echo "bytecode in the tree" >&2
  exit 1
fi
if grep -n '^find_read_records()' gates/*.sh gates/*.py >/dev/null 2>&1; then
  echo "filename read-record scan is still here" >&2
  exit 1
fi
for file in gates/*.sh; do
  bash -n "$file"
done
python3 - << 'PY'
import json, os, tempfile, importlib.util
spec = importlib.util.spec_from_file_location("km1_extract", "gates/km1_extract.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
lines = ["SURVIVOR base: %d l4=4" % i for i in range(2001)]
lines.append("SURVIVOR base: x l4=0")
tmp = tempfile.mkdtemp()
src = os.path.join(tmp, "km1.json")
with open(src, "w", encoding="utf-8") as handle:
    json.dump({"survivor_lines": lines}, handle)
digest, nbytes, counts, kept = mod.extract(src)
assert counts["survivor_lines"]["n"] == 2002
assert counts["survivor_lines"]["l4=0"] == 1
assert len(kept) == 2001
assert all("l4=0" not in line for line in kept)
assert len(digest) == 64 and nbytes > 0
print("km1 extract keeps every non-l4=0 line")
PY

export STAGE="$(mktemp -d)"
# shellcheck source=gates/lib.sh
source gates/lib.sh
set +e
out="$(p241c_decide gates/p241c-lock.txt)"
rc=$?
set -e
test "$rc" -eq 2
test "$out" = "REFUSED unset"
root="$(mktemp -d)"
mkdir -p "$root/PT005/hesper"
printf 'the real letter\n' > "$root/PT005/hesper/deepseek-letter.md"
decoy="$root/PT005/hesper/something-read.md"
printf '%s\n' "$HASH_EARLY" > "$decoy"
sha="$(sha256sum "$root/PT005/hesper/deepseek-letter.md" | awk '{ print $1 }')"
lock="$(mktemp)"
printf 'path PT005/hesper/deepseek-letter.md\nsha256 %s\n' "$sha" > "$lock"
set +e
out="$(p241c_decide "$lock" "$root")"
rc=$?
set -e
test "$rc" -eq 0
test "$out" = "OK"
bad="$(mktemp)"
printf 'path PT005/hesper/something-read.md\nsha256 %s\n' "$sha" > "$bad"
set +e
out="$(p241c_decide "$bad" "$root")"
rc=$?
set -e
test "$rc" -eq 2
test "$out" = "REFUSED hash"
echo "p241c lock ok"

yml_opts="$(awk '/^          - /{print $2}' .github/workflows/office-gate.yml | head -6 | paste -sd ' ' -)"
case_opts="$(awk '/^    status\)/{f=1} f && /^    [a-z0-9-]+\)/{print $1}' gates/dispatch.sh | tr -d ')' | paste -sd ' ' -)"
test "$yml_opts" = "status p233-pack p191 p241ab p241c collect"
test "$case_opts" = "status p233-pack p191 p241ab p241c collect"
test "$(grep -c 'github.token' .github/workflows/office-gate.yml)" = "1"
if grep -q 'GITHUB_SHA' .github/workflows/office-gate.yml; then
  echo "workflow still follows GITHUB_SHA" >&2
  exit 1
fi
echo "menu matches"
echo "self-check ok"
