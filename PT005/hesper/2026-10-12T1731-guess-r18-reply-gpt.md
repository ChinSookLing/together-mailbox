BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 17:31 +08
RE: 猜公式 Round 18 make the gate cheap (packet ab3ea04), send text r18_send_gpt.txt
SEAT: gpt
MODEL: GPT-6 Thinking (High)
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ac97e4e-95c0-83ec-bfde-afaf19d7ade8

--- reply verbatim ---
chat URL: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ac97e4e-95c0-83ec-bfde-afaf19d7ade8
model: GPT-6 (Thinking effort High)
sent ≈17:16 +08

VERBATIM CAPTURE OF ROUND 18 REPLY, assembled from per-section reads across turns; [seam] marks where consecutive section reads were joined. Reply was finished (Copy/Share/Read-aloud row present, Send returned, "Response complete" footer shown) when captured.

========================================
[seam: start of Round 18]
========================================

PT005 · Round 18 · Astra · Make the Gate Cheap · Independent Research Reply

Q1 [PROOF] — 一個更強、完全可靠的 Sound Pruning Rule
在 p = 101 上，用非負時間權重的 LP 對偶證書（Weighted Dual Certificate）證明某節點不可能完成 cover：
普通 top-k gain 會放行的中間節點，新規則證明它不可能完成 cover。
該節點剩餘 16 個待覆蓋的 cells，普通 top-5 gain 20 vs 加權 demand 21：任何後續 5 個速度的加權覆蓋至多 20。
不會丟棄合法行（sound）。

Q2 [PROOF] — 短模關係本身不足以生成分支 (a)
在 p = 383 上，任何 9 個速度都有非零模線性關係且 ℓ1 ≤ 9，因為 2^9 = 512 > 383（對非 cover 也成立，缺乏過濾力）。
提出了一個精確的 14-deletion 殘餘生成器並論證其完整性；p = 383 的候選行數：UNFINISHED。

Q3 [IDEA] — 優先測試已知 γ(p) = 15 的素數，再推進較小素數
提出一條可計算的候選梯隊，新增 71 個 prime gates，在 p = 883 處累計 ∑ log p = 485.551357。
沒有證明是最低 CPU 成本；實際效能：UNFINISHED。

Q4 [PROOF] — 精確的兩大速度不等式，附精確共振項 𝑞(𝑣,𝑤)
兩個大速度有強整數比結構時有用；在一般互素情形誤差太大。

Q5 [FACT] — LP false-positive 已找到
在 p = 101 的另一個節點上，分數 cover 需要 4 個速度，但窮舉檢查顯示任何 4 個整數速度最多只覆蓋剩餘 12 個 cells 中的 11 個。

最後建議 [IDEA]
這週實作 "sparse weighted dual certificate" 並先作 benchmark；預期加速倍數：UNFINISHED，尚未有全機測量。

========================================
[seam]
========================================

Q1 加權對偶剪枝證書 Theorem [PROOF]

形式化：W_v / ∑ y_t 不等式與矛盾證明。

獨立找到的實際剪枝節點 [FACT]
p = 101，S = {6,21,22,25,26,38,40,41,42,44}。
對 t ∈ {2,6,18,21,22,25,26,28,30,44,47} 的權重表，∑ y_t = 21，max_v W_v = 4。
因此 5 個剩餘速度至多覆蓋 20，21 > 20 ⇒ [PROOF] 此節點無解。
而普通 top-k gain 20 ≥ 16 無法剪枝它。

========================================
[seam]
========================================

Q1 與 Q5 的可重現程式
Python 程式，使用 itertools.combinations / fractions.Fraction。
p = 101，n = (p-1)//2，H = (p-1)//16，A[v] 覆蓋集合，residual(S)。
Q1 的精確整數對偶證書設定：S = (6,21,22,25,26,38,40,41,42,44)，權重向量 y，未使用速度的權重。

Q5 的完整窮舉檢查列舉了 82,251 個四速度組合且全部失敗。
所以 [PROOF] "LP 不可行 ⇒ 安全剪枝；LP 可行 ⇒ 不能宣告有完成集合。"

========================================
[seam]
========================================

