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

yml_opts="$(awk '/^          - /{print $2}' .github/workflows/office-gate.yml | head -23 | paste -sd ' ' -)"
case_opts="$(awk '/^    status\)/{f=1} f && /^    [a-z0-9-]+\)/{print $1}' gates/dispatch.sh | tr -d ')' | paste -sd ' ' -)"
test "$yml_opts" = "status p233-pack p191 p241ab p241c p409 p383 p307 p337 p397 p431 p443 p463 p461 p439 p433 p449 p479 p467 p487 prime collect update"
test "$case_opts" = "status p233-pack p191 p241ab p241c p409 p383 p307 p337 p397 p431 p443 p463 p461 p439 p433 p449 p479 p467 p487 prime collect update"
for name in p383 p307 p337 p397 p431 p443 p463 p461 p439 p433 p449 p479 p467 p487; do
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
for f in gates/p191.sh gates/p241ab.sh gates/p241c.sh gates/p409.sh gates/p383.sh gates/p307.sh gates/p337.sh gates/p397.sh gates/p431.sh gates/p443.sh gates/p463.sh gates/p461.sh gates/p439.sh gates/p433.sh gates/p449.sh gates/p479.sh gates/p467.sh gates/p487.sh; do
  grep -q 'math_menu_lock' "$f"
  grep -q 'math_menu_detach' "$f"
  if grep -E -q '^detach office-gate-' "$f"; then
    echo "raw detach remains in ${f}" >&2
    exit 1
  fi
done
for f in gates/p191-run.sh gates/p241ab-run.sh gates/p241c-run.sh gates/p409-run.sh gates/p383-run.sh gates/p307-run.sh gates/p337-run.sh gates/p397-run.sh gates/p431-run.sh gates/p443-run.sh gates/p463-run.sh gates/p461-run.sh gates/p439-run.sh gates/p433-run.sh gates/p449-run.sh gates/p479-run.sh gates/p467-run.sh gates/p487-run.sh; do
  grep -q 'math_run_lock' "$f"
  grep -q 'math_run_ready' "$f"
done
for f in gates/p383-run.sh gates/p307-run.sh gates/p337-run.sh gates/p397-run.sh gates/p431-run.sh gates/p443-run.sh gates/p463-run.sh gates/p461-run.sh gates/p439-run.sh gates/p433-run.sh gates/p449-run.sh gates/p479-run.sh gates/p467-run.sh gates/p487-run.sh; do
  sum_line="$(grep -n 'sha256sum -c' "$f" | head -1 | cut -d: -f1)"
  ready_line="$(grep -n 'math_run_ready' "$f" | head -1 | cut -d: -f1)"
  test "$sum_line" -lt "$ready_line"
done
lockhome="$(mktemp -d)"
mkdir -p "$lockhome/stage" "$lockhome/kit" "$lockhome/office-gate/state"
cat > "$lockhome/run.sh" << EOF
set +x
set -euo pipefail
source "$(pwd)/gates/lib.sh"
math_run_lock
math_run_ready
printf '%s\n' ran >> "\$HOME/ran.txt"
while [[ ! -f "\$HOME/stop" ]]; do
  sleep 0.1
done
EOF
run_menu() {
  local id="$1" status=0
  (
    set +x
    set -euo pipefail
    export HOME="$lockhome"
    export STAGE="$lockhome/stage"
    export MATH_LOCK_TEST=1
    detach() { /bin/bash "$2" >>"$HOME/run.log" 2>&1 8>&- 9>&- & }
    math_menu_lock
    math_menu_detach office-gate-test "$lockhome/run.sh"
  ) >"$lockhome/log-${id}.txt" 2>&1 || status=$?
  printf '%s\n' "$status" > "$lockhome/code-${id}"
}
run_menu a &
run_menu b &
wait
sort "$lockhome/code-a" "$lockhome/code-b" > "$lockhome/codes"
printf '0\n2\n' > "$lockhome/want"
if ! cmp -s "$lockhome/codes" "$lockhome/want"; then
  echo "two menus were not one success and one refusal" >&2
  echo "codes $(paste -sd ' ' "$lockhome/codes")" >&2
  echo "log a" >&2; cat "$lockhome/log-a.txt" >&2 || true
  echo "log b" >&2; cat "$lockhome/log-b.txt" >&2 || true
  echo "run log" >&2; cat "$lockhome/run.log" >&2 || true
  exit 1
fi
test "$(wc -l < "$lockhome/ran.txt")" = "1"
run_menu c
test "$(cat "$lockhome/code-c")" = "2"
test "$(wc -l < "$lockhome/ran.txt")" = "1"
held="$(tr -cd '0-9' < "$lockhome/kit/math-lock.holder")"
printf '%s\n' stop > "$lockhome/stop"
for ((n=0; n<50; n++)); do
  if [[ ! -d "/proc/${held}" ]]; then
    break
  fi
  sleep 0.1
