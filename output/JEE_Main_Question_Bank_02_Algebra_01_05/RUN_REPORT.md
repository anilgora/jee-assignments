# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_01_05

Paper: 20 numerical (blank-answer) questions, printed Q81-Q100, Algebra (sequences, matrices, quadratics, counting). Deck Q n = printed Q n+80. 111 slides, 736 native equations. Maths pages were checked on page images.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.25** (45 / 20 questions, 4 marks each). No equivalence-relation adjustment, no MCQ floor (no MCQs).
- Questions per level: Level 1: 2 (Q2, Q4) | Level 2: 11 | Level 3: 7 (Q6, Q8, Q13, Q14, Q16, Q17, Q20) | other levels: none.
- Medium confidence: Q5, Q6, Q8, Q13-Q16, Q19, Q20; Q17 Low (answer guessable, bound needs Hadamard/eigenvalue idea); rest High. Nearest anchors are approximate.

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): +4 for every question (all are numerical/blank-answer type, JEE Advanced default for numerical), 0 otherwise; stated on the section divider. Type label "Numerical Type" (answers include values above 9).

## Solutions whose source is corrected or written
- Q1 (printed 81) - corrected (gap): PDF lists common terms 11..395 without showing first common term, difference lcm = 12, or that 395 is last (next 407 > 403).
- Q5 (85) - corrected (gap): "203 pairs" not counted (404 terms a5..a2020 = 202 pairs + (a1,a2024)); added index sum 2025.
- Q6 (86) - corrected: PDF writes "B^-1 = adj(A^-1) = B = adj(A)" (B^-1 = -A, not B) and finishes |P| = -38 yet states 38. Chain fixed; the determinant |3B+I| is -38 (sympy). See answer-key note.
- Q8 (88) - corrected (ANSWER CHANGED): PDF subtracts only multiples of 36 (150-25 = 125). "Not divisible by 4 and 9" = by neither: 150 - (75+50-25) = 50 (brute force). See answer-key note.
- Q13 (93) - corrected (gap): sqrt(961) appears without evaluating P4^2 = -63 and 4(alpha beta)^4 = 1024.
- Q14 (94) - corrected: determinant of [[a,d],[b,c]] written as ad-bc (entries mislabeled); Case III / IV only asserted. Notation fixed, arguments and Case IV count (8) added. Brute force 36.
- Q15 (95) - corrected: equation printed "x^2 - 7x + lambda" (should be 70x); no enumeration showing alpha = 1,2,3,4 fail. Added.
- Q17 (97) - corrected (gap): PDF only asserts the maximiser 3I; added Hadamard bound proving 27 is the maximum.
- Q19 (99) - corrected: target expression printed "(A+I)^3 + (A-I) - 6A" (missing cube); orthogonality and the expansion 2A^3+6A added.
- Q20 (100) - corrected (gap): A^m = [[m+1,-m],[m,1-m]] not proved and only the (1,1) entry compared; added A = I+N, N^2 = O and the all-entries check.
- No question was `written`. Source pdf: Q2, Q3, Q4, Q7, Q9, Q10, Q11, Q12, Q16, Q18. (Q16: the PDF repeats its last block twice; the duplicate was dropped.)

## Answer key - needs your attention
- **Q8 (printed 88): PDF key 125 looks wrong under the natural reading.** "Divisible by 2 and 3 but not divisible by 4 and 9" means by 6, and by neither 4 nor 9: answer 50 (brute force). 125 is the count of multiples of 6 that are not multiples of 36 (the "not by both" reading). Deck shows 50 (key noted on the slide). Please decide.
- **Q6 (printed 86): PDF key 38 equals |det|; the determinant |3B+I| itself is -38.** Deck shows -38 with "(PDF key: 38)". If |.| is meant as modulus, the key 38 stands.
- All other keys verified by sympy / brute force (Q1-5, 7, 9-20 correct).

## Alternates
Given for 19 of 20 questions (all except Q3).
Question with NO alternate:
- Q3 (83) - the only route is det = 0 for the homogeneous system; Sarrus/cofactor expansion is the same computation reworded, and row reduction with parameters is longer, not different.
Honest strength notes: Q2 (exterior angles), Q7 (middle-term shortcut) and Q10 (Cayley-Hamilton, still needs b) are lighter variants of the main route; Q1, Q4, Q5, Q6, Q8, Q9, Q11-Q20 use clearly different ideas (CRT, eigenvalues, symmetry about the mean, periodicity mod 36, sum of N_p^2, Hadamard vs eigenvalue bound, nilpotent N, etc.).

## Useful Result / Pattern
All 20 questions have useful_results slides (3 bullets each); formulas spot-checked numerically (sum formulas, Q4 eigenvalue powers, Q11 trace recurrence t0..t4, Q12 H.P. condition with a=6,c=9, Q13 S^2-P^2=4(ab)^n, Q14 N_p counts, Q16 G.P. triangle test, Q19 identity).

## make_ppt.py warnings
- None: first build printed only "736 converted to native PowerPoint equations" and the save line.

## Skipped / assumed
- Marks and negative marking not printed: assumed +4 / 0.
- Ratings are judgement calls using approximate nearest anchors; Q17 and Q8 are the least certain.
- No rendering/thumbnails (no soffice); slides were not visually checked.
