# Opus: PT005 progress map — which prime doors are closed, running, planned (CC BY 4.0). Style as pt005_sketches.
import math
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
BG, FG, DIM = "#14131a", "#e8e6f0", "#8a879a"
GOLD, BLUE, VIOLET, GREY, DARK = "#f2c14e", "#3b6ea5", "#5b4a8f", "#3a3846", "#201f27"
NEED = 481.07
def isprime(n): return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
closed2 = {239: "L2", 223: "L10"}; closed1 = {233}; running = {401: "office PC", 191: "chair"}
cores = {223: 65, 233: 117, 191: 260, 241: 936, 227: 8424, 211: 8515, 181: 17667, 229: 18346, 179: 83239,
         199: 105794, 197: 120627}
plan = set(closed2) | closed1 | {191}
s = sum(math.log(p) for p in plan)
p = 239
while s <= NEED:
    p += 1
    if isprime(p) and p not in plan: plan.add(p); s += math.log(p)
pmax = max(plan)
primes = [q for q in range(131, 800) if isprime(q)]
fig = plt.figure(figsize=(16, 9), dpi=110, facecolor=BG)
fig.suptitle("Proof Table 005 · progress map · 16 runners", color=FG, fontsize=20, y=0.975)
ax = fig.add_axes([0.03, 0.27, 0.94, 0.62]); ax.set_facecolor(BG); ax.axis("off")
cols = 16
for i, q in enumerate(primes):
    x, y = i % cols, -(i // cols)
    if q in closed2: fc, tc = GOLD, BG
    elif q in closed1: fc, tc = BLUE, FG
    elif q in running: fc, tc = VIOLET, FG
    elif q in plan: fc, tc = GREY, FG
    else: fc, tc = DARK, "#5d5a6b"
    ax.add_patch(plt.Rectangle((x, y), 0.88, 0.80, facecolor=fc, edgecolor=BG))
    ax.text(x + 0.44, y + 0.50, str(q), color=tc, ha="center", va="center", fontsize=10, fontweight="bold" if q in plan else None)
    note = closed2.get(q) or ("1 machine" if q in closed1 else running.get(q)) or (f"{cores[q]} cores" if q in cores and q not in plan else "")
    if note: ax.text(x + 0.44, y + 0.18, note, color=tc, ha="center", va="center", fontsize=6.5)
rows = (len(primes) - 1) // cols
ax.set_xlim(-0.1, cols); ax.set_ylim(-rows - 0.3, 1.0)
# legend
lx = fig.add_axes([0.03, 0.17, 0.94, 0.06]); lx.axis("off"); lx.set_xlim(0, 10); lx.set_ylim(0, 1)
for k, (c, t) in enumerate([(GOLD, "closed · two machines · in ledger"), (BLUE, "closed · one machine"),
                             (VIOLET, "running now"), (GREY, f"planned, not started (up to {pmax})"),
                             (DARK, "not needed in this plan")]):
    lx.add_patch(plt.Rectangle(([0, 2.1, 3.8, 5.3, 7.6][k], 0.3), 0.25, 0.45, facecolor=c, edgecolor=GREY))
    lx.text([0, 2.1, 3.8, 5.3, 7.6][k] + 0.32, 0.52, t, color=FG, va="center", fontsize=9.5)
# budget bar
bx = fig.add_axes([0.06, 0.06, 0.88, 0.05]); bx.set_facecolor(BG); bx.axis("off")
segs = [(sum(math.log(q) for q in closed2), GOLD), (sum(math.log(q) for q in closed1), BLUE),
        (sum(math.log(q) for q in running), VIOLET)]
segs.append((NEED - sum(v for v, _ in segs), GREY))
x0 = 0
for v, c in segs:
    bx.add_patch(plt.Rectangle((x0, 0), v, 1, facecolor=c, edgecolor=BG, lw=1.5)); x0 += v
bx.set_xlim(0, NEED); bx.set_ylim(0, 1)
done = segs[0][0]
bx.text(0, 1.35, f"budget Σ log p: in ledger {done:.2f} · + one machine {segs[1][0]:.2f} · + running {segs[2][0]:.2f}"
        f"  of {NEED} needed  ({len(plan)} doors in this plan)", color=FG, fontsize=11)
fig.text(0.5, 0.012, "plan: the cheap small primes 191, 223, 233 replace the most expensive large ones · "
         "every door is one computer check that p divides the speed product · Opus · CC BY 4.0",
         color="#6b6878", ha="center", fontsize=9)
fig.savefig("pt005_progress_map.png", facecolor=BG)
print("plan doors", len(plan), "pmax", pmax, "sum", round(s, 2), "in ledger", round(done, 2))
