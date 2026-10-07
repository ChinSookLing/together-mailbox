#!/usr/bin/env python3
"""Encode all normalized irredundant level-2 survivors except the five seeds.

The excluded seeds are validated instances, not assumed to be a complete list.
An UNSAT proof for the resulting formula would prove that completeness.
Only the irredundant branch is encoded; reducible-branch coverage is separate.
"""
import json, re
from pathlib import Path
from check_model import constraints, violated

P=401
SEEDS=[
 [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
 [1,2,3,4,5,6,7,8,9,10,11,12,13,15,28],
 [402,2,406,408,8,410,412,414,430,432,38,60,91,149,566],
 [402,406,408,8,410,412,414,420,430,449,60,480,118,139,586],
 [402,7,418,18,44,450,50,484,104,506,122,524,550,171,174],
]


def dist(x,m):
    r=x%m;return min(r,m-r)


def normalize(w):
    out=set();m=2*P
    for anchor in w:
        if anchor%2==0:continue
        unit=pow(anchor,-1,m)
        out.add(tuple(sorted(dist(unit*v,m) for v in w)))
    return sorted(out)


def validate_survivor(w):
    assert len(w)==15 and all(v%P for v in w)
    C=[dist(v,P) for v in w]
    assert len(set(C))==15
    cover=[[i for i,c in enumerate(C) if 16*dist(t*c,P)<P]
           for t in range(1,(P+1)//2)]
    assert all(cover)
    assert {owners[0] for owners in cover if len(owners)==1}==set(range(15))
    assert sum(v%2 for v in w)>=2
    assert not any(all(16*dist(t*v,2*P)>=2*P for v in w)
                   for t in range(2*P))


def make_constraints(blockers):
    p=P;n=(p-1)//2
    c=[]
    c.append(({u:1 for u in range(1,p)},15))
    c.append(({u:-1 for u in range(1,p)},-15))
    c.append(({u:1 for u in range(1,p,2)},2))
    c.append(({1:1},1))
    for cls in range(1,n+1):c.append(({cls:-1,p-cls:-1},-1))
    for t in range((p-1)//8+1,p+1):
        c.append(({u:1 for u in range(1,p) if 8*dist(t*u,2*p)<p},1))
    for t in range(1,n+1):
        covered=[u for u in range(1,p) if 16*dist(t*u,p)<p]
        c.append(({u:1 for u in covered},1))
        c.append(({**{u:-1 for u in covered},p-1+t:-14},-15))
    for cls in range(1,n+1):
        terms={p-1+t:1 for t in range(1,n+1) if 16*dist(t*cls,p)<p}
        terms[cls]=-1;terms[p-cls]=-1
        c.append((terms,0))
    for E in blockers:c.append(({u:-1 for u in E},-14))
    return c


def write(path,cs):
    with path.open('w') as out:
        out.write(f'* #variable= 600 #constraint= {len(cs)}\n')
        out.write('* p=401; level=2; irredundant branch only; INPUT NOT AN UNSAT PROOF\n')
        for terms,rhs in cs:
            out.write(' '.join(f'{a:+d} x{u}' for u,a in terms.items())+f' >= {rhs} ;\n')


def run():
    directory=Path(__file__).resolve().parent
    orbit_lists=[]
    for w in SEEDS:
        validate_survivor(w);orbit_lists.append(normalize(w))
    flat=[E for orbit in orbit_lists for E in orbit]
    assert len(flat)==len(set(flat))==22
    for E in flat:validate_survivor(E)
    base=make_constraints([]);with_blocks=make_constraints(flat)
    write(directory/'p401-level2-ir-base.opb',base)
    write(directory/'p401-level2-ir-except-five.opb',with_blocks)
    records=[]
    for E in flat:
        values={u:1 for u in E}
        for t in range(1,201):
            hits=sum(16*dist(t*u,401)<401 for u in E)
            values[400+t]=int(hits==1)
        assert not violated(directory/'p401-level2-ir-base.opb',values)
        failures=violated(directory/'p401-level2-ir-except-five.opb',values)
        assert len(failures)==1 and failures[0]>len(base)
        records.append({'normalized_speeds':E,'excluded_by_constraint':failures[0]})
    # The LP relaxation is feasible even with all 22 exception blocks.
    # Common denominator 398: x1=1, x400=0, other x=7/199, all q=1/2.
    fractional={u:(398 if u==1 else 0 if u==400 else 14)
                for u in range(1,401)}
    fractional.update({400+t:199 for t in range(1,201)})
    assert all(0<=v<=398 for v in fractional.values())
    assert not violated(directory/'p401-level2-ir-except-five.opb',fractional,398)
    result={'p':401,'scope':'irredundant level-2 branch',
            'variables':600,'base_constraints':len(base),
            'constraints_with_exception_blocks':len(with_blocks),
            'normalizations_per_seed':[len(o) for o in orbit_lists],
            'total_normalizations':len(flat),
            'all_seed_models_validated':True,
            'LP_relaxation_fractional_feasible':True,
            'LP_assignment':{'x1':'1','x400':'0','other_x':'7/199','all_q':'1/2'},
            'exception_list_completeness':'NOT_PROVED; UNSAT proof needed',
            'models':records}
    (directory/'p401-level2-exceptions.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='models'},indent=2))


if __name__=='__main__':run()
