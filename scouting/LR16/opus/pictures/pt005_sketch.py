# Opus: Proof Table 005 sketches, in the style of the PT001 sketches (CC BY 4.0).
# Left: the L7 shift criterion as a wheel mod 8.  Right: the prime "doors" for 16 runners and the log budget.
import math, json
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
BG, FG, DIM = "#14131a", "#e8e6f0", "#8a879a"
BLUE, ROSE, VIOLET, GOLD, GREY = "#3b6ea5", "#8e3a5c", "#5b4a8f", "#f2c14e", "#3a3846"
def isprime(n): return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
fig = plt.figure(figsize=(16, 8), dpi=110, facecolor=BG)
fig.suptitle("Proof Table 005 · sketches", color=FG, fontsize=20, y=0.97)
# ---------- left: mod-8 wheel ----------
ax = fig.add_axes([0.02, 0.10, 0.42, 0.78]); ax.set_facecolor(BG); ax.set_aspect("equal"); ax.axis("off")
cost = {0: 0, 1: 1, 2: 2, 3: 1, 4: 4, 5: 1, 6: 2, 7: 1}
col = {0: GOLD, 1: BLUE, 2: VIOLET, 4: ROSE}
for r in range(8):
    th1 = 90 - r * 45 + 22.5; th0 = th1 - 45
    ax.add_patch(Wedge((0, 0), 1.0, th0, th1, width=0.42, facecolor=col[cost[r]], edgecolor=BG, linewidth=3))
    mid = math.radians((th0 + th1) / 2)
    ax.text(1.12 * math.cos(mid), 1.12 * math.sin(mid), str(r), color=FG, ha="center", va="center", fontsize=15)
    ax.text(0.79 * math.cos(mid), 0.79 * math.sin(mid), f"{cost[r]}", color=BG if cost[r] == 0 else FG,
            ha="center", va="center", fontsize=16, fontweight="bold")
ax.text(0, 0.16, "mod 8", color=FG, ha="center", fontsize=20)
ax.text(0, -0.05, "a + 2b + 4c < 8", color=GOLD, ha="center", fontsize=15)
ax.text(0, -0.22, "one rule, no new level", color=DIM, ha="center", fontsize=11)
ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.45, 1.3)
ax.text(0, -1.30, "each speed costs its number: odd 1 · 2 mod 4 → 2 · 4 mod 8 → 4 · 0 mod 8 → free (gold)\n"
        "if the 15 costs add up to less than 8, a good time exists (ledger L7, Astra)", color=DIM, ha="center", fontsize=10)
# ---------- right: prime doors ----------
bx = fig.add_axes([0.50, 0.24, 0.47, 0.62]); bx.set_facecolor(BG); bx.axis("off")
small = {223: 65, 233: 117, 191: 260, 241: 936, 227: 8424, 211: 8515, 181: 17667, 229: 18346, 179: 83239,
         199: 105794, 197: 120627}
primes = [p for p in range(131, 760) if isprime(p)]
cols = 16
for i, p in enumerate(primes):
    x, y = i % cols, -(i // cols)
    if p == 239: fc = GOLD
    elif p == 131: fc = ROSE
    elif p in small: fc = VIOLET if small[p] > 1000 else BLUE
    elif p < 239: fc = "#24222c"
    else: fc = GREY
    bx.add_patch(plt.Rectangle((x, y), 0.86, 0.78, facecolor=fc, edgecolor=BG))
    bx.text(x + 0.43, y + 0.39, str(p), color=BG if p == 239 else FG, ha="center", va="center", fontsize=8)
bx.set_xlim(-0.2, cols); bx.set_ylim(-(len(primes) // cols) - 0.4, 1.0)
bx.text(cols / 2, 1.05, "prime doors for 16 runners (131 – 757)", color=FG, ha="center", fontsize=14)
bx.text(cols / 2, -(len(primes) // cols) - 1.1,
        "gold: closed and reproduced 3× (239) · rose: maths OK, ~700 M rows (131) · blue: ≤ 1,000 small covers (cheap?)\n"
        "violet: > 1,000 small covers (expensive) · darkest: not measured yet · grey: cost by model L6, not yet run",
        color=DIM, ha="center", fontsize=10)
# ---------- budget bar ----------
cx = fig.add_axes([0.53, 0.09, 0.41, 0.04]); cx.set_facecolor(BG); cx.axis("off")
need = 481.07; have = math.log(239)
cx.add_patch(plt.Rectangle((0, 0), need, 1, facecolor=GREY)); cx.add_patch(plt.Rectangle((0, 0), have, 1, facecolor=GOLD))
cx.set_xlim(0, need); cx.set_ylim(0, 1)
cx.text(0, 1.5, f"Σ log p needed: {need:.2f} (ledger L8)  ·  closed so far: log 239 = {have:.2f}", color=FG, fontsize=11)
fig.text(0.5, 0.015, "Opus · Tuzi and Affiliates · CC BY 4.0", color="#6b6878", ha="center", fontsize=9)
plt.savefig("pt005_sketches.png", facecolor=BG)
print("primes drawn", len(primes))
