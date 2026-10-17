# PT005 R45 Track A - Puck's own program (second program). Full open subtrees from the SAME roots as Hesper's
# hesper_r45.py (roots copied as input only; the engine is Puck's own from r43f3/check/puck_f3_check.py, numpy
# packbits OR over 128x256 half-lifts; it does not import or reuse Hesper code).
# Definitions (R43/R44/R45 common): level M=2^k p; node = 15 ints in 1..M-1 (multiset); children at 2M = all 2^15
# choices w_i or w_i+M; covered T: some i with 16*||T w_i||_M < M; improper: all T in 1..M/2 covered and >=2 odd;
# L7-closed: some even D|M, |E_D|>=2, sum_{E_D} g_i*ceil((D/g_i)/8) < D; open = improper and not L7-closed.
# Depth d_i = k - v2(w_i) if v2(w_i)<k else 0; F0 = #{v2(w_i)>=k}; Fj = #{d_i>=j} (j=1..5).
# survival_depth: 0 = no open child; else 1 + max over open children. No level cap, no node cap except the two
# level-p p=17 roots that Hesper capped (replaced, as Hesper did, by their chain nodes at 2p/4p/8p).
import sys, os, json, glob, time, hashlib, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../r43f3/check'))
from puck_f3_check import open_children, open_direct, v2
D = '/workspace/mbx_pt5/PT005'
def roots():
    R = []
    R.append(("witnessA_p17", 17, 136, [1,3,3,5,7,8,18,22,40,55,69,75,87,105,110]))
    R.append(("witnessB_p17", 17, 136, [1,3,8,11,13,15,37,49,73,75,79,84,113,117,118]))
    R.append(("W5_p17", 17, 544, [189,224,72,447,176,500,144,128,384,266,80,64,48,32,16]))
    R.append(("GPT_p19_152", 19, 152, [39,59,41,61,43,101,121,8,47,125,145,15,73,55,37]))
    R.append(("Astra_p23_X_184", 23, 184, [10,26,28,56,78,94,95,99,100,121,122,142,146,162,172]))
    R.append(("R43_GPT_p47", 47, 47, [2,4,5,6,7,8,10,11,13,15,17,18,19,22,23]))
    R.append(("R43_Astra_p43", 43, 43, [2,5,5,6,8,9,13,14,16,16,17,18,19,20,21]))
    R.append(("R43_Grok_p17@2p", 17, 34, [8,11,11,15,3,5,15,11,7,16,1,15,16,3,13]))
    R.append(("R43_Grok_p17@4p", 17, 68, [8,11,11,49,37,5,15,11,7,50,1,15,16,3,13]))
    R.append(("R43_Grok_p17@8p", 17, 136, [8,113,11,49,37,73,83,11,75,50,1,15,16,3,13]))
    R.append(("R43_GPT_p47@2p", 47, 94, [49,51,5,6,7,55,57,11,13,62,17,18,19,69,23]))
    R.append(("R43_GPT_p47@4p", 47, 188, [143,51,5,6,7,149,57,11,107,62,17,112,113,163,23]))
    R.append(("R43_GPT_p47@8p", 47, 376, [143,51,193,194,195,149,245,199,295,62,205,112,113,351,23]))
    R.append(("R43_Astra_p43@2p", 43, 86, [2,5,9,13,16,19,48,49,51,57,59,60,61,63,64]))
    R.append(("R43_Astra_p43@4p", 43, 172, [2,13,16,48,49,51,91,95,105,143,145,146,147,149,150]))
    R.append(("R43_Astra_p43@8p", 43, 344, [2,13,16,49,91,105,143,146,220,223,267,317,319,321,322]))
    R.append(("R43_Astra_p17_X@2p", 17, 34, [1,1,3,3,3,5,6,7,7,8,8,18,19,21,22]))
    R.append(("R43_Astra_p17_Y@8p", 17, 136, [1,3,8,21,22,35,37,41,42,71,73,74,75,86,87]))
    R.append(("AstraR_p47_row", 47, 47, [1,2,3,5,6,8,9,10,11,12,13,14,15,20,21]))
    R.append(("seed20261016_p53", 53, 53, [3,5,6,7,8,9,11,14,15,17,21,23,26,26,26]))
    R.append(("seed20261016_p59", 59, 59, [1,4,5,5,6,7,11,16,17,18,20,21,23,28,29]))
    R.append(("seed20261016_p61", 61, 61, [1,2,5,6,11,11,12,14,16,18,23,26,27,29,30]))
    for f in sorted(glob.glob(D + '/hesper/proofmap/3/l30b/scan/scan_p*.json')):
        d = json.load(open(f)); p = d['p']; tag = os.path.basename(f)[5:-5]
        for j, n in enumerate(d['nodes']):
            R.append((f"l30b_scan_{tag}_{j}", p, 32 * p, n['w32p']))
    return R
def fvec(w, M, p):
    k = (M // p).bit_length() - 1
    d = [k - v2(x) if v2(x) < k else 0 for x in w]
    return [sum(1 for x in w if v2(x) >= k)] + [sum(1 for t in d if t >= j) for j in range(1, 6)]
if __name__ == '__main__':
    out = os.path.dirname(os.path.abspath(__file__))
    ch = {}; status = {}; labels = {}; t0 = time.time()
    R = roots()
    for lab, p, M, w in R:
        key = (p, M, tuple(sorted(w)))
        if not open_direct(list(key[2]), M): status[lab] = 'not_open'; print(lab, 'not_open', flush=True); continue
        stack = [key]
        while stack:
            k = stack.pop()
            s = labels.setdefault(k, set())
            if lab in s: continue
            s.add(lab)
            if k not in ch:
                kids, _ = open_children(list(k[2]), k[1])
                ch[k] = [(k[0], 2 * k[1], c) for c in kids]
            stack.extend(ch[k])
        status[lab] = 'done'; print(lab, 'done', len(labels), round(time.time() - t0), flush=True)
    surv = {}
    for k in sorted(labels, key=lambda k: -(k[1] // k[0])):
        surv[k] = 0 if not ch[k] else 1 + max(surv[c] for c in ch[k])
    rows = sorted(labels, key=lambda k: (k[0], k[1], k[2]))
    with open(out + '/puck_r45_nodes.csv', 'w') as f:
        f.write('p,k,M,coords,F0,F1,F2,F3,F4,F5,n_open_children,survival_depth,source\n')
        for k in rows:
            p, M, w = k
            f.write(f"{p},{(M//p).bit_length()-1},{M},{' '.join(map(str, w))},{','.join(map(str, fvec(w, M, p)))},{len(ch[k])},{surv[k]},{'|'.join(sorted(labels[k]))}\n")
    nl = ''.join(f"{p} {M} {' '.join(map(str, w))}\n" for p, M, w in rows)
    open(out + '/puck_r45_nodelist.txt', 'w').write(nl)
    print('NODES', len(rows), 'SHA256_NODELIST', hashlib.sha256(nl.encode()).hexdigest(), flush=True)
    print('STATUS', json.dumps(status), flush=True)
    print('SECS', round(time.time() - t0), flush=True)
