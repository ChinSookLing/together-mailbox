# R9 scoring search (protocol fixed in packet ec15a2d): for N, scan primes upward from START,
# 150 s per prime with findcoversN.py; stop after 6 consecutive primes with no cover found.
# Idempotent: a prime whose output already has a 'done' line is not rerun.
import subprocess, sys, os
N=int(sys.argv[1]); start=int(sys.argv[2]); d=os.path.dirname(os.path.abspath(__file__))
def isprime(m): return m>1 and all(m%q for q in range(2,int(m**.5)+1))
p=start; miss=0; last=None; log=[]
while miss<6:
    if isprime(p):
        out=f"{d}/N{N}_p{p}.txt"
        if not (os.path.exists(out) and any(l.startswith('done') for l in open(out))):
            with open(out,'w') as fh:
                subprocess.run(['timeout','220','python3',f'{d}/../findcoversN.py',str(p),str(N),'100000','1','150'],stdout=fh)
        found=sum(1 for l in open(out) if l.startswith('cover'))
        if found: last=p; miss=0
        else: miss+=1
        log.append((p,found)); print(N,p,found,'miss_run',miss,flush=True)
    p+=1
print('RESULT N',N,'observed death line',last,'table',log,flush=True)
