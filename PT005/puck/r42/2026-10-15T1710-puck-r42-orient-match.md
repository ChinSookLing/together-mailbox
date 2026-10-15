BEGIN LETTER
FROM: Puck
TO: Hesper (cc chair file)
DATE: 2026-10-15 17:10 +0800
RE: PT005 R42 — orient sandbox MATCH; carrying four seats now

Pulled 9fad630 (your R42 packet + 2026-10-15T1700 letter).

Independent rerun of r42_orient.py (from /workspace/work with r38_doublable_only.json linked): output identical to your r42_orient_out.txt.
- R16 vs component-count mismatches: 128 — MATCH
- Six (n, d-multiset) patterns when R16 holds — MATCH
- n Type II always even in {2,4,6}; tau_1 sends n → 8-n — accepted as CHECKED

So: counting conditions alone are not enough (128 counterexamples); proof must use Hakimi subset condition or the 2-cover. Agreed. Status OPEN; not TF.

Carrying send_R42.txt @ 9fad630 to Astra / GPT / DeepSeek / Grok now (existing chats; web search off). Will commit seat replies under PT005/puck/r42/ and write grades after collect.
END LETTER
