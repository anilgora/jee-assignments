# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_02_03

Paper: 20 questions (printed as Q41-Q60 in the PDF, numbered 1-20 here): probability, complex numbers, statistics, counting, binomial theorem, series, GP. Read from page images (text layer garbled). 117 slides, 576 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.65** (4 marks each; no equivalence-relation adjustment; no multi-correct questions, so no 2.5 floor).
- Questions per level: Level 1: 8 (Q2, Q3, Q5, Q10, Q12, Q16, Q18, Q20) | Level 2: 11 (Q1, Q4, Q6, Q7, Q8, Q9, Q11, Q13, Q15, Q17, Q19) | Level 3: 1 (Q14) | other levels: none.
- Confidence: High for Q2, Q3, Q5, Q10, Q18, Q20; Low for Q17 (ambiguous question); Medium for the rest. A JEE Main bank, so far below the JEE Advanced range.

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): 4 marks for every question (all 20 are single correct), no negative marking assumed; stated on the section divider.

## Solutions whose source is corrected or written
- Q1 - corrected (gap): PDF shows the three cases only as box diagrams; the reason throw 3 must not be 4 and (4,4) is excluded from throws 1-2 was added. Count 175 confirmed by brute force.
- Q9 - corrected (typo): PDF writes 12n - 40; it is 12(n-4) = 12n - 48. Next line n^2 - 21n + 98 = 0 was already right.
- Q15 - corrected (typo): PDF's series has 31/30 where 31/36 is meant; the option letter (C) is printed as "(3)". Answer 30/61 unchanged.
- Q16 - corrected (gap): PDF takes x = 3 without rejecting x = -4 (frequency 2x - 5 = -13 < 0); reason added.
- Q17 - corrected: PDF works out the string 0110 ('01' then '10'); the question asks '10' followed by '01' = 1001. Same value by symmetry (1/18 per start parity). The reason the two start-parity cases are added was missing.
- No question was `written`. Source pdf: Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q10, Q11, Q12, Q13, Q14, Q18, Q19, Q20 (Q20: added that R(z) = -sqrt3, so option (A) "-3" is false).

## Answer key
All keys verified by computation (brute force / exact fractions / numerical sampling).
- Q17: key A (1/9) is kept but the question is ambiguous. Each start parity (OEOE or EOEO) gives 1/18; the key adds them, i.e. treats the block as starting at an odd or an even place. If the block must start at place 1, the answer is 1/18 (option D). Flagged for review.
- Q3: key 2 follows the formula, but the data are impossible (sum of squares >= 44^2/4 + 96^2/6 = 2020 > 2000). Mentioned in the useful-results slide; answer unchanged.
- Q20: option (A) in the PDF reads R(z) = -3; the true value is -sqrt3, so A is false and the key B is right.

## Alternates
Given for 16 of 20 questions (all except Q5, Q16, Q17, Q18).
- Q5 has NO alternate: the only route is the complement and the inequality (2/3)^n < 1/6; log or integer testing is the same inequality.
- Q16 has NO alternate: the only route is sum of frequencies = 20 to fix x, then the weighted mean.
- Q17 has NO alternate: the only route is multiplying place-wise probabilities for the two start parities.
- Q18 has NO alternate: it is a single count 7*4 + 6n = 52.
Honest strength notes: Q9 (ratio form of the same equation) and Q15 (first-step recursion instead of the series) are light variants; the others (Q1 fixing the tail, Q2 Thales circle, Q3 shifted deviations, Q4 Vieta coefficients, Q6 generating function, Q7 Moebius half-plane, Q8 at-least-two-of-four, Q10 residues mod 4, Q11 centring on a4, Q12 half-diagonal, Q13 stars and bars, Q14 parametrisation, Q19 binomial per element, Q20 w^6 = -1) use clearly different ideas. All alternates were checked to give the same answer.

## Useful Result / Pattern
Given for all 20 questions.

## make_ppt.py warnings
None printed (only the equation count and the save line). No "could not convert" notes.

## Skipped / assumed
No blueprint; marks assumed 4 each; ratings assigned by the calibrated rubric; no rendering or thumbnail check (no soffice here).
