# Run report - SHEET_LIMIT_FCopy_JM

Paper: Exercise J-M (Limits), 24 JEE Main questions (Jan 2023 Q1-6, Apr 2023 Q7-11, Jan 2024 Q12-18, Apr 2024 Q19-24), numbered 1-24 as in the PDF. The PDF has answers and solutions (Hindi text ignored). Date of run: 2026-10-14. All 24 final answers were checked numerically (high-precision evaluation of each limit); every answer in the PDF key is correct.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks assumed (none printed; stated in the section dividers): JEE Advanced defaults, 4 marks for every question (single-correct Q1-16 and Q19-21; numerical Q17, 18, 22, 23, 24). Total 96. Questions with options A-D are single-correct, those without options are numerical.

## Difficulty
Marks-weighted difficulty index (adjusted): **2.29** (these are JEE Main questions; no expected distribution, below the official Advanced range 2.6-3.2).
Level counts: L0 = 0, L1 = 1 (Q9), L2 = 15 (Q1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 14, 16, 20, 21, 22), L3 = 8 (Q4, 10, 15, 17, 18, 19, 23, 24), L4 = 0, L5 = 0.
No equivalence-relation adjustment and no MCQ floor applied. Medium-confidence ratings: Q2, 4, 6, 8, 10, 12, 15, 17, 18, 19, 23, 24.

## Solutions whose solution_source is "corrected" (5)
- Q3: the PDF's second/third lines print the surds as sqrt(2n^4+3n+1)-sqrt(n^4+n+3) (and 3n-1) instead of the question's 2n^4+4n+3 and n^4+5n+4. Limit unaffected; rewritten with the correct polynomials and conjugate difference n^4-n-1.
- Q4: the PDF misprints the constant (q^2+82+16 for q^2+8q+16), never uses 4+2p+q=0 to show the cosine's argument is exactly (x-2p)^2, and writes [f]=0 after "using L'Hospital" without showing f stays below 1/2 (which decides the floor). Added both steps; answer 0 unchanged.
- Q18: in the right-hand limit the PDF's derivative step is garbled (extra factor 2 in the denominator, radical inverted: sqrt(2-x^2) instead of 2/sqrt(2-x^2)). Both tend to sqrt(2); corrected derivative shown, R = pi/sqrt2 and answer 18 unchanged.
- Q19: the PDF's numerator sum is sum_{r=1}^{n-1}((r-1)^2-(r-1))(n-r), an index shift in the first factor only (true terms are (k^2-k)(n-k)); the polynomial it lists is not that of the question. Its leading term n^4/12 coincides, so the answer 1/3 is right. Rewritten with the correct general term.
- Q23: right setup but wrong constants: the PDF writes the limit as 2(1/a+4/(sqrt17+1))^2(4/(sqrt17-1))^2 (factor should be 32: 16*2 sin^2(u/2)), evaluates it to 68/(9-sqrt17) (which is really 17(9+sqrt17)/16) and then states 17(9+sqrt17). Final value 17(9+sqrt17)=223.09 and answer 170 are right; the working was corrected.

## Solutions with solution_source "written" (0)
None; the PDF has a solution for every question. Small additions inside "pdf" solutions: Q1 (n^{1/sin^2 t} factor written in full notation), Q2 (the endpoints -7.5 and -6.5 are excluded because the one-sided values are 8 and 6; PDF only argued -7.5), Q16 (parity checks for each pre-image), Q12 (the PDF's last rationalisation line is cut off in print; completed), Q20 (typo 3c+12 in the PDF read as 3c+2), Q15 (explicit "tends to 1 from above").

## Answer key / question problems
No answer key is wrong. (PDF typo noted: Q24 prints "(1+sin)^{(1/2)cot x}" without the argument x; read as (1+sin x).)

## Alternates and results
Alternates given for 22 of 24 questions (all except Q8 and Q9). useful_results given for all 24.
Questions with NO alternate:
- Q8: the only argument is a squeeze with every factor in (0,1); using the smallest/largest factor (PDF) or the uniform bound sqrt2-1 are the same idea, so no genuinely different method.
- Q9: pure standard-limit/equivalent-infinitesimal evaluation; Taylor/L'Hospital are just heavier restatements, so no genuinely different elegant method.
Borderline alternates (different technique but same underlying Taylor information): Q11, Q13, Q17 give the derivative / repeated-L'Hospital form (N''(0), N'''(0)) of the series method in the main solution. Q15's alternate is a model-function check (valid only because the MCQ has a unique answer; stated in the slide).

## make_ppt.py warnings
First build printed three "could not convert" notes (Q3, Q10, Q19 answer strings) because the answer strings were not raw strings and \f / \a were turned into control characters. Cause fixed in the generator (raw strings); rebuilt with no notes or warnings. 1036 equations converted to native equations; 157 slides.

## Skipped / assumed / guessed
- Rendering/thumbnail checks were skipped (no soffice/mnt skills); the deck was not visually inspected, only built without warnings.
- Concepts, chapter name ("Limit"), question types and marks are my own assignment (no blueprint).
- Question texts were transcribed from page images; Q24's "(1+sin x)^{(1/2)cot x}" and Q1's printed prefactor were read from slightly small print.
