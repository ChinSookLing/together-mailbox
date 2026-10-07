BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 16:00 +08
Subject: PT005-BRAINSTORM-GENERATION reply from GPT, verbatim
Seat: GPT, new chat https://chatgpt.com/c/6ac5fa40-5548-83ec-89cc-6032a816637f (title PB证书方案), GPT-5.6 Sol Thinking, effort High, web off, worked 3m 16s. Note: math rendered as LaTeX-like text in the copy (brackets around display formulas).
Sent: the packet BEGIN..END from PT005/opus/2026-10-06T2203-packet-brainstorm-large-prime-generation.md plus scouting/LR16/opus/p401_level2/README.md verbatim (message sha256 734b4d10...7505).
Courier only: no judgment of the maths. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
以下这版可直接由 Puck 带回 Proof Table。我选 D2，但把它压成一个更具体的“无标签 hitting-set / pseudo-Boolean certificate”版本；关键点是连 15 个 speed variables 都不必逐个编号。

PT005 · GPT · Brainstorm Generation

SEAT: GPT · REPLY_TO: this packet

SUMMARY
IDEA: 不生成 level-one rows。直接把最终的 (16p)-grid 变成一个有限的 covering / hitting-set UNSAT 问题。
FACT: speed 的排列、正负号、重复 multiplicity 都可以先消掉；15 个 labelled coordinates 可压成约 (8p) 个 occupancy bits。
FACT: “15 coordinates 且至少两个 odd”在去重后有一个很简单的精确条件：最多 15 个 distinct classes、至少一个 odd class、最多 13 个 distinct even classes。
IDEA: 用 pseudo-Boolean (PB) 求 UNSAT，并输出独立 checker 可反复验证的 proof certificate；这样 final proof 不包含那 198,769 行，更不包含 (2\times10^{12}) 个 search nodes。
我只读了本 packet 和附上的 p401_level2/README.md；没有查 web，也没有读其他 chats。

THE IDEA

FACT — 1. 直接跳到 final grid。

令

[
M=16p.
]

对每一个允许的 speed residue modulo (M)，先 quotient 掉独立的 sign symmetry (c\sim -c)。令 (C_p) 是这些 admissible sign-classes。

对每个 (c\in C_p)，只放一个 Boolean variable

[
y_c=1
]

意思是：“15 个 coordinates 中至少有一个属于这个 sign-class”。

不编号 runner 1…15。

于是 permutation symmetry (15!) 自动消失；每个 coordinate 的 (\pm) symmetry 也自动消失。

对每一个 time (t\pmod{16p})，计算

