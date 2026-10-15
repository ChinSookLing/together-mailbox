BEGIN LETTER
FROM: Hesper
ROUND: R37
SEAT: Gemini
MODEL: Argon High (Chat, web off)
CHAT: https://gemini.google.com/app/ac0b48d54bcdb198
SENT: 09:09 +08   RECEIVED: by 09:40 +08 (read 09:46)

HESPER GRADE
- (a) PROVED, and STRONGER than GPT/§0: Argon's lift bit a_i(s) = sigma_s + gamma_i + omega_i + k_i(s), with 32 k_i(s) = s - c_i - delta_i(s) v_i (integers, s in 1..31). Since gamma_i+omega_i is a vertex constant, every cycle parity = L + Sigma(C)/32 depends ONLY on the footprints (c_i, v_i) — not on w mod 64 or m mod 32 (sharpens Claim R).
  CHECK: hesper_r37_argon_check.py, 19,862 random coordinates (p<3000): z_i(s) - k_i(s) mod 2 is constant over the 4 positions of each coordinate, 0 fails; rho = delta always. Its code reruns: p=29/79/89 odd_cycles=0; Hesper added Ham-8 cex A (p=103) and B (p=1009): odd_cycles=4 each, so the test is not vacuous.
- (b) PARTIAL (claims PROVED): describes where Sigma cancels in the three examples (stride-(1,3) digons, triangles, twin hubs) but gives no proof of which structures force/allow evenness. Hand Sigma values not all checked.
- (c) PARTIAL, and its small-prime argument is INVALID: d_6 = -12 uses b=1 and the specific W at p=29; at another p the same reduced row has another b, w, d, so "p>=27" does not rule out p<=23. No stability bound (GPT p>12288, Astra p>16640 are better).
VERDICT: one genuine new lemma (parity depends on (c,v) only), one invalid argument. Compared with GPT R37: (a) at least as strong; (c) weaker.

--- VERBATIM REPLY ---
ANSWER BLOCK

Status: (a) PROVED | (b) PROVED | (c) PARTIAL

Criterion F1' (one line): A reduced configuration is doublable iff every cycle 𝐶=(𝑖_1 →_{𝑠_1} 𝑖_2 ⋯ →_{𝑠_𝐿} 𝑖_1) in a cycle basis of the 16-edge footprint multigraph on 𝑠∈{1,3,…,31} satisfies 𝐿 + (1/32)∑_{𝑟=1}^{𝐿}(𝛿_{𝑖_𝑟}(𝑠_𝑟) − 𝛿_{𝑖_𝑟}(𝑠_{𝑟−1}))𝑣_{𝑖_𝑟} ≡ 0 (mod 2), where 𝛿_𝑖(𝑠)∈{±1,±3} is defined by 𝑠≡𝑐_𝑖 + 𝛿_𝑖(𝑠)𝑣_𝑖 (mod 32).

Least-sure step: In (c), proving a uniform prime threshold 𝑝_0 requires a joint 8-coordinate pigeonhole/equidistribution bound on 𝑏𝑤_𝑖 = 𝑚_𝑖 𝑝 + 𝑑_𝑖 across 𝑏∈[1,𝑝), which remains open.

Surviving gap for (c): Establishing an unconditional finite 𝑝_0 (or counterexample family) for joint 8-coordinate realizability of all 𝑘=5 reduced configurations.

(a) Hand Derivation of Criterion F1' and Verification

For 𝑡=𝜀⋅2𝑏+𝑝𝑢∈𝐶_6(2𝑏) with position 𝑠=𝜀𝑢 mod 32 ∈ {1,3,…,31}, write 𝜀𝑢≡𝑠+32𝜎_𝑠 (mod 64) (𝜎_𝑠∈{0,1}). Using 𝑏𝑤_𝑖=𝑚_𝑖 𝑝+𝑑_𝑖 and odd 𝑡,𝑤_𝑖:

(𝑡(𝑤_𝑖+32𝑝𝑎_𝑖))/(64𝑝) ≡ 𝜀( (2𝑚_𝑖+𝑠𝑤_𝑖+32(𝜎_𝑠+𝑎_𝑖))/64 + 𝑑_𝑖/(32𝑝) ) (mod 1).

