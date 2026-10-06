# RUN REPORT - JEE_Main_Question_Bank_01_Integral_Calculus_02

Paper: 20 questions (printed Q21-Q40, numbered 1-20 in the deck), all Definite Integration, all single correct.

## Blueprint
No blueprint was used. **Concepts self-assigned (no blueprint) - please review.**
Marks: none printed, so JEE Advanced defaults were used: 4 marks for every Single Correct question (Q1-Q20). Stated in the section divider.

## Difficulty
- Marks-weighted difficulty index (adjusted): **2.40** (all questions 4 marks).
- Level 2: 12 (Q2, Q3, Q6, Q9, Q11, Q12, Q14, Q16, Q17, Q18, Q19, Q20). Level 3: 8 (Q1, Q4, Q5, Q7, Q8, Q10, Q13, Q15). Levels 0, 1, 4, 5: none.
- No equivalence-relation questions and no multi-concept one-or-more-correct questions, so no adjustment or floor applies.
- The anchors disagree on the plain king-property question: rubric.md text lists 2026-P2-Q4 as L1, anchors.md/csv give it L3. I followed the anchors file (L3) for king-property questions with an extra stage. Confidences are mostly Medium.

## Solutions that are `corrected` or `written` (no `written`)
- Q4 (PDF Q24): the line after $\tan x=t$ drops the factor $8\pi$ ($I=\int dt/(t^2+2^2)$) and has a stray "U ="; factor restored. Answer $2\pi^2$ right.
- Q8 (PDF Q28): the first line after the substitution is labelled $I_2$ but is $I_1$; relabelled. Answer 4 right.
- Q12 (PDF Q32): substitution written $x=\sin2\theta$; must be $x=\sin^2\theta$. Answer right.
- Q16 (PDF Q36): half-finished duplicate line for $f(4)$, and $\alpha=f(1)$ taken without comparing with $f(5)$; comparison added ($f(5)=125/4>f(1)=29/4$). Answer 157 right.
- Q19 (PDF Q39): the PDF skips the second L'Hopital step and its third-derivative numerator has the wrong sign on the sine term (correct: $-e^x\cos(1-e^x)-e^{2x}\sin(1-e^x)$). Value $-1/6$ unaffected.
- All other solutions are as printed (`pdf`); small additions where the PDF is terse: Q1 (the identity $1/(1+5^{-x})=5^x/(5^x+1)$), Q3 (the evaluation of the four pieces, which the PDF skips), Q7 (the substitution finish, which the PDF leaves unfinished), Q13 (the by-parts evaluation behind "on solving"), Q18 (check of the other options). Typos with no effect on the working (Q17 "x^2/22", Q2 "I-3 ln sqrt3") were fixed silently.

## Answer key problems
None. All 20 keys agree with my checks: every definite integral and limit was recomputed numerically with mpmath; Q26, Q28, Q34, Q35 (deck Q6, Q8, Q14, Q15) were verified symbolically/by hand and Q15 by an explicit cubic F.

## Alternates and results
- Alternate solutions given for **18 of 20 questions** (one each): Q1-Q10, Q12-Q15, Q17-Q20 (all numbered as in the deck). All were verified by hand and by the numerical checks above.
- Questions with NO alternate:
  - Q11: the only route is the king property $t\to6-t$ after $\ln x=t$; the geometric "point symmetry about $(3,\frac12)$" view is the same idea reworded.
  - Q16: the only route is the sign of $f'$ and endpoint values; no genuinely different method.
- Modest alternates (valid but close in spirit to the main route): Q10 (parts in $x$ rather than $t$), Q14 ($u=x^3$ instead of the chain rule), Q18 and Q1 (odd/even split versus the king trick), Q13 (same).
- Useful Result / Pattern given for **all 20 questions**.

## make_ppt.py output
- "Equations: 833 converted to native PowerPoint equations." 122 slides, 20 questions. No warnings and no "could not convert" notes.

## Skipped / assumed / guessed
- The deck was not rendered (no soffice step per run rules); slide fit was not checked visually.
- Levels and chapter names are my own ratings from the calibrated rubric; nearest anchors are approximate.
- The PDF text layer is garbled for maths; every page was read from images.
- Q3: the stem prints $\gcd(p,q,r)=1$; with $p=5,q=2,r=3$ it holds.
