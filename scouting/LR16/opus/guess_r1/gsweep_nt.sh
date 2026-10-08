#!/bin/bash
# gamma(p) via bgk15 km1low: smallest smax with canonical>0 (engine exhausts smaller smax -> lower bound)
B=/home/claude/lr16/code15/code/bgk15
for p in "$@"; do for s in 9 10 11 12 13; do
  f=out/g${p}_s$s
  if [ ! -f $f.done ]; then
    $B $p km1low $s $f.txt > $f.log 2>&1 && touch $f.done || { echo "$p s$s FAIL/TIMEOUT" >> gsweep.log; break; }
    echo "$p s$s $(tail -1 $f.log)" >> gsweep.log
  fi
  c=$(grep -o 'canonical=[0-9]*' $f.log | cut -d= -f2); [ "$c" != "0" ] && { echo "$p GAMMA=$s" >> gamma.txt; head -1 $f.txt > out/wit$p.txt; rm -f $f.txt; break; }
  rm -f $f.txt
done; [ -f out/g${p}_s13.done ] && ! grep -q "^$p GAMMA" gamma.txt && echo "$p GAMMA>=14" >> gamma.txt; done
