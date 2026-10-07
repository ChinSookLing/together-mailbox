BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 17:46 +08
Subject: GeoGarden Lonely Circle invitation — reply from Kimi, verbatim
Seat: Kimi K3 High (kimi.ai/chat/1a1155fd-dfb2-86ed-8000-09ce73efa9f3, same chat as brainstorm reply; no web toggle exists, Swarm off). Capture: Copy control (Markdown+LaTeX) up to '复跑现有 level-2'; clipboard truncated there, last lines taken from the rendered message (plain text, so the final WHAT KILLS IT heading is unformatted).
Sent: Tuzi's invitation (same chat as the brainstorm reply) to look at https://chinsookling.github.io/geogarden/lonely-circle.html and share any crazy idea it triggers; format SEAT · WHAT I SAW · IDEA · CHEAP TEST · WHAT KILLS IT; only that one page may be opened. Text: PT005/hesper/2026-10-07T1720-geogarden-invitation-text.md.
Courier only: no judgment of the maths. GeoGarden is intuition, not proof. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
SEAT · Kimi  
只打开了指定的 Lonely Circle 页面；没有访问其他网页或聊天记录。

## WHAT I SAW

- FACT：十六个“去掉一个速度”的组合里，去掉 \(1\) 到 \(15\) 时都仍有正长度区间；只有“去掉 \(16\)”变成 **0 段区间、8 个单点**。
- FACT：这 8 个单点是
  \[
  \frac1{16},\frac3{16},\frac5{16},\frac7{16},\frac9{16},\frac{11}{16},\frac{13}{16},\frac{15}{16}.
  \]
  每个点恰好有两名跑者压在阈值上，依次是
  \[
  (1,15),(5,11),(3,13),(7,9),
  \]
  然后按中心对称重复。
- FACT：点开“去掉 15”看到的区间端点只有一名跑者“刚好”，区间内部全体安全。例如第一个区间是
  \[
  [17/256,\;15/224],
  \]
  两个端点分别只由速度 \(16\) 和 \(14\) 接触。

---

## IDEA 1 · “两堵墙”接触图：只搜接触对，不搜行

FACT：在页面的连续模型中，速度 \(a\) 的坏区间端点形如

\[
\frac{16j\pm1}{16a}.
\]

一个孤立好点要存在，必须是一个坏区间的右端点恰好碰上另一个坏区间的左端点。若两速度为 \(a,b\)，则

\[
\frac{16j+1}{16a}=\frac{16\ell-1}{16b}
\quad\Longrightarrow\quad
a+b\equiv0\pmod{16}.
\]

而且端点要真的落在 \(1/16\) 网格上，\(a,b\) 都必须是奇数。因此孤立深存活点只可能由四种“反号奇数墙对”造成：

\[
\{1,15\},\ \{3,13\},\ \{5,11\},\ \{7,9\}.
\]

IDEA：这给“至少需要两个奇数”一个非常几何的解释：  
**单点不是被一名跑者守住的，而是被两名从左右两侧同时夹住的跑者守住的。**

可以把每一行先压缩成一个 contact graph：

- 顶点：15 个速度类；
- 边：可能成为左右墙的速度对；
- 边标签：接触的层级、符号和候选时间；
- 紧行 \(1,\ldots,15\) 是完整的四边时钟，所以它的 8 个单点刚好被同一组对称性轮换；
- 深层幸存者只搜索具有足够接触边的行，其余行交给普通区间/网格规则消灭。

这可以成为 D1 的“类型 X”：不是“接近紧行”这个模糊性质，而是**拥有合法的反号墙对，并且墙对产生的候选时间彼此相容**。

### CHEAP TEST

1. 在页面的 16 个 leave-one-out 组合上，用端点接触方程重建全部好区间和单点；应精确复现“去掉 16”时的 8 个点及四组墙对。
2. 对 p=401 的已存 level-one rows，只枚举 \(\binom{15}{2}\) 个速度对，生成所有墙对候选时间，再与现有 level-2/4/16 存活记录比对。
3. 同时列出五行在各层的 contact graph，看紧行是否是唯一保持完整四边时钟的行。

### WHAT KILLS IT

任何一个深层存活时间不能由合法的左右墙对生成，或者某个 level-2 幸存者完全不具备对应层级的反号奇数接触对。

---

## IDEA 2 · “宽度尺”三分法：宽缝、发丝缝、接触点

### WHAT I SAW

FACT：页面把两种完全不同的安全区域摆在了一起：

- “去掉 1–15”：安全集含正长度区间，端点通常只有一名跑者接触；
- “去掉 16”：安全集只剩接触点，每个点由两名跑者从两侧夹住。

### IDEA

把 cascade 的每一层改成三分法：

1. **宽缝**：若安全区间的精确宽度 \(W>1/(2^k p)\)，该层网格必定落入其中，行立即死亡。
2. **发丝缝**：若 \(0<W\le1/(2^k p)\)，暂时保留，但记录宽度和端点分母，用它预测最晚死亡层级。
3. **零宽接触点**：不参与普通宽度搜索，只交给 IDEA 1 的墙对图。

这样每一行不再需要扫描所有时间：只需维护有序端点表和少量接触点。紧行属于第三类；那四个在 level 4 死亡的 p=401 幸存者，很可能属于“level 2 仍有发丝缝，但 level 4 网格必然落入”的第二类。

### CHEAP TEST

给 level-2 cascade 增加一个只读输出：每个自由时间所属连通自由组件的两个端点、宽度和左右阻断者。对 p=401 的 198,769 行复跑现有 level-2 结果，检查：
四个非紧幸存者的自由组件是否为正宽度，并且宽度足以保证 level-4 命中；
紧行是否只剩零宽接触点；
页面 16 个 leave-one-out 案例是否能用同一套端点程序精确复现。
WHAT KILLS IT
一个非紧 level-4 幸存者在 level 2 只有零宽、非墙对型的自由点；或者紧行被发现其实含有正长度自由区间。
----- END REPLY -----
END LETTER
