# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_01_02

Paper: 20 questions, all Single Correct Type, Algebra. The paper prints them as Q21-Q40 (it continues the previous bank file); they are numbered 1-20 in the deck (deck Q n = printed Q n+20). 121 slides, 815 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.15** (172 / 80 marks; 4 marks each). No equivalence-relation adjustment and no MCQ floor (all single-correct).
- Questions per level: Level 1: 2 (Q5, Q19) | Level 2: 13 | Level 3: 5 (Q7, Q8, Q9, Q11, Q20) | other levels: none.
- Medium confidence: Q1, Q4, Q7, Q8, Q9, Q11, Q16, Q20. The rest High.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper): +4 for single-correct questions (JEE Advanced default per the run instructions), 0 otherwise; stated on the section divider.

## Solutions whose source is corrected or written
- Q5 (printed 25) - corrected: the PDF gives only the sum of the new roots (-8) and writes x^2+8x+12=0 without the product; the product 12 was added. Answer (B) unchanged.
- Q12 (printed 32) - corrected: PDF writes last term as a+(2n+1)d; it is a+(2n-1)d (next line already uses 2nd-d). It also states "integral terms = 4" without showing a or the terms; a = 3/2 and the terms were added. Answer (B) unchanged.
- Q13 (printed 33) - corrected: PDF line "a^2+14a+25-120<0" is a wrong expansion; correct is a^2-10a+25-120+24a = a^2+14a-95. Answer (C) unchanged.
- Q16 (printed 36) - corrected: PDF treats (a-1)A as 3A (gets 2^10 3^6); with a = 3 it is 2A, giving 2^16, so m=16, n=0. m+n = 16 either way, answer (C) unchanged.
- Q20 (printed 40) - corrected (gap): the PDF asserts |A-2A^T| = 4 with confusing P/Q naming; |M|^2 = 16 only gives |N| = +-4, and alpha > 0 is needed to exclude -4. Argument added. Answer (B) unchanged.
- No question was `written`. The other 15 are source pdf (harmless typos only: Q1 "A22 A22" in the C22 line; Q3 reuses "a" for the first term, notation tidied to 18-d = 10; Q8/Q17 PDF uses n for k).

## Answer key
All 20 printed answers verified with sympy / numerics (cofactor identity, A^50-type powers, telescoping sums for 20 and 10 terms, determinant identities for the x=0 and general-x cases, adj/determinant powers 2^16, alpha = 1, B sum = -88, etc.). No answer key is wrong.

## Alternates
Alternates given for 18 of 20 questions (all except Q14 and Q20).
Honest notes on strength: Q7 and Q9 (guess the closed form of S_n from partial sums and check) and Q19 (characteristic-polynomial route, longer than the direct determinant) are lighter variants, not radically different; Q16's alternate (adj M = |M| M^-1) is a different bookkeeping of the same facts. The others use clearly different ideas (nilpotent powers Q4, root substitution Q5, rank-one A = uu^T Q6, Cayley-Hamilton Q8, normalising the GP Q10, matrix determinant lemma Q11 and Q15, parameter separation + AM-GM Q13, difference table / hockey-stick Q18, ratio trick Q12 and Q17, middle-term view Q2, option test Q3, cofactor theorem Q1).
Questions with NO alternate:
- Q14 - the only way to evaluate the ratios is the three-term recurrence from the root equation; "multiply by alpha^(n-2)" is the recurrence's own derivation, so no genuinely different method exists.
- Q20 - the antisymmetry |N| = -|M| (N^T = -M, odd order) is the whole idea; computing both determinants directly is the same route reworded, so none given.

## Useful Result / Pattern
All 20 questions have a useful_results slide (3 bullets each); formulas spot-checked numerically (determinant lemma, power-sum recurrence, Newton/hockey-stick sum for N=3, S_n closed forms for n up to 11, adj(2M)=4adj(M), charpoly of A, range of the parameter function).

## make_ppt.py warnings
None printed (only the note "815 converted to native PowerPoint equations"). No "could not convert" messages. Slides were not rendered (no soffice/thumbnails in this environment).

## Skipped / assumed / guessed
- Concepts and levels self-assigned; nearest anchors cited in the ratings file are approximate (closest chapters in anchors.md).
- Page text extracted with pdftotext; the garbled maths was checked against page images (all 16 pages viewed).
- Excel report built with build_report.py; recalc step skipped (no /mnt/skills), so formula cells have no cached values.
- The paper has no title in its text layer for this part; the deck title is "JEE Main Question Bank 02 Algebra 01 (Paper 02)".
