# RUN REPORT - JEE_Main_Question_Bank_01_Integral_Calculus_06

Paper: 20 questions (printed Q101-Q120), deck numbers 1-20, all single-correct, all Differential Equations.

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **2.30** (138 / 60 marks). No equivalence-relation adjustment or MCQ floor applied (no such questions).
- Questions per level: Level 1: 2 (Q2, Q17) | Level 2: 11 (Q1, 5, 6, 7, 9, 11, 13, 14, 15, 19, 20) | Level 3: 6 (Q3, 8, 10, 12, 16, 18) | Level 4: 1 (Q4) | Levels 0 and 5: none.
- Lowest-confidence rating: Q16 (Low; ill-posed branch question).

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): JEE Advanced default for single-correct = 3 marks each (stated on the section divider).

## Solutions whose source is corrected or written
- Q8 (printed 108) - **written**: the PDF prints, under Q108, the working and answer of Q109. A full solution was written; the key letter B (-3/e) is correct.
- Q10 (printed 110) - corrected: the PDF's integrated line omits the `2x` term and the constant `C`; restored. The printed question has "beta*gamma - 4 alpha" in the denominator, which is clearly "beta*y - 4 alpha" (the PDF's own working uses y); that reading is used. Answer (A) unchanged.
- Q16 (printed 116) - corrected: PDF does not justify discarding the branch sin^-1 y = -x + c (y >= 0 does) and does not mention the constant solution y = 1; added. Answer (A) kept.
- Q17 (printed 117) - corrected: PDF writes mu = e^(-bt) for y = mu e^(-bt) with y(0)=1; correct is mu = 1 (later lines of the PDF use mu = 1). Answer (D) unchanged.
- All other questions are `pdf` (working verified). Small notation typos silently fixed (Q9 "y tan^-1 x" for y e^(tan^-1 x); Q3 "ln n"/I.F. wording; Q11 tan(pi/2) handled as "denominator = 0"). A few steps the PDF skipped were added as bullets (Q1 linear form, Q3 constant C check, Q7 algebra, Q20 final alpha).

## Answer key
- **Q4 (printed 104): the PDF's key is wrong.** The key says (B), but the PDF's own working ends at (4 - sqrt2)/14, which is option (A); numerical integration of the ODE from y(pi/3)=sqrt3/10 gives y(pi/4)=0.18470 = (4 - sqrt2)/14. Option B is about 1.155. Deck answer: (A).
- Q16 (printed 116) is ill-posed in the strict sense: y = sin x on [0, pi/2] followed by y = 1 is also a C^1 solution and would give y''+y+1 = 2 at x = 2 (option C). The intended answer (A) = 1 is kept and the caveat is on the slide and in the speaker notes.
- Q8 (printed 108): the ODE is singular at x = 1 (ln x = 0); the key -3/e uses the same constant on both sides of x = 1. Kept as the intended reading; noted in the speaker notes.
- All other printed answers were checked numerically (scipy ODE integration / closed forms) and are correct.

## Alternates
Alternate solutions given for 18 of 20 questions: Q1, 2, 3, 4, 7 (two alternates), 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. Each reaches the same answer and was verified. Closer relatives of the main method: Q1 (variation of constants vs integrating factor), Q3 (substitute first, then guess particular solution), Q18 (w = (y-3)/y vs partial fractions), Q19 (product rule vs integrating factor).

### Questions with NO alternate
- Q5 (printed 105): the only practical route is the factorisation of the quartic and splitting the numerator as the sum of the two factors; every other route (definite integral from -1 to 0, tan^-1 addition) uses the same split.
- Q6 (printed 106): the integrating factor x^2+4 is just the product-rule form (d/dx[(x^2+4)y]); a definite integral from 0 to 2 is the same working. No genuinely different method.

## Useful Result / Pattern
Every one of the 20 questions has a `useful_results` slide.

## make_ppt.py warnings
None. The build printed no warnings and no "could not convert" notes; 854 equations converted to native PowerPoint equations; 127 slides. Slides were not rendered or opened in PowerPoint here (no soffice rendering in this environment).

## Skipped / assumed / guessed
- Concepts and levels are self-assigned; levels are judgement against the calibrated anchors (cited per question in the ratings file).
- Printed "gamma" in Q10 treated as "y" (see above).
- Marks (3 per question) are assumed.
