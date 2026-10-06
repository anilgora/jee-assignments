# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_01_04

Paper: 20 questions (printed Q61-Q80), Algebra (matrices/determinants, linear systems, sequences). Q1-13 single correct, Q14-20 "Integer Type" (answers are integers, some above 9, so labelled Numerical). Deck Q n = printed Q n+60. 127 slides, 743 native equations. Q7 = Q13 (printed 67 = 73) and Q8 = Q11 (printed 68 = 71) are duplicate questions in the PDF; both copies are in the deck.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.15** (43 / 20 questions, 4 marks each). No equivalence-relation adjustment, no MCQ floor.
- Questions per level: Level 1: 2 (Q1, Q5) | Level 2: 13 | Level 3: 5 (Q3, Q8, Q11, Q16, Q17) | other levels: none.
- Medium confidence: Q2, Q3, Q4, Q8, Q10, Q11, Q14, Q16, Q17; the rest High. Nearest anchors are approximate.

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): +4 for single-correct and +4 for the integer/numerical questions (JEE Advanced defaults), 0 otherwise; stated on the section dividers.

## Solutions whose source is corrected or written
- Q1 (printed 61) - corrected (gap): PDF jumps from the sum formulas to r = 6; added the cancellation of a(1-r^64) and 1+r = 7.
- Q2 (62) - corrected (gap): constant term (-21) never checked and the identification of the given cubic with the characteristic polynomial not justified; added (sympy: a=-5, b=-1 is the unique solution of A^3-4A^2+A+21I=0).
- Q3 (63) - corrected (ANSWER CHANGED, see below): PDF calls statement (II) false, but its own result trace(adj adj R) = xyz(x+y+z) is never 0, so the "if" part never holds and (II) is vacuously true. Deck answer (B); PDF key (D).
- Q6 (66) - corrected (gap): PDF writes (alpha,beta) = (5,3) with no enumeration; added factor-pair parity enumeration and option check.
- Q7 (67) - corrected: PDF's D has second row (4,3,-2); must be (7,3,-2) (with 4, lambda would be 26). lambda=5 correct.
- Q8 (68) and Q11 (71) - corrected (gap): PDF stops at k = 3, 20, 37 with no integrality argument (k = 3 mod 17) or count; added, plus existence of lambda=-17, mu=45. Brute force: 3 solutions.
- Q10 (70) - corrected: PDF's telescoping has wrong second factor, 1/((2n-1)(2n+3)); correct is 1/((2n+1)(2n+3)), S_n = 2(1/3 - 1/((2n+1)(2n+3))). Also see answer-key note.
- Q12 (72) - corrected (gap): beta calculation and the consistency (rank) remark added.
- Q13 (73) - corrected: same row typo as Q7.
- Q14 (74) - corrected (gap): added that both eigenvalues +1 and -1 are attained (AM = -M, AX = X for X perpendicular to M).
- Q17 (77) - corrected: PDF's 2(A+I) third row (-2,-6,2) should be (-4,-6,2); the determinant expansion det(A+I)=15 and |adj B| = |B|^2 were omitted; added.
- Q18 (78) - corrected (gap): PDF ends "= 55(353)+40" without evaluating the sums; added 19455 and k = 353.
- Q19 (79) - corrected (gap): PDF does not check that each root of D=0 gives NO solution (could be infinitely many); added check for all three (ranks 2 vs 3, verified with sympy).
- No question was `written`. Source pdf: Q4 (notation slip "adj(n^-1)" only), Q5, Q9, Q15, Q16, Q20.

## Answer key - needs your attention
- **Q3 (printed 63): PDF key (D) looks wrong / debatable.** Since x,y,z are all non-zero, trace(adj adj R) is never 0, so statement II ("if trace = 0 then ...") is vacuously TRUE; statement I is false. Strict logic gives (B). The deck shows (B) with the key noted; if you want the conventional key (D) taught, edit the "answer" field and last bullets in the JSON. Please decide.
- **Q10 (printed 70): question is slightly inconsistent.** With the printed S_n, S_0 = -15/64, so T_1 = S_1 = 105/64, not 15/8 (formula value). Strictly the sum is 64/105 + 2/15 = 26/35, which is not an option. The intended key (C) 2/3 (formula valid for all n) is kept and the remark is on the solution slide.
- All other keys verified by sympy / brute force (Q1, 2, 4-9, 11-20 correct).

## Alternates
Given for 19 of 20 questions (all except Q16). Q8/Q11 and Q7/Q13 (duplicates) have different alternates each (Q7: row combination, Q13: solve in z; Q8: lattice direction by cross product, Q11: treat x+y+z=s as a third equation); Q7 has two alternates.
Honest strength notes: Q10 (partial fractions) and Q18 (difference of squares) are lighter variants of the main route; Q2 (trace/det instead of full polynomial) and Q9 (set p=q=0) are shortcuts rather than new ideas; Q1, Q4, Q5, Q7, Q8, Q11-15, Q17, Q19, Q20 use clearly different ideas.
Question with NO alternate:
- Q16 - the Sophie Germain factorisation followed by telescoping is the only natural route; guess-and-induct needs the same identity for the induction step, so it would be a reworded copy.

## Useful Result / Pattern
All 20 questions have a useful_results slide (3-4 bullets); formulas spot-checked numerically (G.P. odd/even sums, Q16 partial sum 12/13 at n=2, adj(adj) powers, Householder trace/det, skew-symmetric det(I+A)=15, sum of powers 55/385/3025, left null vectors).

## make_ppt.py warnings
- First build: "could not convert $\int|{\rm linear}|$" (Q15 useful result, `{\rm ...}` not supported). Fixed by rewriting that phrase in words; rebuilt with no warnings.

## Skipped / assumed
- Marks and negative marking not printed: assumed +4 / 0. Integer-type answers labelled "Numerical Type" because several exceed 9.
- Nearest anchors for ratings are approximate; ratings for Q3, Q8, Q11, Q16, Q17 (level 3) are judgement calls.
- No rendering/thumbnails (no soffice); slides were not visually checked.
