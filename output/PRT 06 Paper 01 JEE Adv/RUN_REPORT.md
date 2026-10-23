# Run report: PRT 06 Paper 01 JEE Adv

## Inputs
- Paper: `papers/PRT 06 Paper 01 JEE Adv.pdf` (17 pages, scanned image PDF with the solutions printed; read from page images).
- Blueprint: none was used. **Concepts self-assigned (no blueprint) - please review.**
- Marks are not printed in the PDF, so JEE Advanced defaults were assumed: Single correct (Q1-4) 4, one-or-more correct (Q5-8) 4, paragraph (Q9-10) 3, integer 0-9 (Q11-15) 4, numerical (Q16-18) 4. Total 70. This is stated in the section dividers.
- Question types were inferred from the layout and answers: Q11-15 have single-digit answers (Integer 0-9), Q16-18 (answers 10, 27, 45) are Numerical. Numbering is continuous 1-18.

## Difficulty (calibrated skill; no equivalence-relation questions; MCQ multi-concept floor applies to Q8 only and does not change it)
- Marks-weighted difficulty index: **2.54** (official JEE Advanced 2021-2026: 2.59-3.21; this paper sits at the low end).
- Questions per level: L1 = 2 (Q11, Q16); L2 = 8 (Q1, Q2, Q3, Q7, Q9, Q12, Q14, Q18); L3 = 4 (Q4, Q5, Q15, Q17); L4 = 4 (Q6, Q8, Q10, Q13); L0 = 0; L5 = 0.
- Medium-confidence ratings are marked in the Excel; Q8, Q10 and Q13 are the ones most worth a second look.

## Solutions whose source is corrected or written
- **Q8 (corrected):** the PDF assumed that if 8 occurs twice then x6 = x7 = 8, ignoring x5 = x6 = 8 with x7 > 8. It therefore found only 5 data sets, max range 7 and least x3 = 5, and its text concluded A, B, C true and D false, which contradicts its own key (C). Correct (brute-force checked): 14 data sets (5 with 8 thrice, 9 with 8 twice), max range 13, least x3 = 3, so only (C) is true.
- **Q13 (written):** the PDF gives only a hand sketch and the words "four corner points", so a full step-by-step solution was written (crossings at x = ±1 and x ≈ ±0.4696; answer 4 confirmed numerically).
- All other questions: `pdf` (PDF working is correct and reproduced; every step re-derived, final answers confirmed by computation: Q4 by brute force over all 1024 pairs, Q10 by series summation, Q11, Q14, Q15, Q16, Q17, Q18 by direct computation).

## Answer key check
- Q8: the key (C) is correct, but the PDF's written working does not support it (see above). No other key looks wrong.

## Alternates and useful results
- Alternate solutions were written for Q1-Q17 (17 of 18).
- Q18 has no alternate: the only natural route is recognising the two sums as (1+x+x^2)^10 and (1-x)^10 with product (1-x^3)^10; the remaining routes (direct convolution of coefficients, roots of unity) are the same idea or much worse, so none was invented.
- Modest alternates (related to the main method rather than wholly different): Q3 (L'Hospital instead of series), Q4 (generating function over four element-states vs the PDF's binomial odd-sum), Q5 (explicit sequences and squeeze), Q16 (ogive interpolation view of the same formula). Q11 (Catalan symmetry), Q2 (identity D = x^2 + n(n+1)), Q6 (f = g sin(pi x) slope-jump principle), Q8 (single witnesses instead of enumeration), Q12 (modulus form of max/min), Q14 (complete the square), Q15 (differentiate the equation to get an ODE) are genuinely different.
- Every question 1-18 has useful_results.

## make_ppt.py output
- `note: Q7: very long question - font reduced to 20 pt.` - harmless, left as is.
- Two equations in the Q10 alternate first stayed as LaTeX text because of `\rm odd`; resolved by renaming the symbol (`G_o`), rebuilt, no "could not convert" notes remain.

## Skipped / assumed / guessed
- No rendering or thumbnail check of the slides was possible (no soffice); only the script's own checks were used.
- Concept names, chapters and the type labels for Q11-18 were assigned by me.
- A first reading of Q3 at low resolution suggested a sign mismatch in the question; at high resolution the printed question matches the PDF solution, so no correction was needed (answer 9, key B).
- Alternates for Q4 and Q5 are verified but only moderately different (see above).
