# Run report - SHEET_DIFFERENTIAL_EQUATION_FCopy_JM

Paper: Exercise J-M (JEE Main differential-equation questions, 2023-2024), 65 questions (Q1-65, numbered continuously as in the PDF); the PDF has answers and solutions. Date of run: 2026-10-14.

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper; JEE Advanced defaults from the task, stated in the section dividers): every question 4 marks (single-correct Q1-12, 14-20, 27-36, 45-57; numerical-value Q13, 21-26, 37-44, 58-65; total 260). Types were taken from the paper: option questions = Single Correct, no options = Numerical. The eight sections in the deck are just the consecutive runs of the same type (the PDF mixes the two types).

## Difficulty
Marks-weighted difficulty index (adjusted): **2.14** (below the official JEE Advanced range 2.6-3.2; this is a JEE Main chapter sheet, no expected distribution).
Level counts: L0 = 0, L1 = 10 (Q4, 5, 19, 30, 34, 43, 44, 55, 58, 63), L2 = 36, L3 = 19 (Q3, 7, 8, 10, 16, 21, 22, 24, 25, 26, 35, 36, 37, 40, 41, 42, 51, 57, 60), L4 = 0, L5 = 0.
No equivalence-relation adjustment and no MCQ floor applied (no such questions). Medium-confidence ratings: Q3, 7, 8, 10, 13, 16, 21, 22, 24-26, 35, 36, 37, 40-42, 49, 51, 57, 60, 62.

## Solutions whose solution_source is "corrected" (11)
- Q4: PDF divides by (alpha - beta), assuming alpha != beta; case alpha = beta (integral gives gamma t) added. Answer 0 right.
- Q10: PDF working stops after the substitution 3t - t^3 = z (page ends); integration, constant and evaluation at x = 2 completed. Answer A right.
- Q21: PDF jumps from c = sqrt3 to "|-2| = 2"; steps added (closed form xy = sin x + sqrt3 cos x, (xy)'' = -xy). The PDF's printed answer letter "B" is wrong for a numerical question; the value is 2.
- Q22: PDF writes "b = 3" where the point is Q(a, 1/2) (should be a = 3) and an unused "c = 1"; variable fixed. Answer 5 right.
- Q27: PDF writes "mu = e^{-bt}" for y(0)=1 (should be mu = 1); fixed.
- Q31: PDF's last line "y(2) = 2(1 + sin 2) - 2 sin 2 = 2" does not follow from its own antiderivative; replaced by the simplified antiderivative (x^2-2x) sin x + C. Answer 2 right.
- Q37: PDF stops at "2(2x+3y) + 9|2x+3y-8| = x + c" (log sign also missing); the rest (c = 18, matching to alpha = 1, beta = 2, gamma = 8) completed. Answer 29 right.
- Q42: PDF stops after "u e^{-y} = integral of e^{-y} e^{2y} dy"; remainder completed (u = e^{2y}, e^{2 alpha} = sqrt3). Answer 9 right.
- Q50: PDF writes "y . tan^-1 x = ..." where the left side should be y . e^{tan^-1 x}; fixed. Answer A right.
- Q51: PDF reads the printed "(beta gamma - 4 alpha)" as "(beta y - 4 alpha)" and omits +2x in one line; with beta = 0 (forced) both readings give the same circle. Answer A right.
- Q60: PDF writes the limit as "x -> infinity" (should be t -> x); the rest is right. Answer 24 right.

## Solutions with solution_source "written" (1)
- Q49: the PDF prints, under Q49, a copy of Q50's solution ((1+x^2)y' + y = e^{tan^-1 x}), so no solution for Q49 exists; a complete one was written. Answer B (-3/e) agrees with the key.

All other questions (53) are "pdf": the printed working is correct and reproduced with only the notation changed (and, in a few places, an obvious step such as the integral of x*sec^2 x or the sign case in Q16 spelled out).

## Answer key / question problems
- Q21: key shows "B" but the question has no options; correct value 2 (the working gives it).
- Q25: key says "Bonus". Computed value is 4 + ln 3 (about 5.10), not an integer; the answer field shows this.
- Q36: key "Bonus" is right: no real alpha satisfies f(0) = 2 and lim f(-inf) = 1 (checked both signs of alpha).
- Q41: answer 20 agrees with the key, but the question is ill-posed: the solution y = 2/(3x) + x^2/3 has Y'(1) = 0, against the condition Y'(x) != 0, and the "signed area" used is only valid where Y' < 0 (x < 1). Kept as the key's answer; the deck does not mention this problem, it is flagged here only.
- Q49: key B (-3/e) kept, but y = -3(ln x + 1)/(2x ln x) blows up at x = 1, so the constant on x > 1 is not determined by y(1/e) = 0; the key takes the same constant on both sides (remark added as the last bullet).
- Q57: key A (= 1, from y = sin x) kept; y'^2 = 1 - y^2 also has the constant solution y = 1, so y = sin x on [0, pi/2] glued to y = 1 gives another admissible solution with value 2 at x = 2 (remark added as the last bullet).
- Q51: printed "(beta gamma - 4 alpha)" kept as printed (the PDF solution treats it as beta y); the answer is unaffected.
- No other answer key looked wrong; every final answer was checked numerically (ODE solved or substituted back with sympy/scipy).

## Alternate solutions
Alternates (a genuinely different technique) were written for 49 of 65 questions: Q1-6, 8-10, 12-16, 18-25, 27-31, 33-38, 41, 42, 47, 48, 50, 51, 54-58, 60-63, 65 (each verified by hand against the answer; many are also numerically confirmed). Where an alternate is a variant of the same idea (e.g. Q6 definite integral of an exact derivative) it still changes the method (no constant, no integrating factor) and is stated as such in its idea strip.
Questions with NO alternate (16), and why:
- Q7, Q11, Q17, Q26, Q32, Q43, Q44, Q45, Q46, Q49, Q53: first-order linear (or exact-derivative) equations or direct partial-fraction integrals - variation of constants, integrating factor and "recognise the exact derivative" are the same computation, so no genuinely different method exists (Q43/44/46 only have the definite-integral variant, which is not a new idea).
- Q39, Q52, Q64: one separable/exact-differential step; the only other route is plugging in the answer, which would be padding.
- Q40: the limit-as-derivative step and the homogeneous equation have no second route.
- Q59: the substitution x + y + 2 = t is the only reasonable way to solve; monotonicity then gives the extrema.

## Useful Result / Pattern
Every question (1-65) has useful_results (2-4 general, conditioned statements each).

## make_ppt.py warnings
None after the final build (373 slides, 2384 equations converted). An earlier build printed "could not convert ... \frac{32}{9} / \frac{4+e^2}{4} / \frac{693}{128}": caused by three non-raw strings in my script turning "\f" into a form-feed; fixed and rebuilt. No equation is left as LaTeX text.

## Skipped / assumed / guessed
- No rendering or thumbnail check (no soffice/skills in this environment); the deck was built but not viewed.
- The difficulty xlsx was not recalculated (recalc.py not available); its formulas fill on opening in Excel.
- Levels are my calibrated estimates against the user's anchors (mostly L2 for routine integrating-factor/homogeneous chains, L1 for one-step questions, L3 for hidden-structure or numerical questions with several linked ideas); a few are Medium confidence (listed above).
- Concepts are self-assigned in standard JEE wording; Hindi text in the PDF was ignored (English only).
- Tags used for chapter in the ratings: "Differential Equation" for all questions.
