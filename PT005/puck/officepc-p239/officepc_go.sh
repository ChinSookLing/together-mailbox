#!/bin/bash
# Puck: same as Opus's setup_k15.sh, except the zip was downloaded and checked on Puck's computer
# (sha256 0d1de116...621d OK) because the office network was too slow; only code/ was copied over.
set -euo pipefail
mkdir -p ~/lr16 ~/kit && cd ~/lr16
rm -rf code && tar xzf /mnt/c/Users/GIGABYTE/code_only.tgz && cd code
{
echo "ZIP checked on Puck's box: 0d1de11611730f34e9726a53bca84fb17acb2346016cca529e565427015b621d  fifteen_runners_code_and_logs.zip: OK"
grep -E 'basegen_k_campaign.cpp|bgk_incremental_gain.h|cascade_filter_k.cpp' SOURCES_SHA256.txt | sha256sum -c -
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
} 2>&1 | tee ~/kit/setup.log
grep -q SETUP_OK ~/kit/setup.log
cd ~/lr16/code
echo READY
