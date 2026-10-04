# PT005 · TEST-2 · Fable-A 回报（Lean）

席位（seat）：Fable-A（testing seat）· 由 Tuzi 携带 · 主席（Chair）：Opus
**STATUS CLAIM: OPEN**（依协议：主席先读文件，再由 Puck 重跑）

## 1. 结果一览

| 部分 | 内容 | 我这边的结果 |
|---|---|---|
| PART A | A1–A5，精确有理数（ℚ） | 全部通过编译 |
| PART B | B1–B6，各自独立定理（ℚ） | 全部通过编译（含约 2,100 位的 B6） |
| PART C（可选） | 对所有实数 t ∈ (0,1)，H1(t) > 900 | **完整证出**（定理 `partC`），无遗留缺口 |

没有 INCOMPLETE 项。文件中没有 `sorry`、`admit`、`native_decide`、新 `axiom`。
29 条 `#print axioms` 全部只依赖 Lean 标准三公理 `[propext, Classical.choice, Quot.sound]`。

**这份回报没有覆盖的东西**：只形式化了包里列出的算术事实与那一个实数不等式。Allikvere Theorem 3.8 本身、乘积界（product bound）的推导、t_14 < 1/3、R_15 < 1/2 的形状引理（shape lemma）整体，都**不在**这个文件里。

## 2. REPORT 字段

- **文件**：`PT005.lean`（402 行，随附）
- **sha256**：`d5c5d22e77311b74e753a9f3c54dcdfede26d4c68ff5a8773a045c8e77be7505`
- **命令**：`lake env lean PT005.lean`
- **exit code**：`0`
- **运行时间**：`real 1m56.520s / user 0m15.448s / sys 0m54.270s`
  （开始 2026-10-04T15:57:17+08:00，结束 15:59:14+08:00；墙钟时间主要花在此容器载入 Mathlib 的 `.olean`，实际运算约 15 秒）
- **工具链**：`Lean (version 4.30.0, x86_64-unknown-linux-gnu, commit d024af099ca4bf2c86f649261ebf59565dc8c622, Release)`
- **Mathlib**：`lake-manifest.json` 中 `rev = c5ea00351c28e24afc9f0f84379aa41082b1188f`（与包一致），使用官方预编译 cache（8459 个文件）
- 其他哈希：`lake-manifest.json` = `a129f664fd6d5275bf1908c8269c2f34851bf51c0cf5e3ae440ff5c0d10e3258`；`lean-toolchain` = `54727eec5cba149c18842e6deb5c41b369d66455c93ce135d7d5347c782b2325`

### 完整输出（full output）

```
'PT005.A1' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.A2_lt' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.A2_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.A3_c13' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.A3_c14' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.A3_ratio' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.prod_c_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.A4' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.A5_lower' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.A5_attained' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.A5_gt' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.A5' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B1_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B1_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B2_gt' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B2_lt' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B3' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B4' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B5_lo' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B5_hi' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B6' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B5_lo_real' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B5_hi_real' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.B6_real' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.cubicR_mono' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.hasDerivAt_g' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.F_mid' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.F_gt' depends on axioms: [propext, Classical.choice, Quot.sound]
'PT005.partC' depends on axioms: [propext, Classical.choice, Quot.sound]

real	1m56.520s
user	0m15.448s
sys	0m54.270s
exit=0
```

没有 error，也没有 warning。

### 重跑所需的项目文件（给 Puck）

`lean-toolchain`：

```
leanprover/lean4:v4.30.0
```

`lakefile.toml`：

```toml
name = "pt005"
version = "0.1.0"
defaultTargets = ["PT005"]

[[require]]
name = "mathlib"
git = "https://github.com/leanprover-community/mathlib4"
rev = "c5ea00351c28e24afc9f0f84379aa41082b1188f"

[[lean_lib]]
name = "PT005"
```

步骤：`lake update`（会自动取 Mathlib cache）→ `lake env lean PT005.lean`。

## 3. 陈述与定理名对照（请主席逐条核对陈述是否忠实）

| 包里的陈述 | Lean 定理 | 备注 |
|---|---|---|
| A1: B 14 − 1/3 = 83/192 | `A1` | |
| A2: 391/960 < 83/192；B 13 ≤ 391/960 | `A2_lt`, `A2_le` | |
| A3: c′ 13 = 4/15, c′ 14 = 43/120 | `A3_c13`, `A3_c14` | |
| A3: c′(i+1)/c′ i > 4/3，i = 1..13 | `A3_ratio` | `∀ i ∈ Finset.Icc 1 13` |
| A4: ∏c′ / ∏c = 6192/4675 | `A4` | 两个乘积都取 `Finset.Icc 1 14`；另有 `prod_c_ne_zero` |
| A5: min c(i+1)/c i = 3751/2349 且 > 4/3 | `A5` | 以 `Finset.inf'` 表述；另拆成 `A5_lower`（下界）、`A5_attained`（在 i = 6 取到）、`A5_gt` |
| B1 | `B1_eq`, `B1_pos` | |
| B2 | `B2_gt`, `B2_lt` | |
| B3 | `B3` | |
| B4 | `B4` | |
| B5 | `B5_lo`, `B5_hi` | |
| B6 | `B6` | `norm_num` 直接完成 |
| C: ∀ t ∈ (0,1), H1(t) > 900 | `partC` | `theorem partC (t : ℝ) (h0 : 0 < t) (h1 : t < 1) : H1 t > 900` |

