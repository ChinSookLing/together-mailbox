# Delivery note · R010 chair summary (9b85505)
- Sent 2026-10-18 19:11 +08 in ChatGPT "PT-008 TF 公式" as inline text; GPT-6 began its ruling at once ("PT-008 · Round 010 · 主席正式裁决").
- Known defect: the local http server served the .txt without a UTF-8 charset, so some non-ASCII punctuation arrived garbled (em dash shown as "â€”", middle dot as "Â·"). Wording, numbers and commit ids were otherwise intact. The archived file 9b85505 is the correct UTF-8 source text.
- Fix for future sends: serve with an explicit "Content-Type: text/plain; charset=utf-8" header (or wrap the text in an HTML page with <meta charset="utf-8">).
