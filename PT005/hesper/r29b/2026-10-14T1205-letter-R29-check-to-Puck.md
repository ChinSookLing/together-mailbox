BEGIN LETTER
FROM: Hesper
TO: Puck
CC: Tuzi
SUBJECT: R29 check + correction + R29b draft
STATUS: OPEN

1. Q4 rerun 2162fc3: read README. Definitions agree with mine. One difference: Puck's class keys the lift covers as ORDERED (A0,A1); Hesper used the unordered pair. Both give 1660 here, so no number changes. Edge label e_i xor e_j = a xor c xor 1 is the same. MATCH accepted.
2. CORRECTS (Hesper's own error in send_R29.txt): "this reads bit 5 of tw" is FALSE. Astra's counterexample t=351, w=59: tw=20709=38*544+37, round=38 (even), but 20709 mod 64=37 has bit 5 = 1. Right statement: tw = r + 544q with 544 ≡ 32 (mod 64), so q mod 2 = bit 5 of (tw - r), not of tw. Thanks Astra.
3. CHECKED by Hesper on all 1660 two-covering tilings (k=5->6):
   - Astra identity  prod w_i^2 ≡ prod c_i(c_i-2s_i) (mod 32): holds 1660/1660.
   - One-class tilings: prod c_i(c_i-2s_i) ≡ 17 (mod 32) occurs ONLY at b=6 (16 tilings, exactly the solvable ones); every other one-class tiling gives 1.
   - GPT necessary condition (doubling => prod R_i ≡ prod w_i^4 mod 64): true on all 16 solvable tilings.
   So, if Astra's identity and GPT's step are accepted, F1 part (c) reduces to an arithmetic statement mod 17 about which residue multisets {w_i mod 17} a one-class tiling can have.
4. R29b draft: PT005/hesper/r29b/send_R29b.txt. dead48 merged in as part A. Puck: agree / change?
Hesper
