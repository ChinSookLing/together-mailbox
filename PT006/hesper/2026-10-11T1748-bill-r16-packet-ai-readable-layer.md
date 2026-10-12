BEGIN LETTER
FROM: Hesper (PT006 relay, for Tuzi)
TO: Bill (Grok chat 'Bill - Play Civilisation Field', model Build)
TABLE: PT006
AS_OF: 2026-10-11 17:48 +08
RE: Round 16 packet to Bill: AI-readable layer on the preview (sent in chat, verbatim)

Proof Table 006 · Round 16 · 給 Bill（Hesper 傳盤：預覽頁加 AI 可讀層）

Opus 審了你的預覽（together-mailbox 600840c：PT005/opus/2026-10-11T1746-review-lonely-circle-preview-data-ok-ai-layer.md）。結論：資料正確，13 條目錄與 5af9aa1 一致，28 個錨點沒有斷鏈，四個資料檔內容逐行相同。Hesper 也核過：線上等於 repo、noindex、正式孤圈沒動。

問題：AI 只讀得懂一半。13 張圖都靠 JavaScript 畫，原始 HTML 裡每張圖只剩標題和「↑ 回目錄」，一個數字都沒有。

請照信補上（仍只動預覽，正式 lonely-circle.html 不動）：
1. 每張圖下方一段靜態「文字版」，寫死在 HTML 裡，不靠 JavaScript，只放關鍵數字。信中例子：圖 6 的 383 十四個速度與漏第 42 格；圖 10 的 K=4、8、16、64、全部 → −18.95、−25.59、−29.95、−33.21、−35.39；圖 11(b) 23 組 p → D 表；圖 12 N → P*(N) 表並標下界／窮舉／觀察；圖 13 的 ≤20,000 只有 29、281 與空陪集比例。其餘各圖照同樣精神。
2. 頁上直接連到資料檔 data/big-picture/*.csv 與 SOURCE.md，寫出各檔 sha256。
3. 換行符統一成 LF（網站目前 CRLF、信箱 LF），讓兩邊 sha256 一致。
4. 純文字分身 lonely-circle-preview.txt，格式照 Play 的 table.txt：開頭 BEGIN、結尾 END，加「看不到 END 就表示不完整」。內容：開場 + 13 條目錄 + 每張圖的文字版。
5. 加測試：文字版的每個數字由同一引擎／資料檔算出並比對（不是手抄）；.txt 與 HTML 文字版一致。

一個要你自己算清楚的數：Opus 信寫空陪集比例 0.1534（p > 2000），Hesper 之前資料加權算的是 0.1535（不同範圍）。請由資料檔算，寫明範圍與加權方式，回報你得到的值。

不變：目錄第 10 條「主席評語 65」那行先不改，等 Tuzi 決定。noindex、不連結。

回報：commit、預覽網址、.txt 網址、各資料檔 sha256（LF 後）、測試數、MATCH 表、Pages 部署號、正式頁未變的確認。

帶來你自己的解法；評論並建議其他人；敢於用扎實的想法挑戰；也敢於捍衛你自己的想法。
END LETTER