### 建模上的选择（modelling choices），请留意

1. `B` 的定义逐字照包：`def B (r : ℕ) : ℚ := ((2 * r : ℚ) / (16 * (16 - r)))^2`。其中 `16 − r` 是在 ℚ 里相减（不是自然数截断减法），由 `B_def`（`rfl`）明示。
2. `c i = B i − B (i−1)` 里的 `i − 1` 是自然数减法，只在 i ≥ 1 使用；`B_zero : B 0 = 0`，所以 `c 1 = B 1`。
3. `B'`：`if r = 13 then 391/960 else B r`；`c' i = B' i − B' (i−1)`。
4. PART B 在 ℚ 上陈述。PART C 在 ℝ 上，`H1` 用真正的实数幂（`Real.rpow`）：
   `H1 t = (1 + 2*t + 27*t^2) * (qR t)^13 / t ^ ((28:ℝ)/15)`。
   B5、B6 以 `exact_mod_cast` 搬到 ℝ（`B5_lo_real`, `B5_hi_real`, `B6_real`），所以 PART C 确实是站在 B5–B6 上面。

## 4. PART C 的证明路线

记 P(t) = 1 + 2t + 27t²，q(t) = 1 + 2t − t²，g(t) = 15·log P + 195·log q − 28·log t，F(t) = P^15·q^195 / t^28（即 H1 的 15 次方）。

1. `hasDerivAt_g`：在 (0,1) 上 g′(t) = 28·(1−t)·cubic(t) / (t·P(t)·q(t))，其中 cubic 正是包里的 378t³ + 25t² + 10t − 1。
2. `cubicR_mono`：cubic 在 [0,∞) 递增（代数恒等式，不用微积分）。
3. `g_lo_le`：由 B5 的 cubic(lo) < 0，g 在 (0, lo] 上递减；`g_hi_le`：由 cubic(hi) > 0，g 在 [hi, 1) 上递增。
4. `F_mid`：在 [lo, hi] 上，P、q 递增而 t^28 ≤ hi^28，所以 F(s) ≥ P(lo)^15·q(lo)^195 / hi^28 > 900^15，这一步就是 B6。
5. `F_gt` 把三段拼起来；`partC` 用 (t^(28/15))^15 = t^28 回到 H1。

路线不需要求出 cubic 的根 t* 本身，只用 lo、hi 两个端点。

## 5. 过程记录（时间全部取自工具输出）

- 15:44:40 开始；15:47:17 Mathlib 就绪。
- 写 Lean 之前，先用 Python 精确分数把包里每条陈述算了一遍，全部相符（A5 的最小值在 i = 6；B6 左右两边之比约 2.07，分子 2113 位、分母 2101 位）。
- 第 1 次编译（15:49:05，exit 1）：A1–A5、B1–B6 一次通过。唯一的错误出在我自己多加的一条辅助引理 `c_values`（包里没有，其中两个数值是我没算就写的），Lean 拒绝了，已整条删除。
- 第 2 次编译（15:53:55，exit 1）：加入 PART C，4 处战术（tactic）层面的错误（`convert` 的目标数、一处 `rw`）。
- 第 3 次编译（15:55:03，exit 0）。
- 第 4 次编译（15:57:17–15:59:14，exit 0）：加入 `B_def`、文件头说明、更多 `#print axioms` 后的最终版本，即上面哈希对应的文件。
- 总用时约 15 分钟（预算 60 分钟）。

## 6. 规则回应

- 引用来源：只读了 Tuzi 附上的包文件 `2026-10-04T1541-packet-Fable-A-test2-Lean.md`；没有凭记忆引用任何论文内容。
- 没有搜索或阅读其他对话。
- 账户记录（account records）：没有打开任何记忆文件。系统在本次对话开头自动提供了一段个人简介与记忆文件名清单，我没有读取其中任何文件，也没有用到。
- 没有使用任何 key 或密码。
- 注意：这次不是全新对话里贴入 BEGIN–END 区块，而是在同一对话里以附件形式收到包；内容以附件为准。
