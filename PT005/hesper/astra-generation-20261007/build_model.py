#!/usr/bin/env python3
"""Write the normalized 16-runner residual problem in Boolean OPB form.

All arithmetic is integral. This generates a problem, not an UNSAT proof.
For each signed residue u, four bits encode multiplicity 0..15 and a fifth
bit encodes presence. Coordinates repeating modulo 16p are retained.
"""
import argparse, hashlib, json
from math import isqrt
from pathlib import Path


def write_model(p, path, raw=False):
    assert p>=17 and all(p%d for d in range(2,isqrt(p)+1))
    modulus=16*p
    residues=[u for u in range(1,8*p+1) if u%p]
    times=[p]+[t for t in range(p+1,8*p+1) if t%p]
    n=len(residues);count=2*n+4+(0 if raw else 3)+len(times)
    terms_total=0
    with path.open('w') as out:
        out.write(f'* #variable= {5*n} #constraint= {count}\n')
        out.write(f'* p={p}; modulus={modulus}; raw={raw}; threshold=1/16\n')
        out.write('* Semantic/proof scope is in README.md; no solver proof is included.\n')
        def emit(terms,rhs):
            nonlocal terms_total
            items=[(a,x) for a,x in terms if a]
            terms_total+=len(items)
            out.write(' '.join(f'{a:+d} x{x}' for a,x in items)+f' >= {rhs} ;\n')
        def multiplicity_terms(weights):
            return [(weight*(1<<b),5*j+b+1) for j,weight in enumerate(weights)
                    for b in range(4) if weight]
        for j,u in enumerate(residues):
            bits=[(1<<b,5*j+b+1) for b in range(4)];presence=5*j+5
            emit(bits+[(-1,presence)],0)
            emit([(-a,x) for a,x in bits]+[(15,presence)],0)
        emit(multiplicity_terms([1]*n),15)
        emit(multiplicity_terms([-1]*n),-15)
        emit(multiplicity_terms([int(u%2!=0) for u in residues]),2)
        emit([(1,5)],1)  # a unit maps one odd coordinate to residue 1
        if not raw:
            s4=[];s8=[];s16=[]
            for u in residues:
                if u%2: v=(1,1,2)
                elif u%4: v=(2,2,2)
                elif u%8: v=(0,4,4)
                elif u%16: v=(0,0,8)
                else: v=(0,0,0)
                s4.append(v[0]);s8.append(v[1]);s16.append(v[2])
            for weights,rhs in [(s4,4),(s8,8),(s16,16)]:
                emit(multiplicity_terms(weights),rhs)
        for t in times:
            blocked=[]
            for j,u in enumerate(residues):
                r=t*u%modulus
                if min(r,modulus-r)<p:blocked.append((1,5*j+5))
            emit(blocked,1)
    return {'p':p,'raw':raw,'residue_types':n,'boolean_variables':5*n,
            'constraints':count,'time_constraints':len(times),
            'coefficient_occurrences':terms_total,'bytes':path.stat().st_size,
            'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'status':'INPUT_GENERATED_NOT_SOLVED'}


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('p',type=int)
    ap.add_argument('output',type=Path);ap.add_argument('--raw',action='store_true')
    args=ap.parse_args()
    print(json.dumps(write_model(args.p,args.output,args.raw),indent=2))
