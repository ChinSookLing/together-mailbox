#!/bin/sh
# TOGETHER - PROOF TABLE 004 - Round 3 - Turn 11 - item L3-C (prime gate p = 83) - Fable-A
# Every command of the turn, in order.  Needs: a C compiler (cc), python3.  No network.
# Usage:  sh pt004_l3c_run.sh [ARCHIVE_DIR]
#   ARCHIVE_DIR (optional) = folder holding p83/ and certificates_p83/ taken from
#   fourteen_lonely_runners_package.zip of Zenodo record 22066772 (small_gates/).
#   Without it the comparison with the archive is skipped; everything else still runs.
set -e
step() { echo "== $1"; }

step "build";                         cc -O2 -std=c11 -o pt004_l3c pt004_l3c.c
step "stage 1: tiny cases";           python3 pt004_l3c_tests.py > stage1_tests.out
step "level one, p = 43 (extra)";     ./pt004_l3c level1 43 13 level1_p43.txt > level1_p43.log
step "stage 2: level one, p = 83";    ./pt004_l3c level1 83 13 level1_p83.txt > level1_p83.log
step "second implementation, p = 43"; python3 pt004_l3c_level1_check.py 43 13 level1_p43.txt > level1_check_p43.out
step "second implementation, p = 83"; python3 pt004_l3c_level1_check.py 83 13 level1_p83.txt > level1_check_p83.out
step "stage 3: lifts 2..32 and 14";   ./pt004_l3c cascade 83 13 level1_p83.txt cascade_p83.txt > cascade_p83.log
if [ -n "$1" ]; then
  step "comparison with the archive"
  python3 pt004_l3c_compare.py level1_p83.txt cascade_p83.txt cascade_p83.log "$1" > compare_p83.out
else
  echo "== comparison with the archive skipped (no ARCHIVE_DIR given)"
fi
step "sha256 of the outputs"
sha256sum stage1_tests.out level1_p43.log level1_p43.txt level1_p83.log level1_p83.txt \
          level1_check_p43.out level1_check_p83.out cascade_p83.log cascade_p83.txt
[ -f compare_p83.out ] && sha256sum compare_p83.out
echo "== all steps finished"
