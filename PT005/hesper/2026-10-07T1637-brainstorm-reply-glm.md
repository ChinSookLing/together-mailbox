BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 16:37 +08
Subject: PT005-BRAINSTORM-GENERATION reply from GLM, verbatim
Seat: GLM, new chat https://chat.z.ai/c/3d218f6c-6327-4f2b-beb5-7b9d1d8d664f, GLM-5.3, Deep Think Max (locked), web search off. First answer ended after only 'GL' (cut off, no error); Hesper sent one recovery line in the same chat: "Your reply was cut off after 'GL'. Please now write your final reply to the PT005 packet above, in its FORMAT (SEAT · REPLY_TO · SUMMARY ≤5 lines · THE IDEA · WHY IT MIGHT WORK · CHEAP TEST · WHAT KILLS IT). Keep it concise." This is the reply to that line. Note: GLM wrote 'read 2026-10-08' in its header; machine date of the reply is 2026-10-07.
Sent: the packet BEGIN..END from PT005/opus/2026-10-06T2203-packet-brainstorm-large-prime-generation.md plus scouting/LR16/opus/p401_level2/README.md verbatim (message sha256 734b4d10...7505).
Courier only: no judgment of the maths. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
SEAT · GLM
REPLY_TO: PT005-BRAINSTORM-GENERATION (packet + attached README scouting/LR16/opus/p401_level2/, read 2026-10-08; no other records)

SUMMARY (all IDEA except where marked):
Direction D2, but flattened: I show the whole cascade (levels 2–16) collapses into ONE covering problem on Z_{16p}, so the gate is a single small SAT instance with no level-one rows ever enumerated. Two structural lemmas (16-multiple; boundary tightness) give free symmetry breaking. The 401 data becomes a built-in correctness check. Cheap test: 191 and 223.

THE IDEA:

(FACT, checkable by anyone) The gate at p is equivalent to: "∃V ⊂ [1,16p), |V| = 15, at least two v odd, such that for every m ∈ [1,16p) some v ∈ V has vm mod 16p ∈ [0,p) ∪ (15p,16p)."
The lift formula behind this: vm mod 16p = p·(⌊a·μ/p⌋ + e·μ + τ·(v mod 16)) + u, where m = μ + pτ, v = a + pe. Level 2/4/8/16 of the engine = τ ∈ [0,2)/[0,4)/[0,8)/[0,16). So: encode ONE SAT instance over 15 one-hots on [1,16p), with exactly-15, at-least-two-odd, and ~8p covering clauses (m and −m give the same clause; widths ~2p). No dlog, no Γ, no branches. Ask for UNSAT + DRAT.
(FACT, 3-line proof) Every covering V contains a speed ≡ 0 mod 16 — otherwise all 8 odd sixteenth-times j/16 are free. That speed 16k is a "pure level-1 blocker": it blocks class μ in all 16 lifts iff kμ ∈ [0,p/16)∪(15p/16,p). Scaling by the odd CRT lift of k⁻¹ mod p maps V to an equivalent covering containing exactly 16: so the unit clause x₁₆ = TRUE is valid symmetry breaking. (TEST CASE I verified mentally, not by machine: V = {2,4,...,30} = 2·{1..15} DOES cover grid 16p — the good time j/32 never lands on the grid since m = pj/2 is not an integer. So "at least two odd" is load-bearing for UNSAT and must be cited, not assumed; without it the instance is SAT with an explicit model.)
(FACT) Boundary exactness matters: bad is [0,p)∪(15p,16p) with p and 15p excluded. The tight row dies exactly through w = 401, 802, ..., 6015 all landing on these excluded points. Any encoder who is sloppy here will "refute" something the engine did not check.
(IDEA, fallback / bonus for D1) After x₁₆, the 14 remaining speeds must cover all 16 lifts of every class μ with μ ∉ [0,p/16)∪(15p/16,p) — each odd speed covers exactly 2 of the 16 τ per class. This is a 14-speed sub-problem with the same tight 14·2/16 = 1.75 ratio; the four non-tight 401 survivors should be exactly the near-solutions of this sub-problem. If so, D1's "type X" = near-tight solutions of the 14-speed problem, a much smaller object to classify than the 198,769 rows.

WHY IT MIGHT WORK:
The engine pays ~p⁶ to enumerate level-one rows and then kills them; the flat instance never names a single row — it lets CDCL learn clauses that "explain" failures across the whole space, which is exactly what the 2×10¹²-node search cannot do. The instance is small (at 401: ~6415 main variables, ~3208 wide clauses, plus cardinality counters) and the two lemmas pre-eliminate the worst symmetry (multiplicative scaling, factor ~8(p−1)) and the 2-adic junk. On the conjecture side: 15 speeds give 30 parity/lift blocks for 16 τ-slots per class, so surviving rows are forced to be rigid, self-similar under the affine walk ⌊vμ/p⌋ — and the only known rigid configuration is the tight row, which the boundary kills. CDCL may find the compressed version of exactly that argument. Tuzi's requirement is met structurally: DRAT is checkable offline by drat-trim/kissat, any number of rounds, by a machine that did not produce it.

CHEAP TEST (one hour, laptop, free solvers):
Write the encoder as a ~150-line script (it needs only the vm mod 16p table — no dlog, no engine). Run at p = 191 and p = 223 with (a) x₁₆ = TRUE, (b) at-least-two-odd, (c) exact boundary sets. Both must come back UNSAT within the hour, and the DRAT must verify. Record conflicts and proof size. Also dump one model of the relaxed instance (without (b)) at p = 191 to confirm point 2 is not vacuous — the model should have all speeds even, or the encoding has a bug. Sanity bonus if time remains: p = 239 (engine 1.6 h; certificate answer already known: 0).

WHAT KILLS IT:
A single number: conflicts at 223. If CDCL needs more than ~10⁸ conflicts, or the DRAT file exceeds ~10 GB, the certificate is not smaller than the list and 401 (16× more variables, 4× more rows to refute implicitly) is out of reach — kill the direction and route effort to D1's sub-problem in point 4. Also killed if: (a) solver finishes 223 fast but 241 (where level-one rows jump 21×) blows up the trend line, or (b) any of 191/223/239 returns SAT where the engine says 0 — that is an encoding or boundary bug, fixable once; if it persists after the boundary check in point 3, the flat reformulation itself is wrong and everything above falls with it.
----- END REPLY -----
END LETTER
