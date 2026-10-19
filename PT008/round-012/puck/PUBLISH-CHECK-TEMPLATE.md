# PUBLISH-CHECK (template) - HB / C1 final, PT-008 R012
Fill after Bill's publish report. Puck: independent consistency check. Do not edit the finals.

Reference: branch PT-008 commit 5ccce35, dir PT008/round-012/publication/final/
| file | expected sha256 |
|---|---|
| HB-PUBLICATION-FINAL.md | 53d9f13aa6876b7f5d306701c5e46762030a791c7ab9e5d6fe45d13b5b184399 |
| C1-PUBLICATION-FINAL.md | fd1f60fa6beac4783fcfc3607105b89af0982804369ecbbff104dde94cfc84e1 |
| EDITORIAL-CHANGELOG-R012.md | bf26ba463b174ff42bb2ab55f63799dc2052c5b2c31b256dfa396d5860f4aba3 |
Gate 3: Hesper MATCH at 5fde1b8. Chair acknowledgement of MATCH: [seen / not seen] (hold if objection).

## Published page record
- HB URL: 
- C1 URL: 
- changelog link: 
- page version / revision id: 
- publish time (SGT, UTC+8): 
- check time (SGT): 
- reported by Bill (message ref): 

## Checks (PASS / FAIL / N/A)
1. Re-hash of public raw content: HB [ ] C1 [ ]  (hash found: ...)
2. Diff vs final file (empty?): HB [ ] C1 [ ]  (normalization noted: line endings / trailing newline / escaping)
3. If only a rendered page: block-by-block text comparison, 0 differences [ ]
4. HB wording present: "union of two box-shaped sufficient regions", r in (1, 8/7] and [4, 13/2], not wholly inside Omega [ ]
5. C1 B4: Opus sentence "w in [4/5, 6/5)" unchanged + marked editorial correction (4/5, 6/5); rule w=4/5,6/5 -> LB(1), w=1 -> HB [ ]
6. Credits: "Proof author: Opus (Claude)", DeepSeek e65a779, Gemini b5878c9 [ ]
7. Limits line "internally verified, not externally peer-reviewed" [ ]
8. Ratings shown: HB, C1 = PROVED (PT-008 internal); F5, E_N still UNFINISHED; no claim of external peer review or Argon's withdrawn claim [ ]
9. Privacy scan of public text (emails, tokens, account names) clean [ ]
10. Nothing outside the two files was altered on the page unexpectedly [ ]

## Verdict
CONSISTENT / INCONSISTENT (details): 
If INCONSISTENT: tell Tuzi + chair; Bill fixes to match final byte-for-byte; re-check.
Signed: Puck
