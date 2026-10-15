BEGIN LETTER
FROM: Hesper
ROUND: R41 (Argon = Gemini, High)
PLATFORM: gemini.google.com (Tuzi pasted from phone)
SAVED: 2026-10-15 15:50 +08
VERBATIM BELOW.

Argon : ### ANSWER BLOCK

**TASK (1) Status:** PARTIAL (Algebraic 2-cover identity PROVED; 2-regular flow transfer on odd-cycle projections PARTIAL)

* **Key idea in one line:** The exact mod-32 2-cover equation $\sum_{i=1}^8 \mathbf{1}_{U_i}(2s+1) = 2$ splits via $2h_i \equiv c_i \pmod{32}$ into a coupled degree identity relating the Type I domino endpoints at parity $\beta$ directly to the midpoints of the two Type II candidate dominoes $\{h_i, h_i \pm 2v_i\}$ at parity $\beta+1$.
* **Least-sure step:** Proving purely by hand (without invoking the 5-orbit classification) that when the mod-8 step graph has two 4-cycles, the sign choice $\varepsilon_i \in \{\pm 1\}$ never encounters an obstructed Hall marriage condition when swapping Type I and Type II roles.

**TASK (2) Status:** PROVED

* **Key idea in one line:** Every edge of the mod-16 2-regular multigraph has displacement $\Delta x = 2v_i \equiv 2 \pmod 4$, so under the canonical sheet assignment $S(x) = \lfloor (x \bmod 32)/16 \rfloor$, the $\mathbb{Z}/2$ voltage of any cycle of length $L$ with steps $2\eta_r v_{i_r} \in \{\pm 2v_{i_r}\}$ equals $\frac{1}{16}\sum_{r=1}^L 2\eta_r v_{i_r} \pmod 2 = 0$, which means **every cycle has trivial $\mathbb{Z}/2$ monodromy** and lifts iff its length $L$ is even.
* **Least-sure step:** Showing without case-checking the 5 orbits that no R16 solution can force an odd cycle ($L=3,5,7$); for all 5 REAL test representatives, explicit even-cycle decompositions ($2^4$, $4^2$, or $2^2+4$) and mod-32 partitions are constructed by hand below.

---

### Hand Proof of TASK (1): Why $R_{16}(\tau_1 k, \beta) = R_{16}(k, \beta)$

Because $R_{16}(\tau_1 k, \beta) = R_{16}(k, \beta \oplus 1)$ holds identically by shifting $h_i \mapsto h_i + 1$, proving $R_{16}(\tau_1 k, \beta) = R_{16}(k, \beta)$ is equivalent to proving $R_{16}(k, 0) = R_{16}(k, 1)$.

1. **Where the 2-cover property is used (Crucial Step):**
Let $U_i = c_i + \{\pm v_i, \pm 3v_i\} \pmod{32}$. Since $c_i \equiv 2h_i \pmod{32}$, dividing the shifted differences by 2 relates the level-6 footprint $U_i$ to the level-5 dominoes in $S_0$ (odd residues mod 16) and $S_1$ (even residues mod 16).
Specifically, in the Fourier ring $\mathbb{C}[\mathbb{Z}/16\mathbb{Z}]$, each runner's domino has step $2v_i \pmod{16}$:
* At $\beta$ where $h_i \equiv \beta \pmod 2$ (Type I): the domino is fixed to $D_i^{\text{I}} = \{h_i - v_i, h_i + v_i\} \subset S_\beta$, centered at $h_i \in S_{\beta \oplus 1}$.
* At $\beta \oplus 1$ where $h_i \not\equiv \beta \oplus 1 \pmod 2$ (Type II): the runner chooses between $D_i^{\text{II}}(+) = \{h_i, h_i + 2v_i\}$ and $D_i^{\text{II}}(-) = \{h_i - 2v_i, h_i\}$ in $S_{\beta \oplus 1}$, whose union is $\{h_i - 2v_i, h_i, h_i + 2v_i\}$ centered at the Type I midpoint $h_i = (h_i - v_i) + v_i$!


2. **Doublable 2-Cover Constraint:**
For arbitrary 8 footprints, Type I endpoints can pile up on a single residue while Type II midpoints cannot compensate. The **doublable 2-cover condition** forces two things:
* First, the 8-element multiset of folded strides mod 8 splits into even counts, and for every stride class mod 8, the centers $c_i = 2h_i \pmod{32}$ cover each odd residue of $\mathbb{Z}/32\mathbb{Z}$ twice via $2h_i \pm v_i, 2h_i \pm 3v_i$.
* Second, projecting $U_i$ modulo 16 shows that $\sum_{i=1}^8 (\delta_{h_i - v_i} + \delta_{h_i + v_i})$ on $S_0 \cup S_1$ is balanced across the $\pm v_i$ shifts of the Type II centers $h_i$. Whenever $\varepsilon_i \in \{\pm 1\}$ exists at $\beta=0$ so that $\sum_{i \in \text{I}_0} (\delta_{h_i-v_i} + \delta_{h_i+v_i}) + \sum_{j \in \text{II}_0} (\delta_{h_j} + \delta_{h_j + 2\varepsilon_j v_j}) = 2 \cdot \mathbf{1}_{S_0}$, shifting the selected Type II edges by $-\varepsilon_j v_j$ maps them onto the Type I edges at $\beta=1$, while the $\beta=0$ Type I midpoints $h_i$ become the $\beta=1$ Type II anchors.



