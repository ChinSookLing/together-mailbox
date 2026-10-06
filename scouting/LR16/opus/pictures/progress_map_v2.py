# Opus: PT005 progress map v2 (CC BY 4.0) — after the Γ debate (Kimi, Qwen, GPT, Astra, GLM feedback, chair note 34).
import math
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
BG, FG, DIM = "#14131a", "#e8e6f0", "#8a879a"
GOLD, BLUE, TEAL, VIOLET, GREY, DARK = "#f2c14e", "#3b6ea5", "#2f8f83", "#5b4a8f", "#3a3846", "#201f27"
NEED = 481.07
def isprime(n): return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
status = {239: ("ledger", "L2 · ~1.6 h"), 223: ("ledger", "L10 · ~2.4 h"),
          233: ("one", "1 machine · ~4.6 h"), 191: ("one", "1 machine · ~3.7 h"),
          241: ("part", "(a)(b) done · (c) 46/936"), 401: ("run", "office PC · ~26 h wall")}
cores = {179: 83239, 181: 17667, 197: 120627, 199: 105794, 211: 8515, 227: 8424, 229: 18346}
plan = {191, 223, 233, 241}
s = sum(math.log(p) for p in plan); p = 238
while s <= NEED:
    p += 1
    if isprime(p) and p not in plan: plan.add(p); s += math.log(p)
pmax = max(plan)
col = {"ledger": (GOLD, BG), "one": (BLUE, FG), "part": (TEAL, FG), "run": (VIOLET, FG)}
primes = [q for q in range(131, 800) if isprime(q)]
fig = plt.figure(figsize=(16, 10), dpi=110, facecolor=BG)
fig.suptitle("Proof Table 005 · progress map v2 · 16 runners", color=FG, fontsize=20, y=0.975)
fig.text(0.5, 0.925, "every door uses the author's method + L7 (HAND-CHECKED) · the forced-family converse is NOT needed by any door "
         "(chair note 34) · hours = chair-machine CPU", color=DIM, ha="center", fontsize=10)
ax = fig.add_axes([0.03, 0.30, 0.94, 0.60]); ax.set_facecolor(BG); ax.axis("off")
cols = 16
for i, q in enumerate(primes):
    x, y = i % cols, -(i // cols)
    if q in status: fc, tc = col[status[q][0]]; note = status[q][1]
    elif q in plan: fc, tc, note = GREY, FG, ""
    else: fc, tc = DARK, "#5d5a6b"; note = f"{cores[q]:,} cores" if q in cores else ""
    ax.add_patch(plt.Rectangle((x, y), 0.88, 0.80, facecolor=fc, edgecolor=BG))
    ax.text(x + 0.44, y + 0.52, str(q), color=tc, ha="center", va="center", fontsize=10,
            fontweight="bold" if q in plan else None)
    if note: ax.text(x + 0.44, y + 0.2, note, color=tc, ha="center", va="center", fontsize=6)
rows = (len(primes) - 1) // cols
ax.set_xlim(-0.1, cols); ax.set_ylim(-rows - 0.3, 1.0)
lx = fig.add_axes([0.03, 0.21, 0.94, 0.06]); lx.axis("off"); lx.set_xlim(0, 10); lx.set_ylim(0, 1)
items = [(GOLD, "in ledger (two machines)"), (BLUE, "closed, one machine"), (TEAL, "partly done"),
         (VIOLET, "running"), (GREY, f"planned (up to {pmax})"), (DARK, "not in this plan")]
xs = [0, 1.75, 3.45, 4.85, 6.0, 7.95]
for (c, t), x0 in zip(items, xs):
    lx.add_patch(plt.Rectangle((x0, 0.3), 0.22, 0.45, facecolor=c, edgecolor=GREY))
    lx.text(x0 + 0.3, 0.52, t, color=FG, va="center", fontsize=9.5)
bx = fig.add_axes([0.06, 0.09, 0.88, 0.045]); bx.set_facecolor(BG); bx.axis("off")
def L(kind): return sum(math.log(q) for q, (k, _) in status.items() if k == kind)
segs = [(L("ledger"), GOLD), (L("one"), BLUE), (L("part"), TEAL), (L("run"), VIOLET)]
segs.append((NEED - sum(v for v, _ in segs), GREY))
x0 = 0
for v, c in segs:
    bx.add_patch(plt.Rectangle((x0, 0), v, 1, facecolor=c, edgecolor=BG, lw=1.5)); x0 += v
bx.set_xlim(0, NEED); bx.set_ylim(0, 1)
bx.text(0, 1.35, f"Σ log p: in ledger {segs[0][0]:.2f} · one machine {segs[1][0]:.2f} · partly done {segs[2][0]:.2f} · "
        f"running {segs[3][0]:.2f} · needed {NEED}  ({len(plan)} doors in this plan)", color=FG, fontsize=11)
fig.text(0.5, 0.035, "the bar counts doors, not a partial proof: the theorem needs ALL doors of the plan; one missing door and nothing is proved.\n"
         "small primes 191, 223, 233 (below 239) replace the largest ones (727, 733, …) · Opus · CC BY 4.0",
         color="#8a879a", ha="center", fontsize=9)
fig.savefig("pt005_progress_map_v2.png", facecolor=BG)
print("plan", len(plan), "pmax", pmax, round(s, 2), [round(v, 2) for v, _ in segs])
