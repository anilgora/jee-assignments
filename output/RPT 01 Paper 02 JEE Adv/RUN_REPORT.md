# Run report: RPT 01 Paper 02 JEE Adv

## Inputs
- Paper: `papers/RPT 01 Paper 02 JEE Adv.pdf` (15 pages, scanned, no text layer; read from page images, solutions printed). 17 maths questions: single correct Q1-4, one-or-more correct Q5-8, paragraph Q9-10 (one paragraph, two single-correct parts), numerical (paper numbering restarts) deck Q11-17. Deck numbering continuous 1-17.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks assumed (not printed): JEE Advanced defaults, stated in the section dividers: single correct 4 (Q1-4), one-or-more correct 4 (Q5-8), paragraph 3 (Q9-10), numerical 4 (Q11-17). Total 66. Types were inferred from the layout and answers (Q5-8 have multi-letter answers; Q11-17 have no options and answers like 46, so "Numerical Type", not integer 0-9).

## Difficulty (calibrated skill)
- Marks-weighted difficulty index (adjusted): **2.65** (inside/near the lower end of the official range 2.6-3.2).
- Questions per level (adjusted): L1 = 1 (Q1); L2 = 4 (Q2, Q3, Q11, Q15); L2.5 = 1 (Q8, multi-correct floor); L3 = 10 (Q4, Q5, Q6, Q7, Q9, Q12, Q13, Q14, Q16, Q17); L4 = 1 (Q10); L0 and L5 = 0.
- Multi-concept MCQ floor applied to Q8 only (level 2 raised to 2.5). No equivalence-relation questions.
- Confidence Medium on all except Q1, Q3, Q15 (High). The xlsx has live formulas without cached values (recalc.py not available here).

## Solutions whose source is corrected or written
- None. All 17 are `pdf`: every printed solution is correct and reproduced in full.
- Small gaps filled without changing the method (still `pdf`): Q1 (verification of the A^n pattern); Q4 (attainability of the minimum at x_k = 60 sqrt(a_k)); Q5 (explicit y_n and the A = 3^(2^(n-1)) steps of (C)); Q7(C) (why rank 2 gives infinitely many solutions); Q8 (statement D verdict, which the PDF's page break cuts to the inequality tan != 1); Q9 (why A=B=0 needs sin 6 theta = 0); Q10 (why the tangents cancel by theta -> pi - theta); Q13 (case y = 1 in the discriminant method); Q14 (the cot-difference step); Q15 (solution count in (2 pi, 3 pi], which the PDF page continues).

## Answer key check
- All 17 printed answers match my independent checks (sympy/numpy numerical tests): Q1 C (28), Q2 B (14 pi/3, roots 0, pi/3, 2pi/3, 5pi/3, 2pi), Q3 A, Q4 B (1/72 attained), Q5 A,B,C,D, Q6 A,B,D, Q7 A,B,C,D, Q8 A,B,C, Q9 B (5), Q10 A (-2, sum -2.0000), Q11 4, Q12 5, Q13 9, Q14 4, Q15 6, Q16 46, Q17 1. No wrong key found.

## Alternates and useful results
- Alternate solutions were written for 15 of 17 questions (Q1-13, Q15, Q16).
- Genuinely different methods: Q1 (I+N nilpotent binomial series), Q3 (Vieta symmetric functions instead of elimination), Q4 (AM-GM with a free parameter instead of Cauchy-Schwarz), Q5 (x_n = 2 coth(theta_n), doubling formula), Q7 (interpolation/Lagrange reading of the Vandermonde system), Q8 (subtract and add equations, no determinant), Q9 (complex geometric series, sixth roots of unity), Q10 (pairing theta with pi - theta, no tangents), Q12 (characteristic polynomial via Newton's identity), Q13 (AM-GM on x + 1/x instead of discriminant), Q15 (AM-GM equality condition), Q11 (P'(x) > 0, monotonic).
- Modest alternates (same core idea, different route): Q2 (tangent half-angle for the second factor), Q6 (quadratic fit from second difference, partial fractions with gap telescoping), Q16 (shift u = x - 2 with eigenvalues of the traceless matrix; structurally close to the main solution).
- **No alternate: Q14.** The cot-difference telescoping is the only elegant route; direct numerical evaluation of six terms is not elegant or genuinely different.
- **No alternate: Q17.** The equality-case of AM-GM plus factorial telescoping is the one natural path; a perfect-square rewriting of the same bound is just a rewording.
- Every question 1-17 has useful_results.
- Checks run (sympy/numpy): Q1 inverse sum 28 and I-10N+55N^2; Q2 roots and sign changes; Q3 alpha+beta=6, alpha*beta=7; Q4 equality attained, parametric bound 1/72; Q5 recurrence vs closed forms vs coth form for n=1..4; Q6 a_n, sums (1/18, 5/144), N=1 check of (C); Q7 Vandermonde factorisation, z formula, ranks for (a,b) in several cases; Q8 determinant factorisation; Q9/Q10 root list, -C/B = -tan - (-1)^m, pair sums, total -2; Q11 coefficients (3,0,0,0,7/2,2) and one real root; Q12 symmetry of C and Newton identity; Q13 range [1/3, 3]; Q14 S=4; Q15 six roots; Q16 Q(x), root sets, det(B^3+8I) = 64 - Q^3, V=46; Q17 partial sums approach 1.

## make_ppt.py output
- "871 equations converted to native PowerPoint equations", 120 slides, 17 questions. Only note: "Q7: very long question - font reduced to 22 pt" (harmless, the four statements are long). No warnings, no "could not convert" notes.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters, levels and nearest anchors assigned by me; anchors are only loosely comparable for several rows (Q9/Q10 paragraph levels in particular).
- The paragraph (Q9, Q10) is repeated on both parts. Q9 is rated 3 and Q10 rated 4 by my judgement.
- Python environment: the system PIL was broken; fixed with `pip install --force-reinstall pillow`; numpy and sympy installed for checks (not part of the repo).
