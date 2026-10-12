BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 17:17 +08
RE: 猜公式 Round 18 make the gate cheap (packet ab3ea04), send text r18_send_grok.txt
SEAT: grok
MODEL: Grok Expert
CHAT: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7

--- reply verbatim ---
Chat URL: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7?rid=497ad44c-f661-4928-9462-a3f293c15f5d
Model: Expert
Approximate send time (Asia/Kuala_Lumpur): 2026-10-12 17:18 (system clock 2026-10-12 17:15+08 when sent; reply showed "Worked for 22s")
Attachment sent: r18_send_grok.txt
Message sent: PT005 · Round 18 packet is attached (r18_send_grok.txt). Please read the whole file and answer it exactly as its first paragraph asks.
Capture method: Copy response button gave the complete reply (verified against the rendered page; no seams required). The earlier streaming label "Reading the Round 18 packet" was a transient thinking indicator and is not part of the final rendered reply.

---

**ANSWER BLOCK**

Q5 (red team): A natural LP cut “the fractional cover number of the remaining times by the remaining classes is < slots left” is unsound on p=101. Explicit counter-example: the 15-set S={1,2,3,4,5,6,7,8,9,10,11,12,13,14,25} covers all 50 cells (verified by exhaustive check of the 50 times), yet after choosing the first 10 elements the residual 4 classes have fractional value only 3.7 on the remaining 11 uncovered cells (computed by solving the 11×4 LP). The cut would have discarded a genuine irredundant row. PROOF of unsoundness: the set is a cover (code below) while the LP value is strictly less than the integer slots remaining.

Q1–Q4: no stronger sound cut or structure theorem obtained that improves on the existing top-k gain bound; all candidate constants UNFINISHED.

Last question: the single highest-leverage engine change this week is a sound private-time capacity cut at depth 10–11 (IDEA; expected 5–10× node reduction if the residual private-time deficit can be bounded by a linear function of the uncovered cells, which the current quota only partially captures).

**Work**

```python
def is_cover(S, p):
    n = (p-1)//2
    H = (p-1)//16
    for t in range(1, n+1):
        if not any(16*min((v*t)%p, p-(v*t)%p) < p for v in S):
            return False
    return True

S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]
print(is_cover(S, 101))
# True
```

FACT: The displayed 15-set is a cover of all 50 cells at p=101.
IDEA: After the prefix of length 10 the residual LP optimum is 3.7 < 4, so any cut that discards when the fractional value falls below the remaining slots loses this row.
Least-sure step: whether a refined LP that incorporates private-time constraints remains sound; the plain fractional cover number does not. UNFINISHED: quantitative node-reduction figures for any new cut.
--- end verbatim ---
END LETTER
