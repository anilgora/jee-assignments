# Run report: PRT 06 Paper 02 JEE Adv

## Inputs
- Paper: `papers/PRT 06 Paper 02 JEE Adv.pdf` (23 pages, scanned image PDF with the solutions printed; read from page images).
- Blueprint: none was used. **Concepts self-assigned (no blueprint) - please review.**
- Marks are not printed in the PDF, so JEE Advanced defaults were assumed and stated in the section dividers: Single correct (Q1-4) 4; one-or-more correct (Q5-10) 4; matching (Q11-12) 3; integer 0-9 (Q13-17) 4; numerical (Q18) 4. Total 70.
- Question types were inferred from layout and answers: Q13-17 have single-digit answers (5, 5, 2, 5, 4) so they are Integer (0-9); Q18 (answer 59) is Numerical. Numbering is continuous 1-18.

## Difficulty (calibrated skill; no equivalence-relation questions; MCQ multi-concept floor 2.5 applies to Q5 and Q7 but does not change them)
- Marks-weighted difficulty index: **2.59** (181/70; official JEE Advanced 2021-2026: 2.59-3.21; this paper sits at the low end, equal to 2024).
- Questions per level: L0 = 0; L1 = 2 (Q1, Q12); L2 = 6 (Q2, Q3, Q4, Q6, Q11, Q18); L3 = 8 (Q5, Q7, Q8, Q9, Q10, Q13, Q15, Q16); L4 = 2 (Q14, Q17); L5 = 0.
- Medium-confidence ratings are marked in the Excel; Q5, Q7, Q10, Q14 and Q17 are the ones most worth a second look.

## Solutions whose source is corrected or written
- **Q7 (corrected, minor):** the PDF says the discontinuities of f are at x = n + 1/k for k in Z, |k| >= 2. Negative k gives points where f is continuous; the correct set is x = n + 1/m with integer m >= 2. Statement (D) and the key (A, C, D) are unaffected.
- **Q10 (corrected, minor):** the PDF heads the final check "Verification for n = 4" but computes n = 3 (as option D requires). Label fixed to n = 3; values and key (A, B, C) are correct.
- All other questions: `pdf` (working correct and reproduced; every step re-derived and every final answer confirmed by computation: Q4 by brute force over all permutations, Q8 and Q9 by exhaustive enumeration, Q10 identities for n = 2..7, Q13/Q16/Q17 by sympy series, Q15 numerically (L(20000) = 2.0002), Q14 sign-change count, Q18 exactly).
- Q5's PDF only says "from graph options ABC are correct"; I wrote the per-option verdicts from the graph into the solution bullets (no error, nothing in the PDF contradicted), so it is still marked `pdf`.
- Q8's PDF uses "by symmetry" for the equality of the three pair-intersections without justification; this is true (cyclic symmetry of positions and colours) and brute force confirms 17/56, so no correction was needed. The alternate states the symmetry explicitly.

## Answer key check
- No answer key looks wrong. All 18 keys confirmed (Q1 A, Q2 A, Q3 B, Q4 A, Q5 ABC, Q6 ABC, Q7 ACD, Q8 ABD, Q9 ABD, Q10 ABC, Q11 A, Q12 A, Q13 5, Q14 5, Q15 2, Q16 5, Q17 4, Q18 59).

## Alternates and useful results
- Alternate solutions were written for Q2-Q8 and Q10-Q18 (16 of 18).
- Q1 has no alternate: the only natural method is n from the variance, then 1 - P(0) - P(1); the (3+2)^4 view with denominator 625 is just the same computation, so none was invented.
- Q9 has no alternate: each statement has one natural counting method (gap method, mirror half, inclusion-exclusion over blocks, block + gaps); positions-first instead of letters-first is a reordering, not a different idea.
- Modest alternates (related to the main method rather than wholly different): Q4 (choose the position pattern first, then fill), Q5 (work in theta = tan^-1 x instead of the graph), Q11 (different route per item), Q13 (repeated implicit differentiation instead of series), Q15 (Riemann-sum recognition plus error bounds). Genuinely different: Q2 (raw second moment with origin at 3), Q3 (L'Hospital and direct differentiation), Q6 (centring at 1.5), Q7 (sequences and squeeze), Q8 (direct count of the pair intersection), Q10 (committee double counting), Q12 (sequential pairing, head/tail symmetry, complement, bijection), Q14 (t = (sin t / t)^2 monotonicity), Q16 (series reversion), Q17 (1^infinity shortcut), Q18 (positive and negative deviations balance).
- Every question 1-18 has useful_results.

## make_ppt.py output
- `note: Q8, Q9, Q11, Q12: very long question - font reduced` (20-22 pt) - harmless, left as is.
- No "could not convert" warnings, no warnings about sources, answers or short solutions. 936 equations converted to native equations; 140 slides.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks were used.
- Concept names, chapters (for the difficulty skill) and the type labels for Q11-18 were assigned by me; Q13 and Q16 were filed under "Methods of Differentiation".
- Q18: the PDF asserts the mode is 3 without checking k > 6; I confirmed that for k >= 7 the mode is 4 and no integer k gives mean deviation 7/8 there, so k = 4 is the only solution.
- Q14: the PDF's root count was confirmed numerically (one root near -0.80 and one near 1.80).
