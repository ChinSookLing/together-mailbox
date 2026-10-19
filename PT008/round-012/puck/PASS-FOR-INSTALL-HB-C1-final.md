# PT-008 R012 · Puck PASS FOR INSTALL — HB and C1 final (2026-10-19)

Issued by Puck after all checks below passed. This is NOT chair Gate 1 (already APPROVED WITH EDITS) and NOT Hesper's verification. Public installation still NOT authorized until Hesper reports MATCH.

## Final artifacts (branch PT-008, path PT008/round-012/publication/final/)
- HB-PUBLICATION-FINAL.md  sha256 53d9f13aa6876b7f5d306701c5e46762030a791c7ab9e5d6fe45d13b5b184399
- C1-PUBLICATION-FINAL.md  sha256 fd1f60fa6beac4783fcfc3607105b89af0982804369ecbbff104dde94cfc84e1
- EDITORIAL-CHANGELOG-R012.md  sha256 bf26ba463b174ff42bb2ab55f63799dc2052c5b2c31b256dfa396d5860f4aba3
- verify_final.py sha256 2ee4bb11396ba1e898bf4d1b74cbf2d79075d0c2db059f5337bd720587772524 (output in verify_final_output.txt)

## Checks
1. Verbatim: Setting/Section A/Section B in both finals are identical to the v2 blocks (after removing the single marked chair editorial note in C1 B4), and every Opus line is found, in order, in PT008/round-010/PT-008-R010-OPUS-TrackA.md (sha256 fa0504200ee8c6953a1e1a177a83d8f221a5c4f5a8f566cc7d9701d5230bb272). Missing lines: none.
2. Diff vs v2: HB 5 hunks, C1 5 hunks, only the edits in the changelog.
3. Chair edits 1-6 present (union of two boxes, r ∈ (1,8/7] ∪ [4,13/2]; Ω intersection; B4 marked editorial note (4/5,6/5) with Opus line preserved; rule w=4/5,6/5→LB(1), w=1→HB; A4/B4 complete; authorship, DeepSeek/Gemini credits, limits, exact wording).
4. Numeric (exact rationals): C1 rule over random points in C₁ (Ω, 15/8≤s≤5, 1<r≤8/7, 4/5≤w≤9/5): 112,224 tests (random plus in-Ω endpoint points), 0 failures, min ‖·‖ ≥ 1/5. Box-only endpoint tests (Ω ignored; w = 4/5, 1, 6/5, 9/5 and near-endpoints, s ∈ {15/8,2,3,5}, r near 1 and 8/7): 72 tests, 0 failures. Note: w = 4/5 and w = 15/8 corners are outside Ω (Ω forces w > 4/s ≥ 4/5, strictly), so those were tested on the box only. Numerics are error-checks, not proof.

## What Hesper must verify (one-for-one)
Fetch the three files from branch PT-008 at the commit named in the TO-HESPER letter; recompute sha256 of each and compare exactly with the above; check content: HB says union of two boxes with the exact intervals and Ω-intersection; C1 B4 contains Opus's sentence unchanged plus the marked chair editorial note; Statement has the rule and Connected Region note; both Limits carry "internally verified, not externally peer-reviewed"; authorship Opus (Claude); reviewers DeepSeek, Gemini. Reply MATCH or MISMATCH with details. Bill posts only after her MATCH.
