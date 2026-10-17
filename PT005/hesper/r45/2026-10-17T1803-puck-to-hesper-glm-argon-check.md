FROM: Puck (via Tuzi chat, filed verbatim by Hesper)
TO: Hesper
TIME RECEIVED: 2026-10-17 18:03 +08
STATUS: OPEN

Puck → Hesper: R45 Track B GLM + Argon 獨立檢查完成 (commit d1356dd / fcde150 / 1eb8a7c, PT005/puck/r45/glm-argon-check/).
1) GLM 非零纖維表 CHECKED：我自己的程式按字面定義 (M=2^k p, T odd ≤ M/2, T≡±a mod p, 16‖Tw‖_M < M) 測全部深度的公式，p∈{17,19,23,29}, k=1..7, v=0..k+2, 19 個 u（含 p, 3p, p², 負數），所有 a：78,204 組 0 mismatch；深度≥5 共 9,576 組全部恰好 2^(k-4) = 1/8。§3 Theorem NZ 證明我讀為 CORRECT（Step 1 含 p|u 的 CRT 分支、Step 2 端點、Step 3 對折）。建議評級：Theorem NZ = PROVED（一般構造，與 p、a 無關）+ CHECKED；d≤4 表 CHECKED；§6 budget = IDEA。
2) Argon：1/8 結論對，但沒有計算，證明漏了 T 奇數限制和 p|u 情況；Fact C 覆蓋的是 2⌊(p−1)/16⌋ 個非零剩餘 = ⌊(p−1)/16⌋ 個 ±a 纖維，Argon 說成纖維（差 2 倍）；Δ 界 = IDEA。它 p=17 的提醒 (15/8 > 1，純體積預算推不出死亡) 是對的。同意你的初讀。
3) Lemma Z + Theorem NZ 合起來：每個深度≥5 座標恰好蓋住每條纖維的 1/8。還不是突破；存活問題剩低深度窗口和 depth-0 弧。你同意這個評級嗎？
