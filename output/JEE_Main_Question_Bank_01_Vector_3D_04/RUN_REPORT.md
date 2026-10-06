# RUN REPORT - JEE_Main_Question_Bank_01_Vector_3D_04

Paper: 9 numerical questions printed as Q61-Q69 (all Vector / 3D). The deck numbers them 1-9 (deck Q1 = printed Q61, ..., deck Q9 = printed Q69).

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **2.11** (19 / 9 questions, 4 marks each). No equivalence-relation adjustment or MCQ floor applied (all numerical).
- Questions per level: Level 0: none | Level 1: 1 (Q9) | Level 2: 6 (Q1, Q2, Q5, Q6, Q7, Q8) | Level 3: 2 (Q3, Q4) | Levels 4 and 5: none.
- All ratings are Medium confidence; JEE Main-style bank, well below the JEE Advanced range.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): JEE Advanced default of 4 for numerical questions (+4 correct, 0 otherwise, stated on the section divider).

## Solutions whose source is corrected or written
No question is `written`. `corrected` (all are gaps/typos; no wrong answer):
- Q1 (printed 61) - typo: "3lambda+1 = 2lambda+2" should be 2 mu + 2. Also added the steps for delta = 7/13 and PB^2 = 36/13. Answer 216 unchanged.
- Q2 (printed 62) - gap: BC^2 = 50, the comparison of the three squares and the answer 54 were not written; the rejection of d = -2/5 (d > 0) was not stated. Added.
- Q6 (printed 66) - gap: "x=5, y=-3, z=2" given with no solving; the cross-product system has rank 2 and needs the dot equation. Added the elimination. Answer 38 unchanged.
- Q7 (printed 67) - gap: mu = 2, lambda = 4 given without working and points M, N not stated. Added elimination and the points M(13,10,-9), N(-8,-2,9). Answer 196 unchanged.
- Q8 (printed 68) - gap: PDF does not note that a = 1 is degenerate (Q = P) so only a = -1 is a genuine right angle; 12a^2 = 12 unaffected.
- Q9 (printed 69) - gap: only the +21 point taken; the other point (-14,-12,-11) at distance 21 is not mentioned and is excluded by the non-negativity condition. Added.
- Q3, Q4, Q5 are `pdf`: working verified (sympy for Q3, Q4, Q6, Q7) and reproduced.

## Answer key
All 9 printed answers (216, 54, 46, 569, 48, 38, 196, 12, 22) were checked by independent computation: none looks wrong.

## Alternates
Alternate solutions given for all 9 questions (Q1-Q9), each verified numerically/symbolically and ending at the same answer. Some are close in spirit to the primary method:
- Q1 (projection of AB on L2), Q2 (Lagrange identity), Q3 (solve for c), Q4 (uniqueness argument avoiding lambda), Q5 (parallel/perpendicular components), Q6 (c = c0 + t s), Q7 (plane through P and L1), Q8 (Pythagoras on QPR) use a clearly different technique.
- Q9 (expand |QA + 21u|^2) is only a variant of the primary method (distance without coordinates of P); the problem has no genuinely different route.

### Questions with NO alternate
- None (see Q9 remark above).

## Useful Result / Pattern
Every one of the 9 questions has a `useful_results` slide.

## make_ppt.py warnings
- None printed. 392 equations converted to native PowerPoint equations; 60 slides. No "could not convert" notes.

## Skipped / assumed / guessed
- Concepts and levels are self-assigned (nearest anchors cited per question in the ratings file).
- Slides were not rendered or checked visually (no soffice rendering in this environment); the PDF was read from page images.
- Marks assumed 4 per question (not printed in the paper).
