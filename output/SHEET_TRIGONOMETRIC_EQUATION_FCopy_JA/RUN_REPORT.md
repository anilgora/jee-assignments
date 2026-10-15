# Run report - SHEET_TRIGONOMETRIC_EQUATION_FCopy_JA (Exercise J-A, 6 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for the single-correct questions (Q1, Q3), the integer question (Q2) and the numerical question (Q4); 3 marks for the matching questions (Q5, Q6). Stated in the section dividers. Total 22 marks.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.95** (no equivalence-relation or multi-correct adjustments apply).
- Levels: Level 2 = 1 (Q2), Level 3 = 4 (Q1, Q3, Q4, Q5), Level 4 = 1 (Q6); Levels 0, 1, 5 = none.
- Q6 is the official JEE Advanced 2026 P1 Q14, already an anchor rated 4 by the user; that level was reused. Medium-confidence ratings: Q1, Q3, Q4, Q5.
- Workbook: `SHEET_TRIGONOMETRIC_EQUATION_FCopy_JA_difficulty.xlsx` (recalc.py not available, so cached formula values are absent until opened in Excel).

## Solutions corrected (solution_source = corrected)
- **Q1** - the PDF writes sin x(1 + 2cos x - 3 + 4sin^2 x) = 3, but 2 sin2x = 4 sin x cos x, so the middle term is 4cos x. Its following lines (2 - 4cos^2x + 2cos x; 9/4 - (2cos x - 1/2)^2; "L.H.S. <= 9/4") are therefore wrong. Correct: 2 - 4cos^2x + 4cos x = 3 - (2cos x - 1)^2 <= 3 < 3/sin x unless sin x = 1, where the left side is 2. Answer (D) unchanged.

No question needed `written`.

## Gaps in the PDF filled while keeping solution_source = pdf
- Q5: the PDF states only the element counts ("x has 2 elements"); the elements in each interval were listed to show the count (endpoint -5pi/18 in (II); 13pi/12 < 6pi/5 in (III)).
- Q6 (R): the PDF does not say that cos x = (-1-sqrt17)/4 < -1 is rejected; added. Q3: the check that no root equals 0, +-pi/2 was made explicit. Q2, Q4: PDF working correct as is.

## Answer key
No answer key looks wrong. All answers were checked numerically (sign-change scans / direct substitution): Q1 max of the left side on (0,pi) is about 2.73 < 3; Q2 all eight roots; Q3 roots -5pi/9, -pi/3, pi/9, 7pi/9; Q4 root-sum identity; Q5 counts 2, 2, 6, 4; Q6 counts 5, 3, 2, 4.

## Text-layer problems in the PDF
The extracted text lost most maths symbols; all questions and solutions were read from page images (110 dpi).

## Alternates and results
- Alternate solutions were written for **all 6** questions (Q1 bound via 2 sin x(2cos x - cos 2x); Q2 reduction to cos 4x = 0; Q3 cos A - cos B factorisation with AP-sum; Q4 R cos(x - phi) symmetry; Q5 unit-circle chord / scaled-interval counting; Q6 elimination with substitution and an evenness/parity argument).
- **No alternate:** none. Weaker alternates (organisation rather than a wholly new idea): Q2 (single-function cos 4x reduction, close to the PDF's route) and Q3 (product-form of the same cos A = cos B step, with a new AP-sum shortcut). Q6's alternate is an elimination argument, not a full independent count.
- Every question has useful_results (4-5 bullets).

## make_ppt.py output
No warnings: 347 equations converted to native PowerPoint equations; 54 slides, 6 questions. No rendering check was possible (no PowerPoint/LibreOffice here).

## Skipped / assumed / guessed
- Concepts and chapter names self-assigned (all Trigonometric Equation); ratings are my judgement against the anchors.
- Q2 labelled "Integer Type (0 to 9)" (answer 8); Q4 "Numerical Type".
- recalc.py and slide rendering were skipped (not available).
