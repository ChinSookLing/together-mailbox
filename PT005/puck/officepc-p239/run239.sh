#!/bin/bash
cd ~/lr16/code
date "+%F %T %Z" > ~/kit/run239.time
python3 ~/kit/kcascade_run.py ./bgk15 ./cascade_k15p 239 12 ~/lr16/out239 > ~/kit/run239.log 2>&1
date "+%F %T %Z" >> ~/kit/run239.time
