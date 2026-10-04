# TEST (Opus) of Qwen turn 16 (PT005), Test A: leave-one-out fit log T = A + B log p + C x on the author's K=14 costs
# (irredundant generation CPU-s, paper_v2 cost table). x = (k m - n)/n, m = floor((p-1)/(k+1)), n = (p-1)/2.
import numpy as np
T = [(239,1301),(241,4566),(307,14558),(353,24185),(397,57216),(449,70074),(499,260613),(521,236244),(547,444985),(557,573547),(563,499447),(569,351085)]
def x(p, k): n = (p-1)/2; m = (p-1)//(k+1); return (k*m - n)/n
p = np.array([t[0] for t in T], float); y = np.log([t[1] for t in T]); X = np.array([x(int(q),14) for q in p])
print("x14 table:", [(int(a), round(b,3)) for a,b in zip(p,X)])
M = np.c_[np.ones_like(p), np.log(p), X]
b = np.linalg.lstsq(M, y, rcond=None)[0]; r = y - M@b
print("full fit A=%.2f B=%.2f C=%.2f rms=%.3f" % (b[0], b[1], b[2], np.sqrt((r**2).mean())))
res = []; Cs = []
for i in range(len(p)):
    keep = np.arange(len(p)) != i
    bi = np.linalg.lstsq(M[keep], y[keep], rcond=None)[0]; Cs.append(bi[2]); res.append(y[i] - M[i]@bi)
print("LOO residuals:", [(int(a), round(float(e),3)) for a,e in zip(p,res)])
print("LOO rms = %.3f ; C range %.1f .. %.1f" % (np.sqrt(np.mean(np.square(res))), min(Cs), max(Cs)))
M0 = np.c_[np.ones_like(p), np.log(p)]; res0 = []
for i in range(len(p)):
    keep = np.arange(len(p)) != i
    bi = np.linalg.lstsq(M0[keep], y[keep], rcond=None)[0]; res0.append(y[i] - M0[i]@bi)
print("LOO rms without x = %.3f" % np.sqrt(np.mean(np.square(res0))))
for q in (239,241,251,263,307,367): print(q, "x15=%.3f" % x(q,15), "x14=%.3f" % x(q,14))