done
if [[ -d "/proc/${held}" ]]; then
  echo "holder did not exit" >&2
  exit 1
fi
rm -f "$lockhome/stop"
run_menu d
test "$(cat "$lockhome/code-d")" = "0"
test "$(wc -l < "$lockhome/ran.txt")" = "2"
printf '%s\n' stop > "$lockhome/stop"
echo "math lock excludes a second menu"
test ! -e "$lockhome/kit/math-lock.stopped"
confirm="$(mktemp -d)"
mkdir -p "$confirm/stage" "$confirm/kit" "$confirm/office-gate/state"
cat > "$confirm/hold.sh" << EOF
set +x
set -euo pipefail
source "$(pwd)/gates/lib.sh"
math_run_lock
math_run_ready
while [[ ! -f "\$HOME/stop" ]]; do
  sleep 0.1
done
EOF
hold_rc=0
(
  set -euo pipefail
  export HOME="$confirm"
  export STAGE="$confirm/stage"
  export MATH_LOCK_TEST=1
  export MATH_LOCK_POLLS=0
  detach() {
    /bin/bash "$2" >>"$HOME/run.log" 2>&1 8>&- 9>&- &
    local n
    for ((n=0; n<50; n++)); do
      [[ -s "$HOME/kit/math-lock.holder" ]] && return 0
      sleep 0.05
    done
    return 1
  }
  math_menu_lock
  math_menu_detach office-gate-test "$confirm/hold.sh"
) >"$confirm/hold-menu.txt" 2>&1 || hold_rc=$?
printf '%s\n' "$hold_rc" > "$confirm/hold.code"
if [[ "$hold_rc" != "0" ]]; then
  echo "holder confirmation failed" >&2
  cat "$confirm/hold-menu.txt" >&2 || true
  cat "$confirm/run.log" >&2 || true
  exit 1
fi
test ! -e "$confirm/kit/math-lock.stopped"
printf '%s\n' stop > "$confirm/stop"
held="$(tr -cd '0-9' < "$confirm/kit/math-lock.holder")"
for ((n=0; n<50; n++)); do
  [[ ! -d "/proc/${held}" ]] && break
  sleep 0.1
done
miss="$(mktemp -d)"
mkdir -p "$miss/stage" "$miss/kit" "$miss/office-gate/state"
miss_rc=0
(
  set -euo pipefail
  export HOME="$miss"
  export STAGE="$miss/stage"
  export MATH_LOCK_POLLS=0
  export MATH_LOCK_CANCEL_POLLS=2
  detach() { return 0; }
  math_menu_lock
  math_menu_detach office-gate-test "$miss/none.sh"
) >"$miss/menu.txt" 2>&1 || miss_rc=$?
printf '%s\n' "$miss_rc" > "$miss/code"
test "$miss_rc" = "2"
test ! -e "$miss/kit/math-lock.stopped"
cancel="$(echo "$miss"/kit/math-cancel-*)"
test -s "$cancel"
gen="${cancel##*/math-cancel-}"
late_rc=0
(
  set -euo pipefail
  export HOME="$miss"
  export OFFICE_GATE_LOCK_GEN="$gen"
  source "$(pwd)/gates/lib.sh"
  math_run_lock
  printf '%s\n' ran >> "$HOME/ran.txt"
) >"$miss/late.txt" 2>&1 || late_rc=$?
test "$late_rc" = "2"
test ! -e "$miss/ran.txt"
test -s "$miss/kit/math-lock.refused"
slow="$(mktemp -d)"
mkdir -p "$slow/stage" "$slow/kit" "$slow/office-gate/state"
cat > "$slow/slow.sh" << EOF
set +x
set -euo pipefail
source "$(pwd)/gates/lib.sh"
while [[ ! -f "\$HOME/child-go" ]]; do
  sleep 0.05
done
math_run_lock
math_run_ready
printf '%s\n' ran >> "\$HOME/ran.txt"
EOF
slow_rc=0
(
  set -euo pipefail
  export HOME="$slow"
  export STAGE="$slow/stage"
  export MATH_LOCK_POLLS=0
  export MATH_LOCK_CANCEL_POLLS=40
  detach() {
    /bin/bash "$2" >>"$HOME/run.log" 2>&1 8>&- 9>&- &
    (
      local n
      for ((n=0; n<80; n++)); do
        [[ -f "$HOME/kit/math-cancel-${OFFICE_GATE_LOCK_GEN}" ]] && break
        sleep 0.05
      done
      printf '%s\n' go > "$HOME/child-go"
    ) &
  }
  math_menu_lock
  math_menu_detach office-gate-slow "$slow/slow.sh"
) >"$slow/menu.txt" 2>&1 || slow_rc=$?
printf '%s\n' "$slow_rc" > "$slow/code"
if [[ "$slow_rc" != "2" ]]; then
  echo "slow start was not a refusal" >&2
  cat "$slow/menu.txt" >&2 || true
  cat "$slow/run.log" >&2 || true
  exit 1
