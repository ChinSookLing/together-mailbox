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
test "$rc" -eq 0
test "$out" = "OK"
dash="$(mktemp)"
printf 'path -\nsha256 -\n' > "$dash"
set +e
out="$(p241c_decide "$dash")"
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

yml_opts="$(awk '/^          - /{print $2}' .github/workflows/office-gate.yml | head -11 | paste -sd ' ' -)"
case_opts="$(awk '/^    status\)/{f=1} f && /^    [a-z0-9-]+\)/{print $1}' gates/dispatch.sh | tr -d ')' | paste -sd ' ' -)"
test "$yml_opts" = "status p233-pack p191 p241ab p241c p409 p383 p307 p337 collect update"
test "$case_opts" = "status p233-pack p191 p241ab p241c p409 p383 p307 p337 collect update"
for name in p383 p307 p337; do
  grep -q "    ${name})" gates/dispatch.sh
  grep -q "          - ${name}" .github/workflows/office-gate.yml
  grep -q "${name}" gates/publish.sh
  test -f "gates/${name}.sh"
  test -f "gates/${name}-run.sh"
done
test "$(grep -c 'github.token' .github/workflows/office-gate.yml)" = "1"
if grep -q 'environment:' .github/workflows/office-gate.yml; then
  echo "workflow still requires a GitHub Environment" >&2
  exit 1
fi
job_if="$(awk '/^  update:/{f=1} f && /^    if:/{print; exit}' .github/workflows/office-gate.yml)"
test "$job_if" = "    if: inputs.gate == 'update'"
test "$(grep -c 'github.triggering_actor' .github/workflows/office-gate.yml)" = "1"
if grep -q 'GITHUB_SHA' .github/workflows/office-gate.yml; then
  echo "workflow still follows GITHUB_SHA" >&2
  exit 1
fi
pin_file="$(sha256sum SHA256SUMS | awk '{ print $1 }')"
pin_one="$(grep -oE '[0-9a-f]{64}' .github/workflows/office-gate.yml | sort -u)"
test "$(printf '%s\n' "$pin_one" | grep -c .)" = "1"
test "$pin_one" = "$pin_file"
# shellcheck source=gates/update.sh
source gates/update.sh
allow_path "gates/update.sh"
allow_path "gates/p409-run.sh"
if allow_path "gates/../lib.sh"; then echo "allow_path accepted .."; exit 1; fi
if allow_path "/etc/passwd"; then echo "allow_path accepted absolute"; exit 1; fi
if allow_path "gates/nested/x.sh"; then echo "allow_path accepted nest"; exit 1; fi
if allow_path "SHA256SUMS"; then echo "allow_path accepted the index as a member"; exit 1; fi
allow_prefix "PT005/bill/2026-10-08T0850-office-gate-update/repo"
if allow_prefix "PT005/bill/../repo"; then echo "prefix accepted .."; exit 1; fi
if allow_prefix "PT005/hesper/x/repo"; then echo "prefix accepted a non-bill seat"; exit 1; fi
allow_record_path "PT005/hesper/2026-10-08T0459-gpt-consent-office-gate-remote-update.md"
if allow_record_path "PT005/bill/LETTER.md"; then echo "record path accepted Bill"; exit 1; fi
if allow_record_path "PT005/hesper/../x.md"; then echo "record path accepted .."; exit 1; fi
is_commit "1c3d8e243240246e1f9b091e0ac94ed32d7826a0"
if is_commit "1c3d8e2"; then echo "short sha accepted"; exit 1; fi
if is_commit "HEAD"; then echo "HEAD accepted"; exit 1; fi
allow_actor "ChinSookLing"
if allow_actor "hesper[bot]"; then echo "bot actor accepted"; exit 1; fi
if allow_actor ""; then echo "empty actor accepted"; exit 1; fi
if allow_actor "ChinSookLing "; then echo "padded actor accepted"; exit 1; fi
allow_url "$(raw_url 1c3d8e243240246e1f9b091e0ac94ed32d7826a0 PT005/hesper/x.md)"
if allow_url "$(raw_url main PT005/hesper/x.md)"; then echo "branch url accepted"; exit 1; fi
if allow_url "https://example.com/SHA256SUMS"; then echo "other host accepted"; exit 1; fi
rec="$(mktemp)"
printf 'BEGIN LETTER\nFROM: Hesper\nPASS FOR INSTALL\n%s\nEND LETTER\n' "$pin_file" > "$rec"
record_ok "$rec" "$pin_file"
printf 'FROM: Bill\nPASS FOR INSTALL\n%s\n' "$pin_file" > "$rec"
set +e
( record_ok "$rec" "$pin_file" )
rc=$?
set -e
test "$rc" -eq 2
printf 'FROM: Hesper\n%s\n' "$pin_file" > "$rec"
set +e
( record_ok "$rec" "$pin_file" )
rc=$?
set -e
test "$rc" -eq 2
shape="$(mktemp -d)"
mkdir -p "$shape/gates"
printf 'x\n' > "$shape/SHA256SUMS"
printf 'x\n' > "$shape/gates/a.sh"
chmod 0644 "$shape/SHA256SUMS" "$shape/gates/a.sh"
check_tree_shape "$shape"
chmod 4755 "$shape/gates/a.sh"
set +e
( check_tree_shape "$shape" )
rc=$?
set -e
test "$rc" -eq 2
chmod 0644 "$shape/gates/a.sh"
ln -s a.sh "$shape/gates/link.sh"
set +e
( check_tree_shape "$shape" )
rc=$?
set -e
test "$rc" -eq 2
echo "update checks ok"
echo "menu matches"
echo "self-check ok"
