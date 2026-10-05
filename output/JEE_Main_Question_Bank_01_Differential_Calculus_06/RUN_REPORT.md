# RUN REPORT - JEE_Main_Question_Bank_01_Differential_Calculus_06

Paper: 20 questions (printed Q101-Q120, numbered 1-20 in the deck). Q1-12 Limits (Q7-12 numerical answers), Q13 continuity and a functional equation, Q14-15 3D lines, Q16 linear system, Q17-20 continuity and differentiability.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so JEE Advanced defaults were used: 4 marks for every question (Single Correct Q1-6 and Q13-20; Numerical Q7-12). Stated in the section dividers. The Numerical label is used for Q7-12 because answers such as 98, 24, 100, 170 are not single digits.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.10** (all questions 4 marks).
- Level 1: 2 questions (Q2, Q6). Level 2: 14 (Q1, Q3, Q4, Q5, Q7, Q10, Q12, Q13, Q14, Q15, Q16, Q18, Q19, Q20). Level 3: 4 (Q8, Q9, Q11, Q17). No level 0, 4 or 5.
- No equivalence-relation questions and no multi-concept one-or-more-correct questions, so no adjustment or floor applies.
- Medium-confidence ratings: Q3, Q8, Q9, Q11, Q12, Q13, Q17.

## Solutions that are `corrected` or `written` (no `written`)
- Q1 (printed 101) - corrected: PDF's first line for b has (1 - cos x) in the numerator instead of sin^2 x = (1 - cos x)(1 + cos x), and the line for a is cut off. Answer 32 unchanged.
- Q7 (printed 107) - corrected: PDF omits the minus sign of Vieta's sum of roots (-B/A); a+b is -7/6, not 7/6. The answer is squared, so 98 is unchanged. Added a check that the limiting quadratic 6x^2+7x+2=0 has real roots.
- Q8 (printed 108) - corrected: PDF restarts the sum at r = 1 so it gets f(x) = tan(x/2); with the printed lower limit r = 0 the correct f(x) = tan x. Answer 1 unchanged (it holds for any f(x) -> 0, f(x) != x).
- Q9 (printed 109) - corrected: PDF only sketches the first sum and never shows that the second sum contributes 285 before writing P^2+P-572 >= 0. Supplied the missing steps. Answer 24 unchanged.
- Q11 (printed 111) - corrected: PDF's last lines turn the constant 32 into 2 and claim 68/(9-sqrt17) = 17(9+sqrt17) (13.9 vs 223.1). Correct chain keeps 32: 1088/(9-sqrt17) = 17(9+sqrt17). Answer 170 unchanged.
- Q16 (printed 116) - corrected: typo "m^2 - 3x + 2 = 0" (should be m); Delta_x not shown. Added Delta_x = 2m^2 - 6m + 4. Answer 440 unchanged.
- Q20 (printed 120) - corrected: PDF says "f(x) < 0 => f decreasing"; should be f'(x) < 0. Answer (A) unchanged.
- Other solutions were reproduced as printed (`pdf`), with a few justification phrases added (Q3 squeeze sides, Q4 parity reasoning, Q6 bounds on the bases).

## Answer key problems
- None. All 20 keys agree with my checks (numerical with mpmath/brute force for Q1, 2, 4-13, 16-18; by hand for Q3, 14, 15, 19, 20).
- Q3 (printed 103): the PDF's question text never says [.] is the greatest integer function; the solution treats it so. The answer is 0 under either reading.
- Q4 (printed 104): the braces { } in the limit are read as grouping, not fractional part (a fractional-part reading would give 1, which is not an option).

## Alternates and results
- Alternate solutions given for **18 of 20 questions** (one each): Q1-2, Q4-18, Q20.
- Questions with NO alternate:
  - Q3 (printed 103): the only route is the squeeze 1 < f(5x)/f(x) < f(7x)/f(x); a function example such as ln x is only a sanity check, not a method.
  - Q19 (printed 119): continuity at one point needs LHL, RHL and f(3); the sign of the modulus and the floor are resolved the same way in any approach, so no genuinely different method exists.
- Modest alternates (valid and verified, but close in spirit to the main route): Q6 (logarithm form of the same bound), Q10 (binomial linearisation vs L'Hopital), Q17 (table of h(x) vs one-sided limits), Q18 (binomial vs conjugate), Q9 (term-by-term limit vs squeeze).
- Useful Result / Pattern given for **all 20 questions**.

## make_ppt.py output
- "Equations: 857 converted to native PowerPoint equations." 127 slides. No warnings and no "could not convert".

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per the run rules); slide fit was not checked visually.
- Levels are my own ratings from the calibrated rubric; the paper is JEE Main level, so everything is at 1-3. Nearest-anchor references in the ratings workbook are approximate.
- Chapter names in the ratings (Limits, Continuity and Differentiability, 3D Geometry, Matrices and Determinants) are self-assigned.
- The PDF text layer was garbled for maths, so every page was read from page images at 80 dpi; Q111's constants were confirmed numerically.
