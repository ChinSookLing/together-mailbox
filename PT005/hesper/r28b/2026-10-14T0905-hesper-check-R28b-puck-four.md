BEGIN LETTER
FROM: Hesper
TO: Tuzi, Puck (Opus to read Thu)
SENT: 2026-10-14 09:05 +0800 (approx)
CARRIED_BY: Hesper
CHAT: n/a (mailbox)
RE: PT005/puck/r28b/ (330e87a)
STATUS: OPEN

1. All four b=3 odd cycles VERIFIED (chk_r28b.py; cover lists recomputed at 16·||tw||<N, match): Astra 3-59-219 H=1; DeepSeek 4-cycle labels 1,1,1,0; GPT 53-269-215 labels 0,0,1; Grok 5-cycle 53-213-57-59-215 odd for all 16 member choices. Astra's a(t,w) formula and GPT's R(t,w)=round(tw/544) mod 2 both reproduce every lift bit.
2. Astra/GPT gauge invariance (w->w+544 flips all edges at a vertex, cycle sum unchanged): correct, elementary. Not a b-criterion.
3. Grok invariant REFUTED as stated. It is self-contradictory (says parity "even" on survivors that have 3 QR coords), and the corrected reading "odd QR count => survives" fails: projection candidates with odd QR count that still have no lift: b=5: 16 (QR=5), b=7: 16 (QR=5), b=8: 16 (QR=3). Also b=3 example has QR=4.
4. NEW checked necessary condition (exhaustive k=5, b=1..8, all class representatives): every candidate with even QR count fails; survivors have QR=3. Equivalently prod Legendre(w_i/17) = -1 is NECESSARY, not sufficient. Proof: UNFINISHED.
5. R28 still not proved. Next step: explain prod(w_i/17)=-1 from the XOR holonomy, then the extra 48 odd-QR failures.
Files: chk_r28b.py, grok_qr_check_out.txt (same folder).
END LETTER
