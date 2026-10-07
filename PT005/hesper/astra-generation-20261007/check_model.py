#!/usr/bin/env python3
"""Check the OPB encoding, NOT a solver proof.

The builder enumerates speeds and multiplies. This checker derives each bad
set by modular inversion of the allowed signed products. It does not import
the builder. Also includes exact integer-scaled checks of fractional LP models.
"""
import argparse, json, re
from collections import Counter
from math import gcd
from pathlib import Path


def constraints(path):
    for line in path.open():
        line=line.strip()
        if not line or line.startswith('*'):continue
        lhs,rhs=line.split(' >= ')
        assert rhs.endswith(' ;')
        terms={}
        for term in re.finditer(r'([+-]\d+) x(\d+)',lhs):
            a,v=map(int,term.groups());assert v not in terms
            terms[v]=a
        assert ' '.join(f'{a:+d} x{v}' for v,a in terms.items())==lhs
        yield terms,int(rhs[:-2])


def bad_set_inverse(p,t):
    m=16*p;g=gcd(t,m);q=m//g;inv=pow(t//g,-1,q)
    result=set()
    for b in range(1-p,p):
        if b%g:continue
        root=(b//g)*inv%q
        for j in range(g):
            u=(root+j*q)%m
            if u%p:
                result.add(min(u,m-u))
    return result


def check_encoding(p,path,raw=False):
    U=[u for u in range(1,8*p) if u%p];n=len(U);stream=iter(constraints(path));checked=0
    def expect(terms,rhs):
        nonlocal checked
        assert next(stream)==(terms,rhs),f'constraint {checked+1} mismatch'
        checked+=1
    def mterms(weight):
        return {5*j+b+1:(1<<b)*weight(u) for j,u in enumerate(U)
                for b in range(4) if weight(u)}
    for j,u in enumerate(U):
        expect({**{5*j+b+1:1<<b for b in range(4)},5*j+5:-1},0)
        expect({**{5*j+b+1:-(1<<b) for b in range(4)},5*j+5:15},0)
    expect(mterms(lambda u:1),15);expect(mterms(lambda u:-1),-15)
    expect(mterms(lambda u:int(u&1)),2);expect({5:1},1)
    if not raw:
        for D in (4,8,16):
            def weight(u):
                if u%D==0:return 0
                g=gcd(u,D);return g*((D//g+7)//8)
            expect(mterms(weight),D)
    for t in range(p,8*p+1):
        if t!=p and t%p==0:continue
        B=bad_set_inverse(p,t)
        expect({5*(u-1-u//p)+5:1 for u in sorted(B)},1)
    assert next(stream,None) is None
    header=path.open().readline().strip()
    assert header==f'* #variable= {5*n} #constraint= {checked}'
    return {'p':p,'constraints_verified':checked,
            'result':'ENCODING_CHECKED_NOT_AN_UNSAT_PROOF'}


def exact_assignment(p,speeds):
    m=16*p;odd=next(u for u in speeds if u%2)
    scale=pow(odd,-1,m)
    counts=Counter(min((u*scale)%m,m-(u*scale)%m) for u in speeds)
    values={}
    for u,count in counts.items():
        assert 0<u<8*p and u%p and 1<=count<=15
        j=u-1-u//p
        for b in range(4):values[5*j+b+1]=(count>>b)&1
        values[5*j+5]=1
    return values


def violated(path,values,denominator=1):
    return [i for i,(terms,rhs) in enumerate(constraints(path),1)
            if sum(a*values.get(v,0) for v,a in terms.items())<rhs*denominator]


def check_fractional(p,path):
    N=(p-1)//2;H=(p-1)//16
    assert N>=10 and 10*H>=N
    # A common denominator N keeps this verification purely integral.
    values={}
    for u in range(1,8*p):
        if u%p==0:continue
        numerator=N if u in (1,2,3,4,8) else 10 if u%16==0 else 0
        if numerator:
            j=u-1-u//p;values[5*j+1]=numerator;values[5*j+5]=numerator
    assert all(0<=x<=N for x in values.values())
    assert not violated(path,values,N)
    return {'p':p,'LP_fractional_feasible':True,'denominator':N,
            'zero_residue_multiplicity_numerator':10,
            'conclusion':'root LP infeasibility/dual certificate is impossible for this formulation'}


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('p',type=int)
    ap.add_argument('file',type=Path);ap.add_argument('--raw',action='store_true')
    ap.add_argument('--fractional',action='store_true');a=ap.parse_args()
    print(json.dumps(check_encoding(a.p,a.file,a.raw)))
    if a.fractional:print(json.dumps(check_fractional(a.p,a.file)))
