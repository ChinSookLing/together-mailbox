# PT005 · TEST-3 · Fable-A 回报（形状引理 shape lemma，Lean）

席位（seat）：Fable-A · 由 Tuzi 携带 · 主席（Chair）：Opus
**STATUS CLAIM: OPEN**（依协议：主席先读，Puck 再重跑）

## 1. 结果一览

| 步骤 | 内容 | 我这边的结果 | Lean 定理 |
|---|---|---|---|
| D1 | ∀ x ∈ (0,1]，a x > 8/5 | 通过编译 | `D1` |
| D2 | Case 2：至少两个坐标等于 1 ⟹ H u > 900 | 通过编译 | `D2` |
| D3 | L 在 (0, 3/35] 严格递减 | 通过编译 | `D3` |
| D4（stretch） | 化约 + 完整定理 | **通过编译，无遗留缺口** | `shape_lemma` |

**[FACT]** 完整陈述已被 Lean 接受：

```lean
theorem shape_lemma (u : Fin 15 → ℝ) (hu : ∀ i, 0 < u i ∧ u i ≤ 1) (hone : ∃ i, u i = 1) :
    H u > 900
```

其中

```lean
noncomputable def aR (x : ℝ) : ℝ := qR x / x ^ ((2 : ℝ) / 15)      -- 实数幂 Real.rpow
noncomputable def wR (x : ℝ) : ℝ := x ^ 2 / qR x
noncomputable def H (u : Fin 15 → ℝ) : ℝ := (∑ i, wR (u i)) * ∏ i, aR (u i)
-- qR x = 1 + 2 * x - x ^ 2 来自 PT005.lean
```

没有 INCOMPLETE 项。没有 `sorry`、`admit`、`native_decide`、新 `axiom`。11 条 `#print axioms` 全部只依赖 `[propext, Classical.choice, Quot.sound]`。

**这份文件没有覆盖的东西（请主席特别留意）**

- **[FACT]** 文件证明的是“H u > 900”。“H u > 900 等价于或推出 R_15 < 1/2”这一步**没有**形式化，Allikvere 的定理与乘积界也不在里面。
- **[FACT]** D4 的路线是我自己推导的，**不是**作者模板里的 (β, φ) 分析。我没有看到那份模板，所以没有引用它。Lean 检查的是我这条路线的每一步；它与作者论证是否一致，需要主席对照原文判断。

## 2. REPORT 字段

- **文件**：`PT005Shape.lean`（657 行，随附），`import PT005`，原文件未改动
- **sha256**
  - `PT005Shape.lean` = `9713a45e28cb67c8cbbcbc991bcfc43b87ba7257ac094b2921526a2d4fae2f0a`
  - `PT005.lean` = `d5c5d22e77311b74e753a9f3c54dcdfede26d4c68ff5a8773a045c8e77be7505`（与 test 2 相同）
- **命令**（两步）：
  1. `lake build PT005`（把已批准的文件编成可 import 的模块）
  2. `lake env lean PT005Shape.lean`
- **exit code**：`0`
- **运行时间**（第 2 步）：`real 0m43.138s / user 0m28.682s / sys 0m14.540s`（2026-10-04T17:20:21+08:00 开始，17:21:05 结束）
  第 1 步在我这边 `real 7m49.211s`，几乎全是容器读盘，`Build completed successfully (8476 jobs)`。
- **工具链**：Lean 4.30.0，Mathlib `c5ea00351c28e24afc9f0f84379aa41082b1188f`，项目文件（`lakefile.toml`、`lean-toolchain`）与 test 2 回报中列出的完全相同。

### 完整输出（full output）

```
'PT005.D1' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.D2' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.D3' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.crit_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.crit_small' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.H_eq_H1' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.H_gt_of_small' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.isCompact_Kset' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.continuousOn_H' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.H_gt_at_min' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.shape_lemma' depends on axioms: [propext, Classical.choice, Quot.sound]

real	0m43.138s
user	0m28.682s
sys	0m14.540s
exit=0
```

没有 error，也没有 warning。

## 3. 各步的陈述与路线

### D1 — `theorem D1 (x : ℝ) (h0 : 0 < x) (h1 : x ≤ 1) : aR x > 8/5`

**[FACT]** 用的是包里“避开精确根”的路线，再多切一刀，连 u2 也不需要：

| 区间 | 论证 |
|---|---|
| (0, 23/280] | 14x² − 13x + 1 ≥ 0，a 递减，a x ≥ a(23/280) |
| [23/280, 237/2800] | q 递增、x² ≤ h²，再用 **B3** |
| [237/2800, 3/8] | 14x² − 13x + 1 ≤ 0，a 递增，a x ≥ a(237/2800) |
| [3/8, 1] | a x ≥ q x ≥ q(3/8) = 103/64 > 8/5，不用导数 |

- **[FACT]** 导数：`hasDerivAt_ga`，d/dx (15·log a) = −2(14x² − 13x + 1)/(x·q)，与主席给的式子一致。
- **[FACT]** 没有用到 B2 和 √113。二次式在 23/280 和 237/2800 的符号由 Lean 直接算出（`quadR_nonneg_low`、`quadR_nonpos_mid`），内容上与 B2 等价。

