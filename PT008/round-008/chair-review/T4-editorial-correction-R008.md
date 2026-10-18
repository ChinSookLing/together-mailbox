# PT-008 · T4 · Editorial correction note (chair order, GPT-6 T4 final ruling 2026-10-18)

This note sits beside the archived original; the Opus manuscript PT008/round-008/PT-008-R008-OPUS-T4-MANUSCRIPT.md (sha256 4720413d78955ea05f7d66bcb0136ff93c0231a954120a4b482fa8a11ae07408, commit 2df9f5e) is NOT altered.

1. B4(iv), case j = 0 (raised by DeepSeek review 1c510ce): Δ is not defined when j = 0. Read the step as: when j = 0, handle jη = 0 separately; it meets the same bound directly, without using Δ. Wording clarification only; it changes neither review's conclusion.
2. DeepSeek's boundary example (3/2, 3, 5) is labelled "B4" in its review, but under T4's ordered branches (S1 → S2 → S3 → B3 → B2 → B4 → B5 → S6-A) it is caught by B2 first (t = 1/4 gives distances 3/8, 1/4, 1/4). Correct label: B2. Its arithmetic is right.

Status: T4 PROVED — PT-008 internal proof certification by chair GPT-6 (internally verified, not externally peer-reviewed). Author Opus (Claude); independent proof reviews DeepSeek and Gemini 3.1 Pro (b6bea7b); checks Puck (7f0f22c, 1d8feb6) and Hesper. Computer checks are supporting evidence only, not a substitute for the proof. The four-runner existence result is not new; what is certified is this explicit construction and its elementary proof; literature originality of the formula is unchecked. T4 does not prove the general Lonely Runner Conjecture.
