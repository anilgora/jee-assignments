# RUN REPORT - SHEET_P_&_C_FCopy_JM (Permutations & Combinations, Exercise J-M, 58 questions)

**Blueprint:** none was available. Concepts self-assigned (no blueprint) - please review.
Marks assumed (none printed in the paper): Single Correct 4, Numerical 4 (JEE Advanced defaults, as instructed). Q4 has no options in the PDF, so it is treated as Numerical. Stated in the section dividers. Total 232 marks; every question is 4 marks, so the weighted index equals the mean level.

## Difficulty
- Marks-weighted difficulty index (adjusted = unadjusted; no equivalence-relation or multi-concept adjustment applies): **1.81**
- Levels: L1 x20 (Q1-6, 12, 15-18, 24, 26, 28-30, 34, 41, 42, 49); L2 x30 (Q7-11, 13, 14, 19-23, 25, 27, 31-33, 36, 37, 40, 43, 44, 47, 48, 50, 51, 53, 55-57); L3 x7 (Q38, 39, 45, 46, 52, 54, 58); L4 x1 (Q35); L0 and L5 none.
- This is a JEE Main chapter sheet, so the index sits well below the official Advanced range (2.6-3.2); it is reported as it is. Only one P&C Advanced anchor group exists (2021-P2-Q1 L2, 2024-P1-Q11 L4, 2025-P1-Q10 L5, 2026-P1-Q11 L3), so confidence is Medium on several casework questions.

## Solutions that are corrected or written
- Q9 (corrected): the PDF's list of prefixes (7, 5, 37, 357, 3537, 3535, 35337) omits the prefix 355 (25 numbers) and so sums to 1411, yet prints 1436. Added 355; numbers above 35337 are 1250+125+50+10 = 1435, rank 1436. Answer unchanged.
- Q14 (corrected): the working gives 840 x 60 = 50400 but the answer line prints 504000 (extra zero). Correct answer 50400.
- Q35 (corrected): the PDF's block method (abc or cba glued: 7C1 x 2 x 6!/(2!2!2!) = 1260) counts a number once per A.P. triple it contains. Correct count of numbers with at least one A.P. triple is 944 (inclusion-exclusion S1 - S2 + S3 = 1260 - 360 + 44; exactly one / two / three triples: 672 / 228 / 44). Brute force over all 1680 strings agrees.
- Q52 (corrected): the PDF working ends at 8C1 x 4C2 = 48, contradicting its own key B (16). Choosing a first vertex counts every triangle 3 times, so the answer is 48/3 = 16.
- No question was "written" from scratch.
- Clarifications that keep source "pdf": Q3 (the TOH block of 2 words, lost in the PDF text, restored from the stated total); Q4 (statement and working were garbled in the text layer; read from the page image: 2n+1Pn-1 : 2n-1Pn = 11:21); Q10 (digit 7 lost in the sum "2+4+5+6+8"; it is 2+4+5+6+7+8 = 32); Q42 (the PDF jumps from 8C(m+2) > 8C3 to m = 2; added the one-line justification that 8Cr > 56 only for r = 4); Q45 (cases regrouped to say which (xA, xB, xC) each product belongs to); Q47 and Q58 (small clarifications of the counts).

## Answer key
Every answer was checked by brute force (itertools / sympy). The PDF's key is wrong for:
- Q14: printed 504000, correct 50400.
- Q35: printed 1260, correct 944 (if constant triples such as aaa were also counted as "A.P." the count would be 1208; 1260 is wrong under either reading).
- Q52: working gives 48, key B = 16 is right.
Other points: Q7 is read as ordered pairs (x, y) (120; unordered would be 60). Q8's key prints "6860 or 3"; 6860 is correct (the "or 3" looks like a stray). Q29 follows the key 432 (no letter used twice); if EE were allowed the count would be 504 - the wording "without repetition" supports 432. All other answers agree with the key: Q1 B, Q2 A, Q3 A, Q4 45, Q5 60, Q6 546, Q8 6860, Q9 1436, Q10 32, Q11 21, Q12 240, Q13 2997, Q15 105, Q16 81, Q17 C, Q18 B, Q19 D, Q20 B, Q21 A, Q22 B, Q23 C, Q24 D, Q25 B, Q26 B, Q27 A, Q28 171, Q30 31, Q31 16, Q32 4898, Q33 26664, Q34 44, Q36 413, Q37 16, Q38 72, Q39 B, Q40 B, Q41 C, Q42 A, Q43 C, Q44 553, Q45 11376, Q46 3734, Q47 169, Q48 101, Q49 A, Q50 B, Q51 B, Q53 D, Q54 C, Q55 5626, Q56 125, Q57 36, Q58 70.

## Alternates and results
- Alternate solutions were produced for 52 of 58 questions (Q4 and Q17 have a modest alternate: ratio matching / polynomial division; Q52 has two). Each was checked numerically against the answer.
- Questions with NO alternate (no genuinely different method; any other route is a reworded copy of the main one):
  - Q5: two independent multiset arrangements; the only variants are binomial rewrites of the same product.
  - Q32: inclusion-exclusion over two glued strings is the only short route.
  - Q35: any other route is a long hand enumeration of avoiding-strings (736); no elegant alternative.
  - Q50: block counting then reading the second word of the O-block; from-the-end counting is a mirror image.
  - Q51: ordered partition into labelled sets is a multinomial; sequential choice or word-arrangement is the same formula.
  - Q55: only the case sum over a (the mirror symmetry is given in the results slide).
- Weakest alternates (genuine but close in spirit): Q7 (fix x, count y), Q17 (polynomial division), Q25 (slice by first digit), Q37 (list the 16 multiples), Q41 (inclusion-exclusion vs shift), Q49 (direct count vs complement).
- Every question (1..58) has a useful_results slide.

## make_ppt.py output
- "Q2, Q30, Q41, Q49: only 3 solution bullets" - harmless; the PDF's solutions for these are only 3 steps long and are reproduced in full.
- No "could not convert" warnings. 1359 equations converted to native PowerPoint equations; 312 slides.

## Skipped / assumed / guessed
- No rendering or thumbnail check was done (no soffice); the deck was not viewed visually.
- Concepts, section marking and question types are assumptions (no blueprint, no printed marks); the PDF's blank-line gaps (no questions numbered 17, 20, 50 missing) were not an issue - all 58 printed questions 1..58 are present.
- Difficulty levels follow the calibrated rubric but use few P&C anchors; L1-L2 for Main-style counting questions is a judgement.
- Q35's S3 = 44 was obtained by enumeration, not by hand; S1 and S2 are shown by hand.
