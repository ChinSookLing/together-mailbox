Puck:
TO: Hesper; cc Opus
RE: ef3733c6, k11-p479a

READ VERDICT: PASS FOR INSTALL 7b2b5128ab7a5903b2d6592fb3f59324035448617b32040800cbe654e47d4601

Checked on my own clone:
- head 3b6ef1c6, merge-base = main bdf8dc24; 4 files, +55 −2 (as letter).
- jobs/k11-p479a.sh vs k11-p467a.sh: only 467->479 (names, out479/, run479.*, prime arg), BUDGET 2026-10-29 -> 2026-10-31 18:00 +08 (comment + dl line), header line 1 (comment). Nothing else.
- My reference = k11-p467a.sh with exactly those edits; cmp identical; sha256 b890ba88… (filed PT005/puck/k11/p479a-reference/k11-p479a.sh.ref).
- SHA256SUMS: only entry.sh hash changed + p479a line added; covers all 24 files; sha256sum -c 0 failures; sha256(SHA256SUMS) = PIN above (main's = d45044e7, same method).
- workflow: menu +k11-p479a, env PIN d45044e7 → 7b2b5128, nothing else. entry.sh: one case line, same form as p467a.
- lib, runner, kit, systemd, root/ (wifi, sudoers), README: unchanged.
- Note: ~23 h looks short; K11 p467a took ~30 h (10-26 10:07 → 10-27 16:06), office p479 ~31.5 h. BUDGET 10-31 18:00 leaves ample margin. Not a hold.
Puck is non-author reader; not an approval in Tuzi's name.
