BEGIN LETTER
FROM: Hesper
TO: Puck (cc chair file, OPEN until chair reads)
DATE: 2026-10-15 13:35 +0800
RE: PT005 R38 Argon (Puck c96008f / 944ae34) — grade agreement + two notes

1) AGREE: (A) PARTIAL. F1'' (dim ker L = dim ker L0) is the signed-Laplacian restatement of F1', correct, not new structure. Ham-8 vertex-sum reduction is a valid lemma but low priority: F1-Ham8 is already PROVED (R34) and our exhaustive (c,v) table (9a4a4be/09e0e98) has no mixed doublable (2^8).
2) AGREE: (B) PARTIAL-strong; constructions CHECKED 3/3 (your reruns). Stability lemma p>768: PROVED with one side condition to state explicitly: the interval gives >=4 candidates in the class mod 32 and at most 3 are excluded (w mod P in {0,+-1}), so only >=1 is guaranteed per coordinate. If two coordinates share identical (m mod 32, w mod 32, sgn d) they need distinct w; then require p > 6*32*(3+mu) (mu = max multiplicity of identical data; worst case p > 2112), or check that no realized config has repeated full data. With that, PROVED.
3) KEY CONSEQUENCE (proposed R39 core, Hesper): the lemma makes the realized set monotone: anything realized at any prime is realized at every p > p0. So the set realized at ONE prime above p0 equals the union over all primes. One exact k=5 layer computation at P=769 (or above 2112 if mu>1): if it gives 640 = the 5 affine orbits, the "only 5 of 39 orbits / 5 of 11 classes" statement becomes a THEOREM for all p > p0 (lemma + finite check), and p in 67..p0 is a finite, checkable range. This is the clean route to R38(c), better than asking a seat to lower 768.
4) Seat identity note: this answer came from the ChatGPT tab "Prove F1 Criterion". Tuzi's Gemini Argon chat (ac0b48d…) is separately running R38 since ~13:05. Keep the two answers labelled by platform; both stay R38. Capture is a translation, not verbatim.
No breakthrough. No TF.
END LETTER
