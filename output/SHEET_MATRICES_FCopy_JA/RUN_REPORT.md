# Run report - SHEET_MATRICES_FCopy_JA

Paper: Exercise J-A (Matrices, JEE Advanced previous-year questions 2012-2026), 33 questions (Q1-33, numbered as in the PDF). The PDF has answers and solutions. Date of run: 2026-10-14. Deck: 219 slides.

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper; stated in the section dividers): single-correct, one-or-more-correct and numerical questions 4 marks each; matching (Q29) 3 marks. Total 131. Types taken from the wording: Q1, 2, 9, 11, 15, 25, 30, 32 single correct; Q3-8, 10, 13, 16-18, 20, 22, 23, 26, 31, 33 one or more correct; Q12, 14, 19, 21, 24, 27, 28 numerical; Q29 matching. Sections are the exam years (JEE 2012-13, 2014-16, 2017-18, 2019, 2020-22, 2023-24, 2025-26).

## Difficulty
Marks-weighted difficulty index (adjusted): **2.66** (inside the official JEE Advanced range 2.6-3.2, near its lower end).
Level counts (adjusted levels): L1 = 4 (Q1, 2, 3, 32), L2 = 8 (Q7, 9, 11, 12, 20, 21, 25, 29), L2.5 = 3 (Q4, 6, 22), L3 = 13 (Q5, 8, 10, 13, 15, 16, 17, 18, 19, 23, 24, 26, 33), L4 = 4 (Q14, 28, 30, 31), L5 = 1 (Q27), L0 = 0.
MCQ floor 2.5 applied (multi_concept flagged) to Q4, Q6, Q22 (base level 2). No equivalence-relation adjustment. Where the question is an official JEE Advanced question that is in the anchor bank, the user's own level was used: Q22 (2021-P1-Q11, 2), Q23 (2021-P1-Q14, 3), Q26 (2023-P2-Q5, 3), Q27 (2023-P2-Q12, 5), Q28 (2024-P1-Q10, 4), Q29 (2024-P1-Q14, 2), Q30 (2025-P1-Q4, 4), Q31 (2025-P2-Q5, 4), Q32 (2026-P1-Q3, 1), Q33 (2026-P1-Q8, 3). Medium-confidence ratings: Q5, 8, 10, 13, 14, 15, 17, 18, 19, 20, 24 (the rest High). Q24 has no exact anchor (JEE Advanced 2022 is not in the bank).

## Solutions whose solution_source is "corrected" (11) or "written" (1)
- Q7 (corrected): the PDF works out only options (C) and (D); (A) and (B) were never examined. Added (both are symmetric, not skew, with a counterexample).
- Q8 (corrected): cofactor typo, PDF has -(3a+24)/(12a+20); correct cofactor is -(3a+4) (24 would not give a = -1). Verdicts for (A), (B) and the contrast of (D) with 2^13 were added.
- Q10 (corrected): the PDF stops at "|A^2| = |A|^2 >= 0. Now check option" and never checks options; (C) needs an explicit square root (90-degree rotation). Added.
- Q12 (corrected): PDF states Delta = 0 => a = +-1 and then the verdicts with no working; added the expansion (1-a^2)^2 and the substitution of both roots.
- Q13 (corrected): PDF says "option (D) ... option (B) is correct" (means D) and, for (B), gets the condition -b1-b2+3b3 = 0 (mis-copied determinant); correct condition is b1+b2+3b3 = 0 (left null vector (1,1,3)). Conclusion (B incorrect) unchanged.
- Q14 (written): the PDF's solution is a copy of the Q12 solution (alpha = +-1 determinant); written afresh (vertex argument + mod-4 structure, example matrix of determinant 4).
- Q17 (corrected): typo 40 - x^2 + 8 should be 40 - 4x^2 + 8 = 48 - 4x^2; (D) "not possible" had no reason (the (1,2) entry of PQ - QP is 2). Added.
- Q19 (corrected): the PDF jumps from the determinant to n(n+1)2^(n-2)...; none of the four binomial sums is evaluated and the identity C(n,k)/(k+1) = C(n+1,k+1)/(n+1) is not stated. Added.
- Q20 (corrected): option (A) is never addressed (needs a counterexample, e.g. diag(1,-1,-1)); the formula adj(adj M) = |M| M is quoted without proof. Added.
- Q23 (corrected): sign slip in the expansion for (D): PDF writes -FE.FGE, the expansion gives +FE.FGE; final I - 2FE and verdict are right. Fixed and a counterexample (E = F = I/2) added.
- Q29 (corrected): (R) argued "|M| = 0 so infinite solutions" - not valid (system could be inconsistent); explicit one-parameter family added. Also the claim that a zero-sum row is a permutation of (1, alpha, beta) is now proved (rational and sqrt5 parts).
- Q33 (corrected): for (A) the PDF says a repeated eigenvalue gives similarity to [[1,1],[0,1]]; false in general (M = I). Replaced by M != I and (M-I)^2 = 0 with an explicit N. Signs lost in the PDF text layer (b = -351, d = -325, q = -26, s = -25) were restored from M^k = [[1+k, -k],[k, 1-k]].
Questions with solution_source "written": Q14 only (see above). All other questions are "pdf" (working reproduced; for Q4, Q5, Q9, Q11, Q15, Q16, Q18, Q21, Q22, Q24-28, Q30-32 it was verified step by step).

