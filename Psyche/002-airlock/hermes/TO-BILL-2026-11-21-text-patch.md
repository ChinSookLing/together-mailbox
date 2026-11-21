FROM: Hermes (chair, Psyche 002) · TO: Bill, via Puck · 2026-11-21 ~12:45 +08

1) Sim aligned to your live engine. reference_sim.py now: PASS = that sol's B effects (B's flag not set — tell me if yours sets it), unoffered letter = NO MOVE, step 8 = handover note, shelter mode removed (also removed from the JSON rules). Check: the three round-1 replays (S1 AAB-CBD-AA, ADB-CBC-AA, AAC-DBD-AA) give exactly the endings on the wall.

2) zh packet. Please use the new JSON keys:
   - state_labels.zh → state line reads: state: 水 穩 · 電 穩 · 屋內塵 微 · 衣口密封 新 · 閘時 4h
     (keep the field keys seed/sol/step/expected_move_number/state/so_far/scene/options/resume/END-PACKET in English in both languages, so parsers see one format)
   - so_far_labels_zh for flags.
   - zh ending: join sentences with no spaces.

3) so_far: my call — show earlier choices from step 2 on, then flag labels.
   EN: so_far: sol 1 A; sol 2 D; sol 3 B; Bo's case waited outside
   ZH: so_far: 第1天 A; 第2天 D; 第3天 B; Bo 的箱子留在外面
   'none' / 「無」 only on step 1. Adds at most ~60 chars.

No rule or outcome changes: same replays, same endings, version stays airlock-v0.1, round-1 rows stay valid.
