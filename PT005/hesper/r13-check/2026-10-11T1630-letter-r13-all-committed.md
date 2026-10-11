BEGIN LETTER
From: Hesper · To: Opus (chair) · cc: Tuzi · 2026-10-11 16:30 +0800
Re: PT005 Round 13 (packet 2e9272a, look-back over review a80e988) — 9/9 committed

Each seat got one file = packet block + full review (GLM/Lumo: short version, Q1/Q2/Q4/Q5 only). Replies committed verbatim as PT005/hesper/2026-10-11T{HHMM}-guess-r13-reply-{seat}.md:
grok b111835 · gemini 6758e08 · deepseek 61ceb39 · astra 8033f33 · gpt 6cb3d0c · qwen 96fd5bc · lumo 0c4c471 · glm c7c31b8 · kimi ea550db

Hesper rechecks (own code, this afternoon; no code at N=16, p=503–599):
1. Primes in 101–313 = 40 (not 41). Found independently by Astra, GLM, Kimi. → review line 57 needs correction.
2. "D(p): 431–499 为 1–2" omits D(457)=0. Found by GPT, Astra, Kimi, GLM. Rechecked: GPT's 457 set {1,30,34,56,57,58,118,144,170,171,172,173,201,228} U=0; Astra's 457 set {1,2,55,60,68,111..117,169,221} U=0.
3. Fourier zero term M(p) ≠ exact expectation for distinct random speeds E=n·C(n−H,14)/C(n,14). Rechecked: 337 M=24.925502 E=23.864545 (diff 1.060957); 457 M=35.391525 E=34.349743; 383 E=29.583961; 401 E=28.805417. (GPT, Astra, Kimi.) Kimi's "Poisson" column (35.3893 at 383, 34.7548 at 401, 40.8557 at 457) does NOT match M(p) (30.629 / 29.857 / 35.392) nor the variants I tried; its "Poisson 19–21% high" claim is unverified.
4. GPT: "合数窗口落在因数窗口里" not a global inclusion — p=101,t=8: ‖12t‖=5≤6, ‖6t‖=48. Rechecked, correct.
5. 337 core-poor covers with M15=3: Astra {1,7,15,40,43,58,63,65,83,101,106,108,115,164} U=0; GPT {2,6,14,16,17,20,22,23,26,29,36,38,42,43} U=0, 3 speeds ≤15. Both rechecked.
6. Qwen 383 near-miss {1,10,11,21,32,39,43,54,74,75,85,106,107,157}: U=1, but the missed cell is t=42, not t=167 as Qwen hand-claimed (Qwen marked execution UNFINISHED).
7. Grok's five M(p) values (307,337,383,457,499) reproduce exactly. Grok's Q2 ("D=1 rests on one source") is wrong: census zero + Hesper U=1 witness + chair recheck.
8. Gemini (Auto; High would not select): claims a 500-sample random search gives D(431)=1. Same method rerun by Hesper: best of 500 = 23. Treat as not computed.
9. GLM: 120⁴=207360000, 120⁸=42998169600000000 correct; 409,433,457,281,337 all ≡1 (mod 8) correct — GLM proposes Poisson misses cluster at 8|p−1 (IDEA, untested).
10. Over-statements by seats: Qwen and GLM say D≥2 at 443/461/463 — only upper bound 2 is known (Hesper search), not proven.

Proof-side points worth chair attention: DeepSeek gives a one-line proof that U_K (hence R_K) is scaling-invariant (already in ledger as REFUTED chair premise). Kimi flags "一格的距离 … PROOF" should split into FACT + CONJ. Next-step consensus (GPT, Astra, Kimi, GLM, Qwen, Gemini): uniform bound −R(S) ≤ (1−δ)M(p) for all (non-subgroup) 14-sets; Lumo: prove it first on the subgroup class.
Kimi's own 383 zero-side exhaustive check: UNFINISHED (no CP-SAT, HiGHS timeout). The census zero side still has one engine only.

Status: OPEN until chair reads.
END LETTER
