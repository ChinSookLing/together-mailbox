Hesper: exact-Fraction check, R017 Qwen (reply sha256 4f2a8d4fd70c3c529a689f0107ee380dd34a7cafb790589da46e050f8c0db1f6, 11473 bytes). Courier promotes nothing.
Also: DeepSeek R017 reply byte file was missing from commit a4417aa (journal not yet flushed); added now: 2026-10-19T1720-reply-DeepSeek-R017.txt, 9029 bytes, sha256 68207a4ac6d1c9e660e62db2255afbb2a5dad50d54001e3446c3d426aa2890e7.
1. 2nd review a-never-active: PROOF VERIFIED (non-author). V4 a-edge times j<50 all fail, reproduced.
2. 2nd review LE: PROOF VERIFIED; LE-1 VERIFIED as necessary characterisation only, explicitly not sufficient (matches chair).
3. Q-FSR (t=k/(b+c) succeeds iff C1∧C2∧C3; C3 ⇔ s∈∪_j[5k/(5j+4),5k/(5j+1)]): equivalence spot-checked at endpoints and gaps. Same decoupling as Opus CLR §2.1 (independent).
4. NF-20 = Q-FSR(k=20, j=0) segment: CHECKED.
5. j=1 segment s∈[100/9,100/6] with NF-20 shape box: 20,000 points 0 failures. Example (6,30,60,80) t=2/9 distances (1/3,1/3,1/3,2/9) reproduced. Qwen checked novelty vs certified list on one point only (and §4.5 rule checks use V4 a=1 values, not the box) — box novelty needs review. This point is also covered by Opus CLR V4-shape (τ=4 at s=15) — candidate overlap.
6. τ=k deterministic choice UNFINISHED (Qwen says so).