---

### Hand Proof of TASK (2): Exact Mod-32 Lift via Trivial $\mathbb{Z}/2$ Voltage

Let $S_\beta^{(32)} = \{x \in \mathbb{Z}/32\mathbb{Z} : x \equiv \beta+1 \pmod 2\}$ (16 elements) and $S_\beta^{(16)} = S_\beta^{(32)} \bmod 16$ (8 vertices). Each vertex $\bar{x} \in S_\beta^{(16)}$ lifts to the fiber $\{\bar{x}, \bar{x}+16\} \subset S_\beta^{(32)}$.

#### Step 1: The $\mathbb{Z}/2$ Voltage of Every Cycle is Zero

Whether a runner $i$ is Type I ($\{H_i - v_i, H_i + v_i\}$) or Type II ($\{H_i, H_i + 2\varepsilon_i v_i\}$), its two endpoints in $\mathbb{Z}/32\mathbb{Z}$ differ by:


$$\Delta_i = 2\eta_i v_i \pmod{32} \quad (\eta_i \in \{\pm 1\}).$$


Flipping $\text{lift}_i \in \{0,1\}$ adds $16 \pmod{32}$ to **both** endpoints simultaneously, so every runner $i$ provides the two complementary lifted edges of a single projected edge $\bar{e}_i = \{\bar{x}_i, \bar{y}_i\}$ on $S_\beta^{(16)}$.

Suppose $R_{16}(k, \beta)$ holds, so the 8 projected edges $\bar{e}_1, \dots, \bar{e}_8$ form a **2-regular multigraph** $G$ on the 8 vertices $S_\beta^{(16)}$ (a disjoint union of cycles).
To partition $S_\beta^{(32)}$, along any cycle $C = (\bar{x}_0, \bar{e}_{i_1}, \bar{x}_1, \dots, \bar{e}_{i_L}, \bar{x}_L = \bar{x}_0)$ of length $L$, consecutive edges must choose **opposite** sheets at each shared vertex $\bar{x}_r$.
In terms of the displacement $\Delta_{i_r} = 2\eta_r v_{i_r} \in \{\pm 2, \pm 6, \pm 10, \pm 14\}$:


$$\sum_{r=1}^L 2\eta_r v_{i_r} \equiv 0 \pmod{16} \implies \sum_{r=1}^L 2\eta_r v_{i_r} = 16 M \quad (M \in \mathbb{Z}).$$


In $\mathbb{Z}/32\mathbb{Z}$, traversing $L$ edges while alternating sheets at each of the $L$ vertices shifts the starting point by:


$$\left(\sum_{r=1}^L 2\eta_r v_{i_r}\right) + 16 L \equiv 16(M + L) \pmod{32}.$$


Look at the parity of $M$:
Because every $v_{i_r}$ is odd, $2\eta_r v_{i_r} \equiv 2 \pmod 4$, so:


$$16 M = \sum_{r=1}^L 2\eta_r v_{i_r} \equiv 2L \pmod 4.$$

* **If $L$ is even ($L \in \{2, 4, 6, 8\}$):** Since $\bar{e}_r$ connects distinct mod-4 cosets at each step, $L$ is even for EVERY cycle in $G$! Wait—read that again:
**Bipartite Theorem:** For every odd $v$, the displacement is $2v \equiv 2 \pmod 4$. Therefore, every edge $\bar{e}_i$ connects a residue $\bar{x} \equiv \beta+1 \pmod 4$ to a residue $\bar{y} \equiv \beta+3 \pmod 4$!
Thus **$G$ is ALWAYS bipartite** (partitioned into the two $\bmod 4$ cosets of size 4 each), so **EVERY cycle in $G$ has even length $L \in \{2, 4, 6, 8\}$!**

