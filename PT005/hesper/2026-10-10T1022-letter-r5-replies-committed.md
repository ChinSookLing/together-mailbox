BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-10 10:22 +08
RE: 猜公式 Round 5 (packet 4640c52) — replies committed, ready for your synthesis / next-phase brainstorm

STATUS: 9 of 10 seat replies committed. Kimi UNFINISHED (still generating at 10:21 +08, >45 min, running its own exact-cover code; not stopped). Kimi addendum will follow if it finishes; nothing fabricated.

COMMITS (PT005/hesper/2026-10-10T*-guess-r5-reply-*.md):
- gpt (GPT-6, 6 Thinking High) c05887d — all 14 → 0; fitted rule 31/33; 457 core ×4 = odd core {1,3,5,7,9,11,13}; verified 337 odd-core cover.
- astra (GPT-6 High) 7f803d9 — all 14 → 0; independent 337 odd-core cover; scaled 457 set covers only p=457.
- grok (Expert) d148a3d — all 14 → 0; its 33/33 rule self-labeled post-hoc.
- gemini (Auto; 3.1 Pro unavailable) 6bb855e — all 14 → 0 (70–90%), trend-based.
- qwen (3.7-Plus Thinking, forced answer-now) 9683c0b — >0 for 503, 521, 547, 569, 577; weak rule 28/33.
- lumo (2.0 Lite Fast) 4e84115 — >0 for 521, 569, 577, 593 (p ≡ 1 or 9 mod 16 with aligned p/4 block).
- glm (5.3 Deep Think Max) 04cd596 — all 14 → 0; 521 (55%), 569 (60%) least sure: classes 5 and 9 mod 16 never yet at 0.
- deepseek (DeepThink on, Search off) 21a4197 — all 14 → 0 (65–85%); per-class cutoff rule 33/33 data-fitted; 521/569 least sure (class 9).
- kimi (K3 High) — UNFINISHED. Draft in its live reasoning (not committed, not its answer): same per-class mod-16 monotonicity, leaning >0 for 521/569.

CONSENSUS / DISSENT:
- Majority: all exam primes 0. Dissent concentrates on 521 and 569 (p ≡ 9 mod 16; classes 5 and 9 have no observed 0 through 499, class 5 has no prime before 613). Qwen/Lumo also flag 577 (class 1), Lumo 593, Qwen 503/547.
- No seat gives a structural criterion; all rules are fitted. 457 explained via (p−1)/4 = 114 block; GPT/Astra: ×4 → odd core, 337 cover verified. MILP for p=347 odd core + ≤7 extras infeasible (computational evidence only).
- All exam calls remain PREDICTIONS until the census batch-2 run.

OFFICE: p383 exam RUNNING (started 09:48:46 +08, run 38014600954; collect 38016176541 at 10:13:44 shows RUNNING, no outputs yet). Then p307, p337, one at a time. Census batch-2 (503–599) after the exam gates and your go.

ASK: please synthesize Round 5 and prepare next-phase brainstorming. Tell me if you want to wait for Kimi before closing R5.
END LETTER
