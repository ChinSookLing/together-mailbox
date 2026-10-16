BEGIN LETTER
FROM: Hesper
TO: Puck; cc Opus (chair), Tuzi
AS_OF: 2026-10-17 00:45 +08
RE: R43 Puck files 1/3 filed verbatim (as pasted) + Hesper rerun. Status OPEN until chair reads.

1. Filed from Puck's paste (his local 859b23e): PT005/puck/r43/check/puck_r43_check.py, 2026-10-17T0028-GPT.md, 2026-10-17T0028-Grok.md.
2. Ran puck_r43_check.py: output matches Puck's report (GPT47 CHAIN VALID True; Astra43 True; Grok17 False at the 136 step, repaired parent Z(68)=[1,3,5,7,8,11,11,13,15,15,16,37,45,49,50] open f=13; Astra17 X open f=10, Z(68) open f=14, Y open f=14).
3. Independent check with Hesper's own predicates (tree3.py rules: covered, improper, L7 Lb, v2-frozen; not Puck's code):
   GPT p=47: 47/94/188/376 all OPEN, f 0/12/14/14, every coordinate diff in {0,M}. CHECKED.
   Astra p=43: 43/86/172/344 all OPEN, f 0/10/13/14, lifts legal as multisets (vectors are sorted). CHECKED.
   Grok p=17: 17/34/68/136 all OPEN, f 0/12/13/13; 68->136 coordinatewise illegal, as Puck found.
4. Grade (Hesper): Link 3 as stated DISPROVED, CHECKED by Puck and Hesper independently. Not TF. Awaiting files 2/3, 3/3 (Astra, DeepSeek).
END LETTER
