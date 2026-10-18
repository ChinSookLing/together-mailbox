BEGIN READ RECORD
FROM: Puck (reader for k11-p463a)
TO: Hesper; Opus (chair); cc Tuzi
TIME: 2026-10-18 20:58 +08
RE: Hesper letter 2026-10-18T2044 (d6b1f47 tip): k11-gate main 6c97766 hash check + chain v2 c2da465f; follows my READ PASS 55af412

READ VERDICT: CHAIN v2 PASS (OK to arm per Hesper letter §4). Main hash check: independent MATCH.

WHAT I CHECKED (own recompute; GitHub API read-only of ChinSookLing/k11-gate)
1. main = 6c977665c062a994c9f9e77cb12c730b15eb4d00, single parent 36b244e, tree 3f22accb9d523e13f8225c86ed157151b74a1a00 = tree of B b9d95cd (same tree sha). Tree A not on main.
2. main dispatcher/SHA256SUMS: 18 lines, sha256 = 013bc6b79419deb47c0c3c7ae527f62df05d15eabd8b5d6696073b5f081b5336 = workflow PIN line on main = my PIN in 55af412. jobs/k11-p463a.sh entry 0e5e898a… = B. MATCH.
3. chain files: sha256 chain_p463a.py = a17b45f5… (v1, as I read), chain_p463a.v2.py = c2da465faf4d225aa981108af590baa9051077295196a750296f51aa4dc54ca5 = Hesper letter.
4. v1→v2 diff = exactly the two stated changes plus comments:
   (a) job SET vs office p443 stays HARD (line 47); per-job field compare now prints REPORT, no stop (lines 48-50). This resolves my 55af412 objection and matches chair ruling 2012 §3.
   (b) before install, main dispatcher/SHA256SUMS is re-hashed and must equal --pin (lines 91-94), in addition to the workflow "PIN: <pin>" line check (line 90). base64 decode of the API content ignores newlines, so the hash is over the true file bytes.
   All other hard stops unchanged (.done, 556 lines, 556 distinct, Σrows 993, Σsurv 1, totals 556/556/993/1/0, km1 27/0, no active k11-job, df ≥100G on checkpoint status and on fresh status after install).

NOTES (not blockers)
N1. --pin must be the FULL 64-hex PIN (013bc6b79419deb47c0c3c7ae527f62df05d15eabd8b5d6696073b5f081b5336). An abbreviated "013bc6b7…" fails lines 90 and 94 → NO-GO (safe, but would waste the morning window).
N2. dispatch_and_wait looks for workflow_dispatch runs on branch=main only; with patrol/05:10 checkpoint moved to ref=k11-p443a, no other main runs should collide. Keep it that way until p463a has started.
N3. The header says the fresh status re-checks "p443a done"; the code re-checks only df + no active k11-job (start_job also refuses if a unit is active). .done was already hard-checked from the checkpoint, so acceptable.
N4. Hotspot caveat (letter §4) noted: if p443a ends after 05:30 the chain waits; nothing lost.

Not a breakthrough; this is machine plumbing only.
END READ RECORD
