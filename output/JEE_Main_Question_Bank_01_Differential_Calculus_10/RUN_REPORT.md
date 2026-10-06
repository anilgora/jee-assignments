# RUN REPORT - JEE_Main_Question_Bank_01_Differential_Calculus_10

Paper: 16 questions (printed Q181-Q196, numbered 1-16 in the deck). Q1-Q12 single correct, Q13-Q16 numerical. Topics: maxima and minima, extreme values on closed intervals, roots of cubics, integral-defined function.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so JEE Advanced defaults were used: 4 marks for every question (Single Correct Q1-12; Numerical Q13-16). Stated in the section dividers. The "Numerical Type" label is used for Q13-Q16 (the paper does not mark them as 0-9 integer type).

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.625** (all questions 4 marks).
- Level 1: 6 questions (Q3, Q6, Q9, Q10, Q13, Q14). Level 2: 10 (Q1, Q2, Q4, Q5, Q7, Q8, Q11, Q12, Q15, Q16). No level 0, 3, 4 or 5.
- No equivalence-relation questions and no multi-concept one-or-more-correct questions, so no adjustment or floor applies.
- Low confidence: Q4 (flawed question). Medium: all others. Paper is JEE Main level.

## Solutions that are `corrected` or `written` (no `written`)
- Q3 (printed 183) - corrected: PDF factors as 6(x^2 - 3a + 2a^2); the middle term must be 3ax. Factorisation (x-a)(x-2a) and answer (C) are right.
- Q4 (printed 184) - corrected: PDF writes the product as a1 a5 a6 = a(a+4d)(a+3d); the question's product is a1 a4 a5 = a(a+3d)(a+4d) (the later working is right). Also P(d) -> +infinity as d -> -infinity, so there is no global maximum; d = 8/5 is the local maximum (P = 72/25). Key (B) kept.
- Q11 (printed 191) - corrected: PDF's option numbering is inconsistent (says "option (4) is incorrect", meaning (C), and never discusses (B)). Rewritten so (A), (B), (C) are shown false and (D) true. Answer (D) unchanged.
- Q12 (printed 192) - corrected: PDF writes f(2) = ... = -4 = 4 and labels its sketch "max = 17, min = -17"; correct values are f(2) = -4, max 17, min -7. A decreasing-function argument was added. Answer (C) unchanged.
- Q15 (printed 195) - corrected: PDF replaces (x^2+x+2)/((x+2)(x+3)) by 1/((x+2)(x+3)); equal only in sign (x^2+x+2 > 0). Justification and the f'' test for the minimum added. Answer 39 unchanged.
- All other solutions are as printed (`pdf`), with small justifications added where terse: Q1 (maximum at 1/e, powers), Q2 (sign table), Q7 (values f(-1), f(2) omitted in the PDF), Q8 (factorisation of f' and the endpoint comparison the PDF omitted), Q9, Q13, Q14 (second-derivative test), Q16 (multiplicity argument).

## Answer key problems
- Q4 (printed 184): the question says "greatest" but the product has no global maximum (unbounded as d -> -infinity); the key 8/5 is right only as the local maximum.
- All other 15 keys agree with my checks (sympy / numerical scans for Q2, Q4, Q7, Q8, Q11, Q12, Q13, Q16; by hand for the rest).

## Alternates and results
- Alternate solutions given for **13 of 16 questions** (one each): Q1-Q3, Q5-Q7, Q9-Q15.
- Questions with NO alternate:
  - Q4 (printed 184): any other route (shifting the variable, logarithmic differentiation) is the same single-variable cubic maximisation; no genuinely different method.
  - Q8 (printed 188): factoring f' in cos x and comparing with the endpoint is the method; the only other routes are option elimination, which still needs the same values.
  - Q16 (printed 196): the sign scheme of f' with multiplicities is the only method.
- Modest alternates (valid and verified but close in spirit to the main route): Q3 (gap between critical points), Q9 (Vieta product of roots), Q10 (mirror symmetry of f', g'), Q12 (completing squares for monotonicity).
- Useful Result / Pattern given for **all 16 questions**.

## make_ppt.py output
- "Equations: 605 converted to native PowerPoint equations." 96 slides. No warnings and no "could not convert" notes.

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per the run rules); slide fit was not checked visually.
- Levels are my own ratings from the calibrated rubric; nearest-anchor references are approximate.
- Chapter names in the ratings are self-assigned.
- The PDF text layer was garbled for maths; pages were read from images and answers recomputed.
- Q14: the rectangle is assumed axis-parallel and symmetric about the x-axis (as in the PDF).
