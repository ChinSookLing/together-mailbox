"""Builds airlock-v0.2-events.json and seed-table-v0.2.csv/.md from airlock-v0.1-events.json (Hermes, 2026-11-21).
v0.2 = v0.1 rules + a seed that really changes the game through a 48-row lookup table (no PRNG anywhere)."""
import json, copy, os, csv
H = os.path.dirname(os.path.abspath(__file__))
V1 = json.load(open(os.path.join(H, "..", "airlock-v0.1-events.json")))
T = copy.deepcopy(V1)

CREW = ["Lin", "Ade", "Bo", "Cass", "Dee"]          # five people on base; all five rotate
ROLES = ["R1", "R2", "R3", "R4", "R5"]               # v0.1 holders: R1 Lin, R2 Ade, R3 Bo, R4 Cass, R5 Dee
ROLE_DESC = {
 "R1": "sol 1 returner; at the lock on the sol 5 echo",
 "R2": "first of the pair (two_at_once); coughs in the filter echo; last EVA on sol 7",
 "R3": "carries the cracked case (two_at_once); re-buries its site (water_low)",
 "R4": "in the rover when the storm comes (storm_warning)",
 "R5": "twists a wrist on the rover ladder (hurt_hand)"}
STORM_SLOT = [3, 4, 6, 2]                             # index k % 4 ; 3 = v0.1
START = [(12, 12), (9, 12), (12, 9)]                  # (water, power), index (k // 16) % 3 ; (12,12) = v0.1
MOVABLE = ["two_at_once", "water_low", "hurt_hand"]   # keep this relative order (water_low refers back to the case)
FIXED_NIGHTS = [[0, 1], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0]]  # v0.1 S1's six nights (water, power), every seed

