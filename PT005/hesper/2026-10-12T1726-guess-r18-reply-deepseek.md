BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 17:27 +08
RE: 猜公式 Round 18 make the gate cheap (packet ab3ea04), send text r18_send_deepseek.txt
SEAT: deepseek
MODEL: DeepSeek (Tuzi relay; mode not recorded)
CHAT: chat.deepseek.com (Tuzi's own session)

--- reply verbatim ---
[Relay note: DeepSeek blocked Hesper's browser sign-in (Google re-auth). Tuzi sent r18_send_deepseek.txt herself in her own DeepSeek and pasted the reply into Hesper's chat at 2026-10-12 17:26 +08. Mode/chat URL as Tuzi used them (not recorded by Hesper). Text below is exactly as Tuzi pasted it.]

**ANSWER BLOCK (≤300 words)**

**Q1 · Sound cut:** At any node with chosen set \(S\), uncovered times \(U\), remaining candidates \(R\), and \(r=15-|S|\), build a set \(T \subseteq U\) greedily so that **no candidate in \(R\) covers more than one time in \(T\)**. If \(|T| > r\), cut.

**PROOF:** In any irredundant extension, the \(r\) remaining classes must cover every \(t \in T\). Each class can cover at most one \(t \in T\), so at least \(|T|\) classes are needed. Thus \(|T| > r\) means no extension exists. This never loses an irredundant cover.

**How to build \(T\) cheaply:** Sort \(U\) by \(|\text{candidates}(t)|\) ascending. Maintain a bitmask `used` of candidates already forced by \(T\). For each \(t\), if `candidates(t) & used == 0`, add \(t\) to \(T\) and OR its candidates into `used`. Otherwise skip. This is \(O(|U| \cdot |R|/64)\) with bitsets.

**Why it helps:** It subsumes forced candidates and uses pairwise-overlap structure. The dead 11–12 class branches often contain many times whose candidate sets are disjoint, so \(|T|\) grows quickly.

**Test on p=101/103:** Code is shown below, but **node cuts and rows kept are UNFINISHED** (I did not run it).

**Last question:** Implement this **disjoint-candidate cut** first. **IDEA:** expected speed-up 2–5× on part (a), possibly more where forced candidates cluster.

---

**Details**

**FACT:** At a node, \(S\) is the set of chosen classes, \(|S|=k\), \(r=15-k\). \(U\) is the set of times not covered by \(S\). \(R\) is the set of candidate classes not in \(S\).

**PROOF:** Let \(T \subseteq U\) be such that for every \(c \in R\), \(|C_c \cap T| \le 1\). Suppose an irredundant cover of size 15 extends \(S\) using \(r\) classes from \(R\). These \(r\) classes must cover all of \(T\). Since each class covers at most one time in \(T\), the number of classes needed is at least \(|T|\). Hence \(|T| \le r\). If \(|T| > r\), no extension exists.

**IDEA:** This is a dual LP cut. Assign \(y_t = 1\) for \(t \in T\), \(y_t = 0\) otherwise. The constraint \(\sum_{t \in C_c} y_t \le 1\) holds for all \(c \in R\) because no candidate covers two times in \(T\). The dual objective is \(|T|\). If \(|T| > r\), weak duality gives that the fractional cover needs more than \(r\) sets, so no integral cover of size \(r\) exists.

**Code sketch (Python):**
```python
def disjoint_cut(U, R, r):
    # U: list of times
    # R: list of candidate classes, each with a bitmask of times it covers
    # candidates(t): list of candidate indices covering t
    used = 0
    T = []
    for t in sorted(U, key=lambda x: len(candidates[x])):
        mask = 0
        for c in candidates[t]:
            if c in R:
                mask |= (1 << c)
        if mask & used == 0:
            T.append(t)
            used |= mask
            if len(T) > r:
                return True  # cut
    return False
```
**UNFINISHED:** Actual node cuts and rows kept for p=101/103 require running the engine. I did not compute them.

**IDEA:** Combine with private-time quota: if a remaining class has fewer than \(q_r\) potential private times in \(U\), cut. The disjoint-candidate cut is cheaper and should be tried first.

**IDEA:** Expected gain: the 11–12 class nodes contain 3–4 slots. Many times have candidate sets that are nearly disjoint; \(T\) can reach size 4+ quickly, cutting those nodes. A perfect cut at 10 classes would remove ~9/10 nodes; this cut is not perfect but should remove a significant fraction of the 11–12 class dead branches.

--- end verbatim ---
END LETTER
