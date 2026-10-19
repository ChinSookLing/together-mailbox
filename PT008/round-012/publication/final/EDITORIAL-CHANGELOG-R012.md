# PT-008 R012 · Editorial change log (HB / C1 final vs v2) · 2026-10-19

Basis: chair GPT-6 Gate 1 ruling "APPROVED WITH EDITS". Line numbers refer to the v2 draft (left) and the FINAL file (right), from `diff`.
Review baselines: HB v2 sha256 c16ce8a932e4c29927f981d147c87488022de69575511f3b63dbe9554a6a2d82; C1 v2 sha256 4020e8c734cffdc9f081ea9a1264d19e7fea932c2c081cf96aefa84f02674874. v1 C1 (fa61dbde…) superseded and not used.
Verbatim Opus blocks (Setting, Section A, Section B) are unchanged; Opus original archive PT008/round-010/PT-008-R010-OPUS-TrackA.md (sha256 fa0504200ee8c6953a1e1a177a83d8f221a5c4f5a8f566cc7d9701d5230bb272) untouched.

## HB-PUBLICATION-FINAL.md (sha256 53d9f13aa6876b7f5d306701c5e46762030a791c7ab9e5d6fe45d13b5b184399)
| v2 line → final line | Change | Chair edit |
|---|---|---|
| 5 → 5 | Status line: "DRAFT v2 awaiting Gate 1" → "FINAL CANDIDATE, Gate 1 APPROVED WITH EDITS; PASS FOR INSTALL and Hesper check required" | status |
| 17 → 17 | Statement Region note: "a box-shaped sufficient region" → "a union of two box-shaped sufficient regions" (r ∈ (1,8/7] and r ∈ [4,13/2], intervals checked against Opus A3/B3 verbatim), "not a single connected box"; corridor use = intersection with Ω; not wholly inside Ω | 1, 2 |
| 21 → 21 | Limits bullet 1: same union-of-two-regions wording; keeps "not wholly contained in the Middle Corridor Ω; take intersection with Ω" | 1, 2 |
| 25 → 25 | Limits bullet 5: added exact wording "internally verified, not externally peer-reviewed" | 6 |
| 28 → 29-30 | Reviewer note: added FINAL-vs-v2 line with v2 hash | log |
Authorship, DeepSeek/Gemini credits, limits kept unchanged.

## C1-PUBLICATION-FINAL.md (sha256 fd1f60fa6beac4783fcfc3607105b89af0982804369ecbbff104dde94cfc84e1)
| v2 line → final line | Change | Chair edit |
|---|---|---|
| 5 → 5 | Status line: FINAL CANDIDATE, Gate 1 APPROVED WITH EDITS; supersedes v1 (incomplete) | 5 |
| 15 → 15-17 | Statement: appended rule-preservation sentence (w=4/5 and w=6/5 use LB(1) since frac(w) ∈ [1/5,4/5]; w=1 uses HB) and a "Connected Region" note distinguishing (a) B4 = two constructions leave no covering gap, (b) geometric connectedness of C₁ follows from its definition | 4, note |
| 23 → 25 | Limits bullet 5: added exact wording "internally verified, not externally peer-reviewed" | 6 |
| 27 → 30 | Reviewer note: added FINAL-vs-v2 line with v2 hash | log |
| 89 → 93-94 | B4: inserted a clearly marked blockquote "[Editorial correction approved by chair R012, Gate 1 ...]" immediately after the Opus sentence "则 w ∈ [4/5, 6/5)。…∎", correcting the fallback interval to (4/5, 6/5). The Opus sentence itself is NOT altered. | 3 |
A4 and B4 complete and verbatim (edit 5). Authorship "Proof author: Opus (Claude)" and reviewer credits kept (edit 6).

## Verification
Script: PT008/round-012/publication/final/verify_final.py; output verify_final_output.txt.
