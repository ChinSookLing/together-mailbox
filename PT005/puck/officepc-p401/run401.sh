#!/bin/bash
# Puck: RUN-SHEET-p223-then-p401.md step 3 (b2f36c2), p=401 pilot; end time appended when it finishes
cd ~/lr16/code
date '+%F %T %Z' | tee ~/kit/run401.time
python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 401 12 ~/lr16/out401 > ~/kit/run401.log 2>&1
date '+%F %T %Z' | tee -a ~/kit/run401.time
