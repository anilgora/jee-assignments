# Run report: JEE_Main_Question_Bank_01_Algebra_05

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_05.pdf` (printed Q81-Q100, renumbered 1-20). Q1-8 Sequence and Series (A.P./G.P./A.G.P. and series), Q9-20 Determinants / linear systems.
Files: `_content.json`, `_Analysis.pptx` (132 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question** - Q1-8 numerical, Q9-20 single correct (JEE Advanced defaults); stated on the section dividers.

## Difficulty
Marks-weighted difficulty index: **1.95** (no equivalence-relation or multi-correct adjustments).
Level 1: 4 questions (Q12, 15, 16, 20). Level 2: 13 questions (Q2, 3, 4, 5, 6, 9, 10, 11, 13, 14, 17, 18, 19). Level 3: 3 questions (Q1, 7, 8). Levels 0, 4, 5: none.
JEE Main-style bank rated on the Advanced scale, so the index is low. Levels were judged against a few anchors (e.g. 2023-P1-Q14, 2025-P1-Q12), not a full anchor comparison per question; Q1, Q7, Q8 are Medium confidence.

## Solutions: corrected / written
No question was `written`. Corrected (answer unchanged):
- **Q1 (printed 81):** the printed statement says only "a1 = b1" (value missing); the PDF's working uses a1 = b1 = 1, now stated in the first bullet. The PDF's step labels are garbled ("(A)-(2)", "(B)-(4)") and it states a9 = 37, b10 = 130 without computing them; the values are supplied.
Reproduced from the PDF (`pdf`) with small fill-ins of omitted steps: Q3 (2800 itself excluded), Q9 (why sin(theta)=0 is rejected), Q10 (why the determinant vanishes for every (r,k)), Q11 (x = 0 rejected), Q12 (the PDF stops at "alpha+beta+2 != 0"; the option check is added), Q13 (other options judged), Q14 (determinant expanded, ratios), Q16 (typo "9xA" read as 9x; expansion terms spelled out), Q17 (other options judged), Q18 (rank/consistency check added; D, Dx, Dy, Dz in the PDF re-verified and correct), Q20 (y = 2z option rejected).

## Answer key
All printed keys agree with my own computation (sympy/brute force: Q1 461, Q2 8, Q3 710 by direct count, Q4 6952, Q5 150, Q6 16, Q7 k = 2, Q8 7; Q9-Q20 options re-derived). No key looks wrong. Q1's statement is incomplete (see above).

## Alternates and results
All 20 questions have one alternate solution and all 20 have useful_results. Techniques: closed forms a_n, b_n with binomials (Q1), shortcut telescoping formula with a_9 = 0 (Q2), periodicity mod 33 (Q3), pairing terms (Q4), A.P. parametrisation of reciprocals (Q5), S - rS method (Q6), quadratic general term with sum formulas (Q7), complete homogeneous sum / Cauchy product of G.P.s (Q8), cross-product direction of two rows (Q9), rank <= 2 of u_i + v_j matrix (Q10), matrix determinant lemma (Q11, Q12), subtract equations to isolate z (Q13), directions from numeric equations first (Q14), numerical option elimination (Q15), roots by equal rows/columns (Q16), row dependency of rows vs right-hand sides (Q17), eliminate x and compare the reduced equations (Q18), multilinearity in columns (Q19), dependency E3 = E1 - 2E2 plus cross product (Q20).
No question lacks an alternate. Weakest (closest to the main solution or more of a check): Q6 (S - rS is the standard AGP technique), Q14, Q15 (numerical elimination), Q2 (shortcut formula).

## make_ppt.py warnings
None (758 equations converted natively; no "could not convert" notes).

## Skipped / assumed
No rendering/thumbnail check was possible (no soffice step). Concepts and marks assumed as above. Q1 assumes a1 = b1 = 1.