### D2 — `theorem D2 (u) (hu : ∀ i, 0 < u i ∧ u i ≤ 1) (h2 : ∃ i j, i ≠ j ∧ u i = 1 ∧ u j = 1) : H u > 900`

**[FACT]** “至少两个坐标为 1”写成“存在两个不同的下标 i ≠ j”。证明：留下这两个坐标，其余 13 个因子用 D1 的 8/5，其余 13 个加项 ≥ 0 丢掉，得 H ≥ 4·(8/5)^13 > 1801（**B4**）。通用下界是 `H_two_lower`。

### D3 — `theorem D3 : StrictAntiOn LR (Ioc 0 (3/35))`

```lean
noncomputable def LR (x : ℝ) : ℝ := qR x * (1 - 13 * x + 14 * x ^ 2) / (15 * x ^ 2 * (1 + x))
```

**[FACT]** 这里我换了路线：纯代数，不用导数，所以**没有用到 B1 和那个五次式**。对 0 < x < y ≤ 3/35，

L x − L y = (y − x)·K / (15x²y²(1+x)(1+y))，K = (1+x)(1+y)(14x²y² − 12xy + x + y) − 56x²y²，

恒等式是 `LR_sub`，K > 0 由 y ≤ 3/35 的初等估计得到。主席给的 dL/dx 公式没有被形式化。

### D4 — 化约与组装

**[IDEA → 已由 Lean 检查]** 我的路线：

1. **小坐标**（`H_gt_of_small`）：若某个 u_j ≤ 1/200，则 a(u_j) > 2，配合一个等于 1 的坐标与 D1、B4，直接得 H > 900。所以只需看所有坐标 ≥ 1/200 的情形。
2. **极小点存在**（`isCompact_Kset`、`continuousOn_H`）：集合 K = {u : 每个 u_i ∈ [1/200, 1]，且某个 u_i = 1} 是紧的，H 在其上连续，取到最小值。只需证极小点处 H > 900（`H_gt_at_min`）。
3. 在极小点 u：
   - 若某坐标正好等于 1/200，回到第 1 步；
   - 若有两个坐标为 1，用 D2；
   - 否则恰有一个坐标 i0 为 1，其余都在 (1/200, 1) 内，每个坐标都是单变量局部极小点。
4. **临界点方程**（`crit_eq`）：对 x ↦ (w x + C)·(a x·Pr) 求导置零，得
   15x²(1+x) = S·q(x)·(14x² − 13x + 1)，S = Σ_i w(u_i)，也就是 L(x) = 1/S（`LR_eq_of_crit`）。
5. **坐标落在 (0, 3/35)**（`crit_small`）：因为 w ≤ 1/2，S − w(x) ≤ 7；而
   15x²(1+x) − (7q + x²)(14x² − 13x + 1) = 7(1 − x)(12x − 1)·q，在 x ∈ [3/35, 1) 上为正，与上式矛盾。
6. **全部相等**：这些坐标都满足 L = 1/S 且都在 (0, 3/35]，由 D3 的单射性相等。
7. **Case 3**（`H_eq_H1`）：一个坐标为 1、其余 14 个都等于 t 时 H u = H1 t，再用 test 2 的 `partC`。

“全部 u_i = 1”的情形已含在 D2 里，不需要单独处理。

### 用到了 test 2 的哪些结果

**[FACT]** B3（D1）、B4（D2 与小坐标情形）、`partC`（Case 3，因此间接用到 B5、B6）。B1、B2 在这个文件里没有用到。

## 4. 数值旁证（不属于证明）

**[ESTIMATE]** 浮点计算，仅用来确认形式化的量与预期一致：

- H1 的最小值约 944.96，在 t ≈ 0.072477 处；H(1, t, …, t) 与 H1(t) 在该点数值相同。
- a 在 (0,1] 上的最小值约 1.61525（8/5 的余量很小）。
- 20 万组随机点搜索到的 H 最小值约 2024.6，没有低于 900 的。

## 5. 过程记录（时间取自工具输出）

- 17:02:59 开始；`lake build PT005` 到 17:10:48 才结束（读盘慢）。
- 写 Lean 之前用 sympy 核对了三个代数恒等式（D3 的差公式、临界点方程、第 5 步的因式分解），都成立。
- 第 1 次编译（17:17:15，exit 1）：5 处错误，全是技术性的（B3/B4 从 ℚ 搬到 ℝ 的写法、紧集等式的一处 `simp`、两处隐式参数），另有 2 个弃用名警告。D1–D3 与 D4 的数学引理一次通过。
- 第 2 次编译（17:18:28，exit 1）：剩 B3/B4 搬运的 2 处。
- 第 3 次编译（17:19:24，exit 0）。
- 最终运行（17:20:21–17:21:05，exit 0），即上面哈希对应的文件。
- 总用时约 18 分钟（预算 60 分钟）。

## 6. 规则回应

- 来源：只读了 Tuzi 附上的包 `2026-10-04T1641-packet-Fable-A-test3-shape-lemma-Lean.md` 和我自己的 `PT005.lean`。没有凭记忆引用论文或作者模板。
- 没有搜索或阅读其他对话。
- 账户记录（account records）：没有打开任何记忆文件；系统自动提供的个人简介与文件名清单没有用到。
- 没有使用任何 key 或密码。
