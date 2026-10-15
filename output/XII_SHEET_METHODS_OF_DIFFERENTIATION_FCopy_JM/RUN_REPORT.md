# Run report - XII_SHEET_METHODS_OF_DIFFERENTIATION_FCopy_JM (Exercise J-M, 16 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for every question (10 single-correct: Q1, Q2, Q3, Q7-Q11, Q14, Q15; 6 numerical: Q4, Q5, Q6, Q12, Q13, Q16). Stated in the section dividers. Total 64 marks.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.19** (no equivalence-relation or multi-correct adjustments apply).
- Levels: Level 1 = 3 (Q1, Q6, Q8); Level 2 = 7 (Q2, Q3, Q4, Q7, Q10, Q11, Q14); Level 3 = 6 (Q5, Q9, Q12, Q13, Q15, Q16); Levels 0, 4, 5 = none.
- Ratings are my judgement against the anchors (JEE Main-origin questions); confidence Medium except Q1, Q6, Q8, Q14 (High).
- Workbook: `XII_SHEET_METHODS_OF_DIFFERENTIATION_FCopy_JM_difficulty.xlsx` (recalc.py not available, so cached formula values are absent until opened in Excel).

## Solutions corrected (solution_source = corrected)
- **Q1** - PDF applies L'Hospital's rule, which assumes f' is continuous at 2 (not given). Answer 12 unchanged; added a rigour remark, and the alternate (first-principles split) needs only differentiability.
- **Q12** - PDF's last lines read "f'(4)/f'(4) = 124 x 2 = 248"; denominator should be f'(2) and the factor 14 was dropped (14 x 124/7 = 248). Fixed the final step. Answer 248 unchanged.

No question needed `written`.

## Answer key problems
None. All 16 keys match and were verified (sympy / hand): Q1 12, Q2 (B), Q3 (B) -1/2, Q4 40, Q5 17, Q6 7, Q7 (B), Q8 (A), Q9 (A) -15 (explicit f = x^5 - 5x^4 + 60x^2 - 120x + 64 has f(1) = 0), Q10 (D), Q11 (C), Q12 248 (closed form f = (4^x - 2^x)/4), Q13 16, Q14 (D), Q15 (D), Q16 16.

## Gaps in the PDF filled while keeping solution_source = pdf
Q2: added why cot^-1(cot theta) = theta (theta in (0, pi/2)); renamed the PDF's repeated angle to phi. Q3: added the sign analysis for the moduli on x/2 in (pi/4, pi/2) and the range check for cot^-1. Q9: PDF typo "t''(x)" read as f''(x); added that the limit's existence forces f(1) = 0. Q16: split the PDF's compressed second-derivative line into steps (values u = -1, (x - yy')^2 = 1/2).

## Text-layer problems in the PDF
The extracted text lost most maths symbols; all questions and solutions were read from page images (85 dpi). The PDF also prints each question in Hindi; only the English text was used.

## Alternates and results
- Alternate solutions were written for **15 of 16** questions (Q1 first-principles split; Q2 sin(cot^-1 u) = 1/sqrt(1+u^2); Q3 rationalising to (1+|cos x|)/sin x; Q4 Taylor series of y; Q5 x = cosh u; Q6 factor x^n - 1 plus derivative definition; Q7 direct derivative gives dy/dt = -1/2; Q9 operator method (1-D)(1-D^3)^-1; Q10 Euler substitution x = 5e^theta; Q11 row-wise differentiation of the determinant; Q12 solve the functional equation f = k(4^x - 2^x); Q13 series reversion; Q14 implicit differentiation of y ln cos x = -ln sin x; Q15 eliminate t to get (x^2+y^2)^2 = 16xy; Q16 parameter q = x^2 - y^2).
- **No alternate:** Q8 - the inverse-function derivative has one standard route (g'(63) = 1/f'(4)); implicit differentiation of t^3 + t - 5 = x or the mirror-image slope argument is the same computation reworded, so none was invented.
- Weaker alternates (a different organisation rather than a wholly new idea): Q14 (product rule instead of quotient rule), Q6 (factorisation instead of L'Hospital), Q4.
- Every question (all 16) has useful_results (4 bullets each).

## make_ppt.py output
No warnings: 672 equations converted to native PowerPoint equations; 107 slides, 16 questions. No rendering check was possible (no PowerPoint/LibreOffice here).

## Skipped / assumed / guessed
- Concepts and chapter names self-assigned (all Methods of Differentiation; a second concept added where another chapter is involved).
- Q8 (options printed, "Ans. A") is labelled Single Correct; the stem is otherwise numerical-style. Numerical questions labelled "Numerical Type" (JEE Main numerical format).
- recalc.py and slide rendering were skipped (not available).
