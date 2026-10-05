SEAT · REPLY_TO: chair note 24  
Read: only the supplied PT005-DEEPSEEK-L7-PACKET; no other account records.

SUMMARY  
FACT: Astra’s lemma is algebraically sound under its stated hypotheses.  
FACT: Q1(a)–(e) check out; the D=8 table is correct; the open-arc/ceil bound has no off-by-one.  
FACT: Use in Lemma 2.2(ii) is fine if D | L·p determines the relevant gcd/divisibility and no grid-time witness is required.  
ESTIMATE: The only real gap is application-side: the packet does not show e ≥ 2 for every improper lift.  
VERDICT: HOLDS as a conditional lemma; INCOMPLETE for the full Lemma 2.2(ii) use unless that e ≥ 2 check is supplied elsewhere.

Q1  
(a) FACT. Write u_i = g_i a, D = g_i D_i, with gcd(a,D_i)=1. As q runs 0,…,D−1, the shift u_i q/D = a q/D_i mod 1 depends only on q mod D_i. Each residue mod D_i occurs exactly g_i times. Since a is invertible mod D_i, a q mod D_i runs through all D_i residues. Hence D_i distinct points, each visited exactly g_i times.

(b) FACT. Let N = D_i. The grid spacing is 1/N. An open arc of length L = 1/8 contains at most ceil(N/8) grid points. If N = 8k, the arc length is exactly k spacings, and an open interval of that length cannot contain k+1 points because the endpoints would be separated by exactly the length. So max k = ceil(N/8). If N = 8k+r, 1 ≤ r ≤ 7, max is k+1 = ceil(N/8). If N < 8, ceil(N/8)=1, and two grid points are at distance at least 1/7 > 1/8, so at most one. The bound is correct.

(c) FACT. The bad set is “distance < 1/16”, an open arc of total length 2/16 = 1/8. Points at distance exactly 1/16 are not counted. Therefore a shift q not in the forbidden union gives distance ≥ 1/16, which is allowed.

(d) FACT, with context caveat. For i ∈ E, g_i < D, so g_i ceil(D_i/8) ≥ g_i D_i/8 = D/8. Hence S_D ≥ eD/8. Since S_D < D, e < 8, so e ≤ 7. Given the context’s 15 non-zero speeds, |B| = 15−e ≥ 8, so B is nonempty. Also |B| = 15−e ≤ 13 because e ≥ 2, so B has at most 13 distinct values. If the total count 15 were not assumed, B nonemptiness would not follow from e < 8 alone; the packet supplies this via the 16-runner/15-speed context.

(e) FACT. LRC(m) gives a real time where all B-speeds are at distance at least 1/(m+1) ≥ 1/14 > 1/16. By continuity, there is an open interval around that time where all B-speeds remain > 1/16. Rationals are dense, so choose rational t_0 in that interval.

Q2  
FACT. For D = 8, on E:  
- odd u_i: gcd = 1, D_i = 8, summand = 1·ceil(8/8)=1.  
- u_i ≡ 2 mod 4: gcd = 2, D_i = 4, summand = 2·ceil(4/8)=2·1=2.  
- u_i ≡ 4 mod 8: gcd = 4, D_i = 2, summand = 4·ceil(2/8)=4·1=4.  
- u_i ≡ 0 mod 8 is in B, not E.  
So S_8 = a + 2b + 4c is correct.

Q3  
FACT. If D | L·p and u ≡ w mod L·p, then u ≡ w mod D. Thus D | u iff D | w, and gcd(D,u) = gcd(D,w mod D). So the residue class mod L·p determines the needed divisibility data and the g_i.  
FACT/IDEA. Nothing in the quoted property requires the witness time t to lie on the grid (L·p)^{−1}Z. Lemma 2.2(ii) asks for “some t”; Astra’s t_0 + q/D is rational but need not be on that grid. Astra’s “no” is correct under the quoted use. If some external gate-closing step demanded a grid witness, that would be a different requirement not present in the quoted context.

Q4  
FACT. The lemma assumes e ≥ 2. The proof does not derive it. In the Lemma 2.2(ii) application, one must verify that every improper lift w has e ≥ 2 for the chosen D. The packet does not show this. If an improper lift has e = 0 or e = 1, the lemma cannot be applied, and LRC(15) or LRC(14) would be needed instead.  
FACT. The “15−e ≤ 13” count relies on the total number of non-zero speeds being 15. The lemma as quoted omits that total, but the surrounding context supplies it.  
FACT. No off-by-one found: the strict inequality S_D < D, the open bad arc, and the ceil(D_i/8) bound all match.  
ESTIMATE. No other hidden assumption appears. Duplicate speeds in B can be reduced to distinct values; negative speeds do not matter because ||t u|| = ||t (−u)||.

Q5  
VERDICT: HOLDS as a conditional lemma, with the stated hypotheses. The application to Lemma 2.2(ii) is INCOMPLETE as presented, because the packet does not establish e ≥ 2 for every improper lift. If that check is supplied elsewhere, the use is sound.