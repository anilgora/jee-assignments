# Run report - SHEET_TRIGONOMETRIC_EQUATION_FCopy_JM (Exercise J-M, 16 questions)

**Blueprint:** none was used. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** the sheet prints no marks, so JEE Advanced defaults were used: 4 marks for every question (11 single-correct: Q1, Q2, Q5-Q12, Q14; 5 numerical: Q3, Q4, Q13, Q15, Q16). Stated in the section dividers. Total 64 marks. (These are JEE Main questions; the sheet's real JEE Main marking was not printed, so nothing else was assumed.)

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.25** (no equivalence-relation or multi-correct adjustments apply).
- Levels: Level 1 = 2 (Q11, Q12); Level 2 = 8 (Q1, Q2, Q5, Q6, Q8, Q9, Q10, Q14); Level 3 = 6 (Q3, Q4, Q7, Q13, Q15, Q16); Levels 0, 4, 5 = none.
- Ratings are my judgement against the anchors (JEE Main-origin questions, so lower than Advanced); confidence Medium except Q8, Q11, Q12, Q14 (High).
- Workbook: `SHEET_TRIGONOMETRIC_EQUATION_FCopy_JM_difficulty.xlsx` (recalc.py not available, so cached formula values are absent until opened in Excel).

## Solutions corrected (solution_source = corrected)
- **Q2** - PDF's third line ends "(log sin x)^2 - 4(log sin x)(log cos x) + 4(log cos x)^2 = 1"; it must be "= 0" (the next line, log sin x = 2 log cos x, only follows from 0). Also added that the negative root of sin x is rejected. Answer 4 unchanged.
- **Q4** - typo "cos 3θ/1" in the PDF's second line, should be cos(3θ/2). Working after it is correct. Answer 25 unchanged.
- **Q6** - sign error in "2 sin²θ(sin⁴θ − 1)" (should be 1 − sin⁴θ) and a garbled next line; rewrote those two lines. Factorisation sin²θcos²θ(2sin²θ − 1) = 0 and answer 9 are right.

No question needed `written`.

## Answer key problems
- **Q9: the printed key "A" (= 1) looks WRONG.** The PDF's own solution ends with "sum of solutions = -1", which is option (C). Verified: LHS is identically 4, so x³ − x² + 2 = 0, whose only real root is x = −1 (the other roots are 1 ± i); numeric scan confirms. The deck shows (C) −1. (The printed A = 1 is the Vieta sum of all three roots, probably the source of the slip.)
- All other answers match the key and were verified numerically (Q1 range [-1.5,-1]; Q3 six angles, sum 2; Q4 11 solutions; Q6 nine zeros; Q7 n=13 and AGP sum; Q8 both roots tested; Q10 n=5 (3 roots); Q11 max of LHS 1.98<2; Q12 min 1; Q13 r=4; Q14 root 0.748 and theta<π/4; Q15 min t = 0.8453; Q16 roots 0.386, 1.962).

## Gaps in the PDF filled while keeping solution_source = pdf
- Q3: added the check that tan is defined at the six angles. Q7, Q9: added the intermediate lines (S − S/2 step wording; 4 − sin²2x = 3 + cos²2x cancellation, domain cos2x ≠ 0). Q8: added why the root with 4 + 5 tan < 0 is rejected (PDF only says "rejected"). Q10: PDF only draws a graph; the reason n = 5 (2π + α ≤ 5π/2 < 3π − α) was written out. Q12: stated the bound term by term. Q16: PDF only sketches the graph; kept that as step 7 and gave the rigorous count in the alternate.

## Text-layer problems in the PDF
The extracted text lost most maths symbols; all questions and solutions were read from page images (85 dpi). The PDF also prints each question in Hindi; only the English text was used.

## Alternates and results
- Alternate solutions were written for **all 16** questions (Q1 via cos2x = c giving λ = (cos²2x − 3)/2; Q2 via p = log_cos sin and AM-GM; Q3 via sin(A+B) = 0 and φ = θ + π/4; Q4 via cos X − cos Y = −2 sin sin; Q5 convexity/symmetry of 9^t + 9^(1−t); Q6 via w = cos2θ giving w(w² − 1)/4; Q7 telescoping a_k = (k+2)/2^k; Q8 line-circle geometry; Q9 cos²x = (1+c)/2 giving cos⁶ − sin⁶ = (3c + c³)/4; Q10 sin²+cos² grouping and sign-of-roots test; Q11 monotonicity of e^s − 2e^(−s); Q12 monotone cubic in cos x; Q13 quadratic in sin x with roots 2, (a−4)/2 and sin54° − sin18° = 2cos36° sin18°; Q14 auxiliary angle; Q15 w = cos2θ bi-quadratic; Q16 concavity + IVT).
- **No alternate:** none. Weaker alternates (organisational / change of variable rather than a wholly new idea): Q4 (sine-product factorisation), Q10, Q12, Q15 (w instead of t), Q3 (same equation n = sinθ + cosθ reached via sin(A+B)).
- Every question has useful_results (4-5 bullets).

## make_ppt.py output
No warnings: 721 equations converted to native PowerPoint equations; 111 slides, 16 questions. No rendering check was possible (no PowerPoint/LibreOffice here).

## Skipped / assumed / guessed
- Concepts and chapter names self-assigned (all Trigonometric Equation; second concept added where another chapter is involved).
- All five numerical questions labelled "Numerical Type" (JEE Main numerical format; Q3/Q16/Q15 have single-digit answers but are not printed as 0-9 integer type).
- recalc.py and slide rendering were skipped (not available).
