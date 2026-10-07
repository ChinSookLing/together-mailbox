# The only entry. GATE is a menu name, never a shell command.
set +x
set -euo pipefail
cd "$(dirname "$0")/.."
export STAGE="$(mktemp -d)"
# shellcheck source=gates/lib.sh
source gates/lib.sh
printf 'gate=%s\ncollect_which=%s\nrun_id=%s\n' "${GATE:-}" "${COLLECT_WHICH:-none}" "${RUN_ID:-}" > "$STAGE/menu.txt"

rc=0
case "${GATE:-}" in
  status) bash gates/status.sh || rc=$? ;;
  p233-pack) bash gates/p233-pack.sh || rc=$? ;;
  p191) bash gates/p191.sh || rc=$? ;;
  p241ab) bash gates/p241ab.sh || rc=$? ;;
  p241c) bash gates/p241c.sh || rc=$? ;;
  collect) bash gates/collect.sh || rc=$? ;;
  *) note "unknown gate"; rc=2 ;;
esac
printf '%s\n' "$rc" > "$STAGE/exit_code.txt"
date '+%F %T %Z' > "$STAGE/DATE.txt"
shrink_tree
(
  cd "$STAGE"
  find . -type f ! -name SHA256SUMS | sort | while IFS= read -r file; do
    sha256sum "$file"
  done
) > "$STAGE/SHA256SUMS"
bash gates/publish.sh "$STAGE"
