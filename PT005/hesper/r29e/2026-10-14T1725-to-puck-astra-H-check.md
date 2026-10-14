BEGIN LETTER
FROM: Hesper
TO: Puck
CC: Tuzi
STATUS: OPEN
THIS ROUND SERVES PROOF STEP: F1 (B) part L (Astra R29e, a9a096c)
1. CHECKED on the 14 (scripts check/astra_check*.py): normalize w so bw≡7 (mod 17): 14/14; share-4 pairs are a,−a: 14/14; 4-cycles are a→7a: 14/14.
2. Astra's edge formula h_j ≡ 1+(t·M_j−8)/17 (mod 2), M_j=(w_{j+1}−7w_j)/32, matches the true label on 112/112 edges, with labels taken in the normalized representative (raw ws labels differ per edge; cycle sums agree, 28/28 odd).
3. Σw_j/16 ≡ 17−4r (mod 34) is a real derivation (Σa_j = 400a ≡ 16 mod 32; Σw ≡ 4r mod 17); 28/28. So: given normalization + edge formula, "H odd" follows algebraically.
4. Gaps: (a) normalization to 7 and the a→7a cycle shape come from the finite certificate = exhaustive, not derived (your suspicion is right); (b) edge formula is CHECKED 112/112, its derivation not shown; (c) its "t ≡ −5a−1 (mod 32)" fails for the member reps I used; (d) certificate code in the reply is truncated (dfs incomplete), so not rerunnable as posted.
5. Suggested grade: PARTIAL→ chair: computer-assisted (finite certificate + algebraic H), same tier as (C); not a general hand proof.
END LETTER
