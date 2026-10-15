# RUN REPORT - XII_SHEET_AREA_UNDER_CURVE_FCopy_JM

Paper: Area Under Curve sheet, Exercise J-M (33 questions, all JEE Main PYQs 2021-2022). Deck: `XII_SHEET_AREA_UNDER_CURVE_FCopy_JM_Analysis.pptx` (205 slides).

## Difficulty
- Marks-weighted difficulty index: **2.15** (all questions carry equal marks, so it equals the mean level).
- Level 1: 6 questions (Q2, Q4, Q10, Q12, Q14, Q20). Level 2: 16. Level 3: 11 (Q5, Q7, Q13, Q18, Q19, Q21, Q22, Q23, Q29, Q31, Q32). No Level 0, 4 or 5.
- No equivalence-relation adjustment or multi-correct floor applies (no such questions). Ratings: `..._ratings.json`; Excel: `..._difficulty.xlsx`.

## Blueprint and marks
- No blueprint exists for this paper. **Concepts self-assigned (no blueprint) - please review.**
- No marks are printed in the paper. Assumed JEE Advanced defaults: **4 marks for every question**, both Single Correct (Q1-4, 8-9, 12-18, 25-33) and Numerical (Q5-7, 10-11, 19-24). Stated in the section dividers.
- Sections: 7 dividers following the interleaved SCQ / Numerical runs in the paper.

## Solutions whose source is `corrected` (PDF working had an error)
- Q1: PDF wrote the substitution as "x = cos(theta) d(theta)", used 1/4 where 1/8 is needed, and omitted limits; fixed, answer (A) unchanged.
- Q3: PDF's A = (4-sqrt2)log2(e) - 2 log2(e) + 1; the middle term must be -2 ln2. alpha, beta, gamma and the answer were right.
- Q9: PDF integrated the first piece over 0..pi/2 (should be 0..pi/4); later lines use the right limits.
- Q11: PDF antiderivative printed as x^4/2 - x^3 - 12; correct is x^4/2 - x^3 - 6x^2. Answer 114 unchanged.
- Q17: PDF first branch y = 2x - 7/2 for x < -1; correct is y = 2x + 7/2. Answer unchanged.
- Q22: the set A1 as printed (|x| <= y^2, |x| + 2y <= 8) has infinite area (unbounded for y < -2). The PDF silently drew only y >= 0; the solution states this assumption. Answer 6 kept.
- Q31: PDF's normal "y = -(x) - ..." drops the factor 6 in the first term; correct y = -6x + 3 + 54. Answer (C) unchanged.

Steps added without any error in the PDF (source kept `pdf`): Q10 and Q28 (PDF jumps to the answer; evaluation steps added), Q23 (explanation of the factor 3/2), Q27 (PDF solved only the negative-sign case; test of the positive case added).
`written`: none.

## Answer key
No answer key disagrees with the verified answers. Every key was checked by symbolic or numeric computation (sympy). Only Q22 is questionable as a statement (see above).

## Alternates and results
- Alternate solutions for **all 33 questions** (Q1-Q33), each a different method and verified numerically: Archimedes' two-thirds rule, the |a|(b-a)^3/6 formula, horizontal against vertical strips, Simpson's rule, symmetry, inverse-function area identity, parametric/astroid formula, and so on.
- Questions with NO alternate: none.
- Weakest alternates (genuinely different technique, but close in spirit to the main method): Q1 (parts directly in x, with a Simpson check), Q24 (ratio first), Q27 (spotting 728 = 3^6 - 1).
- `useful_results` given for all 33 questions.

## make_ppt.py warnings
- None. It reported 1146 equations converted to native equations, 205 slides, and no "could not convert" notes. Rendering through LibreOffice was skipped (not available in this environment), so slide layout was not inspected visually.

## Skipped / assumed
- Figures in the PDF were read from page images; the Q31 figure (A1 under the curve, A2 to its left) was inspected at high resolution and matches the PDF's solution.
- Levels use the calibrated skill's anchors; most questions are JEE Main routine, hence the low index. Medium-confidence ratings: Q3, 5, 6, 7, 11, 13, 15, 18, 19, 21-23, 29, 31, 32.
