#!/bin/bash
# regenerate one p=401 irredundant job and keep the cascade survivor lines
r=$1; s=$2; E=../code15/code/bgk15; C=../code15/code/cascade_k15p
$E 401 irsubrootrawc $r $s ir_${r}_${s}.txt > gen_${r}_${s}.log
$C 401 filter ir_${r}_${s}.txt > surv_${r}_${s}.txt 2> casc_${r}_${s}.log
rm -f ir_${r}_${s}.txt; echo done > done_${r}_${s}
