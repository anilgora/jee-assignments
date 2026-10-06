# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_01_01

Paper: 20 questions (printed 1-20, no renumbering needed), all Single Correct Type, Algebra. 128 slides, 882 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.95** (156 / 80 marks; 4 marks each). No equivalence-relation adjustment and no MCQ floor applied (all single-correct).
- Questions per level: Level 1: 4 (Q3, Q7, Q11, Q14) | Level 2: 13 | Level 3: 3 (Q16, Q17, Q20) | other levels: none.
- Medium confidence: Q2, Q6, Q16, Q17, Q20. The rest High.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper): +4 for single-correct questions (JEE Advanced default per the run instructions), 0 otherwise; stated on the section divider.

## Solutions whose source is corrected or written
- Q3 - corrected: the PDF's last line says "A10 = 4a + 2a" (typo); correct value 4a + 2b. Also added the cofactor-sign step. Answer (A) unchanged.
- Q13 - corrected: PDF's last line reads "x^2 - 195x + 95x + 9506 = 0" (slip); correct is x^2 - 195x + 9506 = 0. Answer (C) unchanged.
- Q15 - corrected: PDF says "8 + 2n must be a complete square"; it should be 4 + n (roots -2 +- sqrt(4+n)). Its following lines already use 4 + n. Answer 6 unchanged.
- Q16 - corrected (gap): the PDF stops at |A| = 6 and states 216 without the final step; added det(AB) = |A|*|B| with |B| = |A|^2. Answer 216 unchanged.
- No question was `written`. Other 16 questions: source pdf (Q17 has a harmless typo in the PDF, "P12 and P12" for "P11 and P12"; the working itself is right).

## Answer key
All 20 printed answers verified (sympy / numerics: linear system, determinants, A^50, root counts, d = 6, cofactor matrix, power-sum values, Newton identity numeric check, etc.). No answer key is wrong.

## Alternates
Alternates given for 19 of 20 questions (Q2-Q20); Q10 has two.
Honest notes on strength: Q4 (re-centre at x = 1 and track the constant term), Q9 (list the terms, use 5d), Q14 (count roots by discriminant/Vieta) and Q19 (middle-term rule) are lighter variants rather than radically different methods; the others use clearly different ideas (block matrix for Q6, convexity/evenness for Q7, componendo-dividendo for Q8, orthonormal rows for Q10, adjoint identity A*adj(A) = |A|I for Q16, root identity for Q17, y1+y4 = y2+y3 for Q20).
Questions with NO alternate:
- Q1 - the only routes are elimination, Cramer's rule or expressing the target equation as a combination of the rows (coefficients -39/71, -5/71, -49/71: uglier than direct elimination); no genuinely different, elegant method exists.

## Useful Result / Pattern
All 20 questions have a useful_results slide (3-4 bullets each); formulas spot-checked numerically (power sums, Newton relation, remainder of x^5, cofactor determinant, A^50).

## make_ppt.py warnings
None printed (only the note "882 converted to native PowerPoint equations"). No "could not convert" messages. Slides were not rendered (no soffice/thumbnails in this environment).

## Skipped / assumed / guessed
- Concepts and levels self-assigned; nearest anchors cited in the ratings file are approximate (closest chapters in anchors.md).
- Page text extracted with pdftotext; garbled maths checked against page images (all 15 pages viewed).
- Q6: the given recurrence A^n = A^(n-2) + A^2 - I was checked at n = 3 and A^50 computed directly (same result).
- Excel report was built with build_report.py; recalc step skipped (no /mnt/skills), so formula cells have no cached values.
