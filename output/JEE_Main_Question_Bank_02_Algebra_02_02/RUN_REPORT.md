# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_02_02

Paper: 20 questions (printed as Q21-Q40 in the PDF, numbered 1-20 here): binomial theorem, probability, statistics, complex numbers, determinants, P&C. Read from page images (text layer garbled). 123 slides, 767 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.85** (4 marks each; no equivalence-relation adjustment; Q11 is a one-or-more-correct question but single-concept, so no 2.5 floor).
- Questions per level: Level 1: 7 (Q1, Q6, Q7, Q9, Q15, Q18, Q19) | Level 2: 9 (Q2, Q3, Q4, Q5, Q8, Q10, Q13, Q16, Q17) | Level 3: 4 (Q11, Q12, Q14, Q20) | other levels: none.
- Confidence: High for Q1, Q6, Q7, Q9, Q15, Q18, Q19; Low for Q13 (a Bonus question); Medium for the rest. A JEE Main bank, so the index is far below the JEE Advanced range.

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): 4 marks for every question (Q1-Q10 and Q12-Q20 single correct; Q11 one-or-more-correct because the key lists B, D), no negative marking assumed; stated on the section dividers.

## Solutions whose source is corrected or written
- Q1 - corrected: PDF wrote P(B) = (1/4)^4; it is (1/2)^4 = 1/16. Later lines (1/(16-1-4)) were right.
- Q4 - corrected (gap): PDF only states the ellipse; the z = 4e^{i theta} derivation and the 17/4 > 4 > 15/4 argument for 4 crossings were missing.
- Q7 - corrected: PDF wrote 1016 = 0 + (n-1) x 8 => 10 = 8n; should be n - 1 = 127. (Also listed the first condition as r = 0..1016 rather than even r.)
- Q8 - corrected (gap): PDF stops at minimum |z| = 2 sqrt 2; maximum 4 and the comparison of the options were added.
- Q9 - corrected (typos): "P(x >= 1) >= 9/19" should be 9/10, and "1 - P(x = 1)" should be 1 - P(x = 0).
- Q11 - corrected: PDF writes 350^2 where the variance 350 is meant, then rejects alpha = 30 as "not possible" and gets only 500, contradicting its own key B, D. alpha = 30 gives sigma_B = 0 (allowed), sum of variances 900.
- Q13 - corrected (gap): PDF says "Data inconsistent" without the reason (C(N,j) = 2 only for N = 2, but N = 2r + 4 >= 4); added.
- Q16 - corrected (gap): the strict sign needs x1 != 0 and the existence of cases B and C had to be shown; added.
- Q17 - corrected: PDF writes 2 alpha + 1 = 5; subtracting gives -5 (alpha = -3, b = 6 are right). Options were not evaluated; added.
- Q19 - corrected (typo): PDF gives (1-i)/(1+i) = i; it is -i.
- Q20 - corrected (gap): the argument that both digit sums equal 12 and the origin of 3! x 2 x 2 were missing; added. Count 60 confirmed by brute force.
- No question was `written`. Source pdf: Q2, Q3, Q5, Q6, Q10, Q12, Q14, Q15, Q18. (Q5: PDF lists the matrix with rows/columns taken in order 3,2,1 (same determinant); I stated that step and the identity (w+1)^2 = w. Q15: PDF's Method II is cut off; I completed it.)

## Answer key
All keys verified by computation (sympy / brute force / exact fractions).
- Q11: key "B, D" is right (500 and 900); the PDF's own working only reaches 500.
- Q13: key "Bonus" is right (no n, r satisfy the data).
- Q2: key (A) is the intended answer; strictly, negative k in [-3, -2 sqrt 2) also satisfies the condition, but all options list positive k, so no option is literally an "iff" statement. No change made.

## Alternates
Given for 18 of 20 questions (all except Q7 and Q9).
- Q7 has NO alternate: the only route is the two integrality conditions on r (8 | r) and counting an A.P.; any reparametrisation is a rewording.
- Q9 has NO alternate: the only route is 1 - 2^-n >= 0.9 giving 2^n >= 10; testing n = 3, 4 is the same inequality evaluated, not a different method.
Honest strength notes: Q1 (reduced-sample-space count), Q12 (ratio test instead of factorial products) and Q13 (bound on a single Pascal sum) are light variants; Q2 (committee double counting), Q3 (complex completion of the square), Q4 (|z+1/z|^2 = 16 + 1/16 + 2cos 2 theta), Q5 (rank-one matrix), Q6 (shift), Q8 (AM-GM), Q10 (Venn regions), Q11 (within + between variance), Q14 (Newton power sums), Q15 (complement), Q16 (z2 = is/z1), Q17 (|z+1|^2 via Vieta), Q18 (linearity), Q19 (alpha^2 + beta^2 = 0), Q20 (symmetry of zero's position) use clearly different ideas. All alternates were checked to reach the same answers (numerically or symbolically where possible).

## Useful Result / Pattern
All 20 questions have useful_results slides (3 bullets each); formulas spot-checked numerically (e.g. det(yI + vv^T) for n = 2, power-sum formula p^5 + q^5 at p = 1, q = 2 giving 33, combined-variance formula on {0},{2}, A.P. criterion (n - 2r)^2 = n + 2 at n = 7, r = 2, ellipse semi-axes r +- 1/r for r = 4, absorption identity at n = 5, r = 2).

## make_ppt.py warnings
None. Output only: "767 converted to native PowerPoint equations" and the save line; no "could not convert" warnings and no bullet-count warnings.

## Skipped / assumed
- Marks and marking scheme not printed: assumed 4 marks, no negative marking.
- Concepts self-assigned; levels are judgement calls (Q11, Q12, Q14, Q20 vs Q2-Q5 least certain). Nearest anchors cited are from JEE Advanced, so they are only rough guides for a JEE Main bank.
- Q11 typed as one-or-more-correct because the key gives B, D.
- No rendering/thumbnails (no soffice); slides not visually checked.
- Hindi text of the questions not reproduced (English only).
- Q2 option (A) read from the page image as "2 sqrt 2 < k <= 3".
