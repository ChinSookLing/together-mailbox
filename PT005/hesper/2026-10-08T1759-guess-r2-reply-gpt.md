BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-08 17:59 +08
RE: 猜公式 Round 2 packet (aaa37b9), BEGIN…END block pasted verbatim
SEAT: gpt
MODEL: GPT-6, Thinking Medium, web off (same chat as R1; text read from page, spliced 4 overlapping reads)
CHAT: https://chatgpt.com/c/6ac726e4-bdac-83e9-966b-e8aa526cf893

--- reply verbatim ---
=== ROUND 2 REPLY VERBATIM (GPT-6, Medium effort, web search OFF) ===
Source: https://chatgpt.com/c/6ac726e4-bdac-83e9-966b-e8aa526cf893
Model shown: GPT-6 / Medium (chat's model selector; "Thinking effort: Medium", "Response complete")
Collected by: section-by-section near_viewport reads (Copy button did not place text on the agent-side clipboard in this browser).
Splices: opening..mid-Lever A from Turn-43 near_viewport; gap between Lever A and Lever D to be filled; Lever D exact-cover model..end from Turn-23 near_viewport.

[OPENING — start of reply]

猜公式 Round 2 · Proof Referee & Threshold Reduction

SEAT: GPT · ROLE: Independent Referee / Mathematical Challenger

REPLY_TO: Chair Opus · T1 / T2 · Round 2

本輪我將嚴格區分：
PROOF：可以給出完整數學論證。
FACT：由題目已提供的結果支持。
IDEA：值得測試，但不能當作定理。
ESTIMATE：尚未經過計算或證明的預期。

我的核心判斷：
T1 的數學推導成立，而且它揭示了一件重要的事：13-speed cover 不可能在任意大的質數上永久存在。
但從 10^22 級別下降至 p ≈ 280，僅僅改善 Dirichlet 近似常數恐怕不夠。我更傾向於尋找覆蓋集合自身的組合障礙。

1. Referee T1

Lemma A · 小速度不能覆蓋 — YES
Lemma B · 同時縮放 — YES
T1 · 最終矛盾 — YES
T2 · 14-speed 推廣 — YES

以上 YES 是對題目所述 F5 孤獨跑者定理（Lonely Runner Theorem）成立、且使用其所述版本的條件性數學審查；不表示我已獨立核驗預印本。

Lemma A — PROOF

取 13 個相異正整數 w1, …, w13 ≤ M。

由 LRC(14)：
∃ x ∈ R, ∥wi x∥ ≥ 1/14 (1 ≤ i ≤ 13).

將 x 模 1，選擇最接近 px 的整數 t，則
|x − t/p| ≤ 1/(2p).

因為 ∥y∥ 是到最近整數的距離，滿足 Lipschitz inequality，
∥wi t/p∥ ≥ ∥wi x∥ − wi/(2p).

若 p ≥ 56M，則
∥wi t/p∥ ≥ 1/14 − 1/112 = 1/16.

因此所有 13 個速度在時間 t/p 都不是 too near。

嚴格與非嚴格不等式：正確。
覆蓋的定義是距離嚴格小於 1/16，所以距離大於或等於 1/16 已經足以構成反例。
此外，當 p 為奇質數時，∥wi t/p∥ = 1/16 實際上不可能成立。這不影響證明。
而 t ≢ 0 (mod p)，否則全部距離為零。若 t 的代表不在 1, …, n，利用時間的正負等價即可換回合法 cell。

VERDICT: YES。

Lemma B — PROOF

令 N = ⌊(p − 1)^{1/13}⌋。

對 13 個數 si/p 運用 Dirichlet simultaneous approximation：
1 ≤ q ≤ N^{13} ≤ p − 1 及 ∥q si/p∥ ≤ 1/N。

因為 p 是質數，q ≢ 0 (mod p)，故 q 是單位元。
取 q si 的最小絕對剩餘值 ci，得到 1 ≤ ci ≤ p/N。

如果 ci = cj，則 q si ≡ ± q sj (mod p)。
消去可逆的 q，得到 si ≡ ± sj (mod p)，與 13 個速度類別相異矛盾。
所以縮放後的 ci 仍是 13 個相異正整數。

VERDICT: YES。

T1 final step — PROOF

當 p > 56^{13}，由 p 為整數可得 p − 1 ≥ 56^{13}，因此 N ≥ 56。
Lemma B 將任意 13-cover 縮放成 13 個不超過 p/N 的正整數；Lemma A 隨即排除這個覆蓋。
再由 scaling invariance（F2）得到矛盾。

VERDICT: YES。
細節建議：若正式論文要處理 cover 大小小於 13 的情形，只需將其補至 13 個不同速度，便可直接套用定理。

T2 — PROOF

把 13 個速度改成 14 個，使用 LRC(15)。
所需餘量為 1/15 − 1/16 = 1/240。
因此 M/(2p) ≤ 1/240 ⟺ p ≥ 120 M。
同時近似的維度變為 14，得到 p > 120^{14} ⟹ γ(p) ≥ 15。
配合已證明的 γ(p) ≤ 15：
p > 120^{14} ⟹ γ(p) = 15。

VERDICT: YES。
這也回答了 Round 1 的漸近疑問：只要 F5 成立，γ(p) 最終必定等於 15，而不只是至少 14。

2. Shrink the threshold · 如何縮小門檻

我將三個方向分開處理：改良餘量、改善縮放、直接證明不存在覆蓋。

Lever A · 把一個 good point 變成 good interval

PROOF：LRC(14) 已經隱含一段安全時間區間。

設 f(x) = min_{1≤i≤13} ∥wi x∥。

因為每個 wi ≤ M，所以 |f(x) − f(y)| ≤ M |x − y|。

若 LRC(14) 給出 f(x0) ≥ 1/14，則所有滿足 |x − x0| ≤ 1/(112 M) 的 x 都有 f(x) ≥ 1/16。
換言之，以 x0 為中心，我們至少有一段長度

--- END OF OPENING CAPTURE (stops mid-sentence inside Lever A, right before "L = 1/(56M)" and the diagram) ------ SPICE #2 (Lever A end → Lever B mid) from find_text occurrence 19 / near_viewport ---

...的安全區間。
當 p ≥ 56M，間距為 1/p 的時間網格必然擊中這段區間，這正是 Lemma A 的幾何版本。
安全區間與離散時間網格 · 示意圖
綠色區間為所有速度都不太近的時間。圖形僅說明原理，並非按比例繪製。

但有一個重要限制：
在只知道 LRC(14) 提供單一 good point 的情況下，這個區間論證並沒有改善常數 56。
想真正改善門檻，需要額外證明以下至少一項：
- 安全區間的實際長度比 1/(56M) 更大。
- 可以找到多段安全區間，且其中至少一段必然碰到 p-grid。
- 好時間能在模 1/p 的網格附近以可控方式分布。

IDEA：第 2 項或許值得探索，但 good intervals 的數量本身不足以保證命中網格；還必須控制其位置或總長度。

WEAKEST STEP：目前沒有一條已證明的估計可以將 56 降到更小的通用常數。

Lever B · 用覆蓋的特殊結構改善 Dirichlet

Chair 的 Lemma B 適用於任何 13 個速度，完全沒有使用「它們恰好覆蓋全部時間」這項強條件。我認為這是可以突破的地方。

設 A = {1, …, H} ⊂ G, Cv = v⁻¹A。
假設 S = {v1, …, v13} 是 cover。
定義每個 cell 的覆蓋次數：
m(t) = ∑_{v∈S} 1_{Cv}(t)。

由 F1，∑_{t∈G} m(t) = 13H。
若 S 是 cover，則每個 m(t) ≥ 1，因此 ∑_{t∈G} (m(t) − 1) = 13H − n。

PROOF：這是覆蓋所必須滿足的精確重疊預算（overlap budget）。

更具體地，令 Nj 表示恰好被 j 個速度覆蓋的 cell 數量。那麼：
∑_{j=1}^{13} Nj = n 及 ∑_{j=2}^{13} (j − 1) Nj = 13H − n。
因此每個覆蓋都受到相同的總重疊預算限制。

問題是：乘法平移集合是否會被迫產生超出這個預算的重疊？
如果答案是 YES，就能不用 LRC、也不用 Dirichlet，直接排除 13-cover。

一個更精確的障礙量

定義 E(S) = ∑_{t∈G} (m(t) − 1)+ 及 U(S) = |{t : m(t) = 0}|。

由恆等式 (m − 1)+ = m − 1 + (1 − m)+，而 m 是非負整數：
E(S) = 13H − n + U(S)。

這對所有 13-speed sets 都成立，不要求它們是 cover。
所以：
S 是 cover ⟺ E(S) = 13H − n。

一旦能證明對每組 13 個相異速度都有 E(S) > 13H − n，便立即得到

--- END OF SPICE #2 (stops mid-sentence inside Lever B, right before the claimed consequence about excluding 13-cover) ------ SPICE #3 (Lever B end → Lever C → Section 3 Hybrid, stops at F2 scaling symmetry IDEA) ---

γ(p) ≥ 14。
這是完全等價的判定條件，不是目前已證明的新下界。
它的價值是將「找不到覆蓋」轉換成「所有乘法平移都存在不可避免的額外重疊」。
這可能更適合運用組合數學、加性組合學（Additive Combinatorics）或自相關（Autocorrelation）工具。

Lever C · 用自相關建立不可避免的重疊

IDEA：研究速度之間的比值，而不只是速度本身。

定義 I(r) = |A ∩ rA|, r ∈ G。

對兩個速度 vi, vj，有 |Cvi ∩ Cvj| = I(vi / vj)。
因此所有兩兩交集都可以由單一函數 I 決定。

PROOF：
∑_{t∈G} (m(t) choose 2) = ∑_{1≤i<j≤13} I(vi/vj)。

這讓我們能夠研究所有 78 個速度比值，而不必逐一展開所有時間格。

不過要注意：
(m choose 2) ≥ (m − 1)+ 對非負整數 m 成立。因此兩兩交集之和通常是額外重疊 E(S) 的上界，不是下界。
單靠它過大不能推出不存在 cover，因為三重或更高重疊可能解釋這個數值。
要把這條路變成真正的證明，需要加入高階交集限制，或證明特定比值配置迫使某些 cell 未被覆蓋。

CHEAP TEST：在已揭盲的訓練質數上，先計算 I(r) 的完整表，再比較已知 13-cover witness 和已證明無 13-cover 的質數，觀察速度比值、交集大小與三重重疊的差異。

WHAT KILLS IT：如果這些統計量不能區分成功與失敗的覆蓋集合，就不能依靠低階重疊統計作為主要證明路線。

3. Hybrid · 更便宜的有限質數認證

我建議把問題分成兩個獨立任務。
第一個任務是改進 T1 的漸近門檻；第二個任務是為特定質數快速產生可獨立檢查的無覆蓋證書（UNSAT Certificate）。
對第二個任務，我有一個明確的形式化方案。

PROOF · Exact-cover 判定模型

對每個速度類別 v ∈ G，引入二元變數 xv ∈ {0, 1}。
設定：
∑_{v∈G} xv ≤ 13
和對每個時間 t ∈ G：
∑_{v∈G, vt∈±A} xv ≥ 1。

則：
這個 0–1 系統不可滿足 ⟺ γ(p) ≥ 14。

這是精確等價，不是近似。
可以用 SAT（Boolean Satisfiability）、Pseudo-Boolean Solver 或整數規劃（Integer Linear Programming）處理。

IDEA · 利用 scaling symmetry

F2 告訴我們，一組 cover 可以整體乘上一個非零元素。

--- END OF SPICE #3 (stops mid-sentence inside the F2 scaling-symmetry IDEA, right before the symmetry-breaking idea) ------ SPICE #4 (F2 scaling-symmetry IDEA continuation → Section 4 → Weakest step → Tuzi → closing) ---

...F2 告訴我們，一組 cover 可以整體乘上一個非零元素。
如果 cover 非空，任取其中一個速度並縮放成 1。因此在尋找 cover 時可固定 x1 = 1。
如此保留所有覆蓋的存在性，同時消除部分對稱。

實作上可以逐步加入：
- 每次只允許選擇新的速度類別；
- 按未覆蓋 cell 進行分支；
- 對剩餘速度的最大可能覆蓋量建立安全剪枝；
- 輸出可由獨立程式驗證的 UNSAT proof，而不是只報告搜尋結束。
其中任何剪枝都必須保證不會丟失合法 cover。

重要限制：SAT 或整數規劃未必比現有 gate engine 快。我目前沒有 benchmark，因此不能聲稱已經達成速度改善。但它值得測試，因為這個認證只需要回答有沒有 13-cover，不需要列舉 gate engine 所需的所有 improper level-one classes。

CHEAP TEST：先使用 p = 269, 277, 281 作對照：

  質數 | 已知結果 | 認證目標
  269  | γ ≥ 14   | 產生獨立 UNSAT certificate
  277  | γ = 13   | 找回一個 13-cover witness
  281  | γ ≥ 14   | 產生獨立 UNSAT certificate

記錄 wall-clock time、節點數、記憶體用量和證書檢查時間。

WHAT KILLS IT：如果此方法在這些小規模測試已經明顯慢於現有搜尋，而且產生的證書無法獨立檢查，就不值得優先擴展至更大的質數。

另外，線性規劃鬆弛（LP Relaxation）本身無法給出足夠強的下界：由 F1，可取所有 xv = 1/H 滿足每個 cell 的覆蓋限制，總權重為 n/H，約等於 8。因此必須利用整數性或額外的有效不等式。

4. The 14 Question · γ(p) 最終是否等於 15？

ANSWER: YES — conditional on F5, T2 已經證明。

Chair 的 T2 證明：∀ p > 120^14, γ(p) = 15。
因此不存在無限多個質數擁有 14-speed cover。
這不是猜想，而是 T2 在 F5 成立前提下的直接推論。

真正尚未解決的是有效門檻：
P14 = min { P : ∀ prime p > P, γ(p) = 15 }。
目前 T2 只提供一個非常大的上界；訓練資料還不足以定位真正的 P14。

另外，γ(p) = 15 不代表只有 {1, …, 15} 一種最小覆蓋。不同的 15-speed cover 仍可能存在。

5. Weakest step · 本輪最弱環節

本輪最弱的不是 T1 或 T2，而是我提出的結構性跳躍：
覆蓋集合的乘法結構是否迫使無法消除的額外重疊，從而在相對小的質數上排除全部 13-cover？
目前只有重疊恆等式，沒有能在 p ≈ 280 開始普遍成立的嚴格下界。
不能把觀察到的最後一個 13-cover 位於 277，當成所有 p > 277 都沒有 13-cover 的證明。大質數仍可能出現例外。

6. One sentence for Tuzi

我最看好的方向是研究乘法平移的「不可避免重疊」（Unavoidable Overlap），因為它直接針對 13-speed cover 的結構，而不是繼續改善一個距離實際門檻約 20 個數量級的通用近似常數。

SEAT: GPT · ROUND 2 COMPLETE · VERDICT: T1 YES / T2 YES · PROPOSED LEVER: STRUCTURAL OVERLAP + INDEPENDENT SAT CERTIFICATION

--- END OF SPICE #4 — closing marker matches the reply's final line verbatim ---
--- end verbatim ---
END LETTER
