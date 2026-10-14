# Run report - SHEET_FUNCTION_FCopy_JM

Paper: Exercise J-M (Functions), 47 JEE Main questions (Jan 2023, Apr 2023, Jan 2024, Apr 2024), numbered 1-47 as in the PDF. The PDF has answers and solutions (with Hindi text, ignored). Date of run: 2026-10-14.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed; stated in the section dividers): JEE Advanced defaults, 4 marks for every question (single-correct Q1-12, 18-22, 28-34, 36-43 and numerical Q13-17, 23-27, 35, 44-47). Total 188. Question types follow the paper: questions with options A-D are single-correct (including Q4, which prints a blank but has options), questions without options are numerical.

## Difficulty
Marks-weighted difficulty index (adjusted): **1.87** (far below the official JEE Advanced range 2.6-3.2; these are JEE Main questions, no expected distribution).
Level counts: L0 = 0, L1 = 11 (Q2, 5, 7, 21, 28, 32, 34, 39, 43, 46, 47), L2 = 32, L3 = 3 (Q24, 41, 45), L4 = 1 (Q13), L5 = 0.
No equivalence-relation adjustment and no MCQ floor applied. Medium-confidence ratings: Q4, 6, 8, 10, 11, 12, 13, 17, 19, 22, 24, 27, 29, 30, 33, 37, 38, 41, 44, 45.

## Solutions whose solution_source is "corrected" (10)
- Q10: not wrong but incomplete. The PDF gives four formulas and a graph; the interval of each piece and the overlap argument for the union were added.
- Q16: incomplete. The PDF jumps from f^3 to f^5; the f^4 step was added.
- Q23: the PDF prints "Ans. 384" and "Ans. Matrix 180". The working gives 180, which is correct; 384 is a wrong key line.
- Q24: the PDF's argument for m = 0 is only a sketch (it checks x = 5, 6). A full proof was added; m = 0, n = 3, answer 9 unchanged.
- Q27: incomplete. The PDF derives the closed form and then states the answer without evaluating 2f(2)+f'(2); the evaluation (121857 = 119*2^10+1) was added.
- Q29: incomplete. The PDF never shows that the new denominator 2|x|+2x+7 is never zero (g(x) never equals -1/2); added.
- Q38: the PDF concludes "into" from the sign change of f'; that shows many-one only. The range [-2, 8/5] was added. Also a denominator typo (x^2-4x+19) fixed.
- Q40: the PDF labels "f(3) = [log2(25+25)] = 5" (that is f(5)) and never computes f(3) = 3; corrected. The range and answer (120) are unchanged.
- Q41: the PDF's graph of g misses the point g(0) = -a (it shows a hollow point at the origin). Included g(0) = -a; the conclusion is unchanged.
- Q45: the PDF writes the bound "1/3 >= [a] >= -3/5"; the correct bound is -3/5 < [a] <= 1/5. Conclusion unchanged.

## Solutions with solution_source "written" (0)
None; the PDF has a solution for every question. Small additions inside "pdf" solutions: Q1 (check of x = 1 and why (C) fails), Q17 (why f(1) = 1 and why 3x3 = 9 is the only real condition), Q20 (A^2+BC > 0), Q30 (values on each piece), Q22 (explicit check of the identity and the range-of-g remark), Q8, Q9, Q31. Plain typos in the PDF reproduced with the right expression: Q11 ([x^2-x+2] where [x^2-x+1] is meant), Q19 ("x in I" where x not in I is meant), Q33 ("f(x) is neither" where gof is meant), Q2 (uses k for n).

## Answer key / question problems
- Q23: the key line "384" is wrong; the correct answer is 180 (re-derived two ways, and by the symmetry method).
- Q22: the key says "Bonus"; this is right since f is determined only on [1, infinity) (range of g). Kept as "Bonus (formally 5)".
- Every other answer was re-derived, and checked by computation for Q13 (3240 by brute force), Q24, Q27, Q38, Q40, Q41.

## Alternate solutions
Alternates (a genuinely different technique) were written for 29 of 47 questions: Q1, 2, 3, 4, 6, 8, 9, 12, 13, 16, 19, 20, 23, 24, 25, 26, 27, 29, 30, 32, 33, 35, 37, 38, 41, 42, 43, 44, 45. Each was verified by hand (several also numerically) against the answer.
Questions with NO alternate (18), and why:
- Q5: the only route is subtracting the two conditions; trying values of n is the same step.
- Q7, Q21, Q34, Q39: single-step domain or range conditions; no different route exists.
- Q10: piecewise range on unit intervals is the only route.
- Q11: "min at the vertex" and "t+[t] is increasing" are the same argument.
- Q14: matching a(x^b+c)-3 with 2x^3+7 is the only route.
- Q15: telescoping of the series is the only route.
- Q17: the count of free elements is the same as the main solution.
- Q18: both sets reduce to x < -1; the checks are the same computation.
- Q22: it is one substitution and a remark on the range of g.
- Q28: two counterexamples; no second method.
- Q31: intersection of two sign charts; no different method.
- Q36: ordered pairs and one-one assignment of the rest is the only route.
- Q40: five evaluations and a factorial.
- Q46: arithmetic series bound; "mean of the AP" is the same computation.
- Q47: list solutions and count bijections.

## Useful Result / Pattern
Every question (1-47) has useful_results (3 general, conditioned statements each; formulas spot-checked numerically, e.g. Q9, Q27, Q42, Q44).

## make_ppt.py warnings
None printed: 1430 equations converted to native PowerPoint equations, 262 slides, 47 questions. No equation was left as LaTeX text.

## Skipped / assumed / guessed
- No rendering or thumbnail check (no soffice in this environment); the deck was built but not viewed. The difficulty xlsx was not recalculated (recalc.py not available).
- Levels are my calibrated estimates against the user's anchors; the Function-chapter anchors are Advanced-level, so JEE Main questions were placed below them. Medium-confidence levels are listed above.
- Concepts are self-assigned. The chapter is "Function" for every question in the ratings sheet although a few questions draw on other chapters (e.g. Q31, Q42 conics, Q35 counting).
- Figures in the PDF (graphs in Q10, Q30, Q33, Q37, Q41) are described in words, not redrawn.
- Q22's displayed answer is "Bonus (formally (A) 5, ...)", not a single option.
