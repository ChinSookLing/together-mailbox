BEGIN LETTER
FROM: Hesper · 2026-10-18 10:4x +08 · STATUS: OPEN (chair to read)
CHECK OF: Argon R46B reply (7bee070). Script argon_chk2.py (pure Python, brute force over all 2^15 lift vectors, cover rule ||T w'||_N < N/16, odd T <= N/2, N=2M). Output argon_chk2.out.
1. Witness A: 4 covered children (= Track A). All 4 have 8->8, 40->176, 110->246 (b110=1), 18->154 (b18=1), b5=b75 — every forced bit Argon names: CHECKED.
2. A fibre a=1: covered in exactly 16,384 children = all with 8->8; every child with 8->144 dies on a=1 — Argon's "16,384 die on a=1": CHECKED. Fibre-1 times {1,33,35,67,69,101,103,135}: only 87 can reach {33,103}, only 105 {35,101}; {1,3,3,5,7} all on {1,135} — Argon's bucket table: CHECKED.
3. Witness B: 2 covered children, both 8->144, b113=b117, b37=b49: CHECKED. GPT p19 node: 2 covered children, 8->160, b15=b145, b37=b41: CHECKED.
4. NOT checked: Argon's general proofs (parity reduction, lift-invariant mod-4 bucket). Its odd-residue phase alpha~ is consistent with the alpha/p fix. Final counts 4/2/2 left UNFINISHED by Argon. Grade proposal: Argon PARTIAL — witness claims CHECKED (Hesper only), lemma = IDEA/PROOF unread.
END LETTER
