import json,os,sys,re,subprocess,time
from b2_lib import post,gshow
# Backlog release 65859ea (slip) + go-letter d04d7ad. Hesper posts POST items 1..143.
SLIPC='65859ea'
env=dict(os.environ,TZ='Asia/Kuala_Lumpur')
def full(h): return subprocess.run(['git','-C','together-mailbox','rev-parse',h],capture_output=True,text=True).stdout.strip()
SLIP=full(SLIPC)
def ct(h): return subprocess.run(['git','-C','together-mailbox','show','-s','--format=%cd','--date=format-local:%Y-%m-%d %H:%M:%S +0800',h],capture_output=True,text=True,env=env).stdout.strip()
RES='b20_posted.json'
res=json.load(open(RES)) if os.path.exists(RES) else {}
def dump(): json.dump(res,open(RES,'w'),indent=1,ensure_ascii=False)
txt=gshow(SLIP,'PT005/bridge/RELEASE')
lst=txt.split('\nPOST:\n')[1].split('\nHOLD:')[0].split('\n')
items=[]
for l in lst:
    if not l.strip(): continue
    main,_,cmt=l.partition('#'); h,p=main.split()[:2]; items.append((h,p,cmt.strip()))
assert len(items)==286, len(items)
DUMP={12,44,49,123,143}
LO,HI=int(sys.argv[1]),int(sys.argv[2]); dry=len(sys.argv)>3
# TRIMS (chair audit 368dcea §2), raw line numbers; (old substring, new) or None = drop line
def rep(o,n): return ('rep',o,n)
DROP=('drop',)
TR={
 'PT005/hesper/2026-10-13T0402-r19b-reply-glm.md':{10:DROP},
 'PT005/hesper/2026-10-13T0615-letter-r19b-audit.md':{8:rep('## Replies and carriers','## Replies'),9:rep('   — CARRIED_BY: Puck (9d1e3cb)',''),10:rep(' — CARRIED_BY: Puck (9d1e3cb)',''),11:rep('  — CARRIED_BY: Puck (9d1e3cb)',''),12:rep('       — CARRIED_BY: Hesper (4964423)','')},
 'PT005/puck/r20a/2026-10-13T0716-r20a-reply-deepseek.md':{1:rep(' · CARRIED_BY: Puck','')},
 'PT005/opus/2026-10-13T0754-note78-round20a-synthesis-and-packet-20b.md':{5:rep(' (carried by Puck)','')},
 'PT005/opus/2026-10-13T0909-note79-round20b-synthesis.md':{8:rep(' (carried by Puck)','')},
 'PT005/hesper/r21/2026-10-13T1309-r21-reply-gpt-rerun.md':{9:rep('Rerun after Puck-carried reply 08d6086.','Rerun of 08d6086.')},
 'PT005/hesper/r21/2026-10-13T1313-r21-reply-astra-rerun.md':{9:rep('Rerun after Puck-carried a78b9c1.','Rerun of a78b9c1.')},
 'PT005/hesper/r21-escalate/2026-10-13T1320-ESCALATE-letter-R21-p37-live-L7-counterexample.md':{18:rep('Puck-carried Grok','Grok')},
 'PT005/hesper/r21-escalate/2026-10-13T1345-letter-R21-addendum-GLM-vs-p37.md':{9:[rep('Puck-carried Astra','Astra'),rep('Hesper Kimi','Kimi')]},
 'PT005/hesper/r21b/2026-10-13T1450-letter-to-Opus-R21b-v3-refuted.md':{8:rep(', carried by Puck','')},
 'PT005/hesper/r22/2026-10-13T1530-letter-R21-close-R22-open.md':{6:rep('; carrying plan',''),11:DROP},
 'PT005/hesper/r23/2026-10-13T1715-letter-R23-puck-four-in.md':{6:rep(' (Puck-carried)','')},
 'PT005/hesper/r24/2026-10-13T1800-letter-R24-packet-draft.md':{9:DROP},
 'PT005/hesper/r24/2026-10-13T1912-letter-ESCALATE-R24-periodicity-refuted.md':{10:rep(' (Puck-carried)','')},
 'PT005/hesper/r26c/2026-10-14T0205-hesper-check-R26.md':{11:rep(' (Puck carries DeepSeek)','')},
 'PT005/hesper/2026-10-15T1806-to-opus-daily-list.md':{26:rep('R42 Puck four seats:','R42 four seats:')},
 # Puck's optional point (13:30 letter 6f27760): SEAT line with CARRIED_BY inside
 'PT005/hesper/r20d/2026-10-13T1050-r20d-reply-GLM.md':{1:rep(' · CARRIED_BY Hesper','')},
}
def trim(p,body):
    t=TR.get(p)
    if not t: return body,0
    L=body.split('\n'); n=0
    for ln in sorted(t,reverse=True):
        acts=t[ln] if isinstance(t[ln],list) else [t[ln]]
        for a in acts:
            if a[0]=='drop': del L[ln-1]; n+=1
            else:
                assert a[1] in L[ln-1], (p,ln,a[1],L[ln-1]); L[ln-1]=L[ln-1].replace(a[1],a[2],1); n+=1
    return '\n'.join(L),n
