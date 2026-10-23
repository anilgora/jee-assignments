# Run report: RPT 01 Paper 01 JEE Main

## Inputs
- Paper: `papers/RPT 01 Paper 01 JEE Main.pdf` (16 pages, scanned, no text layer; read from page images, solutions printed). 25 maths questions: 20 single correct (Q1-20) and 5 numerical (paper numbering Q1-5), deck numbering continuous 1-25.
- Blueprint: none. **Concepts self-assigned (no blueprint) - please review.**
- Marks are not printed; JEE Advanced defaults assumed and stated in the section dividers: single correct 4 (Q1-20), numerical 4 (Q21-25). Total 100. No negative marking stated (same convention as the earlier JEE Main decks).
- Type split assumption: the paper has no section headers; Q21-25 (answers 39, 50, 44, 4, 860, mostly outside 0-9) are shown as "Numerical Type".

## Difficulty (calibrated skill; no equivalence-relation questions, no MCQs so no floor)
- Marks-weighted difficulty index (adjusted): **2.20** (below the official Advanced range, as expected for a JEE Main paper).
- Questions per level: L1 = 1 (Q11); L2 = 18 (Q1, 2, 4, 5, 6, 7, 10, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25); L3 = 6 (Q3, 8, 9, 12, 14, 21); L0, L4, L5 = 0.
- Confidence Medium on Q1, 3, 8, 9, 12, 13, 14, 15, 18, 21; High on the rest. No Low.
- The xlsx has live formulas without cached values (recalc.py is not available here); open it in Excel to see computed values.

## Solutions whose source is corrected or written
- **Q18 (corrected, minor):** the question gives Tr((A-B)^2) = 14 but the PDF expands (A+B)^2. The cross term vanishes either way, so the answer -8 is unchanged; the working now expands (A-B)^2 as in the question.
- No question is `written`; all other 24 are `pdf`. Small gaps filled without changing the method (still `pdf`): Q2 (sign of each factor just after 0, since the PDF only shows the wavy figure); Q5 (the check of each candidate against sin x + cos x >= 0, which the PDF states only as the final list); Q7 (g(1), g(3) expressions); Q10 (factorisation of P and of the denominator, which the PDF skips); Q13 (cofactors of adj, which the PDF shows only as the final matrix); Q19 (which solutions are rejected by tan x > 0, cos x < 0, and why); Q9 (explicit factor 2(c+1)(2c-1)^2 form); Q15 (full off-diagonal entry of A^T A).

## Answer key check
- All 25 printed answers match my independent computation (sympy / numerical): Q1 C, Q2 B, Q3 B, Q4 A, Q5 A, Q6 B, Q7 A, Q8 B, Q9 C, Q10 B, Q11 D, Q12 A, Q13 B, Q14 A, Q15 D, Q16 A, Q17 C, Q18 B, Q19 D, Q20 A, then 39, 50, 44, 4, 860. No wrong key found.

## Alternates and useful results
- Alternate solutions were written for 23 of 25 questions.
- Genuinely different methods: Q3 (Pell numbers, explicit integer determinant), Q7 (explicit positive root and monotonic h(s)), Q8 (PR is a reflection; column-space direction), Q9 (eigenvalues of (2cos t - 1)I + J), Q12 (real eigenvalue of a det-1 orthogonal matrix is 1), Q13 (adj = inverse, (I+N)^-10), Q14 (affine line q = 4p - 3 through (1,1),(3,9)), Q15 (unit row + Cauchy-Schwarz), Q18 (entrywise Tr(M^2) = sum m_ij m_ji), Q21 (use the extreme terms p, q; 3p^2 - 10pq + 3q^2 = 0), Q22 (Vandermonde after C3 - C2), Q24 (cover-up rule with A + B + C = 0).
- Modest alternates (same core idea, different viewpoint or order): Q2 (quadrant by quadrant), Q5 (restrict to [0, pi/2] before squaring), Q6 (impose the GP condition on the first three terms), Q10 (test-point option elimination), Q11 (complete the square), Q16 (test-angle option elimination), Q17 (restrict first, then count in the 3x window), Q19 (impose the inequalities first), Q20 (digits of 5^60 via log 5 = 1 - log 2), Q23 (closed form of sum 1/(k(k+1)(k+2))), Q25 (factor 2 out of C3 and clear with the all-ones row).
- **No alternate: Q1.** The cot-difference telescoping is the only elegant route; the other routes (term-by-term numerical evaluation, rewriting the identity) are not genuinely different.
- **No alternate: Q4.** Everything flows from A*H = G^2 = b^2; a parametrisation a, ar, ar^2 only rewords it with heavier algebra.
- Every question 1-25 has useful_results.
- Numerical/symbolic checks (sympy/numpy): Q1 sum = 4; Q2 solution set from a fine grid (transitions at pi/6, pi/2, pi, 3pi/2, 11pi/6); Q3 lambda = 5 and a7a5 - a6^2 = 8, plus Pell integers; Q5 roots pi/4, pi/2; Q7 factorisation and the h(s) endpoints (s = -1 and 7/3); Q8 det = 0 at lambda = 2 and column-space direction (cos 15, -sin 15); Q9 factorisation 2(t+1)(2t-1)^2; Q12 P P^T = I, det P = 1, det(P - kI); Q13 A^10 and adj; Q14 det M = 2(x-y)(x-z)(y-z)(3k^2 - 4k - 3); Q16 identity residual 0 and test angles; Q17 six roots and filter; Q19 grid roots pi/6, 2pi/3, 7pi/6, 4pi/3; Q20 digits of 6^40 (32) and 5^60 (42); Q22 D_r = 2; Q24 partial fractions and sum 4; Q25 T_k and S_10 = 860; Q23 sum = 44. Q4, Q6, Q10, Q11, Q15, Q18, Q21 by hand.

## make_ppt.py output
- "992 equations converted to native PowerPoint equations", 158 slides, 25 questions. No warnings, no "could not convert" notes.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks.
- Concept names, chapters, levels and nearest anchors assigned by me; anchors are only loosely comparable for several rows.
- Question wording was transcribed from the solutions pages (the paper has no separate question section); Q13's matrix was read at higher resolution to confirm the entry 2 in the top-right corner.
- Python environment: system PIL was broken; fixed with `pip install --ignore-installed Pillow`; sympy and numpy installed for checks (not part of the repo).
