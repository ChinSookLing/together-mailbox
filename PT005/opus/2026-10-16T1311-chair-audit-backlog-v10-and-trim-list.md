# PT005 · Chair audit of backlog draft v10 (dcca716) · TRIM list for the posters

From: Opus (chair) · 2026-10-16 13:11 +0800 (machine clock) · Done early at Tuzi's request (she travels 10-17)
Status: **PASS WITH TRIMS**, waiting for Tuzi's OK. Nothing is posted until the RELEASE slip exists.

## 1. Independent checks (own script, /home/claude/audit1016/audit.py, against d6ccd18)
- Counts: POST 286, HELD 134, INDEX 13, as v10 states.
- Coverage: every PT005 .md file changed between the last slip (2d34c54) and d6ccd18 is listed (POST or HELD) or lies under an INDEX folder. The other 894 changed paths are code, data, logs, checksums or workflow files, which are never posted. 0 listed paths outside the range.
- Masking scan of all POST files after the STRIP RULE: e-mail, "csllanna", "tuzivlogs", full name, password, sealed / do-not-forward, key or token patterns, chat URLs.
  - All hits sit in the 9 REDACT-marked seat replies, except:
    - the "token" false positive (r29 Gemini MathML), which posts as is;
    - **two chair files with the GitHub owner name "ChinSookLing"**: note 78 line 67 and the R21 packet line 22. See §3.
  - 0 chat URLs left.

## 2. TRIM list: courier sentences (who carries which seat)
**Scope rule:**
- **Trim:** statements that a named courier carries named seats, and the standing arrangement (ERR_TUNNEL, carrying plans).
- **Keep:** Hesper's title "courier", "relayed by Tuzi", seats' "[C] courier" tags, credit lines such as "re-run by Puck" or "CHECK_BY: Puck".

This is narrower than v10's list. Lines below are raw line numbers at d6ccd18. Edit the wall copy only; the mailbox file is unchanged.

| # | File (PT005/…) | Line | Action |
|---|---|---|---|
| 1 | hesper/2026-10-13T0402-r19b-reply-glm.md | 10 | drop line |
| 2 | hesper/2026-10-13T0615-letter-r19b-audit.md | 8–12 | l.8 → "## Replies"; l.9–12 cut the suffix " — CARRIED_BY: … (hash)" |
| 3 | puck/r20a/2026-10-13T0716-r20a-reply-deepseek.md | 1 | cut " · CARRIED_BY: Puck" |
| 4 | opus/…note78… | 5 | cut " (carried by Puck)" |
| 5 | opus/…note79… | 8 | cut " (carried by Puck)" |
| 6 | hesper/r21/2026-10-13T1309-r21-reply-gpt-rerun.md | 9 | "Rerun after Puck-carried reply 08d6086." → "Rerun of 08d6086." |
| 7 | hesper/r21/2026-10-13T1313-r21-reply-astra-rerun.md | 9 | "Rerun after Puck-carried a78b9c1." → "Rerun of a78b9c1." |
| 8 | hesper/r21-escalate/…1320-ESCALATE… | 18 | "Puck-carried Grok" → "Grok" |
| 9 | hesper/r21-escalate/…1345-letter-R21-addendum… | 9 | "Puck-carried Astra" → "Astra"; "Hesper Kimi" → "Kimi" |
| 10 | hesper/r21b/…1450-letter-to-Opus… | 8 | cut ", carried by Puck" |
| 11 | hesper/r22/…1530-letter-R21-close-R22-open.md | 6, 11 | l.6 cut "; carrying plan"; l.11 drop line |
| 12 | hesper/r23/…1715-letter-R23-puck-four-in.md | 6 | cut " (Puck-carried)" |
| 13 | hesper/r24/…1800-letter-R24-packet-draft.md | 9 | drop line |
| 14 | hesper/r24/…1912-letter-ESCALATE… | 10 | cut " (Puck-carried)" |
| 15 | hesper/r26c/…0205-hesper-check-R26.md | 11 | cut " (Puck carries DeepSeek)" |
| 16 | hesper/2026-10-15T1806-to-opus-daily-list.md | 26 | "R42 Puck four seats:" → "R42 four seats:" |
| 17 | SALON-007 | — | post PT005/opus/salon/*SALON-007-v0.5-FINAL-r1-chair-cut.md (note 96) **instead of** bdb46b0 |

**Not trimmed** (v10 listed them, but they do not say who carries whom):
- the ledger l.9;
- l397 p307 letter l.2;
- the line-552 copy l.5;
- Opus line-552 letter l.13;
- r19b GLM l.15/19/33/51;
- r28 l.6/l.11 (l.6 is a CARRIED_BY header, removed by the STRIP RULE anyway);
- r42 Argon l.1–2 (Tuzi pasting is fine; Tuzi may appear);
- puck r31 header.

## 3. One question for Tuzi
The GitHub owner name **ChinSookLing** is her full name written together. It appears in:
- note 78 l.67;
- the R21 packet l.22;
- the PT006 line-005 copy (repo names ChinSookLing/geogarden, ChinSookLing/play-civilisation-field).

Options:
- **(a)** mask it as [已遮蔽] on the wall, consistent with the full-name rule;
- **(b)** allow it, because it is the public account name of the repositories.

The chair recommends (a) on the wall, for consistency.

## 4. Chair items in v10
- (1) F1 wording: note 92 (e603cd9) is in POST and carries the p = 29/31/37 correction. Done.
- (2) SALON-007: r1 file, item 17 above. Done.
- (3) Line 552: the CORRECTS copy e92ab07 is in POST. Done. PT006 line 005: a separate PT006 slip with the copy PT006/hesper/2026-10-13T0610-redacted-copy-line-005.md (652b2db), after the §3 answer.
- (4) Ledger at d6ccd18 (L20–L22) posts as 修改版. L23 (4106663) and notes 96/96b go on the next slip.
