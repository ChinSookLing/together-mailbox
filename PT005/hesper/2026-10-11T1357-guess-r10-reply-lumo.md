BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 13:57 +08
RE: 猜公式 Round 10 (packet 0104439), send text r10_send_full.txt or r10_send_short.txt
SEAT: lumo
MODEL: Lumo 2.0 Lite Fast (short version)
CHAT: https://lumo.proton.me/u/11/c/1b04e910-acf8-481d-80b9-8deeab93d8db

--- reply verbatim ---
Lumo Round 10 final reply (PT005 · Big Picture, Opus packet 0104439)
Source: https://lumo.proton.me/u/21/c/1b04e910-acf8-481d-80b9-8deeab93d8db
Mode: Lumo 2.0 Lite, Fast mode (is-active), web search toggle OFF

Verbatim reply from Lumo (as shown in the chat; inline math here is the page's rendered display — the chat shows the same prose plus rendered math):

Proof: Expand B(x) as a Fourier series ∑ b̂(k) e(kx). Substitute into U(S) = ½ ∑_t ∏_v B(vt). The product becomes a sum over vectors k of (∏ b̂(k_v)) e(t ∑ k_v v). Summing over t yields p if ∑ k_v v ≡ 0 (mod p) and 0 otherwise. Thus U(S) = (p/2) ∑_{k ∈ ker} ∏ b̂(k_v).

457 Relations: The dominant terms come from the consecutive block 111..117. Under scaling u=4, these map to 1..13 (odds). Short relations involve small integer combinations of these odds summing to 0 mod p. Specifically, relations like k_1(1) + k_2(3) + … = 0 with coefficients |k| ≤ 4 and ≤ 4 non-zeros (e.g., 1+13=14, 3+11=14) generate large contributions because b̂(k) decays slowly for small k. They likely explain >80% of the −35.39 resonance needed to cancel M(p).

Resonance Budget: A cover requires ∑_{k≠0} ∏ b̂(k_v) ≈ −M(p). Since |b̂(k)| ∼ 1/8, we need roughly 8^14 "weight" from short relations, implying dozens of distinct short linear dependencies among the speeds. As p grows, M(p) increases (capacity gap widens), requiring more or stronger relations. Random sets lack sufficient short relations; 457 survives because its consecutive block creates an abundance of short relations (arithmetic progression structure) that random sets do not possess.

Proving p > P₀: Yes, one can prove no cover exists for p > P₀ if P₀ is where the maximum possible resonance from any set (even structured ones) falls below M(p). Dirichlet scaling ensures any 14 speeds can be scaled to ≲ p^{13/14}, but the number of short relations for such sets is bounded by combinatorial limits (roughly O(p^ε)), whereas M(p) grows linearly with p. Once p exceeds the point where max resonance < M(p), covers vanish. This avoids the 120^14 brute force by bounding the structure of solutions.

For Tuzi: Fourier transforms the problem from "finding a lucky set" to "balancing a resonance equation," revealing that structural arithmetic progressions (like 457's block) are the only way to generate enough short relations to cancel the growing capacity gap M(p).

Least-sure step: Quantifying the exact maximum number of short relations a non-consecutive set can have; assuming the bound is tight enough to force extinction before p ≈ 1000.

---
Notes on labels and word limit:
- Lumo did NOT label any claim with FACT / PROOF / IDEA despite the instruction; the only "Proof:" label is the heading of answer 1.
- The reply is approximately 340 words, slightly over the ≤300-word constraint.
- The page's "Copy" button produced a "Copied to clipboard" toast but the copied content was not accessible to the clipboard-read tool, so this verbatim text was assembled from the page's rendered text (find_text matches 9 and 10) and cross-checked with the full extract; the prose, math, and ending ("… before p ≈ 1000.") all match the visible chat and the reply terminates before "Conversation encrypted".

--- end verbatim ---
END LETTER
