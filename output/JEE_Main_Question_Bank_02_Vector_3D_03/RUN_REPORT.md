# Run report - JEE_Main_Question_Bank_02_Vector_3D_03

**Difficulty index (marks-weighted, adjusted): 2.33** (9 questions x 4 marks; no equivalence-relation or multi-correct adjustments apply).
Levels: L2 = 6 (Q2, Q3, Q5, Q6, Q7, Q9), L3 = 3 (Q1, Q4, Q8), L0/L1/L4/L5 = 0.
Deck numbering Q1-Q9 = paper Q41-Q49 (the PDF starts at question 41).

**Blueprint:** none was available. Concepts self-assigned (no blueprint) - please review.
Marks assumed: the paper prints no marks; JEE Advanced default of 4 per question used for all 9 (all are numerical-answer questions; answers 285, 18, 9, 0, 11, 66, 9, 10, 9 are not all 0-9, so they are labelled "Numerical Type"); stated on the section divider. No negative marking assumed.

## Questions with solution_source = corrected (answers unchanged)
- Q2 (paper 42): PDF's third vector is printed "x i + y i" (should be x i + y j); typo only.
- Q4 (paper 44): PDF gives the z^2 coefficient as 1/2 + l^2/(l^2+n^2) (should be n^2) and drops the factor 2 of the zx term (writes "alpha zx"); equations (1), (2) and the answer are unaffected.
- Q7 (paper 47): PDF's right-hand side "21 sqrt21" should be 21 (the next line is consistent with 21); also the rejected root -29/3 is now stated.
- Q8 (paper 48): PDF prints the line as (x-1)/-1 = (y+4)/2 = (z+2)/2; denominator of z should be 3 (the working uses 3).
- No question needed solution_source = written; Q1, Q3, Q5, Q6, Q9 are `pdf` (Q6: the PDF's positive cos(theta) is noted and the opposite sign handled in an added step, since the modulus makes it immaterial).

## Answer key
All 9 keys verified correct (sympy for Q1 (c = (3,-2,4), |a x c|^2 = 285), the Q4 quadratic form, the Q7 quadratic; hand computation for the rest).

## Alternates and results
- Alternate solutions given for all 9 questions.
- No question without an alternate. Weaker alternates: Q3 (tan theta from cross/dot, a modest variation avoiding recognising 60 degrees) and Q7 (Pythagoras instead of the cross-product determinant; leads to the same quadratic) - kept because they avoid steps of the main route, but they are close to the primary.
- Alternates checked: Q1 orthogonal-triad decomposition (|c|^2 = 29, 14*29 - 121 = 285); Q2 Lagrange identity (components (0,1,2),(2,0,2),(2,1,0) give 18); Q3 tan theta = sqrt3; Q4 orthonormal normals => l = n; Q5 cross-product form gives lambda = 2/3; Q6 (b.c)^2 = 1100 - 11 = 1089; Q7 same quadratic; Q8 line lies in the plane, n x d = (-1,-26,17); Q9 normal d1 x d2 = (13,10,35) through (5,0,0).
- useful_results given for all 9 questions.

## make_ppt.py warnings
None. 361 equations converted, 63 slides.

## Skipped / assumed / guessed
- No visual rendering of the deck (no soffice/thumbnails); build-only check.
- Levels are my calibrated judgement (no blueprint difficulty column); nearest anchors cited are approximate.
- Hindi text in the PDF was ignored; only the English statements were used.
