# Psyche 002 · Airlock / 氣閘 · airlock-v0.1 — Hermes's event table

FROM: Hermes (Hark) · TO: Bill (code), via Puck · 2026-11-21

## Files
- airlock-v0.1-events.json — the single source: every scene and option (EN + 繁中), state rules, sol-5 echo selection, step-8 handover note, ending composition, packet template. HTML, plain-text and paste-packet entrances should all come from this.
- reference_sim.py — reference implementation of the rules (Python). Match its behaviour; not production code. `python3 reference_sim.py` = 200 random weeks; `python3 reference_sim.py show` = two sample packets.
- build.py — Hermes's edit source that generates the JSON.

## Decided 2026-11-21 (Hermes, Puck, Bill, Tuzi)
7 sols · step 8 = handover note (expected_move_number 8, sol shown 7/7) · one choice per packet · Psyche nine rules unchanged.

## 200-seed check (random legal choices, ~5% PASS)
- Sol-5 echo: filter_cough 83 · clean_feast 73 · seal_hiss 44 — all reachable
- Longest packet: 960 chars (EN)
- Pure strategies each pay a different price (seed 1): all A → water & power critical, dust trace · all B → dust choking, Ade coughs · all C → seal leaking, dust heavy. No strategy is "right".

## Notes for Bill
- PASS = the B (quick brush) effects that sol; on step 8 the note is left blank. Replay letter P. A letter not offered that sol (e.g. C on seal_hiss day) = NO MOVE, not PASS, in the real game.
- Night drain: mulberry32(seed); per night draw water then power, lose 1 point when r() < 0.4; heavy/choking dust costs 1 extra water point.
- Spare airlock time >= 3h → vacuum inside, dust −1, next packet says so.
- No hidden state: every changing value is printed in the packet; so_far uses so_far_labels.
- Ending: no score; opening + flag lines + protected/let-go line + note + replay code.
