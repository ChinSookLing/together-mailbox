# Puck: PUBLISH CHECK HB / C1 v3 (status-line update)

Checked by: Puck (PT-008), 2026-10-19 (SGT, UTC+8), after Bill's v3 update. Web page fetched with curl (raw bytes), both /table.txt and /table (HTML), HTTP 200.

## Bill's v3 report (digest)
- Updated only HB and C1 status lines (line 5 of each) to the v3 text.
- Update time: 2026-10-19T10:31:59+08:00. STATE_VERSION 42dd639f. AS_OF 2026-10-19T10:31:59+08:00.
- Commits: 56d2876 (status line), c9f416d (timestamp stamp).
- Status line still carries the original publish time 2026-10-19T09:56:43+08:00 (per chair ruling, not changed).
- Bill's reported live hashes: HB 8c070700...a0bb, C1 187d4762...a734e, T4 3bae49ad..., LN aee7ecd6... (all matched below).

## Method
Blocks = lines strictly between BEGIN X / END X, LF-joined plus one trailing newline (same as PUBLISH-CHECK v2 delimiting).

## Results
| Item | Bytes | sha256 | Expected | Result |
|---|---|---|---|---|
| HB | 5832 | 8c07070061e341ba749e17c34faca914bd3c73a477ff02a4e2bf6a32987ba0bb | same | MATCH |
| C1 | 7792 | 187d4762b5d875e09e727c4481a40bbf20ee972d249fd45b8e56ceb72a6a734e | same | MATCH |
| T4 | 16196 | 3bae49ad8bc9c49f8850e1c19567a581d8a97f146dfbc8118070a70c37256485 | same | UNCHANGED |
| LN | 3948 | aee7ecd68944ce151ea02e8062c487c74285dbc929bae2fa3296e6f448de7125 | same | UNCHANGED |

- cmp live HB / C1 against PT-008 commit 1ba2a60 `PT008/round-012/publication/final/HB-PUBLICATION-FINAL-v3.md` and `C1-PUBLICATION-FINAL-v3.md`: byte-identical (sha256 equal).
- Block order on page: T4 (139-419), LN (420-479), HB (480-555), C1 (556-672). OK.
- Whole-page diff against my earlier verified copy (v2 publication, table.txt 09:56 version, saved in /workspace/r12/pub): exactly 7 changed lines: HB status line (485), C1 status line (561), and the page header/footer metadata lines (AS_OF x3, STATE_VERSION x2: lines 4, 10, 12, 14, 674). No other change.
- Required sentences ("Internally verified, not externally peer-reviewed." / "The general five-runner formula F5 remains UNFINISHED." / "This result does not prove the general Lonely Runner Conjecture."): present in HB and C1, in TXT and in HTML (HTML counts equal TXT counts after unescape: 6 / 2 / 2).
- "Not yet published": 0 in TXT, 0 in HTML. "FINAL CANDIDATE": 0 in TXT, 0 in HTML.
- HTML, after html.unescape, contains both HB and C1 blocks exactly equal to TXT blocks. Only display escaping (e.g. &lt;) differs.
- No token strings (github_pat, ghp_, Bearer, token) in page; no private data seen.
- No changelog text published as a section and no R012 track reports. The page only carries the in-lemma references "See EDITORIAL-CHANGELOG-R012.md" (kept in the approved text) and the "Track" wording inside Opus's proof text.
- Status line time is the original publish time 09:56:43, not 10:31:59. This is OK per chair ruling.

## Verdict
CONSISTENT. v3 is live and byte-identical to the approved v3 files; only the two authorized status lines (plus page AS_OF/STATE_VERSION metadata) changed.
