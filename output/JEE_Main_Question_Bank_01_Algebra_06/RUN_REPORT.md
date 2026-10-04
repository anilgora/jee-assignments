# Run report: JEE_Main_Question_Bank_01_Algebra_06

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_06.pdf` (printed Q101-Q120, renumbered 1-20). Determinants (Q1-5, 7-15, 17, 19), linear systems (Q2, 5, 7-10, 12), matrices (Q14, 16, 18, 20).
Files: `_content.json`, `_Analysis.pptx` (127 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question**: Q2, Q7, Q13 numerical; all others single correct (JEE Advanced defaults); stated on the section dividers.

## Difficulty
Marks-weighted difficulty index: **1.85** (no equivalence-relation or multi-correct adjustments).
Level 1: 4 questions (Q9, 16, 18, 20). Level 2: 15 questions (Q1-8, 10, 12-15, 17, 19). Level 3: 1 question (Q11). Levels 0, 4, 5: none.
JEE Main-style bank rated on the Advanced scale, so the index is low. Levels were judged against the rubric and a few anchors, not a full anchor comparison per question; Q11 and Q15 are Medium confidence.

## Solutions: corrected / written
No question was `written`. Corrected (the answer is unchanged in every case):
- **Q2 (printed 102):** the PDF's inequality reads 1 <= k^2 <= 30; 15 <= 5k^2 <= 150 gives 3 <= k^2 <= 30 (the PDF's own list of k and the count 8 are right). The lower limit 15 is garbled in the PDF.
- **Q4 (printed 104):** after C2 -> C2 - C3 the first entry of the second column is printed x (must be y); the last line has (c-b-1), which must be (c-b+1) since y - z = c - b + 1; as printed it gives y(b-a), not y(a-b).
- **Q9 (printed 109):** 2(8+2) - 3(12-2) + 2(-3-2) is printed as 32 - 30 - 10 = -8; it is 20 - 30 - 10 = -20 (still non-zero).
- **Q12 (printed 112):** the printed matrix has 2a+1 in the third entry of row 2 (the equation has a+1; with 2a+1 the determinant would be a(20a^2+36a+37)); the working for D and the sign of the quadratic (discriminant -1259) are missing and added.
- **Q15 (printed 115):** the PDF's expansion line drops the term -d(2 sin t - d) and is not a valid expansion; correct expansion given, (d+2)^2 - sin^2 t as the PDF states.
- **Q16 (printed 116):** (3,1) entry of P^2 printed as 9+3x3+1 = 19; it is 27. P^3, P^4 are skipped; added. P^5 as printed is correct.
- **Q17 (printed 117):** second entry of row 2 after R2-R1 printed -cos t - sin t (should be -2cos t - sin t); the factor e^{-t} is dropped (|A| = 5e^{-t}, not 5).
Reproduced from the PDF (`pdf`) with small fill-ins of omitted steps: Q1, Q3 (interval of 2θ), Q5, Q6, Q7 (factor λ-3, why the roots are 0, 3), Q8 (k = -2 case), Q10 (rank argument), Q11, Q13, Q14, Q18 (A^16 step and option check), Q19, Q20.

## Answer key
All printed keys agree with my own computation (sympy / brute force; Q2 counted by brute force = 8). No key looks wrong. In Q15 the PDF finds d = 1 or -5; only -5 is an option.

## Alternates and results
Alternates for 19 of 20 questions; all 20 have useful_results. Techniques: evaluation at x = 0, 1 plus leading coefficient (Q1), cross product of two rows (Q2), R1-R2 giving cos2θ factor (Q3), numerical specialisation (Q4), eq1 - eq3 without k (Q5), R1-R3 / R2-R3 (Q6), case split λ = 3 vs y = z (Q7), elimination to 2x2 (Q8, Q9), Gaussian elimination consistency (Q10), Vieta form a(a²-3b) (Q11), column-sum trick (Q12), symbolic determinant x(x-1)² (Q13), A = I + vvᵀ (Q14), multilinearity in sin θ (Q15), nilpotent binomial (Q16), Wronskian / Abel (Q17), complex-number rotation (Q18), Vandermonde formula (Q19).
Weakest alternates (close to the main solution): Q13 (symbolic expansion only changes the last step; the log part is the same), Q8, Q9 (elimination vs Cramer).

## Questions with NO alternate
- **Q20:** the only routes are adding the upper-right entries (the PDF's method), the same fact phrased as exp(kN) with N² = 0, or induction, all the same idea reworded; no genuinely different method, so none was added.

## make_ppt.py warnings
First build: four "could not convert" notes for the Q20 options (my mistake: row separators had lost a backslash in the JSON). Fixed in the content and rebuilt; the final build prints no warnings (702 equations converted natively).

## Skipped / assumed
No rendering/thumbnail check was possible (no soffice step). Concepts and marks assumed as above. Q8's statement (E) is read literally ("infinitely many solutions if k != -2"). Q2: Hindi/English duplicate text in the paper was ignored.
