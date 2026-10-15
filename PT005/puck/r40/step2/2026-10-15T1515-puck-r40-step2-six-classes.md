BEGIN LETTER
FROM: Puck
TO: Hesper (cc chair file)
DATE: 2026-10-15 15:15 +0800
RE: PT005 R40 step 2 — why 34 orbits never occur: the mod-16 level-5 shadow rule R16 (640 / 0)

Own script: puck/r40/step2/puck_r40_step2.py (+_out.txt); inputs only the two committed tables.

1) Level-5 domino (hand-derived; 0 mismatches vs raw hit test, 19,264 cases, p=29..47). Cell T=b+ps, with s of parity b+1 mod 32. Hit <=> s=(j-m)v, |d+pj|<2p, j of parity m+b+1, so each speed hits exactly 2 cells. Put x=-mv, h=c/2 mod 16, so x is h or h+16 (the footprint forgets this bit). Case A (h=b mod 2) gives {x-v, x+v}. Case B (h!=b) gives {x, x+2εv} with ε=-sgn d free.
2) R16: project mod 16. Each residue of parity b+1 mod 16 must be covered exactly twice. Since every speed hits exactly 2 cells, this holds for ANY real exact k=5 tiling, at any p and b.
3) Counts on all configs. R16 holds on 640/640 REAL and 0/6,528 NEVER, at both b parities. R16(β=0) = R16(β=1) on all 7,168. The R16 set equals the 640-set, and R16 => mod-32 exact cover on every config.
4) Local form (= R16 on all 7,168): (a) overfill: the fixed cells (A: h±v; B: h) put more than 2 on some residue; (b) dead free end: some B end h±2v misses every residue that is still short.
   - 28 NEVER orbits (5,632 configs) overfill at BOTH parities.
   - 6 orbits (896 configs) overfill at one parity and have a dead end at the other.
   - Example (0,1)²(0,5)²(6,15)²(10,1)²: b odd puts 4 anchors at residue 0; b even puts 4 cells at residue 5.
5) This kills all 34: the 23 orbits of the 6 missing classes and the 11 missing orbits inside the 5 realized classes. Mod-8 projection alone kills only 1,792/6,528; no level-6 input needed.
6) Consequence: NEVER configs are not realized at ANY prime. Derivation + exhaustive check; no stability lemma needed.

Grade: PROVED-candidate (hand derivation + exhaustive check). It becomes PROVED after your independent rerun. Still open: a conceptual reason why β=0 and β=1 always agree, and why R16 always lifts mod 32 (both computed only). Not a breakthrough; no TF.
END LETTER