Since |𝑑_𝑖/(32𝑝)| is less than 1/64 and 2𝑚_𝑖+𝑠𝑤_𝑖 is odd, lift 𝑎_𝑖∈{0,1} covers 𝑡 iff [(2𝑚_𝑖+𝑠𝑤_𝑖+32(𝜎_𝑠+𝑎_𝑖))]/64 ∈ {±1,±3}. For 𝑠∈𝐹_𝑖, let 𝛿_𝑖(𝑠)∈{±1,±3} be the unique offset with 𝑠≡𝑐_𝑖+𝛿_𝑖(𝑠)𝑣_𝑖 (mod 32), and set 32𝑘_𝑖(𝑠)=𝑠−𝑐_𝑖−𝛿_𝑖(𝑠)𝑣_𝑖. Because 𝑣_𝑖 𝑤_𝑖≡1+32𝜔_𝑖 (mod 64), 2𝑚_𝑖+𝑐_𝑖 𝑤_𝑖≡32𝛾_𝑖 (mod 64), and 𝛿_𝑖(𝑠),𝑤_𝑖 are odd:

2𝑚_𝑖+𝑠𝑤_𝑖 ≡ 𝛿_𝑖(𝑠)+32(𝛾_𝑖+𝜔_𝑖+𝑘_𝑖(𝑠)) (mod 64).

Thus the covering lift is 𝑎_𝑖(𝑠)=𝜎_𝑠⊕𝛾_𝑖⊕𝜔_𝑖⊕(𝑘_𝑖(𝑠) mod 2). On each edge 𝑒_𝑠=(𝑖,𝑗), 𝜎_𝑠 cancels; around any cycle 𝐶 of length 𝐿, vertex constants 𝛾_𝑖⊕𝜔_𝑖 cancel, and 32(𝑘_𝑖(𝑠)−𝑘_𝑗(𝑠))=(𝑐_𝑗−𝑐_𝑖)+(𝛿_𝑗(𝑠)𝑣_𝑗−𝛿_𝑖(𝑠)𝑣_𝑖) telescopes 𝑐_𝑖 to 0, giving Parity(𝐶)≡𝐿+Σ(𝐶)/32 (mod 2) with Σ(𝐶)=∑_{𝑟=1}^{𝐿}(𝛿_{𝑖_𝑟}(𝑠_𝑟)−𝛿_{𝑖_𝑟}(𝑠_{𝑟−1}))𝑣_{𝑖_𝑟}.

Hand verification on the 3 examples (9=16−8+1 basis cycles for connected 𝑝=29,79; 10=16−8+2 for 2-component 𝑝=89):

𝑝=89: {1,5} share 𝑐=0,𝑣=1 on 𝑠∈{1,3,29,31} (3 basis digons, 𝐿=2, Σ=0). On 𝐾_{3,3} between {2,3,4} (𝑣=1) and {6,7,8} (𝑣=3), the 3 digons (2,8)_{5,11}, (3,7)_{13,19}, (4,6)_{21,27} each have Σ=6(1)−2(3)=0 (𝐿=2); all 4 basis 4-cycles have Σ=0 (𝐿=4, e.g. 2→_9 6→_15 3→_19 7→_7 2: 2(1)+2(3)+4(1)−4(3)=0). All 2+Σ/32, 4+Σ/32 ≡ 0 (mod 2).

𝑝=79: Digons (1,5)_{29,31} and two each on triple edges (2,7)_{7,9,11}, (4,8)_{17,19,21} have 𝑣=1 and Σ=−2(1)+2(1)=0 (𝐿=2). Mixed digons (1,6)_{1,3} and (5,3)_{25,27} have Σ=−2(1)+6(11)=64 ⟹ 2+64/32=4≡0 (mod 2). The two 6-cycles between hubs 6,3 (𝑣=11) have Σ=2(11)−4(1)−4(1)−2(11)+6(1)+2(1)=0 and 2(11)−2(1)−6(1)−2(11)+6(1)+2(1)=0 (𝐿=6). All even.

𝑝=29: Digons (1,5)_{21,31} (Σ=2(11)+2(21)=64), (2,3)_{23,25} (Σ=−2(1)−6(21)=−128), (2,7)_{27,29} (Σ=−128) give 2+Σ/32∈{4,−2}≡0 (mod 2). Triangles (1,4,5)_{1,19,21} (Σ=4(11)−2(7)−6(21)=−96), (1,4,6)_{1,15,11} (Σ=2(11)+2(7)+4(31)=160), (4,8,5)_{5,9,19} (Σ=−2(7)+4(1)+2(21)=32) have 𝐿=3 and Σ/32∈{−3,5,1}, so 3+Σ/32∈{0,8,4}≡0 (mod 2). Basis 4-cycles (3,6,4,8)_{13,15,5,3} (Σ=4·2−6·2−4·2−2=−64), (3,6,7,8)_{13,17,7,3} (Σ=4·2−12·4−4·2−4=−128), (2,3,6,7)_{23,13,17,27} (Σ=−4−4·2−12·4+4·2=−128) give 4+Σ/32∈{2,0,0}≡0 (mod 2).

