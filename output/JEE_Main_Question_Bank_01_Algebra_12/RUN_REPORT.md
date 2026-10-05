# Run report: JEE_Main_Question_Bank_01_Algebra_12

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_12.pdf` (printed Q221-Q240, renumbered 1-20). All 20 questions are Probability (Q1, Q2, Q5 also touch quadratics/AM-GM), all Single Correct.
Files: `_content.json`, `_Analysis.pptx` (111 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question** (JEE Advanced default for single-correct; all questions are single-correct with four options). Stated on the section divider.

## Difficulty
Marks-weighted difficulty index: **1.60** (equal marks; no equivalence-relation or multi-concept adjustments).
Level 1: 9 questions (Q3, 4, 6, 7, 8, 9, 10, 12, 14). Level 2: 10 questions (Q1, 2, 5, 11, 15, 16, 17, 18, 19, 20). Level 3: 1 question (Q13). Levels 0, 4, 5: none.
JEE Main-style bank rated on the Advanced scale, so the index is low. Medium confidence: Q1, Q2, Q5, Q13. Levels judged against a few anchors (2021-P2-Q17 L1, 2021-P2-Q1 L2, 2023-P2-Q2 L3), not a full per-question anchor comparison.

## Solutions: corrected / written
No question was `written`. Corrected:
- **Q1 (printed 221):** the PDF's line for b=6 is garbled ("3b = 4ac"); it should be 36 = 4ac, so ac = 9, a = c = 3. Count (8) and answer unchanged.
- **Q5 (printed 225):** the PDF writes ab > 108 but lists (18,6), whose product is exactly 108, and counts 13 cases. "Not less than" means ab >= 108 (with ">" the count would be 11). Sign corrected; count 13/23 and answer unchanged.
Reproduced from the PDF (`pdf`) with small fill-ins of omitted values/steps: all others. Q13: the PDF assumes the five possible compositions (2-6 white) are equally likely a priori; this convention is stated explicitly in the deck (a binomial prior would give 3/8, not an option).
Q19: dividing by q and by 1-p discards the degenerate root p = 1; noted in the solution.

## Answer key
All printed keys match my own computation (exact fractions in Python for every question). No wrong key.

## Alternates and results
Alternates for 18 of 20 questions; all 20 have useful_results. Techniques: square-free parts (Q1), count by (a,c) with 6 - floor(2 sqrt(ac)) (Q2), natural frequencies (Q3), complement by number of addresses (Q4), a = 12 + t substitution (Q5), pooled coins (Q6), symmetry of orderings (Q7), sequential conditional probabilities (Q8), disjoint-union listing (Q9), stars and bars (Q10), hypergeometric variance formula (Q11), equally likely 3-faced die (Q12), Vandermonde-type identity (Q13), ratio-monotonicity plus direct sum count (Q15), independent variances (Q17), tail-sum formula (Q18), s = sqrt(n) substitution (Q19), expected number of leading white balls (Q20).
Weaker alternates (close to main solution): Q6 (same pooling idea used in other banks), Q8 (sequential product vs combination ratios), Q15 (partly a justification of the main step), Q19 (reparametrisation of the same algebra).

## Questions with NO alternate
- **Q14:** the only routes (Venn regions, P(A) - P(A and B), a population of 35 people) are the same subtraction in different words; no genuinely different method.
- **Q16:** n = 16 via C(n,7) = C(n,9) and the probability C(16,2)/2^16 can only be reached by the same binomial formula (factorial form or symmetry are the same step); no genuinely different method.
Both still have useful_results.

## make_ppt.py warnings
None. Build printed only "645 equations converted to native PowerPoint equations"; no "could not convert" messages.

## Skipped / assumed
No rendering/thumbnail check (no soffice). Concepts, marks and levels assumed as above. Hindi/English duplicate text ignored. The PDF text layer is partly garbled in the working (symbols), so the working was reconstructed from the text and verified by computation rather than from page images.
