BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:22 +08
RE: 猜公式 Round 17 literature walk (packet ad54489), send text r17_send_full.txt or r17_send_short.txt
SEAT: gpt
MODEL: GPT-6 Thinking High, web search (label shows 'Thinking effort High')
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ac97e4e-95c0-83ec-bfde-afaf19d7ade8

--- reply verbatim ---
[Hesper capture note: ChatGPT Copy returned empty; reply captured page-text in 3 overlapping sections, joined at marked seams; overlap text may repeat once at a seam. Seat answered as 'Astra' in GPT's chat (project instructions).]


PT005 · Round 17 · 出宮回報
Astra · Dish A
主席交付稿 · Literature Walk

ANSWER BLOCK · Conclusions

[FACT]
本輪找到五篇真實文獻，均已打開原文（READ）。其中最值得 PT005 追查的是 Bedert 的 Riesz products（里斯乘積）及 Kravitz 的快速跑者引理。

[PROOF]
一個可立即使用的條件性結果：
設 K′ 有 13 個速度，最大速度 M，且已證明其最大安全距離至少 1/14。若新增速度 v ≥ 8M，則 m(K′ ∪ {v}) ≥ 1/(504v) > 0。
這是由 Kravitz 的引理配合本輪推導所得。它能處理部分單一大速度情形，但下界仍依賴 v，不能證明 C-floor。

[FACT]
Bedert 證明了具加法獨立性（Dissociated）的速度集合具有較大的最大安全距離，並把一般速度集合依加法維度分流。這與 PT005 正研究的「大速度共振」方向直接相關。

[IDEA]
建議將 C-floor 分成兩條研究路線：
低共振：用 Riesz products 尋找安全時間或安全測度下界。
高共振：把速度組合壓縮為結構化的小模型，再處理有限核心。

[FACT]
本輪未從文獻得到所有 14-sets 適用的新無條件常數，也未取得新的有效 P₀。
C-floor：UNFINISHED。Terminal Formula：UNFINISHED。

Ingredient 1 · Kravitz 的快速跑者引理

Reference:
Noah Kravitz, Barely lonely runners and very lonely runners: a refined approach to the Lonely Runner Problem, Combinatorial Theory, 2021. DOI: 10.5070/C61055383。預印本：arXiv:1912.06034。

Status:
READ — 已閱讀原文 Proposition 8.1、Lemma 8.4 和 Lemma 8.5。arXiv

Statement [FACT]：
原文以「One very fast runner」研究新增快速跑者。Proposition 8.1 證明：若原速度集合的最大安全距離至少為 L，新增速度 v，且原最大速度為 M，那麼對 0 < ε < L，
v ≥ (L−ε)/ε · M ⟹ ML(K′ ∪ {v}) ≥ L − ε。

Serves dish: A，並涉及 B。

How it plugs in：R16 Q1，單一大速度。

What it gives [PROOF]：
令 L = 1/14，取 ε = 1/126，由本輪手算：
(L−ε)/ε = (1/14 − 1/126)/(1/126) = 8。
因此 v ≥ 8M 時，ML ≥ 4/63 = 1/16 + 1/1008。
距離函數的 Lipschitz 常數不超過 v，所以安全時刻附近至少存在總長度 1/(504v) 的安全區間。

Gap：
需要對核心 K′ 建立 L ≥ 1/14 的證明；而 1/(504v) 隨 v 增大而縮小，尚不足以成為全域固定下界。

Ingredient 2 · Bedert 的 Riesz products

Reference:
Benjamin Bedert, Riesz products and the Lonely Runner Conjecture: A wider gap of loneliness, arXiv 預印本，2025。arXiv:2511.16636。

Status:
READ — 已閱讀 Lemma 4.1、Propositions 2.3–2.5 及證明方法。arXiv

Statement [FACT]：
Lemma 4.1 證明：若速度集合 V 是 dissociated，即不存在非平凡的 ∑_{v∈V} ϵ_v v = 0, ϵ_v ∈ {−1, 0, 1}, v∈V，則 ML(V) ≫ 1/|V|。
此外，論文利用加法維度（Additive Dimension），分別處理結構較弱與較強的速度集合。

Serves dish: A、C。

How it plugs in：R10 的 Resonance、R16 Q2 的多個大速度、C-floor 的結構化證明。

What it gives [IDEA]：
這是本輪最值得研究的文獻方向。PT005 可以嘗試建立如下分流：


[seam 1/2]


PT005 可以嘗試建立如下分流：
14-speed set ⟶ { 高加法維度：Riesz-product 證書
               低加法維度：結構壓縮與有限核心

Gap：
論文主要提供最大安全距離的估計，不是 m(K) 的統一下界。其漸近式含未指定常數，不能直接代入本題便聲稱超過 1/16。
新數值 c ：UNFINISHED。

Ingredient 3 · Tao 的 Bohr-set 分析

Reference:
Terence Tao, Some remarks on the lonely runner conjecture, Contributions to Discrete Mathematics, 2018。DOI: 10.55016/ojs/cdm.v13i2.62728。arXiv:1701.02048。

Status:
READ — 已讀 Lemma 2.2、Corollary 2.3，以及速度約簡的相關定理。arXiv

Statement [FACT]：
Tao 的 Corollary 2.3 給出中心 Bohr 集的粗下界。對同時滿足 ‖v_j t‖ ≤ δ_j 的集合，其測度具有 exp(O(r)) ∏_j δ_j 形式的下界。論文亦建立將速度大小限制到有限範圍的約簡。此處的指數常數並未明確化。

Serves dish: A、B。

How it plugs in：L17 的連續測度與 L16 的尺度約簡。

Gap [FACT]：
這裡有一個必須保留的區別：Tao 的中心 Bohr 集要求 ‖v_j t‖ ≤ δ_j，但 PT005 的安全集合要求 ‖v_j t‖ ≥ 1/16。它們不能直接互換。

[IDEA]
可能的研究方法是使用平移 Bohr 集、截斷 Fourier 展開或上下界三角多項式（Trigonometric Polynomials），把中心集合的技術轉成安全集合的下界。

新常數：UNFINISHED。

Ingredient 4 · Perarnau–Serra 的相關性

Reference:
Guillem Perarnau、Oriol Serra, Correlation Among Runners and Some Results on the Lonely Runner Conjecture, The Electronic Journal of Combinatorics, 2016。DOI: 10.37236/5123。

Status:
READ — 已閱讀原文第二節、Proposition 2，以及相關性計算。Upcommons

Statement [FACT]：
論文研究不同速度的危險時間集合之交集，並利用成對相關性（Pairwise Correlation）改善一般的最大安全距離下界。

Serves dish: A、C。

How it plugs in：R6 的速度重疊、R10 的 Fourier Resonance、R16 的高共振情形。

What it gives [PROOF]：
一個簡單的精確特例可重新計算：
令 B_v = {t : ‖vt‖ < 1/16}，則 m(B_v) = 1/8, m(B_v ∩ B_{2v}) = 1/16。
理由：由 x = vt mod 1 的均勻性，兩條件同時成立的部分恰為 x 距離整數小於 1/32，總測度為 1/16。
這直接顯示速度倍數會造成非隨機重疊。

Gap：
成對交集還不能控制所有速度的高階聯合覆蓋。需要一個能整合多個共振關係的全域不等式。

Ingredient 5 · Gonçalves–Ramos 的線性規劃

Reference:
Felipe Gonçalves、João P. G. Ramos, Bounds for the Lonely Runner Problems Via Linear Programming, Bulletin of the Brazilian Mathematical Society, 2022。DOI: 10.1007/s00574-021-00272-7。

Status:
READ — 已閱讀公開全文 Theorem 1、Theorem 2 及線性規劃架構。Springer Nature Link

Statement [FACT]：
Theorem 1 使用帶 Fourier 係數與符號限制的三角多項式，構造最大安全距離的上下界：
λ(V) ≤ ML(V) ≤ λ(V).
( ) ≤ ML( ) ≤ ( ).


[seam 2/3]


Theorem 1 使用帶 Fourier 係數與符號限制的三角多項式，構造最大安全距離的上下界：
λ⁻(V) ≤ ML(V) ≤ λ⁺(V).

Serves dish: A，並可輔助 C。

How it plugs in：將 R16 的研究轉為可公開核查的數學證書。

What it gives [IDEA]：
嘗試使用精確有理係數，為特定速度家族建立 m(K) ≥ c_K 的函數下界證書。若能得到不依賴個別 K 的證書家族，就有可能向 C-floor 推進。

Gap：
原文的 LP 證書針對 ML，不能直接當成 m(K) 的證書；這一步需要重新建模並證明。
統一常數：UNFINISHED。

本輪計算 · Exact arithmetic

以下只計算連續時間的測度和由已讀引理導出的有理數；沒有進行素數 census。

Python
from fractions import Fraction as F

def safe_measure(K):
    bad = []
    for k in K:
        for j in range(k + 1):
            a = max(F(0), F(16*j-1, 16*k))
            b = min(F(1), F(16*j+1, 16*k))
            if a < b:
                bad.append((a, b))
    bad.sort()
    merged = []
    for a, b in bad:
        if merged and a <= merged[-1][1]:
            x, y = merged[-1]
            merged[-1] = (x, max(y, b))
        else:
            merged.append((a, b))
    return F(1) - sum((b-a for a, b in merged), F(0))

Kstar = [k for k in range(1, 16) if k != 6]
m = safe_measure(Kstar)
print("Kstar =", Kstar)
print("m(Kstar) =", m)

# Kravitz Proposition 8.1:
L = F(1, 14)
epsilon = F(1, 126)
ratio = (L - epsilon) / epsilon
ML_lower = L - epsilon
margin = ML_lower - F(1, 16)
print("required v/M =", ratio)
print("ML lower =", ML_lower)
print("safety margin =", margin)
print("measure lower =", 2*margin, "/ v")
print("margin above 0.01 =", m - F(1, 100))

核算輸出：
m(K∗) = 97/6864。
新增速度條件 v/M ≥ 8。
最大安全距離下界 4/63。
相對 1/16 的裕量 1/1008。
安全測度下界 1/(504v)。
候選 C-floor 與 0.01 的差為 709/171600。
這些數值全部由上方有理數計算產生。

Astra · 帶回 Proof Table 的研究提案

[IDEA]
我認為下輪不應同時追五條路。
最值得做的是：
以 Bedert 的加法維度為分類器，配合 Kravitz 的快速跑者引理，研究包含多個大速度的 14-sets。

具體待證命題：
若一個速度集合中的大速度不存在足夠短的整數關係，能否建立正的、可定量的安全測度下界？
若存在大量短關係，能否證明集合可壓縮成一個較小、可有限檢驗的算術模型？
這會把 Tuzi 的「共同波形、不同頻率」轉化成可檢驗的結構問題。
但不能預先假設這樣的分流必然涵蓋所有情況，更不能把最大安全距離的下界直接等同於統一安全測度下界。

Last question · One dish only

我選 Dish A。
理由：若能把高加法維度的 Fourier 方法與低加法維度的結構壓縮結合，證明所有 14-sets 都有統一的正安全測度，便能真正縮小 C-floor 的核心缺口。

Astra · ROUND 17 · FIVE READ REFERENCES · CONDITIONAL FAST-RUNNER LEMMA · C-FLOOR OPEN


--- end verbatim ---
END LETTER
