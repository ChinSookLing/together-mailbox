# Menu only. No write token and no publish. GATE is a menu name, never a command.
set +x
set -euo pipefail
cd "$(dirname "$0")/.."
export STAGE="$(mktemp -d)"
# shellcheck source=gates/lib.sh
source gates/lib.sh
printf 'gate=%s\ncollect_which=%s\nrun_id=%s\n' "${GATE:-}" "${COLLECT_WHICH:-none}" "${RUN_ID:-}" > "$STAGE/menu.txt"

rc=0
if python3 - << 'PY'
import os, sys
names = ("GITHUB_TOKEN", "GH_TOKEN", "RESULT_TOKEN", "ACTIONS_RUNTIME_TOKEN")
bad = [k for k in names if os.environ.get(k)]
bad += [k for k, v in os.environ.items() if v.startswith(("ghs_", "github_pat_"))]
if bad:
    print("refusing: token visible in the menu step:", " ".join(sorted(set(bad))))
    sys.exit(3)
PY
then
  case "${GATE:-}" in
    status) bash gates/status.sh || rc=$? ;;
    p233-pack) bash gates/p233-pack.sh || rc=$? ;;
    p191) bash gates/p191.sh || rc=$? ;;
    p241ab) bash gates/p241ab.sh || rc=$? ;;
    p241c) bash gates/p241c.sh || rc=$? ;;
    p409) bash gates/p409.sh || rc=$? ;;
    p383) bash gates/p383.sh || rc=$? ;;
    p307) bash gates/p307.sh || rc=$? ;;
    p337) bash gates/p337.sh || rc=$? ;;
    collect) bash gates/collect.sh || rc=$? ;;
    update) note "update is a separate job. This menu does not swap the tree."; rc=2 ;;
    *) note "unknown gate"; rc=2 ;;
  esac
else
  note "REFUSED. A write token was visible in the menu step. Nothing ran."
  rc=3
fi
unset GITHUB_TOKEN GH_TOKEN RESULT_TOKEN ACTIONS_RUNTIME_TOKEN || true
printf '%s\n' "$rc" > "$STAGE/exit_code.txt"
date '+%F %T %Z' > "$STAGE/DATE.txt"
shrink_tree
(
  cd "$STAGE"
  find . -type f ! -name SHA256SUMS | sort | while IFS= read -r file; do
    sha256sum "$file"
  done
) > "$STAGE/SHA256SUMS"
install -d "${HOME}/office-gate/state"
printf '%s\n' "$STAGE" > "${HOME}/office-gate/state/stage-${RUN_ID:?}.path"
exit "$rc"
