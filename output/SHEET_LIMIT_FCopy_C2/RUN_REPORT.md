# Run report - SHEET_LIMIT_FCopy_C2

Paper: Exercise C-2 (Limits), 34 questions (Q1-34, numbered as in the PDF): Q1-22 evaluate/prove, Q23-31 paragraph questions (3 paragraphs), Q32-34 match-the-column. The PDF has answers and solutions. The text layer is garbled, so all pages were read from images. Date of run: 2026-10-14.

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed), JEE Advanced defaults, stated in the section dividers: Q1-8 and Q10-22 subjective/numerical = 4 marks each; Q9 one-or-more-correct = 4; Q23-31 paragraph single-correct = 3 each; Q32-34 matching = 3 each. Total 124. Q21 (four parts a-d) is treated as one 4-mark question.

## Difficulty
Marks-weighted difficulty index (adjusted): **2.04** (below the official JEE Advanced range 2.6-3.2; expected for a limits exercise sheet).
Level counts: L0 = 0, L1 = 7 (Q1, 7, 11, 18, 24, 25, 28), L2 = 18 (Q2-6, 10, 12-17, 21, 23, 26, 27, 32, 34), L2.5 = 1 (Q9, multi-concept MCQ floor), L3 = 8 (Q8, 19, 20, 22, 29, 30, 31, 33), L4 = 0, L5 = 0.
No equivalence-relation adjustment. MCQ floor applied to Q9 only. Medium confidence: Q8, 9, 19, 22, 29, 31, 33. The workbook was not recalculated (no recalc.py); the index was computed by hand.

## Solutions whose solution_source is "corrected" (7)
- Q7: **PDF answer e^-1 is wrong.** The PDF writes base-1 as (sqrt(n^2+n)-(n+1))/n; it is (sqrt(n^2+n-1)-n)/n, exponent limit +1. Correct answer e (n = 10^8 gives 2.7182818).
- Q9: PDF leaves the answer blank, never shows option (D) and never concludes. Added (D) (coefficient of x^n in (1+x)^2n is C(2n,n)) and the conclusion: all four options (A, B, C, D) are correct.
- Q14: PDF's telescoped form drops the last factor 1/cos(theta/2^n); added it. Limit theta/tan(theta) unchanged (checked numerically for theta = 0.7, n = 5).
- Q15: PDF says t = ln x -> +infinity; as x -> 0+ it is -infinity. Algebra and the answer e^3 unchanged.
- Q20: PDF's expansion of the numerator is inconsistent (stray terms); rewritten order by order. L = 1/2 and answer 307 unchanged (numerical check 0.49999999).
- Q29: PDF argues f(x^3-x^2) > f(0) = 4 and f(2x^4-x^5) > 4, which is false (f(0) is an isolated value). Correct bounds from monotonicity: f > 3 on the left, f > 2 on the right. Limits 3 and 2, answer 3, unchanged.
- Q31: PDF writes [f(...)] = 3 and then uses 9; the expression is [3 f(...)], and 3f -> 9+, so the bracket is 9. Answer 5 unchanged.

## Solutions with solution_source "written" (0)
None; the PDF had a usable solution for every question.

## Answer key / question problems
- Q7: key e^-1 wrong, correct e (see above).
- Q9: answer blank in the PDF; correct answer (A, B, C, D).
- Q13: PDF answer line reads "g(x) = sin x and l = e"; the asked value is the limit, e.
- All other answers re-derived and checked numerically with mpmath (limits evaluated at 10^-8 to 10^-9 or 10^6 to 10^8 etc.): Q1-6, 8, 10-12, 14, 16, 20, 22, 32-34 and the geometry limits Q17, Q19 (formulas). Paragraph answers Q23-31 checked by reasoning.

## Alternate solutions
Alternates (a different technique or viewpoint) were written for 27 of 34 questions: Q1-22, Q26, Q27, Q32, Q33, Q34. Each was checked against the answer by hand or numerically.
Questions with NO alternate (7), and why:
- Q23: the only method is the |x|<1 branch of the paragraph's f and the limit (1+lambda)/3 = 2; no second route.
- Q24: single step, f(x) = x sin(1/x) for |x|>1 and the standard limit.
- Q25: single step, continuity at -2 and sin(1/2) < 1/2.
- Q28: single step, domain 0<r<2 then range; a parametric reading is the same step.
- Q29: the only reasoning is the side of approach of each argument (a concrete model function is a check, not a method).
- Q30: the only reasoning is [f]=2, f(-x)->3 and the fractional part; expansions of 1-cos x are the same step.
- Q31: the only reasoning is the sign of sin x - x, then the floors; a series for the argument is the same step.
Borderline alternates (different viewpoint, not very different arithmetic), please judge: Q2 (derivative test instead of series), Q4 and Q5 (equivalents/logarithm instead of substitution/1^inf rule), Q10 (exact recurrence + Viete), Q12 (Euler sine product for L only, splitting for N and M), Q21 (weighted-average view), Q22 (derivatives at 0 instead of series), Q32 (Taylor equivalents for all four parts).

## Useful Result / Pattern
All 34 questions have useful_results (2-3 bullets each).

## make_ppt.py warnings
- "Q24: only 2 solution bullets" - the PDF's working is a single line; expanded to 4 bullets (branch for |x|>1, formula, substitution, limit) and rebuilt; no warnings remain. No "could not convert" warnings; 1285 equations converted.

## Skipped / assumed / guessed
- Concepts self-assigned (no blueprint); marks assumed as above; levels are my own application of the calibrated rubric.
- No recalc.py, thumbnails or rendering; the deck (206 slides) was not opened in PowerPoint here.
- Q21 (4 parts) and Q32-34 (match the column) are single questions with one answer line each.
- The content JSON was edited by hand for Q24 after the first build; the deck was rebuilt from the final JSON.
