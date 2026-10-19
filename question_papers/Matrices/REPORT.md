# Matrices: generation report

Blueprint: `qp_blueprints/Matrices.xlsx`. There is no `Matrices_config.xlsx`, so the check ran without `--config`.
This scheduled run made the paper on 19-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy and mpmath were missing for `python3`. I installed them with `python3 -m pip install pandas openpyxl sympy mpmath`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- `build_paper.py --blueprint` passed with **no errors and no warnings**. No script was edited and no check was weakened.
- I rendered and looked at:
  - page 1 of each of the three PDFs;
  - page 9 of the full-solutions PDF;
  - the Q28 page of the shortened-solutions PDF (augmented matrix `[A | I]`).

  The Hindi is shaped, and matrices, fractions and limits are 2D. This paper has no paragraph question.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the blueprint has only Single Correct and Numerical types and nothing above level 3.
- **Paper:** 29 questions: 6 Single Correct (Q1-Q6), then 23 Numerical (Q7-Q29).
- **Reorder (`--reorder`), old -> new:**
  111->1, 113->2, 117->3, 122->4, 126->5, 127->6, 103->7, 104->8, 105->9, 106->10,
  107->11, 108->12, 109->13, 110->14, 112->15, 114->16, 115->17, 116->18, 118->19, 119->20,
  120->21, 121->22, 123->23, 124->24, 125->25, 128->26, 129->27, 130->28, 131->29.
- **Answer Plans:** the blueprint had none, so the script drew all 29. Every answer matches its plan; the build checks this.
  - SCQ letters: Q1 C, Q2 A, Q3 B, Q4 D, Q5 A, Q6 B.
  - Numerical styles: Q7 negative integer, Q8 2-digit, Q9 negative decimal, Q10 (0,1), Q11 3-digit, Q12 positive decimal, Q13 positive decimal, Q14 negative decimal, Q15 2-digit, Q16 3-digit, Q17 negative integer, Q18 (0,1), Q19 negative integer, Q20 negative decimal, Q21 3-digit, Q22 (0,1), Q23 positive decimal, Q24 2-digit, Q25 positive decimal, Q26 negative decimal, Q27 negative integer, Q28 2-digit, Q29 (0,1).
- **Cells containing ";":** none.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision. There were no errors, and the blueprint file was not edited.
  - **More than two concepts in a Main-pattern row** (the Main pattern normally has at most two). Every concept is used.
    - Q1: 3 concepts.
    - Q6: 3 concepts.
    - Q14: 3 concepts.
    - Q16: 4 concepts.
    - Q17: 3 concepts.
  - **Concepts repeated across rows.** Each use has a different mechanism.
    - "Higher integral powers": Q1, Q10, Q11, Q12, Q13, Q14, Q18.
    - Cayley-Hamilton (both wordings): Q2, Q15, Q16, Q17.
    - "Inverse of a square matrix": Q6, Q16, Q17, Q26, Q27.
    - "Adjoint": Q2, Q5, Q6.
    - "Application of properties of determinant": Q5, Q6, Q27.
    - "Orthogonal": Q3, Q8, Q19.
    - "De Moivre": Q1, Q12, Q22.
    - "Transformations": Q1, Q22.
    - "Special types": Q7, Q8.
    - "Matrix multiplication": Q7, Q9.
    - "Transpose": Q3, Q9.
    - "Pattern/induction": Q10, Q14.
    - "A = I + N": Q11, Q14.
    - "Special powers": Q16, Q18.
    - "Trace": Q20, Q21.
    - "Homogeneous system": Q4, Q23.
    - "System of linear equations": Q23, Q29.
    - "Symmetric/skew": Q21, Q24.
    - "Counting matrices": Q24, Q25.
    - "Elementary operations": Q26, Q28.
  - **Concept text with a stray `$`.** One concept name in the blueprint contains a stray `$`: "Cayley-Hamilton Theorem & Characteristic Equation: Calculating higher powers A^n$ and inverse A^{-1}." It was copied exactly as given. You may want to fix it in the blueprint.