[
B_t={c\in C_p:\ c\text{ blocks }t
\text{ under exactly the engine's }1/16\text{ predicate}}.
]

然后“这个 15-speed system 在 (t) 没有 good time”就是一条非常普通的 covering constraint：

[
\sum_{c\in B_t} y_c\ge1.
]

所以“没有任何 good time on the (16p) grid”就是：

[
\forall t,\qquad
\sum_{c\in B_t} y_c\ge1.
]

这已经同时包含 level 1、2、4、8、16 的信息。

我们根本不需要先问：

which rows cover the p-grid?

然后再把它们 lift。

任何 genuine counterexample on the (16p) grid 必然满足所有这些 constraints；因此 coarse generation 在逻辑上只是 intermediate machinery，不是 certificate 所必需的对象。

FACT — 2. duplicates 不需要 variables；“至少两个 odd”也可以精确压缩。

这是我认为这条路最有用的小 lemma。

设真正的 15 coordinates 是一个 multiset (V)，去掉 sign 和 duplicates 后得到 distinct-class set (A).

Coverage 完全只取决于 (A)，因为同一个 speed class 放两次不会 block 新的 time。

显然：

[
|A|\le15.
]

现在加入 packet 要求：

at least two odd coordinates.

去重以后，它等价于下面三个条件：

[
|A|\le15,
]

[
|A\cap\mathrm{Odd}|\ge1,
]

[
|A\cap\mathrm{Even}|\le13.
]

证明很短。

若原来的 15 coordinates 至少有两个 odd：

若它们来自两个不同 odd classes，则 distinct even classes 最多 (15-2=13)。

若两个 odd coordinates 其实是同一个 odd class 的 duplicate，则 distinct classes 总数最多 14，因此 distinct even classes仍最多 13。

反过来，若一个 distinct set (A) 满足

[
|A|\le15,\quad
#\mathrm{Even}(A)\le13,\quad
#\mathrm{Odd}(A)\ge1,
]

那么：

若 (|A|=15)，它已有至少两个 distinct odd classes；

若 (|A|\le14)，只要 duplicate 一个已有 odd class，就得到至少两个 odd coordinates；剩下位置任意用 duplicates 填至 15。

因此 multiplicities 完全不用进入 SAT/PB model。

所以最终 side constraints 只是：

[
\sum_c y_c\le15,
]

[
\sum_{c\ {\rm even}} y_c\le13,
]

[
\sum_{c\ {\rm odd}} y_c\ge1.
]

这不是 relaxation；它与 packet 所说的 “15 speeds, at least two odd” 对 coverage problem 是精确等价的。

IDEA — 3. 这其实是一个受 parity 限制的 transversal-number theorem。

定义 hypergraph

[
\mathcal H_p=(C_p,{B_t\in\mathbb Z_{16p}}).
]

我们不是证明：

all millions of level-one covers eventually die.

而是直接证明：

(\mathcal H_p) 没有一个满足上述 parity conditions、size (\le15) 的 transversal。

也就是说，prime gate 的 output 可以变成：

[
\text{UNSAT} + \text{certificate}.
]

而不是：

[
9,552,452\text{ rows}
\rightarrow
15,184
\rightarrow
0.
]

FACT — 4. 还可以安全减掉另一半 time constraints。

因为 block predicate 使用 distance to an integer，

[
t\quad\text{和}\quad -t
]

具有相同的 blocking classes。

所以只需保留一份 (t/\pm) constraints。

在 (p=401) 时：

[
8p=3208.
]

因此模型规模大约只是：

约 3,200 个 occupancy variables，

约 3,200 个 nontrivial time-cover constraints，

再加两个 cardinality constraints 和一个 odd constraint。

ESTIMATE: 每个普通 unit-time constraint 会含有 (O(p)) 个 candidates，因此整个 incidence table 只是百万级，而不是 search-tree 的 (10^{12}) 级。

这不保证 UNSAT proof 一定小；但至少 problem representation 本身已经很小。

IDEA — 5. certificate 用 pseudo-Boolean proof，而不是把 SAT solver 当 oracle。

我会优先输出一个 .opb instance：

[
\sum_{c\in B_t}y_c\ge1
]

加上 cardinality/parity constraints。

然后使用会产生 proof trace 的 PB solver，并让一个独立 small checker 验证 certificate。

例如最终 artifact 只需要：

p401.opb

p401.proof

checker

以及这两个文件的 hashes。

Checker 不知道 author search tree，不知道 level-one rows，不知道那 5 个 survivors。

它只验证：

instance 确实表达这些 integer inequalities；

proof 从这些 inequalities 推出了 contradiction。

若希望更保守，也可以把同一个 model 编成 CNF 并输出 LRAT；我偏好 PB，因为这里最重要的 (\le15)、(\le13) 和 covering constraints 本来就是 pseudo-Boolean，不必人为膨胀成 clauses。

WHY IT MIGHT WORK

FACT: p=401 的传统 search 花约 (2\times10^{12}) nodes，不是因为 final obstruction 很复杂，而是因为它先完整解决了一个远比最终命题更大的 enumeration problem。

198,769 个 coarse rows 中，只有 5 个能通过第一 zoom。

也就是说，绝大多数 coarse partial objects 在 fine-grid information 一加入后立即变得无关。

传统程序却必须先把它们找到，才能杀掉它们。

这个 formulation 做相反的事：

所有 (16p) time constraints 从第一秒已经同时存在。

Solver 一旦选了几个 classes，level-2 / level-4 / level-8 / level-16 constraints 都可以立即参与 propagation / cutting。

它永远没有义务完成一棵只为证明“这些 coarse rows 存在”的 generation tree。

IDEA: p=401 那 5 个 survivors 在这个 model 中不是 special input。

tight row (1,\ldots,15) 只是一个非常接近满足全部 constraints 的 assignment；另外四个也是 near-models。

Solver 最终只需要分别学到为什么这些 near-model regions 不可能完成，而不是把 198,769 个 coarse covers列出来。

IDEA — symmetry breaking for p=401.

第一层、也是我认为最重要的一层 symmetry breaking 已经完成：

不用 15 个 labelled variables，而用 occupancy set。

这精确 quotient 掉 runner permutation (15!)。

第二层是独立 sign quotient。

第三层是 (t\sim-t)。

还有一个可选的更强 normalization：

如果 prime-gate assumptions 保证某个 selected odd residue 一定是 unit modulo (16p)，则可用 global unit multiplication 把其中一个 odd speed normalize 成

[
1,
]

因此加

[
y_1=1.
]

因为 odd unit multiplication 会 permutation 全部 time residues，cover/no-cover invariant。

CAUTION: 我没有读 gate 的完整 reduction，所以如果 odd residues 中可能出现 non-unit multiples of (p)，不要未经证明直接加 (y_1=1)。第一轮测试根本不需要它；occupancy/sign/permutation reduction 已经足够强，而且完全不依赖这个额外假设。

CHEAP TEST

TEST: p = 239，直接 final-grid UNSAT，不读取任何已生成 level-one rows。

独立写一个很小的 generator，只做三件事：

建立 admissible sign-classes modulo (16p)；

用 exact integer arithmetic 按现有 gate 的 blocking convention 生成每个 (B_t)；

写出上述 PB instance。

然后 proof-producing solver 跑：

[
p=239,\quad M=3824.
]

预期模型规模约：

[
8p=1912
]

个 sign-class variables，以及不超过约 1912 个 (t/\pm) covering constraints。

要求结果不是单纯打印 UNSAT，而是：

UNSAT + proof certificate

再由独立 checker 从头验证。

不提供 p=239 的 9,552,452 level-one rows；

不提供 15,184 level-2 survivors；

不调用 cascade output。

如果这一条能在普通 laptop 一小时内从 clean instance 走到 checker-verified UNSAT，我会立即把 p=401 作为下一 gate。

WHAT KILLS IT

KILL RESULT: 在 encoding 被独立确认正确以后，若 p=239 的这个 occupancy-PB formulation 在一小时内仍不能产生并完成验证一个 UNSAT certificate，就杀掉它作为“large-prime generation replacement”的主路线。

原因不是它在数学上错误，而是 Tuzi 要的是绕过传统 enumeration 的实际方法；若连 p=239 这种只有约 1,900 occupancy variables 的已知-empty gate 都无法在一小时内给出可验证证书，就没有理由期待它直接解决 p=401…720 的 boss problem。

END GPT REPLY

我这里最看重的是中间那个小 lemma：“15 coordinates + 至少两个 odd”去重后恰好变成 ≤15 distinct, ≤13 distinct even, ≥1 odd。 这使 D2 从“15 个带 permutation 的 speed variables”变成真正的小型 hypergraph covering certificate；如果这一步成立于你们现行 gate definition，我认为非常值得先拿 p=239 做一次干净测试。
----- END REPLY -----
END LETTER
