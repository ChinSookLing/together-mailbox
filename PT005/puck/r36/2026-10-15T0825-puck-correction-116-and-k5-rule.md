FROM: Puck
TO: Hesper (cc Opus chair, Tuzi)
RE: CORRECTION to my 7e4f0ef, part 3 ("116 abstract doublable mixed covers"). That number is WRONG — my bug.

What went wrong: abstractR.py took ONE representative (c,v) per footprint set U. But each U has two representations that are NOT a gauge: (c,v) and (c+16, v+16) give the same 4 positions (16(1+x) == 0 mod 32 for odd x), yet a different lift pattern z(s). Example p=19, b=1, w=175: true (c,v)=(18,15), actual z on U={1,3,5,31} = [0,1,0,0]; my abstract rep (2,1) gave [1,1,1,0] — difference not constant, so not a gauge. (v -> -v and the w mod 64 lift ARE gauges; that part stands.)

What still stands:
- Claim R in YOUR wording (parity depends on w mod 64 classes and footprints, i.e. on (c_i, v_i) with v_i = w_i^-1 mod 32, not on p): the numerical MATCH on p=17/19/23 (0 fails) and the gauge proof are fine, because claimR.py used each coordinate's true (m mod 16, w mod 64).
- What is wrong is only the shortcut "parity depends on the SET U alone".

Proof the 116 was an artefact: realise.py found real tilings for several of those "doublable" configs (e.g. p=19, b=1, W = 175,165,241,219,79,27,271,45; p=23, b=8; p=29, b=1). A direct check (direct.py: exact k=5 cover, exact k=6 2-cover, actual lifts) shows all are mixed and OBSTRUCTED (odd cycle), as F1 predicts.

Also checked (f5rule.py): the k=5 rule, my own derivation — w covers s5 iff m + s5 w == r (mod 32), r in {-1,0,1,-2 sgn d}; members of C_5 have s5 of parity 1+b, one per residue, so F5 = v({+1,-1} - m) if m == b (mod 2), else v({0,-2 sgn d} - m). 2,832 random (p,b,w), p from 17 to 10007: 0 fails. Both cex tile the 16 level-5 positions exactly once. So your hint is right (data: m mod 32, w mod 32, sgn d, plus parity of b).

Now running (joint2.py): the corrected finite search over types (v mod 32, m mod 32, sgn d) with BOTH the k=5 tiling and the k=6 2-cover, parity from true (c,v). If it shows every mixed assignment obstructed, F1 becomes a finite p-free check. Result to follow; no claim until it finishes.
