# PT005 R30 — p=19 transfer (Puck's four seats)

Packet: PT005/hesper/p19/send_R30_p19.txt @ c02bfff
Prompts sent ~20:06–20:09 +0800; collected by ~20:27 +0800.
Web/search OFF; DeepThink ON for DeepSeek; no Stop/Regenerate.
GPT first attempt: Connection interrupted → one resend (not Regenerate), then collected.

| Seat | Status | Sent | Received | File |
|------|--------|------|----------|------|
| Astra | PARTIAL | ~20:06 | ~20:16 | 2026-10-14T2006-r30-reply-Astra.md |
| GPT | PARTIAL | ~20:06 / resend | ~20:27 | 2026-10-14T2006-r30-reply-GPT.md |
| DeepSeek | PARTIAL | ~20:06 | ~20:16 | 2026-10-14T2006-r30-reply-DeepSeek.md |
| Grok | PARTIAL | ~20:09 | ~20:10 | 2026-10-14T2006-r30-reply-Grok.md |

## Consensus (4/4 PARTIAL)
- H = Q + D (mod 2) is p-independent on an alternating Hamiltonian 8-cycle.
- Distinct w mod 16 ⇒ Q=0, D=1 ⇒ H=1 ⇒ not doublable; checked on the nine p=19 length-8 sample rows.
- Gap for general PROVED: prove every prime p≥17 forces distinct w mod 16 in the length-8 mixed case.
- Part (2) single-class (p=17 b=6 vs p=19 never): unfinished.

## Puck independent checks
- Census MATCH (3ed5c93): p=19 doubling census CHECKED (two sandboxes).
- Objection: RESULTS line "every length-4 case has 8 distinct w mod 16" is too strong — 340 shortest-odd-4; 308 have 8 distinct; 32 fail (see 2026-10-14T2016-puck-notes-mod16-len4.md). Length-8 still 172/172.
- Breakthrough: NOT yet. Conditional transfer only; no general construction for distinctness.
