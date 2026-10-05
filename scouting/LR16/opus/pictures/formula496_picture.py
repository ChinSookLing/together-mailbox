# Opus: "Why exactly 496,000?" picture for PT005 chair note 30 (CC BY 4.0). Same style as pt005_sketches.
import math, json
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
BG, FG, DIM = "#14131a", "#e8e6f0", "#8a879a"
BLUE, ROSE, VIOLET, GOLD, GREY = "#3b6ea5", "#8e3a5c", "#5b4a8f", "#f2c14e", "#3a3846"
p, n = 223, 111
lg = {pow(3, k, p): k for k in range(p - 1)}
Dbar = sorted({lg[r] % n for r in range(1, p) if 16 * min(r, p - r) < p})
core = json.loads(open("/home/claude/lr16/core223/cores.jsonl").readline())["core"]
cov = [[(d - lg[s]) % n for d in Dbar] for s in core]          # time classes (log order) each speed covers
mult = [0] * n
for c in cov:
    for t in c: mult[t] += 1
assert min(mult) >= 1

fig = plt.figure(figsize=(18, 7.6), dpi=110, facecolor=BG)
fig.suptitle("Proof Table 005 · why every core gives exactly 496,000", color=FG, fontsize=20, y=0.975)

# ---------- A: 13 shifted copies of one shape cover the whole circle ----------
ax = fig.add_axes([0.005, 0.06, 0.33, 0.82]); ax.set_facecolor(BG); ax.set_aspect("equal"); ax.axis("off")
for k, c in enumerate(cov):
    R = 0.42 + 0.038 * k
    for t in range(n):
        a = math.pi / 2 - 2 * math.pi * t / n
        on = t in c
        ax.add_patch(Circle((R * math.cos(a), R * math.sin(a)), 0.011 if on else 0.004,
                            color=BLUE if on else GREY, lw=0))
Rout = 0.42 + 0.038 * 13 + 0.06
for t in range(n):
    a = math.pi / 2 - 2 * math.pi * t / n
    ax.add_patch(Circle((Rout * math.cos(a), Rout * math.sin(a)), 0.016, color=GOLD, lw=0))
ax.text(0, 0.10, "13 speeds", color=FG, ha="center", fontsize=17)
ax.text(0, -0.04, "each = the same shape,", color=DIM, ha="center", fontsize=11)
ax.text(0, -0.14, "shifted (discrete-log order)", color=DIM, ha="center", fontsize=11)
ax.text(0, -1.22, "A · inner rings: one speed each (blue = time classes it blocks)\n"
        "outer gold ring: all 111 time classes blocked —\nthe 13 speeds alone leave no good time",
        color=DIM, ha="center", fontsize=10)
ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.4, 1.12)

# ---------- B: the frozen 13 and the 8x8 free choices ----------
bx = fig.add_axes([0.355, 0.06, 0.30, 0.82]); bx.set_facecolor(BG); bx.set_aspect("equal"); bx.axis("off")
for i in range(13):                                   # 13 frozen runners: ≡ 0 mod 16
    bx.add_patch(Rectangle((i * 0.62, 6.35), 0.52, 0.52, facecolor=GOLD, edgecolor=BG))
    bx.text(i * 0.62 + 0.26, 6.61, "0", color=BG, ha="center", va="center", fontsize=10, fontweight="bold")
bx.text(4.0, 7.2, "13 core runners: speed ≡ 0 (mod 16) → frozen", color=FG, ha="center", fontsize=12)
odd = list(range(1, 16, 2))
x0, y0, s = 1.0, 0.3, 0.68
for i, a in enumerate(odd):
    for j, b in enumerate(odd):
        bx.add_patch(Rectangle((x0 + i * s, y0 + j * s), s - 0.06, s - 0.06, facecolor=ROSE, edgecolor=BG))
    bx.text(x0 + i * s + s / 2 - 0.03, y0 - 0.25, str(a), color=DIM, ha="center", fontsize=9)
    bx.text(x0 - 0.25, y0 + i * s + s / 2 - 0.03, str(a), color=DIM, ha="right", va="center", fontsize=9)
bx.text(x0 + 4 * s, y0 - 0.75, "runner 14: odd speed mod 16", color=DIM, ha="center", fontsize=10)
bx.text(x0 - 0.75, y0 + 4 * s, "runner 15", color=DIM, ha="center", va="center", rotation=90, fontsize=10)
bx.text(x0 + 4 * s, 5.85, "8 × 8 = 64 ways for the other two — none helps", color=FG, ha="center", fontsize=12)
bx.text(4.0, -1.55, "B · forced-family lemma: if the frozen speeds already block every time class,\n"
        "the free runners cannot open a gap.  Each of these 64 is then killed by L7 at D = 4",
        color=DIM, ha="center", fontsize=10)
bx.set_xlim(-1.2, 8.8); bx.set_ylim(-2.0, 7.7)

# ---------- C: the count, then predictions vs measurement ----------
cx = fig.add_axes([0.70, 0.50, 0.29, 0.36]); cx.set_facecolor(BG); cx.axis("off")
cx.text(0.0, 0.95, "496,000 = 64 × 7,750", color=GOLD, fontsize=22, fontweight="bold", transform=cx.transAxes)
rows = [("neither extra class in the core", "4,851", "× 1"), ("one extra class in the core", "1,274", "× 2"),
        ("same class twice, in the core", "13", "× 3"), ("two core classes", "78", "× 4")]
for k, (lab, num, w) in enumerate(rows):
    y = 0.70 - 0.15 * k
    cx.text(0.0, y, lab, color=FG, fontsize=11.5, transform=cx.transAxes)
    cx.text(0.80, y, num, color=FG, fontsize=11.5, ha="right", transform=cx.transAxes)
    cx.text(0.84, y, w, color=DIM, fontsize=11.5, transform=cx.transAxes)
cx.text(0.0, 0.06, "4,851 + 2·1,274 + 3·13 + 4·78 = 7,750 · the same for all 65 cores",
        color=DIM, fontsize=10, transform=cx.transAxes)

dx = fig.add_axes([0.725, 0.12, 0.26, 0.30]); dx.set_facecolor(BG)
labels = ["223\n(all 65)", "233\ncore 0", "233\ncore 58", "191\ncore 0", "191\ncore 130"]
meas = [496000, 536640, 544960, 383616, 390592]
simple = [496000, 536640, 536640, 376704, 376704]
xs = range(len(labels))
dx.scatter(xs, [m / 1000 for m in meas], s=110, color=GOLD, zorder=3, label="measured (= refined formula)")
dx.scatter(xs, [m / 1000 for m in simple], s=110, facecolor="none", edgecolor=FG, lw=2, zorder=4,
           label="simple formula, written down first")
dx.set_xticks(list(xs)); dx.set_xticklabels(labels, color=DIM, fontsize=9)
dx.tick_params(colors=DIM); dx.set_ylim(360, 610); dx.set_ylabel("lifts per core (thousands)", color=DIM, fontsize=9)
for sp in dx.spines.values(): sp.set_color(GREY)
dx.grid(axis="y", color=GREY, lw=0.6, alpha=0.6); dx.set_axisbelow(True)
dx.legend(loc="upper right", fontsize=8.5, facecolor=BG, edgecolor=GREY, labelcolor=FG)
dx.set_title("C · predictions made before the runs", color=FG, fontsize=11, loc="left")
fig.text(0.855, 0.015, "refined formula: 64 × #(row, covering 13-subset) — 5 of 5 exact",
         color=DIM, ha="center", fontsize=9.5)
fig.savefig("pt005_496000_picture.png", facecolor=BG)
print("ok")
