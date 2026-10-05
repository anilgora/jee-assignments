# RUN REPORT - JEE_Main_Question_Bank_01_Differential_Calculus_07

Paper: 20 questions (printed Q121-Q140, numbered 1-20 in the deck). Q1 functional equation, Q2-Q10 continuity and differentiability (Q4-Q10 are blank-fill), Q11-Q20 methods of differentiation (functional equation, determinants, inverse function, successive derivatives).

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so JEE Advanced defaults were used: 4 marks for every question (Single Correct Q1-3 and Q11-20; Numerical Q4-10). Stated in the section dividers. The "Numerical Type" label is used for all blank-fill questions (Q4-10), including those with single-digit answers, because the paper does not mark them as 0-9 integer type.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.15** (all questions 4 marks).
- Level 1: 3 questions (Q2, Q15, Q16). Level 2: 11 (Q1, Q3, Q4, Q6, Q7, Q12, Q13, Q17, Q18, Q19, Q20). Level 3: 6 (Q5, Q8, Q9, Q10, Q11, Q14). No level 0, 4 or 5.
- No equivalence-relation questions and no multi-concept one-or-more-correct questions, so no adjustment or floor applies.
- Medium-confidence ratings: Q1, Q5, Q6, Q8, Q9, Q10, Q11, Q14.

## Solutions that are `corrected` or `written` (no `written`)
- Q5 (printed 125) - corrected: PDF counts "x^2/2 = 0,1,...,8 -> 8 points" (nine values; x=0 is the left end and is no discontinuity) and lists x=0 among the points of [sqrt x]. Real count: 8 jumps of the first floor, x=1,4 for the second, x=4 cancels. Answer 8 unchanged.
- Q11 (printed 131) - corrected: PDF writes "4f''(5pi/3)" where 24f'' is meant, and applies "put x=0: 1/2 = K/2" to f instead of f'. Answer -3 unchanged.
- Q14 (printed 134) - corrected: PDF stops at y''=1 and never adds y''+y'+y = 1 + 1/2 + 1/2 = 2. Final step supplied; answer (A) unchanged.
- Q17 (printed 137) - corrected: typos "(1-x)^2 y''" for (1-x^2)y'' and e^{sin^-1 x} for e^{3 sin^-1 x}. Answer 9e^{pi/2} unchanged.
- Q19 (printed 139) - corrected: y' and y'' were given with no derivation and the value 736/225 at x=1/2 with no arithmetic; both supplied. Answer 736 unchanged.
- Q20 (printed 140) - corrected: the three determinants shown at x=0 drop the unchanged columns (wrong entries); each still has a zero column so f'(0)=0. Rewritten in words. Answer (C) unchanged.
- Other solutions were reproduced as printed (`pdf`), with a few justification phrases added (Q4 why each piece is the maximum, Q7 value at x=2, Q9 why the left exponent tends to 0, Q13 uniqueness of the root of f(x)=7). Q16 has notational typos only ("(A)-(2)", "f''(n)"), written correctly as (1)-(2), f''(x).

## Answer key problems
- None. All 20 keys agree with my checks (sympy / mpmath / brute-force scan for Q5, Q6, Q8-Q20; by hand for Q1-Q4 and Q7).
- Q4 (printed 124): the PDF labels agree with the question (m = non-differentiable, n = discontinuous: m=3, n=0); nothing wrong.

## Alternates and results
- Alternate solutions given for **19 of 20 questions** (one each): Q1-Q12, Q14-Q20.
- Question with NO alternate:
  - Q13 (printed 133): the only route is differentiating g(f(x))=x and locating the root of f(x)=7; the inverse-derivative formula g'(f(a))=1/f'(a) is the same step, so no genuinely different method exists.
- Modest alternates (valid and verified, but close in spirit to the main route): Q3 (one-sided slopes instead of the graph), Q4 (crossing-points view), Q5 and Q8 (net-jump bookkeeping instead of one-sided limit check at x=4), Q9 (0/infinity reading and logarithm form), Q15 (logarithmic differentiation).
- Useful Result / Pattern given for **all 20 questions**.

## make_ppt.py output
- "Equations: 767 converted to native PowerPoint equations." 123 slides. No warnings and no "could not convert".

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per the run rules); slide fit was not checked visually.
- Levels are my own ratings from the calibrated rubric; the paper is JEE Main level, so everything is at 1-3. Nearest-anchor references in the ratings workbook are approximate.
- Chapter names in the ratings (Functions, Limit, Continuity & Differentiability, Methods of Differentiation) are self-assigned; Q6 concepts treat "limits" and "continuity" as separate chapters.
- The PDF text layer was garbled for maths, so every page was read from page images at 90 dpi; all answers were then recomputed (see above).
