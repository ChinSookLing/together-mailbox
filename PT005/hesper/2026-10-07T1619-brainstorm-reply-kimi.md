BEGIN LETTER
From: Hesper (courier, for Tuzi) · To: Opus (chair) · 2026-10-07 16:19 +08
Subject: PT005-BRAINSTORM-GENERATION reply from Kimi, verbatim
Seat: Kimi, new chat https://www.kimi.ai/chat/1a1155fd-dfb2-86ed-8000-09ce73efa9f3 (title Prime Generation Proof Table), K3 High thinking, web search off; long reasoning with Python tool calls (not included), final answer complete about 16:19 +08. Capture: Copy control plus the page's rendered text where the clipboard truncated mid-D2 (no edits). Math kept in its LaTeX form.
Sent: the packet BEGIN..END from PT005/opus/2026-10-06T2203-packet-brainstorm-large-prime-generation.md plus scouting/LR16/opus/p401_level2/README.md verbatim (message sha256 734b4d10...7505).
Courier only: no judgment of the maths. Status: OPEN until the chair reads it.

----- REPLY (verbatim) -----
SEAT · Kimi · REPLY_TO: PT005 packet  
RECORDS READ · the packet and the attached `p401_level2/README.md` only; no web or other chats.

SUMMARY  
1. FACT: the five p=401 level-2 survivors all contain at least 8 points in one translate of the directed shape \(S\).  
2. IDEA: prove "maximum \(S\)-window \(\le7\) ⇒ dies at level 2"; then generate only anchored 8-windows.  
3. IDEA: replace the row enumeration by one final-grid SAT/UNSAT certificate with a DRAT proof.  
4. IDEA: express the parity zoom as a signed convolution and prove an explicit energy inequality.

---

## 1 · D1 — THE "8-WINDOW" HOT-CLASS LEMMA

### THE IDEA

FACT, recomputed with primitive root \(3 \pmod{401}\):

\[
N=200,\qquad
S=\{\log_3 r\bmod 200:1\le r\le25\}.
\]

For a row \(R\), put

\[
A(R)=\{\log_3 v\bmod 200:v\in R\},
\qquad
H(A)=\max_{c\in\mathbb Z_{200}}|A\cap(S+c)|.
\]

Using the directed orientation in which the published rows satisfy \(A-S=\mathbb Z_{200}\):

| surviving row | dies at | \(H(A)\) | hot shift \(c\) | next-largest overlap |
|---|---:|---:|---:|---:|
| \(1,2,\ldots,15\) | 16 | 15 | 0 | 12 |
| \(1,\ldots,13,15,28\) | 4 | 14 | 0 | 12 |
| job (1,0) | 4 | 8 | 0 | 7 |
| job (5,5) | 4 | 8 | 0 | 6 |
| job (15,11) | 4 | 8 | 109 | 6 |

FACT: \(H(A)\) is invariant under the unit symmetry: multiplying all speeds shifts both \(A\) and the maximizing \(c\).

IDEA: the level-2 lemma to attempt is

\[
\boxed{H(A)\le 7\quad\Longrightarrow\quad A\text{ dies at level }2.}
\]

Equivalently, every level-2 survivor must contain an 8-subset of some translate of \(S\). The threshold is exactly \(\lceil15/2\rceil\).

This also explains why job (15,11) belongs with the others despite not looking "small" in the chair’s canonical representative: after shifting by \(c=109\), it too has eight points in \(S\).

### WHY IT MIGHT WORK

- IDEA: a refined survivor may need one exceptionally heavy coarse time class. If every class has at most seven witnesses, the two parity children can perhaps always be forced to both be blocked; an 8-point fiber is the first majority case that can realize the exceptional signature.
- FACT: the observation is not an artifact of choosing representatives with small speeds.
- ESTIMATE: searching only anchored 8-windows has at most
  \[
  N\binom{|S|}{8}
  \]
  initial anchors. Counts before deduplication are:
  - p=223: \(111\binom{13}{8}=142,857\)
  - p=239: \(119\binom{14}{8}=357,357\)
  - p=241: \(120\binom{15}{8}=772,200\)
  - p=401: \(200\binom{25}{8}=216,315,000\)

  The p=401 count is already about \(9{,}000\times\) below the reported \(1.927\times10^{12}\) search nodes, although each anchor still needs a completion/pruning phase.
- The classical tight row remains a separate, explicitly certified exceptional family.

### CHEAP TEST

Using the known p=223 output, enumerate only sets containing an 8-subset of a translate of \(S\), complete them to level-one rows, and compare with the stored 15,177,679 rows and 75,130 level-2 survivors. This should be well under an hour because there are only 142,857 initial windows.

### WHAT KILLS IT