fi
test ! -e "$slow/ran.txt"
test ! -e "$slow/kit/math-lock.stopped"
test -s "$slow/kit/math-lock.refused"
echo "timeout does not stop a lock holder"

# ---- Prime door (chair note 122). Dry runs: no systemd, no kcascade.
test "$(cat gates/primes.txt)" = "$(printf '491\n499\n503\n509\n521\n523')"
test "$(grep -cvE '^[1-9][0-9]{2,3}$' gates/primes.txt || true)" = "0"
test "$(sort gates/primes.txt | uniq -d | grep -c . || true)" = "0"
grep -q '          - prime' .github/workflows/office-gate.yml
grep -q 'PRIME: ${{ inputs.prime }}' .github/workflows/office-gate.yml
grep -q 'TICKET: ${{ inputs.ticket }}' .github/workflows/office-gate.yml
grep -q '|prime|' gates/publish.sh
n_inputs="$(awk '/^    inputs:/{f=1; next} f && /^[a-z]/{f=0} f && /^      [a-z_]+:$/{n++} END{print n}' .github/workflows/office-gate.yml)"
test "$n_inputs" -le 10
for x in 491 499 503 509 521 523; do prime_on_list "$x"; done
for x in 487 467 2 1000 "491 " " 491" "491;id" "0491" "" "49" "4910" "\$(id)"; do
  if prime_on_list "$x"; then echo "prime_on_list accepted [$x]"; exit 1; fi
done
test "$(office_units | grep -c .)" = "24"
grep -qx office-gate-p523 <<< "$(office_units)"
grep -qx office-gate-p487 <<< "$(office_units)"
door() {
  local home="$1" prime="$2" rc=0
  ( export HOME="$home" STAGE="$home/stage" PRIME="$prime"
    unit_active() { return 1; }
    math_menu_lock() { echo "reached math lock" > "$HOME/reached"; exit 7; }
    source gates/lib.sh
    unit_active() { return 1; }
    math_menu_lock() { echo "reached math lock" > "$HOME/reached"; exit 7; }
    P="${PRIME:-}"
    # run the door body up to the math lock
    eval "$(sed -n '/^P=/,/^math_menu_lock$/p' gates/prime.sh)"
  ) >/dev/null 2>&1 || rc=$?
  printf '%s\n' "$rc"
}
dh="$(mktemp -d)"; mkdir -p "$dh/stage" "$dh/office-gate/state"
test "$(door "$dh" 487)" = "2"; grep -q 'not on gates/primes.txt' "$dh/stage/NOTE.txt"
test "$(door "$dh" 'x')" = "2"
test "$(door "$dh" 499)" = "2"; grep -q 'p491 comes first' "$dh/stage/NOTE.txt"
test "$(door "$dh" 491)" = "7"
date > "$dh/office-gate/state/p491.done"
test "$(door "$dh" 491)" = "2"; grep -q 'p491 is already done' "$dh/stage/NOTE.txt"
test "$(door "$dh" 499)" = "7"
echo MISMATCH > "$dh/office-gate/state/p499.mismatch"
test "$(door "$dh" 499)" = "2"; grep -q 'mismatch' "$dh/stage/NOTE.txt"
test "$(door "$dh" 503)" = "2"
echo "prime door refuses off-list, done, mismatch and out-of-order primes"
grep -q 'export OFFICE_GATE_PRIME="$P"' gates/prime.sh
grep -q 'math_menu_detach "office-gate-p${P}" "$ROOT/gates/prime-run.sh"' gates/prime.sh
grep -q 'kcascade_run.py" ./bgk15 ./cascade_k15p "$P" 8 "$OUTD"' gates/prime-run.sh
test "$(grep -c 'cascade_k15p "$P" 8 ' gates/prime-run.sh)" = "2"
grep -q 'math_run_lock' gates/prime-run.sh
sum_line="$(grep -n 'sha256sum -c' gates/prime-run.sh | head -1 | cut -d: -f1)"
ready_line="$(grep -n 'math_run_ready' gates/prime-run.sh | head -1 | cut -d: -f1)"
test "$sum_line" -lt "$ready_line"
# Unit text: old doors unchanged, prime units low priority.
u_old="$( unset OFFICE_GATE_PRIME; OFFICE_GATE_LOCK_GEN=g unit_text office-gate-p487 /x/p487-run.sh )"
if grep -qE 'Nice|CPU|IOSched|OFFICE_GATE_PRIME' <<< "$u_old"; then echo "old unit text changed"; exit 1; fi
u_new="$( OFFICE_GATE_PRIME=491 OFFICE_GATE_LOCK_GEN=g unit_text office-gate-p491 /x/prime-run.sh )"
for l in 'Environment=OFFICE_GATE_PRIME=491' 'Nice=19' 'CPUSchedulingPolicy=idle' 'CPUWeight=idle' 'IOSchedulingClass=idle' 'Environment=OFFICE_GATE_LOCK_GEN=g'; do
  grep -qx -- "$l" <<< "$u_new"
