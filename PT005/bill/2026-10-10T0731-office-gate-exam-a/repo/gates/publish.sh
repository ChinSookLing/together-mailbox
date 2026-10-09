# Push one result directory to the results branch of this private repo.
# Never pushes main. Never prints the token.
set +x
set -euo pipefail
src="${1:?}"
repo="${RESULT_REPO:?}"
token="${RESULT_TOKEN:?}"
: "${GATE:?}" "${RUN_ID:?}"
case "$GATE" in
  status|p233-pack|p191|p241ab|p241c|p409|p383|p307|p337|collect) ;;
  *) echo "refusing gate name" >&2; exit 2 ;;
esac
case "$RUN_ID" in
  *[!0-9]*) echo "refusing run id" >&2; exit 2 ;;
esac

if grep -R -l -e 'ghs_' -e 'github_pat_' -e 'AUTHORIZATION: bearer' -e 'AUTHORIZATION: basic' -e 'x-access-token:' "$src" >/dev/null 2>&1; then
  echo "refusing to publish a file that looks like a token" >&2
  exit 3
fi

work="$(mktemp -d)"
cleanup() { rm -rf "$work"; }
trap cleanup EXIT
git init -q "$work"
git -C "$work" remote add origin "https://github.com/${repo}.git"
basic="$(printf 'x-access-token:%s' "$token" | base64 | tr -d '\n')"
git -C "$work" config http.https://github.com/.extraheader "AUTHORIZATION: basic ${basic}"
unset basic
if git -C "$work" ls-remote --heads origin results | awk '{ print $2 }' | grep -qx 'refs/heads/results'; then
  git -C "$work" fetch -q --depth 1 origin results
  git -C "$work" checkout -q -B results FETCH_HEAD
else
  git -C "$work" checkout -q --orphan results
fi
dest="results/${GATE}/${RUN_ID}"
mkdir -p "$work/$dest"
cp -a "$src"/. "$work/$dest/"
git -C "$work" add -- "$dest"
git -C "$work" -c user.name=office-gate -c user.email=office-gate@local commit -q -m "results ${GATE} ${RUN_ID}"
git -C "$work" push -q origin HEAD:results
printf 'published %s\n' "$dest"
