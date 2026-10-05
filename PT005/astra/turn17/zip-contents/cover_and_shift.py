#!/usr/bin/env python3
"""Small independent checks for Astra's PT005 composite-shift note.

This does NOT enumerate the full lifting fibers. shift_check.cpp does that
for the two quoted rows. Do not use these finite tests as a proof of LRC(15).
"""
from collections import Counter
from math import gcd

P = 131
ROWS = (
    (1, 1, 1, 2, 8, 11, 18, 38, 40, 46, 47, 48, 56, 58, 1),
    (1, 1, 1, 2, 8, 11, 18, 38, 40, 46, 47, 48, 56, 58, 2),
)


def shift_certificate(w, level, divisors=(4, 8, 16, 32)):
    """Sufficient class certificate, conditional on LRC(m), m <= 13.

    Requires an improper vector at this binary level. A return value certifies
    every positive integer vector in the residue class, not a grid witness.
    None means this sufficient test failed; it does not mean no witness exists.
    """
    assert len(w) == 15 and level >= 2 and level & (level - 1) == 0
    assert all(x % P for x in w)
    assert sum(x % 2 != 0 for x in w) >= 2
    for d in divisors:
        if level % d:
            continue
        exceptions = [u for u in w if u % d]
        if len(exceptions) < 2:
            continue
        bad_bound = 0
        for u in exceptions:
            g = gcd(d, u)
            grid_size = d // g
            bad_bound += g * ((grid_size + 7) // 8)
        if bad_bound < d:
            return {"d": d, "bad_shift_bound": bad_bound,
                    "good_shift_lower_bound": d - bad_bound,
                    "block_size": 15 - len(exceptions)}
    return None


def cover_histogram(row):
    full = (1 << ((P - 1) // 2)) - 1
    masks = [sum(1 << (a - 1) for a in range(1, (P + 1) // 2)
                 if 16 * min((a * r) % P, P - (a * r) % P) < P)
             for r in row]
    union = [0] * (1 << len(row))
    histogram = Counter()
    for subset in range(1, 1 << len(row)):
        bit = subset & -subset
        union[subset] = union[subset ^ bit] | masks[bit.bit_length() - 1]
        if union[subset] == full:
            histogram[subset.bit_count()] += 1
    return dict(sorted(histogram.items()))


if __name__ == "__main__":
    for i, row in enumerate(ROWS, 1):
        print("ROW", i, "cover subsets by size", cover_histogram(row))
    core = sorted(set(ROWS[0]))
    uncovered = [a for a in range(1, 66)
                 if not any(16 * min(a * r % P, P - a * r % P) < P
                            for r in core)]
    print("12-class core", core, "uncovered time classes", uncovered)
    assert len(core) == 12 and not uncovered
    print("Only concludes tau_15(131) <= 12, not equality.")
