# Run report: PRT 07 Paper 02 JEE Adv

## Inputs
- Paper: `papers/PRT 07 Paper 02 JEE Adv.pdf` (15 pages, scanned image PDF with solutions printed, no text layer; read from page images). 17 maths questions; the paper restarts numbering in each section (Q1-4 SCQ, Q5-8 MCQ, two paragraph questions, integer Q1-4, numerical Q1-3), deck numbering is continuous 1-17. Question wording was transcribed from the solutions pages.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks are not printed; JEE Advanced defaults assumed and stated in the section dividers: single correct 4 (Q1-4), one-or-more correct 4 (Q5-8), paragraph 3 (Q9-10), integer 4 (Q11-14), numerical 4 (Q15-17). Total 66.
- Types: Q11-14 shown as Integer (0-9) (answers 2, 9, 4, 8); Q15-17 as Numerical (answers 6, 28, 2.5 - the 2.5 is not an integer, 6 and 28 are outside 0-9).

## Difficulty (calibrated skill; no equivalence-relation questions)
- Marks-weighted difficulty index (adjusted): **2.83** (inside the official Advanced range 2.59-3.21).
- Questions per level (integer level): L2 = 6 (Q1, Q3, Q5, Q11, Q12, Q17); L3 = 8 (Q2, Q4, Q7, Q8, Q9, Q13, Q14, Q16); L4 = 3 (Q6, Q10, Q15); L0, L1, L5 = 0.
- Multi-correct floor (2.5): applied to Q5 (level 2 -> 2.5). Q8 is also flagged multi-concept but its level 3 is above the floor.
- Medium confidence on most rows (see the Excel); no Low.

## Solutions whose source is corrected or written
- **Q16 (corrected):** the PDF says that for |k| >= 4 the equation 2x^3 - 6x = k has "only one real root". At |k| = 4 it has two distinct real roots (one double, e.g. 2(x+1)^2(x-2) for k = 4), and the double root is not an extremum. Conclusion n = 1 and the answer 28 are unchanged; the case was rewritten.
- All other questions: `pdf` (every step re-derived; final answers checked numerically/symbolically). Small gaps filled without changing the method: Q4 (t = e gives no tangent; added), Q8 (the PDF never states that option D is false), Q6 and Q11 (the expansion/branch details written out), Q17 (the expansion of the dot product).

## Answer key check
- All 17 printed answers match my independent computation (Q1 B, Q2 A, Q3 B, Q4 A, Q5 ABC, Q6 ABD, Q7 ABD, Q8 ABC, Q9 C, Q10 B, then 2, 9, 4, 8, 6, 28, 2.5). No key looks wrong.
- Option texts of Q2 were read from a low-resolution page image; the correct option (e^{-7/36}) matches the key letter A.

## Alternates and useful results
- Alternate solutions were written for Q1-Q5 and Q7-Q17 (16 of 17).
- Q6 has no alternate: the only route is to find the active branch of the min/max on each interval and test the breakpoints; every other route (sketching, sign charts) is the same argument reworded, so none was invented.
- Modest alternates (a different viewpoint or toolset on the same core idea rather than a wholly different technique): Q5 (parametrisation u), Q13 (cleaner tools for each sub-part), Q15 (corner-transmission criterion). The rest are genuinely different methods, e.g. Q2 Leibniz coefficients, Q4 Newton-Raphson intercept map, Q7 conditional independence from P(A)=1/2, Q8 negative-binomial view, Q14 sign alternation of (f')^2+f f'' at nine points, Q16 evolute of the parabola, Q17 Thales circle / perpendicular bisector.
- Every question 1-17 has useful_results.
- Numerical checks done: Q2 series coefficients (sympy), Q4 tangent counts, Q6 piecewise f (max, kinks), Q7 full enumeration, Q8 series sums, Q10, Q14 root count, Q15 one-sided slopes, Q16 minima count for k = -6..6, Q3 Cauchy-Schwarz bound.

## make_ppt.py output
- "917 equations converted to native PowerPoint equations", 127 slides, 17 questions. Only note: "Q5: very long question - font reduced to 20 pt" (harmless, kept). No "could not convert" notes, no warnings.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters and levels assigned by me; the anchors for Q2, Q13 and Q16 are only loosely comparable.
- Python environment: system PIL was broken; fixed with `pip install --force-reinstall pillow` (not part of the repo).
