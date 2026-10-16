import re,subprocess,difflib,json,sys
t=open('table_1016.txt',encoding='utf-8').read()
blocks=re.findall(r'^LINE (\d+)\n(.*?)^BEGIN TEXT\n(.*?)\nEND TEXT$',t,re.S|re.M)
B={int(n):(h,x) for n,h,x in blocks}
slip=open('/home/claude/together-mailbox/PT005/bridge/RELEASE').read()
post=[l.split()[:2] for l in slip.split("\nPOST:\n")[1].split("\nHOLD:\n")[0].splitlines()]
strip=re.compile(r"^(CARRIED_BY:|CARRIER:|SEND_TEXT:|\{CARRIER\}=|CHAT:|CHAT URL:|Chat URL:|对话网址|Source chat)")
urlre=re.compile(r"https?://[^\s)\]>]*?(grok\.com|chatgpt\.com|chat\.z\.ai|chat\.qwen\.ai|kimi\.ai|kimi\.com|gemini\.google\.com|chat\.deepseek\.com|lumo\.proton\.me)[^\s)\]>]*")
def git(h,p): return subprocess.run(['git','-C','/home/claude/together-mailbox','show',f'{h}:{p}'],capture_output=True).stdout.decode('utf-8','replace')
def norm(s): return [x.rstrip() for x in s.strip('\n').split('\n')]
# gather wall lines 568..856, merge splits by path
seq=[]
for n in range(568,857):
    if n not in B: print(n,"MISSING"); continue
    hdr,txt=B[n]
    first,_,body=txt.partition('\n')
    m=re.search(r'信箱提交 ([0-9a-f]{7,40}) (\S+ \S+ \+08(?:00)?) · (\S+?)(?: · .*)?$',first)
    typ=re.search(r'^TYPE: (.*)$',hdr,re.M); spk=re.search(r'^SPEAKER: (.*)$',hdr,re.M)
    if not m:
        # continuation of split?
        seq.append((n,None,None,txt,first,(typ and typ[1],spk and spk[1]))); continue
    seq.append((n,m[1],m[3],body,first,(typ and typ[1],spk and spk[1])))
# merge continuation parts
merged=[]
for x in seq:
    if merged and (x[1] is None or x[2]==merged[-1][2]): 
        p=merged[-1]; merged[-1]=(p[0]+[x[0]],p[1],p[2],p[3]+"\n"+x[3],p[4],p[5])
    else: merged.append(([x[0]],x[1],x[2],x[3],x[4],x[5]))
print("wall entries",len(merged),"slip POST",len(post))
paths=[m[2] for m in merged]
order_ok = paths==[p for h,p in post]
print("order equals slip:",order_ok)
if not order_ok:
    for i,(a,b) in enumerate(zip(paths,[p for h,p in post])):
        if a!=b: print("  first diff at",i,a,b); break
problems=[];report=[]
for (ns,h,p,body,first,ts),(hs,ps) in zip(merged,post):
    if h and not hs.startswith(h) and not h.startswith(hs[:len(h)]): problems.append((ns,"HASH",h,hs))
    src=git(hs,p)
    s2=[]
    for x in src.split('\n'):
        if strip.match(x.strip()): continue
        x=urlre.sub("[chat link removed]",x)
        x=x.replace("FROM: Hesper (carrier)","FROM: Hesper")
        s2.append(x)
    a=norm("\n".join(s2)); b=norm(body)
    if a!=b:
        d=[l for l in difflib.unified_diff(a,b,lineterm='',n=0) if not l.startswith(('---','+++','@@'))]
        report.append((ns,p,d))
print("entries differing from mechanical strip:",len(report))
for ns,p,d in report:
    print(f"== {ns} {p.replace('PT005/','')}")
    for l in d[:8]: print("   ",l[:160])
# scans on wall text
W="\n".join(B[n][1] for n in range(568,858) if n in B)
for k,r in {"email":r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}","csllanna":"(?i)csllanna","fullname":r"(?i)chin\s+sook|sook\s+ling","chaturl":urlre.pattern,"carry":r"(?i)carried by puck|puck-carried|puck carries|ERR_TUNNEL|CARRIED_BY"}.items():
    hits=re.findall(r".{0,40}(?:"+r+").{0,40}",W)
    print(k,len(hits)); [print("   ",h[:120]) for h in hits[:6]]
