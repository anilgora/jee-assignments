# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_02_04

Paper: 20 questions (printed as Q61-Q80 in the PDF, numbered 1-20 here): complex numbers, series, probability, binomial theorem, matrices, statistics, counting. Read from page images (text layer garbled). 115 slides, 702 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.30** (4 marks each; no equivalence-relation adjustment; no multi-correct questions, so no 2.5 floor).
- Questions per level: Level 0: 1 (Q19) | Level 1: 13 (Q1, Q3, Q4, Q5, Q7, Q8, Q9, Q10, Q13, Q14, Q17, Q18, Q20) | Level 2: 6 (Q2, Q6, Q11, Q12, Q15, Q16) | other levels: none.
- Confidence: Medium throughout (a JEE Main bank, far below the JEE Advanced range; no close Advanced anchors).

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): 4 marks for every question (all 20 are single correct), no negative marking assumed; stated on the section divider.

## Solutions whose source is corrected or written
- Q2 - corrected (typo): PDF's step 2 has "+10" where "+40" is meant ((r-1)^2/4 + 6(r-1)/2 + 10 = ((r-1)^2+12(r-1)+40)/4); the next line r^2+10r+29 already uses 40.
- Q7 - corrected (typo/gap): PDF's final line drops the minus sign in sqrt(-54) and says the imaginary part is +-2 sqrt6 without noting the real cases +-6 have imaginary part 0.
- Q11 - corrected (gap): PDF stops after the first root a=(sqrt7-1)/6; second root a=(-1-sqrt7)/6 ([a] = -1, value 0) written out.
- Q12 - corrected (gap): final remark added that y^2+y-k-k^2 = (y-k)(y+k+1), the root y=k being the pole z=ki of u (the question intends the closure). Answer k=2 unchanged.
- Q15 - corrected (gap): PDF lists "62, 83, 99, 46" without showing they come from p in {31,68}, q in {15,31} by symmetry; added.
- Q16 - corrected (written part): PDF ends at "r=3, n=8"; the whole centroid part (C=(1,0), (3x-1)^2+(3y)^2=20) was missing and is written.
- No question was fully `written`. Source pdf: Q1, Q3, Q4, Q5, Q6, Q8, Q9, Q10, Q13, Q14, Q17, Q18, Q19, Q20. (Routine algebra expanded in Q10; verdicts of other options only noted in Q20; the PDF diagram labels the centre in Q9 as (1,10), a typo for (1,0), not used in the slides.)

## Answer key
All keys verified by computation (numerical sums, brute force, exact fractions, sympy).
- Q11: the PDF key is "Drop" and this is correct for the printed question: the possible values are 0 and -(1+sqrt7)/4, neither is an option. Slide answer is "Dropped - no option matches". If the stem is read as 1 + [a]/(4b), the value is 1 (option C) - probably the author's intention. Flagged for review.
- Q12: key B (k=2) kept; see the pole remark above.
- All other keys agree with the computed answers.

## Alternates
Given for 15 of 20 questions (Q1, Q2, Q3, Q4, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q14, Q15, Q16, Q20).
No alternate (no genuinely different method exists):
- Q5 - two-stage total probability; the only route is weighting the two branch probabilities (a 72-outcome uniform space is the same computation).
- Q13 - single count: |ab|=100, divisors times signs; any other count is the same one.
- Q17 - Bayes with the three group weights; expected-counts form is the same fraction.
- Q18 - one G.P. equation and one dice count.
- Q19 - direct binomial mean and s.d.; the shortcut sqrt(np/q) is listed under useful results.
Light variants (still distinct ideas, but modest): Q9 (explicit witness segment instead of a picture), Q14 (Fermat instead of binomial expansion), Q2 (derivatives of sinh instead of splitting into three series), Q4 (Pascal's rule instead of nCr = n/r (n-1)C(r-1)). The others use clearly different ideas (Q1 conjugate modulus, Q3 same-parity pairs, Q6 DFT, Q7 conjugate roots, Q8 deviations from the combined mean, Q10 Pythagoras, Q11 Apollonius circle and sign test, Q12 division first, Q15 geometric series in x/(1+x), Q16 Pascal row and perpendicular vectors, Q20 counterexample elimination). All alternates were checked to give the same answer.

## Useful Result / Pattern
Given for all 20 questions.

## make_ppt.py warnings
None printed (only the equation count and the save line). No "could not convert" notes.

## Skipped / assumed
- No rendering to images (no soffice); the deck was built and the script reported no problems but was not viewed.
- Difficulty xlsx formulas are not recalculated (no recalc step available); index 1.30 computed by hand from the levels.
- Ratings' nearest-anchor column says "JEE Main level; no close Advanced anchor" for every question.
