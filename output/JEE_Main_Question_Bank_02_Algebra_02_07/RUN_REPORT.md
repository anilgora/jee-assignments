# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_02_07

Paper: 20 questions (printed Q121-Q140, numbered 1-20 here), all numerical: binomial theorem, P&C, probability, complex numbers, statistics, theory of equations, series. Read from page images plus the text layer. 123 slides, 800 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.90** (4 marks each; no equivalence-relation adjustment; no multi-correct questions, so no 2.5 floor). Computed by hand as 38/20; workbook formulas not recalculated (no recalc step).
- Questions per level: Level 1: 7 (Q2, Q3, Q7, Q9, Q15, Q18, Q20) | Level 2: 8 (Q1, Q4, Q5, Q8, Q11, Q13, Q16, Q17) | Level 3: 5 (Q6, Q10, Q12, Q14, Q19) | other levels: none.
- Confidence Medium throughout (JEE Main bank; no close Advanced anchors).

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): 4 marks for every question (all Numerical Type, no negative marking assumed); stated on the section divider.

## Solutions whose source is corrected or written
- Q6 (PDF 126) - corrected (typo): PDF's last line gives the upper bound as 248; the question says 281. Conclusion n = 5 unchanged.
- Q7 (PDF 127) - corrected (omission): PDF lists the seven (p,q,r) triples but never evaluates or adds them; values and the sum 612 added.
- Q9 (PDF 129) - corrected (gap): PDF does not explain why (-w)^162 = 1; added (162 even and a multiple of 3).
- Q10 (PDF 130) - corrected (flawed argument): PDF treats the locus as the circle on diameter alpha-beta and sets |alpha-beta|^2 = 2*lambda, then solves for lambda = 2. The given right-hand side is 2*lambda, not |alpha-beta|^2, so that step is unjustified. Correct argument (parallelogram identity) gives |alpha-beta|^2 = 4 for every lambda > 1. Answer 2 unchanged.
- Q11 (PDF 131) - corrected (gap): PDF jumps from a = 2 to r + 1/r = 5/2 and r = 2, and never uses a3+a4+a5 = 14 (which selects r = 2 over r = 1/2). Intermediate quadratic, the use of the condition, and sum of squares 85.25 written out.
- Q14 (PDF 134) - corrected (incomplete): PDF stops at the line 2x - y + 2 = 0 and never computes AB or 30(AB)^2; distance from centre, chord length and 24 added. (Also prints "-x2 y" for "-k2 y".)
- Q16 (PDF 136) - corrected (arithmetic): PDF has 1919 x 1920 = 3684880; correct is 3684480 (so 100*lambda + 3684479). Last two digits 79, answer 63 unaffected.
- No question was fully `written`. Source pdf: Q1, Q2, Q3, Q4, Q5, Q8, Q12, Q13, Q15, Q17, Q18, Q19, Q20 (notation cleaned; some steps made explicit, e.g. Q12 splitting r = (r-1)+1, Q19 telescoping sums, Q13 Bayes algebra, Q17 rejecting a = 110).

## Answer key
All 20 keys verified by computation (exact fractions, brute-force enumeration of strings/permutations, sympy expansion for Q1/Q4, modular arithmetic) and all agree with the PDF: 54, 1, 81, 0, 806, 5, 612, 0, 3, 2, 211, 465, 432, 24, 9, 63, 10, 32, 160, 2736. No key looks wrong. The PDF labels no marks.

## Alternates
Given for 18 of 20 questions (all except Q4 and Q20). Clearly different ideas: Q1 (clear denominators to a polynomial in x^3), Q2 (64 = 63+1), Q3 (equidistribution of residues), Q7 (binomial of a binomial, rational part of (1+2^(1/3))^m), Q8 (reduce mod x^2+x+1), Q9 (Newton recurrence, period 6), Q10 (coordinates with alpha = -d, beta = d), Q11 (a_i a_(6-i) = a_3^2 and the given a3+a4+a5 = 14), Q12 (r(30-r) falling-factorial split), Q13 (odds form of Bayes, polar coordinates), Q14 (explicit intersection points), Q15 (odds x likelihood ratio), Q16 (Carmichael exponent, 19^-1 = 79), Q17 (unit-square scaling), Q18 (split by last digit), Q19 (undetermined-coefficient telescoping G(r) = r!(r-1)(r+5)).
Light variants (distinct but modest): Q5 (ratio of consecutive terms with t = y/x - close to the PDF's coefficient ratios), Q6 (generating function / integration instead of falling factorials), Q17 (complement scaled to the unit square).
No alternate:
- Q4 - once (1-x)(1+x+x^2) = 1 - x^3 is seen, the exponent argument (3r or 3r+1 never equals 2012) is the whole problem; roots-of-unity filters give only sums of coefficients over residue classes, not an individual coefficient, so no genuinely different method.
- Q20 - the sum of coefficients minus the three omitted ends is the only route; a probability reading (Bin(9,1/3) weights) is the same computation reworded.

## Useful Result / Pattern
Given for all 20 questions.

## make_ppt.py warnings
None printed (only the equation count and the save line). No "could not convert" notes.

## Skipped / assumed
- No rendering to images (no soffice); the deck was built without warnings but not viewed.
- Difficulty xlsx formulas not recalculated; index computed by hand.
- Ratings' nearest-anchor column says "JEE Main level; no close Advanced anchor" for every question; the justification column is a brief key-step note.
