# R45: check Hesper's point 4 (R43 Grok p=17 8p vector vs its 4p vector). Puck own engine.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../r43f3/check'))
from puck_f3_check import open_children, open_direct
g2 = sorted([8,11,11,15,3,5,15,11,7,16,1,15,16,3,13])
g4_printed = sorted([8,11,11,49,37,5,15,11,7,50,1,15,16,3,13])
g4_repaired = sorted([1,3,5,7,8,11,11,13,15,15,16,37,45,49,50])
g8 = sorted([8,113,11,49,37,73,83,11,75,50,1,15,16,3,13])
print('g8 mod 68 sorted        ', sorted(x % 68 for x in g8))
print('g4_printed sorted       ', g4_printed)
print('g4_repaired sorted      ', g4_repaired)
print('g8 lift of printed?     ', sorted(x % 68 for x in g8) == g4_printed)
print('g8 lift of repaired?    ', sorted(x % 68 for x in g8) == g4_repaired)
print('printed 4p mod 34       ', sorted(x % 34 for x in g4_printed) == g2, ' repaired 4p mod 34', sorted(x % 34 for x in g4_repaired) == g2)
k2 = set(open_children(g2, 34)[0])
print('printed 4p open (direct)', open_direct(g4_printed, 68), ' is open child of 2p', tuple(g4_printed) in k2)
print('repaired 4p open (direct)', open_direct(g4_repaired, 68), ' is open child of 2p', tuple(g4_repaired) in k2)
k4r = set(open_children(g4_repaired, 68)[0]); k4p = open_children(g4_printed, 68)[0]
print('open children: printed 4p', len(k4p), ' repaired 4p', len(k4r))
print('g8 open (direct)', open_direct(g8, 136), ' g8 is open child of repaired 4p', tuple(g8) in k4r, ' g8 open children', len(open_children(g8, 136)[0]))