done
if ( OFFICE_GATE_PRIME=487 unit_text office-gate-p487 /x >/dev/null ); then echo "unit_text took an off-list prime"; exit 1; fi
echo "unit text ok"
# Close-out verdict.
vd="$(mktemp -d)"
mk() { : > "$vd/ir"; local r s; for s in "$@"; do printf '{"r": 1, "s": %s, "rows": 0}\n' "$s" >> "$vd/ir"; done; }
printf 'ir jobs 3 done 0 todo 3\n' > "$vd/log"
mk 1 2 3;   [[ "$(prime_verdict 0 "$vd/log" "$vd/ir")" == DONE* ]]
mk 1 2;     [[ "$(prime_verdict 0 "$vd/log" "$vd/ir")" == UNFINISHED* ]]
mk 1 2 3;   [[ "$(prime_verdict 1 "$vd/log" "$vd/ir")" == UNFINISHED* ]]
mk 1 2 2;   [[ "$(prime_verdict 0 "$vd/log" "$vd/ir")" == MISMATCH* ]]
mk 1 2 3 4; [[ "$(prime_verdict 0 "$vd/log" "$vd/ir")" == MISMATCH* ]]
printf 'ir jobs 3 done 0 todo 3\nir jobs 4 done 3 todo 1\n' > "$vd/log"
mk 1 2 3;   [[ "$(prime_verdict 0 "$vd/log" "$vd/ir")" == MISMATCH* ]]
: > "$vd/log"
[[ "$(prime_verdict 0 "$vd/log" "$vd/ir")" == UNFINISHED* ]]
printf 'ir jobs 0 done 0 todo 0\n' > "$vd/log"; : > "$vd/ir"
[[ "$(prime_verdict 0 "$vd/log" "$vd/ir")" == UNFINISHED* ]]
echo "verdict ok"
# One-line ticket (note 122 B).
tk="$(mktemp -d)"
C40=1c3d8e243240246e1f9b091e0ac94ed32d7826a0
S64=e71080598f0cec1166347abce64973f544ee5c8340c74f1d4e2fdf5174fb9b59
good() { printf 'tree_commit %s\ntree_prefix PT005/bill/F1/repo\nread_record_commit %s\nread_record_path PT005/puck/r.md\nread_record_sha256 %s\nnew_pin %s\n' "$C40" "$C40" "$S64" "$S64"; }
good > "$tk/t"; ( parse_ticket "$tk/t" ) > "$tk/out"
test "$(grep -c . "$tk/out")" = "6"
grep -qx "tree_prefix PT005/bill/F1/repo" "$tk/out"
tbad() { local rc=0; ( parse_ticket "$tk/b" ) >/dev/null 2>&1 || rc=$?; test "$rc" = "2"; }
{ good; printf 'new_pin %s\n' "$S64"; } > "$tk/b"; tbad
{ good; printf 'extra x\n'; } > "$tk/b"; tbad
good | grep -v '^new_pin' > "$tk/b"; tbad
good | sed 's/^tree_prefix /tree_prefix  /' > "$tk/b"; tbad
good | sed 's/^read_record_path .*/read_record_path a b/' > "$tk/b"; tbad
allow_ticket_path "PT005/bill/F1/TICKET.txt"
if allow_ticket_path "PT005/hesper/F1/TICKET.txt"; then echo "ticket path accepted a non-bill seat"; exit 1; fi
if allow_ticket_path "PT005/bill/../TICKET.txt"; then echo "ticket path accepted .."; exit 1; fi
if allow_ticket_path "PT005/bill/F1/repo/TICKET.txt"; then echo "ticket path accepted a nested file"; exit 1; fi
rc=0
( TICKET="$C40:PT005/bill/F1/TICKET.txt" TREE_COMMIT="$C40" TRIGGERING_ACTOR=ChinSookLing main_update ) >/dev/null 2>&1 || rc=$?
test "$rc" = "2"
rc=0
( TICKET="$C40:PT005/bill/F1/TICKET.txt" TRIGGERING_ACTOR=hesper main_update ) >/dev/null 2>&1 || rc=$?
test "$rc" = "2"
grep -q 'ticket new_pin is not the incoming SHA256SUMS hash' gates/update.sh
grep -q 'record does not name the ticket tree_commit' gates/update.sh
grep -q 'ticket folder is not the tree folder' gates/update.sh
echo "ticket checks ok"
echo "self-check ok"
