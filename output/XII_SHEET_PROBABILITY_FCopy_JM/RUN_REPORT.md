# Run report - XII_SHEET_PROBABILITY_FCopy_JM (Exercise J-M, 45 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for every question (38 single-correct: Q1-Q8, Q10-Q15, Q18-Q29, Q33-Q44; 7 numerical: Q9, Q16, Q17, Q30, Q31, Q32, Q45). Stated in the section dividers. Total 180 marks. Q18 prints "n is equal to ___" but also gives options and key "C", so it is treated as single-correct.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.93** (no equivalence-relation or multi-correct adjustments; no MCQ in the sheet).
- Level 1 = 10 (Q1, Q5, Q9, Q10, Q11, Q13, Q15, Q20, Q25, Q41); Level 2 = 28 (Q2, Q3, Q6, Q7, Q8, Q12, Q14, Q16, Q17, Q18, Q19, Q21, Q22, Q23, Q24, Q26, Q33-Q40, Q42-Q45); Level 3 = 7 (Q4, Q27-Q32); Levels 0, 4, 5 = none.
- JEE Main-origin questions, so the index is well below the Advanced range (2.6-3.2). Confidence Low for Q28, Q29, Q31 (idea availability); Medium for most; High for the one-step questions.
- Q29 (symmetric and transitive relations) did NOT get the equivalence-relation +0.5: the question never asks about equivalence relations or classes. Say if you want the adjustment applied (Q29 would become 3.5).
- Workbook: `XII_SHEET_PROBABILITY_FCopy_JM_difficulty.xlsx` (recalc.py not available, so cached formula values are absent until opened in Excel).

## Solutions corrected (solution_source = corrected) - 6 questions
- **Q11** - the PDF's numerator series is printed as (5/6)^5 + (5/6)^5 (1/6) + ...; the X = 5 term is (5/6)^4 (1/6). Rewritten; answer 25/36 unchanged.
- **Q19** - PDF writes 33C16 in the denominator of P(X=16)/P(X=17) where P(X=17) has 33C17; equal values, so 1320 unchanged.
- **Q21** - option (B) is printed P(E1' n E2') = P(E1')P(E2) but the PDF evaluates the right side with P(E2') (15/24); with the printed P(E2) it is 5/24. Verdict (false) and answer (C) unchanged.
- **Q31** - the PDF says "divisible by 21 when divided by 3" and lists the three cases without explaining why divisibility by 7 is automatic (N = 111111 + 7M, and 111111 = 3.7.11.13.37) or why only k = 0, 3, 6 eights work (digit sum 6 + 7k). Argument added; count 22 and answer 33 unchanged.
- **Q32** - the PDF's per-size counts are 2, 9, 4, 1 (sum 16, not 19). For n(A) = 7 the missing index can be any of E1..E7, which is 7 ways, not 4; 2 + 9 + 7 + 1 = 19. The final answer 19 was right, one intermediate number wrong.
- **Q36** - PDF's second line reads 0 <= (2-3P)/8 <= 1 although P(E2) = (2-p)/8 (the interval it quotes, [-6, 2], is the correct one for (2-p)/8). Typo fixed; answer 5/3 unchanged.

No question needed `written`.

## Answer key problems
None. All 45 keys were verified by hand and by computation (brute force or exact arithmetic for Q1, Q4, Q5, Q8, Q14, Q22, Q24, Q26, Q27, Q28, Q30, Q31, Q32, Q34, Q37, Q38, Q43, Q45). Q8's key is printed "(3)", read as the third option, i.e. (C) 5.

## Gaps in the PDF filled while keeping solution_source = pdf
Q2: added that the integer count is for (-16, 3) intersected with [-5, 30]. Q6: derived the arithmetico-geometric sum (the PDF only quotes the result). Q8: added the check that n = 4 fails (needed for "smallest"). Q10: added the check that both roots satisfy 2p <= 1. Q12: filled the algebra between the PDF's equation and x = 1/8. Q27: replaced the PDF's bare table of six solutions by a systematic casework on f(b). Q29: added why (x, y) in R forces all four pairs. Q43: stated why only 337 and 1685 add to the multiples of 2 or 3. Q4, Q40, Q41, Q44, Q45: small explanations added.

## Text-layer problems in the PDF
Maths symbols, inequality signs and several fractions were garbled in the text layer; ambiguous items (Q3, Q4, Q11, Q12, Q15, Q18, Q19, Q20, Q21, Q32, Q33, Q35, Q36, Q40, Q41, Q42) were checked against page images. Hindi duplicates were ignored. Q23's option exponents (6^5, 5^4, 5^5, 6^4) were read from the garbled text (275/65, 36/54, 181/55, 46/64) and are not image-verified; the answer (D) 46/6^4 is the only one equal to 276/6^5.

## Alternates and results
- Alternate solutions were written for **30 of 45** questions: Q1 symmetry; Q2 vertex form; Q3 outcome-multiplicity count; Q4 proportional rows by ratio r; Q5 binomial view; Q6 tail-sum formula; Q7 modulo 3; Q8 binomial symmetry; Q10 xor-bias identity; Q11 memorylessness; Q13 heads vs tails (Bin(6,1/2)); Q14 uniform ordered pair; Q15 handshake count; Q17 complement for P(fail); Q18 odds form of Bayes; Q19 ratio recurrence; Q21 conditional form of option (C); Q22 binary representation of 48; Q25 ratio recurrence; Q26 conditioning on the first digit; Q27 sum of used values; Q28 count (b,c) for each (a,d); Q29 equivalence relation on a subset; Q30 generating polynomial; Q32 complement and distinct partitions; Q38 periodicity of 35; Q41 ratio already given; Q42 four-cell table; Q43 Euler totient; Q45 hypergeometric variance formula.
- Weaker alternates (a different organisation rather than a wholly new idea): Q2 (vertex form of the discriminant test), Q17 (complement for the denominator), Q25 (ratio recurrence), Q30 (generating polynomial is the same case sum), Q42 (four-cell table).
- **No alternate (15 questions), no genuinely different method exists:** Q9 (only the inequality 2^n >= 10); Q12 (any route is the same sum of six pair products, reduces to 1/6 - 2x^2); Q16 and Q20 (restrict to the conditioning set and renormalise; no other idea); Q23 (solve P(4H) = P(5H) then add three binomial terms; the 'tails' version is the same terms); Q24 (the choose-one-from-each-gap count is the only route); Q31 (the decomposition 111111 + 7M is already the main method); Q33 and Q39 (mean/variance system then binomial terms); Q34 (counting along beta instead of alpha is only a cross-check, noted in the results slide); Q35 (the PDF already uses the Venn-region method); Q36 (interval intersection only); Q37 (direct sum; the failures-version is the same terms); Q40 (linearity is the same as np); Q44 (the posterior-weights form is the PDF's own computation).
- Every question (all 45) has useful_results (3 bullets each).

## make_ppt.py output
No warnings and no "could not convert" notes: 1346 equations converted to native PowerPoint equations; 253 slides, 45 questions. No rendering check was possible (no PowerPoint/LibreOffice here).

## Skipped / assumed / guessed
- Concepts and chapter names self-assigned (Probability for every question; second concept from another chapter where one is involved).
- Q18 treated as single-correct (options present); Q8 key "(3)" read as option (C).
- Ratings are my judgement against the anchors; no anchor is a close match for most items, so the "nearest anchor" strings are approximate.
- recalc.py and slide rendering were skipped (not available).
