# Determinant: generation report

Blueprint: `qp_blueprints/Determinant.xlsx`. There is no `Determinant_config.xlsx`, so the check ran without `--config`.
This scheduled run generated the paper on 18-Oct-2026 with the `jee-question-paper` skill, way B (blueprint supplied directly).

## Environment
- `xelatex` and `pdftoppm` were already installed.
- pandas, openpyxl, sympy, mpmath and python-docx were missing for `python3`. They were installed with `python3 -m pip install pandas openpyxl sympy mpmath python-docx lxml`.
- The `.sty` files were copied to `~/texmf/tex/latex/local/`.
- The paper title in `meta.json` is "Determinant", and the file names use `Determinant`.
- The first build stopped on one error: in Q20 a `\nu` had been written as a newline character by the question generator. The JSON was fixed and the second build passed with no errors and no warnings. No script was edited and no check was weakened.
- Page 1 of each of the three PDFs was rendered and checked. The Hindi is shaped correctly and the equations (determinants, fractions) are 2D.

## Blueprint check
- **Pattern:** inferred as **JEE Main**, because the paper has only Single Correct and Numerical types and nothing above level 3. The paper name comes from the file name.
- **Paper:** 23 questions: 7 Single Correct (Q1-Q7), then 16 Numerical (Q8-Q23).
- **Reorder (`--reorder`):** the single-correct rows moved to the front. Old -> new:
  80->1, 83->2, 85->3, 86->4, 90->5, 93->6, 95->7, 81->8, 82->9, 84->10, 87->11, 88->12, 89->13, 91->14, 92->15, 94->16, 96->17, 97->18, 98->19, 99->20, 100->21, 101->22, 102->23.
- **Answer Plans:** the blueprint had none, so the script drew all 23:
  Q1 Option C, Q2 Option A, Q3 Option B, Q4 Option D, Q5 Option A, Q6 Option B, Q7 Option D;
  Q8 negative integer, Q9 positive 2-digit integer, Q10 negative decimal, Q11 decimal between 0 and 1, Q12 positive 3-digit integer, Q13 positive decimal,
  Q14 positive decimal, Q15 negative decimal, Q16 positive 2-digit integer, Q17 positive 3-digit integer, Q18 negative integer, Q19 decimal between 0 and 1,
  Q20 negative integer, Q21 negative decimal, Q22 positive 3-digit integer, Q23 decimal between 0 and 1. Every answer matches its plan; the build checks this.
