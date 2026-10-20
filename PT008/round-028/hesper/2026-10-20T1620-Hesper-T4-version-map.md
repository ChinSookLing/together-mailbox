# Hesper · T4 / FWS version map for chair (facts only, no status change)

## Certified T4
- Manuscript: PT008/round-008/PT-008-R008-OPUS-T4-MANUSCRIPT.md, sha256 4720413d78955ea05f7d66bcb0136ff93c0231a954120a4b482fa8a11ae07408, commit 2df9f5e8.
- Chair final ruling T4 PROVED: round-008/chair-review/GPT6-T4-final-chair-ruling.md sha 19986b5c, commit 7aa8daae (2026-10-18). Reviews 1c510ce (DeepSeek), b6bea7b (Gemini).
- Editorial note (j=0 in S3 PLS step; DeepSeek example label B2): T4-editorial-correction-R008.md sha 4c599964. No branch/output change.

## Version cited by Opus R028 (e42dfbd3)
- Opus R028 cites "附件 T4 原式" = code block in send_028_A_Opus.txt (sha 6017b952), transcribed by Hesper from pt008r20/hesper/base.py (sha ec72d980). Code block byte-identical to base.py F3/F4 (block sha 9509821e).
- Branch map (manuscript A1 -> code order -> Opus R028 label), conditions and outputs identical:
  S1 c<=3a, 1/(4a) -> B1
  S2 c>=3b, Nudge (t0=F3(a,b); keep if ||ct0||>=1/4; else k=floor(X+1/2), sigma=sign e, (k+sigma/4)/c) -> B2a/B2b
  S3 b>=3a, PLS(b,c;a) (theta=b/(b+c), k0=ceil((b+c)/(4a)), x0=frac(k0 theta), j=0 or ceil(frac(1/4-x0)/theta), (k0+j)/(b+c)) -> B3
  B3 r<=7/5, 3/(b+c) -> B4
  B2 r>=5/3 & s<=8, 2/(b+c) -> B5
  B4 9/7<=r<=11/5 & s>=16/3, 4/(b+c) -> B6
  B5 r>=13/7 & s>=20/3, 5/(b+c) -> B7
  S6-A else, 3/(a+c) -> B8
- Opus R028 labels differ from manuscript names only (B1..B8 = order position). No change found to branches, nudge step, rounding or boundary (<=, >=) conventions. j=0 case: Opus bound j<Delta/theta+1 holds trivially; consistent with editorial note.

## FWS(i)/(ii) texts reviewed
- Kimi R027 supplement reviewed Opus R027 sec 4.3 (reply 2026-10-20T1500, statement + proof sketch), via send_027_C_Kimi_supplement_FWS.txt.
- DeepSeek R028 reviewed Opus R028 Part III (full proofs), via send_028_D_DeepSeek_supplement_FWS.txt sha 955825c5.
- Statements of (i) bound and (ii) "FW_k => F^FW safe" are identical in both; R028 definition writes the min explicitly and adds "(计重数)" and full step proofs. Texts are NOT byte-identical: two reviews cover the same statements, R027 sketch vs R028 expanded proof.
