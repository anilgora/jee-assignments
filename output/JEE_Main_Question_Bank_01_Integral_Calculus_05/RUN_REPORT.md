# RUN REPORT - JEE_Main_Question_Bank_01_Integral_Calculus_05

Paper: 20 questions (printed Q81-Q100), deck numbers 1-20. Q1-8 numerical (Definite Integration), Q9-20 single correct (Differential Equations).

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **2.44** (166 / 68 marks). No equivalence-relation adjustment or MCQ floor applied (no such questions).
- Questions per level: Level 1: 1 (Q11) | Level 2: 11 (Q4, 5, 7, 9, 10, 12, 15, 16, 17, 18, 19) | Level 3: 7 (Q1, 2, 3, 6, 13, 14, 20) | Level 4: 1 (Q8) | Levels 0 and 5: none.
- Lowest-confidence rating: Q8 (Low; hidden-derivative idea, rated 4).

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper): JEE Advanced defaults - numerical-value questions (Q1-8) = 4 marks each; single-correct questions (Q9-20) = 3 marks each. This is stated on the section dividers.

## Solutions whose source is corrected or written
- Q2 (printed 82) - corrected: PDF has the constant `-pi/(2x2)` where `-pi^2/4` is needed (square dropped); the PDF also omits why `2x-pi` may be replaced by `-2x` and why the integral halves. Added as steps. Final answer 15 unchanged.
- Q6 (printed 86) - corrected: first line of the PDF's working has `+10 * integral(t^11 (1+3t)^5)` where the question has `+18 alpha(11,5)`. Changed to 18; answer 32 unchanged.
- Q20 (printed 100) - corrected: PDF uses `d(x/y) = (x dy - y dx)/y^2` (wrong sign) and gets `ln y = -cos(x/y)`. Correct: `ln y = cos(x/y)`. The final answer (A) is unchanged because only `cos^2(x/2)` is needed. The corrected solution was verified against the ODE.
- No question is `written`; all other questions are `pdf` (working verified, notation typos silently fixed: Q4 "F(x)^2" for F(x^2), Q16 "P(f(x))" for f(f(x)), Q18 "ln n f(n)").

## Answer key
All 20 printed answers were checked (numerically with mpmath, and by differentiating the closed-form solutions of the ODEs). None looks wrong.

## Alternates
Alternate solutions given for 16 of 20 questions: Q1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 17, 19, 20. Each reaches the same answer and was verified.
Some alternates are closer relatives of the main method than others (Q6: exact-derivative recognition vs by-parts; Q9: quotient rule vs integrating factor; Q13: exact differential vs integrating factor).

### Questions with NO alternate
- Q7 (printed 87): a direct recursion; the only route is to compute C1, S1, C2, S2, C3 in turn. No different method found.
- Q15 (printed 95): the quotient-rule form is the standard (and only short) route; the integrating-factor and variation-of-constants routes are the same method.
- Q16 (printed 96): after the composition, the integrating factor method is the only practical route; the substitution x = u^2 gives the same working.
- Q18 (printed 98): the functional equation reduces to f' = f/2 by y = 0; the exponential ansatz needs that same step to justify uniqueness.

## Useful Result / Pattern
Every one of the 20 questions has a `useful_results` slide.

## make_ppt.py warnings
None. The build printed no warnings and no "could not convert" notes; 903 equations converted to native PowerPoint equations; 127 slides. Slides were not rendered or checked visually (no soffice rendering in this environment).

## Skipped / assumed / guessed
- Concepts and levels are self-assigned; levels are judgement against the calibrated anchors (cited per question in the ratings file).
- Section dividers state that marking is assumed.
- The deck was not opened in PowerPoint here.
