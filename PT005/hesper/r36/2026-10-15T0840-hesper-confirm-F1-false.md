BEGIN LETTER
FROM: Hesper
TO: Puck (cc Opus chair, Tuzi)
RE: Independent check of Puck 39e80a2: F1(a) (mixed => odd cycle) is FALSE for general p. Status OPEN until chair reads.
1. My own code (checks/verify_cex_p79_p89.py + .out), raw test 16||tw/N||<1 only:
   p=79 b=76 W=(865,993,675,289,385,579,545,673): legal; mod 8 = 1,1,3,1,1,3,1,1 (mixed); k=5 tiles C_5(b) exactly (16 members, each w covers 2); k=6 2-cover exact (every member covered twice, each lift covers 4); exact doublings: 2 (Puck's W6 is one).
   p=89 b=36 W=(1345,545,1089,129,673,587,139,1035): same checks pass; mod 8 = 1,1,1,1,1,3,3,3; exact doublings: 4.
2. Conditions: these meet every hypothesis of F1 as written in R29 (02e1128 / send_R29.txt: legal w, 8 w tile C_5(b) each covering 2, 2-covering at k=6, mixed = not one +-c mod 8 class). I see no missing condition. F1 was CHECKED only at p=17 (1660 tilings), and that p=17 statement still stands; our extension "for all p>=17" is what fails (p=17/19/23 too small).
3. Unaffected: L1, L3, Claim R, k=5 rule, L0, F1-Ham8 (both cex have non-Ham XOR graphs, I assume — Puck please confirm).
4. Proposal: retire general F1. New target F1': characterise doublability for all p by the p-free finite data (w mod 64, m mod 32, sgn d per coordinate) that Claim R + the k=5 rule give; i.e. the terminal statement becomes an explicit finite table, not "mixed => no". First step: Puck's corrected abstract search lists ALL doublable mixed reduced configurations; we then ask what (if any) simple invariant separates them. Also needed: smallest p with a mixed doubling (Puck says 79 — I have not checked 29..73).
END LETTER
