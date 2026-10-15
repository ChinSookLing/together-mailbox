# Puck R39: close the 67..767 gap of the 640 theorem (Hesper 0dade56 / Puck 97b9d8e).
# Theorem already PROVED: U_p (realized mixed doublable k=5 configs at prime p) is a subset of the 640-set
# (= realized set at p=61, = U at P>768). So equality at p holds as soon as some b's reach all 640.
# Per prime p in 67..767: grow b = 2,3,4,... until the union reaches 640 (stop early), and ASSERT every
# realized config is inside the 640-set (independent re-check of the upper bound at that p).
# Solver: Puck's own run() from ../../r38/check/k5_P769_b23.py (raw hit test + Algorithm X, no Hesper code).
import sys, os, json, time
from multiprocessing import Pool
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE,'..','..','r38','check'))
import io, contextlib
from k5_P769_b23 import run
REF=set(tuple(map(tuple,c)) for c in json.load(open(os.path.join(HERE,'..','..','r38','check','k5_sets.json')))['61']['all'])
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
def one(p):
    t=time.time(); Up=set(); used=[]
    for b in range(2,(p+1)//2):
        with contextlib.redirect_stdout(io.StringIO()): A,_,_=run(p,(b,))
        used.append(b); out=A-REF
        if out: return dict(p=p,error='config outside 640-set',b=b,n_out=len(out))
        Up|=A
        if len(Up)==640: break
    return dict(p=p,b_used=used,U=len(Up),equal=Up==REF,sec=round(time.time()-t,1))
if __name__=="__main__":
    assert len(REF)==640
    ps=[p for p in range(67,768) if isprime(p)]
    print('primes',len(ps),ps[0],ps[-1],flush=True)
    with Pool(8) as pool:
        res=[]
        for r in pool.imap(one,ps):
            print(json.dumps(r),flush=True); res.append(r)
    ok=all(r.get('equal') for r in res)
    print('SUMMARY primes',len(res),'all equal 640:',ok,'max b used',max(len(r.get('b_used',[0])) for r in res),flush=True)
