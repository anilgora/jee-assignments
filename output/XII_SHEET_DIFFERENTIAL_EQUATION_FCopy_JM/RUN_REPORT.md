# Run report - XII_SHEET_DIFFERENTIAL_EQUATION_FCopy_JM (Exercise J-M, 64 questions)

**Blueprint:** none. **Concepts self-assigned (no blueprint) - please review.**
**Marks assumed:** none printed, so JEE Advanced defaults: 4 marks for every question (single-correct: Q1-7, 14-24, 26-42, 48-60; numerical value: Q8-13, 25, 43-47, 61-64). Stated in the section dividers. Total 256 marks. All questions are JEE Main problems.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.27** (145/64; equal marks, no equivalence-relation adjustment, no multi-correct floor). Below the official Advanced range (2.6-3.2), expected for JEE Main questions.
- Level 1 = 5 (Q11, 17, 49, 52, 57); Level 2 = 39; Level 3 = 18 (Q4, 7, 8, 9, 10, 14, 16, 22, 39, 44, 48, 54, 55, 59, 60, 61, 62, 63); Level 4 = 2 (Q46, Q64); Levels 0 and 5 = none. Confidence Medium for most. The DE anchors are mostly L2 Advanced questions, so ratings are loose.
- Workbook: `XII_SHEET_DIFFERENTIAL_EQUATION_FCopy_JM_difficulty.xlsx` (recalc.py unavailable; cached values appear when opened in Excel).

## Solutions corrected / written
No question was `written`. Three are `corrected`:
- **Q9** - PDF takes the domain as the symmetric interval $|x+2|<e^\lambda$ and gets 4, but $x=-2$ is a singular point, so the domain is $(-2,\,3e^{e^{-2/3}}-2)$ and $|\alpha+\beta|=3e^{e^{-2/3}}-4\approx1.013$ (checked numerically). Answer field keeps the official 4; the last solution bullet states the caveat. See answer key.
- **Q19** - PDF treats only upward-opening parabolas; the full family is $121(y'')^2=100$ (not an option). Remark added; (B) unchanged.
- **Q46** - PDF's integrating factor $e^{\tan^{-1}(\tan 2x/\sqrt2)}$ jumps by $\pi$ at $x=\pi/4$, invalid at $x=\pi/3$; misprints $\tan^2x$, $\pi/18$. Used the continuous factor; answer 2 unchanged.
- Silent misprint fixes (source kept `pdf`): Q1 (y=1 for y=-1), Q3 ($1/\sqrt C$), Q4 (sign chart showed $1+\sqrt3$ outside the domain), Q6, Q8, Q15, Q17, Q18, Q24, Q32, Q37, Q43, Q53, Q54, Q64; steps added where the PDF skipped them: Q13, Q20, Q21, Q33, Q59. Q60: Hindi says x<-1, English x>-1; English followed.

## Answer key
- **Q9:** key 4 holds only under the symmetric-interval reading; strictly ≈1.013 (see above).
- **Q62:** question is inconsistent (area from 3 to 3 is 0 yet $(y/3)^3=1$); true area is $(y/x)^3-1$. Official 6 follows from differentiating; kept.
- **Q25:** data inconsistent (the integral relation forces $\varphi(5)=0$ but $\varphi(0)=4$ gives $\varphi(5)=19$); intended answer 4 kept.
- **Q44:** 42 requires one formula $y=\tan x/(1+\tan x)$ on all intervals of S; assumed, stated in the solution. **Q47:** $\alpha=6,\beta=8$ are the intended integers. **Q32:** ODE singular at x=0; the entire-function extension is used (as in the PDF).
- All other keys agree with sympy/numeric checks.

## Alternates and results
- Alternates for **all 64 questions**, each checked against the answer. Several are milder variants (definite integral from the initial point, particular-solution guess, z=ye^x variants): Q2, 5, 11, 12, 13, 50, 51, 56, 58, 60, 63.
- **No question lacks an alternate.** Every question has `useful_results`.
- Caveat: the Q34, Q36, Q41, Q43 alternates were not separately executed by the worker that wrote them (the main solutions and answers were).

## make_ppt.py warnings
- None; build printed only "2795 converted to native PowerPoint equations" and "418 slides, 64 questions". No "could not convert".

## Skipped / assumed
- Only English text read; figures (e.g. Q27) described in words. No visual render check of the deck. Chapter label for all ratings: Differential Equations. Per-question work was drafted by four parallel workers and merged; levels were not re-normalised across chunks beyond a skim.
