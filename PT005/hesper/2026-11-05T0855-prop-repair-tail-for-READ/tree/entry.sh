# Fixed menu. Called by the workflow after the hash check.
set +x
set -euo pipefail
OUT="/tmp/k11-out/${RUN_ID}"; install -d "$OUT"; export OUT
source "$(dirname "$0")/lib.sh"
printf '%s\n' "$GATE" > "$OUT/menu.txt"
date '+%F %T %Z' > "$OUT/DATE.txt"
case "$GATE" in
  status)     bash "${D}/gates/status.sh" ;;
  checkpoint) bash "${D}/gates/checkpoint.sh" ;;
  selftest)   start_job selftest; bash "${D}/gates/status.sh" ;;
  k11-p383a)  start_job k11-p383a; bash "${D}/gates/status.sh" ;;
  k11-p397a)  start_job k11-p397a; bash "${D}/gates/status.sh" ;;
  k11-p431a)  start_job k11-p431a; bash "${D}/gates/status.sh" ;;
  k11-p443a)  start_job k11-p443a; bash "${D}/gates/status.sh" ;;
  k11-p463a)  start_job k11-p463a; bash "${D}/gates/status.sh" ;;
  k11-p461a)  start_job k11-p461a; bash "${D}/gates/status.sh" ;;
  k11-p439a)  start_job k11-p439a; bash "${D}/gates/status.sh" ;;
  k11-p449a)  start_job k11-p449a; bash "${D}/gates/status.sh" ;;
  k11-p433a)  start_job k11-p433a; bash "${D}/gates/status.sh" ;;
  k11-p467a)  start_job k11-p467a; bash "${D}/gates/status.sh" ;;
  k11-p479a)  start_job k11-p479a; bash "${D}/gates/status.sh" ;;
  close-k11-p479a) bash "${D}/gates/close-k11-p479a.sh"; bash "${D}/gates/status.sh" ;;
  k11-p487a)  start_job k11-p487a; bash "${D}/gates/status.sh" ;;
  k11-p491a)  start_job k11-p491a; bash "${D}/gates/status.sh" ;;
  k11-p499a)  start_job k11-p499a; bash "${D}/gates/status.sh" ;;
  k11-p503a)  start_job k11-p503a; bash "${D}/gates/status.sh" ;;
  repair-tail) bash "${D}/gates/repair-tail.sh"; bash "${D}/gates/status.sh" ;;
  *) note "not on menu: $GATE"; exit 2 ;;
esac
