# Run report: RPT 03 Paper 01 JEE Main

## Inputs
- Paper: `papers/RPT 03 Paper 01 JEE Main.pdf` (15 pages, scanned, no text layer; read from page images, solutions printed). 25 maths questions: 20 single correct (Q1-20) and 5 numerical (paper numbering Q1-5), deck numbering continuous 1-25. The paper has no separate question section; question text was transcribed from the solutions pages.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks not printed; JEE Advanced defaults assumed and stated in the section dividers: single correct 4 (Q1-20), numerical 4 (Q21-25). Total 100. Same convention as RPT 01 and RPT 02 Paper 01. The numerical answers (12, 2, 4, 17, 4) are shown as "Numerical Type" because 12 and 17 are outside 0-9.

## Difficulty (calibrated skill)
- Marks-weighted difficulty index (adjusted): **2.04** (below the official Advanced range, as expected for a JEE Main paper).
- Questions per adjusted level: L0 = 1 (Q19); L1 = 3 (Q3, 6, 8); L2 = 15 (Q1, 2, 4, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 25); L3 = 6 (Q5, 7, 9, 11, 21, 24); L4, L5 = 0.
- No equivalence-relation questions; no one-or-more-correct questions, so neither adjustment applies.
- Confidence High on Q1, 3, 6, 8, 10, 12, 13, 14, 16, 17, 19, 20, 25; Medium on the rest; no Low.
- The xlsx has live formulas without cached values (recalc.py is not available here); open it in Excel to see computed values.

## Solutions whose source is corrected or written
- **Q2 (corrected, minor):** the PDF writes the limit as x -> 0^- in the first two lines of the limit computation; (sin x)^x is defined only for x > 0, so the limit is x -> 0^+. Values and answer (D) unchanged.
- No question is `written`; the other 24 are `pdf`. Small gaps filled without changing the method (still `pdf`): Q4 (f(0)=0 from x=y=0, which the PDF uses without stating), Q7 (derivation of which crossing roots lie on the valid branch), Q12/Q24 (nothing added beyond the PDF steps), Q21 (t = 0 case noted in the alternate; there d^2 = 16 > 12).

## Answer key check
- All 25 printed answers match my independent check (hand derivation, sympy and numerical evaluation): Q1 B, Q2 D, Q3 B, Q4 A, Q5 B, Q6 A, Q7 C, Q8 B, Q9 D, Q10 B, Q11 A, Q12 B, Q13 A, Q14 C, Q15 A, Q16 C, Q17 A, Q18 B, Q19 A, Q20 B, then 12, 2, 4, 17, 4. No wrong key found.

## Alternates and useful results
- Alternate solutions were written for 20 of 25 questions (Q1-5, 7-12, 13, 15, 17-19, 21-23, 25).
- Genuinely different methods: Q1 (point symmetry of a cubic about its inflection point), Q3 (g = (x+2) sgn(x-2)), Q4 and Q23 (subtract x^3 to get a Cauchy additive function), Q5 (ln x < x-1, e^t >= 1+t, and Cauchy MVT), Q7 (shift t = x-1, even function, golden ratio), Q8 (factorisation (x-1)^2 (x+2)), Q9 (f = t - {t}(1-{t}) with cancellation of the corner at g = 0), Q10 (discriminant of the depressed cubic), Q11 (theta = 2 arctan(1/(2 sqrt a)) by symmetry), Q12 (AM-GM without calculus), Q15 (strict peak of f equal to 1), Q18 (expand the determinant first, Vieta), Q19 (eliminate the parameter), Q21 (complete the square in d^2), Q22 (Taylor series instead of L'Hopital), Q25 (f''(r) from the factored f').
- Modest alternates (same core idea, different tool): Q2 (standard limit x ln x -> 0 plus an explicit interior test point; the IVT step is the same), Q13 (root-distance formula and binomial expansion), Q17 (Leibniz rule and standard limit).
- **No alternate: Q6.** After expanding the 2x2 determinant, implicit differentiation is the only natural route; writing y = sqrt(x^3+3) would only reword it.
- **No alternate: Q14.** Continuity and equal one-sided derivatives at the junction for both functions, then f'/g', is the single idea; the limit-definition ratio is the same computation.
- **No alternate: Q16.** The normal's intercept and the sign of 1 + ln x on each side are the only tools; a substitution u = 1 + ln x is the same argument.
- **No alternate: Q20.** The discriminant (equivalently completing the square) and the subnormal formula have no genuinely different route.
- **No alternate: Q24.** Thresholds m > 1 and m > 2 come from the same squeeze argument for each term; any other route repeats it.
- Every question 1-25 has useful_results.
- Checks done: Q1 depressed cubic and symmetry (sympy); Q2 g(0), g(1), g(pi/2) numerically; Q4/Q23 f = x^3 + cx; Q5 inequality chain at x = 1.01, 1.5, 3, 6; Q7 and Q9 non-differentiable points by numerical one-sided derivatives (Q9: 4 vs 0 at x = 1 and x = 1.5 only); Q10 discriminant sign; Q11 theta formula, d(theta)/dt = -4/5 and tan(theta) = 4/3; Q12 volume 32 pi/9; Q13 sqrt(4.24) = 2.0591; Q17 y''(e) e^3 = -1; Q18 determinant expansion, f'(0), f''(0) and the cubic factorisation (sympy); Q19 alternate derivative 11/4 (sympy); Q21 minimum of d^2 = 12; Q22 limit 2 and series 1 + x + x^2 (sympy); Q25 f''(1) + f''(2) = 4. Others by hand.

## make_ppt.py output
- "888 equations converted to native PowerPoint equations", 152 slides, 25 questions. No warnings, no "could not convert" notes.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters, levels and nearest anchors assigned by me; anchors are only loosely comparable for several rows.
- Python environment: system PIL was broken; fixed with a forced reinstall of Pillow; sympy and numpy installed for checks (not part of the repo).