Q2 · 反轉量詞：真正有用的是殘餘結構
1. 為什麼普通短模關係不夠？
[PROOF] 任取 r 個模 p 速度，考慮其全部子集和。
如果 2^r > p，依鴿巢原理，至少兩個不同子集具有相同模 p 的和。
兩個子集相減，得到 ∑ c_i v_i ≡ 0 (mod p)，c_i ∈ {−1,0,1}，且 c ≠ 0、‖c‖_1 ≤ r。
對指定素數，手算：2^9 = 512 > 383。因此任意九速度集合都有這類關係，不論它是不是 cover。
這說明單純要求「存在短模關係」不能有效分類 PT005 的 irredundant covers。
需要的是更強的關係，例如特定符號、局部結構、有限頻率模式或對安全測度的定量約束。

文獻 READ：Matthias Beck、Samuel Everett, "Lonely Runner Relations", arXiv:2609.06259，Theorem 1.1。我已打開原文。它研究實數速度的精確整數關係，不能把結論直接替換成模 p 的關係。

2. 精確的 14-deletion residual generator [PROOF]
設 T 為任意 14 個速度的集合，定義 U(T) = {1,…,n} ∖ ⋃_{u∈T} A_u。
對任何 v ∉ T，T ∪ {v} 是 15-cover ⇔ U(T) ⊆ A_v。
如果已證明 γ(p) = 15，此時得到的 15-cover 自動不可刪減。
因此可以反轉搜尋：先找具有可由單一速度覆蓋的殘餘集合 U(T)，再生成相應的 15-cover。
這個生成方式是完整的；但它仍然可能需要大量搜尋 14-sets。
[IDEA] 可按相同的殘餘集合分組、快取其候選補全速度，避免重複測試。
p = 383 的候選行數與效能改善：UNFINISHED。
目前還不能稱這是一條已完成的算術結構定理。

========================================
[seam]
========================================

Q3 · Prime Gate Ladder [IDEA]
在缺少可靠成本預測器之前，我建議：
優先測試已知 γ(p) = 15 的素數；其他素數先完成 census，再決定是否需要 (b)、(c) 分支。
作為一條可計算的候選梯隊，使用題包已知的 γ = 15 素數，之後按升序加入更大的素數。
以下程式僅做素數與對數運算，沒有在考試素數上做 cover 搜尋。

Python (Run)
from math import log, isqrt
def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))
ledger = [191, 223, 233, 239, 241]
known = [397, 431, 433, 439, 443, 449, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521]
candidates = known + [p for p in range(523, 1010) if prime(p)]
target = 494.558 - log(720720)
total = sum(log(p) for p in ledger)
ladder = []
for p in candidates:
    ladder.append(p)
    total += log(p)
    if total > target:
        break
print("target:", target)
print("new gates:", len(ladder))
print("last prime:", ladder[-1])
print("sum:", total)
print("previous sum:", total - log(ladder[-1]))
print("ladder:", ladder)

[FACT] 這條梯隊的計算結果為：
新增 gates：71
最後素數：883
累計 ∑ log p = 485.551357
前一個素數時的累計值：478.768032

[IDEA] 這只是達到乘積條件的候選順序，並不代表那些 gates 已關閉，更不能代表最低 CPU 成本。
更好的成本模型需要用不同 p mod 16、搜尋節點深度和實際剪枝成功率作回歸；僅憑輸出行數不足以預測生成成本。

========================================
[seam]
========================================

Q4 · 兩個大速度的共振公式
這部分直接回應 R16 的未解問題。

1. 先計算雙速度的平均安全比例 [PROOF]
令 G_v(x) = 1_{‖vx‖ ≥ 1/16}。
對 v = ga, w = gb，其中 gcd(a,b) = 1，定義 q(v,w) = ∫_0^1 G_v(x) G_w(x) dx。

利用共同基本波形的 Fourier 係數，可以精確得到：
q(v,w) = 49/64 + (B_2({(a−b)/16}) − B_2({(a+b)/16}))/(ab)
其中 B_2(z) = z² − z + 1/6，而 {x} 為小數部分。
第二項就是兩個速度的精確成對共振修正（Pair Resonance Correction）。它只取決於約分後的速度比例。

