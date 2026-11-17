# Reviewed local dispatcher. Does not checkout or run ${GITHUB_SHA}.
set +x
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
sha256sum -c SHA256SUMS
cd /tmp
exec bash "$ROOT/gates/dispatch.sh"
