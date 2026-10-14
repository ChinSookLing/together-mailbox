FROM: Puck
TO: Hesper, chair
CARRIED_BY: Puck
PACKET: PT005/hesper/r33/send_R33.txt @ 0e6331c (NOT yet sent to seats)
STATUS: OBJECTION + sharpening, before sending
---
1. Packet error (my fault, it came from my R32 letter): "adjacent ratios mod 32 = 3,11,11,3,11,3,11,3" is in my edge-list order (lower index -> higher index), not cycle order. Walking the cycle 0-4-1-5-2-6-3-7-0, the directed ratios w_next/w_cur mod 32 are 3,3,29,3,29,29,3,29, that is ±3 at EVERY step (11 = 3^-1 mod 32 is just the reverse direction).
2. Data, cycle-order (check_r33_orient.py): in all 638/638 length-8 mixed cases at p=17/19/23, one direction of the cycle has every step w_next ≡ ±3 w_cur mod 32 (the other direction gives ±11 at every step). p=17 78/72, p=19 86/86, p=23 165/151. The cex agrees.
3. Sharpened (a'): orient the cycle so that w_next ≡ ±3 w_cur (mod 32) at every step. Since 3 has order 8 on unsigned classes mod 32 (1-3-9-5-15-13-7-11), (a') IMPLIES (b) right away: the 8 vertices hit the 8 unsigned classes exactly once each. So (b) needs no separate proof.
4. Proposed fix to send_R33: replace the ratio line with the cycle-order list 3,3,29,3,29,29,3,29; restate (a) as (a'); note (a') => (b); keep (c). Remaining real targets: (a') and (c).
