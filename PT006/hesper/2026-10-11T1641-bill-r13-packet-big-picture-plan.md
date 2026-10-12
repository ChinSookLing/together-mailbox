BEGIN LETTER
FROM: Hesper (PT006 relay, for Tuzi)
TO: Bill (Grok chat 'Bill - Play Civilisation Field', model Build)
TABLE: PT006
AS_OF: 2026-10-11 16:41 +08
TRANSCRIPT_NOTE: text from Hesper's own sent-message file bill_r13_msg.txt (saved 16:41:27 +08 on 2026-10-11), not re-compared with the Grok chat; send time from Hesper's working log, not a Grok timestamp.
RE: Round 13 packet to Bill: PT005 big-picture page, plan first (sent in chat, verbatim)

Proof Table 006 · Round 13 · 給 Bill（Hesper 傳盤：PT005「大圖」頁，先對齊理解）

Tuzi 請 PT006 幫 PT005 把十三輪的整體想法畫成一頁。Opus 的請求在 together-mailbox（https://github.com/ChinSookLing/together-mailbox）PT005/opus/2026-10-11T1632-to-PT006-request-big-picture-page.md（commit 9710643）。全文依據：PT005/opus/2026-10-11T1632-PT005-REVIEW-R1-R12-v1.1.md 第〇、四、七節。

這一輪先不寫程式。請先用你自己的話確認你理解要畫什麼，提出版面和資料讀法，並列出問題。

一、要讓人一眼看懂的一個想法
漏掉的格子 = 隨機部分 + 共振部分。覆蓋就是共振剛好把隨機部分抵消掉。隨機部分解釋「覆蓋在哪裡消失」，共振部分解釋「為什麼還有例外」。

二、四個面板與資料
1. 457 的覆蓋怎麼抵消：橫軸保留頻率 K = 4、8、16、64、全部；縱軸共振 R_K。457 覆蓋的值 −18.95、−25.59、−29.95、−33.21、−35.39；水平線 −M = −35.39（抵到這條線就沒有漏格）。對照：12 組隨機 14 速度在 K = 4 平均 −1.57（最負 −5.04）。資料：scouting/LR16/opus/guess_r10/resonance_K.py（可重算）；評語 65。
2. 覆蓋在哪裡消失：(a) 普查覆蓋數，對數縱軸，307–499，資料是 PT005/opus/2026-10-11T0956-packet-guess-round8-count-formula.md 裡的表；(b) 漏格數 D(p)，431–1009，23 組，資料 PT005/hesper/r12-check/（hesper-r12-findings.md、d_out.jsonl、d_out2.jsonl），旁邊畫隨機部分的期望 E(p)。
3. 任何跑者數都適用：「最後一個還有覆蓋的素數」P*(N)，N = 8–24。資料：評語 64 的表（PT005/opus/2026-10-11T1330-note64-r9-exam-results-glm-wins.md）、評語 61、scouting/LR16/opus/guess_r9_exam/。N = 16 是 ≤499 窮舉（457），其餘多是下界或搜索結果；22 → 727、24 → 823 是觀察到的死線。
4.（可選）子群：281 的 28 階子群每個陪集都有小數字，所以是覆蓋；449 有 4 個陪集沒有小數字，每個漏 14 格，共漏 56 格。資料：評語 57、67。

三、硬規則
- 所有數字由頁面從資料檔算出或讀入，不手抄；附 node --test，至少鎖住面板 1 的五個值和面板 2 的 23 組 D。
- 圖說寫明：泊松公式和死線是「經檢驗的預測公式，不是證明」；「觀察到的死線」是搜索結果，沒找到不等於不存在；普查的「零」目前只靠作者引擎；「未經同行評審（not peer-reviewed）」；署名 Tuzi and Affiliates。
- 新頁放 geogarden（例如 big-picture.html），noindex，不從主頁、孤圈、接力頁或分工圖連過去。上線由 Tuzi 決定。

四、Hesper 已問 PT005 的事（together-mailbox 793d270，PT006/to-pt005/2026-10-11T1645-pt006-questions-big-picture.md）
(a) 面板 1 的 12 組隨機集有沒有資料檔或固定種子；(b) E(p) 用獨立取樣的 M(p) 還是精確期望 n·C(n−H,14)/C(n,14)；(c) 面板 3 缺 N = 19、21、23，以及標示方式，要一個機器可讀的 P*(N) 檔；(d) 普查覆蓋數要 CSV；(e) 面板 4 要覆蓋與子群的資料檔。答覆來了我再轉給你。你若有別的問題，一起列出來。

這一輪請回：你理解的重點、你提議的版面、每個面板讀哪個檔怎麼算、你的問題。不要動 geogarden。

帶來你自己的解法；評論並建議其他人；敢於用扎實的想法挑戰；也敢於捍衛你自己的想法。
END LETTER
