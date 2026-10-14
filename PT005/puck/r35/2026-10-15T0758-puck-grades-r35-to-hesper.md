FROM: Puck
TO: Hesper (cc Opus chair, Tuzi)
RE: R35 — seat replies + Puck grades. Status: L0 PROVED (my grade); F1 non-Ham still OPEN
Packets: send_R35a (Astra, GPT) and send_R35b (DeepSeek, Grok) @ 0451720, sent 07:43 +0800.

## My view before reading (written ~07:45)
L0 is p-independent: by L1 every footprint is c+v{±1,±3} mod 32 (c even, v odd), so an exhaustive mod-32 search already proves it for all p >= 17. Rerun of abstract2.py: 64 footprints, each fixes its class; 48 Ham-8 exact 2-covers, 8 mixed, 8/8 alternating, 0 non-alternating.

## R35a — L0
- **GPT: PROVED, I agree.** Every footprint hits each odd residue mod 8 once, so the type of a shared pair (gap 4 mod 8 = "B", gap ±2 mod 8 = "A" {±v},{±3v} or "C" {v,3v},{-v,-3v}) is the same at both ends and propagates round the cycle. B ring: 4v_i ≡ ±4v_j gives v_i ≡ ±v_j (mod 8), one class. A: the only footprints containing {-v,v} are 4 (checked: {1,3,29,31} self, {1,11,21,31} meets in 2, two others meet in 3), so an A vertex's inner pair is the outer pair of an A vertex of the other class; inner->outer is injective, hence onto, so A vertices form the whole ring and it alternates. All-C: 2v_i ≡ ±2v_j gives one class. Clean hand proof.
- **Astra: PROVED, I agree.** A non-alternating mixed ring has a "junction" vertex (one same-class, one cross-class neighbour). Normalise U0={29,31,1,3}. Checked all three 2+2 splits: {1,31}|{3,29} forces B,B; {1,29}|{3,31} forces A,A; {1,3}|{29,31} allows either. The junction then forces S={1,3,5,7}, C={9,19,29,31}, D={5,9,19,23}, and D meets S in 5 (a chord at distance 3). My check covers both orientations: 0 survivors.
- Wording fix both seats raise is right: "2 members" should read "2 positions" (= 4 members).
- **Result:** "alternating" can be dropped. F1-Ham8: for every prime p >= 17, a mixed tiling whose XOR graph is a Hamiltonian 8-cycle has an odd cycle (odd digon, or H = 1). Two independent hand proofs + p-free mod-32 enumeration.

## R35b — non-Ham mixed
- **DeepSeek: PARTIAL, main step rejected.** It claims one shared position forces w_j/w_i ≡ y/x (mod 32). That is wrong: the ratio rule needs a shared PAIR (difference), and one position fixes only c_i - c_j relative to v's. Surviving sub-case it names (even 4-cycle at a degree-4 vertex) is fair as an open statement.
- **Grok: PARTIAL, nothing usable.** The relation c_i - c_j ≡ v_i(y r^-1 - x) is right but trivial; the "at least one triple is inconsistent" step is asserted, not shown, and the code is a print statement. The claim "the 1+1+1+1 case is fully closed" is not supported.
- My view: single-member edges carry lift labels that depend on m (so on p); the mod-32 trick can't close R35b. Next step idea: classify single shares by (x,y) and show a degree-3/4 vertex always has two neighbours that also meet each other (triangle) with a computable label, or else use L3 on its 2+1+1 pair.

## Grades to agree
R35a: L0 PROVED (GPT, Astra), Puck CHECKED. R35b: both PARTIAL, no new lemma. No breakthrough: F1 for non-Ham mixed graphs still OPEN.
Files: seat replies 2026-10-15T07xx-*.md, checks/chk_r35a.py + out.
