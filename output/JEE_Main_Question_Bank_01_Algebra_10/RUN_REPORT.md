# Run report: JEE_Main_Question_Bank_01_Algebra_10

Paper: `papers/JEE_Main_Question_Bank_01_Algebra_10.pdf` (printed Q181-Q200, renumbered 1-20). Q1-Q19 Permutations and Combinations; Q20 Permutations + Probability.
Files: `_content.json`, `_Analysis.pptx` (120 slides), `_ratings.json`, `_difficulty.xlsx`.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed): **4 per question** (JEE Advanced default for single-correct and numerical). Q1-Q3 and Q20 are Single Correct, Q4-Q19 Numerical. Stated on the section dividers.

## Difficulty
Marks-weighted difficulty index: **1.60** (equal marks; no equivalence-relation or multi-concept adjustments).
Level 1: 8 questions (Q4, 6, 10, 12, 13, 16, 17, 20). Level 2: 12 (Q1, 2, 3, 5, 7, 8, 9, 11, 14, 15, 18, 19). Levels 0, 3, 4, 5: none.
JEE Main-style bank rated on the Advanced scale, so the index is low. Medium confidence: Q5, 8, 9, 14, 15, 18, 19. Levels were judged against anchors 2021-P2-Q1 (L2), 2021-P2-Q17 (L1), 2026-P1-Q11 (L3), not a full per-question anchor comparison.

## Solutions: corrected / written
No question was `written`. Corrected:
- **Q2 (printed 182):** total written as $^{15+3-1}C_3=136$; $^{17}C_3=680$, the right form is $^{17}C_2$ (= 136). The PDF also switches variable names (t, r for x) in "z = 15 - 2t, r in {0..7}-{5}"; unified to x. Answer 114 unchanged.
- **Q9 (printed 189):** final line adds 5 + 75 + 200 + 900 (= 1180); Case II gives 300 (the PDF shows 300 in its own case), so total 5 + 300 + 200 + 900 = 1405. Answer unchanged.
Reproduced from the PDF (`pdf`) with fill-ins of omitted steps: all others (e.g. reason for the 50-50 parity split in Q4, the 2 <= p < q <= 16 range in Q5, why EA/AE are the only orders in Q20). Q8: the PDF drops higher-order terms (x^18, x^20) without comment; made explicit as harmless. Q17: the answer 432 assumes "without repetition" means no letter appears twice in the word (E counted once); noted in the deck (504 if EE were allowed).

## Answer key
All printed keys match my own computation (brute force in Python for Q1-Q3, Q5, Q6, Q8-Q15, Q17 (under the no-repeated-letter reading), Q18, Q19, Q20; Q4, Q7, Q16 by direct argument). No wrong key. Only caveat: Q17 reading above.

## Alternates and results
Alternates for 18 of 20 questions; all 20 have useful_results. Techniques: Bell number minus one partition (Q1), sorted triples times 3! (Q2), residue classes mod 3 (Q3), roots-of-unity filter f(1),f(-1) (Q4), Euler totient sum (Q5), pattern-first count (Q6), double counting k*C(10,k) (Q7), direct digit pairs (Q8), exponential generating function (Q9), mirror-group sum of squares (Q10), reflection x -> 7-x (Q11), residue patterns (Q12), counting words after it (Q13), complement/inclusion-exclusion (Q14), partitions into parts <= 3 formula (Q15), positions-first count (Q17), four distinct couples C(n,4)*12 (Q18), swap symmetry (Q20).
Weakest alternates (close to the main solution): Q10 (same cases, symmetry shortcut), Q12 (residue patterns vs complement), Q13 (counting after instead of before), Q17 (positions-first, same arithmetic).

## Questions with NO alternate
- **Q16:** the only route is counting intersection points by family (parallel / concurrent / mixed); the complement count 190 - 45 - 44 is the same bookkeeping.
- **Q19:** the inclusion-exclusion with glued blocks is the natural method; direct counting without it is the same count in disguise.

## make_ppt.py warnings
None. Build printed only "605 equations converted to native PowerPoint equations"; no "could not convert" messages.

## Skipped / assumed
No rendering/thumbnail check (no soffice). Concepts, marks and levels assumed as above. Hindi/English duplicate text ignored.
