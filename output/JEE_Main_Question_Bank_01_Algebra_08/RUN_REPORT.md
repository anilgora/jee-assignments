# Run report: JEE_Main_Question_Bank_01_Algebra_08

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_08.pdf` (printed Q141-Q160, renumbered 1-20), all Matrices and Determinants.
Files: `_content.json`, `_Analysis.pptx` (123 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question** (JEE Advanced default): Q1-Q13 single correct, Q14-Q20 numerical (the PDF gives no options for printed Q154-Q160). Stated on the section dividers.

## Difficulty
Marks-weighted difficulty index: **2.00** (no equivalence-relation or multi-correct adjustments).
Level 0: 1 question (Q11). Level 1: 2 (Q3, Q7). Level 2: 13 (Q1, 2, 4, 5, 6, 9, 12, 13, 15-19). Level 3: 4 (Q8, Q10, Q14, Q20). Levels 4 and 5: none.
JEE Main-style bank rated on the Advanced scale, so the index is low. Medium confidence: Q1, Q2, Q8, Q9, Q10, Q14, Q17-Q20.

## Solutions: corrected / written
No question was `written`. Corrected:
- **Q7 (printed 147):** as printed A has the scalar 1/(5!6!7!) in front of a 3x3 matrix, so |A| = 2/(5!6!7!)^2, not 2. The PDF takes |A| = 2 (factorials removed from the rows cancel the scalar, i.e. the original is a determinant expression). I kept that intended reading and the key 2^16, and said so in the notes.
- **Q8 (printed 148):** the combined fraction for |A||A-I| is mistyped, and case 2 is labelled 2(1-a)^3 = -a although its quadratic comes from the square. Fixed; answer 5/2 unchanged.
- **Q14 (printed 154):** cofactor C32 printed as -(3a+6); the correct minor is 3a+4, so C32 = -(3a+4). With 3a+6 one would get a = -7/3. Corrected value gives a = -1, answer 17.
- **Q16 (printed 156):** first factor of A^2 shows 3 instead of 2 in the (2,2) place; the equation is printed with 2A^19 instead of aA^19. Answer 4 unchanged.
- **Q17 (printed 157):** the (1,2) entry of A^10 - (adj 2A)^10 is printed 2^11 x 1023; it is 1023 x 1025. The first column is zero anyway, so det = 0 and the answer 16 stand.
- **Q18 (printed 158):** the PDF jumps to k = 1 with no working; I added the factorisation (k-1) b2 [2 b1 + (k+1) b2] = 0.
- **Q19 (printed 159):** the PDF's A-I has last row (0, -w, -w), i.e. a33 = 1-w, but the question prints a33 = w+1. Working and key 36 are kept for a33 = 1-w.
Reproduced from the PDF (`pdf`) with small fill-ins of omitted steps: Q1-Q6, Q9-Q13, Q15, Q20 (e.g. the division by d in Q2, why the four multisets in Q20, the 1/2 and square-root steps in Q3-Q5, the check of C32 sign in Q14).

## Answer key
All printed keys match my own computation (sympy / brute force: Q9 = 31 singular of 81, Q10 sum 100, Q16 a=-2 b=2, Q17 det 0, Q20 = 766), but three keys hold only under a reading different from the printed text:
- **Q7:** key 2^16 holds only if |A| = 2 is intended (see above); as printed the answer is 2^16/(5!6!7!)^8, which is not an option.
- **Q18:** as printed, (k^2+1) b2^2 != -2 b1 b2 does not exclude the second factor, so k is not unique (any k other than 0, 1 is possible for a suitable B). With the intended (k+1) b2^2 != -2 b1 b2 the key k = 1 is exact.
- **Q19:** as printed (a33 = w+1) alpha = (7 - i sqrt3)^2 = 46 - 14 sqrt3 i (about 46 - 24.2 i), not 36. Key 36 is right for a33 = 1-w.
- **Q15:** the data are inconsistent for real x, y, z (sum x^2 = 1 and xyz = 2 contradict AM-GM; t^3 - t^2 - 2 has one real root). The key 7 is the intended algebraic value; a remark bullet is on the slide.

## Alternates and results
Alternates for 17 of 20 questions; all 20 have useful_results. Techniques: rotated row pair (x,y),(-y,x) with x^2+y^2 = 5 (Q1), adj A = (tr A)I - A closed form (Q2), S = P+I with S^T = aS (Q3), eigenvalues of an idempotent / rank = trace (Q4), Cayley-Hamilton (Q5), Fibonacci coefficients of powers (Q6), Vandermonde via C3-C2 (Q7), symmetric/skew split (Q8), dependent column pairs (Q9), entry sum u^T X u (Q10), adj(adj X) = |X|^(k-2) X (Q13), solving Pq = k e3 column-wise (Q14), circulant determinant sign (Q15), eigenvalue test of a polynomial identity (Q16), common eigenvector for A and adj(2A) (Q17), R2+R1 shortcut (Q19), row-by-row convolution count (Q20).
Weakest alternates (close to the main solution): Q6 (Fibonacci form of the same reduction, but it gives the answer by adding/subtracting two numbers), Q13 (same exponent bookkeeping through a different identity), Q19 (only a computational shortcut for the determinant), Q20 (same cases counted in a different order).

## Questions with NO alternate
- **Q11:** counting free entries of a symmetric matrix is the only route; there is no other view.
- **Q12:** after |adj A| = |A|^2 gives alpha = 4, the quadratic form is a single evaluation; any other order of multiplication is the same arithmetic.
- **Q18:** the only route is expanding and factoring the quadratic form; the "X is a scaled orthogonal matrix" view needs the identity for all B, which the question does not give.

## make_ppt.py warnings
The final build printed no warnings (816 equations converted natively).

## Skipped / assumed
No rendering/thumbnail check was possible (no soffice step). Concepts and marks assumed as above. Hindi/English duplicate text in the paper was ignored. Printed Q157 and Q158 have no options in the PDF, so they were treated as numerical. Level ratings were judged against the rubric and a few anchors, not a full anchor comparison per question.
