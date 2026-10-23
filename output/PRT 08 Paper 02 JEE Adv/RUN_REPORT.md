# Run report: PRT 08 Paper 02 JEE Adv

## Inputs
- Paper: `papers/PRT 08 Paper 02 JEE Adv.pdf` (15 pages, no text layer; read from page images, solutions printed). 17 maths questions; numbering restarts per section in the paper (SCQ 1-4, MCQ 5-9, matching 10-11, integer 1-3, numerical 1-3); deck numbering is continuous 1-17.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks are not printed; JEE Advanced defaults assumed and stated in the section dividers: single correct 4 (Q1-4), one-or-more correct 4 (Q5-9), matching 3 (Q10-11), integer 4 (Q12-14), numerical 4 (Q15-17). Total 66.
- Types: the PDF has no section headers for the last two groups; Q12-14 (answers 2, 3, 6) shown as Integer (0-9), Q15-17 (answers 8, 18, 8) as Numerical (18 is outside 0-9). This split is my assumption.

## Difficulty (calibrated skill; no equivalence-relation questions)
- Marks-weighted difficulty index (adjusted): **2.85** (inside the official Advanced range 2.59-3.21).
- Questions per level: L1 = 1 (Q14); L2 = 6 (Q3, Q10, Q11, Q15, Q16, Q17); L3 = 5 (Q1, Q2, Q4, Q5, Q6); L4 = 5 (Q7, Q8, Q9, Q12, Q13); L0 and L5 = 0.
- Multi-correct floor (2.5): not binding (Q5, Q7, Q8 are multi-concept but already at 3-4). No equivalence-relation adjustment.
- Confidence Medium on most rows, High on Q3, Q10, Q11, Q14, Q15, Q17. No Low.

## Solutions whose source is corrected or written
- **Q5 (corrected):** the PDF writes "Choosing x1 = 1/sqrt2" without showing why that point gives a common tangent, and gives no verdict for (A) or (D). Added the intercept condition (tangent of slope m to x^2 = 3y/2 has intercept -3m^2/8) and the verdicts. Answer unchanged. See the answer-key note below.
- **Q7 (corrected):** the PDF's "divide by x^2" step is valid only for x>0 (for x<0 the root changes sign), yet it later uses f(-1). The formula f = sqrt((x^2-x+1)/(x^2+x+1)) is nevertheless right for all real x because its derivative equals f' everywhere (checked symbolically); added that as one bullet. Answer unchanged.
- All other questions: `pdf` (every step re-derived; answers checked numerically/symbolically). Small gaps filled without changing the method: Q6 (g(0)=0 needed for L'Hopital stated), Q8 (centres on opposite sides, |lambda1-lambda2| computed, so P is the midpoint of T1T2), Q3 (acute-angle check 1+m1m2>0).

## Answer key check
- All 17 printed answers match my independent computation (Q1 B, Q2 C, Q3 A, Q4 B, Q5 ABC, Q6 ABCD, Q7 ACD, Q8 BC, Q9 ACD, Q10 A, Q11 A, then 2, 3, 6, 8, 18, 8).
- **Q5 (C) is only conditionally true.** The question has two common tangents: x1 = 1/sqrt2 (line 2sqrt2 x - y - 3 = 0, PQ = 3sqrt2, area 9/(4sqrt2)) and x1 ~ 0.9028 (slope ~2.853, PQ ~ 3.739, area ~ 1.632). The key A,B,C follows the first tangent, which I kept; for the second tangent (C) would be false. The question wording ("a common tangent") is ambiguous - please decide whether to keep the key.
- Q2: the PDF's applications of the King property are correct; I confirmed I = -pi numerically (trapezoid sum -3.14159).

## Alternates and useful results
- Alternate solutions were written for all 17 questions (Q1-Q17).
- Genuinely different methods: Q1 (product-to-sum plus doubling the distance to y=x), Q2 (full-period shift by pi), Q3 (given point is common; h' = 1/(x-1)), Q5 (double-root test of the line), Q6 (composition of Taylor polynomials), Q7 (differentiate the antiderivative; trigonometric roots of the cubic), Q8 (orthogonal circle from power of a point; projection of M1M2), Q9 (u = 1+sqrt3 tan x, centring theta, cos = (D-1)/2), Q10 (Beta function; tan^2(sec^2-1)), Q11 (reflect the centre instead of the line; general-form orthogonality), Q12 (integrate once, Rolle twice), Q13 (monomial test with rising factorials), Q14 (factorisations f-16 and f-20), Q17 (right-triangle meaning of N/T; integrate ln(y/x) directly).
- Modest alternates (a different viewpoint or toolset on the same core idea): Q4 (one direct substitution t = x/sqrt(1-x^2) plus the standard formula), Q15 (vertex value instead of the discriminant), Q16 (eliminate x to get v(u); zig-zag picture of h).
- No question was left without an alternate.
- Every question 1-17 has useful_results.
- Numerical/symbolic checks done: Q1 limit and minimum distance; Q2 trapezoid sum (full range and the 2-pi version); Q3 slopes and h'; Q4 sum 1.1024 (n=4000) vs 1.1107 and the integral; Q5 all common-tangent roots, double-root factorisation; Q6 limits via sympy; Q7 F' = f' at 5 points, cubic roots (1.899, -0.407, -1.492); Q9 all three integrals and K; Q10 Beta values; Q11 expansion identity; Q13 sympy identity with random f; Q12 example moments; Q14, Q15 factorisations and vertex value; Q16 reasoning by cases; Q17 by hand.

## make_ppt.py output
- "945 equations converted to native PowerPoint equations", 135 slides, 17 questions. Only notes: font reduced to 20 pt for the long question text of Q5, Q8 and Q11 (harmless, kept). No "could not convert" notes, no warnings.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters, levels and nearest anchors assigned by me; anchors for several rows are only loosely comparable.
- Question wording was transcribed from the solutions pages (the paper has no separate question section). The List-I/List-II tables of Q10 and Q11 were flattened into text lines.
- Python environment: system PIL was broken; fixed with `pip install --force-reinstall pillow` (not part of the repo).
