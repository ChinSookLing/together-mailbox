# Remote tree swap only. Never starts a math gate.
# The workflow job calls this. The menu does not.
# A hand bootstrap installs this file the first time. It does not skip the record.
set +x
set -euo pipefail

refuse() {
  printf '%s\n' "$*" >&2
  exit 2
}

is_commit() { [[ "$1" =~ ^[0-9a-f]{40}$ ]]; }
is_sha256() { [[ "$1" =~ ^[0-9a-f]{64}$ ]]; }

allow_actor() { [[ "$1" == "ChinSookLing" ]]; }

# SHA256SUMS is the index. Inside it, only gates/<one name>.
allow_path() {
  local path="$1" name
  case "$path" in
    *..*|/*|.*|*' '*) return 1 ;;
    gates/*/*) return 1 ;;
    gates/*) ;;
    *) return 1 ;;
  esac
  name="${path#gates/}"
  [[ "$name" =~ ^[A-Za-z0-9._-]+$ ]] || return 1
  [[ "$name" != .* ]] || return 1
  return 0
}

allow_prefix() {
  [[ "$1" != *..* ]] || return 1
  [[ "$1" =~ ^PT005/bill/[A-Za-z0-9][A-Za-z0-9._-]*/repo$ ]]
}

allow_record_path() {
  local path="$1" seat
  [[ "$path" != *..* ]] || return 1
  [[ "$path" =~ ^PT005/[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*$ ]] || return 1
  seat="${path#PT005/}"
  seat="${seat%%/*}"
  [[ "$seat" != "bill" ]] || return 1
  return 0
}

raw_url() {
  printf 'https://raw.githubusercontent.com/ChinSookLing/together-mailbox/%s/%s\n' "$1" "$2"
}

allow_url() {
  case "$1" in
    https://raw.githubusercontent.com/ChinSookLing/together-mailbox/[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]/*) return 0 ;;
    *) return 1 ;;
  esac
}

fetch_file() {
  local url="$1" dest="$2"
  allow_url "$url" || refuse "refusing url"
  curl -fsSL --proto '=https' --proto-redir '=https' --max-time 60 --output "$dest" "$url"
}

