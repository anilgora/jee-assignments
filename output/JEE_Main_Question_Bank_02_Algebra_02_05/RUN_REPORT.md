# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_02_05

Paper: 20 questions (printed Q81-Q100, numbered 1-20 here): complex numbers, statistics, counting, probability, binomial theorem, series. Read from page images plus the text layer. 122 slides, 656 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.85** (4 marks each; no equivalence-relation adjustment; no multi-correct questions, so no 2.5 floor).
- Questions per level: Level 1: 6 (Q1, Q3, Q4, Q8, Q11, Q12) | Level 2: 11 (Q2, Q5, Q6, Q7, Q9, Q10, Q15, Q16, Q17, Q18, Q19) | Level 3: 3 (Q13, Q14, Q20) | other levels: none.
- Confidence Medium throughout (JEE Main bank; no close Advanced anchors).

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): 4 marks for every question (Q1-Q9 single correct, Q10-Q20 numerical), no negative marking; stated on the section dividers. The PDF labels Q10-Q20 "Integer type" but answers go above 9 (e.g. 300, 118), so they are labelled Numerical Type.

## Solutions whose source is corrected or written
- Q14 - corrected (gap): PDF states b = e^2 with no reason; added that the numerator of the r-th term is sum of rCk = 2^r, so b = sum 2^r/r! = e^2.
- Q16 - corrected (typo): PDF's x = -1 line prints a0 - a1 + a2 + ... + a19 + a20 = 1; the odd terms should alternate in sign (-a3, ..., -a19). Result unaffected.
- Q18 - corrected (typo): PDF's last line adds 2+4+5+6+8 (digit 7 of 245678 missing, which would give 25) but states 32; correct sum 2+4+5+6+7+8 = 32. Block positions (1-56, 57-71) also made explicit.
- No question was fully `written`. Source pdf: all others (notation cleaned only: Q19's PDF line "sum of alpha_r = sum[(x+3)^n-(x+2)^n]" is replaced by "value at x=1"; Q13's PDF brackets rewritten with explicit alternating sums).

## Answer key
All 20 keys verified by computation (brute force over permutations/digits, exact fractions, sympy, numerical series) and all agree with the PDF. Notes: Q15 key 120 counts ordered pairs (x, y) (unordered would be 60) - flagged on the slide; Q12 relies on the principal value of the fractional power.

## Alternates
Given for 18 of 20 questions (all except Q17 and Q20). Light variants (distinct but modest ideas): Q12 (polar form instead of algebraic simplification), Q16 (choose-factors count for a2; the odd-sum part still uses f(1), f(-1)), Q19 (factorisation A^n-B^n with A-B=1 instead of G.P. ratio), Q9 (guess closed form and prove by induction), Q18 (count from the other end). Others use clearly different ideas (Q1 period-3 blocks, Q2 y=tan(theta), Q3 variance formula for A.P., Q4 divisor sum, Q5 fix first digit, Q6 count all strings then remove leading zero, Q7 (p+q)^n+(p-q)^n over 2, Q8 parallel-axis identity, Q10 i*conj(z)=z and tan^-1 difference, Q11 classify by number of 3s, Q13 finite-difference identity, Q14 integrating the exponential generating function, Q15 fix x and count y).
No alternate:
- Q17 - once the expression is seen as (1+x)^17(1-x)/x^15, reading two coefficients is the only route; the symmetry g(1/x) = -x^12 g(x) is only a check and is listed under useful results.
- Q20 - the enumeration is by the common sum; organising by the partner of 7 is the same 9 splits x 8 arrangements, so no genuinely different method (given under useful results).

## Useful Result / Pattern
Given for all 20 questions.

## make_ppt.py warnings
None printed (only the equation count and the save line). No "could not convert" notes.

## Skipped / assumed
- No rendering to images (no soffice); the deck was built without warnings but not viewed.
- Difficulty xlsx formulas not recalculated (no recalc step); index 1.85 computed by hand from the levels (37/20).
- Ratings' nearest-anchor column says "JEE Main level; no close Advanced anchor" for every question.
