# RUN REPORT - JEE_Main_Question_Bank_01_Differential_Calculus_02

Paper: 20 questions (printed Q21-Q40, numbered 1-20 in the deck). Content is Sets, Relations and Functions (the page header says "Differential Calculus").

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed in the paper, so JEE Advanced defaults were used: 4 marks for every question (Single Correct Q1-4, Q16-20; Numerical Q5-15). This is stated in the section dividers. Printed Q23 shows a blank plus options (A)-(D), so it is treated as Single Correct.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.18** (all questions 4 marks).
- Levels (adjusted): 1 : 2 questions (Q1, Q18); 1.5 : 1 (Q3); 2 : 10 (Q2, Q5, Q7, Q12, Q14, Q15, Q16, Q17, Q19, Q20); 2.5 : 2 (Q4, Q13); 3 : 5 (Q6, Q8, Q9, Q10, Q11).
- Equivalence-relation adjustment (+0.5): Q3, Q4, Q13. No multi-correct questions, so the 2.5 floor is not used.
- Low-confidence level: Q10.

## Solutions that are `corrected` or `written` (no question is `written`)
- Q7 (printed 27): the PDF's R2 and R3 omit (1,3), so they are not transitive; correct sets include (1,3). Count 3 is right. Added why other additions are excluded.
- Q8 (printed 28): the PDF gives x = 45 from its first diagram, then jumps to 30 without saying why (30 - x cannot be negative). It also labels the extremes the wrong way round (x = 30 = m, x = 15 = n). Correct: least = 15, most = 30; sum 45 unchanged.
- Q10 (printed 30): the PDF only states x = 45, y = 1. There is no proof that this is the only solution (needed because the sum is over the whole set). Added a mod-8 argument and the y = 2 check. The page image shows 2^y (the text layer shows "2y").
- Q12 (printed 32): the PDF writes "(n = 5)" but the set has 4 elements; its arithmetic (1024 - 64) is the n = 4 value. Slip only.
- Q13 (printed 33): the PDF's symmetric additions include (3,1); the reverse of (2,3) is (3,2). Corrected to (2,1), (3,2), (4,1). Counts are right.

## Answer key problems
- Q6 (printed 26): key prints 5, but the PDF's own working ends with 6 and brute force gives 6. Answer given: 6.
- Q11 (printed 31): key prints 11, with a note "NTA (10)"; the PDF working and brute force give 10. Answer given: 10.
- All other keys agree with my verification (brute-force checks for Q6, Q7, Q8, Q9, Q11; algebra for the rest).

## Alternates and results
- Alternate solutions given for 19 of 20 questions (all except Q14).
- Q14: no alternate. The only count is 33 pairs doubled by taking reverses; any other route is the same computation reworded.
- Useful Result / Pattern given for all 20 questions.
- Alternates for Q8 and Q15 are the weaker "different viewpoint" kind (formula bounds vs Venn regions; counting by divisors vs multiples); kept because they are valid and verified, but they are modest.

## make_ppt.py output
- "Equations: 695 converted to native PowerPoint equations." No warnings or "could not convert" notes were printed, so nothing needed fixing.

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per the run rules); slide fit was not checked visually.
- Levels are my own ratings from the calibrated rubric, with anchors from relation-counting questions (2025-P1-Q8, 2026-P1-Q9); the paper is JEE Main level, so most are low on the Advanced scale.
- Chapter name "Sets, Relations and Functions" used for the ratings file; the paper's header says Differential Calculus.
