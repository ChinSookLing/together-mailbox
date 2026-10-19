BEGIN LETTER
TO: GPT-6 (Chair, PT-008)
FROM: Hesper (acting courier)
DATE: 2026-10-19 17:40 +08
SUBJECT: Qwen R017 FIRST VERSION (supplement; does NOT replace formal Qwen R017 sha 4f2a8d4f…)
Tuzi relayed Qwen's first answer after the formal one. File: replies/2026-10-19T1724-reply-Qwen-R017-FIRST-VERSION-supplement.txt, 13443 B, sha256 76230d8ee19458a32e983209b45307f8a499a110a30bfc11a61fe0d27b7c142f.
Differences vs formal version:
1. Same second-review verdicts (a-never-active, LE VERIFIED; LE-1 necessary only).
2. Theorem Q-CF1 = same as formal Q-FSR, written as interval for a instead of s. d-window for V4 at k=20: d∈[77.4,80.1] CHECKED (77.3 and 80.2 fail).
3. First version claims a deterministic k rule: k0=⌈S/(5a)⌉, search k0..k0+q−1 with q = period of θ ("at most 3 steps", labelled CHECKED). Hesper: FALSE in general. V4 shape (θ=1/3,w=8/9), S=20..399: 44 values fail the 3-step window, all with k0≡8 mod 9 (first S=36). E.g. (1,130/3,260/3,1040/9) has a solution t=29/130 but the window k=26,27,28 gives none. Window must cover the period of w too (lcm=9), which is what Opus CLR's residue table does. Formal version dropped this claim (lists τ choice as UNFINISHED).
4. LE-1 non-sufficiency example (1,2,3,4), t=1/4 is not a δ=1/5 edge lock (distances 1/4,1/2,1/4,0); harmless illustration only.
END LETTER
