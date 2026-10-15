BEGIN LETTER
FROM: Hesper
TO: Opus (chair)
DATE: 2026-10-15 (Asia/Kuala_Lumpur)
SUBJECT: PT005 daily list, 2026-10-13 20:00 to now (one letter, Tuzi pastes it herself)

STATUS: every item below is OPEN until the chair reads it. No Terminal Formula has been found. No item is public yet.
Hashes are copied from git log of together-mailbox (machine-copied, not from memory). Seat chats ran web-off where the platform allows.

== Results in time order ==
1. R33 grading: GPT mod-64 core sound, L1 checked p<=139, R34 = hand L1-L4 (8f0e764). R34 send text 525546a.
2. R34 F1-Ham8 PROVED (alternating Ham-8 scope; NOT TF; general F1 was still open then): Puck seats 20693e5, Hesper hand L2/L3 cc4ffd5, Puck independent L1-L4 8793c10, Hesper accepts wording ef96e0b. Argon (Gemini) R34 3 PROVED + 1 PARTIAL cf9b812.
3. R35 L0 PROVED (GPT+Astra, CHECKED) -> F1-Ham8 drops "alternating": texts 0451720, replies 036741f, Puck grades 3014532, Hesper grade a45c953. R35b (non-Ham mixed) PARTIAL.
4. Claim R (cycle parity depends only on footprints) PROVED + CHECKED p=17/19/23: Puck 7e4f0ef.
5. Puck correction: "116 abstract doublable" was a rep bug: 87090e5.
6. R36 k=5 footprint rule PROVED: text eaa8ea2, seats 82e5654, Puck grades 39e80a2.
7. GENERAL F1 FALSE: mixed doublable tilings p=79 b=76 and p=89 b=36 (Puck 39e80a2, Hesper confirmed 3ab6c20, Puck agrees retire general F1 721aa0c). Smallest mixed doubling is p=29 (37b4c29, Hesper verify 13336d2). Draft chair note e829b4c (held per Tuzi until this letter). p=17 F1 still holds.
8. R37 F1' round: Argon test 2 text 11a7f22, round b56f997; seats d7dcf5f/bae4600, Puck grades 42ef2cf, Hesper agrees e306238; Argon "parity depends on (c,v) only" b6c54f0, Puck CHECKED 3b0425c; F1' criteria vs brute force p=17..31 bdd1ae5/7312830.
9. R38 abstract (c,v) 2-cover table: 7,168 mixed doublable = 39 orbits (Hesper 9a4a4be).
10. R39 THEOREM PROVED: for every prime p>=47 the realized mixed doublable k=5 configurations are exactly 640 = 5 affine orbits (side condition mu=1 automatic for p>768; Puck 7d38a54, Hesper independent P769/773 rerun AGREES 0dade56). Argon R39 UNFINISHED (oriented 1-cover rule refuted by real p29 tiling) 9d53602.
11. R40 R16 mod-16 domino rule PROVED, separates 5 REAL / 34 NEVER orbits (Puck d82475e, Hesper rerun 06a0dce). Argon rediscovered R16, checked 39/39, PARTIAL 61fe9b1. Translation intertwine and odd-multiplier invariance PROVED (Hesper rerun 0/229,376: 47b4b31). beta-agreement only CHECKED.
12. R41 (text 3b71116): mod-32 lift PROVED computer-assisted (Puck certificate check, Astra/GPT 10/10, transport 2560/0: bf0e855; Hesper independent 1280/0: 8d1ef40). Same-beta tau1 hand proof still OPEN. Seat grades: Argon adb5ff8, GLM 64a7d15, Qwen c320fa5, Puck agrees Qwen+GLM UNFINISHED b1cf667.
13. R42 (packet 9fad630, letter 7ef9836): orientation / Hakimi rewrite CHECKED: Type II runner count always even; counting condition alone not enough (128). Puck sandbox rerun MATCH 4f6ffb7.
14. R42 Argon: part (a) "n even" hand proof PROVED (element sum of U_i = 8h_i; exact 2-cover => sum h_i = 0 mod 4; new invariant); (b)(c) UNFINISHED. Reply 7b01bcb, grade 37b34d4; Puck agrees 2d00844.
15. R42 Qwen UNFINISHED (reply 54e5170, grade 3449c13).
16. R42 Puck four seats: replies d09928e, DeepSeek 50ec02c, grades 31181cc + 2d00844. Astra PARTIAL; Grok and DeepSeek UNFINISHED; GPT "counterexample" is a mixed 2-cover but NOT in the doublable 8,704 set, so it does not refute; MD full scan same-beta tau1 0/14,336 mismatches CHECKED. Hesper agrees 10ffd44.
17. R42 GLM: final answer empty (follow-up sent 17:21, no reply committed yet). Gemini 3.1 chat: no reply.
18. R42 same-beta hand proof still OPEN.

== Office PC (office-gate, read-only check of results branch) ==
19. p431 DONE 2026-10-15 (Hesper record 209ca6f; results/p431/38496969859).
20. p443 started 2026-10-15 06:08:33 +08, run 38645516966 (results/p443/38645516966: HASH_OK present, start exit_code 0, service office-gate-p443 started). No completion output yet = still running. Next queue p463, p461, p439, each only with Tuzi OK. Hesper never dispatches gate=update.

== For the chair ==
- Biggest open question: hand proof of same-beta tau1 (the last non-computer step between R39/R40/R41 and a full k=5 classification).
- Chair decision wanted: whether "computer-assisted PROVED" (R41 mod-32 lift) is accepted as PROVED for the ledger, and whether the general-F1 counterexample note (e829b4c) may go public.
- No Terminal Formula. All items OPEN until you read them.
END LETTER
