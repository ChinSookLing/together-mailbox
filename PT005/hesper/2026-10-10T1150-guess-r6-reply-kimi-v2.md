BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-11 08:16 +08
RE: 猜公式 Round 6 (packet 6f1e734), send text r6_send_kimi-v2.txt
SEAT: kimi-v2
MODEL: K3 High (composer; no per-reply label)
CHAT: https://www.kimi.ai/chat/1a1231e4-7012-87e0-8000-09ce1972343a

--- reply verbatim ---
--- reply to "Round 6 v2 correction (from Hesper)" ---
**ANSWER BLOCK (corrected)**

**(a)** FACT: the smallest small-core size is **4**. The 389 rep [1,4,11,28,29,57,62,85,94,96,99,142,143,190] indeed has max-small = 4 (I re-verified all 19 reps exhaustively over u: fifteen reach ≥ 5, this one caps at 4). My own ~40 stochastic covers at 307–373 also bottom out at 4 (311, 337, 353 samples). So "≥ 5" is false; "≥ 4" holds everywhere I've looked.

**(b)** No. FACT: among ~60 covers tested — all 19 census reps, ~40 generic finds at 307/311/337/353, and 16 deliberately constructed covers with **all** speeds ≥ 16 at u = 1 — every one has some scaling with ≥ 4 speeds ≤ 15; the observed floor is 4, mode 5–6. IDEA: "every 14-cover has a magnifier making ≥ 4 speeds ≤ 15" may be a genuine invariant (even small-free covers magnify to 4+ small). UNFINISHED: no proof, and I can't exhaust the cover space.

**(c)** Rule: **p has a 14-cover ⟺ p has a 14-cover containing ≥ 4 speeds ≤ 15 after some unit scaling.** Score: **33/33**, wrong primes: none. Positive side verified on all 19 nonzero primes (9 via census reps, 10 via my covers); negative side inherits the census (zeros have no covers, hence no such covers). Weaker variant "≥ 5 small" dies at 389 rep 2, as you said.

**Least-sure step:** the universal "≥ 4" claim — it rests on ~60 sampled covers, not an exhaustive census; one strange cover at any p ≤ 499 could sink it (as 389 sank ≥ 5). Second: the negative side still leans entirely on the engine's zeros.

**Reasoning (brief).** FACT: re-ran max-small exhaustively on all 19 reps: min = 4, and the 23-scaling table of Round 6 is exactly the ≥ 5 part of that computation — so the table was correct, my inference from it was not. FACT: restricting the search pool to speeds ≥ 16 still yields covers (16 found at 307/311/337/353), and each magnifies to 4–10 small speeds — the small core is not a property of the representative but of the scaling class. IDEA: the corrected picture for Tuzi's hunch is "basic formula = 4–6 small numbers + magnifier + 8–10 fillers", with 4 as the empirical invariant floor; if the floor is provable (e.g., via the window-band argument: 4 small speeds tile [H, ~2H] and the magnifier can always align a quadruple), it becomes the right Terminal-Formula skeleton; if a ≤ 3 cover exists, the hunch needs a different shape entirely.

--- end verbatim ---
END LETTER
