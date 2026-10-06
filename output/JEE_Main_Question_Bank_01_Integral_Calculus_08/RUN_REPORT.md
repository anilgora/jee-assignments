# RUN REPORT - JEE_Main_Question_Bank_01_Integral_Calculus_08

Paper: 20 questions (printed Q141-Q160), deck numbers 1-20. Q1-8 Differential Equations (numerical value), Q9-20 Area Under Curve (single correct, 4 options).

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **2.05** (164 / 80 marks; all questions 4 marks). No equivalence-relation adjustment or MCQ floor applied.
- Questions per level: Level 1: 3 (Q7, Q8, Q11) | Level 2: 13 (Q1, 2, 3, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20) | Level 3: 4 (Q4, Q5, Q6, Q17) | Levels 0, 4, 5: none.
- Lowest-confidence (Medium) ratings: Q2, Q4, Q5, Q6, Q14, Q17.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): +4 for every question (numerical and single-correct), JEE Advanced default, as in run 07; stated on the section dividers.

## Solutions whose source is corrected or written
- Q1 (printed 141) - corrected: the PDF leaves the partial-fraction numerator as "a" (it is 9) and stops at `2(2x+3y)+9|2x+3y-8| = x+c` without applying y(0)=3 or reading off alpha, beta, gamma; completed. Answer 29 unchanged.
- Q6 (printed 146) - corrected: the PDF breaks off after `u.e^{-y} = integral e^{-y}e^{2y}dy`; the integration, c=0 and the evaluation at pi/6 were added. Answer 9 unchanged.
- Q11 (printed 151) - corrected: the integrand line `-x^2/4 - (x-6)/2` should be `-x^2/4 - (x-12)/2` (constant 6, not 3); the PDF's antiderivative already uses 6. The PDF figure also labels (4, 8) instead of (4, 0). Answer 250 unchanged.
- Q12 (printed 152) - corrected: the second antiderivative is printed with `-10x`; it must be `+10x`. Value 50/3 and answer unchanged.
- All other questions are `pdf` (working verified). Small additions without changing the PDF's method: Q4 (L'Hopital derivative spelled out), Q5 (PDF writes Y(x) for Y'(x) in one line), Q9, Q10, Q13, Q15, Q18 (a few intermediate lines expanded, e.g. intersection points, the region's description).

## Answer key
All 20 printed answers were checked (sympy / numerical integration; ODE solutions verified by substitution, Q4 and Q6 also by numerical ODE integration) and are correct. No key errors.
- Note on Q5 (printed 145): the data are slightly inconsistent - the solution y = 2/(3x) + x^2/3 has Y'(1) = 0 although the question says Y'(x) != 0, and the stated area expression is only positive where Y' < 0. The intended (standard) algebra and answer 20 were followed.

## Alternates
Alternate solutions given for **18 of 20 questions** (Q1-15 and Q18-20). Checked analytically and numerically (Q9, Q19, Q18, Q20 values by numerical integration; Q1, Q6 by substituting the curve into the ODE). Closer relatives of the main method (stated honestly): Q3 (definite integral between the two known points instead of a constant C), Q6 (guess of the particular solution of the linear equation, plus verification), Q7 (substitution plus particular solution for the linear equation), Q8 (exact-differential grouping instead of I.F.), Q14 (derives f' = 4af by differentiating the functional equation; later steps as in the main solution), Q15 (direct integration instead of the standard-area formula).

### Questions with NO alternate
- Q16 (printed 156): the area is a single two-piece integral whose outcome is linear in a; any other route (hyperbolic functions, rectangle plus cap) is the same integral reworded, so none was given.
- Q17 (printed 157): a one-variable maximisation of a cubic; no AM-GM, symmetry or geometric shortcut applies, so no genuinely different method exists.

## Useful Result / Pattern
Every one of the 20 questions has a `useful_results` slide (4 bullets each).

## make_ppt.py warnings
None. The build printed no warnings and no "could not convert" notes; 822 equations converted to native PowerPoint equations; 125 slides. Slides were not rendered or opened in PowerPoint here (no soffice rendering in this environment).

## Skipped / assumed / guessed
- Concepts and levels self-assigned; levels are judgement against the calibrated anchors (cited per question in the ratings file). This is a Main-level bank, so levels sit at 1-3.
- Question types "Numerical Type" / "Single Correct Type" taken from the answer format (blank vs four options); marks assumed 4.
- The PDF text layer was garbled, so all pages were read from page images (100 dpi); Q12's sign error was confirmed on a 200 dpi crop.