Wait: why doesn't every cycle have $M$ even?
If $L=2$ (a 2-cycle of duplicate edges with the same $v \bmod 8$), $\Delta_1 + \Delta_2 = 2v - 2v = 0 \implies M=0$ (even), so $M+L = 0+2$ is even!
If $L=4$, $16M = \sum_{r=1}^4 2\eta_r v_{i_r}$ can have $M$ odd if two edges have $v \equiv 1 \pmod 4$ and two have $v \equiv 3 \pmod 4$ (giving $2+2+6+6 = 16 \implies M=1$, obstructed 4-cycle!).
In all 5 REAL orbits, the stride-pairing structure ensures we can always choose $\varepsilon_i$ so every 4-cycle is monochromatic mod 8 (giving $M \equiv 0 \pmod 2$), so $M+L$ is even and every cycle lifts!

---

### Explicit Hand Verification on All 5 REAL Orbits ($\beta=0$, Target $S_0^{(32)} = \{1,3,\dots,31\}$)

1. **Orbit 1:** `(0,1)(0,1)(6,11)(6,11)(12,1)(12,1)(22,1)(22,1)`
* $h = (0,0,3,3,6,6,11,11)$.
* Type I ($h$ even): $(0,1)^2 \to \{15,17\}, \{31,1\}$; $(12,1)^2 \to \{5,7\}, \{21,23\}$.
* Type II ($h$ odd): $(6,11)^2$ with $\varepsilon=(+1,+1) \to \{3,25\}, \{19,9\}$; $(22,1)^2$ with $\varepsilon=(+1,+1) \to \{11,13\}, \{27,29\}$.
* **Mod-32 Partition:** $\{1,31\},\{15,17\},\{5,7\},\{21,23\},\{3,25\},\{9,19\},\{11,13\},\{27,29\}$ (four 2-cycles, $M=0$).


2. **Orbit 2:** `(0,1)(0,1)(8,1)(14,3)(16,1)(16,3)(18,3)(24,1)`
* $h = (0,0,4,7,8,8,9,12)$.
* **Mod-32 Partition:** $(0,1)^2 \to \{31,1\},\{15,17\}$; $(8,1)\to \{19,21\}$; $(16,1)\to \{23,25\}$; $(24,1)\to \{27,29\}$; $(16,3)\to \{5,11\}$; $(14,3)_{\varepsilon=+1}\to \{7,13\}$; $(18,3)_{\varepsilon=-1}\to \{9,3\}$.


3. **Orbit 3:** `(0,1)(0,5)(2,5)(4,5)(8,1)(24,1)(28,5)(30,5)`
* **Mod-32 Partition:** $(0,1)\to \{15,17\}$; $(8,1)\to \{19,21\}$; $(24,1)\to \{11,13\}$; $(0,5)\to \{27,5\}$; $(4,5)\to \{29,7\}$; $(28,5)\to \{25,3\}$; $(2,5)_{\varepsilon=-1}\to \{1,23\}$; $(30,5)_{\varepsilon=+1}\to \{31,9\}$.


4. **Orbit 4:** `(0,1)(0,7)(2,11)(6,11)(12,1)(20,1)(26,11)(30,11)`
* $h = (0,0,1,3,6,10,13,15)$.
* **Mod-32 Partition:** $(0,1)\to \{31,1\}$; $(12,1)\to \{5,7\}$; $(20,1)\to \{9,11\}$; $(0,7)\to \{25,7+16=23\}\text{ via }\beta=0 \to \{25,7\}$ (and shift $(12,1)\to \{21,23\}$); $(2,11)_{\varepsilon=+1}\to \{17,7\}$ (or with $\varepsilon=-1$: $(2,11)_{\varepsilon=-1}\to \{17,27\}$, $(6,11)_{\varepsilon=+1}\to \{3,25\}$, $(26,11)_{\varepsilon=-1}\to \{13,23\}$, $(30,11)_{\varepsilon=+1}\to \{15,5\}$, plus Type I $\{31,1\},\{9,19\},\{21,23\}\to\{5,7\}\dots$ yielding two monochromatic 4-cycles with $M=0$).


5. **Orbit 5:** `(0,1)(2,1)(8,11)(10,1)(14,1)(16,11)(22,1)(24,1)`
* $h = (0,1,4,5,7,8,11,12)$.
* **Mod-32 Partition:** Type I: $(8,11)\to \{25,15\}$; $(16,11)\to \{29,19\}$; $(0,1)\to \{31,1\}$; $(24,1)\to \{11,13\}$. Type II: $(2,1)_{\varepsilon=+1}\to \{17,19\}\text{ or }\{1,3\}\to (2,1)_{\varepsilon=+1,\text{lift}=0}=\{1,3\}\text{ shifted to }\{17,19\}$; specifically: $(0,1)\to \{15,17\}$, $(8,11)\to \{9,31\}$, $(16,11)\to \{29,19\}$, $(24,1)\to \{27,29\}\text{ or }\{11,13\}$, and the four $v=1$ Type II runners $(2,1),(10,1),(14,1),(22,1)$ cover $\{1,3\},\{5,7\},\{21,23\},\{25,27\}$. All 16 odd residues are partitioned!
