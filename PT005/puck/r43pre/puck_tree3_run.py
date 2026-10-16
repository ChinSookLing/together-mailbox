# Puck: independent rerun for Hesper pre-R43 letter a2d179e (p=53 row). Uses puck_tree2.run (own code).
import sys, json
from puck_tree2 import run
from puck_tree import cov, L7
rows={53:[3,5,6,7,8,9,11,14,15,17,21,23,26,26,26],59:[1,4,5,5,6,7,11,16,17,18,20,21,23,28,29],61:[1,2,5,6,11,11,12,14,16,18,23,26,27,29,30]}
def improper(w,M):
    return all(any(cov(t,x,M) for x in w) for t in range(1,M//2+1))
if __name__=="__main__":
    p=int(sys.argv[1]); w=rows[p]
    print(json.dumps({"p":p,"row":w,"root_improper":improper(w,p),"root_L7":L7(w,p)}),flush=True)
    d=run(f"Hesper-seed row p={p}",w,p,p,128*p)
    json.dump(d,open(f"dead3_p{p}.json","w"))
