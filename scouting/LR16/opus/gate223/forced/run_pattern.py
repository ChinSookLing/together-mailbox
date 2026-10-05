import json,subprocess,os,time,sys
from concurrent.futures import ThreadPoolExecutor
DEAD=time.time()+float(os.environ.get("BUDGET","480"))
cs=[json.loads(l)["core"] for l in open("cores.jsonl")]
done=set()
if os.path.exists("pattern.jsonl"): done={tuple(json.loads(l)["core"]) for l in open("pattern.jsonl")}
def job(C):
    if time.time()>DEAD or tuple(C) in done: return
    inp="".join("SURVIVOR base: "+" ".join(map(str,sorted(C+[a,b])))+" l2=0\n" for a in range(1,112) for b in range(a,112))
    out=subprocess.run(["./pattern223"],input=inp,capture_output=True,text=True).stdout
    pats=[l for l in out.splitlines() if l.startswith("PATTERN")]; tot=[l for l in out.splitlines() if l.startswith("TOTAL")][0]
    with open("pattern.jsonl","a") as f: f.write(json.dumps(dict(core=C,patterns=pats,total=tot))+"\n")
with ThreadPoolExecutor(2) as ex: list(ex.map(job,cs))
R=[json.loads(l) for l in open("pattern.jsonl")]
from collections import Counter
print(len(R),"of",len(cs),Counter(tuple(r["patterns"]) for r in R))
