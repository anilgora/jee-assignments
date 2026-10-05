# Run report: JEE_Main_Question_Bank_01_Algebra_11

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_11.pdf` (printed Q201-Q220, renumbered 1-20). All 20 questions are Probability, all Single Correct.
Files: `_content.json`, `_Analysis.pptx` (120 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question** (JEE Advanced default for single-correct). Stated on the section divider. Question type assumed Single Correct for all (four options each).

## Difficulty
Marks-weighted difficulty index: **1.70** (equal marks; no equivalence-relation or multi-concept adjustments).
Level 1: 6 questions (Q5, 6, 8, 12, 14, 17). Level 2: 14 questions (Q1, 2, 3, 4, 7, 9, 10, 11, 13, 15, 16, 18, 19, 20). Levels 0, 3, 4, 5: none.
JEE Main-style bank rated on the Advanced scale, so the index is low. Medium confidence: Q2, 4, 13, 18, 20. Levels were judged against a few anchors (2021-P2-Q17 L1, 2021-P2-Q1 L2, 2024-P1-Q2 L3, 2023-P2-Q2 L3), not a full per-question anchor comparison.

## Solutions: corrected / written
No question was `written`. Corrected:
- **Q11 (printed 211):** the PDF's table for sum = 5 lists the pair (3,2) twice; the last row must be (4,1) with weight 1/6 x 1/6. The total 9/36 and the answer are unchanged.
- **Q20 (printed 220):** the PDF states a = 1/12, b = 1/3. b = 1/3 is wrong (it breaks 4a+6b=1); correct is b = 1/9. The PDF's later 24a+280b - (46/9)^2 = 566/81 is right only for b = 1/9, so the answer is unchanged. The missing intermediate 24a+280b = 298/9 was added.
Reproduced from the PDF (`pdf`), with small fill-ins of omitted steps: all others (e.g. De Morgan step in Q7 and Q10, P(X=2) value and sum-to-1 check in Q3, the explicit list of HT outcomes in Q9). Q15: the answer takes "randomly chosen natural number" to mean k mod 4 is uniform on {0,1,2,3}; stated in the deck.

## Answer key
All printed keys match my own computation (exact fractions in Python for every question; Q6, Q18 and Q20 also checked by substitution). No wrong key.

## Alternates and results
Alternates for all 20 questions; all 20 have useful_results. Techniques: pooled-ball counting (Q1), negative-binomial reading (Q2), hypergeometric variance formula (Q3), choose the excluded 4 instead (Q4), natural frequencies (Q5), E[X(X-2)]=0 (Q6), four-region table (Q7), exchangeability (Q8), indicator variables (Q9), Vieta on the roots (Q10), generating polynomials (Q11), degree count per square (Q12), win-odds ratio per round (Q13), independent products (Q14), fix k2 and use i^(k1-k2)=-1 (Q15), indicator covariance (Q16), pooled-ball counting (Q17), expected white count (Q18), difference of independent Bernoullis (Q19), rescale X to X/2 (Q20).
Weakest alternates (close to the main solution): Q7 (region table is the same set algebra), Q20 (rescaling is the same computation with smaller numbers), Q17 (same idea as Q1's alternate).

## Questions with NO alternate
None.

## make_ppt.py warnings
None. Build printed only "552 equations converted to native PowerPoint equations"; no "could not convert" messages.

## Skipped / assumed
No rendering/thumbnail check (no soffice). Concepts, marks and levels assumed as above. Hindi/English duplicate text ignored. The question stem of Q20 (a table in the PDF) is written as a line of values in the deck.
