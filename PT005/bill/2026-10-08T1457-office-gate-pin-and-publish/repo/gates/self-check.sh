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

yml_opts="$(awk '/^          - /{print $2}' .github/workflows/office-gate.yml | head -8 | paste -sd ' ' -)"
case_opts="$(awk '/^    status\)/{f=1} f && /^    [a-z0-9-]+\)/{print $1}' gates/dispatch.sh | tr -d ')' | paste -sd ' ' -)"
test "$yml_opts" = "status p233-pack p191 p241ab p241c p409 collect update"
test "$case_opts" = "status p233-pack p191 p241ab p241c p409 collect update"
test "$(grep -c 'github.token' .github/workflows/office-gate.yml)" = "1"
if grep -q 'environment:' .github/workflows/office-gate.yml; then
  echo "workflow still requires a GitHub Environment" >&2
  exit 1
fi
job_if="$(awk '/^  update:/{f=1} f && /^    if:/{print; exit}' .github/workflows/office-gate.yml)"
test "$job_if" = "    if: inputs.gate == 'update'"
test "$(grep -c 'github.triggering_actor' .github/workflows/office-gate.yml)" = "1"
if grep -q '^          - office-wsl-1$' .github/workflows/office-gate.yml; then
  echo "office-wsl-1 is not a runner label" >&2
  exit 1
fi
test "$(grep -c '^          - office-wsl$' .github/workflows/office-gate.yml)" = "1"
test "$(grep -c '^          - office-wsl-2$' .github/workflows/office-gate.yml)" = "1"
test "$(grep -c '^          - office-wsl-3$' .github/workflows/office-gate.yml)" = "1"
test "$(grep -c '^          - office-wsl-4$' .github/workflows/office-gate.yml)" = "1"
test "$(grep -c 'default: office-wsl$' .github/workflows/office-gate.yml)" = "1"
if grep -q '^  group: office-gate$' .github/workflows/office-gate.yml; then
  echo "concurrency is still one group for every PC" >&2
  exit 1
fi
grep -F 'group: office-gate-${{ inputs.machine }}' .github/workflows/office-gate.yml >/dev/null
test "$(grep -F -c 'runs-on: [self-hosted, "${{ inputs.machine }}"]' .github/workflows/office-gate.yml)" = "2"
test "$(grep -F -c 'MACHINE: ${{ inputs.machine }}' .github/workflows/office-gate.yml)" = "3"
pat='office-wsl|office-wsl-2|office-wsl-3|office-wsl-4'
test "$(grep -c "$pat" gates/lib.sh)" = "1"
test "$(grep -c "$pat" gates/update.sh)" = "1"
test "$(grep -c "$pat" gates/publish.sh)" = "1"
grep -F 'allow_machine "${MACHINE:-}"' gates/dispatch.sh >/dev/null
grep -F 'results/${MACHINE}/${GATE}/${RUN_ID}' gates/publish.sh >/dev/null
if grep -F 'dest="results/${GATE}/${RUN_ID}"' gates/publish.sh >/dev/null; then
  echo "publish path can still collide" >&2
  exit 1
fi
grep -F 'x-access-token:%s' gates/publish.sh >/dev/null
grep -F 'AUTHORIZATION: basic ${basic}' gates/publish.sh >/dev/null
allow_machine "office-wsl"
allow_machine "office-wsl-2"
if allow_machine "office-wsl-1"; then echo "allow_machine accepted office-wsl-1"; exit 1; fi
if allow_machine ""; then echo "allow_machine accepted empty"; exit 1; fi
if allow_machine "office-wsl "; then echo "allow_machine accepted padding"; exit 1; fi
test "$(pinned_user office-wsl gates/machines.txt)" = "gigabyte"
user_is_pinned office-wsl gates/machines.txt gigabyte
if user_is_pinned office-wsl gates/machines.txt alice; then echo "wrong user accepted"; exit 1; fi
if user_is_pinned office-wsl-2 gates/machines.txt gigabyte; then echo "unpinned machine accepted"; exit 1; fi
dup="$(mktemp)"
printf 'office-wsl gigabyte\noffice-wsl alice\n' > "$dup"
if pinned_user office-wsl "$dup"; then echo "duplicate label accepted"; exit 1; fi
printf 'office-wsl gigabyte extra\n' > "$dup"
if pinned_user office-wsl "$dup"; then echo "extra field accepted"; exit 1; fi
printf 'office-wsl Gigabyte\n' > "$dup"
if pinned_user office-wsl "$dup"; then echo "capital user accepted"; exit 1; fi
rm -f "$dup"
user_line="$(grep -n 'user_is_pinned' gates/dispatch.sh | head -1 | cut -d: -f1)"
case_line="$(grep -n 'status)' gates/dispatch.sh | head -1 | cut -d: -f1)"
test "$user_line" -lt "$case_line"
test "$(grep -c 'attempt=1' gates/publish.sh)" = "1"
test "$(grep -c '\[\[ "$attempt" -le 5 \]\]' gates/publish.sh)" = "1"
grep -F 'fetch -q --depth 1 origin results' gates/publish.sh >/dev/null
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
test "$(machine_user office-wsl gates/machines.txt)" = "gigabyte"
if machine_user office-wsl-2 gates/machines.txt; then echo "unpinned machine has a user"; exit 1; fi
if machine_user office-wsl-1 gates/machines.txt; then echo "office-wsl-1 has a user"; exit 1; fi
dup="$(mktemp)"
printf 'office-wsl gigabyte\noffice-wsl alice\n' > "$dup"
if machine_user office-wsl "$dup"; then echo "update accepted a duplicate label"; exit 1; fi
rm -f "$dup"
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
home="$(mktemp -d)"
set +e
HOME="$home" GATE=status COLLECT_WHICH=none RUN_ID=42 MACHINE=office-wsl-2 bash gates/dispatch.sh
rc=$?
set -e
test "$rc" -eq 2
stage="$(cat "$home/office-gate/state/stage-42.path")"
grep -q 'not pinned' "$stage/NOTE.txt"
test ! -f "$stage/host.txt"
bare="$(mktemp -d)"
git init -q --bare "$bare"
seed="$(mktemp -d)"
git init -q -b results "$seed"
echo seed > "$seed/marker"
git -C "$seed" add marker
git -C "$seed" -c user.email=t@local -c user.name=t commit -q -m seed
git -C "$seed" remote add origin "$bare"
git -C "$seed" push -q origin HEAD:results
a="$(mktemp -d)"
b="$(mktemp -d)"
git clone -q --branch results "$bare" "$a"
git clone -q --branch results "$bare" "$b"
echo A > "$a/from-a"
echo B > "$b/from-b"
git -C "$a" add from-a
git -C "$b" add from-b
git -C "$a" -c user.email=t@local -c user.name=t commit -q -m a
git -C "$b" -c user.email=t@local -c user.name=t commit -q -m b
git -C "$a" push -q origin HEAD:results
set +e
git -C "$b" push -q origin HEAD:results
prc=$?
set -e
test "$prc" -ne 0
git -C "$b" fetch -q origin results
git -C "$b" reset -q --hard FETCH_HEAD
echo B > "$b/from-b"
git -C "$b" add from-b
git -C "$b" -c user.email=t@local -c user.name=t commit -q -m b2
git -C "$b" push -q origin HEAD:results
final="$(mktemp -d)"
git clone -q --branch results "$bare" "$final"
test "$(cat "$final/from-a")" = "A"
test "$(cat "$final/from-b")" = "B"
echo "publish retry shape ok"
echo "menu matches"
echo "self-check ok"
