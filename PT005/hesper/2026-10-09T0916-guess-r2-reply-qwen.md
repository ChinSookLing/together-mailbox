BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-09 09:17 +08
RE: 猜公式 Round 2 packet (aaa37b9), BEGIN…END block pasted verbatim
SEAT: qwen
MODEL: Qwen3.7-Plus
CHAT: https://chat.qwen.ai/c/18cf253d-2f8c-48b4-a549-bb7f140a3902

--- reply verbatim ---
Source: https://chat.qwen.ai/c/18cf253d-2f8c-48b4-a549-bb7f140a3902 (Qwen chat, signed in as csllanna@gmail.com via Google). Model shown: Qwen3.7-Plus. Status: complete (Copy button rendered; "Thinking completed" card shown; only one Round 2 reply, no loop or re-send).

The text below is the entire final answer verbatim. Sections 1–3 come from the Reply's Copy button (markdown with inline math using $…$ delimiters). Sections 4–5 are the rendered tail of the same reply as read directly from the page (the copy was truncated by the clipboard display; the on-page text fills the gap). No new message was sent.

== COPIED (Sections 1–3) ==

# Round 2 — Referee and Analysis

## 1. Referee T1

**Lemma A: YES.** 
- LRC(14) is correctly invoked for 13 speeds, giving $x$ with $\|w_i x\| \ge 1/14$. 
- The triangle inequality $\|w_i t/p\| \ge \|w_i x\| - |w_i(x - t/p)| \ge 1/14 - M/(2p)$ is valid. 
- With $p \ge 56M$, this gives $\ge 1/14 - 1/112 = 1/16$. Since "too near" requires strict $< 1/16$, no $w_i$ is too near at cell $t$. 
- $t \not\equiv 0 \pmod{p}$ since $\|w_1 t/p\| \ge 1/16 > 0$, so $t$ is a valid cell.

**Lemma B: YES.**
- Dirichlet for 13 variables with parameter $N$ gives $q \le N^{13} \le p-1$ with $\|qs_i/p\| \le 1/N$, so $qs_i \equiv \pm c_i$ with $c_i \le p/N$.
- Distinctness of $c_i$: if $c_i = c_j$, then $qs_i \equiv \pm qs_j \pmod{p}$, so $s_i \equiv \pm s_j$, contradicting distinctness up to sign. (Note: $s_i \not\equiv -s_j$ is automatic since $s_i + s_j \le 2n = p-1 < p$.)

**Final step: YES.**
- F2 allows scaling by $q$ (a unit since $q \le p-1$). The scaled cover $qS = \{c_1, \dots, c_{13}\}$ up to sign has $c_i \le p/N$.
- Lemma A with $M = p/N$ requires $p \ge 56(p/N)$, i.e., $N \ge 56$, i.e., $p-1 \ge 56^{13}$.

**Weakest step:** The threshold $56^{13}$ is enormous. The proof is logically airtight but practically useless for primes in the hundreds.

---

## 2. Shrinking the Threshold

### What I tried (labeled FACT / PROOF / IDEA)

**PROOF: Any cover contains a speed $< p/16$.** Cell 1 requires some $s$ with $\|s/p\| < 1/16$. Since $s \in \{1,\dots,n\}$ and $n < p/2$, we get $s < p/16$.

**PROOF: After scaling by $s^{-1}$, assume $1 \in S$.** Speed 1 covers cells $\{1, \dots, H\}$. The remaining 12 speeds must cover $\{H+1, \dots, n\}$.

**PROOF: Harmonic alignment.** Cell $H+1 \approx p/16$ requires some $s_2$ with $\|s_2(H+1)/p\| < 1/16$. Writing $H+1 = (p+15-\delta)/16$, we get $s_2(H+1)/p \approx s_2/16$. So $s_2$ must be within $O(1)$ of a multiple of 16. Similarly, cell $kH+1$ forces a speed near $16k/k$. The 13 speeds must be "harmonically aligned" with the cells they cover.

**IDEA: Reduce Dirichlet from 13 to 12 variables.** With $1 \in S$, we need $q \le p/N$ (to keep $c_1 = q$ small) and $\|qs_i/p\| \le 1/N$ for $i=2,\dots,13$. Dirichlet for 12 variables gives $q \le N^{12}$. But we need $N^{12} \le p/N$, i.e., $N^{13} \le p$ — **the same bound**. The constraint $q \le p/N$ exactly cancels the variable reduction.

**IDEA: Better margin via stronger loneliness.** If loneliness were $1/14 + \varepsilon$, the constant 56 would drop to $1/(2(1/112 + \varepsilon))$. But LRC(14) is tight at $1/14$ for worst-case speeds, and no improvement is known for bounded speeds.

**IDEA: Fourier/counting.** A random 13-set leaves $\approx n(7/8)^{13} \approx 0.178n$ cells uncovered. But controlling correlations for the *optimal* cover seems intractable.

**FACT: The threshold $p > 56^{13} \approx 5.3 \times 10^{22}$ stands.** I could not prove any improvement, even a factor of 10. Closing the 20-order-of-magnitude gap to $p \approx 280$ requires a fundamentally different approach — likely one that exploits the harmonic alignment structure directly, rather than via LRC + Dirichlet.

---

## 3. The 14 Question

**$\gamma(p) = 15$ for all sufficiently large $p$.** T2 is correct (same verification as T1, with LRC(15) for 14 speeds and threshold $120^{14}$). So for $p > 120^{14}$, no 14-cover exists, and $\gamma(p) = 15$ (since $\{1,\dots,15\}$ always covers by F3).

**There is no infinite family of 14-covers.** This follows immediately from T2.

**Conjecture for intermediate $p$:** $\gamma(p) = 14$ for some range $280 \lesssim p \lesssim P_1$, then $\gamma(p) = 15$ for $p > P_1$. The transition $P_1$ is likely much smaller than $120^{14}$ — perhaps $P_1 \approx 10^3$ or $10^4$. The data shows $\gamma(p) \ge 14$ for $p \ge 239$, but we don't know if any of these achieve exactly 14.

== RENDERED TAIL (Sections 4–5) ==

## 4. One Sentence for Tuzi

The single most promising lever is the harmonic alignment constraint — any cover must contain a speed < p/16 (to cover cell 1), and after scaling so 1 ∈ S, the remaining speeds are forced to be O(1)-close to multiples of p/t for the cells t they cover, which severely restricts the possible covers and could enable a direct combinatorial obstruction at p ≫ 280 without going through LRC.

## 5. Confidence

| Claim | Confidence |
|---|---|
| T1 is correct (Lemmas A, B, final step) | 98% |
| Threshold cannot be improved via LRC + Dirichlet alone | 90% |
| γ(p) = 15 for all p > 120¹⁴ (no infinite 14-family) | 95% |
| Harmonic alignment is the right structural lever | 70% |
--- end verbatim ---
END LETTER
