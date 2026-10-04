#!/usr/bin/env python3
"""
TOGETHER - PROOF TABLE 004 - Round 3 - Turn 11 - item L3-C: comparison with the archive
Seat: Fable-A (testing seat).

Compares my own results for the prime gate p = 83, k = 13 with the p = 83 certificate data
of Zenodo record 22066772 (J. Allikvere, "Fourteen lonely runners: manuscript, gate
certificates, and audit code", CC BY 4.0).  Only certificate DATA is read:
  small_gates/certificates_p83/SUMMARY.json
  small_gates/p83/raw/*.log, c12/*.log, filt/*.stats, filt/*.out, kill_orbit1.txt, kill_orbit2.txt
No program of the archive is read or run.

My files (written by pt004_l3c):
  LEVEL1   one line per unit orbit of I(13,83,1): the lexicographically smallest sorted tuple
  CASCADE  one line per orbit: |F_2|, |F_4|, ... until the first empty level
  LOG      standard output of the cascade run (holds the level-14 details)

The archive's rows use other representatives of the same orbits, so every archive row is
first brought to my normal form (smallest sorted tuple over all 41 units), in this script.

Standard library only.  Writes nothing.
Usage: python3 pt004_l3c_compare.py LEVEL1 CASCADE LOG ARCHIVE_DIR
       ARCHIVE_DIR = the folder that contains p83/ and certificates_p83/
Exit code 0 if every comparison agrees.
"""
import glob
import json
import os
import re
import sys
from math import gcd

P, K = 83, 13
N = (P - 1) // 2


def fold(x):
    r = x % P
    return min(r, P - r)


COVER = {v: frozenset(a for a in range(1, N + 1) if (K + 1) * fold(a * v) < P) for v in range(1, N + 1)}
ALL_TIMES = frozenset(range(1, N + 1))
_canon_cache = {}


def canon(t):
    """Smallest sorted tuple in the unit orbit of the multiset t (all N units tried)."""
    key = tuple(sorted(t))
    r = _canon_cache.get(key)
    if r is None:
        r = min(tuple(sorted(fold(u * x) for x in key)) for u in range(1, N + 1))
        _canon_cache[key] = r
    return r


def is_cover(t):
    s = set()
    for v in set(t):
        s |= COVER[v]
    return s == ALL_TIMES


def is_irredundant(t):
    cls = sorted(set(t))
    for c in cls:
        s = set()
        for v in cls:
            if v != c:
                s |= COVER[v]
        if s == ALL_TIMES:
            return False
    return True


def parse_levels(text):
    return {int(a): int(b) for a, b in re.findall(r"\bl(\d+)=(\d+)", text)}


