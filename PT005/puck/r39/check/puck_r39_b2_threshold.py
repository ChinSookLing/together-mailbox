# Puck R39 side check: b=2 alone at the primes just below 67 (where does "b=2 alone reaches 640" start?).
import sys,os,io,contextlib,json
from multiprocessing import Pool
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'..','..','r38','check'))
from k5_P769_b23 import run
REF=set(tuple(map(tuple,c)) for c in json.load(open(os.path.join(HERE,'..','..','r38','check','k5_sets.json')))['61']['all'])
def one(p):
    with contextlib.redirect_stdout(io.StringIO()): A,_,_=run(p,(2,))
    return p,len(A),A<=REF
if __name__=="__main__":
    with Pool(5) as P:
        for r in P.imap(one,(43,47,53,59,61)): print('p=%d b=2 alone: %d configs, inside 640-set: %s'%r,flush=True)