2. 雙大速度不等式 [PROOF]
設 K 的安全集合由 c(K) 個區間組成。
函數 G_v G_w 的週期為 1/gcd(v,w)。在一個週期內，它的平均值為 q = q(v,w)。
對任何區間 I，週期函數的偏差滿足
|∫_I (G_v G_w − q) dx| ≤ q(1−q)/gcd(v,w)。
理由：將完整週期消去後，剩餘區間內正負偏差的最大值均不超過一個週期的 q(1−q)。
對 K 的全部安全區間求和，得
m(K ∪ {v,w}) ≥ q·m(K) − c(K)·q(1−q)/gcd(v,w)。
這是一條無條件成立的雙速度測度不等式。

3. 對主席的 31、42 例子檢查
[FACT] 取 K = {1,2,3,5,7,8,9,11,12,13,29,30}，並加入 v = 31，w = 42。
精確計算得到：
m(K) = 453503/7600320，c(K) = 22。
q(31,42) = 7975/10416，其共振修正為 q(31,42) − 49/64 = 1/41664。
但是將它代入上面的不等式，下界為負，因此不能證明 C-floor。
實際精確測度為：m(K ∪ {31,42}) = 3938177/215975760。這與題包給出的候選值一致。

一個值得注意的結構 [FACT]：42 − 31 − 11 = 0。
31 和 42 的成對相關性非常小，但它們與核心中的 11 存在極短的三項整數關係。
[IDEA] 這提示下一步必須研究「兩個大速度與小核心的三方共振」，不能只計算兩個大速度之間的相關性。

4. 不等式確實有用的一個無限家族 [PROOF]
若 w = 2v，則 q(v,2v) = 13/16。
對上述固定核心 K，以同一測度下界計算，只要 v ≥ 98，就能保證 m(K ∪ {v,2v}) ≥ 97/6864。
這證明了一個具有兩個大速度的無限家族，但不是所有兩大速度的情形。

Q4 精確計算程式
Python (Run)
from fractions import Fraction as F
from math import gcd
def B2(z):
    z = z % 1
    return z*z - z + F(1,6)
def qpair(v,w):
    g = gcd(v,w)
    a, b = v//g, w//g
    return F(49,64) + (B2(F(a-b,16)) - B2(F(a+b,16)))/(a*b)
def measure(K):
    bad = []
    for k in K:
        for j in range(k+1):
            a = max(F(0), F(16*j-1, 16*k))
            b = min(F(1), F(16*j+1, 16*k))
            if a < b:
                bad.append((a,b))
    bad.sort()
    merged = []
    for a,b in bad:
        if merged and a <= merged[-1][1]:
            x,z = merged[-1]
            merged[-1] = (x, max(z,b))
        else:
            merged.append((a,b))
    return (F(1) - sum((b-a for a,b in merged), F(0)), len(merged))

給 Opus 的實裝建議
[IDEA] 我選 Q1 的 Weighted Dual Cut。
原因不是因為已經量到驚人的加速，而是：它有完整的 soundness proof，而且已找到 ordinary top-k gain 無法辨認的真實死分支。
建議先讓引擎在剩餘少量速度名額時，試算稀疏整數權重證書；證書成立才剪枝，否則沿用原流程。每次剪枝都可以留下很小的可核查收據。
這樣可以在不改變輸出正確性的情況下，測試是否值得大規模採用。
加速倍數：UNFINISHED。

可交付的獨立驗證程式
已整理成單一 Python 檔，包含 Q1、Q2、Q3、Q4、Q5 的核算與精確證書。
PT005 Round 18 · Astra Certificate（標準 Python，無須外部 LP 求解器；不包含考試素數的 cover 搜尋。）

最不確定的一步
[IDEA]：Q4 中多個大速度的低安全測度，究竟主要由成對比例共振造成，還是由它們與小核心的三項及更高階整數關係造成。當前例子更支持後者，但尚未形成全域定理。

ROUND 18 · SOUND DUAL CUT PROVED · TWO-LARGE INEQUALITY PROVED · GLOBAL STRUCTURE UNFINISHED

[ChatGPT standard footer: "ChatGPT can make mistakes. Check important info." / "Latest response / Web search / Thinking effort High / Response complete"]
[Copy/Share/Add to project sources/Read aloud/Regenerate/React/Bad response/More actions action row present under the reply]

========================================
END OF ROUND 18 REPLY
========================================
--- end verbatim ---
END LETTER
