# Run report - XII_SHEET_LIMIT_FCopy_JM (Exercise J-M, 22 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for every question (Q1, Q4-Q14, Q17-Q21 single correct; Q2, Q3, Q15, Q16, Q22 numerical). Stated in the section dividers. Total 88 marks.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.14** (188/88; no equivalence-relation adjustment, no multi-correct floor since there are no MCQs).
- Levels: Level 1 = 2 (Q10, Q14); Level 2 = 15 (Q1, Q2, Q4, Q5, Q6, Q7, Q8, Q9, Q11, Q13, Q16, Q17, Q18, Q20, Q21); Level 3 = 5 (Q3, Q12, Q15, Q19, Q22); Levels 0, 4, 5 = none. JEE Main questions, so below the Advanced range. All ratings Medium confidence; few Limit anchors exist.
- Workbook: `XII_SHEET_LIMIT_FCopy_JM_difficulty.xlsx` (recalc.py not available; cached values appear when opened in Excel).

## Solutions corrected / written
- **Q3 (corrected)** - PDF prints the expansions with sign slips (ln(1+x) as x + x^2/2 + x^3/3; -gamma x^2(1+x+...) instead of +gamma x^2(1-x+...)) and 'beta - 6' for 'beta = 6'. The three coefficient equations it then uses are right. Expansion line fixed; answer 3 unchanged.
- **Q4 (corrected)** - PDF uses x for both the variable and the summation index (garbled factorisation, 'hx+2'). Rewritten with index n; factorisation (nx+2)((n+1)x+2), telescoping and answer 9/44 unchanged.
- **Q12 (corrected)** - PDF labels the [x]=6 side as R.H.L. and the [x]=7 side as L.H.L. (swapped); cross-multiplication step written out. Equation and answer a = -6 unchanged.
- **Q13 (corrected)** - PDF's last lines have 'tan(cot^-2 2)' and an inconsistent factor 6; rewritten cleanly. Answer 3 unchanged.
- **Q22 (corrected)** - PDF's combined-fraction algebra is garbled and not verifiable (a line such as 12 - 3(4)+8x1-8+3cos2-3cos2 does not follow). Rewritten with g(y) = y^3+2y^2+3 sin y via the same 1^inf + L'Hopital route. Answer 1 is right.
- No question needed `written`.
- Minor remarks kept as `pdf`: Q8's PDF is terse about beta = e^0 = 1; Q6's PDF only says 'a != -1' - the reason (limit becomes infinite) is added in the bullet; Q16 PDF skips the check of the limit value -2, added as a bullet; Q21 PDF does not test the options, verdicts for (A)-(D) added.

## Answer key
All 22 keys agree with numerical checks (mpmath at tiny offsets / direct evaluation; Q12 with a = -6 gives both one-sided limits 1; Q13 partial sums and closed form n/(2n+5) checked; Q15, Q16, Q21, Q22 verified by substitution). **No key is wrong.**

## Alternates and results
- Alternates for **all Q1-Q22** (22 questions): Q1 a^8-b^8 factorisation; Q2 series for cos x sqrt(cos 2x); Q3 derivative test N'''(0)/6; Q4 plug x = 2 into each term; Q5 F''(beta)/2 (double zero); Q6 x = 1/t, derivative; Q7 order-of-vanishing; Q8 tan identity + ln(beta); Q9 F'(1) of the radical difference; Q10 theta = arccos x; Q11 mean value theorem; Q12 reduce to function of n = [x]; Q13 guess-and-induct on tan S_n; Q14 order of zero via derivatives; Q15 integer bounding of 1/alpha; Q16 double-root factorisation (x-1)^2(2x+c); Q17 conjugate; Q18 a^7-u^7 over a^2-u^2; Q19 particular + homogeneous solution; Q20 Bernoulli expansion of 1/(e^t-1); Q21 odd/even (cosh, sinh); Q22 H'(0) of the log.
- **No alternate:** none omitted.
- Honest caveat: alternates for Q3, Q7, Q9, Q14, Q15 are milder variants (different technique but close in spirit to the main solution); all verified symbolically or numerically.
- Every question (1-22) has `useful_results`.

## make_ppt.py warnings
- None. Printed only "790 converted to native PowerPoint equations" and "Saved ... (142 slides, 22 questions)". No "could not convert" messages.

## Skipped / assumed / guessed
- Only English text used (Hindi ignored). Concepts and chapter name ("Limit") self-assigned.
- No visual rendering check (no soffice); layout not inspected.
- Q16's printed stem has no pi inside the sine (the page image shows sin(3x^2-4x+1)); read as printed, answer 11 confirmed numerically.
- Year/session tags from the paper are appended to each question stem.
