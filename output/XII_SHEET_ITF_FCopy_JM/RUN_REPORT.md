# Run report - XII_SHEET_ITF_FCopy_JM (Exercise J-M, 25 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for every question (Q1-17 and Q19-23 single correct; Q18, Q24, Q25 numerical). Stated in the section dividers. Total 100 marks.

## Difficulty
- Marks-weighted difficulty index (adjusted): **1.64** (164/100; no equivalence-relation adjustment, no multi-correct floor since there are no MCQs).
- Levels: Level 1 = 10 (Q2, Q4, Q5, Q7, Q13, Q14, Q15, Q16, Q21, Q23); Level 2 = 14 (Q1, Q3, Q6, Q8, Q9, Q10, Q11, Q12, Q17, Q18, Q19, Q20, Q22, Q24); Level 3 = 1 (Q25); Levels 0, 4, 5 = none. JEE Main questions, so the index is well below the Advanced range. All ratings Medium confidence; nearest anchors are loose (few ITF anchors at levels 1-2).
- Workbook: `XII_SHEET_ITF_FCopy_JM_difficulty.xlsx` (recalc.py not available; cached values appear when opened in Excel).

## Solutions corrected / written
- **Q14 (corrected)** - PDF says "H = sqrt(25) = 25"; the hypotenuse is 5. Fixed; answer (C) unchanged.
- **Q17 (corrected)** - the PDF's inequality list is incomplete (second inequality printed without a left side, sign diagram not tied to factors). Rewritten in full as 2(2x^2-1)/(4x^2-1) >= 0 and x^2/(4x^2-1) >= 0 with their solution sets; answer (D) unchanged.
- **Q21 (corrected)** - first line printed |(x^2 + 4x + 2)/(x^2+3)| <= 1 (wrong sign); the function has x^2 - 4x + 2 (later lines use it). Fixed; answer (B) unchanged.
- **Q22 (corrected)** - line (1) printed as "3cos^2 x = pi + cos^-1 2x"; should be 3cos^-1 x. Fixed, and the PDF's bare claim "all satisfy" now shown with an example check. Answer (A) unchanged.
- **Q25 (corrected)** - PDF has typos: x/(1-x^2) in place of x/sqrt(1-x^2) inside the sin^-1, and "alpha = (k^2-1)/(k^2-2)" where alpha^2 is meant. Fixed (alpha = -beta = +-sqrt(.)). Answer 12 unchanged.
- No question needed `written`.
- Minor remarks, kept as `pdf`: Q10's question stem is incomplete in the paper (noted in the first bullet); Q18 and Q2 skip a line (half-angle value for tan(theta/2), 5-12-13 conversion) which I spelled out; Q7/Q8 etc. reproduced as is.

## Answer key
All 25 keys agree with numerical checks in Python (direct evaluation or scanning; Q8, Q10, Q11 domain/range checked by sampling; Q22, Q24, Q25 verified by substitution). **Q11: the key "Bonus" is correct** - the true domain [-1/2,1) U (2,inf) minus {(3-sqrt5)/2, (3+sqrt5)/2, 3} also excludes x = 3, which option (D) does not. No key is wrong.

## Alternates and results
- Alternates for **Q1, Q2, Q4, Q5, Q6, Q7, Q8, Q10, Q11, Q12, Q13, Q14, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q24, Q25** (21 questions): Q1 lower bound pi/3 (no domain needed); Q2, Q18, Q19 complex-number arguments; Q4 squaring |u|>=1; Q5, Q16 guess-and-induct partial sums; Q6, Q20 test-value elimination; Q7 calculus; Q8 substitution w = 1/(x-1); Q10 alpha = pi/4 + t symmetric form; Q11 cancel then square; Q12 read x^4+x^2 = 6 directly; Q13 exact tan(pi/8); Q14 (1/2)cos(theta - phi); Q17 (4x^2-1)^2 >= 1; Q21 split -D <= N <= D; Q22 t = sin^-1 x (no extraneous roots); Q24 Vieta; Q25 x = sin t substitution plus product-of-roots first.
- **No alternate (genuinely different method not available):** Q3 - plain intersection of two domain conditions, any other route is the same inequalities; Q9 - three branch reductions, any other method restates them; Q15 - direct principal-value reductions, same; Q23 - D+-N >= 0 is already the main method.
- Honest caveat: alternates for Q12, Q13, Q14, Q21, Q24 are mild variants (different technique but short); all verified numerically/symbolically.
- Every question (1-25) has `useful_results`.

## make_ppt.py warnings
- None. Printed only "840 converted to native PowerPoint equations" and "Saved ... (148 slides, 25 questions)". No "could not convert" messages.

## Skipped / assumed / guessed
- Only English text used (Hindi ignored). Concepts and chapter name ("Inverse Trigonometric Functions") self-assigned.
- No visual rendering check (no soffice); layout not inspected.
- Q11 answer shown as "Bonus (...)" since no option is correct.
