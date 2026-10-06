# RUN REPORT - JEE_Main_Question_Bank_01_Trigonometry_01

Paper: 20 questions (printed 1-20), Trigonometry (ratios and equations); 18 single-correct, 2 numerical-value (Q9, Q10). 127 slides.

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **2.05** (164 / 80 marks; every question 4 marks). No equivalence-relation adjustment or MCQ floor applied (no multi-correct questions).
- Questions per level: Level 1: 2 (Q4, Q11) | Level 2: 15 (Q1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 15, 17, 19, 20) | Level 3: 3 (Q14, Q16, Q18) | Levels 0, 4, 5: none.
- Medium-confidence ratings: all except Q3, Q4, Q11, Q15, Q17 (High). This is a Main-level bank, so levels sit at 1-3.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): +4 for single-correct and for numerical-value questions (JEE Advanced default); stated on the section dividers.

## Solutions whose source is corrected or written
- Q1 - corrected (gap): the PDF gives only a sketch of the two graphs, no count. Written out the branch-by-branch count including the two partial end branches. Answer 5 unchanged.
- Q7 - corrected (presentation): the PDF's list of zeros of cos3t and the offsets of +-pi/18 is garbled (one entry printed pi/16 instead of pi/18). Wrote the six solutions of cos3t = 1/2 directly. Answer 6pi unchanged.
- Q8 - corrected (gap): PDF concludes A+B = C from tan(A+B) = tan C without showing the angles lie in the same interval. Added tanA tanB < 1 so A+B < pi/2. Answer unchanged.
- Q14 - corrected (gap): PDF counts n(A) = 4, n(B) = 4 and writes 8 without checking A and B are disjoint. Added the check (only candidate x = 1 is not in A since |sin 2| = 0.909 != 8/pi^2 = 0.811). Answer unchanged.
- Q16 - corrected (gap): PDF says "for 7 solutions n = 13" without justification. Added the ordered list of solutions of cos t = 1/3 and why n = 13 is least. Answer unchanged.
- Q18 - corrected (final answer): the PDF's working ends "Sum of solutions = -1" (option C) but the answer line prints "Ans. A". Corrected to (C) -1 (see answer key below).
- Small clarifying bullets added without changing the PDF's method (source kept as pdf): Q10 (cos t = 0 case, which gives f = 1), Q15 (check that the kept root is a true solution), Q19 (explicit argument for n = 5), Q20 (proof that LHS <= 12), Q12 and Q17 (domain/rejection remarks).
- No question was `written`.

## Answer key
All 20 printed answers were checked numerically (root counting on fine grids, direct evaluation, symbolic reasoning). **Q18's printed key (A) is wrong: the correct answer is (C) -1.** The cubic x^3 - x^2 + 2 = 0 has the roots -1 and 1 +- i; the sum of all roots is 1 (probably how option A arose) but only the real root -1 is a solution. The other 19 keys are correct (printed keys for Q1-Q17, Q19, Q20 all agree with the computed answers).

## Alternates
Alternate solutions given for 17 questions: Q1 monotonicity of g(x) = 2x + 3 tan x - pi; Q2 homogenise with (sin^2+cos^2)^2; Q3 Newton recurrence for power sums; Q4 cot(A+B) addition identity; Q5 period-12 argument with only the 13th term left; Q7 symmetry about pi (pairs summing to 2pi); Q8 special-value test x = 1; Q9 60-degree rotation about Q; Q10 t = tan^2 substitution with monotone g(t); Q13 cos3y triple-angle and cos A = cos B; Q14 casework on sqrt x; Q15 auxiliary angle 5cos(t + phi); Q16 telescoping k/2^k = a_k - a_{k+1}; Q17 half-angle substitution; Q18 u = cos 2x substitution; Q19 factor 2 sin x (sin^2 + cos^2) first; Q20 sum of non-negative and positive parts.
Honest notes: Q3 (recurrence vs. squaring), Q14 (casework vs. substitution), Q19 and Q2 are modest variants - different technique but closely related to the main route.

### Questions with NO alternate
- Q6: the only route is to use the relation to replace tan by cos and recognise (1+a)^3; every variant is the same substitution.
- Q11: the equation factors immediately and counting solutions per period is the only method.
- Q12: after reducing to a quadratic in sin x the factorisation and counting are the only steps; the discriminant route is the same factorisation.

## Useful Result / Pattern
Every one of the 20 questions has a `useful_results` slide (3-4 bullets each); formulas spot-checked numerically (Q2 bound, Q9 side formula, Q16 sum, Q7 pairing).

## make_ppt.py warnings
None. No warnings and no "could not convert" notes; 851 equations converted to native PowerPoint equations; 127 slides. Slides were not rendered or opened in PowerPoint here (no soffice rendering in this environment).

## Skipped / assumed / guessed
- Concepts and levels self-assigned; levels are judgement against the calibrated anchors (cited per question in the ratings file).
- Question types taken from the answer format; marks assumed 4.
- The PDF text layer was garbled, so all pages were read from page images (80 dpi).
- Q9 stem's diagram was interpreted from the picture (P is 4 units from the line containing Q).
