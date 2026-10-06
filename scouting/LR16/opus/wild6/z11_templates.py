# Astra 34 (debate Γ) quotient test for the z = 11 layer: for each canonical 13-core C and each choice of 2 positions
# to be odd, u_k = c_k or c_k + p (parity as chosen); is there a good time T on the 2p grid (all ||T u_k/(2p)|| >= 1/16)?
# A template with NO good time gives w = (8u_1..8u_13, 1, 3): improper, 11 zeros mod 16, zeros not dominating.
import json, itertools, sys
def run(p, cores):
    M = 2*p; bad = []
    for C in cores:
        for i, j in itertools.combinations(range(13), 2):
            u = []
            for k, c in enumerate(C):
                want_odd = k in (i, j)
                u.append(c if (c % 2 == 1) == want_odd else c + p)
            if not any(all(16*min(T*x % M, M - T*x % M) >= M for x in u) for T in range(M)):
                bad.append((C, i, j, u))
    return bad
for p, f in ((223, "/home/claude/lr16/core223/cores.jsonl"), (233, "/home/claude/lr16/core233/cores.jsonl"),
             (191, "/home/claude/lr16/core191/cores.jsonl")):
    cores = [json.loads(l)["core"] for l in open(f)]
    bad = run(p, cores)
    print(f"p={p}: cores {len(cores)}, templates {78*len(cores)}, with NO good time: {len(bad)}", bad[:1], flush=True)