## Answers
| Q | Answer | Q | Answer | Q | Answer |
|---|---|---|---|---|---|
| 1 | (C) 5 | 11 | 283 | 21 | 400 |
| 2 | (A) (-6, 11) | 12 | 1.73 (√3) | 22 | 0.25 |
| 3 | (B) 12 | 13 | 3.50 | 23 | 2.75 |
| 4 | (D) {0, 14} | 14 | -0.18 | 24 | 84 |
| 5 | (A) 702 | 15 | 40 | 25 | 10.50 |
| 6 | (B) 20 | 16 | 363 | 26 | -1.50 |
| 7 | -18 | 17 | -9 | 27 | -6 |
| 8 | 20 | 18 | 0.60 | 28 | 21 |
| 9 | -0.25 | 19 | -89 | 29 | 0.48 |
| 10 | 0.80 | 20 | -3.50 | | |

Q12 is the only answer that is not exact to two decimals. It is √3 = 1.7320…, so the rounding is unambiguous.

## How the answers were checked
I designed every mechanism and its numbers myself. Each answer was then recomputed with sympy (exact) or mpmath:
- **Brute force:**
  - Q8: all symmetric matrices with entries in {-1, 0, 1}.
  - Q24: all 3^6 symmetric matrices.
  - Q25: all 2^9 0-1 matrices.
- **Solved directly:**
  - Q7: all 8 upper triangular square roots were solved exactly and listed.
  - Q26: the reconstructed A was checked by applying operations (i)-(v) to it, which gives I.
- **Answers that must not depend on the choice of matrix:**
  - Q2: the answer was checked on two different matrices with the stated traces.
  - Q16: checked on three different matrices with trace 0 and determinant -1.
  - Q17: checked on two different matrices with eigenvalues 1, -1, 2.
- **Data that must be consistent:** for Q20 and Q21 an explicit matrix pair satisfying the data was exhibited. It is written in the full solution.
- **Limits:**
  - Q10 and Q18: closed forms checked, and Q18 at n = 80.
  - Q13: partial sum to 200 terms.
  - Q22: the nine points evaluated directly at 30 digits.

## Originality report
I named a mechanism for each question and checked it against `known_skeletons.md`, and none matches. Every question was web-searched (WebSearch, standard mode), and the result is recorded per question. Novelty cannot be guaranteed. Many rows of this blueprint ask for standard textbook skills, such as elementary-row-operation inverses (Q28), Cayley-Hamilton reductions (Q15) and infinite-solution systems (Q23), so the novelty there lies in the numbers and the combination, not the method. Please name any question you recognise.

