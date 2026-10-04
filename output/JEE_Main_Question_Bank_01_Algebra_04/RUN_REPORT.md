# Run report: JEE_Main_Question_Bank_01_Algebra_04

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_04.pdf` (printed Q61-Q80, renumbered 1-20; all Sequence and Series: A.P., G.P., A.M./G.M.).
Files: `_content.json`, `_Analysis.pptx` (127 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question** - Q1-8 single correct, Q9-20 numerical (JEE Advanced defaults); stated on the section dividers.

## Difficulty
Marks-weighted difficulty index: **1.95** (no equivalence-relation or multi-correct adjustments).
Level 1: 4 questions (Q4, 7, 10, 11). Level 2: 13 questions (Q1, 2, 3, 5, 8, 9, 12, 13, 16, 17, 18, 19, 20). Level 3: 3 questions (Q6, 14, 15). Levels 0, 4, 5: none.
JEE Main-style bank rated on the Advanced scale, so the index is low.

## Solutions: corrected / written
No question was `written` (the PDF has a solution for all 20). Corrected (answers unchanged):
- **Q1 (printed 61):** PDF's first line says "= 1012" (factor m^2 n missing); restated as "= 1012 m^2 n". Also noted the second coprime split (m,n) = (1, 2023), which the PDF ignores.
- **Q15 (printed 75):** PDF multiplies/divides by negative quantities (m^5(1-m), m^6(1-m), 1-m) without reversing the inequality (writes a(1-m) > m^5(1-m) then "a > m^5"); the two missing reversals cancel, so a > m^5 and a < m^6/2 are right. Rewritten with the reversals; m = 1 excluded explicitly.
Reproduced from the PDF (`pdf`) with small fill-ins of omitted steps: Q3 (why a = 11), Q6 (a_1 check), Q9 (steps from a^2r^3 to r), Q11 (even n excluded), Q14 (why the common terms end in 6), Q16, Q17 (determinant expansion).

## Answer key
Printed keys for three numerical questions are letters, not values, so the key is wrong/unusable: **Q9 (printed 69) "C", Q14 (printed 74) "C", Q18 (printed 78) "C"**. The PDF's own working gives 3, 3 and 3 and I verified these by computation (Q9: 2/3+1+3/2+9/4 = 65/12 and reciprocals 65/18; Q14 common terms 16, 256, 4096; Q18: a=1/8, b=1/12). All other keys agree with my own checks (brute force for Q1, 2, 3, 4, 6, 8, 12, 14, 15, 20).

## Alternates and results
All 20 questions have one alternate solution and all 20 have useful_results. Techniques: closed form by induction (Q1), hockey stick (Q2, Q6), divisor argument on S*T (Q3), covariance (Q4), Lagrange multipliers (Q5), binomial sum (Q6), Q7 mean-of-AP, special-case numerical test (Q8), symmetric parametrisation (Q9), midpoint-square area (Q10), unit-digit period (Q11), completing the square (Q12), ratio parametrisation (Q13), gcd(2^j-1, 2^4-1) (Q14), terms t6, t7 directly (Q15), numeric check plus monotonicity (Q16), row operation (Q17), reciprocal substitution (Q18), index-sum rule (Q19), Vieta on power sums (Q20).
No question lacks an alternate. Weakest (closest to the main solution or more of a check): Q7, Q10, Q13, Q16 (direct evaluation plus monotonicity), Q17, Q18.

## make_ppt.py warnings
None (788 equations converted natively; no "could not convert" notes).

## Skipped / assumed
No rendering/thumbnail check was possible (no soffice step). Concepts and marks are assumed as above. Level ratings were made by judgement against the anchors (anchors.md has few progression questions, so the same few anchors are cited), not by a full anchor comparison per question.
