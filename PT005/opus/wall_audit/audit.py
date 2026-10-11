import re,subprocess,sys
lo,hi=int(sys.argv[1]),int(sys.argv[2])
t=open('table.txt',encoding='utf-8').read()
blocks=re.findall(r'^LINE (\d+)\n(.*?)^BEGIN TEXT\n(.*?)\nEND TEXT$',t,re.S|re.M)
B={int(n):(h,x) for n,h,x in blocks}
fails=0; seen=set()
for n in range(lo,hi+1):
    if n not in B: print(n,'MISSING'); fails+=1; continue
    hdr,txt=B[n]
    typ=re.search(r'^TYPE: (.*)$',hdr,re.M).group(1); spk=re.search(r'^SPEAKER: (.*)$',hdr,re.M).group(1)
    first,_,body=txt.partition('\n')
    if n==lo and '信箱提交' not in first:
        print(n,'OPENING',typ,spk); print(txt); continue
    m=re.search(r'信箱提交 ([0-9a-f]{40}) (\S+ \S+ \+08) · (\S+)$',first)
    if not m: print(n,'BAD FIRST LINE',first[:200]); fails+=1; continue
    h,ct,path=m.groups()
    try: src=subprocess.run(['git','-C','/home/claude/together-mailbox','show',f'{h}:{path}'],capture_output=True,check=True).stdout.decode('utf-8')
    except Exception as e: print(n,'GIT FAIL',path); fails+=1; continue
    ok = body==src or body==src.rstrip('\n') or body.rstrip('\n')==src.rstrip('\n')
    exact = body==src
    # commit time check
    gct=subprocess.run(['git','-C','/home/claude/together-mailbox','show','-s','--format=%cd','--date=format-local:%Y-%m-%d %H:%M',h],capture_output=True,text=True,env={'TZ':'Asia/Kuala_Lumpur'}).stdout.strip()
    # file added in this commit?
    added=subprocess.run(['git','-C','/home/claude/together-mailbox','show','--diff-filter=A','--name-only','--format=',h],capture_output=True,text=True).stdout.split()
    want=('chair_note','Opus') if path.startswith('PT005/opus/') else ('courier_note','Hesper')
    flags=[]
    if not ok: flags.append('TEXT MISMATCH')
    elif not exact: flags.append('trailing-newline-only')
    if (typ,spk)!=want: flags.append(f'TYPE/SPEAKER {typ}/{spk}')
    if not ct.startswith(gct): flags.append(f'TIME {ct} vs git {gct}')
    if path not in added: flags.append('path not added in that commit')
    if path in seen: flags.append('DUPLICATE')
    seen.add(path)
    if re.search(r'SEALED-KEY|do-not-forward',path) or not path.endswith('.md'): flags.append('NEVER-POST?')
    if re.search(r'ghp_[A-Za-z0-9]{20}|github_pat_|-----BEGIN',body): flags.append('SECRET-PATTERN')
    if flags: fails+= any(f!='trailing-newline-only' for f in flags)
    print(n, 'OK' if not flags else ', '.join(flags), path.split('/')[-1][:60])
print('lines',hi-lo+1,'problems',fails)
