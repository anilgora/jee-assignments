# RUN REPORT – JEE_Main_Question_Bank_01_Differential_Calculus_01 (Sets and Relations, Q1–Q20)

**Blueprint:** none. Concepts self-assigned (no blueprint) - please review.
**Marks assumed:** none printed; 4 marks each (JEE Advanced default for single-correct), stated in the section divider. All 20 questions are single-correct (Q6 and Q11 are statement-based single-correct). PDF numbers 1–20 = deck numbers.

## Difficulty
Marks-weighted difficulty index (adjusted, equivalence-relation +0.5 on Q9–Q13 and Q19): **1.80** (unadjusted 1.65).
Base levels: L1 = 8 (Q4, 8, 11, 12, 14, 16, 17, 18); L2 = 11 (Q1, 3, 5, 6, 7, 9, 10, 13, 15, 19, 20); L3 = 1 (Q2). Adjusted levels: 1 ×6, 1.5 ×2, 2 ×7, 2.5 ×4, 3 ×1. Confidence Medium (JEE Main-style questions on the Advanced scale; anchors only indicative).

## Solutions corrected / written
- Q1 corrected: first line of the PDF solution says $|\alpha-1|\le5$; the question has $\le4$ (which gives −3≤α≤5). Fixed; answer unchanged.
- Q2 corrected: PDF concludes k = 6 ("k maximum when k = 6") and uses a₁+1 ∈ {2,…,101} ignoring a_{k+1}+1 ≥ 2, yet its own sequence has 5 pairs and the key is 5. Correct bound: a₁+1 = 2^k(a_{k+1}+1) ≥ 2^{k+1} ⇒ k ≤ 5.
- Q3 corrected: PDF's list of R has every pair written as (y,x) instead of (x,y) (e.g. (−3,3) is not in R). Count 15, m = 3 and answer D unaffected.
- Q19 corrected: PDF's transitivity counter-example uses (6,8) ∈ A×B, but 8 ∉ B. Replaced by (2,1)R(2,4), (2,4)R(3,1), (2,1) not R (3,1); verified by brute force.
- Q20 corrected: PDF's counter-example uses sets of ordered pairs as subsets of S = {1,…,10}, whose elements are numbers. Replaced by {1,2},{2,3},{3,4}.
- Bridging lines added without changing the PDF's method (source "pdf"): Q4 (reverses listed), Q5 (reflexive/symmetric justification), Q6 (S₂ steps), Q9 (impossible sizes), Q10 (reasoning for each added pair), Q13 (tan identity for symmetry; PDF's "(A)+(2)" read as (1)+(2)).
- No question needed "written".

## Answer key
All 20 PDF answers verified by brute force / computation and agree with the key: 1 A, 2 A, 3 D, 4 A, 5 C, 6 C, 7 D, 8 C, 9 D, 10 B, 11 A, 12 B, 13 A, 14 C, 15 A, 16 C, 17 B, 18 B, 19 C, 20 A. (Q2's key A = 5 is right; only the PDF's working was inconsistent.)

## Alternates and Useful Results
- Alternates given for 18 questions: Q1–Q13, Q15–Q19.
- NO alternate: Q14 (the range is a geometric progression summed by a/(1−r); the only other route, T = 1 + (2/5)T, is the same series reworded) and Q20 (checking reflexive/symmetric/transitive with the empty set and an overlap counter-example is the only route; elimination of options is the same checks).
- Useful Result / Pattern given for all 20 questions.
- Alternates only partly different (same ingredients, different packaging) - flagged for review: Q4 and Q5 (use n = |R|−|R∩Rᵀ|, m = |A|−|R∩Δ| instead of listing), Q9 (partition viewpoint of the same count), Q15 (complement 'strict domination' view of the same counter-examples), Q18.

## make_ppt.py warnings
None printed (708 equations converted, 121 slides, 20 questions); no "could not convert" notes.

## Skipped / assumed
- Slides not rendered or visually inspected (no soffice step here); recalc of the Excel skipped (no /mnt/skills).
- Q17: interval [100,700] read as integers (601 of them).
- Concepts and levels self-assigned. Hindi text of the PDF omitted (English statement used).
