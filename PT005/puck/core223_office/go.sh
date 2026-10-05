#!/bin/bash
# Puck: RUN-SHEET-core223.md step 3 (12 workers) then step 5 (compare)
cd ~/core223
date '+%F %T %Z' | tee run.time
WORKERS=12 python3 run_cores.py km1low13_p223.txt 2>&1 | tee run.log
date '+%F %T %Z' | tee -a run.time
cp ~/core223_ref/chair_cores.jsonl chair_cores.jsonl
python3 compare_cores.py cores.jsonl chair_cores.jsonl 2>&1 | tee compare.txt
echo GO_DONE > done.flag
