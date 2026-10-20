# Job k11-p461a (Opus note 111 §3 55620cd; BUDGET per note 112 §3 558efd3), second-machine run of gate p = 461 part (a), office kit unchanged.
# Build once with jobs/kit/setup_k15.sh (sha256 602b6f99...), then kcascade_run.py (sha256 90632d55...) with 16 workers.
# First start: BUDGET stops new jobs at 2026-10-24 18:00 +08. Any start after that runs with no BUDGET.
# Restart-safe: kcascade_run.py skips jobs already in out461/ir.jsonl.
set +x
set -uo pipefail
OUT=/tmp
source "${HOME}/k11-gate/dispatcher/gates/lib.sh"
N=k11-p461a; W="$WORK/$N"; CK="$W/ckpt"; R="$W/out461"; B="$HOME/lr16/code"
install -d "$CK" "$R"
exec >>"$W/run.log" 2>&1
echo "$(date '+%F %T %Z') start $N"
snap() {
  cp -f "$W/run461.time" "$W/hashes.txt" "$W/lscpu.txt" "$CK/" 2>/dev/null
  tail -n 20 "$W/setup.log" > "$CK/setup.log.tail" 2>/dev/null
  tail -n 20 "$W/run461.log" > "$CK/run461.log.tail" 2>/dev/null
  cp -f "$R/ir.jsonl" "$R/km1.json" "$CK/" 2>/dev/null
  n=$(cat "$R/ir.jsonl" 2>/dev/null | wc -l)
  printf '{"job":"%s","ir_lines":%s,"of":602,"time":"%s"}\n' "$N" "$n" "$(date '+%F %T %Z')" > "$CK/latest.json.tmp" && mv "$CK/latest.json.tmp" "$CK/latest.json"
}
if [[ ! -f "$W/build.ok" ]]; then
  if ! command -v unzip >/dev/null 2>&1; then
    install -d "$W/bin"; cp "$D/jobs/kit/unzip-shim.py" "$W/bin/unzip"; chmod +x "$W/bin/unzip"; export PATH="$W/bin:$PATH"
    echo "unzip missing: using jobs/kit/unzip-shim.py"
  fi
  bash "$D/jobs/kit/setup_k15.sh" > "$W/setup.log" 2>&1
  grep -q '^SETUP_OK' "$W/setup.log" || { echo "$(date '+%F %T %Z') setup FAILED"; snap; exit 1; }
  (cd "$B" && sha256sum bgk15 cascade_k15p cascade_filter_k_patched.cpp) > "$W/hashes.txt"
  lscpu > "$W/lscpu.txt"
  date '+%F %T %Z' > "$W/build.ok"
fi
cp -f "$D/jobs/kit/kcascade_run.py" "$B/kcascade_run.py"
now=$(date +%s); dl=$(date -d '2026-10-24 18:00:00 +0800' +%s)
( while sleep 300; do snap; done ) & SNAP=$!
cd "$B"
date '+%F %T %Z' | tee -a "$W/run461.time"
if (( now < dl )); then
  echo "BUDGET=$((dl - now))"
  BUDGET=$((dl - now)) python3 kcascade_run.py ./bgk15 ./cascade_k15p 461 16 "$R" 2>&1 | tee -a "$W/run461.log"
else
  echo "no BUDGET"
  python3 kcascade_run.py ./bgk15 ./cascade_k15p 461 16 "$R" 2>&1 | tee -a "$W/run461.log"
fi
rc=${PIPESTATUS[0]}
date '+%F %T %Z' | tee -a "$W/run461.time"
kill "$SNAP" 2>/dev/null
n=$(wc -l < "$R/ir.jsonl" 2>/dev/null || echo 0)
echo "$(date '+%F %T %Z') kcascade rc=$rc ir_lines=$n"
snap
if (( rc == 0 && n >= 602 )); then date '+%F %T %Z' > "$STATE/$N.done"; echo "DONE $N"; fi
