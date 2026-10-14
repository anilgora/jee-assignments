# Run report - SHEET_METHODS_OF_DIFFERENTIATION_FCopy_JM

Paper: Exercise J-M (Methods of Differentiation), 25 JEE Main questions (2023-2024 shifts) with PDF solutions. Date of run: 2026-10-14. Deck numbering = printed numbering (Q1-25).

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed; stated in the section dividers): single-correct 4 marks (Q1-5, 7-14, 17-24), numerical-value questions 4 marks (Q6, 15, 16, 25). Total 100. Q6, 15, 16, 25 are numerical (no options); all others are single correct.

## Difficulty
Marks-weighted difficulty index (adjusted): **1.92** (chapter sheet of JEE Main questions, so far below the official JEE Advanced range 2.6-3.2; no expected distribution).
Levels: L0 = 0; L1 = 7 (Q5, 7, 10, 17, 18, 22, 23); L2 = 13 (Q1, 2, 4, 6, 8, 9, 11, 12, 13, 15, 16, 24, 25); L3 = 5 (Q3, 14, 19, 20, 21); L4 = 0; L5 = 0.
No equivalence-relation adjustment and no MCQ floor applied. Medium-confidence: Q3, 8, 12, 14, 16, 19, 21, 24, 25. Low confidence: Q20 (flawed question).

## Solutions with solution_source "corrected" (4)
- Q3: the PDF solved sin4t = -sqrt3/2 with the general solution for +sqrt3/2 (roots pi/12, pi/6, ...; sum 3pi/2; beta = 3pi/8) and typed sin^4(3x+t) for sin^4(3pi+t). Correct roots in [0,pi]: pi/3, 5pi/12, 5pi/6, 11pi/12 (sum 5pi/2, beta = 5pi/8). cos4beta = 0 in both cases, so f(beta) = 5/4 and the answer (D) is unchanged.
- Q12: the PDF's three derivative-determinants at x = 0 have wrong entries (e.g. column 3 and column 2 of D2); each still has a zero column, so f'(0) = 0 and answer (C) hold. Rewritten column by column.
- Q20: the PDF itself notes a conceptual mistake in the question. The expression equals a^2 F(1/a) with F(0+) = 1, so the printed limit diverges to +infinity; the key (A) 5/2 + pi/8 equals F'(1). Key kept as the intended answer, and the caveat added to the solution.
- Q24: PDF typos: (1-x)^2 y'' for (1-x^2) y'' and e^{sin^-1 x} for e^{3 sin^-1 x} in the last lines; fixed. Result 9e^{pi/2} unchanged.

## Solutions with solution_source "written" (0)
None. Small additions inside "pdf" solutions: Q2 (the intermediate values y'(-1) = 16 and y''(-1) = -480 that the PDF skips), Q8 (the identity used to simplify the quotient-rule numerator), Q19 (final value step), Q21 (the f''(0) analysis for options C and D, which the PDF omits). Obvious typos silently cleaned: Q1 (f(0) typed without sign), Q4 (messy derivative layout), Q5 (bracket in the last line), Q13 (x^2-x for x^2-2 in one row), Q17 (f(0)=2 line).

## Answer key / question problems
- Q20 (JEE Main April 2024): flawed question, see above. The key (A) is NTA's.
- All other answers were re-derived and checked symbolically/numerically with sympy (Q1-19, 21-25); the PDF keys are correct.

## Alternate solutions
Alternates (genuinely different technique, each verified against the answer) were written for 19 of 25 questions: Q2-13, 16, 19, 21-25.
Questions with NO alternate (6), and why:
- Q1 and Q15: the only route is differentiating and solving a 2x2 linear system for f'(1), f''(2); writing a general cubic and matching coefficients is the same system.
- Q14: continuity plus log differentiation at x = 1 is the whole question; quotient-rule variants are the same computation.
- Q17 and Q18: the inverse-function rule g'(f(x)) = 1/f'(x) at the obvious root is the only method.
- Q20: flawed question, no meaningful alternative.

## Useful Result / Pattern
Every question (1-25) has useful_results (2-3 general, conditioned statements each; formulas were spot-checked numerically, e.g. Q2, Q9, Q16, Q21, Q24, Q25).

## make_ppt.py warnings
None printed: 880 equations converted to native PowerPoint equations, 145 slides, 25 questions. No "could not convert" notes.

## Skipped / assumed
- Rendering and thumbnails were skipped (no soffice/mnt skills in this environment); the deck was not inspected visually.
- Levels are my own ratings from the calibrated rubric; Q14, 19, 20, 21 are the least certain (L2 vs L3).
- Concepts and marks self-assigned as stated above.