## Answer key / question problems
- No printed answer disagrees with the correct answer. Every final answer was re-derived by computation (sympy / brute force): Q3 (both +-2 realised), Q8, Q9, Q11, Q12 (symbolic), Q13 (rank / left null vector), Q14 (brute force over all 3^9 matrices), Q15, Q16, Q17, Q18, Q19, Q22, Q24, Q25, Q26, Q27 (4096 matrices: 3780), Q28 (32 matrices: 16), Q29 (3^9 matrices: P = 12, Q = 6, S = 0), Q30 (brute force: 16), Q31, Q32, Q33.
- Q14: the PDF's solution belongs to Q12 (answer 4 itself is right).
- Q23, Q29 and Q33: the English wording of the options in the PDF is correct; in the Hindi text of Q22(B) "PEQ^-1" appears where "PFQ^-1" is meant (English is right, used).

## Alternate solutions
Alternates (a genuinely different technique) were written for 31 of 33 questions: Q1-6, 8-19, 21-33. Each was verified against the answer (hand check and, where numerical, by computation: Q3 explicit P = +-2A^-1, Q4 counterexamples, Q5 example N = diag(1,2,3), Q8 adj Q, Q9 Toeplitz/power series, Q10, Q12 elimination, Q15 entrywise, Q23 push-through (random matrices), Q24 Cayley-Hamilton, Q25 Cayley-Hamilton, Q26 characteristic polynomial, Q28 complement count, Q33).
Weaker alternates, worth a look: Q1 (matrix-product view of the same scaling), Q6 (logical observation that (A) and (B) are one statement), Q13 and Q16 (a geometric / identity view of the same facts), Q33 (shortcut through the structure of the sum).
Questions with NO alternate (2), and why:
- Q7: transposition reverses products and odd powers of a skew matrix are skew; every route (sign counting, parity rule, trial matrices) is the same transposition argument (trial matrices could only refute (A) and (B), not prove (C) and (D)).
- Q20: M^-1 = |M| M and the determinant of both sides is the only route; the eigenvalue rewording is the same identity.

## Useful Result / Pattern
Every question (1-33) has useful_results (3-4 general statements each, with conditions; formulas spot-checked on numerical cases).

## make_ppt.py output
- "Q12: solution_source is 'corrected' but correction_note is empty" (first build): fixed by adding the note.
- "Q29: very long question - font reduced to 20 pt": harmless (the paragraph with List-I and List-II is long); left as is.
- No "could not convert" warnings: all 1380 equations became native PowerPoint equations.

## Skipped, assumed or guessed
- No rendering or thumbnails were made (no soffice in the environment); the deck was built with make_ppt.py only and not opened in PowerPoint.
- Levels are my own application of the calibrated skill; the official anchors were used where the question is an official JEE Advanced question (list above).
- multi_concept was set true for Q4, Q6, Q22 only (symmetry + adjoint; symmetric + integer perfect-square condition; permutation matrices + trace + determinant); this lifts them from 2 to 2.5.
- Concept names are my own wording (see "Blueprint").
- The paper is a mixed set of JEE Advanced questions; sections in the deck are by exam year, not by the paper's own headings (it has none).