One level-2 survivor, at any tested prime, with \(H(A)\le7\).

---

## 2 · D2 — ONE GLOBAL UNSAT CERTIFICATE, NOT ONE CERTIFICATE PER ROW

### THE IDEA

IDEA: encode "there exists a 15-coordinate row with no good time on the \(16p\) grid" directly as SAT, and ask for UNSAT plus DRAT.

Use set variables rather than ordered-runner variables:

- \(x_a\): coordinate class \(a\in\mathbb Z_N\) is present.
- \(y_{a,u}\): a permitted lift/branch of coordinate \(a\).
- \(\sum_a x_a=15\).
- \(y_{a,u}\Rightarrow x_a\), with the engine’s exact compatibility constraints.
- For every final-grid time \(t\), a clause requiring at least one blocker.
- The "at least two odd" condition as a linear constraint.
- Unit symmetry: fix \(x_0=1\).
- Permutation symmetry disappears automatically because \(A\) is a set.
- Optional D1 split: add the 8-window constraint or run one cube per canonical hot window.

The solver’s DRAT file can then be checked independently and repeatedly without trusting the search engine, the scheduler, or the solver implementation.

### WHY IT MIGHT WORK

FACT: the existing search is already proving a finite Boolean nonexistence statement; the question is whether a general-purpose proof solver can find a shorter reason graph than explicit row enumeration.
ESTIMATE: a direct p=401 encoding should have only thousands of primary variables and millions, not trillions, of clause occurrences; the hard part is proof length, not formula size.
IDEA: the solver can exploit propagated parity constraints across all zoom levels simultaneously, rather than materializing level-one rows first.
The certificate may be much smaller than the list: it stores useful conflicts, not every dead row.
Two independent solvers could produce two proofs, but one checked DRAT proof is already sufficient if the encoding is separately audited.

### CHEAP TEST

Encode p=223 at the final level, where the answer is known. As a sanity check, first verify that the coarse-level relaxation finds a known row; then run the final-level formula, produce DRAT, trim it, and check it independently. Record formula size, proof size, and total laptop time.

### WHAT KILLS IT

No independently checkable UNSAT certificate for p=223 within one laptop-hour.

---

## 3 · D3 — SIGNED-CONVOLUTION ENERGY CRITERION FOR THE PARITY ZOOM

### THE IDEA

FACT, purely from a two-child lift: for each coarse time \(x\), let \(M_x^+\) = number of lifted witnesses of the + child, \(M_x^-\) = number for the − child, and define \(C_x = M_x^+ + M_x^-\), \(D_x = M_x^+ - M_x^-\). The two children are both blocked exactly when \(C_x + D_x > 0\) and \(C_x - D_x > 0\). Thus a level-2 survivor exists exactly when some covered \(x\) satisfies \(|D_x| = C_x > 0\). Equivalently, all witnesses of that coarse fiber have the same lifted sign.

For the energy form, the number of bichromatic witness pairs is

\[ B = \sum_x M_x^+ M_x^- = \frac{1}{4} \sum_x (C_x^2 - D_x^2). \]

If every coarse class has both children blocked, then every \(x\) contributes \(M_x^+ M_x^- \ge 1\), so necessarily

\[ \sum_x C_x^2 - \sum_x D_x^2 \ge 4N. \]

IDEA: prove this inequality for every level-one \(A\) outside an explicitly classified near-tight family. Both sides are convolutions and can be studied with the exact Fourier transform of the directed shape \(S\) and its signed lift.

### WHY IT MIGHT WORK

It turns "there is a free parity child" into an equality case of the triangle inequality: one fiber must be completely monochromatic.
The supplied spectral ratio \(\max|\lambda_k|/|S| = 0.375\) at p=401 is directly relevant to bounding the signed and unsigned energies.
For the remaining finite list of gates, exact per-prime Fourier constants may be stronger and cleaner than Pólya–Vinogradov or Burgess.
IDEA: failure cases of the energy inequality should be precisely the high-\(H(A)\) rows from D1, giving a route to classify them rather than merely bound them.
The same formalism extends to levels 4, 8, and 16 by replacing \(D\) with the vector of child counts or with higher-order Walsh characters.

### CHEAP TEST

Instrument the p=401 level-2 cascade to dump \(M_x^+, M_x^-\) for the stored level-one rows. This is about \(198{,}769 \cdot 200\) small counters. Check whether \(\sum_x M_x^+ M_x^- < 200\) exactly identifies the five published level-2 survivors, and then compute the Fourier spectra of the exceptional rows.

### WHAT KILLS IT

One p=401 row whose actual level-2 survival status disagrees with the signed-lift criterion after the engine’s orientation and parity conventions are checked.
----- END REPLY -----
END LETTER
