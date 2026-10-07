# Push one result directory to the results branch of this private repo.
# Never pushes main. Never prints the token.
set +x
set -euo pipefail
src="${1:?}"
repo="${RESULT_REPO:?}"
token="${RESULT_TOKEN:?}"
: "${GATE:?}" "${RUN_ID:?}"

if grep -R -l -e 'ghs_' -e 'github_pat_' -e 'AUTHORIZATION: bearer' "$src" >/dev/null 2>&1; then
  echo "refusing to publish a file that looks like a token" >&2
  exit 3
fi

work="$(mktemp -d)"
cleanup() { rm -rf "$work"; }
trap cleanup EXIT
git init -q "$work"
git -C "$work" remote add origin "https://github.com/${repo}.git"
git -C "$work" config http.extraheader "AUTHORIZATION: bearer ${token}"
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
