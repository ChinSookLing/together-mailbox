# Menu status. No gate run. No environment dump.
set +x
set -euo pipefail
source "$(dirname "$0")/lib.sh"
{
  printf 'user %s\n' "$(id -un)"
  printf 'host %s\n' "$(hostname)"
  uname -a
} > "$STAGE/host.txt"
df -h "$HOME" > "$STAGE/disk.txt" || true
if user_bus; then
  echo yes > "$STAGE/user_bus.txt"
else
  echo no > "$STAGE/user_bus.txt"
fi
for unit in office-gate-p191 office-gate-p241ab office-gate-p241c office-gate-p409 office-gate-p383 office-gate-p307 office-gate-p337 office-gate-p397 office-gate-p431 office-gate-p443 office-gate-p463 office-gate-p461 office-gate-p439; do
  if [[ -S "${XDG_RUNTIME_DIR:-/nonexistent}/bus" ]]; then
    systemctl --user is-active "${unit}.service" > "$STAGE/${unit}.active" 2>/dev/null || true
  fi
  for mark in done stopped; do
    if [[ -f "$HOME/office-gate/state/${unit#office-gate-}.${mark}" ]]; then
      echo yes > "$STAGE/${unit}.${mark}"
    fi
  done
done
if [[ -f "$HOME/lr16/out409/ir.jsonl" ]]; then
  wc -l < "$HOME/lr16/out409/ir.jsonl" > "$STAGE/out409-ir.count"
else
  echo 0 > "$STAGE/out409-ir.count"
fi
printf '%s\n' "$MAILBOX_PIN" > "$STAGE/mailbox_pin.txt"
# census14 snapshot. Read only. These files are written only in $STAGE.
# No kill, no signal, and no write under $HOME/lr16 or $HOME/kit.
date -Is > "$STAGE/census14.when"
pgrep -c -f 'bgk15 .* km1root' > "$STAGE/census14.workers" || echo 0 > "$STAGE/census14.workers"
if [[ -f "$HOME/lr16/census14/census14.jsonl" ]]; then
  cp -- "$HOME/lr16/census14/census14.jsonl" "$STAGE/census14.jsonl"
else
  printf '%s\n' missing > "$STAGE/census14.jsonl"
fi
tail -n 40 "$HOME/kit/census14.log" > "$STAGE/census14.log.tail" || true

# Primes 383, 307, 337 and the (a) doors. Read only. Writes only in $STAGE.
for p in 383 307 337 397 431 443 463 461 439; do
  if [[ ! -d "$HOME/lr16/out${p}" && ! -f "$HOME/kit/run${p}.log" && ! -f "$HOME/kit/run${p}.time" ]]; then
    continue
  fi
  if [[ -f "$HOME/lr16/out${p}/ir.jsonl" ]]; then
    wc -l < "$HOME/lr16/out${p}/ir.jsonl" > "$STAGE/out${p}-ir.count"
  else
    echo 0 > "$STAGE/out${p}-ir.count"
  fi
  if [[ -f "$HOME/kit/run${p}.log" ]]; then
    tail -n 1 "$HOME/kit/run${p}.log" > "$STAGE/run${p}.log.last" || true
  fi
  if [[ -f "$HOME/kit/run${p}.time" ]]; then
    cp -- "$HOME/kit/run${p}.time" "$STAGE/run${p}.time"
  fi
done

# census14 batch 2 process. Count, pid, elapsed time, cpu, and rss only.
# No command line is written. Does not stop the census, and does not renice or signal it.
# No background job. No write under $HOME/lr16 or $HOME/kit.
# If nothing matches, the file is the fixed text. A missing command does not fail this gate.
{
  ids="$(pgrep -d, -f '[k]m1census[.]py' 2>/dev/null || true)"
  if [[ -z "${ids}" ]]; then
    printf '%s\n' "km1census: not running"
  else
    pgrep -c -f '[k]m1census[.]py' 2>/dev/null || true
    ps -o pid=,etime=,pcpu=,rss= -p "${ids}" || true
  fi
} > "$STAGE/census14b2.pgrep" || true
free -m > "$STAGE/free.txt" || true
tail -n 20 "$HOME/kit/census14b2.log" > "$STAGE/census14b2.log.tail" || true
tail -n 3 "$HOME/lr16/census14/census14.jsonl" > "$STAGE/census14.jsonl.tail3" || true
