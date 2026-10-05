# Run report: JEE_Main_Question_Bank_01_Algebra_13

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_13.pdf` (printed Q241-Q260, renumbered 1-20). Q1-15 Probability (Q1 also determinants, Q3/Q9/Q12/Q14 touch algebra), Q16-20 Binomial Theorem / counting.
Files: `_content.json`, `_Analysis.pptx` (117 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question** for every type present: single correct (Q1-3, Q16-20) and numerical-answer (Q4-15) = JEE Advanced defaults. Stated on the section dividers. Q4-15 have integer answers; labelled Numerical Type (not Integer 0-9, since answers exceed 9).

## Difficulty
Marks-weighted difficulty index: **2.10** (equal marks; no equivalence-relation or multi-concept adjustments).
Level 1: 3 (Q1, Q11, Q18). Level 2: 13 (Q2, 3, 7, 8, 10, 12, 13, 14, 15, 16, 17, 19, 20). Level 3: 3 (Q5, Q6, Q9). Level 4: 1 (Q4). Levels 0 and 5: none.
JEE Main-style bank rated on the Advanced scale, so the index is below the official range. Medium confidence on many (anchors are loose matches).

## Solutions: corrected / written
No question was `written`. Corrected (all small typos/slips; answers unchanged):
- **Q4 (printed 244):** PDF writes a = -9k for r = 4/3; should be a = 9k. Count of 28 verified by brute force.
- **Q5 (245):** PDF's first line sums P(W_i) up to 190; there are 5! = 120 words (the following working already uses 120).
- **Q6 (246):** Bayes expression has 52Cn in the denominator of the second term; it is 51Cn (the PDF's next line assumes they cancel).
- **Q11 (251):** the PDF's yellow-ball table is headed 0,1,3,4; the entries correspond to Y = 1,2,3 (values and sum 112 are right).
- **Q12 (252):** PDF states "a, b, c are different", which is not in the question and contradicts its own list (e.g. (1,2,1)); removed.
- **Q17 (257):** PDF's second derivative has exponent 98 where 48 is meant.
Reproduced from the PDF (`pdf`): Q1, 2, 3, 7, 8, 9, 10, 13, 14, 15, 16, 18, 19, 20 (with small fill-ins: Q2 makes the S2 counterexample explicit as the complement of a point; Q7's printed "39p" is 3^9 p, as the page image shows).
Q9: the answer 5 rests on rejecting alpha = 0 because X = 0 is already a value in the table; stated in the solution.

## Answer key
All printed keys match my own computation (Python exact arithmetic / brute force for every question). No wrong key.

## Alternates and results
Alternates for 17 of 20 questions (Q1-6, 8, 10-19); all 20 have useful_results. Techniques: elimination without determinants (Q1), finite two-point counterexample (Q2), centring x = 33+t (Q3), parametrisation (kq^2, kpq, kp^2) with sum of phi(p)*floor(40/p^2) (Q4), factorial number system for rank (Q5), lost card equally likely among unseen cards (Q6), hypergeometric variance formula (Q8, Q10), linearity of expectation (Q11), count from (a,c) side (Q12), memoryless property (Q13), complement with geometric tail (Q14), first-step equation (Q15), subset-containing-a-fixed-element argument (Q16), coefficients from the binomial theorem (Q17), direct count with at least one even (Q18), solution count a+b+c=4 (Q19).
Weaker alternates (close to the main solution): Q12 (same enumeration from the other variable), Q16 (only the Pascal step is re-explained; the cube sum is the same), Q5 (only the rank step differs; the G.P. step is the same).

## Questions with NO alternate
- **Q7:** every route (generating function, random walk, ratio of binomial terms) reduces to adding the same three binomial terms; no genuinely different method.
- **Q9:** the only other route is re-parametrising by mu instead of alpha, which is the same algebra; no genuinely different method.
- **Q20:** any approach uses the two consecutive-coefficient ratio equations; the alternatives are the same equations rearranged.
All three still have useful_results.

## make_ppt.py warnings
None. Build printed only "696 equations converted to native PowerPoint equations"; no "could not convert" messages.

## Skipped / assumed
No rendering/thumbnail check (no soffice). Concepts, marks and levels assumed as above. Hindi/English duplicate text ignored. Page images were read for Q1, 2, 3, 4, 5/6, 8, 9, 10, 11-15 working where the text layer was garbled; remaining working was verified by computation.