- **Warnings.** These are recorded, not fixed, because the blueprint is your decision:
  - **More than two concepts in a Main row:** Q2 lists 4 concepts (properties, circulant/Vandermonde, trigonometric/logarithmic entries, a row as a linear combination) and Q18 lists 3 (Cramer's rule, parallel disjoint planes, homogeneous systems). All were kept, and every concept is used.
  - **Concepts repeated across rows:** this is expected in a one-chapter paper, and each repeat uses a different mechanism. "Application of properties of determinant" appears in Q1, Q2, Q3, Q8, Q9, Q12 and Q15. "Circulant and Vandermonde" appears in Q2, Q3, Q4 and Q10. "Row as a linear combination" appears in Q1, Q2 and Q5. "Trigonometric or logarithmic entries" appears in Q2, Q11, Q12 and Q13. "Multiplication of determinants" appears in Q14 and Q15. "Cramer's rule" appears in Q6, Q7, Q16, Q17, Q18 and Q20. "Parallel and disjoint planes" appears in Q18, Q19, Q20 and Q21. "Homogeneous systems" appears in Q16, Q18, Q22 and Q23.
  - No cell contained ";". There were no errors. The blueprint file was not edited.

## Answers
Q1 (C) -216, Q2 (A) 6, Q3 (B) 9, Q4 (D) -2, Q5 (A) -1, Q6 (B) -11, Q7 (D) 21,
Q8 -9, Q9 39, Q10 -2.50, Q11 0.25, Q12 324, Q13 3.25, Q14 1.41, Q15 -1.50, Q16 14, Q17 301, Q18 -4, Q19 0.50, Q20 -6, Q21 -3.50, Q22 285, Q23 0.75.

Each answer was recomputed with sympy or mpmath, separately from the hand solution:
- **Symbolic determinants:** Q1 (symbolic b, c), Q4 (roots of the cubic), Q5, Q6 (the full solution in lambda), Q8 (in x, y), Q11, Q13 (identity D = 1 + sum of sin^2), Q15, Q16, Q18, Q22 and Q23.
- **Brute force:** Q3 (n = 1..100), Q7 (all 100 pairs), Q22 (enumeration of t).
- **Q9:** the third-order relation was solved explicitly (basis e^x, e^{2x}, e^{-2x}) and F(log 3) was computed.
- **Q10:** numerical roots of the cubic were used.
- **Q12:** evaluated to 15 digits.
- **Q2:** a dense numerical scan of [0, pi] confirmed exactly six zeros.
- **Q11 and Q13:** grid searches confirmed the maxima 0.25 and 3.25.
- **Q14:** the Gram matrix was checked to be positive definite (so the vectors exist).
- **Q18:** ranks of the coefficient and augmented matrices at k = 1 and k = -5.
- **Q20:** solved all four determinant equations and checked the rank of every solution family.
- **Q21:** the intersection point (8, 5/2, -7/2).
- The only rounded decimal is Q14: sqrt 2 = 1.41421, which is far from a rounding boundary. All other decimals are exact to two places.

## Difficulty
- **Level distribution:** 15 questions at level 2 and 8 at level 3. Every question is rated at its target level, and none is one level off.
- **Marks-weighted index: 2.36** (SCQ 3 marks, Numerical 4 marks). No equivalence-relation or multi-correct adjustments apply. This is a Main-pattern chapter paper, so it is not expected to fall in the Advanced range of 2.6-3.2.
- **Borderline ratings (Medium confidence):**
  - Q6, Q14 and Q20 at level 2 could be read as 1. Q6 is a Cramer quotient with a cancelling factor, Q14 is the Gram identity, and Q20 is the "all determinants zero but no solution" fact.
  - Q7 at level 2 has a counting trap (the z = 0 pairs) and could be read as 3.
  - Q8 and Q23 are the easiest level-3 questions and could be read as 2.
- **Consistency pass:** the hardest level-2 questions (Q7, Q19, Q20) were read next to the easiest level-3 ones (Q8, Q23, Q9), and the order was kept.

## Originality report (per question)
Each mechanism was named before the stem was written and checked against `known_skeletons.md`. None matched, and the build's skeleton lint gave no warning. Every question was web-searched with WebSearch (standard mode); the results are in the table. No near-identical problem was found, so nothing was redesigned for that reason.

| Q | Target | Rated | Mechanism | Web check |
|---|---|---|---|---|
| Q1 | 2 | 2 | the Hankel determinant of P(0..4) for a quadratic P depends only on the leading coefficient; second differences remove b and c (way 4) | not found |
| Q2 | 3 | 3 | a Vandermonde determinant in cos x, cos 2x, cos 3x hidden by the double-angle row; the zeros are the union of three coincidence sets (way 5) | not found |
| Q3 | 2 | 2 | a circulant of n, n+1, n+2 collapses to 9(n+1), so the count becomes a count of perfect squares (way 5) | not found |
| Q4 | 2 | 2 | a circulant containing omega itself, where two eigenvalue factors coincide and give a repeated root (way 4) | ingredient only |
| Q5 | 2 | 2 | the determinant of values of three quadratics at 1, 2, 3 vanishes iff one quadratic is a combination of the other two (way 5) | not found |
| Q6 | 2 | 2 | the limit of a Cramer quotient at the singular parameter; the limit picks one point of the singular system's solution line (way 4) | not found |
| Q7 | 2 | 2 | counting pairs (p, q) for which the Cramer value z = (q-5)/(6-2p) is an integer (way 5) | not found |
| Q8 | 3 | 3 | a Hermitian determinant in z and z-bar that reduces to (1-abs(z)^2)(7-abs(z)^2), then is minimised (way 4) | not found |
| Q9 | 3 | 3 | the determinant of f, g, h and their derivatives, where f, g, h are known only through a common third-order relation; differentiating gives F' = F (way 5) | ingredient only |
| Q10 | 2 | 2 | the ratio of the (0, 2, 3)-power determinant to the Vandermonde determinant is ab+bc+ca, evaluated through Vieta (way 5) | ingredient only |
| Q11 | 2 | 2 | a symmetric trigonometric determinant with a free parameter collapses to lambda sin 2x - lambda^2, which is maximised jointly (way 5) | ingredient only |
| Q12 | 2 | 2 | the rank-one change-of-base matrix with 7 on the diagonal, reduced by row and column scaling (way 4) | ingredient only |
| Q13 | 3 | 3 | I plus a skew-symmetric matrix of sin(angle differences) equals 1 + sum of sin^2, which is bounded with compound angles (way 5) | ingredient only |
| Q14 | 2 | 2 | det M det M^T gives the square of the triple product from six dot products (way 5) | ingredient only |
| Q15 | 2 | 2 | a determinant of (i + jt)^2 that splits as Vandermonde times a scaled determinant, giving -8t^3 (way 4) | not found |
| Q16 | 3 | 3 | the union of the solution lines for both critical lambda, with a lattice minimisation on the lines (way 5) | not found |
| Q17 | 2 | 2 | the remainder of x^6 on division by (x-1)(x-2)(x-3), from the remainder theorem and one Cramer quotient (way 5) | ingredient only |
| Q18 | 3 | 3 | (k-1)I plus a rank-one matrix: parallel disjoint planes at the double root, and a non-zero Cramer determinant at the simple root (way 5) | not found |
| Q19 | 2 | 2 | pairwise disjoint planes fixed by parallel conditions, with an equidistance root that must be rejected, then the distances compared (way 5) | not found |
| Q20 | 2 | 2 | the Cramer failure case: all four determinants zero but no solution forces rank one (way 4) | ingredient only |
| Q21 | 3 | 3 | an inconsistent system of parallel disjoint planes, ranked by distance from the origin, then cut by a line (way 5) | not found |
| Q22 | 2 | 2 | after the homogeneous condition fixes k, lattice points of the solution line t(1,5,7) in a box are counted (way 5) | not found |
| Q23 | 3 | 3 | a determinant with sin and cos swapped factors as (sin - cos)(sin + cos - 1); two solution families in an open interval (way 5) | not found |

**Standard ingredients worth flagging** ("ingredient only" in the table):
- Q4: the circulant factorisation with omega is textbook. A related known problem is IIT 1995, det[[x+1, omega, omega^2], ...] = 0.
- Q9: Abel's identity, W' = -pW, is a university result. The JEE-level route is differentiating a determinant row by row.
- Q10: the generalised Vandermonde / Schur identity. allen.in has det with rows (a,b,c), (a^2,b^2,c^2), (bc,ca,ab).
- Q11: maxima of trigonometric determinants are a common type. Here the parameter is a second variable.
- Q12: the log_x y determinant equal to 0 is standard. Here the diagonal is changed to 7.
- Q13: the bound sin^2 + sin^2 + sin^2 <= 9/4 for angle differences appears in a search result.
- Q14: the Gram identity [a b c]^2 = det of dot products is standard.
- Q17: remainder-by-interpolation is standard. Here Cramer's rule extracts one coefficient.
- Q20: the fact "Delta = Delta_i = 0 can mean no solution (parallel planes)" is a known coaching remark.
- Novelty cannot be guaranteed. Please flag any question you recognise.

## Problems found while verifying
- **Q1:** a first estimate of the value was -4a^3, but sympy gave -8a^3 = -216. The option set uses -108 (= -4a^3) as a distractor.
- **Q16:** the first design had only one admissible lambda and a non-positive direction. It was replaced by a system with two critical values (6 and -2) whose minima differ (30 vs 14), so taking only the positive root is a trap.
- **Q20:** the four determinant equations also have rank-two solution families (lambda = -2, nu = -2; mu = 3, nu = -4/3). Those families have infinitely many solutions, so "no solution" still fixes lambda = -2, mu = 3 uniquely. The value of nu is free, but the answer does not depend on it; the solution says so.
- **Q19:** the equidistance condition gives r/4 = 1 or -1. r/4 = 1 makes P3 coincide with P1, so it is rejected.
- **Full solutions:** the first drafts of Q10, Q18 and Q21 had a garbled line, which was rewritten before the build. In Q10 the expansion of the 2x2 determinant and two values of p(x) were wrong.
- **Q20:** a `\nu` became a newline in the generated JSON. This was fixed after the first build.

## Rows whose concepts were hard to combine naturally
- **Q2** (four concepts): the four concepts are used in one chain. The trigonometric entries give a row that is a linear combination; a row operation (a property) removes it; a Vandermonde factorisation follows. The question asks for a zero count to make the chain matter.
- **Q18** (Cramer, parallel planes, homogeneous systems): "homogeneous" is used for the condition that gives the candidate values of k (Delta = 0), not as a separate system. The stem asks only about the given system.
- **Q16** (Cramer and homogeneous): Cramer's rule appears in its cross-multiplication form for two homogeneous equations, which is how textbooks present the ratio x:y:z.
- **Q14** (Multiplication of determinants alone): the natural home of the multiplication theorem here is the Gram identity, so the question is phrased with vectors.

## Notes
- The Hindi is the assistant's own translation. Please review the specialised terms: पुनरावृत्त मूल (repeated root), अतुच्छ हल (non-trivial solution), संलग्न कोरें (coterminous edges), समान्तर षट्फलक (parallelepiped).
- Q1 and Q5 both use values of quadratics, but the mechanisms differ: a Hankel invariant in Q1, and linear dependence of three polynomials in Q5.
- The stem review is a self-check; an independent reader may still find things.
- `_source/` holds `blueprint.json`, every `qNN.json` and `meta.json`, so a question can be fixed and the paper rebuilt with `build_paper.py`.
