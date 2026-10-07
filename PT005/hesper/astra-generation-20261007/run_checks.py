#!/usr/bin/env python3
"""Reproduce model generation and exact finite controls; not an UNSAT proof."""
import json
from pathlib import Path
from build_model import write_model
from check_model import check_encoding, check_fractional, exact_assignment, violated
from level2_exceptions import run as check_level2

HERE=Path(__file__).resolve().parent

def main():
    records=[]
    for p,raw in [(17,False),(233,True),(233,False),(239,False),(401,False)]:
        path=HERE/f"p{p}-{'raw' if raw else 'residual'}.opb"
        records.append(write_model(p,path,raw))
        records.append(check_encoding(p,path,raw))
        if p in (239,401):
            records.append(check_fractional(p,path))

    control17=[2,28,39,44,46,64,65,76,84,93,95,107,121,124,126]
    a17=exact_assignment(17,control17)
    assert not violated(HERE/'p17-residual.opb',a17)
    records.append({'control':'p17 known grid-improper L7-failing tuple',
                    'result':'SAT_ASSIGNMENT_VERIFIED',
                    'meaning':'encoder is not unconditionally UNSAT'})

    core=[1,7,10,12,31,32,43,45,50,65,85,91,110]
    p=233
    assert all(any(16*min((t*c)%p,p-(t*c)%p)<p for c in core)
               for t in range(1,p))
    forced=[16*c for c in core]+[1,1]
    af=exact_assignment(p,forced)
    assert not violated(HERE/'p233-raw.opb',af)
    failure=violated(HERE/'p233-residual.opb',af)
    assert failure==[3717,3718,3719]
    records.append({'control':'p233 forced family with duplicate odd residue',
                    'raw':'SAT_ASSIGNMENT_VERIFIED',
                    'residual':'REJECTED_BY_THREE_L7_FAILURE_CONSTRAINTS',
                    'failed_constraint_indices':failure})

    at=exact_assignment(401,list(range(1,16)))
    failure=violated(HERE/'p401-residual.opb',at)
    assert failure==[6408]
    records.append({'control':'p401 tight tuple 1..15',
                    'result':'REJECTED_AT_GOOD_BOUNDARY_TIME_1_OVER_16',
                    'failed_constraint_indices':failure})
    (HERE/'encoding-checks.json').write_text(json.dumps(records,indent=2)+'\n')
    check_level2()
    print('PASS: finite encoding controls only. NO UNSAT CERTIFICATE.')

if __name__=='__main__':
    main()

