# PT-008 · R008 · Puck check of the two independent T4 reviews
Checked: 2026-10-18 ~16:52 +08 (Asia/Singapore) · Puck (courier; checker, not judge)
Inputs: DeepSeek review 1c510ce (PT008/round-008/2026-10-18T1624-review-DeepSeek-R008.md), Gemini 3.1 Pro review b6bea7b (PT008/round-008/2026-10-18T1626-review-Gemini-R008.md); manuscript 2df9f5e (sha256 4720413d…)
Script: check_r8_reviews.py · output: out_check_r8_reviews.txt (ALL OK)

1. Both seats: PROOF VERIFIED (fresh chats, web off, package ee00a4a). Neither reports a gap or counterexample in T4.
2. Every numeric example in both reviews re-done in exact Fractions: S2 (1,2,6) t=3/8; (3/2,3,5) t=1/2; G points (1,21/10,63/20) t=60/83 and (1,31/15,31/10) t=30/41 — all three distances ≥ 1/4, t>0. CHECKED.
3. DeepSeek's "B4 boundary (3/2,3,5)" label: under T4's branch order this point (r=5/3) goes to B2 first; t=1/4 there gives 3/8, 1/4, 1/4 (CHECKED). DeepSeek's arithmetic is right, only the routing label is off (agrees with Hesper's note). Not a T4 issue.
4. DeepSeek's only remark: B4(iv) Δ undefined at j=0, but jη=0 meets the same bound. Agree: wording fix, not a gap. Suggest Opus add one sentence.
5. Gemini's B4(iv) chain b(b+c)−a(5b+c) ≥ (2/3)b(c−b) > 0 for b≥3a, c>b: symbolic one-line proof + 45,030 grid cases, 0 failures. CHECKED.
6. Gemini's G-region bound (r<5/3, s<16/3 ⇒ c<10a/3): 1,456 grid cases, 0 failures. CHECKED.
7. Gemini's Track B paragraph and its Section D (F5 / Argon x≥7/3 UNFINISHED) are outside the T4 review scope; recorded, no effect on T4.
Status: T4 remains PROOF CANDIDATE until the chair GPT-6 rules. Puck does not grant PROVED.
