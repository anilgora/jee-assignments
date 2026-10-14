# Run report - SHEET_ITF_FCopy_JM

Paper: Exercise J-M (Inverse Trigonometric Functions), 25 JEE Main questions (Q1-25, numbered as in the PDF). The PDF has answers and solutions. Date of run: 2026-10-14.

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): 4 marks for every question (single correct, one-or-more correct and numerical), all stated in the section dividers. Types taken from the paper: Q3 one-or-more correct (key A, B); Q8, 12, 13, 14, 15, 24, 25 numerical; the rest single correct.

## Difficulty
Marks-weighted difficulty index (adjusted): **1.96** (well below the official JEE Advanced range 2.6-3.2; this is a JEE Main chapter sheet, so that is expected).
Level counts: L0 = 0, L1 = 7 (Q1, 10, 11, 16, 18, 20, 25), L2 = 12 (Q2, 3, 5, 6, 12, 13, 14, 15, 17, 21, 23, 24), L3 = 6 (Q4, 7, 8, 9, 19, 22), L4 = 0, L5 = 0.
No equivalence-relation adjustment and no MCQ floor applied (Q3 is one-or-more-correct but single-concept). Low confidence: Q9 (flawed question). The workbook was not recalculated (no recalc.py); the index was computed by hand.

## Solutions whose solution_source is "corrected" (8)
- Q3: PDF labels the two matching options "Option 3" and "Option 1" (numbering of the original paper); in this paper's order they are (A) and (B). Working and answer (A, B) unchanged.
- Q4: PDF jumps to x = 3 without the reason; added that (x-3)^2+1 >= 1 must equal 1 for sin^-1 and cos^-1 to exist. Answer pi/12 unchanged.
- Q5: **PDF's answer key (C) is wrong.** The PDF's own working ends with the empty set and sum 0, which is option (A). Checked numerically: the left side never exceeds 2pi/3 on [-1/2, 1/2], so S is empty. Correct answer (A) 0.
- Q7: PDF writes the parabola as "x^2+x+y = f(x)"; correct is y = x^2+x. Rest unchanged; answer (C).
- Q8: PDF only lists the case results; the intermediate quadratics and root checks were written out. Answer 2 unchanged.
- Q16: PDF writes x = (-3 +- sqrt17)/8; correct denominator is 4. Count of positive roots (1) unchanged.
- Q19: added the justification that sin A, sin B, sin C are proportional to the sides of a triangle (so the expression is cos C). Answer unchanged.
- Q22: PDF writes cos^-1(xy - sqrt..sqrt..) = pi/2 + alpha, true only when pi/2+alpha <= pi; replaced by taking the cosine of both sides, and the attainment of the minimum (x = y = 0) was added. Answer 0 unchanged.

## Solutions with solution_source "written" (1)
- Q9: the PDF has no answer (key blank) and the solution stops after "Range g(x) is domain of f(x)". Full solution written.

## Answer key / question problems
- Q5: key (C) wrong, correct (A) (see above).
- Q9: **question looks flawed.** Exact domain is D = [3^(-23/6), x0] with x0 ~ 0.03663 (root of x = 3^(-3-7.5x^2)), a closed interval, so the range of g is not an open interval (alpha, beta); the exact value alpha^2 + 5/beta ~ 136.50 matches no option (135 and 136 are each 0.5 away). Answer given as (D) 135, obtained by taking the upper end as 1/27. Please review.
- Q14 and Q15: the PDF key shows "D" and "B" (option letters left over from the original paper) for numerical questions. Values 4 and 2 were derived and checked numerically.
- All other answers re-derived and checked numerically (domain endpoints scanned on a fine grid, equation roots, identities).

## Alternate solutions
Alternates (a genuinely different technique) were written for 21 of 25 questions: Q1-8, Q10-17, Q19, Q21-24. Each was checked against the answer by hand or numerically.
Questions with NO alternate (4), and why:
- Q9: every route is the same chain of domain inequalities (base, positivity of the quotient, |log| <= 1); no different method exists, and the question is flawed anyway.
- Q18: two direct domain conditions; there is no second method beyond reading the same inequalities.
- Q20: the only method is reducing 5 radians into the principal ranges; a graph reading is the same step.
- Q25: the only method is sin^-1 x + cos^-1 x = pi/2 (the range argument is the same step reworded).
Borderline alternates (different viewpoint, not very different arithmetic): Q1 (common factor instead of squaring), Q3 and Q14 and Q24 (complex-number view of the same telescoping/addition), Q10 (monotone composition); please judge.

## Useful Result / Pattern
All 25 questions have useful_results (2-4 bullets each).

## make_ppt.py warnings
- "Q20: only 3 solution bullets" - the PDF's working for Q20 is three steps (reduce both values, then add); it is complete, so no change. No "could not convert" warnings; 905 equations converted.

## Skipped / assumed / guessed
- Concepts self-assigned (no blueprint); marks assumed 4 each.
- No recalc.py, thumbnails or rendering done (not available); the deck was not opened in PowerPoint here.
- Q9's answer is a best reading of a flawed question (see above).
