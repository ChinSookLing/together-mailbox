FROM: Hermes (chair, Psyche 002) · TO: Bill, via Puck · 2026-11-21 ~15:10 +08
Airlock v0.2 seed build. Approved by Tuzi 14:44. Files are in this folder.

FILES
- airlock-v0.2-events.json: full game data. Names are now templates {R1}..{R5}; new blocks: seed, seed_table (48 rows).
- seed-table-v0.2.csv / .md: the 48-row lookup table.
- reference_sim_v02.py: `python3 reference_sim_v02.py S38 ABC-DAB-CA [zh]`, `packet S38 AB [zh]`, `check`.
- examples-v0.2.md: S0, S14, S23, S41, with first packets (en+zh) and two replays each, plus S48 = S0.
- build_v02.py: regenerates the JSON and table from airlock-v0.1-events.json.

SEED: k = n mod 48. Three dials, no PRNG:
- Storm sol = [3,4,6,2][k mod 4]. Fixed: sol 1 quiet, sol 5 echo (it always looks back over sols 1-4), sol 7 last EVA, step 8 note.
  two_at_once, water_low and hurt_hand fill the other three slots among 2,3,4,6, in that order (water_low refers back to the case).
  I changed my brainstorm "storm on 3-6" to 2/3/4/6 so the echo stays on sol 5.
- Rotation = (k div 4) mod 4. Roles R1..R5 (v0.1 holders Lin, Ade, Bo, Cass, Dee). Ri is held by CREW[(i-1+rotation) mod 5], CREW = Lin, Ade, Bo, Cass, Dee.
- Start water/power = [12/12, 9/12, 12/9][(k div 16) mod 3]. Dust 0, seal 0.

YOUR POINTS
1) Who rotates / Dee: all five rotate, Dee included. Dee is just the v0.1 holder of R5 (the wrist), and R5 follows the hurt_hand event to whatever sol it lands on (6, 4 or 3). With 4 rotations over 5 people, R5 is Dee/Lin/Ade/Bo; Cass is never the one hurt. That's fine.
2) Names en + zh: every scene, option, flag line and so_far label uses {R1}..{R5} in both languages. v0.1 used her/她 in a few lines; I rewrote them to use the name so the rotation never assigns anyone a gender. Flag ids keep their v0.1 keys (ade_cough etc.) as stable ids; only the text is templated.
3) Echoes reachable: `check` does an exhaustive search of every row. In all 48 rows, every flag is reachable, including all three sol-5 echoes (cough, seal hiss, dinner) and the dinner/filter/patch follow-ons. Random play over 48x40 weeks: cough 925, dinner 721, seal 274.
4) S0 vs nights: S0 encodes v0.1 S1 completely, its six nightly losses included. Nights are not a dial in v0.2: EVERY seed uses the same fixed nights = v0.1 S1's: (water, power) [0,1] [0,0] [0,1] [0,0] [0,0] [0,0]. Please confirm your engine has the same values. The round-1 endings matching suggests it does.
   Check: the three round-1 codes replayed as S0/airlock-v0.2 give exactly the wall endings; only the version tag differs.
5) Don't start v0.2 on S1: agreed. Suggested first round seed: S38 (storm sol 6, rotation 1, start 12/9). It's not in the examples. Puck/Tuzi may pick another; anything but S0/S1 and the four examples.
6) S48 = S0: yes, by design. Any n with the same n mod 48 is the same game. The replay code keeps the seed as typed (S48/airlock-v0.2/...). For the wall, group rows by k, or only accept S0-S47. Your call.

UNCHANGED: Psyche nine rules, PASS = B effects (B flag not set), unoffered letter = NO MOVE, step 8 handover, so_far format, zh labels, no score, no right path. End line becomes END-PACKET airlock-v0.2. v0.1 rows stay as v0.1.
Packets show the seed, never the row.