def row(k):
    storm = STORM_SLOT[k % 4]; rot = (k // 4) % 4; w, p = START[(k // 16) % 3]
    slots = [s for s in (2, 3, 4, 6) if s != storm]
    order = {1: "quiet_first", storm: "storm_warning", 5: "echo", 7: "last_return"}
    for s, ev in zip(slots, MOVABLE): order[s] = ev
    names = {r: CREW[(i + rot) % 5] for i, r in enumerate(ROLES)}
    return dict(k=k, storm_sol=storm, rotation=rot, water=w, power=p,
                order=[order[s] for s in range(1, 8)], names=names)
TABLE = [row(k) for k in range(48)]

# ---- templatise names (and replace pronouns by names: the rotation must not assign genders) ----
def sub(s, lang):
    rep = [("Lin", "{R1}"), ("Ade", "{R2}"), ("Bo", "{R3}"), ("Cass", "{R4}"), ("Dee", "{R5}")]
    for a, b in rep: s = s.replace(a, b)
    return s
FIX = {  # exact-text overrides where v0.1 used her/她
 "Lin is back from a routine sample run, red-grey dust on her boots and knees. Nobody else is due today. No hurry.":
   "{R1} is back from a routine sample run, red-grey dust on boots and knees. Nobody else is due today. No hurry.",
 "Cass stays in the rover until the storm passes (keeping the rover warm costs power; a long cold night for her)":
   "{R4} stays in the rover until the storm passes (keeping the rover warm costs power; a long cold night for {R4})",
 "讓 Cass 留在漫遊車裡等塵暴過（保暖耗電；她一夜又冷又長）": "讓 {R4} 留在漫遊車裡等塵暴過（保暖耗電；{R4} 一夜又冷又長）",
 "Spend the airlock hours on the filter; Lin brushes herself in (3h; the water loop recovers, her dust comes in)":
   "Spend the airlock hours on the filter; {R1} brushes in alone (3h; the water loop recovers, {R1}'s dust comes in)",
 "把閘時拿去修濾網，Lin 自己刷進門（3 小時；水循環恢復，她的塵進屋）": "把閘時拿去修濾網，{R1} 自己刷進門（3 小時；水循環恢復，{R1} 的塵進屋）",
 "Patch the seal first; Lin brushes herself in (2h; the seal is new again, her dust comes in)":
   "Patch the seal first; {R1} brushes in alone (2h; the seal is new again, {R1}'s dust comes in)",
 "先補密封，Lin 自己刷進門（2 小時；密封回到新，她的塵進屋）": "先補密封，{R1} 自己刷進門（2 小時；密封回到新，{R1} 的塵進屋）",
 "Dee twisted her wrist on the rover ladder. Scrubbing will hurt; the pain should ease by morning. Dust is packed in her glove seams.":
   "{R5} twisted a wrist on the rover ladder. Scrubbing will hurt; the pain should ease by morning. Dust is packed in {R5}'s glove seams.",
 "Dee 在漫遊車梯子上扭了手腕。刷洗會痛，天亮前應該會緩。塵塞滿了她的手套縫。": "{R5} 在漫遊車梯子上扭了手腕。刷洗會痛，天亮前應該會緩。塵塞滿了 {R5} 的手套縫。",
 "Full clean, slowly, with someone holding her arm (2.5h, water, power; it hurts)": "Full clean, slowly, with someone holding {R5}'s arm (2.5h, water, power; it hurts)",
 "慢慢全套清潔，有人扶著她的手（2.5 小時，用水耗電；會痛）": "慢慢全套清潔，有人扶著 {R5} 的手（2.5 小時，用水耗電；會痛）",
 "走衣口，有人幫她脫衣（1.5 小時，耗電，衣口會磨）": "走衣口，有人幫 {R5} 脫衣（1.5 小時，耗電，衣口會磨）",
 "Dee's wrist is better; she remembers who held her arm.": "{R5}'s wrist is better, and {R5} remembers who held that arm.",
 "Dee 的手腕好多了，她記得是誰扶著她。": "{R5} 的手腕好多了，記得是誰扶著那隻手。",
}
def walk(o):
    if isinstance(o, dict): return {k: walk(v) for k, v in o.items()}
    if isinstance(o, list): return [walk(v) for v in o]
    if isinstance(o, str): return FIX.get(o, sub(o, None))
    return o
for key in ("sols", "step8"): T[key] = walk(T[key])
T["ending"]["flag_lines"] = walk(T["ending"]["flag_lines"])
T["state"]["so_far_labels"] = walk(T["state"]["so_far_labels"])
T["state"]["so_far_labels_zh"] = walk(T["state"]["so_far_labels_zh"])
# sols become events placed by the seed; "sol" numbers in v0.1 are the v0.1 (S0) slots only
for e in T["sols"]:
    e["v01_sol"] = e.pop("sol"); e["who_role"] = sub(e.pop("who"), None)
T["events"] = T.pop("sols")

T["meta"].update(version="airlock-v0.2", decided="2026-11-21: seed design approved by Tuzi (14:44), built by Hermes, code by Bill")
T["rules"]["end_line"] = "END-PACKET airlock-v0.2"
for k in ("replay_code", "resume_line"): T["rules"][k] = T["rules"][k].replace("airlock-v0.1", "airlock-v0.2")
T["state"]["start"] = "per seed: water/power from seed_table; dust 0, seal 0"
T["state"]["night_rolls"] = "FIXED for every seed (no PRNG): nights 1..6 (water_loss, power_loss) = " + json.dumps(FIXED_NIGHTS) + " = v0.1 S1's nights. Plus the usual +1 water loss when dust is heavy or choking."
T["state"]["rules_in_order"] = [r.replace("seed's night roll (0 or 1 point each; table night_rolls)", "fixed night table (state.night_rolls)") for r in T["state"]["rules_in_order"]]
T["seed"] = {
 "parse": "S<n>, n = non-negative integer. k = n mod 48. Everything about the game comes from row k of seed_table. S48 = S0, S49 = S1, ... (same game; the replay code keeps the seed as typed).",
 "dials": {"storm_sol": "STORM_SLOT[k % 4] = [3, 4, 6, 2]",
           "rotation": "(k div 4) mod 4 -> role Ri is held by CREW[(i-1 + rotation) mod 5], CREW = Lin, Ade, Bo, Cass, Dee",
           "start": "START[(k div 16) mod 3] = water/power 12/12, 9/12, 12/9"},
 "fixed": "sol 1 = quiet_first, sol 5 = echo (it looks back over sols 1-4), sol 7 = last_return, step 8 = handover. The other three events (two_at_once, water_low, hurt_hand) fill the three non-storm slots among 2,3,4,6 in that order.",
 "roles": ROLE_DESC,
 "s0": "S0 = v0.1 S1 exactly (scene order, names, start 12/12, the six fixed nights). A v0.1 S1 replay replayed as S0/airlock-v0.2 gives the same ending text apart from the version tag.",
 "first_round": "v0.2 must not start on S1 (v0.1 S1 rows are on the wall). Suggested first round seed: S38 (storm sol 6, rotation 1, start 12/9). Keep it off the examples list.",
 "not_shown": "Packets show the seed, never the row. Nothing in the row is a score or a right answer."}
T["seed_table"] = TABLE
json.dump(T, open(os.path.join(H, "airlock-v0.2-events.json"), "w"), ensure_ascii=False, indent=1)

with open(os.path.join(H, "seed-table-v0.2.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["k", "storm_sol", "rotation", "start_water", "start_power", "sol2", "sol3", "sol4", "sol6", "R1", "R2", "R3", "R4", "R5"])
    for r in TABLE:
        w.writerow([r["k"], r["storm_sol"], r["rotation"], r["water"], r["power"], r["order"][1], r["order"][2], r["order"][3], r["order"][5]] + [r["names"][x] for x in ROLES])
ab = {"two_at_once": "pair+case", "storm_warning": "STORM", "water_low": "water low", "hurt_hand": "wrist"}
with open(os.path.join(H, "seed-table-v0.2.md"), "w") as f:
    f.write("# Airlock v0.2 seed table (k = n mod 48)\n\nSol 1 quiet, sol 5 echo, sol 7 last return are fixed. Roles: " + "; ".join(f"{k} {v}" for k, v in ROLE_DESC.items()) + "\n\n")
    f.write("| k | sol2 | sol3 | sol4 | sol6 | start W/P | R1 | R2 | R3 | R4 | R5 |\n|---|---|---|---|---|---|---|---|---|---|---|\n")
    for r in TABLE:
        o = r["order"]; n = r["names"]
        f.write(f"| {r['k']} | {ab[o[1]]} | {ab[o[2]]} | {ab[o[3]]} | {ab[o[5]]} | {r['water']}/{r['power']} | " + " | ".join(n[x] for x in ROLES) + " |\n")
print("built", len(TABLE), "rows")