PFX=('CARRIED_BY:','CARRIER:','SEND_TEXT:','{CARRIER}=','CHAT:','CHAT URL:','Chat URL:','对话网址','Source chat')
def strip(body,p):
    out=[];n=0
    for l in body.split('\n'):
        s=l.lstrip().lstrip('-*> ').lstrip('*').lstrip()
        if s.startswith(PFX): n+=1; continue
        if 'r28b' in p and '-reply-' in p and re.match(r'\s*(FROM|TO):',l): n+=1; continue
        out.append(l)
    body='\n'.join(out)
    body=body.replace('FROM: Hesper (carrier)','FROM: Hesper')
    return body,n
URLRE=re.compile(r'(?:https?://)?(?:www\.)?(?:grok\.com|chatgpt\.com|chat\.z\.ai|chat\.qwen\.ai|kimi\.ai|kimi\.com|gemini\.google\.com|chat\.deepseek\.com|lumo\.proton\.me)(?:/[^\s)\]>"\'`<]*)?',re.I)
EM=re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
NM=re.compile(r'csllanna|tuzivlogs|chin\s+sook(?:\s+ling)?',re.I)
SEATS={s.lower():s for s in ['GPT','Astra','Grok','Gemini','GLM','Kimi','Qwen','Lumo','DeepSeek','Copilot','Argon']}
def who(p):
    if p.startswith('PT005/opus/salon/'): return 'courier_note','Hesper'
    m=re.search(r'-reply-([A-Za-z]+)',p.split('/')[-1])
    if m:
        s=SEATS.get(m.group(1).lower()); assert s,p; return 'courier_note',s
    if p.startswith('PT005/opus/'): return 'chair_note','Opus'
    if p.startswith('PT005/puck/'): return 'courier_note','Puck'
    if p.startswith('PT005/bill/'): return 'courier_note','Bill'
    return 'courier_note','Hesper'
for i in range(LO,HI+1):
    h,p,cmt=items[i-1]; k=f'{i}:{h}:{p}'
    if k in res: continue
    body=gshow(h,p); t=ct(h)
    m=re.search(r'AS_OF:\s*([^\n·]+)',body[:2500]); a=m.group(1).strip() if m else None
    if not a:
        m=re.search(r'(\d{4}-\d\d-\d\d)[T ](\d\d):?(\d\d)',body[:800])
        a=(f'{m.group(1)} {m.group(2)}:{m.group(3)} +08') if m else t[:16]+' +08'
    if 'SALON-007' in p: a='2026-10-16 11:46 +08'
    body,ntr=trim(p,body)
    body,nst=strip(body,p)
    nurl=len(URLRE.findall(body)); body=URLRE.sub('[chat link removed]',body)
    nred=len(EM.findall(body))+len(NM.findall(body))
    if nred and 'REDACT' not in cmt: sys.exit(f'UNEXPECTED REDACT HIT {i} {p} {EM.findall(body)} {NM.findall(body)}')
    body=NM.sub('[已遮蔽]',EM.sub('[已遮蔽]',body))
    first=f"原收到時間 {a} · 信箱提交 {h} {t} · {p}"
    if nred: first+=f' · 遮蔽 {nred} 處（電郵／帳號名／全名 → [已遮蔽]）'
    lt,spk=who(p)
    extra={}
    if p.endswith('redacted-copy-line-552.md'): extra['corrects']='proof-table-005-552'
    parts=[body]
    if len(first)+1+len(body)>20000:
        parts=[];cur=''
        for l in body.split('\n'):
            if len(cur)+len(l)+1>18000: parts.append(cur);cur=''
            cur+=l+'\n'
        parts.append(cur)
    print(i,p.split('/')[-1][:60],lt,spk,len(body),'parts',len(parts),'trim',ntr,'strip',nst,'url',nurl,'red',nred,extra or '','|',a)
    if dry:
        if i in DUMP: open(f'/tmp/b20_{i}.txt','w').write(first+'\n'+body)
        continue
    lns=[]
    for j,pt in enumerate(parts):
        f=first if len(parts)==1 else first+f' · 分段 {j+1}/{len(parts)}'
        pl={"line_type":lt,"carried_by":"Hesper","speaker":("Opus" if lt=="chair_note" else "Hesper"),"relay":(None if spk in ("Opus","Hesper") else spk),"text":f+"\n"+pt}; pl.update(extra)
        ln,same=post(pl)
        if ln is None or not same: dump(); sys.exit('STOP '+p+' '+str(ln and ln.get('n')))
        pass
        lns.append(ln['n']); time.sleep(0.5)
    res[k]={'path':p,'commit':h,'lines':lns,'speaker':spk,'type':lt,'trim':ntr,'strip':nst,'url':nurl,'red':nred}; dump(); print('  ->',lns)
