# Run report - JEE_Main_Question_Bank_02_Differential_Calculus_01_03

Paper: `papers/JEE_Main_Question_Bank_02_Differential_Calculus_01_03.pdf` (20 single-correct questions, 16 pages, Matrix JEE Academy; solutions printed in the PDF). The PDF prints them as Q41-Q60; the deck numbers them 1-20 (deck n = printed n+40).
Files: `_Analysis.pptx` (122 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.**
- No marks printed. Assumed: single-correct 4 marks each, no negative marking; total 80. Stated in the section divider.

## Difficulty
- **Marks-weighted difficulty index (adjusted): 1.95** (80 marks; unadjusted 1.85) - a JEE Main-level bank, well below the Advanced range (2.6-3.2).
- Levels before adjustment: Level 1: 4 (Q3, Q7, Q12, Q17); Level 2: 15 (Q1, Q2, Q4, Q5, Q6, Q8, Q9, Q10, Q11, Q13, Q14, Q15, Q16, Q18, Q20); Level 3: 1 (Q19); Levels 0, 4, 5: none.
- Adjusted: Q10, Q14, Q16, Q19 get +0.5 (equivalence-relation / relation-property questions, treated as in the previous two banks) -> 2.5, 2.5, 2.5, 3.5. No multi-correct floor (no MCQs).
- Q19 rated with Low confidence (two relations, an inequality-reversal trap, anchors point in different directions); the rest Medium/High. Nearest anchors are by topic only; no close Main-level anchors exist.
- `_difficulty.xlsx` built with `build_report.py`; recalc skipped (no /mnt/skills), formulas fill in on opening in Excel.

## Solutions whose source is corrected (one line each)
- Q1 (printed 41): PDF writes -1 <= x^2+1/3 <= 2 and x^2 <= 5/3 (bracket <= 1 needs the argument < 2, strict) and dismisses x^2 = pi without reason; fixed (strict bound, x^2 <= 1 < pi). Key C right.
- Q2 (printed 42): PDF's LHL line drops the tan term's limit pi and prints a stray "/pi"; rewritten. Key C right.
- Q3 (printed 43): PDF has a "x -> 10" typo and skips showing the x cancels with the denominator; added u-substitution. Key B right.
- Q4 (printed 44): PDF names the composite "f(x)", uses x>1 for the last piece and ends "not derivable at x = 1" (it is derivable at 1; fails at 0); fixed. Key B right.
- Q5 (printed 45): PDF's "g(S) != S therefore f(g(S)) != f(S)" is an invalid inference and f(g(S)) is never computed; computed all sets explicitly. Key B right.
- Q6 (printed 46): PDF just labels both parts "differentiable" with no check at 0 (sin|x| and |x| are each non-differentiable there; corners cancel); added one-sided derivatives. Key A right.
- Q9 (printed 49): PDF's first line has cos(pi/6 - h) instead of cos(pi/6 + h); fixed and identities written out. Key B right.
- Q13 (printed 53): PDF's "g'(c)=f'(c)=-f'(c)" assumes a fixed sign of f on each side and proves only necessity of f'(c)=0; replaced by the sign-of-(x-c) argument giving both directions. Key B right.
- Q16 (printed 56): PDF writes "... != (a,b)R(e,f)" without showing that transitivity actually fails; added the counterexample (1,2),(2,1),(1,2). Key A right.
- Q18 (printed 58): PDF mixes x and h (sinh/x) and evaluates factors loosely; rewritten consistently in h. Key A right.
- Q19 (printed 59): PDF turns a/b > -2 into "b/a < -1/2" (wrong in general) and never shows T is transitive (needed to reject options A and C); replaced by an explicit counterexample for S and the transitivity proof for T. Key B right.

## Solutions whose source is written
- None.

## Solutions kept as pdf (reproduced, small expansions only)
- Q7, Q8, Q10, Q11, Q12, Q14, Q15, Q17, Q20. Where the PDF skipped an obvious line (ranges of brackets in Q8, the x -> 1/x substitution in Q17, the algebra in Q12, "onto => bijection" in Q15, domain remark in Q11) the line was added without changing the PDF's method.

## Answer key
- No answer key looks wrong; all 20 keys (C,C,B,B,B,A,D,C,B,B,C,D,B,A,A,A,A,A,B,D) were re-derived. Numerical/brute-force checks run for Q1 (dense scan of [-1,1]: 0 solutions), Q2 (one-sided values 4.1416 / 3.1416), Q3 (sympy limit 1), Q4 (one-sided slopes at 0 and 1), Q6 (one-sided slopes 0), Q9 (sympy 4/3), Q10 (all subsets of a 3-set), Q11, Q14 (closure adds 7), Q15 (brute force for n=8, 9), Q16, Q18, Q19 (counterexamples), Q20.

## Alternates
- Given for 16 of 20: Q1, Q3, Q4, Q5, Q6, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q16, Q17, Q18, Q19. All verified (numerically or symbolically) to reach the same answer. Q8's (determinant criterion) and Q18's (squeeze) alternates are modest variations of technique rather than wholly new ideas.
- **No alternate (no genuinely different method), one line each:**
  - Q2: the only way to evaluate is to split at 0 and read [x]; series/L'Hopital versions repeat the same one-sided steps.
  - Q7: the bounds are the single inclusion-exclusion inequality pair; testing options is the same bounds.
  - Q15: placing five restricted points into six allowed values and permuting the rest is the only counting route (sequential-choice or probability phrasing is the same product).
  - Q20: h(t) is the constant -1 on both sides; combining the two sides in one line is a rewording, not a new method.
- Useful results: **all 20 questions have `useful_results`** (formulas checked on a numerical case where numeric).

## make_ppt.py warnings
- None. 746 equations converted to native equations; no "could not convert" notes, no solution-source warnings.

## Skipped / assumed
- Rendering/thumbnails were not done (no soffice); the deck was not opened in PowerPoint.
- Level ratings are my own judgement against the anchors (Main-level bank, few close anchors).
- The Hindi text in the PDF (legacy font) was not transcribed; only English statements used. All maths was read from page images (text layer garbled).
- Marks, negative marking and the +0.5 treatment of Q10, Q14, Q16, Q19 (relation-property questions) are assumptions. Concepts self-assigned; chapter names for Q7/Q12 ("Sets") have no anchor-chapter equivalent.
