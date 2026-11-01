import subprocess,re,sys
B="/home/claude/lr16/code/bgk15"
def jobs(p):
    out=subprocess.run([B,str(p),"irroots"],capture_output=True,text=True)
    assert out.returncode==0, out
    nr=int(re.search(r"roots=(\d+)",out.stdout)[1]); S=set()
    for r in range(nr):
        o=subprocess.run([B,str(p),"irsubroots",str(r)],capture_output=True,text=True); assert o.returncode==0
        S|={(r,s) for s in range(int(re.search(r"subroots=(\d+)",o.stdout)[1]))}
    return nr,S
for p in map(int,sys.argv[1:]):
    nr,S=jobs(p); print(p,"roots",nr,"jobs",len(S))
