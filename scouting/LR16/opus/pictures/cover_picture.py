# Opus: picture of how 12 speed classes cover all 65 time classes at p = 131 (k = 15, bound 1/16).
# Columns: time classes ordered by discrete logarithm, so every speed's covered set is the SAME shape, shifted.
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
P = 131; n = 65
fold = lambda x: min(x % P, P - x % P)
g = next(g for g in range(2, P) if len({pow(g, k, P) for k in range(1, P)}) == P - 1)   # primitive root
order = []; x = 1
for k in range(n):
    order.append(fold(x)); x = x * g % P
pos = {c: i for i, c in enumerate(order)}
core = [1, 2, 8, 11, 18, 38, 40, 46, 47, 48, 56, 58]
cov = {v: {t for t in range(1, n + 1) if 16 * fold(t * v) < P} for v in core}
count = {t: sum(t in cov[v] for v in core) for t in range(1, n + 1)}
fp = fm.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")
fig, ax = plt.subplots(figsize=(13, 5.2), dpi=150)
for r, v in enumerate(core):
    for t in cov[v]:
        c = "#c0392b" if count[t] == 1 else "#2c3e50"
        ax.add_patch(plt.Rectangle((pos[t], r), 0.9, 0.8, color=c))
for t in range(1, n + 1):
    ax.text(pos[t] + 0.45, len(core) + 0.3, str(count[t]), ha="center", va="bottom", fontsize=6,
            color="#c0392b" if count[t] == 1 else "#555")
ax.set_xlim(-0.5, n + 0.5); ax.set_ylim(-0.5, len(core) + 1.4); ax.invert_yaxis()
ax.set_yticks([r + 0.4 for r in range(len(core))]); ax.set_yticklabels([f"速度类 {v}" for v in core], fontproperties=fp, fontsize=8)
ax.set_xticks([])
ax.set_xlabel(f"65 个时间类（按离散对数排列，原根 g = {g}）· 底下的数字 = 被几个速度盖住 · 红色 = 只被一个速度盖住（私有时间）", fontproperties=fp, fontsize=9)
ax.set_title("p = 131：12 个速度类盖住全部 65 个时间类——每一行是同一个形状，只是平移", fontproperties=fp, fontsize=12)
for s in ax.spines.values(): s.set_visible(False)
plt.tight_layout(); plt.savefig("p131_cover_picture.png")
print("generator", g, "all covered:", all(count[t] >= 1 for t in range(1, n + 1)),
      "private times:", sum(1 for t in count if count[t] == 1), "max overlap:", max(count.values()))
