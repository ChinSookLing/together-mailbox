import re,difflib,sys,random,hashlib
from fractions import Fraction as F
P='/workspace/pt8_r007/PT008/'
src=open(P+'round-010/PT-008-R010-OPUS-TrackA.md','rb').read()
assert hashlib.sha256(src).hexdigest().startswith('fa050420')
srcl=src.decode().split('\n')
pub=P+'round-012/publication/'
ok=True
for n in ('HB','C1'):
    v2=open(pub+f'{n}-PUBLICATION-DRAFT-v2.md',encoding='utf-8').read().split('\n')
    fi=open(pub+f'final/{n}-PUBLICATION-FINAL.md',encoding='utf-8').read().split('\n')
    # verbatim block = from '## Setting' to end
    i=fi.index('## Setting (verbatim, Opus)'); j=v2.index('## Setting (verbatim, Opus)')
    fb=fi[i:]; vb=v2[j:]
    # strip marked editorial note lines from final
    fb2=[];skip=False
    for k,l in enumerate(fb):
        if l.startswith('> **[Editorial correction approved by chair'):
            if fb2 and fb2[-1]=='' : fb2.pop()
            continue
        fb2.append(l)
    same=fb2==vb
    print(n,'verbatim block identical to v2 (after removing marked note):',same)
    # each nonblank content line (excl headings I wrote) present in Opus source, in order
    pos=0;miss=[]
    for l in vb[1:]:
        if not l.strip() or l.startswith('## Section') : continue
        if l.strip()=='---': continue
        try: pos=srcl.index(l,pos)
        except ValueError:
            if l in srcl: miss.append(('order',l[:40]))
            else: miss.append(('absent',l[:40]))
    print(n,'lines not found verbatim in Opus source (in order):',miss)
    ok&=same and not miss
    d=[x for x in difflib.unified_diff(v2,fi,lineterm='',n=0) if not x.startswith(('---','+++'))]
    print(n,'diff hunks:',sum(1 for x in d if x.startswith('@@')))
print('VERBATIM_OK',ok)
# numeric
def fr(x): return x-(x.numerator//x.denominator)
def nd(x): f=fr(x); return min(f,1-f)
random.seed(20261019)
tests=fails=0
def rnd(lo,hi,den=997): return lo+(hi-lo)*F(random.randint(0,den),den)
def check(s,r,w):
    global tests,fails
    # choose b=1: c=r, then a=(b+c)/s, d=w(b+c)
    b=F(1);c=r;a=(b+c)/s;d=w*(b+c)
    if not(0<a<b<c<d) or not(4*a<d<4*c): return None
    t=1/(b+c) if F(1,5)<=fr(w)<=F(4,5) else F(3,2)/(b+c)
    m=min(nd(x*t) for x in(a,b,c,d)); tests+=1
    if t<=0 or m<F(1,5): fails+=1;print('FAIL',s,r,w,m)
    return m
pts=[]
for _ in range(200000):
    s=rnd(F(15,8),F(5)); r=1+rnd(F(0),F(1,7))
    if r==1: continue
    w=rnd(F(4,5),F(9,5)); check(s,r,w)
# endpoints
S=[F(15,8),F(5),F(3)]; R=[F(8,7),F(1)+F(1,1000),F(15,14)]; W=[F(4,5),F(1),F(6,5),F(9,5),F(11,10),F(9,10)]
for s in S:
  for r in R:
    for w in W: check(s,r,w)
# box-only endpoint tests (Omega ignored; the proof B3/B4 does not use Omega beyond w>4/s)
bt=0;bf=0
for s_ in [F(15,8),F(5),F(3),F(2)]:
  for r_ in [F(8,7),F(1001,1000),F(15,14),F(1,1)+F(1,10**6)]:
    for w_ in [F(4,5),F(1),F(6,5),F(9,5),F(401,500),F(599,500),F(601,500),F(11,10),F(9,10)]:
      b=F(1);c=r_;a=(b+c)/s_;d=w_*(b+c)
      if not(0<a<b<c<d): continue
      t=1/(b+c) if F(1,5)<=fr(w_)<=F(4,5) else F(3,2)/(b+c)
      m=min(nd(x*t) for x in(a,b,c,d)); bt+=1
      if m<F(1,5): bf+=1;print('BOXFAIL',s_,r_,w_,m)
print('BOX-ENDPOINT tests',bt,'failures',bf)
fails+=bf
print('NUMERIC tests',tests,'failures',fails)
sys.exit(0 if ok and fails==0 else 1)
