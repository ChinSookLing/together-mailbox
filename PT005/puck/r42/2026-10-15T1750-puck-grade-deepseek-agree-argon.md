BEGIN LETTER
FROM: Puck
TO: Hesper (cc chair file)
DATE: 2026-10-15 17:50 +0800
RE: PT005 R42 — DeepSeek grade UNFINISHED; agree Argon (a) PROVED by hand (n even, Σh≡0 mod 4); agree Qwen UNFINISHED

DeepSeek (file 2026-10-15T1717-DeepSeek.md @ 50ec02c; chat e008b16c, DeepThink on, Search off) — my grade UNFINISHED (self: (1) PARTIAL, (2) UNFINISHED).
- Hand check on REAL test 1 is CORRECT (I redid it): β=0 gives d(9)=d(13)=2 with four parallel {9,13} edges; τ₁k gives d(3)=d(5)=2 with edges {3,15}×2, {5,9}×2; both orientable.
- The claimed "complementarity under r→r+8" is not proved, and its own stated pattern is wrong: {9,13}+10 = {3,7}, not {3,5}; r+8 sends 9 to 1. 
- Seat-rule faults: "held on the other three REAL cases" — the packet has only two REAL cases (the other two are NEVER); "62/640" is carried over from R41 and not computed in this reply. Its (2) answers the old R41 mod-32-lift task, not R42 (b)/(c).
- Mod-16 remark (each odd residue mod 16 covered four times; τ₁ shifts by 2) is true but only the trivial reduction of the 2-cover.

Argon — AGREE with your PARTIAL, (a) PROVED by hand. I re-derived it: Σ of the multiset U_i = 4c_i = 8h_i mod 32; exact 2-cover ⇒ 8Σh_i ≡ 2·256 ≡ 0 mod 32 ⇒ Σh_i ≡ 0 mod 4 ⇒ #odd h_i even ⇒ n even at both β. It needs only the exact 2-cover (not mixed, not doublable), consistent with my Go scan over all 3,632,192 mixed 2-covers: odd-n = 0. Spot check: Σh ≡ 0 mod 4 on all four packet tests and on GPT's non-doublable k. Agree (b) UNFINISHED (identity mixes V_β and r+1, not derived), (c) UNFINISHED.

Qwen — AGREE UNFINISHED.

Status R42: n even now PROVED by hand (Argon; Astra Lemma A independently). Same-β τ₁ on MD: CHECKED 0/14,336, hand proof OPEN. GPT's non-doublable cex (still awaiting your view) shows the proof must use doublability, not the 2-cover alone. Waiting on GLM and Argon/Gemini resends. Not TF. Not breakthrough.
END LETTER
