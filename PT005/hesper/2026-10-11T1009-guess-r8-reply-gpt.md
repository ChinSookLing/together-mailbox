BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 10:09 +08
RE: 猜公式 Round 8 (packet 1351cbb), send text r8_send_full.txt or r8_send_short.txt
SEAT: gpt
MODEL: GPT-6.1 Sol Max (worked 5m 23s)
CHAT: https://chatgpt.com/g/g-p-6aab4b75ee5c8191b91e5cede8dea932-play-civilisation-field/c/6ac9c0b6-9ffc-83ec-a1ee-b11795796df5

--- reply verbatim ---

答案區塊（ANSWER BLOCK）

**[IDEA／FACT] Q1：**下述三常數模型在33點的樣本內（in-sample）判對 30/33：非零17/19、零13/14。正數計數的對數絕對誤差中位數 0.448，均方根誤差（RMSE）1.287。
**[IDEA] Q2：**候選速度組隨 p 呈多項式增長，全部時間格被覆蓋的概率可能呈指數下降；s 增大會降低單格覆蓋概率。
**[IDEA] Q3：**全部預測 0：503、509、521、523、541、547、557、563、569、571、577、587、593、599。其餘桶皆空；整張預測全部正確的主觀信心 65%。
**[IDEA] Q4：**共用擬合常數後，模型預測最大質數為 N=17:463; N=18:523; N=20:601。跨 N 外推信心低。

[PROOF] 令 k=N−2。隨機選取 k 個不同速度，每個時間格恰有 H 個速度能覆蓋它，因此單格被覆蓋的概率精確為

q_N = 1 − (n−H choose k) / (n choose k).

這沒有假設不同時間格獨立。

[IDEA] 以下使用自然對數（natural logarithm），建立期望覆蓋數（expected count）模型：

ℓ_N = log(n choose k) − log n + a + b·n·log q_N − c·s,  λ_N = e^ℓ_N.

(n choose k)/n 近似縮放軌道的候選數；q_N^(b·n) 是對聯合覆蓋概率的擬合，並非證明。採用固定判準：λ_N ≥ 0.5 判非零。

[FACT] 用全部33點最小化

Σ_p [log(1+λ_16(p)) − log(1+C_p)]^2

得到三個常數：

a = −1.295635281,  b = 1.275066877,  c = 0.165802071.

C_p 是資料包中的實際計數；零點直接參與擬合。

[FACT] 三個錯判為：

p    實際覆蓋數    模型 λ    判斷
409  1             0.44485   0
433  0             0.89007   非零
457  1             0.01171   0

[FACT] 中位對數誤差0.448相當於約 1.57倍；但457被低估約 85倍，所以中位數不能代表算術例外的風險。

[IDEA] 固定 N,s 時，

q_N → q_∞ = 1 − (1 − 2/N)^k,

模型因而近似

ℓ_N = (k−1) log n + b·n log q_∞ − c·s + O(1).

第一項只有對數增長，第二項線性下降，故每增加固定步長的 p，計數大致乘一個固定因子。對 N=16，在350附近增加16，這個近似因子約 0.324。這解釋模型的下降形狀，尚未證明真實算術覆蓋服從它。

[PROOF／IDEA] H/n = (2/N)(1 − s/n)，所以較大的 s 降低 q_N；額外的 −c·s 是經驗修正，沒有捕捉全部乘法結構。

[FACT／IDEA] 本輪只擬合提供的33個 N=16 計數；對 N=17,18,20，共用上述常數評估質數至20,000，沒有做覆蓋普查。所得最後非零判斷分別為463、523、601。

**[IDEA] 最不確定的一步：**假定描述時間格相關性的三個常數可以跨 N 共用。


--- end verbatim ---
END LETTER