| Q | Mechanism | Web check |
|---|---|---|
| 1 | two reflection matrices in lines at pi/8 and pi/3 compose to a rotation through 5 pi/12, and the count of n <= 60 with (QP)^n + (PQ)^n = I reduces to a congruence 5n = +-4 (mod 24) (way 5) | ingredient only |
| 2 | the characteristic polynomial is not given; it is rebuilt from tr A, tr A^2 and det A (power sums to elementary sums), and the adjugate is then read from Cayley-Hamilton (way 5) | ingredient only |
| 3 | the sum of squares of the entries of Q X^T Q^T is shown to be independent of the orthogonal Q by writing it as tr(M^T M) (way 4, hidden invariant) | ingredient only |
| 4 | the coefficient matrix is lambda I minus a rank-one matrix with rows in ratio 1:2:3, so the determinant collapses to lambda^2(14 - lambda) and the double root lambda = 0 is the trap (way 4) | ingredient only |
| 5 | the entries of the cyclic determinant are the roots of a given cubic, so the value comes from Vieta (with ab + bc + ca = 0), and the adjugate step turns the negative determinant into a positive square (way 5) | ingredient only |
| 6 | the sum of the entries of adj(A) for a Vandermonde matrix is obtained without cofactors, from A e1 = (1,1,1)^T, which makes the entries of A^{-1} add up to 1 (way 4, hidden invariant) | ingredient only |
| 7 | all eight upper triangular square roots of a fixed triangular matrix are found and an extremal entry sum is asked; the minimum is not at the all-negative diagonal (way 3, a family fixed by two conditions) | found: redesigned |
| 8 | integer orthogonal matrices are signed permutation matrices, and the symmetric ones correspond to involutions with matching signs (way 5) | ingredient only |
| 9 | the inverse of the transpose of a rank-one update I + u v^T is found by associativity, using that u^T v is a scalar (way 5) | ingredient only |
| 10 | a ratio of two matrix invariants (trace and entry sum) of A^n is taken to the limit, so the closed form of A^n by induction is needed (way 5) | not found |
| 11 | the nilpotent part is hidden in a non-triangular integer matrix (A - I has trace 0 and N^3 = O but no zero pattern), so the student must test A - I before expanding (way 4) | ingredient only |
| 12 | the ratio of two entries of A^2026 is asked, so only the angle 2026 pi/3 matters and the large factor 2^2026 cancels (way 5) | ingredient only |
| 13 | a matrix series I + A + A^2 + ... in which A^2 is a scalar matrix, so the series splits into two scalar GPs multiplying I and A (way 4, hidden structure) | ingredient only |
| 14 | an inverse problem for matrix powers: A^10 is given and the entries of A are recovered; the (1,3) entry couples b with the C(10,2) a^2 term (way 3, the matrix is fixed by a condition on its power) | not found |
| 15 | a power and the inverse are combined in one linear expression, so Cayley-Hamilton must be used both upwards (A^4) and downwards (A^{-1}) (way 5) | ingredient only |
| 16 | A is known only through its trace and determinant; Cayley-Hamilton shows A is involutory, and then a power and the inverse of A + 2I are expressed in the basis I, A (way 3, an object fixed by two conditions) | ingredient only |
| 17 | A is given only through three singular shifts A - kI; the inverse is turned into a polynomial in A by Cayley-Hamilton and the determinant of a matrix polynomial is read from the eigenvalues (way 3) | ingredient only |
| 18 | the powers of a matrix that is a combination of I and a hidden idempotent are found by collapsing the binomial expansion, and a limit of an entry is asked (way 4) | ingredient only |
| 19 | two orthogonal matrices are known only by their first columns and determinant; the product B^T C is read as a rotation through beta - alpha, so the entries come from compound angles with Pythagorean triples 3-4-5 and 5-12-13 (way 5) | not found |
| 20 | only traces of squares are given for two non-commuting matrices, and the trace of a different mixed product is asked; the cross terms combine only because tr(AB) = tr(BA) (way 4, a hidden invariant) | not found |
| 21 | the two traces tr(A^2) and tr(AA^T) separate the symmetric and skew parts of an unknown matrix, giving the size of A - A^T without knowing A (way 4, a hidden invariant) | not found |
| 22 | the mean of the squared x-coordinates of the nine images of a point under the powers of a rotation matrix; it equals half the squared distance from the origin because the sum of the 9th roots of unity is zero (way 4, hidden invariant) | not found |
| 23 | both parameters are fixed by 'infinitely many solutions', the first through the homogeneous system (k = 7/4, a fraction) and the second through consistency (beta = 1) (way 3) | not found |
| 24 | a trace condition on A^2 is turned into a weighted count of non-zero entries (diagonal weight 1, off-diagonal pairs weight 2) by symmetry (way 5) | ingredient only |
| 25 | a ratio of an unrestricted count to a symmetric count of 0-1 matrices with a fixed number of 1s; the symmetric count is a selection of diagonal places and off-diagonal pairs under d + 2p = 4 (way 5) | ingredient only |
| 26 | the matrix is not given; only the Gauss-Jordan sequence that reduces it to I is given, and A must be rebuilt by inverting the elementary operations in reverse order (way 5) | ingredient only |
| 27 | the inverse of the 'min(i,j)' matrix is obtained from the row-difference operations that reduce it to an all-ones triangular matrix, and the off-diagonal sum of the inverse is asked (way 4, hidden structure M = U^T U) | ingredient only |
| 28 | a symmetric tridiagonal matrix with determinant 1 is chosen so that the inverse has integer entries and Gauss-Jordan stays exact (way 5, single routine concept) | ingredient only |
| 29 | the parameters of a three-plane system are fixed by 'infinitely many solutions', and the resulting common line is then used geometrically (foot of the perpendicular from the origin), which turns out to be the point of L in the plane z = 0 (way 5) | not found |
Notes on the web checks:
- **Q7 was redesigned.** The first version used a triangular matrix with diagonal 1, 4, 9. The search found a qualifying-exam exercise asking for a square root of a similar 1, 4, 9 upper triangular matrix. I changed N to diagonal 4, 1, 9 with new off-diagonal entries before writing the question.
- **Q8:** nearest is 2025-P1-Q4 (integer orthogonal matrices commuting with a diagonal matrix).
- **Q25:** nearest is JEE Advanced 2009 (symmetric 0-1 matrices with five 1s).
- **Q27:** uses the "min(i,j) matrix", whose tridiagonal inverse is known in linear-algebra texts. It is not a JEE skeleton.

