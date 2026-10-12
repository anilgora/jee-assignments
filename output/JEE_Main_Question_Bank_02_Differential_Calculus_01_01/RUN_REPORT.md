# Run report - JEE_Main_Question_Bank_02_Differential_Calculus_01_01

Paper: `papers/JEE_Main_Question_Bank_02_Differential_Calculus_01_01.pdf` (20 single-correct questions, 15 pages, Matrix JEE Academy; solutions printed in the PDF; Q9 has an answer key only).
Files: `_Analysis.pptx` (114 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.**
- The PDF prints no marks. Assumed: single-correct 4 marks each (run instruction), no negative marking assumed; total 80 marks. Stated in the section divider.
- All 20 questions are single correct (the paper heading), numbered 1-20 as printed.

## Difficulty
- **Marks-weighted difficulty index (adjusted): 2.08** (80 marks). This is a JEE Main-level bank, so it sits well below the Advanced range (2.6-3.2).
- Levels before adjustment: Level 1: 3 (Q1, Q17, Q18); Level 2: 13 (Q2, Q3, Q4, Q5, Q6, Q7, Q9, Q11, Q12, Q13, Q16, Q19, Q20); Level 3: 4 (Q8, Q10, Q14, Q15); Levels 0, 4, 5: none.
- Adjusted: Q6 gets +0.5 (equivalence-relation / relation-property question) -> 2.5. No multi-correct floor applies (no MCQs).
- Low-confidence ratings: none (Medium on most, High on Q1, Q18).
- `_difficulty.xlsx` built with `build_report.py`; recalc skipped (no /mnt/skills), so formula values appear when opened in Excel.

## Solutions whose source is corrected (one line each)
- Q6: PDF proves only "not reflexive" and then wrongly says R is symmetric (ignores 2a != b); (2,1) in R but (1,2) not. Transitivity never checked; added (1,3),(3,2) in R but (1,2) not. Key D is right.
- Q8: PDF typo "f(4)=4+(1)", no counterexample for (A), (B) checked only for n=1,2,3; completed by induction f(n)=n f(1), a counterexample (g = ceil(n/2)), and f onto => f(1)=1. Key A is right.
- Q14: PDF typo "82" for 8q, the perfect-square step (q+4=-2p) is not stated, and the floor step (f -> 1/2 from below so [f]=0) is skipped. Added. Key B is right.
- Q15: PDF writes the first branch as |x|>=2 (should be <=2) and reads the non-differentiable points off a sketch; added the slope comparison at 0, +-1, +-2. Key C is right.
- Q16: PDF rewrites the denominator as sqrt(2n^4+3n+1)-sqrt(n^4+n+3) (paper has 4n+3 and 5n+4); lower-order terms do not change the limit. Key B is right.
- Q17: PDF prefactor "1/n^{sin^2 t}" should be n^{cosec^2 t}; notation fixed. Key D is right.

## Solutions whose source is written
- Q9: PDF gives only the answer (C); full solution written (fog(n) = ceil(n/2); onto, not one-one), checked numerically for n = 1..12.

## Answer key
- No answer key looks wrong; all 20 keys (A,C,D,D,D,D,A,A,C,B,A,B,D,B,C,B,D,A,D,B) were re-derived and agree. Numerical checks run for Q3, 5, 6, 9, 10 (small analogue), 11, 12, 13, 14, 16, 17, 18, 19, 20.
- Q18: the printed limit point is x -> -alpha*beta (= 2); checked on the page image.

## Alternates
- Given for 13 of 20: Q2, Q3, Q4, Q7, Q9, Q11, Q13, Q14, Q15, Q16, Q17, Q18, Q19. All verified (numerically or symbolically) to reach the same answer.
- **No alternate (no genuinely different method), one line each:**
  - Q1: the only route is double counting of incidences; any other phrasing is the same equation.
  - Q5: the count factorises as 6 x 6; per-element counting is just the same enumeration.
  - Q6: each property fails by a counterexample; any other approach repeats the same counterexamples.
  - Q8: each statement is settled by f(n)=n f(1) plus standard composition facts; alternatives are rewordings.
  - Q10: g is forced on Range(f) and free elsewhere; that is the whole solution.
  - Q12: equating one-sided limits is the only route (the "equidistant from 0 and 1" reading is a rewording).
  - Q20: solving f(x)=2^x and the GP sum is the only sensible route; matching powers of 2 is the same equation.
- Useful results: **all 20 questions have `useful_results`** (formulas checked on a numerical case).

## make_ppt.py warnings
- None. 681 equations converted to native equations; no "could not convert" notes, no solution-source warnings.

## Skipped / assumed
- Thumbnails / rendering were not done (no soffice); the deck was not opened in PowerPoint.
- Level ratings are my own judgement against the anchors; this is a Main-level bank so no Advanced anchor matches closely (nearest anchors cited in the ratings are by topic and noted accordingly).
- The Hindi text in the PDF (legacy font) was not transcribed; only the English statements are used.