check_tree_shape() {
  local root="$1" path mode list
  list="$(mktemp)"
  ( cd "$root" && find . -mindepth 1 -printf '%P\n' | sort ) > "$list"
  while IFS= read -r path; do
    [[ -n "$path" ]] || continue
    if [[ -L "$root/$path" ]]; then
      rm -f "$list"
      refuse "symlink refused: $path"
    fi
    if [[ "$path" != "SHA256SUMS" && "$path" != "gates" ]]; then
      if ! allow_path "$path"; then
        rm -f "$list"
        refuse "path not on the allowlist: $path"
      fi
    fi
    mode="$(stat -c '%a' "$root/$path")"
    case "$mode" in
      *[!0-7]*) rm -f "$list"; refuse "odd mode refused: $path" ;;
    esac
    if (( (8#$mode & 06000) != 0 )); then
      rm -f "$list"
      refuse "setuid or setgid refused: $path"
    fi
    if [[ "$(stat -c '%U' "$root/$path")" != "$(id -un)" ]]; then
      rm -f "$list"
      refuse "file owner is not the runner: $path"
    fi
  done < "$list"
  rm -f "$list"
}

record_ok() {
  local file="$1" sums_hash="$2" first
  grep -q 'PASS FOR INSTALL' "$file" || refuse "record has no PASS FOR INSTALL"
  grep -q "$sums_hash" "$file" || refuse "record does not name the tree SHA256SUMS hash"
  first="$(awk '/^FROM:/ { print; exit }' "$file")"
  [[ -n "$first" ]] || refuse "record has no FROM line"
  if [[ "$first" == "FROM: Bill" || "$first" == "FROM: Bill "* ]]; then
    refuse "record is written by Bill"
  fi
  return 0
}

main_update() {
  local tree_commit="${TREE_COMMIT:-}"
  local tree_prefix="${TREE_PREFIX:-}"
  local record_commit="${READ_RECORD_COMMIT:-}"
  local record_path="${READ_RECORD_PATH:-}"
  local record_sha="${READ_RECORD_SHA256:-}"
  local expected="${EXPECTED_PIN:-}"
  local live="${HOME}/office-gate/dispatcher"
  local sums="$live/SHA256SUMS"
  local got stamp work url line path dest
  local incoming newdir backup uid state

  allow_actor "${TRIGGERING_ACTOR:-}" || refuse "refusing actor ${TRIGGERING_ACTOR:-empty}"
  [[ "$(id -u)" -ne 0 ]] || refuse "refusing root"
  [[ "$(id -un)" == "gigabyte" ]] || refuse "runner user is not gigabyte"

  is_commit "$tree_commit" || refuse "tree_commit is not 40 hex"
  is_commit "$record_commit" || refuse "read_record_commit is not 40 hex"
  is_sha256 "$record_sha" || refuse "read_record_sha256 is not 64 hex"
  is_sha256 "$expected" || refuse "expected pin is not 64 hex"
  allow_prefix "$tree_prefix" || refuse "tree_prefix is not PT005/bill/<folder>/repo"
  allow_record_path "$record_path" || refuse "read record path is not a non-Bill seat letter"

  [[ -f "$sums" ]] || refuse "no installed SHA256SUMS"
  ( cd "$live" && sha256sum -c SHA256SUMS ) || refuse "installed tree failed its own SHA256SUMS"
  got="$(sha256sum "$sums" | awk '{ print $1 }')"
  [[ "$got" == "$expected" ]] || refuse "installed SHA256SUMS is not the workflow pin"

  uid="$(id -u)"
  if [[ -S "/run/user/${uid}/bus" ]]; then
    export XDG_RUNTIME_DIR="/run/user/${uid}"
    export DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"
    for unit in office-gate-p191 office-gate-p241ab office-gate-p241c office-gate-p409; do
      state="$(systemctl --user is-active "${unit}.service" 2>/dev/null || true)"
      if [[ "$state" == "active" || "$state" == "activating" ]]; then
        refuse "refusing swap while ${unit} is ${state}"
      fi
    done
  fi

  stamp="$(date -u +%Y%m%dT%H%M%SZ)"
  work="${HOME}/office-gate/incoming.${stamp}"
  [[ ! -e "$work" ]] || refuse "incoming dir already exists"
  install -d -m 0755 "$work/gates"

  url="$(raw_url "$tree_commit" "${tree_prefix}/SHA256SUMS")"
  fetch_file "$url" "$work/SHA256SUMS"
  chmod 0644 "$work/SHA256SUMS"

  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" || "$line" == \#* ]] && continue
    path="${line#*  }"
    [[ "$line" == *"  ${path}" ]] || refuse "SHA256SUMS line is not two-space form"
    allow_path "$path" || refuse "SHA256SUMS names a path that is not allowed: $path"
    dest="$work/$path"
    install -d -m 0755 "$(dirname "$dest")"
    url="$(raw_url "$tree_commit" "${tree_prefix}/${path}")"
    fetch_file "$url" "$dest"
    chmod 0644 "$dest"
  done < "$work/SHA256SUMS"

  ( cd "$work" && sha256sum -c SHA256SUMS ) || refuse "incoming tree failed SHA256SUMS"
  check_tree_shape "$work"
  incoming="$(sha256sum "$work/SHA256SUMS" | awk '{ print $1 }')"
  [[ "$incoming" != "$got" ]] || refuse "incoming tree is the tree already installed"

  url="$(raw_url "$record_commit" "$record_path")"
  fetch_file "$url" "$work/READ_RECORD"
  got="$(sha256sum "$work/READ_RECORD" | awk '{ print $1 }')"
  [[ "$got" == "$record_sha" ]] || refuse "read record sha256 does not match"
  record_ok "$work/READ_RECORD" "$incoming"
  rm -f "$work/READ_RECORD"
  ( cd "$work" && sha256sum -c SHA256SUMS ) || refuse "incoming tree changed after the record check"

  newdir="${HOME}/office-gate/dispatcher.new"
  if [[ -e "$newdir" ]]; then
    mv "$newdir" "${HOME}/office-gate/dispatcher.new.abandoned.${stamp}"
  fi
  mv "$work" "$newdir"

  backup="${HOME}/office-gate/dispatcher.bak.${stamp}.${tree_commit}"
  if ! mv "$live" "$backup"; then
    refuse "could not move the live tree aside; dispatcher.new is left in place"
  fi
  if ! mv "$newdir" "$live"; then
    mv "$backup" "$live" || true
    refuse "rename onto dispatcher failed; previous tree restored if the move back succeeded"
  fi
  if ! ( cd "$live" && sha256sum -c SHA256SUMS ); then
    mv "$live" "${HOME}/office-gate/dispatcher.bak.failed.${stamp}"
    mv "$backup" "$live"
    refuse "post-swap check failed; previous tree restored"
  fi

  install -d -m 0755 "${HOME}/office-gate/state"
  {
    printf 'date %s\n' "$(date -u '+%F %T UTC')"
    printf 'user %s\n' "$(id -un)"
    printf 'old_pin %s\n' "$expected"
    printf 'new_pin %s\n' "$incoming"
    printf 'tree_commit %s\n' "$tree_commit"
    printf 'tree_prefix %s\n' "$tree_prefix"
    printf 'read_record_commit %s\n' "$record_commit"
    printf 'read_record_path %s\n' "$record_path"
    printf 'read_record_sha256 %s\n' "$record_sha"
    printf 'backup %s\n' "$backup"
  } | tee "${HOME}/office-gate/state/update-receipt.txt" | tee "${HOME}/office-gate/state/update-receipt.${stamp}.txt"
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
  main_update
fi
