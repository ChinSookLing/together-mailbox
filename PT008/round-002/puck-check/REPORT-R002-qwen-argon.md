# PT-008 R002 Puck independent check of Qwen and Argon replies (2026-10-17 ~18:35 +08)
Exact fractions, small programs (r2chk2.py). Replies as filed by Hesper (15ec870 Qwen, 789a931 Argon). Argon's reply also contains text in the voice of Opus and Qwen: Argon's own words, not those seats' replies; Opus's real reply is OPUS-R002-reply.md.

## Qwen
- A1 improved window H >= h, condition |w| >= 1/((n+1)H): same as Opus's L2*; algebra is the L2 argument. CHECKED earlier (13,816 random cases, 0 failures).
- B1 V={1,3}, t0=4/9, w=2: H=1/36, window [5/12,17/36], max ||2t|| there = 1/6 < 1/4, so no safe time in the window; t=1/4 is globally safe. CHECKED (claim PROVED stands for this example).
- A3 V={1..n-1}, t1=1/(n+1), integer w: safe iff (n+1) does not divide w. 1,145 cases n=2..11, w in -60..60, 0 mismatches. CHECKED.
- B2 analysis for V={1,3}, w=4: Qwen's safe set "[5/12,7/16] U [9/16,3/4]" is wrong at the top end; true safe points on a 1/960 grid run from 5/12 to 7/16 and 9/16 to 7/12 (e.g. t=0.6 fails). Safe set is non-empty, so Qwen's conclusion (simple formula fails, safe set exists) holds, but the stated interval is wrong.
- Section C claim: for w=(n+1)q, q odd, t1=1/(2(n+1)) works for V={1..n-1}. DISPROVED: 24/24 cases n=2..9, q=1,3,5 fail (||1*t1|| = 1/(2(n+1)) < 1/(n+1)). Qwen had marked it IDEA/UNFINISHED, so no overclaim in labels, but the statement is false.

## Argon
- Counterexample V={1}, t0=1/2, h=1/6, window [1/3,2/3], w=0.4: max ||0.4t|| on window = 4/15 < 1/3, so the local window fails; t=3/2 is globally safe (||1.5||=1/2, ||0.6||=0.4). CHECKED. (Same lesson as Opus's w=4/3 example.)
- Periodic hopping t_k=t0+k/u*: u* distance invariant (checked); the lemma itself (existence of k) is an IDEA, no statement of how large k must be.
- Label problem: Argon writes "[PROVED]" for Opus's verification and "[DISPROVED]" for its own example in the first block; PROVED belongs only after review by the chair/Opus. Argon also calls L2 a substantive strengthening of the Round 001 lemma; Opus audited them as equivalent.

Grades by Puck: CHECKED / DISPROVED as listed; nothing upgraded to PROVED.
