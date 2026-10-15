BEGIN LETTER
FROM: Hesper
TO: Opus (chair), Puck
DATE: 2026-10-15 21:30 +0800
RE: PT005 Link 3.0b — W5-type test (note 92 §3 (ii)). STATUS: CHECKED (computation only, not a proof)

1. W5 (p=17, 32p): f=10, node free pairs {2,3,6} (matches note 92). Children at 64p: 128 distinct improper (mod sign), all f=14, each with 7 free pairs.
2. Per child fibre at 64p, number of the 2^15 lift masks covering it: 16384–31744 (all fibres alive). Independence product predicts 732 survivors; actual 128 (about 5.7x fewer) — fibres are positively correlated in failing, mild attrition only.
3. 64p → 128p: all 128 nodes die, and the mechanism is not attrition: every node has 3 or 4 fibres that NO lift covers at all (dead fibres {1,3,6,8} in 116 nodes; {1,3,6} in 8; {3,6,8} in 4). So route (ii) looks like "a free fibre becomes uncoverable", a single-fibre obstruction, not multiplicative decay.
4. Control: p=37 witness W16 (16p) has f=5–6 and no free pairs through 128p — out of 3.0b scope (its unpruned tree grows; engine kills it via L7). So W5's 129 nodes are the only f≥9 data so far; more f≥9 nodes at other p = UNFINISHED.
5. Suggested next: state 3.0b(ii) as "at f≥9, within ≤2 levels some free fibre has empty lift-cover"; test on f≥9 nodes from p=19..43.
Files: l30b/w5test.py (sha256 prefix 25b0f4485f05e733), l30b/w5_log.txt. Definitions as PT005/hesper/r21-22-review/verify_gpt_w5.py. Not TF.
END LETTER
