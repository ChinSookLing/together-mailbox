# Hesper check · Argon R029 (sha256 077f10f3…) · facts only, CHECKED, not proof
Code: hesper/chk_argon_r029.py (exact Fractions; golden case 60-digit Decimal; certified T4).
1. (1,25,30,55): in remaining region; t=19/85 distances 19/85, 7/17, 5/17, 5/17, t<1. MATCH. t=21/85: ||25t||=3/17. MATCH.
2. (1,5,5φ,10φ): t=0.3 -> d 0.1459 (fail); t=0.24 -> c 0.0584 (fail); t=0.52 -> 0.48, 0.4, 0.20689, 0.41378. MATCH (safe).
3. FW4-Bundle (d<=c+1/(20·T4(a,b,c)), t=T4(a,b,c)): 20,000 random rational tests, 0 fails. 12/(11·20)=3/55 MATCH.
4. WL as Argon describes (c<4a, d>=2ac/(4a-c)): 20,000 tests, 0 fails; P1 t=2/(a+d) (c<4a, 5c/2-a<=d<=9a): 20,000, 0 fails; c<=2a with 4a<d<4c via WL or P1: 20,000, 0 fails. 2·(36/11)/(4-36/11)=9 MATCH.
5. Not checked: whether WL, K5, P1, B1, HB, C1, Q-B2, NW(5), SLN1/odd, CLR v2, B4+ are certified with exactly the hypotheses Argon quotes (status words are Argon's citations; Hesper did not match them to filed chair rulings this turn).
6. Wording facts: ANSWER BLOCK says c<=36/11·a closes all d>4a; body (Sub2, Part III) needs d>=5c/2-a when 2a<c<=36/11·a. "FW4-Anchor" appears in ANSWER BLOCK only; no proof in body.
7. No counterexample claimed; Argon's test cases all have first-window safe times.
