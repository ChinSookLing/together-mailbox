#!/bin/bash
# PT005 office PC kit (Opus): build the author's engine and cascade for K=15 (16 runners) inside WSL Ubuntu.
# Usage:  bash setup_k15.sh            (downloads the author's zip from Zenodo)
#         bash setup_k15.sh path/to/fifteen_runners_code_and_logs.zip
set -euo pipefail
ZIP_SHA=0d1de11611730f34e9726a53bca84fb17acb2346016cca529e565427015b621d
mkdir -p ~/lr16 && cd ~/lr16
if [ $# -ge 1 ]; then cp "$1" fifteen_runners_code_and_logs.zip; fi
if [ ! -f fifteen_runners_code_and_logs.zip ]; then
  curl -L --fail -o fifteen_runners_code_and_logs.zip \
    "https://zenodo.org/api/records/22667683/files/fifteen_runners_code_and_logs.zip/content"
fi
echo "$ZIP_SHA  fifteen_runners_code_and_logs.zip" | sha256sum -c -
rm -rf code && unzip -q fifteen_runners_code_and_logs.zip 'code/*' && cd code
grep -E 'basegen_k_campaign.cpp|bgk_incremental_gain.h|cascade_filter_k.cpp' SOURCES_SHA256.txt | sha256sum -c -
# the one-line scouting patch (ledger L2): relax the static_assert that blocks K=15; only labels and selftest use it
sed 's/static_assert(2 \* K < 29, "tight lookup assumes 2K < P for P >= 29");/static_assert(2 * K < 89, "CHAIR SCOUTING PATCH: tight lookup needs 2K < P; only P >= 89 used");/' \
  cascade_filter_k.cpp > cascade_filter_k_patched.cpp
diff cascade_filter_k.cpp cascade_filter_k_patched.cpp || true
F="-O3 -march=native -std=c++20 -DNW=8 -DMAXN=512 -DBGK_INCREMENTAL_GAIN -DBGK_DEFERRED_PROBES -DBGK_THRESHOLD_WITNESS"
g++ $F -DK=15 -o bgk15 basegen_k_campaign.cpp
g++ -O3 -march=native -std=c++17 -DK=15 -o cascade_k15p cascade_filter_k_patched.cpp
./bgk15 239 info
sha256sum bgk15 cascade_k15p cascade_filter_k_patched.cpp
lscpu | grep -E 'Model name|^CPU\(s\)'; g++ --version | head -1
echo SETUP_OK