## Difficulty (calibrated scale)
- **Levels:** L2: 13 questions; L3: 16 questions.
  - L2: Q2, Q3, Q4, Q9, Q10, Q12, Q15, Q18, Q19, Q20, Q21, Q23, Q28.
  - L3: Q1, Q5, Q6, Q7, Q8, Q11, Q13, Q14, Q16, Q17, Q22, Q24, Q25, Q26, Q27, Q29.
- **On target:** every question is at its target level; no question is one level off.
- **Weighted index:** about **2.55** (build script, JEE Advanced default marks). This is a chapter paper in the Main pattern, so there is no expected official range. No question carries the equivalence-relation adjustment or the MCQ floor.
- **Consistency pass:** the levels were sorted and neighbours compared. The closest calls are Q14 (inverse problem for A^10) and Q25 (ratio of two counts). Both are rated L3 with **Medium** confidence, and a reviewer could place them at L2. On the L2 side, Q20 and Q21 (trace identities) are the hardest. They stay at L2 because each is a routine chain of standard trace facts.
- **Confidence:** High for Q10, Q11, Q15, Q18 and Q28; Medium for the rest. No question has Low confidence.

## Problems found while verifying
- Q7: redesigned after the web check (see above).
- Q11: the first nilpotent candidate came from a non-unimodular change of basis and had fractional entries. It was replaced by an integer N found by search, with N³ = O, N² ≠ O and trace 0.
- Q19: "each with determinant 1" was added to the stem. Without it, the second columns of B and C, and so the answer, are not unique.
- Q20: the data were changed so that its answer (-3.50) does not repeat Q26's (-1.50).
- Q26: the first row-operation sequence gave an integer entry sum, so a sequence was chosen whose sum is a negative decimal, as planned. The order of the inverse operations is spelled out in the full solution.

## Rows whose concepts were hard to combine
- **Q10** (powers + pattern/induction): both concepts are about matrix powers, so the question uses one 2x2 power formula. The "decimal between 0 and 1" plan was met by the limit of trace/entry-sum (0.8).
- **Q13** (powers + GP): the GP enters as the matrix series I + A + A² + …, which splits into two scalar GPs because A² = I/8.
- **Q16** (four concepts): all four are used. Cayley-Hamilton makes A involutory, and that gives the powers and the inverse of A + 2I. The combination is natural, but the stem has to ask for one coefficient (p) of a combined expression.
- **Q29** (system + plane): the link is that the common line of the three planes exists only for the parameter values found from the system. The foot of the perpendicular then happens to be the z = 0 point of the line, which simplifies the ending.

## Notes
- The stem review is a self-check; an independent reader may still find things.
- The Hindi is my own translation. Please review the specialised terms, for example:
  - लांबिक (orthogonal) in Q19;
  - अतुच्छ हल (non-trivial solution) in Q4;
  - उपरि त्रिभुजीय (upper triangular) in Q7;
  - अनुरेख (trace) in Q2, Q16, Q20, Q21 and Q24.
