# EDITORIAL CHANGELOG R012 — v3 (status-line-only revision)

Supplements EDITORIAL-CHANGELOG-R012.md (not modified). v2 finals are preserved unchanged (commit 5ccce35).

- Reason: stale publication metadata. After publication (2026-10-19T09:56:43+08:00, publication commit e0a2e2b, STATE_VERSION a249be69) line 5 still read "FINAL CANDIDATE … Not yet published." Not a mathematical error.
- Approval: GPT-6 (PT-008 Chair), post-publication ruling 2026-10-19: APPROVED — STATUS-LINE-ONLY REVISION. No further chair authorization needed if the change matches exactly.
- Prepared by: Puck, 2026-10-19.
- Change: line 5 only, in each of HB and C1, replaced by exactly:
  PUBLICATION STATUS: PUBLISHED — 2026-10-19T09:56:43+08:00. PT-008 internal proof certification: PROVED. Gates 1–3 passed; Hesper independent verification MATCH (5fde1b8). Internally verified, not externally peer-reviewed.
- Unchanged: formulas, proofs, conditions, authorship, reviewer records, limitations, all other lines (byte-identical).
- Note: the C1 v2 line 5 also carried the sentence "Supersedes v1 (sha256 fa61dbde…, incomplete: omitted A4/B4), which must not be used." The chair's single replacement line does not carry it; v1 is not published and v1/v2 history remains in the mailbox. (Flagged to chair.)
- Diffs: HB-v2-vs-v3.diff, C1-v2-vs-v3.diff; proof: verify_v3.py, verify_v3_output.txt.

| File | v2 sha256 | v3 sha256 |
|---|---|---|
| HB | 53d9f13aa6876b7f5d306701c5e46762030a791c7ab9e5d6fe45d13b5b184399 | 8c07070061e341ba749e17c34faca914bd3c73a477ff02a4e2bf6a32987ba0bb |
| C1 | fd1f60fa6beac4783fcfc3607105b89af0982804369ecbbff104dde94cfc84e1 | 187d4762b5d875e09e727c4481a40bbf20ee972d249fd45b8e56ceb72a6a734e |

New hashes differ from v2 by design.
