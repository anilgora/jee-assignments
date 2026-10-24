# Run report: RPT 03 Paper 02 JEE Adv

## Inputs
- Paper: `papers/RPT 03 Paper 02 JEE Adv.pdf` (14 pages, scanned, no text layer; read from page images, solutions printed). 17 maths questions: single correct Q1-4, one-or-more correct Q5-8, paragraph Q9-10 (one paragraph, two single-correct parts), then two groups with restarted numbering (1-4 and 1-3) = deck Q11-17. Deck numbering is continuous 1-17.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks assumed (not printed): JEE Advanced defaults, stated in the section dividers: single correct 4 (Q1-4), one-or-more correct 4 (Q5-8), paragraph 3 (Q9-10), integer 4 (Q11-14), numerical 4 (Q15-17). Total 66. Assumption: Q11-14 (answers 3, 3, 2, 4) are Integer Type (0 to 9) and Q15-17 (2.25, 343, 240) are Numerical Type; the paper does not name the two groups.

## Difficulty (calibrated skill)
- Marks-weighted difficulty index (adjusted): **2.59** (just under the official-paper range 2.6-3.2).
- Questions per adjusted level: L1 = 1 (Q3); L2 = 6 (Q1, Q2, Q11, Q15, Q16, Q17); L2.5 = 1 (Q5, multi-concept MCQ floor raised it from 2); L3 = 7 (Q4, Q6, Q7, Q8, Q9, Q12, Q14); L4 = 2 (Q10, Q13); L0 and L5 = 0.
- No equivalence-relation questions. Confidence Low on Q9, Q10 (paragraph anchors differ), High on Q1, Q3, Q11, Q15-17, Medium elsewhere. The xlsx has live formulas without cached values (recalc.py not available).

## Solutions whose source is corrected or written
- Q10 - corrected: the PDF writes f''(x) = -f(x) e^{-(f(x))^2/2} (in N'(x) for Statement I and in Statement III). Since f'' = -f (f')^2 = -f e^{-(f)^2}, the exponent must be -(f)^2. Signs and all conclusions are unchanged. I also added the reason M(x) -> -/+ infinity in Statement II (f/x -> 0 because f' -> 0) and named the three root intervals.
- All other 16 are `pdf`. Small gaps filled without changing the method (still `pdf`): Q1 (the root x = 1 is unique because f is strictly increasing); Q9 (f' stays positive so the division by f' is allowed); Q12 (matrices written out with the PDF's values; the PDF's row display of |C1 C2 C3'| is garbled in the scan, the value -1 is correct); Q8 (h(0+) = -1 added to show h stays negative on (0, e^-2]).

## Answer key check
- All 17 printed answers match my checks (sympy/numpy where computational): Q1 B (g'' = -3/32; series reversion agrees), Q2 C (k = 3, V = 24 sqrt3 pi), Q3 A, Q4 D (f = x^2 + x; kinks of h at -2, 0, 2), Q5 A,B,C, Q6 B,C, Q7 A,B,C,D, Q8 B,D, Q9 B, Q10 A (II: three roots confirmed by a numerical ODE solution for c = 0.3, 0.7), Q11 3, Q12 3 (sympy: f'(0) = -1, f''(0) = 1), Q13 2 (sympy roots of the quartic: 0.841, 1.760), Q14 4, Q15 2.25, Q16 343, Q17 240. No wrong key found.

## Alternates and useful results
- Alternate solutions were written for 16 of 17 questions (all except Q14).
- Genuinely different methods: Q1 (series reversion), Q2 (AM-GM on pi r^2 + pi r h + pi r h), Q3 (shift the origin to the inflection point; f(1+t) = t^3 + 2t + 4), Q4 (subtract the common x^2; only |x|-type kinks remain), Q5 (inverse-function theorem and convexity of the inverse), Q6 (completing squares plus the opposite-sides argument), Q7 (power series of ln x/(x-1); f and f' continuous at 1), Q8 (tangents through the origin = critical points of f(x)/x), Q9 (sign of f'' from the ODE; f' never vanishes as it solves a linear ODE), Q10 (f odd and concave; chord slope f(x)/x), Q11 (separate the parameter k = 3x - x^3), Q12 (Maclaurin coefficient matching), Q13 (discriminant of cubic minus the parabola's tangent), Q16 (u = ln x, v = ln y, E = t u' - u), Q17 (Vandermonde and Euler operator).
- Modest alternate (same skeleton, one step done differently): Q15 (MVT slope as the average of f' via one integral; completing the square for c).
- **No alternate: Q14.** The identity [x] + [x + 1/2] = [2x], the switch of the limit at |x| = 1 and the jump count are the only route; any other presentation is a reordering of the same steps.
- Every question 1-17 has useful_results.

## make_ppt.py output
- "926 equations converted to native PowerPoint equations", 140 slides, 17 questions. Only notes: "Q9: very long question - font reduced to 20 pt" and the same for Q10 (paragraph plus options / four statements; harmless). No warnings, no "could not convert" notes.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters, levels and nearest anchors were assigned by me; anchors are only loosely comparable (Q9/Q10 paragraph levels in particular; Q9 = 3, Q10 = 4 is my judgement).
- The paragraph is repeated on both parts Q9 and Q10.
- Python environment: the system PIL was broken; fixed with `pip install --force-reinstall pillow`; numpy, scipy, sympy installed for checks (not part of the repo).
