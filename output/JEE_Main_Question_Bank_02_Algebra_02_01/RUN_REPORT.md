# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_02_01

Paper: 20 single-correct questions (Algebra: binomial theorem, probability, P&C, statistics, complex numbers). Read from page images (text layer garbled). 121 slides, 649 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.95** (4 marks each; no equivalence-relation adjustment, no MCQ floor).
- Questions per level: Level 1: 6 (Q1, Q2, Q8, Q10, Q19, Q20) | Level 2: 9 (Q3, Q4, Q5, Q7, Q9, Q11, Q12, Q16, Q18) | Level 3: 5 (Q6, Q13, Q14, Q15, Q17) | other levels: none.
- Confidence: High for Q1, Q2, Q8, Q10, Q16, Q18, Q19, Q20; Medium for the rest. A JEE Main bank, so the index is far below the JEE Advanced range.

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): 4 marks for every question (single correct, JEE Advanced default), no negative marking assumed; stated on the section divider.

## Solutions whose source is corrected or written
- Q2 - corrected: PDF wrote (n+1)/(r+1) = 55/34 (should be 55/35 = 11/7) and equation (2) as 3n-5r = 4 (should be 3n-5r = 0, since n/r = 5/3). The PDF's own equations give r = -8; with the corrections r = 6, n = 10 (answer unchanged).
- Q6 - corrected: figure counts "7 not first" as 3C1 x 9 x 9 x 9; correct is 3C1 x 8 x 9 x 9 = 1944 (PDF's total 1944 and later numbers were right).
- Q12 - corrected: first-throw gain written 1/2 x 100 (should be 1/3 x 100); the three-losses branch (-150, probability 8/27) was missing and the contributions were never summed. Answer 0 unchanged.
- Q13 - corrected (gap): PDF omitted the condition 3 | (n-r), hence 3 | n, and the argument that 2184 is the least n. Answer unchanged.
- Q16 - corrected (typo): "11^3" in the sum of squares should be 11^2; the value 699 and the answer were correct.
- No question was `written`. Source pdf: Q1, Q3, Q4, Q5, Q7, Q8, Q9, Q10, Q11, Q14, Q15, Q17, Q18, Q19, Q20.

## Answer key
All keys verified by computation (brute force / exact fractions). Q15 is keyed "Bonus" and that is right: the correct probability is 16065/2^15 = 945*17/2^15 (brute force over 4^10 placements), which matches none of the options. No other key looks wrong.

## Alternates
Given for 19 of 20 questions (all except Q13).
- Q13 has NO alternate: the only route is the two divisibility conditions (12 | r, 3 | n) plus counting multiples; reparametrising n = 3m is a rewording, not a different method.
Honest strength notes: Q8 (rotational counting), Q19 (unordered pairs) and Q14 (direct tail sum) are light variants; Q2, Q3, Q4, Q7, Q10, Q12, Q15, Q18, Q20 use clearly different ideas (divisibility shortcut, polar form, Euler criterion, binomial pmf, pairwise variance identity, Wald, over-count correction, A.P. criterion, linearity of expectation). All alternates were checked to reach the same answers (numerically where possible).

## Useful Result / Pattern
All 20 questions have useful_results slides (2-3 bullets each); formulas spot-checked numerically (e.g. S_n recurrence to 18817, A.P. criterion (N-2k)^2 = N+2 at N = 7, 14, pairwise variance identity, tribonacci counts, sum of C(21,k), k<=10 = 2^20).

## make_ppt.py warnings
- "Q8: only 3 solution bullets - a complete solution normally has more": the PDF's own working for Q8 is three lines (list the two equilateral triangles, total 6C3, divide); nothing was omitted. Left as is.
- Otherwise only the "649 converted to native PowerPoint equations" and save lines; no "could not convert" warnings.

## Skipped / assumed
- Marks and marking scheme not printed: assumed 4 marks, no negative marking.
- Concepts self-assigned; levels are judgement calls (Q6, Q14, Q17 least certain).
- No rendering/thumbnails (no soffice); slides not visually checked.
- Hindi text of the questions not reproduced (English only).
