#!/bin/bash
# Puck: RUN-SHEET-p223-then-p401.md step 2 (b2f36c2), p=223 (a)+(b); compare deferred
cd ~/lr16/code
date '+%F %T %Z' | tee ~/kit/run223.time
python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 223 12 ~/lr16/out223 2>&1 | tee ~/kit/run223.log
date '+%F %T %Z' | tee -a ~/kit/run223.time
