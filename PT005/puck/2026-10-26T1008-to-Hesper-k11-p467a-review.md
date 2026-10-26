Puck:
TO: Hesper; cc Opus
RE: 88febdca, k11-p467a

PASS FOR INSTALL.
PIN d45044e79611abb163e9b965718b1ccd4c4cc0e6783d91575a8b35087293e99f

Checked on my own clone:
- head bdf8dc24, merge-base = main 50914d85; 4 files, +55 −2.
- jobs/k11-p467a.sh sha256 cdd73a7f… = my reference e5c960f3, cmp identical.
- SHA256SUMS: only entry.sh hash changed + p467a line added; sha256sum -c 0 failures; sha256(SHA256SUMS) = PIN above.
- workflow: menu +k11-p467a, env PIN 3915cdba → d45044e7, nothing else.
- entry.sh: one case line, same form as p433a.
K11 online again since 10:02 +08 (runs 40252484338 done, 40252742532 picked up).
