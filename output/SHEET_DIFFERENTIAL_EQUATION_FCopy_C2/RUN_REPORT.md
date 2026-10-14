# Run report - SHEET_DIFFERENTIAL_EQUATION_FCopy_C2

Paper: Exercise C-II (Differential Equations), 33 questions; PDF has answers and solutions. Date of run: 2026-10-14.

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper; JEE Advanced defaults, stated in the section dividers):
Subjective Q1-21 = 4, Integer Q22-24 = 4, Paragraph single-correct Q25-30 = 3, Matching Q31-33 = 3 (total 123).
Q22-24 were classed as Integer (0-9) because their answers are single digits; Q1-21 as Subjective (the paper header says "Subjective / Integer type"). Subjective questions were rated in the calibrated skill as type "Numerical".

## Difficulty
Marks-weighted difficulty index (adjusted): **2.31** (lowest of the official range 2.6-3.2; this is a chapter sheet, no expected distribution).
Level counts: L0 = 0, L1 = 4 (Q2, Q27, Q29, Q30), L2 = 15, L3 = 14, L4 = 0, L5 = 0.
No equivalence-relation adjustment and no MCQ floor applied (no such questions). Medium-confidence ratings: Q5, 7, 9-13, 15, 20, 22, 25, 28, 31-33.

## Solutions whose solution_source is "corrected" (11)
- Q9: PDF's second line has the sign of the right side reversed, so its curve does not satisfy the equation as printed; corrected to y/(x-y) = -(1/2)sin^-1 x + pi/4 - 2.
- Q13: PDF says the curve passes through (e, 1/e) when solving for c; the question's point is (1, 1/e) (final curve was right).
- Q14: PDF takes the midpoint R as (0, y) and garbles the x-coordinate condition; rewritten with R = (0, y/2), Q = (x - y dx/dy, 0).
- Q16: PDF subscripts mis-typed after (5) (e^-k, e^-k1 instead of e^-k1, e^-k2) and the final log base misprinted; answer log_{4/3} 2 correct.
- Q17: PDF never evaluates the amount after 10 minutes; step added (275/3 = 91 2/3 gm).
- Q18: PDF prints dy/dx - y/x = kx^2 and y = kx^3/2 + cx (signs lost) which contradicts its own key; correct sign is -k.
- Q19: PDF does not apply "passes through the origin" (c = 0); step added.
- Q22: first line of PDF working prints the denominator as f(h+(x+1)) + f(x+1); should be minus.
- Q24: intermediate line e^2 = -2/(1+f(2)) drops the constant 2 (and "4/2" typo); corrected to e^2 = 2f(2)/(1+f(2)).
- Q32 (C): PDF says f' changes from -ve to +ve at pi/6, 5pi/6 (that is a minimum); at the maxima it changes from +ve to -ve. Also option-by-option checks added for (A), (B), (D).
- Q33: typos in the PDF working ((C) sum printed with |x+1| twice, (D) y = c^(x+c) - 1) and (A) only by graph; rewritten, integer table added.
No question has solution_source "written" (every question had a PDF solution). Other questions are "pdf" (only notation changed, and in a few places an obvious step spelled out).

## Answer key problems
- **Q9: the printed key (1/2)sin^-1 x - y/(x-y) = pi/4 + 2 is wrong for the equation as printed.** Differentiating the key gives (x dy - y dx)/(x-y)^2 = -dx/(2 sqrt(1-x^2)), the opposite sign. Verified numerically (at x = 1/3: LHS of the ODE with the key's curve = -0.530 vs RHS +0.530; with the corrected curve LHS = RHS). The deck gives the corrected answer. (The key would be right if the equation had (x dy - y dx) in the numerator.)
- **Q24: caution, not a key error.** y = 1/(2e^(-x^2/2) - 1) becomes infinite at x = sqrt(2 ln 2) = 1.18, so no differentiable f exists on [0, 2] with f(0) = 1; f(2) = e^2/(2 - e^2) is only a formal value. The intended answer k = 2 is kept. Noted in the deck's Useful Result slide.
- Q20: the PDF's figure and its Hindi text describe an inverted (vertex-down) cone; the English text does not say so. "(vertex downward)" was added to the question text to match the solution.
- All other answers verified by sympy / numerics and agree with the key (Q1-8, 10-23, 25-33).

## Alternate solutions
Alternates (genuinely different method, verified) were produced for 25 questions: Q1, 3-11, 13, 16-18, 20-25, 28, 29, 31-33.

### Questions with NO alternate (8) and why
- Q2: the factorisation (sum and product of roots) is the only natural method; any other route is a reworded version of it.
- Q12: the log-derivative condition g'/g = g''/g' is forced; all routes are this one reworded.
- Q14: the condition "Q = (-x, 0)" gives y' = y/(2x) directly; no distinct method.
- Q15: the condition (y - xy')^2 = xy is homogeneous and y = vx is the only sensible reduction.
- Q19: integrating factor, variation of parameters and guessing (1+x^2) are the same linear-equation method; no distinct elegant route.
- Q26: range of 2xe^x needs the single critical point x = -1; any other proof is the same calculus.
- Q27: a single standard limit.
- Q30: f' = 1/x + e^x > 0 is the whole argument.

## Useful results
Every question (Q1-33) has a Useful Result / Pattern slide.

## make_ppt.py output
Equations: 1216 converted to native PowerPoint equations; 198 slides built. Warnings: none. Notes only:
- "Q31/Q32/Q33: very long question - font reduced to 20 pt" - harmless (the matching columns are long); left as is.
No "could not convert" messages.

## Skipped / assumed / guessed
- No slide images were rendered (no soffice); the deck was not visually inspected, only built without warnings.
- Level ratings are my own judgement against the calibrated anchors (official DE questions are mostly L2, so most questions here are L2/L3); no user ratings were available.
- Matching questions (Q31-33) carry the full matching table in the question text (no option list).
- Q23 integer type: the family of curves y = (a sin x + (b+c) cos x) e^(x+d) has two independent constants, giving a second-order equation (alpha = beta = 2).
- Q21 is a proof question; "answer" is stated as "Proved".
