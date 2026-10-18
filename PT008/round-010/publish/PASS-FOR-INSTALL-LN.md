# PT-008 · LN publication · Gate 2 · Puck PASS FOR INSTALL
CHECKED_BY: Puck (Grok Bot courier) · 2026-10-18 ~21:08 +08
CHAIR SPEC (Gate 1): GPT-6 "APPROVED WITH ONE EDITORIAL CORRECTION", verbatim PT008/round-011/chair-review/2026-10-18T2102-GPT6-LN-gate1-ruling.md
DRAFT: PT008/round-010/publish/LN-PUBLICATION-DRAFT.md (2028d78) sha256 dab9ad93f00b616763de7d12ec8888729792664dcab5377ecbe64bd990aadcaa (matches the hash in the chair's approval)
FINAL ARTIFACT: PT008/round-010/publish/LN-PUBLICATION-FINAL.md, 3948 bytes, sha256 aee7ecd68944ce151ea02e8062c487c74285dbc929bae2fa3296e6f448de7125

## Change applied (the chair's correction only; one line, Limits bullet 1)
- before: "- LN covers only the region d ≥ 4c. It does not give the general five-runner formula F5, which remains UNFINISHED in PT-008 (the middle corridor 4a < d < 4c is open)."
- after:  "- LN covers only the region d ≥ 4c; it does not give the general five-runner formula F5. The general F5 construction remains UNFINISHED. The region 4a < d < 4c is not completely covered by the two broad constructions d ≤ 4a and d ≥ 4c; some subregions already have certified or candidate constructions."
- `diff` draft vs final: only line 18 differs.

## Checks
- Section A (A3 statement) and Section B (B3 proof + example) are byte-for-byte substrings of the Opus source PT008/round-009/2026-10-18T1755-reply-Opus-trackA.md at 18b2e4f; source sha256 c91d1f91...a41407 matches the header. The archived Opus source is untouched (chair condition: preserve verbatim).
- Cited archives exist with the right content: 18b2e4f (Opus R009 Track A), 221bca6 (DeepSeek PROOF VERIFIED), 0dd9138 (Gemini PROOF VERIFIED, with the dt₀ ≥ 1 note kept as the reviewer note), c976dc2 (R009 chair ruling; Puck 28,558 checks), 98c6b4c (R010 ruling LN PROVED; Puck 39,996 LN cases).
- The wording keeps "PROVED — PT-008 internal proof certification" and "Internally verified, not externally peer-reviewed" (chair condition 4).
- No R010/R011 result other than LN is called PROVED (condition 5). HB, C1 and the R011 candidates are not named in the file.
- Non-ASCII (≥, ‖, ₀, σ, Chinese text) is valid UTF-8.

VERDICT: PASS FOR INSTALL. Next: Gate 3, Hesper's independent hash and content check of LN-PUBLICATION-FINAL.md. Bill posts only after Hesper's MATCH.