def main():
    level1_file, cascade_file, log_file, arch = sys.argv[1:5]
    p83 = os.path.join(arch, "p83")
    ok = True

    def check(label, cond, detail=""):
        nonlocal ok
        ok = ok and bool(cond)
        print(f"  [{'OK' if cond else 'DIFFERENT'}] {label}{(' -- ' + detail) if detail else ''}")

    # ------------------------------------------------------------------ A
    print("A. My level-one list, re-examined in Python")
    mine = [tuple(int(x) for x in ln.split()) for ln in open(level1_file)]
    mine_set = set(mine)
    check(f"{len(mine)} rows, sorted, no row twice", mine == sorted(mine) and len(mine_set) == len(mine))
    check("every row is a cover of the 41 time classes (so it lies in I(13,83,1))", all(is_cover(t) for t in mine))
    check("every row is the smallest sorted tuple of its unit orbit (all 41 units tried)",
          all(canon(t) == t for t in mine))
    distinct13 = [t for t in mine if len(set(t)) == 13]
    irred = set(t for t in distinct13 if is_irredundant(t))
    reducible13 = [t for t in distinct13 if t not in irred]
    doubled = [t for t in mine if len(set(t)) == 12]
    covers12 = set(canon(tuple(sorted(set(t)))) for t in doubled)
    other = len(mine) - len(distinct13) - len(doubled)
    print(f"     13 distinct classes, irredundant: {len(irred)}")
    print(f"     13 distinct classes, containing a 12-class cover: {len(reducible13)}")
    print(f"     12 distinct classes with one class doubled: {len(doubled)}")
    print(f"     fewer than 12 distinct classes: {other}")
    print(f"     unit orbits of 12-class covers behind them: {len(covers12)}")

    cascade = {}
    alive = {}
    for ln in open(cascade_file):
        left, right = ln.split(":", 1)
        t = tuple(int(x) for x in left.split())
        cascade[t] = parse_levels(right.split("ALIVE")[0])
        if "ALIVE-AT-32" in right:
            alive[t] = right
    check("the cascade file has the same orbits as the level-one file", set(cascade) == mine_set)
    if set(cascade) != mine_set:
        print("RESULT: SOME COMPARISON DIFFERS (stopped: my two files do not describe the same orbits)")
        return 1
    surv_mine = set(t for t in mine if cascade[t][2] > 0)
    print(f"     my orbits with F_2 not empty: {len(surv_mine)}; with F_2 empty: {len(mine) - len(surv_mine)}")

    # ------------------------------------------------------------------ B
    print("B. The archive's logged level-one counts against mine")
    summary = json.load(open(os.path.join(arch, "certificates_p83", "SUMMARY.json")))
    bf = summary["base_family"]
    ir_rows_log = sum(int(re.search(r"raw_irred13=(\d+)", open(f).read()).group(1))
                      for f in glob.glob(os.path.join(p83, "raw", "ir_*.log")))
    c12_log = {int(re.search(r"root=(\d+)", s).group(1)): int(re.search(r"canonical12=(\d+)", s).group(1))
               for s in (open(f).read() for f in glob.glob(os.path.join(p83, "c12", "c12_*.log")))}
    check(f"archive irredundant rows: logs sum to {ir_rows_log}, SUMMARY says {bf['irredundant_raw_rows']}; "
          f"my irredundant orbits: {len(irred)}",
          ir_rows_log == bf["irredundant_raw_rows"] == len(irred))
    check(f"archive 12-class cover rows under root 0: {c12_log[0]}; my orbits of 12-class covers: {len(covers12)}",
          c12_log[0] == len(covers12))
    check(f"archive 12-cover rows over the 5 roots: {sum(c12_log.values())} (SUMMARY: "
          f"{bf['reducible_12cover_rows_prededup']}, 'prededup')",
          sum(c12_log.values()) == bf["reducible_12cover_rows_prededup"])
    check(f"archive total rows {bf['total_rows_filtered']} = {bf['irredundant_raw_rows']} + 41 x "
          f"{bf['reducible_12cover_rows_prededup']}",
          bf["total_rows_filtered"] == bf["irredundant_raw_rows"] + 41 * bf["reducible_12cover_rows_prededup"])

    # ------------------------------------------------------------------ C
    print("C. Every survivor row of the archive against my cascade (row by row)")
    files = sorted(glob.glob(os.path.join(p83, "filt", "*.out")))
    arch_rows = 0
    not_found = not_cover = level_diff = persist_diff = stats_diff = 0
    arch_orbits = set()
    ir_orbits = []
    prefixes = {}                       # root -> set of 12-prefixes seen in c12_root.out
    surv_by_file = {}
    first_zero_counts = {}
    persistent_rows = 0
    examples = []
    for f in files:
        name = os.path.basename(f)[:-4]
        rows_here = 0
        for ln in open(f):
            base = tuple(int(x) for x in ln.split("base:")[1].split("l2=")[0].split())
            levels = parse_levels(ln)
            rows_here += 1
            if not is_cover(base):
                not_cover += 1
            c = canon(base)
            arch_orbits.add(c)
            if name.startswith("ir_"):
                ir_orbits.append(c)
            else:
                prefixes.setdefault(int(name.split("_")[1]), set()).add(base[:12])
            if c not in cascade:
                not_found += 1
                continue
            if cascade[c] != levels:
                level_diff += 1
                if len(examples) < 5:
                    examples.append((name, base, levels, cascade[c]))
            if ("PERSISTENT" in ln) != (c in alive):
                persist_diff += 1
            persistent_rows += "PERSISTENT" in ln
            zero = [l for l in sorted(cascade[c]) if cascade[c][l] == 0]
            first_zero_counts[zero[0] if zero else 0] = first_zero_counts.get(zero[0] if zero else 0, 0) + 1
        surv_by_file[name] = rows_here
        st = open(f[:-4] + ".stats").read()
        if int(re.search(r"survivors=(\d+)", st).group(1)) != rows_here:
            stats_diff += 1
        arch_rows += rows_here
    check(f"archive survivor rows read: {arch_rows} (SUMMARY: {summary['cascade']['survivor_rows']}); "
          f"each file has as many rows as its .stats says", arch_rows == summary["cascade"]["survivor_rows"] and stats_diff == 0)
    check("every archive row is a cover", not_cover == 0, f"{not_cover} are not")
    check("every archive row's orbit is in my level-one list", not_found == 0, f"{not_found} missing")
    check("for every archive row, l2, l4, l8, l16, l32 are equal to my |F_2| .. |F_32|", level_diff == 0,
          f"{level_diff} rows differ")
    for e in examples:
        print("       example:", e)
    check("the archive's PERSISTENT mark and my 'alive at level 32' agree on every row", persist_diff == 0)
    check(f"set of orbits among the archive's survivors ({len(arch_orbits)}) = my orbits with F_2 not empty "
          f"({len(surv_mine)})", arch_orbits == surv_mine,
          f"only archive {len(arch_orbits - surv_mine)}, only mine {len(surv_mine - arch_orbits)}")

    # ------------------------------------------------------------------ D
    print("D. Rows the archive does not list (they died at level 2), predicted from my data")
    ir_surv_mine = sum(1 for t in irred if cascade[t][2] > 0)
    check(f"irredundant branch: archive survivors {len(ir_orbits)}, all different orbits, all irredundant; "
          f"my irredundant orbits with F_2 not empty: {ir_surv_mine}",
          len(set(ir_orbits)) == len(ir_orbits) == ir_surv_mine and set(ir_orbits) <= irred)
    check(f"irredundant branch: archive rows that died at level 2: {ir_rows_log - len(ir_orbits)}; "
          f"mine: {len(irred) - ir_surv_mine}", ir_rows_log - len(ir_orbits) == len(irred) - ir_surv_mine)
    check("the 12-class rows behind root 0 of the archive are exactly my 2042 orbits of 12-class covers",
          prefixes[0] == covers12)
    for root in sorted(prefixes):
        rows12 = covers12 if root == 0 else prefixes[root]
        predicted = missing = 0
        for s in rows12:
            for x in range(1, N + 1):
                lv = cascade.get(canon(s + (x,)))
                if lv is None:
                    missing += 1
                elif lv[2] > 0:
                    predicted += 1
        st = open(os.path.join(p83, "filt", f"c12_{root}.stats")).read()
        a_rows = int(re.search(r"rows=(\d+)", st).group(1))
        a_surv = int(re.search(r"survivors=(\d+)", st).group(1))
        src = "my own 12-class covers" if root == 0 else "the 12-class rows seen in the archive file"
        check(f"c12 root {root}: archive rows {a_rows}, survivors {a_surv}; from {src} x 41 extensions: "
              f"rows {41 * len(rows12)}, survivors {predicted}",
              a_rows == 41 * len(rows12) and a_surv == predicted and missing == 0,
              f"{missing} extensions are not in my level-one list" if missing else "")
    check("roots 1-4 only repeat 12-class rows of root 0",
          all(prefixes[r] <= prefixes[0] for r in prefixes))

    # ------------------------------------------------------------------ E
    print("E. The archive's cascade totals, recomputed with MY counts on the archive's rows")
    cs = summary["cascade"]
    mine_tot = {"died_l4": first_zero_counts.get(4, 0), "died_l8": first_zero_counts.get(8, 0),
                "died_l16": first_zero_counts.get(16, 0), "died_l32": first_zero_counts.get(32, 0),
                "persistent": first_zero_counts.get(0, 0)}
    for key in ("died_l4", "died_l8", "died_l16", "died_l32", "persistent"):
        check(f"{key}: archive {cs[key]}, mine {mine_tot[key]}", cs[key] == mine_tot[key])
    my_dead = {l: sum(1 for t in mine if [x for x in sorted(cascade[t]) if cascade[t][x] == 0][:1] == [l])
               for l in (2, 4, 8, 16, 32)}
    print(f"     (my own orbit counts, no row twice: empty at level 2: {my_dead[2]}, 4: {my_dead[4]}, "
          f"8: {my_dead[8]}, 16: {my_dead[16]}, 32: {my_dead[32]}, alive at 32: {len(alive)})")
    check("orbits alive at level 32 are the two named in the paper and the archive",
          sorted(alive) == sorted(tuple(int(x) for x in s.split())
                                  for s in summary["persistent_orbits"]["representatives"]))

    # ------------------------------------------------------------------ F
    print("F. The level-14 step")
    arch14 = {}
    for kf in ("kill_orbit1.txt", "kill_orbit2.txt"):
        text = open(os.path.join(p83, kf)).read()
        for blk in text.split("=== level-2 tuple:")[1:]:
            tup = tuple(int(x) for x in blk.split("\n")[0].split())
            digits = tuple(int(x) for x in re.search(r"prefix:([ \d]+)", blk).group(1).split())
            wi = int(re.search(r"witness_improper=(\d+)", blk).group(1))
            ia = int(re.search(r"improper_after_gcd7=(\d+)", blk).group(1))
            arch14[tup] = (digits, wi, ia)
    mine14 = {}
    log = open(log_file).read()
    for mobj in re.finditer(r"level-2 member([ \d]+): nodes=\d+ witness-free completions=(\d+) improper after gcd=(\d+)\n"
                            r"((?:      witness-free completion.*\n)*)", log):
        tup = tuple(int(x) for x in mobj.group(1).split())
        dig = re.findall(r"digits a_i \(w_i \+ a_i\*2p\):([ \d]+)->", mobj.group(4))
        digits = tuple(int(x) for x in dig[0].split()) if len(dig) == 1 else None
        mine14[tup] = (digits, int(mobj.group(2)), int(mobj.group(3)))
    check(f"level-2 members lifted to level 14: archive {len(arch14)}, mine {len(mine14)}, same tuples",
          set(arch14) == set(mine14))
    check("for each one: exactly 1 witness-free completion, 0 improper after the gcd test, and the same "
          "completion (same digits) as in the archive", all(arch14[t] == mine14.get(t) for t in arch14),
          "" if all(arch14[t] == mine14.get(t) for t in arch14) else str([(t, arch14[t], mine14.get(t)) for t in arch14][:2]))

    # ------------------------------------------------------------------ G
    print("G. Level 14 checked literally in Python on the definition (no lifting code)")
    L = 14
    LP = L * P

    def witness(w):
        for j in range(LP):
            if all((K + 1) * min((j * x) % LP, LP - (j * x) % LP) >= LP for x in w):
                return j
        return None

    def gcd_alternative(w):
        for i in range(K):
            g = L
            for j in range(K):
                if j != i:
                    g = gcd(g, w[j])
            if g > 1:
                return True
        return False

    special_ok = True
    random_ok = True
    tried = 0
    state = 20261003
    for tup, (digits, _, _) in sorted(mine14.items()):
        if digits is None:
            special_ok = False
            continue
        w = [tup[i] + digits[i] * 2 * P for i in range(K)]
        if witness(w) is not None or not gcd_alternative(w) or any(x % 7 for x in w):
            special_ok = False
        for _ in range(300):                       # other completions, pseudo-random digits
            d = []
            for i in range(K):
                state = (state * 6364136223846793005 + 1442695040888963407) % (1 << 64)
                d.append((state >> 33) % 7)
            if tuple(d) == digits:
                continue
            tried += 1
            if witness([tup[i] + d[i] * 2 * P for i in range(K)]) is None:
                random_ok = False
    check("each witness-free completion has no witness among all 1162 times, has every coordinate divisible "
          "by 7, and is proper by alternative (a)", special_ok)
    check(f"{tried} other level-14 lifts drawn pseudo-randomly: every one has a witness", random_ok)

    print(f"RESULT: {'every comparison agrees' if ok else 'SOME COMPARISON DIFFERS'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
