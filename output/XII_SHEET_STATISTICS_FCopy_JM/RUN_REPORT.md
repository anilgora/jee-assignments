# Run report - XII_SHEET_STATISTICS_FCopy_JM (Exercise III, JEE Main, 72 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for every question (47 single-correct, 25 numerical; the exact ranges are in the section dividers). Stated in the section dividers. Total 288 marks. (The questions are JEE Main questions, which actually carry +4/-1 and +4/0.)

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.88** (no equivalence-relation or multi-correct adjustments apply).
- Levels: Level 1 = 15 (Q1, Q2, Q5, Q6, Q8, Q9, Q15-Q19, Q21, Q24, Q40, Q54); Level 2 = 51; Level 3 = 6 (Q29, Q38, Q41, Q62, Q65, Q70); Levels 0, 4, 5 = none. JEE Main practice sheet, so far below the Advanced range (2.6-3.2).
- Medium confidence: Q7, Q29, Q36, Q38, Q41, Q62, Q65, Q70.
- Workbook: `XII_SHEET_STATISTICS_FCopy_JM_difficulty.xlsx` (recalc.py not available, cached formula values absent until opened in Excel).

## Solutions that were corrected or written
- **Q4 (written)** - the PDF has no solution (blank "Sol."). Written: (a) true, (b) true, (c) false (variance depends on scale); answer (C) matches the key.
- **Q48 (corrected)** - the PDF's first relation is printed `2a + 8b = 16`; from `32+8a+9b = 48+6a+6b` it is `2a + 3b = 16`. The rest of its working (`14a - 11b = 48`, a=5, b=2, new mean 17/3) is right.
- **Q49 (corrected)** - the PDF's equation (1) is `18a + 37b = 1018`; expanding the mean condition gives `81a + 37b = 1018` (digits transposed). a=8, b=10 satisfy the latter, answer 4 right. The key line says "D" for this numerical question; the answer is 4.
- **Q50 (corrected)** - the median formula is cut off after "x 4" and the next line omits the class width; with width 10, 40 + (128 - a)/30 x 10 = 45 gives a = 113 (the printed form would not). a=113, b=277, answer 164 right.
- **Q62 (corrected)** - the PDF writes the variance as (2a^2 - a + 1)/5 (true value (2a^2 - 86a + 1206)/5) and argues with the discriminant sqrt(40N - 7), which does not prove the claim (40N - 7 = 1 mod 8 can be a square). Replaced by the mod-5 residue check (2a^2 - a + 1 = 0 mod 5 has no solution). Answer 0 is right.

## Answer key
No answer key is wrong. Q49 shows "D" for a numerical question (answer 4; see above). Q1-Q72 final answers were checked by exact arithmetic/brute force for every numerical computation (verify script run: 63 explicit checks, remaining ones checked by hand: Q13, Q16, Q29, Q34, Q43, Q46, Q61).

## Gaps in the PDF filled while keeping solution_source = pdf
- Q22: PDF's p = 1/2 case (gives q = 0, excluded by q != 0) is not mentioned; added.
- Q3, Q5, Q6, Q11, Q12, Q13, Q14, Q18, Q20, Q26-Q28, Q31, Q32, Q36, Q37, Q40-Q42, Q44-Q47, Q51-Q56, Q58-Q61, Q63-Q72: only notation/step layout rewritten into LaTeX, missing small steps (sums of squares, intermediate arithmetic) written out. Q32: the PDF's x-values 5, 15, 25 are class marks shifted by 10; stated explicitly. Q57 and Q58: PDF solution reproduced with the arithmetic completed.
- Q4 and Q5, Q6 have only 3 bullets each (the PDF's working is that short); make_ppt.py notes this and it is harmless.

## Alternates and results
- Alternate solutions (a different technique) for **56 of 72** questions; all verified numerically.
- **No alternate (16)** - no genuinely different method exists:
  - Q4: three concept checks, one-line facts; Q5: mean 0 means every deviation is |a|, one line; Q6: single empirical formula.
  - Q15, Q17: effect of a shift on mean/s.d., a one-line property.
  - Q21, Q24, Q30, Q35: sums about a point; the only route is "variance is origin-free", which is the main solution.
  - Q22: only the linear map conditions; Q39: same idea as Q5 (mean b, s.d. |a|).
  - Q40: only "change of total", the same as the main solution; Q54: the closed form or its expansion are the same computation.
  - Q58: after finding a, b = 3, 4 the mean deviation is direct; Q67: ratio mean/variance and a binomial sum, no second route; Q70: the other routes (exact AGP, numerical bound) are the same computation.
- **Every one of the 72 questions has useful_results** (2-3 bullets each).

## make_ppt.py output
No warnings. Two harmless notes: Q5 and Q6 have only 3 solution bullets (the PDF's working is 3 lines). 1498 equations converted to native PowerPoint equations; 351 slides; nothing stayed as LaTeX text. No rendering check was possible (no PowerPoint/LibreOffice step here).

## Text-layer problems in the PDF
The text layer lost Greek letters and many minus signs. The text of Q5, Q22, Q36, Q48-Q50, Q55-Q57, Q62-Q63 was checked against page images. Hindi duplicates were ignored.

## Skipped / assumed / guessed
- Concepts and chapter names (all Statistics, plus Probability for Q57, Q67, Q72) self-assigned from each question's content.
- Q30's options are not readable in the text layer; read as 3/5, 4/5, 9/10, 7/10 (the key C = 9/10 matches the computed answer).
- Q49 and Q50 stems show "equal to" without options; treated as numerical.
- Q55's symbols were read as mu (girls' mean) and sigma^2 (variance of the 50), checked against the page image.
