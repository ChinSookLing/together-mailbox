# Shared helpers. No courier key. Do not print the environment.
set +x
set -euo pipefail

MAILBOX_PIN=92c31a73cbcda6e4a00893bf2116aca66c5546b7
MAILBOX_URL=https://github.com/ChinSookLing/together-mailbox.git
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PINS="$ROOT/gates/pins.sha256"
HASH_EARLY=7487a9c5b926ae3310cd9c968e4d9f59e831403140081974f8273c66c8bfc053

note() { printf '%s\n' "$*" | tee -a "${STAGE:?}/NOTE.txt" >/dev/null; }

want_hash() {
  local path="$1" line
  line="$(awk -v p="$path" '$2 == p { print $1; exit }' "$PINS")"
  if [[ -z "$line" ]]; then
    echo "no pin for $path" >&2
    return 1
  fi
  printf '%s\n' "$line"
}

check_hash() {
  local file="$1" path="$2" got want
  want="$(want_hash "$path")"
  got="$(sha256sum "$file" | awk '{ print $1 }')"
  if [[ "$got" != "$want" ]]; then
    printf 'HASH FAIL %s\ngot  %s\nwant %s\n' "$path" "$got" "$want" | tee -a "${STAGE:?}/HASH_FAIL.txt" >/dev/null
    return 1
  fi
  printf '%s  %s\n' "$got" "$path" >> "${STAGE:?}/HASH_OK.txt"
}

fetch_pin() {
  local dest="$1"
  rm -rf "$dest"
  mkdir -p "$dest"
  git init -q "$dest"
  git -C "$dest" remote add origin "$MAILBOX_URL"
  git -C "$dest" fetch -q --depth 1 origin "$MAILBOX_PIN"
  git -C "$dest" checkout -q --detach FETCH_HEAD
  local got
  got="$(git -C "$dest" rev-parse HEAD)"
  if [[ "$got" != "$MAILBOX_PIN" ]]; then
    note "pin checkout is $got not $MAILBOX_PIN"
    return 1
  fi
  printf '%s\n' "$MAILBOX_PIN" > "${STAGE:?}/mailbox_pin.txt"
}

fetch_mailbox_main() {
  local dest="$1"
  rm -rf "$dest"
  mkdir -p "$dest"
  git init -q "$dest"
  git -C "$dest" remote add origin "$MAILBOX_URL"
  git -C "$dest" fetch -q --depth 1 origin main
  git -C "$dest" checkout -q --detach FETCH_HEAD
  git -C "$dest" rev-parse HEAD | tee "${STAGE:?}/mailbox_main.txt" >/dev/null
}

# A read record is not this letter and not an Opus file.
# Path is under PT005/, filename contains "read", body contains the pinned cpp sha256.
find_read_records() {
  local root="$1" file base
  [[ -d "$root/PT005" ]] || return 0
  find "$root/PT005" -type f | while IFS= read -r file; do
    case "$file" in
      "$root"/PT005/bill/*) continue ;;
      "$root"/PT005/opus/*) continue ;;
      *office-gate*) continue ;;
    esac
    base="${file##*/}"
    printf '%s' "$base" | grep -qi 'read' || continue
    grep -q "$HASH_EARLY" "$file" || continue
    printf '%s\n' "${file#"$root"/}"
  done
}

user_bus() {
  local uid sock
  uid="$(id -u)"
  export XDG_RUNTIME_DIR="/run/user/${uid}"
  sock="${XDG_RUNTIME_DIR}/bus"
  export DBUS_SESSION_BUS_ADDRESS="unix:path=${sock}"
  if [[ ! -S "$sock" ]]; then
    note "no user bus at ${sock}. Once, as an admin: sudo loginctl enable-linger $(id -un)"
    return 1
  fi
}

unit_active() {
  local unit="$1"
  user_bus || return 1
  local state
  state="$(systemctl --user is-active "${unit}.service" 2>/dev/null || true)"
  [[ "$state" == "active" || "$state" == "activating" ]]
}

detach() {
  local unit="$1" script_src="$2"
  user_bus || return 1
  install -d "$HOME/.config/systemd/user" "$HOME/office-gate/bin" "$HOME/office-gate/state"
  install -m 0755 "$script_src" "$HOME/office-gate/bin/${unit}.sh"
  cat > "$HOME/.config/systemd/user/${unit}.service" <<EOF
[Unit]
Description=office-gate ${unit}
[Service]
Type=oneshot
Restart=no
WorkingDirectory=${HOME}
ExecStart=${HOME}/office-gate/bin/${unit}.sh
StandardOutput=append:${HOME}/office-gate/state/${unit}.log
StandardError=append:${HOME}/office-gate/state/${unit}.log
EOF
  systemctl --user daemon-reload
  systemctl --user start --no-block "${unit}.service"
  note "started ${unit}.service"
}

copy_out() {
  local src="$1" name="$2"
  if [[ -f "$src" ]]; then
    cp -p "$src" "${STAGE:?}/${name}"
  else
    note "missing ${src}"
  fi
}

shrink_km1() {
  local src="$1" name="$2"
  if [[ ! -f "$src" ]]; then
    note "missing ${src}"
    return 0
  fi
  python3 "$ROOT/gates/km1_extract.py" "$src" "${STAGE:?}/${name}.extract.txt"
}

shrink_tree() {
  local file size list
  list="$(mktemp)"
  find "${STAGE:?}" -type f > "$list"
  while IFS= read -r file; do
    size="$(wc -c < "$file")"
    if [[ "$size" -gt 20000000 ]]; then
      sha256sum "$file" > "${file}.sha256"
      head -n 30 "$file" > "${file}.head"
      rm -f "$file"
      note "large file replaced by sha256 and 30 lines: ${file##*/} (${size} bytes)"
    fi
  done < "$list"
  rm -f "$list"
}
