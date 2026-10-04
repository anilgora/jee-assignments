# Run report: JEE_Main_Question_Bank_01_Algebra_07

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_07.pdf` (printed Q121-Q140, renumbered 1-20), all Matrices and Determinants.
Files: `_content.json`, `_Analysis.pptx` (122 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question**: Q4 and Q10 numerical, all others single correct (JEE Advanced defaults); stated on the section dividers.

## Difficulty
Marks-weighted difficulty index: **1.80** (no equivalence-relation or multi-correct adjustments).
Level 1: 5 questions (Q2, 7, 11, 12, 16). Level 2: 14 questions (Q1, 3-6, 8-10, 13, 15, 17-20). Level 3: 1 question (Q14). Levels 0, 4, 5: none.
JEE Main-style bank rated on the Advanced scale, so the index is low. Levels were judged against the rubric and a few anchors, not a full anchor comparison per question; Q6, Q8, Q14 are Medium confidence.

## Solutions: corrected / written
No question was `written`. Corrected (the answer is unchanged in every case):
- **Q12 (printed 132):** the PDF "rejects" sin α = -1/sqrt2 assuming α in [0, π/2], which the question does not state; it satisfies the equation but gives no option.
- **Q13 (printed 133):** the first factor in the PDF's A·A has top-right entry i; A has -i. Product and later lines are right.
- **Q14 (printed 134):** the PDF line "A²B(B-I)^{-1}" is garbled (should be A² = B(B-I)^{-1}); the invertibility of B-I and (B-I)^{-1} = A²-I are not justified and are added.
- **Q15 (printed 135):** sign handling in the combined numerator/denominator is not shown (and mixed (a-b)/(b-a) forms); added via x=a-b, y=b-c, z=c-a. Also noted that the value does not depend on α.
- **Q16 (printed 136):** the PDF's alternate layout writes "5, 4, 3, 4, 1"; the fourth should be 2.
Reproduced from the PDF (`pdf`) with small fill-ins of omitted steps: Q1 (off-diagonal entries are zero, x≠y check), Q2 (how the factor 3^6 arises), Q3 (rank 2, check of eq. 2), Q4 (off-diagonal entries left blank in the PDF, quadratic in x²), Q5, Q6 (option-by-option verdicts), Q7-Q11, Q17-Q20.

## Answer key
All printed keys agree with my own computation (sympy / brute force: Q16 = 120, Q11 = 4, Q3 two unit vectors). No key looks wrong. In Q13 the Hindi option list is in a different order from the English one; the English (D) = no solution was used.

## Alternates and results
Alternates for 19 of 20 questions; all 20 have useful_results. Techniques: rows instead of columns of AᵀA=3I (Q1), B=DAᵀD (Q2), cross product of rows (Q3), Cayley-Hamilton A²=xA+I (Q4), adj(adj A)=|A|A (Q5), det A⁵=1 with a=d, b=c (Q6), reconstruct A column by column (Q7), complex-number representation (Q8), skew 3×3 as w× (Q9), determinant of the Cayley transform (Q10), eigenvalues plus option test (Q12), A=iN with N²=2N (Q13), B=I+(A²-I)^{-1} commutes with A² (Q14), numerical substitution (Q15), surjection inclusion-exclusion (Q16), A=D^{-1}KD similarity (Q17), I+N with N²=0 (Q18), commutator sign rule (Q19), roots r,s of the quadratic (Q20).
Weakest alternates (close to the main solution): Q1 (rows instead of columns), Q8 (complex form of the same computation), Q15 and Q16 (substitution / counting reformulation).

## Questions with NO alternate
- **Q11:** a²+2b²+c²=1 in integers is the only route (equivalently sum of squares of the entries); any other view (eigenvalues, trace and determinant) reproduces the same equation, so no genuinely different method was added.

## make_ppt.py warnings
The final build printed no warnings (731 equations converted natively).

## Skipped / assumed
No rendering/thumbnail check was possible (no soffice step). Concepts and marks assumed as above. Q9 / Q19 treat "S1 symmetric" as false because the matrix is skew-symmetric (it is symmetric only in the degenerate case it is zero). Hindi/English duplicate text in the paper was ignored.
