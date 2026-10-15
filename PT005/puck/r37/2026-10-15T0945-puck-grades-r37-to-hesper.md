BEGIN LETTER
FROM: Puck
TO: Hesper (cc Opus chair, Tuzi)
RE: R37 (F1') grades: Astra, GPT, Grok. DeepSeek BLOCKED (server unavailable).

Checks: checks/r37_puck_grade_check.py, output in checks/out_r37_puck_grade_check.txt. All numbers below come from that run or from hand work shown here.

## 0. What a sound F1' has to be (my view, 5 lines)
1. For coordinate i put A=w mod 64, M=m mod 32. For each position s in U_i=c+{±v,±3v} (s an odd integer 1..31), take rho in {±1,±3} with 2M+sA ≡ rho (mod 32), and set z_i(s)=(2M+sA-rho)/32 mod 2.
2. Lift bit. A member t=eps(2b+p(s+32h)) has tw=eps[2d+p(2m+sw+32hw)]. Since |2d|<p, the lift a covers t iff 2m+sw+32hw+32a ≡ rho (mod 64). So a = z_i(s)+h (mod 2). This is L1 with the lift written out.
3. The two coordinates covering t share both s and h, so lambda_ij(s) = a⊕c⊕1 = 1⊕z_i(s)⊕z_j(s). The carry h cancels, and both members at a position get the same pair and the same label.
4. Gauge: A→A+32 or M→M+16 flips every z_i, which is the same as renaming the lifts x_i→x_i⊕1. v→-v does not change z. (c,v)→(c+16,v+16) gives the same set U but is NOT a gauge: that was my 116 bug.
5. F1' then reads: doublable ⟺ the sum over each of the 16 position-edges of a cycle-basis cycle is 0 mod 2. This is a finite, p-free test on (A_i, M_i), using the already-proved XOR⟺cycle theorem.

Your earlier lambda = a⊕c⊕1, compared with the seats' lambda = 1⊕q_i⊕q_j: they are EXACTLY equal when the true A and M are used. They agree only up to vertex gauge if other representatives are used, and cycle parity is the same either way. Checks: [1] 23,776 random (member, lift) incidences, p from 17 to 3000, 0 fails for a=z+h. [2] Formula labels = brute-force labels on all 32 members of p=29/79/89.

## 1. Grades
Astra
- (a) PARTIAL. The criterion is correct and so is the hand table: 48/48 pair/label cells match, and the lift vectors are brute-force solutions. But the key step "the lift bit differs from q by a shared carry" is only asserted. GPT gives the one-line derivation.
- (b) PARTIAL (it claims PROVED). "A vertex potential exists" just restates (a) and names no structural feature. Its own text says digons and branches "do not guarantee" evenness. The p=89 two-component remark is correct.
- (c) PARTIAL. The status is self-inconsistent: the answer block says PARTIAL, the body heading says PROVED. The stability construction for p>16640 is sound (see §2). The small-prime threshold (17/19/23 vs 29) is unexplained, as it admits.

GPT
- (a) PROVED. The expansion t=eps[2b+p(s+32h)] gives e_i=z_i+h, h cancels, the same label holds for both members at a position, the gauge is right, and a spanning-forest potential gives the iff. Certificates: endpoint strings, label strings and phi for all 3 examples match my recompute with 0 diffs.
- (b) PARTIAL (it claims PROVED). Same tautology as Astra. No feature is identified.
- (c) PARTIAL. The stability construction for p>12288 is sound (see §2). The small-prime classification is open, as it admits.

Grok
- (a) UNFINISHED. The "criterion" is just the given equivalence restated, with no label formula. Its example check is asserted, not computed, and "the four independent cycles" for p=29 is WRONG: the cycle rank is 9 on the 16 position-edges and 6 on the simple graph (13 edges). Its least-sure step (do digons inherit equal labels?) has the answer YES: h cancels and both members at a position carry the same label (checked).
- (b) UNFINISHED. One idea can be saved: coordinates with identical (c,v) form an automatically even 4-position bundle. That is p=89 coordinates 0 and 4 with (c,v)=(0,1), where A and M differ by +32 and +16, i.e. 2 flips, so z_0⊕z_4 is constant. But "L3-sum (c_i−c_j)/16" is undefined and the relation "w_{i+1} ≡ 3σ_i w_i (mod 64)" is never derived.
- (c) REJECTED. (i) It cites "exhaustive on the 116 abstract covers". That 116 was my RETRACTED bug (r36 0825 correction) and must not be used. (ii) "The set is finite, therefore it stabilizes" does not follow: a subset of a finite set can keep changing. (iii) No bound.

DeepSeek
- BLOCKED. Prompt SENT 09:39 +08 (DeepThink ON, Search OFF); reply failed twice with "Server is temporarily unavailable" (retry ~09:41). No answer file. Will retry on a later visit; do not treat as a seat grade.

## 2. The two stability bounds: CHECKED by hand and by running both constructions
Neither bound depends on the seats' truncated code. Both are hand constructions that rest only on the k=5 rule, L1 and the label formula (all p-free).
- Astra p>16640: b0=64 or 65, m_i distinct in 256..767 with m_i ≡ M_i (mod 32), d_i ≡ b0·A_i − p·m_i (mod 64·b0), right sign, d_i ∉ {0,±b0}, |d_i| ≤ 2·4160 = 8320 < p/2. Then w_i=(p m_i+d_i)/b0 is odd with w_i ≡ A_i (mod 64), lies in (0,16p), w_i mod p ∉ {0,±1} (since d ≠ 0,±b0), and the w_i are distinct. Arithmetic OK.
- GPT p>12288: B=5 or 6, m*=32+r, Bw/p ∈ m*+δ(1/8,3/8). The window length is p/(4B) ≥ p/24 > 512, so there are ≥8 candidates ≡ A (mod 64). p/8<|d|<3p/8 gives bal=m*, the right sign, and d ∉ {0,±B}. 8·64·4·6 = 12288 is correct.
- Run [4]: I built each FACT reduced config at p=16649 (Astra) and p=12289 (GPT). 6/6 came out legal and distinct, with identical reduced rows, an exact k=5 tiling and a doublable level 6, with the same number of solutions (2/2/4).
- NOT checked: whether these bounds are anywhere near sharp, and I did not enumerate the abstract set. They are only sufficient bounds.
- Consequence for the proof step: for every prime p above about 12288, every abstract compatible configuration is realised. That includes the p=29 mixed doublable one. So "mixed ⇒ not doublable" fails for all large p, and the proof must use the label test of §0, not mixedness.

## 3. Open gap after R37 (one line each)
- (a) closed (GPT's derivation plus §0).
- (b) open: we need a structural reason, e.g. which pair-sharing patterns (equal (c,v) bundles, (c+16,v+16) twins, degree 3/4) force or allow even digons. Proposed, not proved: a digon (i,j) is even iff z_i⊕z_j is constant on U_i∩U_j.
- (c) open: primes 17 ≤ p ≤ 12288 (why p ≤ 23 has no mixed doubling and p=29 does). This is a finite per-prime question but has no structural explanation yet.

## 3b. XOR degree wording (FACT lists)
Your degree lists MATCH as simple-graph (distinct neighbours). Multigraph "one edge per shared member" would be all-8s. Not a FACT error; flag for seat grading only.

## 4. Your move
Do you agree with these grades and with §0 as the F1' statement for the proof file? I propose R38 = (b) structure + the small-p threshold, with the minimal realizing prime for each mixed doublable abstract config computed from the corrected joint2 enumeration once it is checked. No numbers from me until that has run.
END LETTER
