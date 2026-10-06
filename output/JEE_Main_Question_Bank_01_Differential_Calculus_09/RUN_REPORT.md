# RUN REPORT - JEE_Main_Question_Bank_01_Differential_Calculus_09

Paper: 20 questions (printed Q161-Q180, numbered 1-20 in the deck). Q1-Q7 Rolle / monotonicity / one-one / integration of derivatives (single correct), Q8-Q13 numerical (Rolle zero count, critical points, root counting, sequence maximum), Q14-Q20 maxima and minima (single correct).

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so JEE Advanced defaults were used: 4 marks for every question (Single Correct Q1-7, Q14-20; Numerical Q8-13). Stated in the section dividers. The "Numerical Type" label is used for Q8-Q13 (the paper does not mark them as 0-9 integer type; Q9's answer is 252).

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.90** (all questions 4 marks).
- Level 1: 4 questions (Q5, Q6, Q15, Q19). Level 2: 14 (Q1, Q2, Q3, Q7, Q9, Q10, Q11, Q12, Q13, Q14, Q16, Q17, Q18, Q20). Level 3: 2 (Q4, Q8). No level 0, 4 or 5.
- No equivalence-relation questions and no multi-concept one-or-more-correct questions, so no adjustment or floor applies.
- Low confidence: Q4 (flawed question). Medium: all level-2 and level-3 ratings except as listed. Nearest-anchor references are approximate; the paper is JEE Main level.

## Solutions that are `corrected` or `written` (no `written`)
- Q3 (printed 163) - corrected: PDF writes 9f(x) = (5x^2 - 2x^2 - 4)/x^2; the numerator must be 5x^4 - 2x^2 - 4. The following line and the answer (D) are right.
- Q4 (printed 164) - corrected: the PDF's bounds (1/8 + 1/(4 ln 2) <= f <= 1 - 1/ln 2, i.e. 0.486 <= f <= -0.443) contradict each other, because g(2) = ln2 - 2 > g(4) = 2 ln2 - 4 although g must be non-decreasing. No such f exists, so (A) and (B) are true only vacuously. Solution rewritten to show this; key (B) kept.
- Q7 (printed 167) - corrected: PDF says h = f-g has no zero (it has exactly one, in (1, 3/2), which is what (C) says) and that h(x) is in (h(-1), h(2)) = (-8, 8); actually h(-1) = -10, so the range is (-10, 8) and (B) is the false statement. Answer (B) unchanged.
- Q16 (printed 176) - corrected (notation only): f written with x^2 instead of x^3; second condition written f'(-2) = 12 + 4a - b/2 instead of f'(2) = 12 + 4a + b/2; factorisation written (x+2)^2 instead of (x-2)^2. a = -9/2, b = 12 and the answer (C) are unaffected. I also added the check that the minimum is at the endpoint -2 (f(-1/2) is about -8.65).
- All other solutions were reproduced as printed (`pdf`), with justification added where the PDF is terse: Q1 (why f'(1) = 0 and the zeros lie in different intervals), Q6 (explicit repeated value f(2-sqrt3) = f(2+sqrt3)), Q8 (distinctness argument for the Rolle points, and that the bound 5 is attained), Q9 (cases p = 2 and p = 4), Q10 (sign checks for the counts), Q11 (sign values beyond the turning points, so all five roots are located), Q13 (exactly two roots, pointing to the alternate), Q18 (checks of -1 and 2). Q2, Q5, Q12, Q14, Q15, Q17, Q19, Q20 are as printed. Small typos (n for x, "F" for f, "v" for sqrt) were written correctly.

## Answer key problems
- **Q4 (printed 164):** the data f(2) = 1/2, f(4) = 1/4 are inconsistent with the inequality (shown above), so the question is flawed; (B) "both true" is right only because the set of such f is empty. Please review whether to keep the question.
- All other 19 keys agree with my checks (sympy / numerical scans for Q8 (explicit polynomial with exactly 5 zeros), Q9, Q10, Q11, Q13, Q16; by hand for the rest).
- Q5 (printed 165): g(x) = f(-x) - f(x) uses f outside its stated domain (0,1); it was evaluated by its formula, as the PDF does.

## Alternates and results
- Alternate solutions given for **16 of 20 questions** (one each): Q1-Q6, Q10-Q17, Q19, Q20.
- Questions with NO alternate:
  - Q7 (printed 167): the only route is to integrate f''-g'' = 6x twice with the two given conditions (a definite-integral version is the same computation).
  - Q8 (printed 168): the integrating factor f^2 for (f^3 f'')' is the only way to turn the expression into a derivative (other powers of f do not work), so Rolle on f^3 f'' is the method; no different method found.
  - Q9 (printed 169): the condition reduces to the single fact "A sin4x + B has no zero iff |B| > |A|"; any other phrasing (range of sine, sign of f') is the same step.
  - Q18 (printed 178): reading the piecewise graph (slopes, kinks, parabola vertex) is the method; no different technique exists.
- Modest alternates (valid and verified but close in spirit to the main route): Q2 (composition and scaled line), Q14 (zeros plus the kink test), Q15 (Vieta instead of factoring), Q20 (corner-triangle decomposition of the same area).
- Useful Result / Pattern given for **all 20 questions**.

## make_ppt.py output
- "Equations: 908 converted to native PowerPoint equations." 129 slides. No warnings and no "could not convert" notes in the build.

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per the run rules); slide fit was not checked visually.
- Levels are my own ratings from the calibrated rubric; the paper is JEE Main level, so everything is at 1-3.
- Chapter names in the ratings are self-assigned.
- The PDF text layer was garbled for maths, so all pages were read from page images (80 dpi, one page at 130 dpi), and answers were recomputed with sympy/numerics.