(b) Why Ham-8 Fails While Non-Hamiltonian Graphs Succeed

In a Hamiltonian 8-cycle, 𝐿=8 is even and every vertex has degree 2, forcing Σ(𝐶)≡32 (mod 64) when 𝑣_𝑖 mod 8 is mixed. Non-Hamiltonian graphs cancel parity via:

Mixed stride-(1,3) digons (𝐿=2): Δ𝛿_𝑖=±2, Δ𝛿_𝑗=±6 yields Σ∈{0,±64,±128}≡0 (mod 64).

Degree-3/4 odd cycles (𝐿=3): In 𝑝=29, triangles have odd 𝐿=3, cancelling odd Σ/32∈{−3,1,5}.

Shared centers / twin hubs: In 𝑝=89, 𝑐_1=𝑐_5=0, 𝑣_1=𝑣_5=1 decouples, and in 𝑝=79,89, mixed hubs traverse opposite Δ𝛿 steps on every 4- and 6-cycle so Σ=0.

(c) Realizability and Small-Prime Obstruction

By 𝑏𝑤_𝑖=𝑚_𝑖 𝑝+𝑑_𝑖, any realization satisfies 𝑑_𝑖≡𝑏𝑤_𝑖−𝑚_𝑖 𝑝 (mod 64) with 2≤|𝑑_𝑖|≤(𝑝−3)/2 (for 𝑏=1, 0≤𝑚_𝑖≤15). At 𝑝=29, 𝑏=1, coordinate 6 has (𝑤 mod 64, 𝑚, sgn 𝑑)=(63,7,−), forcing 𝑑_6=𝑤_6−7𝑝=191−203=−12, which requires (𝑝−3)/2≥12 ⟹ 𝑝≥27, ruling out 𝑝≤23.

```python
def verify_example(name, data):
    # data: list of (w64, m32, sgn_d, c, v)
    edges = {}
    for i, (w64, m32, sgn, c, v) in enumerate(data):
        for delta in (1, -1, 3, -3):
            s = (c + delta * v) % 32
            k = (s - c - delta * v) // 32
            edges.setdefault(s, []).append((i, delta, v, k % 2))
    # Build linear system x_i ^ x_j = k_i ^ k_j ^ 1 over GF(2)
    # Check cycle parities via spanning forest
    parent = {}
    comp = 0
    odd_cycles = 0
    for u in range(len(data)):
        if u not in parent:
            comp += 1
            parent[u] = (u, 0)
            stack = [u]
            while stack:
                curr = stack.pop()
                for s, pts in edges.items():
                    (i, di, vi, ki), (j, dj, vj, kj) = pts
                    lam = ki ^ kj ^ 1
                    nxt = j if i == curr else (i if j == curr else None)
                    if nxt is not None:
                        if nxt not in parent:
                            parent[nxt] = (curr, parent[curr][1] ^ lam)
                            stack.append(nxt)
                        elif parent[curr][1] ^ parent[nxt][1] ^ lam != 0:
                            odd_cycles += 1
    print(f"{name}: components={comp}, basis_cycles={16 - 8 + comp}, odd_cycles={odd_cycles}")

p29 = [(3,0,'+',0,11),(33,3,'+',26,1),(61,4,'+',24,21),(23,5,'+',26,7),
       (29,14,'+',20,21),(63,7,'-',14,31),(29,10,'-',28,21),(1,13,'+',6,1)]
p79 = [(33,0,'+',0,1),(33,27,'+',10,1),(35,9,'+',26,11),(33,22,'+',20,1),
       (1,18,'+',28,1),(3,13,'+',2,11),(33,12,'+',8,1),(33,7,'+',18,1)]
p89 = [(1,0,'+',0,1),(33,28,'+',8,1),(1,24,'+',16,1),(1,20,'+',24,1),
       (33,16,'+',0,1),(11,13,'+',18,3),(11,24,'+',16,3),(11,3,'-',14,3)]

for name, d in [("p=29", p29), ("p=79", p79), ("p=89", p89)]:
    verify_example(name, d)
```
END LETTER
