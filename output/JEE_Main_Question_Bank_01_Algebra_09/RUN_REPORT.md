# Run report: JEE_Main_Question_Bank_01_Algebra_09

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_09.pdf` (printed Q161-Q180, renumbered 1-20). Q1-Q4 Matrices and Determinants; Q5-Q20 Permutations and Combinations (Q13 is a series limit).
Files: `_content.json`, `_Analysis.pptx` (119 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question** (JEE Advanced default for single-correct and numerical). Q1-Q4 have no options, so they are Numerical Type; Q5-Q20 are Single Correct. Stated on the section dividers.

## Difficulty
Marks-weighted difficulty index: **1.65** (all marks equal; no equivalence-relation or multi-correct adjustments).
Level 0: 1 question (Q14). Level 1: 7 (Q1, 6, 7, 8, 9, 10, 19). Level 2: 10 (Q2, 3, 5, 11, 12, 13, 15, 16, 17, 20). Level 3: 2 (Q4, Q18). Levels 4 and 5: none.
A JEE Main-style bank rated on the Advanced scale, so the index is low. Medium confidence: Q2, 3, 4, 5, 11, 12, 13, 15, 16, 17, 18, 20.

## Solutions: corrected / written
No question was `written`. Corrected:
- **Q3 (printed 163):** the sum = 7 line reads C(8,5) - 4 = 52 (copied from the sum = 5 case). Correct value is C(10,3) - 4*C(5,3) = 80. The PDF's total (20+52+80+52 = 204) already uses 80, so the answer 204 stands.
- **Q4 (printed 164):** the PDF writes "a + 1 + 3(-3/2a) = 1"; the right side must be 0. The next line and the quadratic 2a^2 + 2a - 9 = 0 are right, answer 2 unchanged (A^3 = A verified symbolically).
- **Q6 (printed 166):** first term printed as 494; 9 x 66 = 594. Sum 594 + 432 + 108 = 1134 is correct.
Reproduced from the PDF (`pdf`) with fill-ins of omitted steps: Q1, Q2, Q5, Q7-Q20 (e.g. the algebra between lines in Q2, the explicit case list in Q11 and Q12, the factorisation behind the telescoping in Q13, why O and A/B/C cases are exhaustive in Q14, the block sizes 24/12/12/12 in Q15, the partition list by number of parts in Q19, the table of 8Ck in Q20).

## Answer key
All printed keys match my own computation (sympy / brute force: Q3 = 204, Q4 root 1.679, Q11 = 4607, Q12 = 161, Q15 = OBBJH, Q17 = 179, Q19 = 15, Q20 = 372). No wrong key.
Q5 note: the figure is not machine-readable; the box rows (3, 3, 2) were taken from the PDF's own solution table. The deck says so in the question text.

## Alternates and results
Alternates for 18 of 20 questions; all 20 have useful_results. Techniques: singular left factor so row 2 = 3/2 row 1 (Q1), Adj(Adj X) = |X|^(n-2) X (Q2), pair-sum weights w(u) and symmetry s <-> 16-s (Q3), characteristic polynomial lambda^3 - lambda (Q4), complement over row-empty cases (Q5), collinear complement (Q6), 11C8 minus one bad case (Q7), gap method (Q9), complement of end-digit pairs (Q11), shifted stars and bars (Q12), e-series tails (Q13), side-wise direct count (Q14), option elimination by block ranks (Q15), choose A then B (Q16), generating function (1+x)^5(1+x+x^2)^3 (Q17), multinomial-as-arrangements view (Q18), conjugate partitions (Q19), unimodal row of 8Ck and nPr ratio shortcut (Q20).
Weakest alternates (close to the main solution): Q11 (complement of the same pair count), Q14 (direct count vs complement, same data), Q16 (sequential choice is the same arithmetic as 9!/(3!)^3), Q18 (same integrality claim read as a multinomial), Q20 (the shortcut uses the same two identities).

## Questions with NO alternate
- **Q8:** the count C(12,2)C(13,2) is a single step; every other view (summing over the middle letter, etc.) is the same count.
- **Q10:** the three cases follow from the quota constraints; the only other route (splitting by boys) gives the same three cases.

## make_ppt.py warnings
First build: "Q14: only 3 solution bullets" - fixed by adding the two explanatory steps (18 points in all; only same-side triples are collinear). Final build printed no warnings (602 equations converted natively).

## Skipped / assumed
No rendering/thumbnail check was possible (no soffice step). Concepts and marks assumed as above. Hindi/English duplicate text was ignored. Levels were judged against the rubric and a few anchors, not a full anchor comparison per question; anchor citations are approximate.
