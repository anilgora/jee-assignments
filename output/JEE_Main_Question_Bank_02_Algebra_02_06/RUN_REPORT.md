# RUN REPORT - JEE_Main_Question_Bank_02_Algebra_02_06

Paper: 20 questions (printed Q101-Q120, numbered 1-20 here), all numerical: complex numbers, probability, statistics, counting, binomial theorem, series. Read from page images plus the text layer. 125 slides, 731 native equations.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.25** (4 marks each; no equivalence-relation adjustment; no multi-correct questions, so no 2.5 floor). Computed by hand as 45/20; the workbook formulas were not recalculated (no recalc step).
- Questions per level: Level 1: 4 (Q2, Q3, Q4, Q6) | Level 2: 8 (Q1, Q7, Q8, Q11, Q12, Q13, Q14, Q15) | Level 3: 7 (Q5, Q9, Q16, Q17, Q18, Q19, Q20) | Level 4: 1 (Q10) | other levels: none.
- Confidence Medium throughout (JEE Main bank; no close Advanced anchors).

## Blueprint
No blueprint used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): 4 marks for every question (all Numerical Type, no negative marking assumed); stated on the section divider. The PDF's answers are all integers; no Integer (0-9) labels were used because several exceed 9.

## Solutions whose source is corrected or written
- Q1 - corrected (typo): PDF line "|x+iy+i| = |x+y-3i|" lacks the i in iy; written as |x+i(y+1)| = |x+i(y-3)|. Result unaffected.
- Q3 - corrected (typo): PDF's last binomial terms "2024C2033 (420)^2023 + 8^2024" (index 2033 > 2024, factor 8 missing); replaced by the general expansion where only 8^2024 lacks the factor 420. Result unaffected.
- Q5 - corrected (gap): PDF jumps to "z^2-3iz-2 is imaginary" with no reason; added that 11iz-13 = 11i*alpha is purely imaginary, so the denominator must be purely imaginary. Result unchanged.
- Q6 - corrected (typo): PDF prints the last variance term as 4(45)^5; it is 4(45)^2 = 8100 (the value it uses).
- Q7 - corrected (wrong formula): PDF's variance line uses sigma^2 = sum f|x-5| / sum f (no square); correct is sum f(x-5)^2 / sum f. Its mean-deviation numerator "4+4+24x2..." should read 4x4. The values m = 8/5 and sigma^2 = 22/5 are right, so the answer 8 stands.
- Q16 - corrected (omission): PDF's list leaves out "numbers starting with 355: 25"; its printed terms add to 1411, not the 1436 it states. With the missing line the total is 1436.
- No question was fully `written`. Source pdf: Q2, Q4, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q17, Q18, Q19, Q20 (notation cleaned only; a few steps made explicit, e.g. Q8 factor 2/62, Q10 term rewriting, Q20 identities).

## Answer key
All 20 keys verified by computation (exact fractions, brute force over strings/permutations/digits, numerical series) and all agree with the PDF. Note: Q13's key reads "6860 or 3"; 6860 is the count with distinguishable fruits (the PDF's own working); "3" is the number of compositions (fruits of a kind treated as identical). The deck gives 6860 and notes this under useful results. The PDF labels no marks.

## Alternates
Given for 19 of 20 questions (all except Q20). Light variants (distinct but modest ideas): Q2 (direct count with weights 1 and 2 instead of the complement), Q11 (choose positions instead of permuting multisets), Q19 (count |C| = 1..3 then remove A- or B-empty cases). Clearly different ideas: Q1 (Re w = |z-1|^2+1 and repeated squaring), Q3 (CRT mod 3 and mod 7), Q4 (sequential match probabilities), Q5 (completing the square in the denominator), Q6 and Q7 (step-deviation), Q8 (equal-size combination formula), Q9 (partitions of 5 into parts at most 3), Q10 (differentiate twice), Q12 (integrate the binomial expansion), Q13 (inclusion-exclusion), Q14 (residues mod 3 with a generating polynomial), Q15 (symmetry: average number), Q16 (base-5 numeral), Q17 (deviations from the mean 9), Q18 (Cauchy-Schwarz, no calculus).
No alternate:
- Q20 - the only route is to absorb 1/(k+1) and 1/(k+2) by raising n and applying Vandermonde; other approaches (integrals, generating functions) reduce to the same convolution or to testing values of n, so no genuinely different method exists.

## Useful Result / Pattern
Given for all 20 questions.

## make_ppt.py warnings
None printed (only the equation count and the save line). No "could not convert" notes.

## Skipped / assumed
- No rendering to images (no soffice); the deck was built without warnings but not viewed.
- Difficulty xlsx formulas not recalculated; index computed by hand.
- Ratings' nearest-anchor column says "JEE Main level; no close Advanced anchor" for every question.
- Printed numbering Q101-Q120 is renumbered 1-20 in the deck.
