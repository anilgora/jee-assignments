# Run report - JEE_Main_Question_Bank_02_Differential_Calculus_01_02

Paper: `papers/JEE_Main_Question_Bank_02_Differential_Calculus_01_02.pdf` (20 single-correct questions, 15 pages, Matrix JEE Academy; solutions printed in the PDF). The PDF prints them as Q21-Q40 (continuing from the previous bank); the deck numbers them 1-20 (deck n = printed n+20).
Files: `_Analysis.pptx` (114 slides), `_content.json`, `_ratings.json`, `_difficulty.xlsx`, this report.

## Blueprint and marks
- **Concepts self-assigned (no blueprint) - please review.**
- No marks printed. Assumed: single-correct 4 marks each, no negative marking; total 80. Stated in the section divider.

## Difficulty
- **Marks-weighted difficulty index (adjusted): 1.95** (80 marks) - a JEE Main-level bank, well below the Advanced range (2.6-3.2).
- Levels before adjustment: Level 1: 6 (Q2, Q7, Q8, Q11, Q15, Q16); Level 2: 10 (Q1, Q3, Q4, Q5, Q6, Q9, Q12, Q14, Q19, Q20); Level 3: 4 (Q10, Q13, Q17, Q18); Levels 0, 4, 5: none.
- Adjusted: Q14 and Q18 get +0.5 (relation-property questions, treated as equivalence-relation questions as in the previous bank) -> 2.5 and 3.5. No multi-correct floor (no MCQs).
- No Low-confidence ratings (Medium on most, High on Q2, Q7, Q8, Q11, Q15, Q16). Nearest anchors are by topic only; no close Main-level anchors exist.
- `_difficulty.xlsx` built with `build_report.py`; recalc skipped (no /mnt/skills), formulas fill in on opening in Excel.

## Solutions whose source is corrected (one line each)
- Q3 (printed 23): PDF only says "from graph, 3 ND points"; added the crossing points x=±1/sqrt2, x=0 and the slope comparison. Key D right.
- Q5 (printed 25): PDF gives branch formulas and a sketch but never the branch ranges or union; added them. Key C right.
- Q9 (printed 29): PDF's "a=1 or x^2+(a+1)x-a != 0" is a wrong statement (the quadratic cannot vanish identically, so a=1 is forced); reworded. Key A right.
- Q10 (printed 30): PDF asserts "limit does not exist at -7.5" without reason and silently drops -6.5; added both end-point checks (left value 8 at -7.5, right value 6 at -6.5) and the point -7. Key A right.
- Q17 (printed 37): PDF jumps to "x^2=1" with no argument it is the only root; added the monotonic argument and root checks. Key C right.
- Q18 (printed 38): PDF writes a^2+c^2 = 9+2*sqrt(36) (that would be rational; correct is 9+2*sqrt3) and mislabels the steps (aR1c for bR1c, aR1b/bR2b etc. for the R2 steps); fixed. Key C right.

## Solutions whose source is written
- None.

## Answer key
- No answer key looks wrong; all 20 keys (D,D,D,C,C,C,B,B,A,A,C,A,A,B,A,B,C,C,C,D) were re-derived. Numerical checks run for Q1, Q3, Q4 (recurrence to n=2100), Q5 (range scan, all four "excluded" values attained), Q6, Q7, Q9, Q10 (limit scan), Q16, Q17 (root scan on [-1,1]), Q19, Q20.

## Alternates
- Given for 15 of 20: Q1, Q2, Q4, Q5, Q6, Q7, Q9, Q10, Q11, Q12, Q13, Q15, Q17, Q18, Q19. All verified (numerically or symbolically) to reach the same answer.
- **No alternate (no genuinely different method), one line each:**
  - Q3: a max of two curves has corners only at the crossings and the active branch's own corner; every route is the same graph reading.
  - Q8: the common domain is just the intersection with the two denominator exclusions; nothing else to try.
  - Q14: each property fails by a single counterexample; difference-set or d=a-b restatements use the same counterexamples.
  - Q16: the one-sided substitution x=-h is the whole solution; the x/|x|=-1 rewrite is the same step.
  - Q20: the kinks of the nested modulus are read off directly; the chain-rule view is the same argument.
- Useful results: **all 20 questions have `useful_results`** (formulas checked on a numerical case where numeric).

## make_ppt.py warnings
- None. 694 equations converted to native equations; no "could not convert" notes, no solution-source warnings.

## Skipped / assumed
- Rendering/thumbnails were not done (no soffice); the deck was not opened in PowerPoint.
- Level ratings are my own judgement against the anchors (Main-level bank, few close anchors).
- The Hindi text in the PDF (legacy font) was not transcribed; only English statements used. Maths was read from page images wherever the text layer garbled it (all of it).
- Marks, negative marking and the +0.5 treatment of Q18 (transitivity only, not a full equivalence-relation question) are assumptions.
