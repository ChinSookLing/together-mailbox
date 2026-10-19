import sys,gzip,csv,json
sys.path.insert(0,"/home/claude/together-mailbox/PT005/opus/r43chk")
from own import open_children
rows=[l.rstrip("\n").split("\t") for l in open("puck/r47B/check/mislabel_list.tsv")][1:]
want={int(r[0]) for r in rows}
out=open(sys.argv[1],"a"); done={json.loads(l)["row"] for l in open(sys.argv[1])} if False else set()
with gzip.open("hesper/r45/widen/nodes_widen.csv.gz","rt") as f:
    rd=csv.reader(f); next(rd)
    for i,r in enumerate(rd):
        if i in want:
            M=int(r[2]); w=[int(x) for x in r[3].split()]
            out.write(json.dumps(dict(row=i,p=int(r[0]),M=M,n_open=len(open_children(w,M)),csv=int(r[10])))+"\n"); out.flush()
print("DONE",file=out)
