# PT-008 R010 · Puck exact check of Opus Track A (Connect the Boxes)

Script: puck_check_R010_A.py (exact Fractions). Output: puck_check_R010_A_output.txt. 11 checks + 2 extra, 0 failures.

## Confirmed
- A3 half-lock box HB, t = 3/(2(b+c)): succeeds at all 77,531 exact grid points of s in [15/8,15/2], r in (1,8/7] and [4,13/2], w in [4/5,6/5], closed edges included. The hand proof B3 reads correctly line by line.
- A4 connected region C1 and its one-comparison rule (frac(w) in [1/5,4/5] gives 1/(b+c), else 3/(2(b+c))): succeeds at all 206,040 exact grid points of the box (115,120 of them inside the corridor; HB branch used 79,560 times). The boundary w = 6/5 works for both outputs, so the join has no gap.
- Corridor in coordinates, 4/s < w < 4r/(1+r): equivalent (a = 1 scaling).
- A2 obstruction: on w = 1, 2, 3 every integer lock k/(b+c) gives ||dt|| = 0. Examples (1,3,4,7), (1,2,3,10), (1,6/5,4,78/5) are in the corridor. (1,3,4,7) works at t = 1/5 (tau = 7/5), and it is not in C1. The C1 example (1,2.16,2.34,4.5) works at t = 1/3.
- These are grid checks in support of the proof, not a completeness claim.

## Puck flag (not a grade)
- ANSWER BLOCK and Sec.C1 say the exact obstruction set of the LB family is the three surfaces w in {1,2,3}. That is too strong: Puck found corridor points with NON-integer w where every LB(k) also fails, e.g. (3,5,11,24) (w = 3/2, all k mod 16 fail; works at t = 67/1000) and (1,7,9,24) (w = 3/2, all k mod 16 fail; works at t = 1/5). The surfaces are where LB fails for the reason in A2, but they are not the whole LB failure set. The A2 theorem and its corollary themselves are fine.
- C1 is a thin slab: it needs 1 < c/b <= 8/7.
