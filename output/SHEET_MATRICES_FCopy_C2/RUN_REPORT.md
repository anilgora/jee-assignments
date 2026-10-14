# Run report - SHEET_MATRICES_FCopy_C2

Paper: Exercise C-II (Matrices, JEE-style sheet), 31 questions (Q1-31, numbered continuously as in the PDF). The PDF has answers and solutions. Date of run: 2026-10-14. Deck: 195 slides.

## Blueprint
No blueprint was available. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper; stated in the section dividers): Numerical, Subjective and Integer questions 4 marks each (Q1-16, total 64); Paragraph single-correct 3 marks each (Q17-28, total 36); Matching 3 marks each (Q29-31, total 9). Total 109. Types were taken from the paper's headings: Q1-2, Q13-14 numerical, Q3-12 and Q15 subjective ("Subjective Type" is not in the standard label table), Q16 integer (JEE 2010), Q17-28 four paragraph sets (17-19, 20-22, 23-25, 26-28), Q29-31 match-the-column.

## Difficulty
Marks-weighted difficulty index (adjusted): **2.09** (below the official JEE Advanced range 2.6-3.2; this is a chapter sheet, no expected distribution).
Level counts: L0 = 0, L1 = 5 (Q5, 7, 11, 13, 17), L2 = 17 (Q1, 3, 4, 6, 8, 9, 10, 14, 15, 16, 18, 19, 20, 26, 27, 28, 31), L3 = 9 (Q2, 12, 21, 22, 23, 24, 25, 29, 30), L4 = 0, L5 = 0.
No equivalence-relation adjustment and no MCQ floor applied (no such questions). Medium-confidence ratings: Q2, 12, 14, 21-25, 29, 30, 31.

## Solutions whose solution_source is "corrected" (8)
- Q5: not wrong but incomplete. The PDF stops at the characteristic equation ("Put lambda = A") and never finds A^-1. Steps for multiplying by A^-1 and the final inverse were added.
- Q8: PDF writes XA != 0 and answers "NO"; XA = (c+2d)[[-2,-4],[1,2]] is zero when c+2d = 0, so "in general not". The PDF also has no working for the second matrix [[1,2],[2,3]]: |A| = -1, so only X = O exists. Both added.
- Q9: (iii) is stated without a consistency check (Delta_1 = 0 alone is not sufficient). Added the row relation R2 = 3R1 - 2R3 and the rank check. Results of the PDF are right.
- Q10: part (c) says "inverse is not possible as |C| = 0", which does not prove there is no solution. Added |C||X| = |A| (0 = -2, impossible).
- Q12: the PDF derives g = h and c = d and then says columns C2, C3 of B are identical. Not forced (a=b=1, c=2, d=1, f=1, g=2, h=3 gives infinitely many solutions of AX = U with g != h, c != d), so the argument is incomplete. It also gives |B3| = +a^2 df; the correct value is -a^2 df. Replaced by the general identity |B| = -Delta_2 (Delta_2 = determinant of A with its 2nd column replaced by U), checked symbolically.
- Q14: PDF divides (1) by (2), which is not allowed without p, q, c, 1-d non-zero. Replaced by multiplying through to get p[bc-(1-a)(1-d)] = 0 and q[...] = 0. Answer 5049 unchanged.
- Q23: PDF says (a+b) in 0..2p-2 contains "only one multiple of p, i.e. p"; it also contains 0 (a = b = 0, already in a = b). Count 2p-1 is right; the pair (0,0) is now accounted for explicitly. Verified by brute force for p = 3, 5, 7, 11.
- Q30: PDF's (C) uses the formula for adj(adj A) (two adjoints); the question has three. For a 2x2 matrix the value is the same (+-2); working rewritten. The elements are taken as all different (as in the Hindi text), N = 24.
Questions with solution_source "written": none. Q22 is "pdf" but a closing remark was added (exactly 4 inconsistent matrices; the PDF shows only three, which is enough for "more than 2").

## Answer key / question problems
- No printed answer disagrees with the correct answer. Every final answer was re-derived and checked by computation: Q1, 2, 3, 4, 6, 7, 9, 10, 12 (example), 13, 15, 16, 17 (2002), 20-25 (brute force over all 12 symmetric matrices and over p = 3, 5, 7, 11), 26-28, 29, 30 (all 24 matrices), 31 (numerics).
- Q8: the key says "NO" for XA = O; this is true only in general (see above).
- Q31(A): on x > 0 the function is increasing, so 2 is the infimum (approached as x -> 0+), not an attained minimum. The key (R) is kept.
- Q31(B): k = 1, 3 assumes AB != 0 (if AB = O every k works); the key is kept.
- Q30: the English wording omits "all elements different" (it is in the Hindi text); without it N would not be a finite permutation count and the key would not hold.

## Alternate solutions
Alternates (a genuinely different technique) were written for 28 of 31 questions: Q1-19, 21-23, 25, 26, 28-31 (Q12's alternate replaces Cramer's rule by elimination for the second part; its first part is the same determinant identity as the main solution). Each was verified against the answer (hand check and, where numeric, by computation).
Questions with NO alternate (3), and why:
- Q20: the count (diagonal ones odd; 3 + 9) can only be reworded (counting zeros instead of ones); no different method.
- Q24: choose a non-zero, b non-zero, c determined by the modular inverse; the other formulations (hyperbola over F_p) are the same count reworded.
- Q27: reduction of exponents modulo 3 after finding (a,b,c) is the only route.

## Useful Result / Pattern
Every question (1-31) has useful_results (4-5 general statements each, with conditions; formulas spot-checked on numerical cases).

## make_ppt.py warnings
None. The script printed only "1164 equations converted to native PowerPoint equations" and "195 slides, 31 questions". No equation was left as LaTeX text.

## Skipped / assumed / guessed
- No rendering or thumbnail check (no soffice in this environment); the deck was built but not viewed. The difficulty xlsx was not recalculated (recalc.py not available).
- Levels are my calibrated estimates against the anchors; the matrix anchors are few and Q23-25 (counting modulo p), Q2, Q12, Q21, Q22, Q29-31 are medium confidence.
- Concepts are self-assigned; Hindi text in the PDF was ignored. "Subjective Type" was used as a type label and "Subjective" in the ratings sheet (neither is in the standard table).
- The paragraph for each group (Q17-19, 20-22, 23-25, 26-28) is repeated on every question slide of the group.
- Q29 and Q30 columns are written inside the question text with line breaks (no separate column fields).
