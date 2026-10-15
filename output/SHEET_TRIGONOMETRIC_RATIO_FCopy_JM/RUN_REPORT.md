# Run report - SHEET_TRIGONOMETRIC_RATIO_FCopy_JM (Exercise J-M, 11 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for every question (Q1-3, Q6-10 single correct; Q4, Q5, Q11 numerical). Stated in the section dividers. Total 44 marks.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.45** (16/11; all questions 4 marks; no equivalence-relation adjustment, no multi-correct floor).
- Levels: Level 0 = 1 (Q8); Level 1 = 4 (Q1, Q3, Q6, Q9); Level 2 = 6 (Q2, Q4, Q5, Q7, Q10, Q11); Levels 3, 4, 5 = none. These are JEE Main questions, so the index is well below the Advanced range. All ratings Medium confidence.
- Workbook: `SHEET_TRIGONOMETRIC_RATIO_FCopy_JM_difficulty.xlsx` (recalc.py not available; cached values appear when opened in Excel).

## Solutions corrected / written
- **Q5 (corrected)** - the PDF ends with "x = 60 deg, y = 30 deg, x/y = 2", but x = tan(theta1) = sqrt3 gives theta1 = 60 deg and theta2/theta1 = 1/2, not the largest; the largest ratio (2) needs theta1 = 30 deg (as in the PDF's own figure). The PDF also never uses the given area to find the scale a = 3 - sqrt3 nor computes the perimeter (a(3 + sqrt3) = 6). Both added; answer 6 unchanged.
- No question needed `written`.
- Q6 (kept as pdf, remark added): the printed first line shows "sin alpha - beta" (missing bracket) - typesetting only. The question itself is vacuous: for alpha, beta in (0, pi/2) both tangents are positive, so tan(alpha) = -5 tan(beta) is impossible; k = -5 is the formal (intended) result. A remark bullet says this.
- Q10 (kept as pdf): the PDF's list of six angles is printed in a shorthand (pi/9, pi/2+pi/18, ...) and its sum line is compressed; I spelled out the six values pi/9, 5pi/9, 7pi/9, 11pi/9, 13pi/9, 17pi/9 (sum 6pi) - same working, clearer notation.
- Q7, Q4, Q9 (kept as pdf): small added justification bullet(s) (A+B in (0,pi) so A+B = C; values of sin18, cos36 quoted).

## Answer key
All eleven keys (B, D, D, 4, 6, C, D, C, A, D, 96) agree with numerical checks in Python (direct evaluation of each expression; Q10 by brute-force scan; Q11 by scanning f). No key is wrong. Only caveat: Q6's premise is inconsistent (see above), key -5 is the formal answer.

## Alternates and results
- Alternates for **Q1-Q7, Q9, Q10, Q11** (10 questions): Q1 explicit tan15 = 2 - sqrt3; Q2 pairing 1+2cos2x with surd values; Q3 roots-of-unity / geometric sum; Q4 1/sin18 - 1/sin54 = 2 by sum-to-product; Q5 tan+cot = 2/sin2theta; Q6 divide by cos(alpha)cos(beta); Q7 test value x = 1; Q9 use cos36 +- sin18; Q10 symmetry theta -> 2pi - theta; Q11 f-1 and 3-f separately.
- **No alternate: Q8.** It is a direct evaluation from a 3-4-5 triangle; any other method (e.g. via sec^2) is the same computation reworded.
- Honest caveat: Q6, Q9 and Q1 alternates are mild variants (different technique but short); all verified numerically.
- Every question (1-11) has `useful_results`.

## make_ppt.py warnings
- None. Printed only "450 converted to native PowerPoint equations" and "Saved ... (73 slides, 11 questions)". No "could not convert" messages.

## Skipped / assumed / guessed
- Only the English text was used (Hindi text ignored). Q5's figure is described in words in the question text since the figure is not reproduced.
- No visual rendering check (no soffice here); layout not inspected.
- Chapter for the ratings is "Trigonometric Ratio"; nearest anchors for Q3, Q5, Q6, Q8, Q9 are loose (few trig anchors at levels 0-1).
