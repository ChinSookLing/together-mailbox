# Push one result directory to the results branch of this private repo.
# Never pushes main. Never prints the token.
set +x
set -euo pipefail
src="${1:?}"
repo="${RESULT_REPO:?}"
token="${RESULT_TOKEN:?}"
: "${GATE:?}" "${RUN_ID:?}"
case "$GATE" in
  status|p233-pack|p191|p241ab|p241c|p409|collect) ;;
  *) echo "refusing gate name" >&2; exit 2 ;;
esac
case "$RUN_ID" in
  *[!0-9]*) echo "refusing run id" >&2; exit 2 ;;
esac
case "${MACHINE:?}" in
  office-wsl|office-wsl-2|office-wsl-3|office-wsl-4) ;;
  *) echo "refusing machine" >&2; exit 2 ;;
esac

if grep -R -l -e 'ghs_' -e 'github_pat_' -e 'AUTHORIZATION: bearer' -e 'AUTHORIZATION: basic' -e 'x-access-token:' "$src" >/dev/null 2>&1; then
  echo "refusing to publish a file that looks like a token" >&2
  exit 3
fi

basic="$(printf 'x-access-token:%s' "$token" | base64 | tr -d '\n')"
unset token
dest="results/${MACHINE}/${GATE}/${RUN_ID}"
ok=0
attempt=1
while [[ "$attempt" -le 5 ]]; do
  if (
    set -euo pipefail
    work="$(mktemp -d)"
    trap 'rm -rf "$work"' EXIT
    git init -q "$work"
    git -C "$work" remote add origin "https://github.com/${repo}.git"
    git -C "$work" config http.https://github.com/.extraheader "AUTHORIZATION: basic ${basic}"
    if git -C "$work" ls-remote --heads origin results | awk '{ print $2 }' | grep -qx 'refs/heads/results'; then
      git -C "$work" fetch -q --depth 1 origin results
      git -C "$work" checkout -q -B results FETCH_HEAD
    else
      git -C "$work" checkout -q --orphan results
    fi
    mkdir -p "$work/$dest"
    cp -a "$src"/. "$work/$dest/"
    git -C "$work" add -- "$dest"
    if ! git -C "$work" diff --cached --quiet; then
      git -C "$work" -c user.name=office-gate -c user.email=office-gate@local commit -q -m "results ${MACHINE} ${GATE} ${RUN_ID}"
      git -C "$work" push -q origin HEAD:results
    fi
  ); then
    ok=1
    break
  fi
  echo "results push was not fast-forward, attempt ${attempt}" >&2
  if [[ "$attempt" -lt 5 ]]; then
    sleep 2
  fi
  attempt=$((attempt + 1))
done
unset basic
if [[ "$ok" != "1" ]]; then
  echo "results push failed after 5 attempts" >&2
  exit 1
fi
printf 'published %s\n' "$dest"
