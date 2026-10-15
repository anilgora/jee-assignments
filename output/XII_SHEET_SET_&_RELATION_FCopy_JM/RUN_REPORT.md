# RUN REPORT - XII_SHEET_SET_&_RELATION_FCopy_JM

Paper: 34 questions (AIEEE / JEE Main), chapter Sets & Relations. 12 are numerical-answer, 22 are single correct.

## Difficulty
- Marks-weighted difficulty index (adjusted levels): **2.15** (all questions 4 marks, 136 marks in all).
- Adjusted levels: L1 x7, L1.5 x4, L2 x8, L2.5 x7, L3 x5, L3.5 x1, L4 x2.
- Equivalence-relation +0.5 applied to Q4, 6, 7, 8, 13, 14, 16, 18, 24, 25, 28, 29. No multi-correct questions, so the 2.5 floor was never used.
- Low-confidence rating: Q15 (the Venn diagrams).
- Chapter sheet of JEE Main questions: far below the 2.6-3.2 range of official Advanced papers, as expected.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed in the paper): +4 for single correct and for numerical questions (JEE Advanced default). This is stated in every section divider. There are no negative-marking lines.

## Solutions: corrected or written (PDF was wrong or missing)
- Q1 corrected: PDF gave no counter-example for transitivity and its reflexive line lost its symbols. Answer (B) unchanged.
- Q2 corrected: PDF put the reason for "not symmetric" under "reflexive" and never checked symmetry. Answer (A) unchanged.
- Q5 written: PDF has one line, "only possible when B = C". Element-chase proof written.
- Q6 corrected: symmetric step garbled with no counter-example; transitivity of S skipped the p = 0 case. Answer (C) unchanged.
- Q7 corrected: symmetric check for B garbled; explicit pair (0,1) added. Answer (A) unchanged.
- Q8 written: PDF stops at "Reflexive;". Full solution written.
- Q10 corrected: typos "n(B) = 8" (should be n(AxB) = 8) and "2^8 = 250" (should be 256).
- Q12 corrected: PDF is a sketch (no k-ranges, no sum of C, no disjointness argument). Answer 5 unchanged.
- Q14 corrected: PDF's symmetric step needs P = P^-1 and its transitive step reuses the same P for both relations. Correct argument uses Q = P^-1 and QP. Answer (B) unchanged.
- Q15 written: PDF is one sentence. Reasoning from the figure written.
- Q17 corrected: Case II line lost the sign (the equation is -(x+3)(x+4) = 6); garbled roots in Case I. Answer (A) unchanged.
- Q19 corrected: typo "n + 1000" for "n + 10000". Answer 832 unchanged.
- Q20 corrected: PDF stops at c >= 87; upper bound c <= 89 and the conclusion added.
- Q21 written: PDF is one sentence about option (C) only. All four options now checked.
- Q23 corrected: typo "A - B = (1,1)" should be (-1,1).
- Q24 corrected: PDF says (10,23) is in R2; it is not (|10-23| = 13).
- Q27 corrected: PDF counts 14 primes and 36/28; correct counts are 15 primes, n(R1) = 38, n(R2) = 30. The difference 8 is the same.
- Q33 written: PDF only asserts that every element of T except 11 is representable; proof written.

All other questions have solution_source = pdf (Q3, 4, 9, 11, 13, 16, 18, 22, 25, 26, 28, 29, 30, 31, 32, 34). Their working is reproduced with notation cleaned into LaTeX, and checks fill a few PDF omissions without changing any step.

## Answer key
Every PDF answer was confirmed. Numerical answers (Q12, 19, 22, 26, 27, 31, 32, 33, 34) were checked by brute force in Python. The relation and set questions were checked by hand. No answer key looks wrong.

## Alternates and useful results
- Alternate solutions given for 30 of 34 questions, each a different method (Boolean matrix, kernel of a function, indicator functions, binomial sum, complement versus direct count, periodicity, Apery set, group action and so on).
- **No alternate** (no genuinely different method exists):
  - Q3: only one kind of counter-example (a word bridging two disjoint words) exists.
  - Q15: the Venn reading of the triple region is the only route.
  - Q16: the class of (4,3) is counted in one natural way ((4k,3k), k <= 7).
  - Q30: counting distinct odd semiprimes up to 60 has one natural route.
- Every question (1-34) has useful_results.

## make_ppt.py warnings
- Only one note: "could not convert $|{\rm domain}|\times|S|$ - left as LaTeX text". Cause: the \rm command in Q30's useful result. Fixed by rewording the text; the rebuild printed no warnings (1140 equations converted, 209 slides).

## Skipped, assumed or guessed
- Q15 depends on reading the three figures: P has two small circles inside a big one, Q and R have the overlap of two circles inside the third. All three show a triple region, matching the key (C).
- Rendering/thumbnails were not checked (no soffice step here); equation conversion succeeded for all but the one snippet above.
- Question numbering follows the paper 1-34. No Hindi text is carried into the deck.
- The title slide uses "Sets & Relations - Paper Analysis"; no AIR marks slide (none supplied).
